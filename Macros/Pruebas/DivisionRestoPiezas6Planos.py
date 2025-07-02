# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 15, 2025 at 10:11:10
# 
# Macro Name = DivisionRestoPiezas6Planos
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D

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






# ---------------------- VÉRTICES ----------------------
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