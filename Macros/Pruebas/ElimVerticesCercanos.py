# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 11:20:39
# 
# Macro Name = VertexElim
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



import apex
from apex.construct import Point3D, Point2D
import math

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

# ---------------------- VÉRTICES ----------------------


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

# Igual para la pieza Inferior Intermedia

part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid = part.getSolid( name = "P_InterMed" )

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