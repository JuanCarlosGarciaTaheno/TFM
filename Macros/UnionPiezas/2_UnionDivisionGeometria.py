# coding: utf-8
import apex
from apex.construct import Point3D, Point2D
from apex import EntityCollection, ColorRGB
from collections import defaultdict
from apex.geometry import GeometrySplitBehavior, split
import math 
from math import sqrt


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

############################################################################################################################
#
#                                Eliminiacion de Vertices sobrantes - Definicion de los planos 
#
############################################################################################################################




# ---------------------- VERTICES ----------------------
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





############################################################################################################################
#
#                                      Eliminacion de vertices extra en Arandela
#
############################################################################################################################


# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Arandela")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Arandela/PartBody")
solid = part.getSolid(name="PartBody")
vertices = solid.getVertices()



tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vertice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Esta en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vertice(s) que no pertenecen a ningun plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vertices a eliminar. Continuando con el siguiente codigo...")
    




############################################################################################################################
#
#                                      Eliminacion de vertices extra en Tornillo
#
############################################################################################################################


# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()


assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca")
assembly_2.show()


part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody")
solid = part.getSolid(name="PartBody")
vertices = solid.getVertices()


tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vertice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Esta en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vertice(s) que no pertenecen a ningun plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vertices a eliminar. Continuando con el siguiente codigo...")
    


# Ensenar toda la pieza
assembly_1 = apex.getAssembly( pathName = apex.currentModel().name )
assembly_1.show()



############################################################################################################################
#
#
#                                    UNION DE TODAS LAS PIEZAS EN LA PARTE INFERIOR
#
#
############################################################################################################################


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






############################################################################################################################
#
#
#                                       ELIMINACION DE VERTICES EXTRAS
#
#
############################################################################################################################


# ---------------------- VERTICES ----------------------


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
    
    # Comprobamos si el vertice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Esta en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vertice(s) que no pertenecen a ningun plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vertices a eliminar. Continuando con el siguiente codigo...")
    
    

############################################################################################################################
#
#
#             PASO INTERMEDIO --- DIVISION DE LA PIEZA EN UN PLANO ZX para obtener vertices relevantes
#
#
############################################################################################################################


# 1. Seleccionar el solido objetivo
part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )

# 2. Crear coleccion de entidad objetivo
_target = apex.EntityCollection()
_target.append(solid)

# 3. Definir el plano ZX en Y = 0.0 (puedes ajustar este valor)
y_cut = 0.0
_locations = [
    apex.Coordinate(0.0, y_cut, -1000.0),   # punto 1
    apex.Coordinate(0.0, y_cut,  1000.0),   # punto 2
    apex.Coordinate(1000.0, y_cut, 0.0),    # punto 3 (define la direccion X)
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

print("Division por plano ZX completada correctamente.")
    

############################################################################################################################
#
#
#                                       Grupos de Z Vertices
#
#
############################################################################################################################

# 

# Obtener el solido tras la division por plano ZX
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Obtener todos los vertices
vertices = solid.getVertices()

# Agrupar coordenadas por Z (con tolerancia)
tolerance = 1e-4
z_groups = defaultdict(list)

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    z_coord = coord[2]
    
    # Redondear para agrupar segun tolerancia
    z_rounded = round(z_coord / tolerance) * tolerance
    z_groups[z_rounded].append(coord)

# Ordenar las claves Z unicas
z_unique_sorted = sorted(z_groups.keys())
print(f"Coordenadas Z unicas encontradas: {z_unique_sorted}")

# Si hay al menos 4 niveles, extraer las 2 intermedias
if len(z_unique_sorted) >= 4:
    z_intermedia1 = z_unique_sorted[1]
    z_intermedia2 = z_unique_sorted[-2]
    print(f"\nZ intermedia 1: {z_intermedia1}")
    print(f"Z intermedia 2: {z_intermedia2}")
else:
    print("No se han encontrado suficientes niveles Z para determinar intermedios.")


############################################################################################################################
#
#
#                                       Divivision PlANO ZX
#
#
############################################################################################################################



# Seleccionar el solido de la pieza a dividir
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Crear una coleccion de entidades con el solido
_target = EntityCollection()
_target.append(solid)

# Realizar la division en cada z_intermedia con plano XY
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

    # Ejecutar la division
    result = apex.geometry.splitOn3PointPlane(
        target = _target,
        locations = _iphysicalCollection,
        splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
    )


############################################################################################################################
#
#
#                          OBTENICION DE LOS CENTRODIES DE LAS CELDAS EN LA PIEZA INFERIOR IZQUIERDA
#
#
############################################################################################################################



# Obtener la pieza y sus celdas
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")
celdas = solid.getCells()

def obtener_celdas_izquierda_ordenadas_por_z(celdas):
    celdas_izq = []

    # Recorremos todas las celdas
    for celda in celdas:
        centroide = celda.getCentroid()
        print(f"Centroide celda: X={centroide.x:.3f}, Y={centroide.y:.3f}, Z={centroide.z:.3f}")
        
        if centroide.y > 0:
            celdas_izq.append((celda, centroide.z))

    # Ordenamos por Z descendente (de mayor a menor Z)
    celdas_izq.sort(key=lambda x: x[1], reverse=True)

    if len(celdas_izq) != 3:
        raise ValueError("Se esperaban exactamente 3 celdas en el lado izquierdo.")

    # Extraemos las celdas en orden superior, media, inferior
    izq_sup, izq_med, izq_inf = [celda for celda, _ in celdas_izq]

    return izq_sup, izq_med, izq_inf



izq_sup, izq_med, izq_inf = obtener_celdas_izquierda_ordenadas_por_z(celdas)


highlight_color = ColorRGB(255, 0, 0)
izq_inf.highlight(highlight_color, lineWidth=2, pointSize=5)


highlight_color = ColorRGB(0, 255, 0) 
izq_med.highlight(highlight_color, lineWidth=2, pointSize=5)


highlight_color = ColorRGB(0, 0, 255)   
izq_sup.highlight(highlight_color, lineWidth=2, pointSize=5)






def calcular_normal(cara):
    # Sacamos 3 vertices para calcular vector normal
    vertices = cara.getVertices()
    p1 = vertices[0].getLocationCartesian()
    p2 = vertices[1].getLocationCartesian()
    p3 = vertices[2].getLocationCartesian()

    # Vectores en la cara
    v1 = [p2[i] - p1[i] for i in range(3)]
    v2 = [p3[i] - p1[i] for i in range(3)]

    # Producto cruz para normal
    normal = [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

    # Normalizamos
    norm = (normal[0]**2 + normal[1]**2 + normal[2]**2)**0.5
    normal = [n / norm for n in normal]

    return normal

def es_horizontal(normal, tolerancia=1e-3):
    # La cara es horizontal si su normal apunta casi paralela al eje Z (+-Z)
    # Normal Z cerca de 1 o -1 -> horizontal
    return abs(abs(normal[2]) - 1.0) < tolerancia

def obtener_cara_no_horizontal_menor_area(celda):
    caras = celda.getFaces()
    cara_min = None
    area_min = float('inf')

    for cara in caras:
        normal = calcular_normal(cara)
        if not es_horizontal(normal):
            area = cara.getArea()
            if area < area_min:
                area_min = area
                cara_min = cara

    return cara_min, area_min

def obtener_cara_objetivo(celda, tolerancia_x=1e-2):
    centroide_celda = celda.getCentroid()
    x_celda = centroide_celda.x
    
    caras = celda.getFaces()
    cara_objetivo = None
    area_min = float('inf')
    
    for cara in caras:
        normal = calcular_normal(cara)
        if not es_horizontal(normal):
            centroide_cara = cara.getCentroid()
            # Comprobar que el centroide Z de la cara este cerca del centroide Z de la celda
            if abs(centroide_cara.x - x_celda) < tolerancia_x:
                area = cara.getArea()
                if area < area_min:
                    area_min = area
                    cara_objetivo = cara

    return cara_objetivo, area_min


cara_obj, area = obtener_cara_objetivo(izq_med, tolerancia_x=0.1)  # Ajusta la tolerancia a lo que necesites
print(f"Cara objetivo: area={area}, centroide Z cercano a {izq_med.getCentroid().z}")


highlight_color = ColorRGB(100, 100, 255)   
cara_obj.highlight(highlight_color, lineWidth=2, pointSize=5)

# Preparar colecciones para el split
_target = apex.EntityCollection()
_target.append(izq_inf)

_splitter = apex.EntityCollection()
_splitter.append(cara_obj)

# Realizar el split
result = apex.geometry.split(
    target = _target,
    splitter = _splitter,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("Split realizado correctamente.")



############################################################################################################################
#
#
#                          OBTENICION DE LOS CENTRODIES DE LAS CELDAS EN LA PIEZA INFERIOR DERECHA
#
#
############################################################################################################################





def obtener_celdas_derecha_ordenadas_por_z(celdas):
    celdas_der = []

    for celda in celdas:
        centroide = celda.getCentroid()
        print(f"Centroide celda: X={centroide.x:.3f}, Y={centroide.y:.3f}, Z={centroide.z:.3f}")
        
        if centroide.y < 0:  # Aqui filtrar las celdas del lado derecho (Y negativo)
            celdas_der.append((celda, centroide.z))

    # Ordenamos por Z descendente (de mayor a menor altura)
    celdas_der.sort(key=lambda x: x[1], reverse=True)

    if len(celdas_der) != 3:
        raise ValueError("Se esperaban exactamente 3 celdas en el lado derecho.")

    der_sup, der_med, der_inf = [celda for celda, _ in celdas_der]

    return der_sup, der_med, der_inf


# Obtener celdas del lado derecho ordenadas
der_sup, der_med, der_inf = obtener_celdas_derecha_ordenadas_por_z(celdas)

# Resaltar para verificar visualmente
der_inf.highlight(ColorRGB(255, 128, 0), lineWidth=2, pointSize=5)
der_med.highlight(ColorRGB(255, 255, 0), lineWidth=2, pointSize=5)
der_sup.highlight(ColorRGB(128, 0, 255), lineWidth=2, pointSize=5)

# Obtener la cara objetivo en la celda intermedia derecha
cara_obj_der, area_der = obtener_cara_objetivo(der_med, tolerancia_x=0.1)
print(f"Cara objetivo derecha: area={area_der}, centroide Z cercano a {der_med.getCentroid().z}")

cara_obj_der.highlight(ColorRGB(0, 255, 255), lineWidth=2, pointSize=5)

# Preparar colecciones para el split
_target_der = apex.EntityCollection()
_target_der.append(der_inf)

_splitter_der = apex.EntityCollection()
_splitter_der.append(cara_obj_der)

# Realizar el split
result_der = apex.geometry.split(
    target = _target_der,
    splitter = _splitter_der,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("Split realizado correctamente en el lado derecho.")



############################################################################################################################
#
#
#                          DIVISION DE LA PIEZA EN LOS 4 PLANOS (1 PLANO YA ESTABA REALIZADO)
#
#
############################################################################################################################



part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Crear una coleccion de entidades con el solido
_target = EntityCollection()
_target.append(solid)



_locations = [
    apex.Coordinate( 0.0, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


_locations = [
    apex.Coordinate( -2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)



_locations = [
    apex.Coordinate( -2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


############################################################################################################################
#
#
#                                    FINALIZACION UNION Y DIVISION DE LA PIEZA INFERIO
#
#
############################################################################################################################


# # Obtener el solido correspondiente
# part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
# solid = part.getSolid(name = "Original_PSuperior")

# # Obtener todas las celdas del solido
# celdas = solid.getCells()

# # Imprimir coordenadas de los centroides
# for i, celda in enumerate(celdas):
#     centroide = celda.getCentroid()
#     print(f"Celda {i+1}: X = {centroide.x:.6f}, Y = {centroide.y:.6f}, Z = {centroide.z:.6f}")




# Obtener solido
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Obtener todas las celdas
celdas = solid.getCells()

# Ordenar todas las celdas por centroide.z de mayor a menor
celdas_ordenadas_z = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)

# Dividir en zonas por posición Z
zona_superior = celdas_ordenadas_z[:8]
zona_media    = celdas_ordenadas_z[8:16]
zona_inferior = celdas_ordenadas_z[16:]

print(f"\nZonas detectadas:")
print(f"  Superior: {len(zona_superior)} celdas")
print(f"  Media   : {len(zona_media)} celdas")
print(f"  Inferior: {len(zona_inferior)} celdas")

# Dividir zona inferior segun la distancia al origen
celdas_con_distancia = []

for celda in zona_inferior:
    centroide = celda.getCentroid()
    distancia = (centroide.x**2 + centroide.y**2 + centroide.z**2)**0.5
    celdas_con_distancia.append((celda, distancia))

# Ordenar por distancia al origen
celdas_con_distancia.sort(key=lambda x: x[1])

# Separar en dos grupos de 8
inferior_cercanas = [celda for celda, _ in celdas_con_distancia[:8]]
inferior_alejadas = [celda for celda, _ in celdas_con_distancia[8:]]

print(f"\nZona inferior dividida:")
print(f"  Cercanas al origen: {len(inferior_cercanas)} celdas")
print(f"  Alejadas del origen: {len(inferior_alejadas)} celdas")

# Colorear para comprobacion (opcional)
for celda in inferior_cercanas:
    celda.highlight(ColorRGB(0, 255, 0), lineWidth=2, pointSize=5)  # Verde


for celda in inferior_alejadas:
    celda.highlight(ColorRGB(255, 0, 0), lineWidth=2, pointSize=5)  # Rojo



##### OBTENER EL AREA A DIVIDIR DE LA ZONA SUPERIOR



def distancia_al_origen(coord):
    return math.sqrt(coord.x**2 + coord.y**2 + coord.z**2)

# 1. Encontrar la celda superior mas cercana al origen
celda_mas_cercana = min(zona_superior, key=lambda c: distancia_al_origen(c.getCentroid()))

# 2. Obtener la cara objetivo de esa celda (por ejemplo la de area minima)
def obtener_cara_min_area(celda):
    caras = celda.getFaces()
    cara_min = min(caras, key=lambda cara: cara.getArea())
    return cara_min

cara_objetivo = obtener_cara_min_area(celda_mas_cercana)

# 3. Colorear la cara para distinguirla 
cara_objetivo.highlight(ColorRGB(0, 255, 255), lineWidth=2, pointSize=5)




### DIVIDIR LA ZONA MEDIA E INFERIOR EXTERIOR

# Importante: Preparar colecciones de entidades para target y splitter

# Convertir listas de celdas en EntityCollection
media_collection = apex.EntityCollection()
for celda in zona_media:
    media_collection.append(celda)

inferior_lejanas_collection = apex.EntityCollection()
for celda in inferior_alejadas:
    inferior_lejanas_collection.append(celda)

splitter_collection = apex.EntityCollection()
splitter_collection.append(cara_objetivo)

# Split en zona media
resultado_media = apex.geometry.split(
    target = media_collection,
    splitter = splitter_collection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

# Split en zona inferior exterior (las mas alejadas)
resultado_inferior_lejanas = apex.geometry.split(
    target = inferior_lejanas_collection,
    splitter = splitter_collection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)



############################################################################################################################
#
#
#                                       INICIO DE LA UNION Y DIVISION DEL TORNILLO
#
#
############################################################################################################################


assembly_1 = apex.getAssembly( pathName = apex.currentModel().name )
assembly_1.hide()

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca" )
assembly_2.show()


######################################################################

#       Union Cuerpo Tornillo entre si

######################################################################


_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_1 = part_1.getSolid( name = "Body.6" )
_target.append( solid_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
result = apex.geometry.mergeBoolean(
    target = _target,
    retainOriginalBodies = False,
    mergeSolidsAsCells = False
)

######################################################################

#       Union Cuerpo Tornillo - Cabeza

######################################################################

assembly_3 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
assembly_3.show()

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
result = apex.geometry.mergeBoolean(
    target = _target,
    retainOriginalBodies = False,
    mergeSolidsAsCells = False
)


#
######################################################################

#                   Divisiones Horizontales

######################################################################

# Paso 1: Obtener todos los vertices de la cabeza del tornillo
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
vertices = solid.getVertices()

# Paso 2: Agrupar por coordenada Z (con tolerancia)
z_groups = defaultdict(list)
tolerance = 1e-3

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    z = coord[2]
    
    # Normalizar con tolerancia
    matched = False
    for key in z_groups:
        if abs(z - key) < tolerance:
            z_groups[key].append(vertex)
            matched = True
            break
    if not matched:
        z_groups[z].append(vertex)


# Ordenar las alturas
sorted_z_values = sorted(z_groups.keys())
if len(sorted_z_values) < 5:
    raise Exception("No se encontraron al menos 3 grupos distintos de altura Z")

# Paso 3: Elegir el grupo intermedio entre la cabeza y el cuerpo
z_middle = sorted_z_values[2]
middle_vertices = z_groups[z_middle]

Z_medio_cabeza =  sorted_z_values[3]

# PASO 4: Obtener la parte y solido - DIVISION
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
_target.append( solid )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, z_middle ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, z_middle ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, z_middle )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print(" Corte realizado entre el cuerpo y la cabeza.")

# PASO 5: Obtener la parte y solido - DIVISION de la Cabeza
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
_target.append( solid )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, Z_medio_cabeza )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print(" Corte realizado en la cabeza.")


######################################################################

#        Divisiones Verticales de la Cabeza celda Inferior

######################################################################

# Paso 1: Obtener todos los vertices de la cabeza del tornillo
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
    
        
celdas = solid.getCells()

def obtener_celdas_ordenadas_por_z(celdas):
    # Creamos una lista con pares (celda, centroide.z)
    lista_celdas_z = [(celda, celda.getCentroid().z) for celda in celdas]

    # Ordenamos por Z descendente (de mayor a menor)
    lista_celdas_z.sort(key=lambda x: x[1], reverse=True)

    # Solo devolvemos la lista de celdas ordenadas
    return [celda for celda, z in lista_celdas_z]



celdas_ordenadas = obtener_celdas_ordenadas_por_z(celdas)

# Imprimir los centroides Z para verificar orden
for i, celda in enumerate(celdas_ordenadas):
    c = celda.getCentroid()
    print(f"Celda {i+1}: Centroide Z = {c.z:.3f}")


segunda_celda = celdas_ordenadas[1]
print("Centroide Z segunda celda:", segunda_celda.getCentroid().z)

_target.append( segunda_celda )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0,0.0 ),
    apex.Coordinate( 0.0, 0.0, 20.0 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


######################################################################

#        CORTES A CELDAS POR DEBAJO DE LA SEGUNDA CELDA (EN Z)

######################################################################

# 1. Obtener todas las celdas del solido
celdas = solid.getCells()

# 2. Obtener la Z del centroide de la segunda celda
z_referencia = segunda_celda.getCentroid().z
print(f"Centroide Z segunda celda: {z_referencia:.6f}")

# 3. Filtrar solo celdas por debajo
celdas_debajo = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda < z_referencia - 0.5:  # Ajuste de margen
        celdas_debajo.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} >= {z_referencia:.3f}")

print(f"\n Numero de celdas por debajo: {len(celdas_debajo)}")
if len(celdas_debajo) == 0:
    raise RuntimeError(" No hay celdas validas por debajo para aplicar los cortes.")

# 4. Definir los 4 cortes (cada uno con 3 puntos)
cortes_locations = [
    [apex.Coordinate(-20.0, 0.0, 0.0),  apex.Coordinate(20.0, 0.0, 0.0),  apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(0.0, -20.0, 0.0),  apex.Coordinate(0.0, 20.0, 0.0),  apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(-20.0, 20.0, 0.0), apex.Coordinate(20.0, -20.0, 0.0), apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(-20.0, -20.0, 0.0), apex.Coordinate(20.0, 20.0, 0.0), apex.Coordinate(0.0, 0.0, -40.0)]
]

# 5. Aplicar cortes secuencialmente
celdas_actuales = celdas_debajo

for i, locations in enumerate(cortes_locations, start=1):
    _iphysicalCollection = apex.ILocationCollection()
    for punto in locations:
        _iphysicalCollection.append(punto)

    # Si no quedan celdas, detener y notificar
    if len(celdas_actuales) == 0:
        raise RuntimeError(f" No quedan celdas que cortar antes del corte {i}")

    try:
        result = apex.geometry.splitOn3PointPlane(
            target=celdas_actuales,
            locations=_iphysicalCollection,
            splitBehavior=apex.geometry.GeometrySplitBehavior.Partition
        )
        celdas_actuales = result
  # Actualizar celdas para el siguiente corte
        print(f" Corte {i} realizado correctamente. Nuevas celdas: {len(celdas_actuales)}")
    except Exception as e:
        print(f" Error en corte {i}: {e}")
        break



######################################################################

#        UNIR CELDAS QUE ESTAN POR ENCIMA DE LA SEGUNDA CELDA (Z)

######################################################################

celdas = solid.getCells()

# 2. Usar Z de la segunda celda como referencia
z_referencia = segunda_celda.getCentroid().z

# 3. Filtrar las celdas que esten por encima
celdas_por_encima = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda > z_referencia - 0.1:
        celdas_por_encima.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} <= {z_referencia:.3f}")

print(f"\n Numero de celdas por encima: {len(celdas_por_encima)}")

# 4. Si hay varias, unirlas con mergeBoolean
if len(celdas_por_encima) > 1:
    _merge_target = apex.EntityCollection()
    for celda in celdas_por_encima:
        _merge_target.append(celda)

    try:
        resultado_union = apex.geometry.mergeBoolean(
            target=_merge_target,
            retainOriginalBodies=False,
            mergeSolidsAsCells=True  # Importante para que no cree cuerpos separados
        )
        print(" Celdas unidas correctamente en una unica celda.")
        # Opcional: seleccionar y colorear el resultado
        apex.selection.set(resultado_union)
        resultado_union[0].setColor(apex.render.Color(255, 150, 150))
    except Exception as e:
        print(f" Error al unir celdas: {e}")
elif len(celdas_por_encima) == 1:
    print("ℹ Solo hay una celda por encima, no es necesario unir.")
else:
    print(" No hay celdas por encima del plano para unir.")
    

######################################################################

#        Division plano ZX del tornillo

###################################################################### 

   
# Dividir por un plano
_target  = celdas_por_encima
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0,0.0 ),
    apex.Coordinate( 0.0, 0.0, 20.0 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)



######################################################################

#        Division plano Horizontal en la Cabeza

###################################################################### 


# 1: Obtener la parte y solido - DIVISION de la Cabeza
celdas = solid.getCells()

# 2. Usar Z de la segunda celda como referencia
z_referencia = segunda_celda.getCentroid().z

# 3. Filtrar las celdas que esten por encima
celdas_por_encima = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda > z_referencia - 0.1:
        celdas_por_encima.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} <= {z_referencia:.3f}")


_target  = celdas_por_encima
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, Z_medio_cabeza )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


###############################################################

#    Uno las dos celdas Superiores de la cabeza del tornillo

###############################################################

part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name="PartBody")

# Obtener y ordenar las celdas segun Z del centroide
celdas = solid.getCells()
celdas_ordenadas = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)

# Tomar las 2 celdas con mayor Z
celdas_superiores = celdas_ordenadas[:2]

# Mostrar centroides para verificacion
print("Centroides de las 2 celdas superiores:")
for i, celda in enumerate(celdas_superiores):
    centroide = celda.getCentroid()
    print(f"Celda {i+1}: x = {centroide.x:.3f}, y = {centroide.y:.3f}, z = {centroide.z:.3f}")

# Unir las 2 celdas superiores
_merge_target = apex.EntityCollection()
for c in celdas_superiores:
    _merge_target.append(c)

try:
    apex.geometry.mergeBoolean(
        target=_merge_target,
        retainOriginalBodies=False,
        mergeSolidsAsCells=True  # muy importante para unir como una sola celda
    )
    print("Celdas superiores unidas correctamente.")
except Exception as e:
    print(f"Error al unir celdas: {e}")


############################################################################################################################
#
#
#                             FINALIZACION UNION Y DIVISION DEL CUERPO Y CABEZA DEL TORNILLO
#
#
############################################################################################################################




############################################################################################################################
#
#
#                               INICIO DE LA DIVISION DEL RESTO DE PIEZAS EN 4 PLANOS
#
#
############################################################################################################################


######################################################################

#        Inicio de los cortes

###################################################################### 

# Ensenar todo las piezas
assembly_1 = apex.getAssembly( pathName = apex.currentModel().name )
assembly_1.show()



_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_1 = part_1.getCurve( name = "RoscaExterior" )
_target.append( curve_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_1 = part_2.getSolid( name = "PartBody" )
_target.append( solid_1 )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_2 = part_3.getSolid( name = "PartBody" )
_target.append( solid_2 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_3 = part_4.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_2 = part_5.getCurve( name = "Helicoil" )
_target.append( curve_2 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_6.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_3 = part_7.getCurve( name = "Rosca" )
_target.append( curve_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_4 = part_8.getCurve( name = "EjeReferencia" )
_target.append( curve_4 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_9.getSolid( name = "PartBody" )
_target.append( solid_5 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)




_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_1 = part_1.getCurve( name = "RoscaExterior" )
_target.append( curve_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_1 = part_2.getSolid( name = "PartBody" )
_target.append( solid_1 )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_2 = part_3.getSolid( name = "PartBody" )
_target.append( solid_2 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_3 = part_4.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_2 = part_5.getCurve( name = "Helicoil" )
_target.append( curve_2 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_6.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_3 = part_7.getCurve( name = "Rosca" )
_target.append( curve_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_4 = part_8.getCurve( name = "EjeReferencia" )
_target.append( curve_4 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_9.getSolid( name = "PartBody" )
_target.append( solid_5 )
_locations = [
    apex.Coordinate( 0.0, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_1 = part_1.getCurve( name = "RoscaExterior" )
_target.append( curve_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_1 = part_2.getSolid( name = "PartBody" )
_target.append( solid_1 )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_2 = part_3.getSolid( name = "PartBody" )
_target.append( solid_2 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_3 = part_4.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_2 = part_5.getCurve( name = "Helicoil" )
_target.append( curve_2 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_6.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_3 = part_7.getCurve( name = "Rosca" )
_target.append( curve_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_4 = part_8.getCurve( name = "EjeReferencia" )
_target.append( curve_4 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_9.getSolid( name = "PartBody" )
_target.append( solid_5 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)



_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_1 = part_1.getCurve( name = "RoscaExterior" )
_target.append( curve_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_1 = part_2.getSolid( name = "PartBody" )
_target.append( solid_1 )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_2 = part_3.getSolid( name = "PartBody" )
_target.append( solid_2 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_3 = part_4.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_2 = part_5.getCurve( name = "Helicoil" )
_target.append( curve_2 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_6.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_3 = part_7.getCurve( name = "Rosca" )
_target.append( curve_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_4 = part_8.getCurve( name = "EjeReferencia" )
_target.append( curve_4 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_9.getSolid( name = "PartBody" )
_target.append( solid_5 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)






