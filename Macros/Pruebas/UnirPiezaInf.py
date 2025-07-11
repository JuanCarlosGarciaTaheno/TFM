# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 14, 2025 at 11:04:47
# 
# Macro Name = UnirPiezaInf
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D
from apex import EntityCollection
from collections import defaultdict

apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N-K''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = True
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
applicationSettingsStudy = apex.setting.ApplicationSettingsStudy(useNewScenario = False,displayPrereleaseScenario = False)
apex.setting.setApplicationSettingsStudy(applicationSettingsStudy = applicationSettingsStudy)
model_1 = apex.currentModel()

# 
# Start of recorded operations
# 

_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_1.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_2 = part_2.getSolid( name = "P_InterMed" )
_target.append( solid_2 )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_3 = part_3.getSolid( name = "Original_PSuperior" )
_target.append( solid_3 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
solid_4 = part_4.getSolid( name = "P_Inferior_Interior" )
_target.append( solid_4 )
result = apex.geometry.mergeBoolean(
    target = _target,
    retainOriginalBodies = False,
    mergeSolidsAsCells = False
)

# 
# Macro recording stopped on Jun 14, 2025 at 11:09:18
# 


def get_plane_normal(p1, p2, p3):
    """Devuelve el vector normal de un plano definido por tres puntos."""
    u = [p2.x - p1.x, p2.y - p1.y, p2.z - p1.z]
    v = [p3.x - p1.x, p3.y - p1.y, p3.z - p1.z]
    return [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ]

def point_plane_distance(p, plane_point, normal):
    """Calcula la distancia signed de un punto a un plano."""
    return (
        normal[0]*(p[0] - plane_point.x) +
        normal[1]*(p[1] - plane_point.y) +
        normal[2]*(p[2] - plane_point.z)
    )

# ---------------------- PLANOS ----------------------
planos = []
# Plano 1
plano_1_pts = [
    apex.Coordinate(-20.0, 0.0, 0.0),
    apex.Coordinate( 20.0, 0.0, 0.0),
    apex.Coordinate( 0.0, 0.0, -40.0)
]
planos.append((plano_1_pts[0], get_plane_normal(*plano_1_pts)))

# Plano 2
plano_2_pts = [
    apex.Coordinate(0.0, -20.0, 0.0),
    apex.Coordinate(0.0, 20.0, 0.0),
    apex.Coordinate(0.0, 0.0, -40.0)
]
planos.append((plano_2_pts[0], get_plane_normal(*plano_2_pts)))

# Plano 3
plano_3_pts = [
    apex.Coordinate(-20.0, 20.0, 0.0),
    apex.Coordinate( 20.0, -20.0, 0.0),
    apex.Coordinate( 0.0, 0.0, -40.0)
]
planos.append((plano_3_pts[0], get_plane_normal(*plano_3_pts)))

# Plano 4
plano_4_pts = [
    apex.Coordinate(-20.0, -20.0, 0.0),
    apex.Coordinate( 20.0,  20.0, 0.0),
    apex.Coordinate( 0.0,  0.0, -40.0)
]
planos.append((plano_4_pts[0], get_plane_normal(*plano_4_pts)))


# # ---------------------- DETECCIÓN DE CARAS HORIZONTALES Y EXTRACCIÓN DE Z ----------------------

# part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
# part_1.show()


# part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
# solid = part.getSolid( name = "Original_PSuperior" )

# vertices = solid.getVertices()


# tolerance_z = 1e-4
# z_horizontales = []

# for face in solid.getFaces():
#     vertices = face.vertices
#     if len(vertices) < 3:
#         continue  # no es una cara útil

#     # Extraemos las coordenadas Z de todos los vértices
#     z_coords = [round(vertex.getLocationCartesian()[2], 6) for vertex in vertices]

#     # Comprobamos si todos los vértices están aproximadamente en el mismo plano Z
#     z_min = min(z_coords)
#     z_max = max(z_coords)

#     if abs(z_max - z_min) < tolerance_z:
#         z_promedio = round(sum(z_coords) / len(z_coords), 6)
#         z_horizontales.append(z_promedio)

# # Eliminamos duplicados y ordenamos
# z_horizontales = sorted(set(z_horizontales))
# print(f"Z horizontales encontradas: {z_horizontales}")

# if len(z_horizontales) >= 4:
#     z_intermedia_1 = z_horizontales[1]
#     z_intermedia_2 = z_horizontales[2]
#     print(f"Z intermedias seleccionadas: {z_intermedia_1}, {z_intermedia_2}")
# else:
#     raise ValueError("No se encontraron al menos 4 caras horizontales para extraer las Z intermedias.")







# ---------------------- VÉRTICES ----------------------


# Igual para la pieza Inferior Intermedia

part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )

vertices = solid.getVertices()



tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vértice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Está en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vértice(s) que no pertenecen a ningún plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vértices a eliminar. Continuando con el siguiente código...")
    
    
    
# PASO INTERMEDIO --- DIVISION DE LA PIEZA EN UN PLANO ZX para obtener vertices relevantes

# 1. Seleccionar el sólido objetivo
part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )

# 2. Crear colección de entidad objetivo
_target = apex.EntityCollection()
_target.append(solid)

# 3. Definir el plano ZX en Y = 0.0 (puedes ajustar este valor)
y_cut = 0.0
_locations = [
    apex.Coordinate(0.0, y_cut, -1000.0),   # punto 1
    apex.Coordinate(0.0, y_cut,  1000.0),   # punto 2
    apex.Coordinate(1000.0, y_cut, 0.0),    # punto 3 (define la dirección X)
]

_location_collection = apex.ILocationCollection()
for pt in _locations:
    _location_collection.append(pt)

# 4. Dividir por plano
result = apex.geometry.splitOn3PointPlane(
    target=_target,
    locations=_location_collection,
    splitBehavior=apex.geometry.GeometrySplitBehavior.Partition
)

print("División por plano ZX completada correctamente.")
    


# Grupos de Z Vertices

# Obtener el sólido tras la división por plano ZX
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Obtener todos los vértices
vertices = solid.getVertices()

# Agrupar coordenadas por Z (con tolerancia)
tolerance = 1e-4
z_groups = defaultdict(list)

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    z_coord = coord[2]
    
    # Redondear para agrupar según tolerancia
    z_rounded = round(z_coord / tolerance) * tolerance
    z_groups[z_rounded].append(coord)

# Ordenar las claves Z únicas
z_unique_sorted = sorted(z_groups.keys())
print(f"Coordenadas Z únicas encontradas: {z_unique_sorted}")

# Si hay al menos 4 niveles, extraer las 2 intermedias
if len(z_unique_sorted) >= 4:
    z_intermedia1 = z_unique_sorted[1]
    z_intermedia2 = z_unique_sorted[-2]
    print(f"\nZ intermedia 1: {z_intermedia1}")
    print(f"Z intermedia 2: {z_intermedia2}")
else:
    print("No se han encontrado suficientes niveles Z para determinar intermedios.")
    
# Seleccionar el sólido de la pieza a dividir
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Crear una colección de entidades con el sólido
_target = EntityCollection()
_target.append(solid)

# Realizar la división en cada z_intermedia con plano XY
for z in [z_intermedia1, z_intermedia2]:
    print(f"Dividiendo en plano XY a z = {z}...")
    
    # Definir 3 puntos sobre el plano XY a altura z
    _locations = [
        apex.Coordinate(-20.0, 0.0, z),
        apex.Coordinate(20.0, 0.0, z),
        apex.Coordinate(0.0, 20.0, z)
    ]
    
    _iphysicalCollection = apex.ILocationCollection()
    for point in _locations:
        _iphysicalCollection.append(point)

    # Ejecutar la división
    result = apex.geometry.splitOn3PointPlane(
        target = _target,
        locations = _iphysicalCollection,
        splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
    )
    
    
    
    
    
    
    
    
    
    
# part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
# solid = part.getSolid(name = "Original_PSuperior")

# # Crear una colección de entidades con el sólido
# _target = EntityCollection()
# _target.append(solid)



# _locations = [
#     apex.Coordinate( 0.0, -2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 0.0, 2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
# ]
# _iphysicalCollection = apex.ILocationCollection() 
# for point in _locations :

#     _iphysicalCollection.append(point)
# result = apex.geometry.splitOn3PointPlane(
#     target = _target,
#     locations = _iphysicalCollection,
#     splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
# )


# _locations = [
#     apex.Coordinate( -2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
# ]
# _iphysicalCollection = apex.ILocationCollection() 
# for point in _locations :

#     _iphysicalCollection.append(point)
# result = apex.geometry.splitOn3PointPlane(
#     target = _target,
#     locations = _iphysicalCollection,
#     splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
# )



# _locations = [
#     apex.Coordinate( -2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
#     apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
# ]
# _iphysicalCollection = apex.ILocationCollection() 
# for point in _locations :

#     _iphysicalCollection.append(point)
# result = apex.geometry.splitOn3PointPlane(
#     target = _target,
#     locations = _iphysicalCollection,
#     splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
# )










































# # # Seleccionar el sólido de la pieza ya dividida
# # part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
# # solid = part.getSolid(name = "Original_PSuperior")

# # # Obtener las celdas (tras divisiones, debe haber 6)
# # cells = solid.getCells()
# # print(f"Se encontraron {len(cells)} celdas.")

# # # Obtener centroides y agrupar celdas por coordenada Z (con tolerancia)
# # z_groups = {}
# # tolerance = 1e-5

# # for cell in cells:
# #     z = cell.centroid.z
# #     z_rounded = round(z / tolerance) * tolerance  # Agrupamos con tolerancia
# #     if z_rounded not in z_groups:
# #         z_groups[z_rounded] = []
# #     z_groups[z_rounded].append(cell)

# # # Confirmamos que hay 3 grupos
# # print(f"Grupos de Z encontrados: {len(z_groups)}")
# # for z_val, celdas in z_groups.items():
# #     print(f"Z={z_val:.4f} mm → {len(celdas)} celda(s)")

# # # Unir las celdas de cada grupo Z
# # for z_val, cell_list in z_groups.items():
# #     if len(cell_list) < 2:
# #         print(f"Advertencia: solo hay {len(cell_list)} celda(s) en Z={z_val:.4f}, se omite unión.")
# #         continue
    
# #     print(f"Uniendo {len(cell_list)} celdas en Z={z_val:.4f}...")

# #     _merge_target = apex.EntityCollection()
# #     for c in cell_list:
# #         _merge_target.append(c)

# #     result = apex.geometry.mergeBoolean(
# #         target = _merge_target,
# #         retainOriginalBodies = False,
# #         mergeSolidsAsCells = True  # Muy importante para mantener un solo solid
# #     )



