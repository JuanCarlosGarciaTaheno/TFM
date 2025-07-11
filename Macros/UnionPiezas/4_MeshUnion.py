# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 15, 2025 at 17:49:05
# 
# Macro Name = 4_MeshUnion
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
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




import math

# Funcion para obtener el angulo de posicionamiento de una celda
def obtener_angulo_xy(centroide):
    """Angulo en plano XY respecto al eje X, sentido horario (sistema Apex Z hacia arriba)."""
    x, y = centroide.x, centroide.y
    angulo = math.atan2(y, x)
    if angulo < 0:
        angulo += 2 * math.pi
    return angulo




#####################################################

#                   ARANDELA

#####################################################

# Lista de rutas a los solidos que quieres mallar
solidos_a_mallar = [
    # Arandela
    {
        "path": "/Union_Apex/Arandela/PartBody",
        "name": "PartBody"
    }
    # # Pieza Superior
    # {
    #     "path": "/Union_Apex/PiezaSuperior1/PartBody",
    #     "name": "PartBody"
    # },
    # # Pieza Inferior Top
    # {
    #     "path": "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior",
    #     "name": "Original_PSuperior"
    # }
]

# Procesar cada solido
for entrada in solidos_a_mallar:
    print(f"\nProcesando solido: {entrada['name']}")
    
    part = apex.getPart(pathName=apex.currentModel().name + entrada["path"])
    solid = part.getSolid(name=entrada["name"])
    
    celdas = solid.getCells()
    print(f"  -> Celdas encontradas: {len(celdas)}")
    
    # Agrupar celdas por Z redondeado (para considerar un mismo "nivel")
    z_groups = {}
    for celda in celdas:
        z = celda.getCentroid().z
        z_rounded = round(z, 2)  # Puedes ajustar la precision
        if z_rounded not in z_groups:
            z_groups[z_rounded] = []
        z_groups[z_rounded].append(celda)
    
    # Ordenar niveles descendentes en Z
    z_niveles_ordenados = sorted(z_groups.keys(), reverse=True)

    # Recorrer por niveles (de arriba a abajo)
    for z_key in z_niveles_ordenados:
        grupo = z_groups[z_key]

        # Ordenar celdas en el nivel por angulo (sentido horario)
        grupo_ordenado = sorted(grupo, key=lambda c: obtener_angulo_xy(c.getCentroid()))

        for celda in grupo_ordenado:
            caras = celda.getFaces()
            
            cara_min = None
            area_min = float('inf')
            
            for cara in caras:
                area = cara.getArea()
                if area < area_min:
                    area_min = area
                    cara_min = cara
            
            centroide = celda.getCentroid()
            print(f"    Celda ID {celda.getId()} - Z = {centroide.z:.3f} - Angulo = {obtener_angulo_xy(centroide):.2f} rad - Cara minima ID {cara_min.getId()} - Área: {area_min:.6f}")
            
            _target = apex.EntityCollection()
            _target.append(celda)
            
            _sweepFace = apex.EntityCollection()
            _sweepFace.append(cara_min)
            
            # Mallado desde la cara mas pequena
            result = apex.mesh.createHexMesh(
                name = "",
                target = _target,
                meshSize = tamano_malla_Arandela,
                surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
                mappedMeshDominanceLevel = 2,
                elementOrder = apex.mesh.ElementOrder.Linear,
                refineMeshUsingCurvature = False,
                elementGeometryDeviationRatio = 0.10,
                elementMinEdgeLengthRatio = 0.20,
                createFeatureMeshOnWashers = False,
                createFeatureMeshOnArbitraryHoles = False,
                preserveWasherThroughMesh = True,
                sweepFace = _sweepFace,
                hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
                projectMidsideNodesToGeometry = True
            )



#####################################################

#                Pieza Superior

#####################################################


# Lista de rutas a los solidos que quieres mallar
solidos_a_mallar = [
    # # Arandela
    # {
    #     "path": "/Union_Apex/Arandela/PartBody",
    #     "name": "PartBody"
    # },
    # Pieza Superior
    {
        "path": "/Union_Apex/PiezaSuperior1/PartBody",
        "name": "PartBody"
    }
    # # Pieza Inferior Top
    # {
    #     "path": "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior",
    #     "name": "Original_PSuperior"
    # }
]

# Procesar cada solido
for entrada in solidos_a_mallar:
    print(f"\nProcesando solido: {entrada['name']}")
    
    part = apex.getPart(pathName=apex.currentModel().name + entrada["path"])
    solid = part.getSolid(name=entrada["name"])
    
    celdas = solid.getCells()
    print(f"  -> Celdas encontradas: {len(celdas)}")
    
    # Agrupar celdas por Z redondeado (para considerar un mismo "nivel")
    z_groups = {}
    for celda in celdas:
        z = celda.getCentroid().z
        z_rounded = round(z, 2)  # Puedes ajustar la precision
        if z_rounded not in z_groups:
            z_groups[z_rounded] = []
        z_groups[z_rounded].append(celda)
    
    # Ordenar niveles descendentes en Z
    z_niveles_ordenados = sorted(z_groups.keys(), reverse=True)

    # Recorrer por niveles (de arriba a abajo)
    for z_key in z_niveles_ordenados:
        grupo = z_groups[z_key]

        # Ordenar celdas en el nivel por angulo (sentido horario)
        grupo_ordenado = sorted(grupo, key=lambda c: obtener_angulo_xy(c.getCentroid()))

        for celda in grupo_ordenado:
            caras = celda.getFaces()
            
            cara_min = None
            area_min = float('inf')
            
            for cara in caras:
                area = cara.getArea()
                if area < area_min:
                    area_min = area
                    cara_min = cara
            
            centroide = celda.getCentroid()
            print(f"    Celda ID {celda.getId()} - Z = {centroide.z:.3f} - Angulo = {obtener_angulo_xy(centroide):.2f} rad - Cara minima ID {cara_min.getId()} - Área: {area_min:.6f}")
            
            _target = apex.EntityCollection()
            _target.append(celda)
            
            _sweepFace = apex.EntityCollection()
            _sweepFace.append(cara_min)
            
            # Mallado desde la cara mas pequena
            result = apex.mesh.createHexMesh(
                name = "",
                target = _target,
                meshSize = tamano_malla_PiezaSuperior,
                surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
                mappedMeshDominanceLevel = 2,
                elementOrder = apex.mesh.ElementOrder.Linear,
                refineMeshUsingCurvature = False,
                elementGeometryDeviationRatio = 0.10,
                elementMinEdgeLengthRatio = 0.20,
                createFeatureMeshOnWashers = False,
                createFeatureMeshOnArbitraryHoles = False,
                preserveWasherThroughMesh = True,
                sweepFace = _sweepFace,
                hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
                projectMidsideNodesToGeometry = True
            )


#####################################################

#                Pieza Inferior

#####################################################

# Lista de rutas a los solidos que quieres mallar
solidos_a_mallar = [
    # # Arandela
    # {
    #     "path": "/Union_Apex/Arandela/PartBody",
    #     "name": "PartBody"
    # },
    # # Pieza Superior
    # {
    #     "path": "/Union_Apex/PiezaSuperior1/PartBody",
    #     "name": "PartBody"
    # },
    # Pieza Inferior Top
    {
        "path": "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior",
        "name": "Original_PSuperior"
    }
]

# Procesar cada solido
for entrada in solidos_a_mallar:
    print(f"\nProcesando solido: {entrada['name']}")
    
    part = apex.getPart(pathName=apex.currentModel().name + entrada["path"])
    solid = part.getSolid(name=entrada["name"])
    
    celdas = solid.getCells()
    print(f"  -> Celdas encontradas: {len(celdas)}")
    
    # Agrupar celdas por Z redondeado (para considerar un mismo "nivel")
    z_groups = {}
    for celda in celdas:
        z = celda.getCentroid().z
        z_rounded = round(z, 2)  # Puedes ajustar la precision
        if z_rounded not in z_groups:
            z_groups[z_rounded] = []
        z_groups[z_rounded].append(celda)
    
    # Ordenar niveles descendentes en Z
    z_niveles_ordenados = sorted(z_groups.keys(), reverse=True)

    # Recorrer por niveles (de arriba a abajo)
    for z_key in z_niveles_ordenados:
        grupo = z_groups[z_key]

        # Ordenar celdas en el nivel por angulo (sentido horario)
        grupo_ordenado = sorted(grupo, key=lambda c: obtener_angulo_xy(c.getCentroid()))

        for celda in grupo_ordenado:
            caras = celda.getFaces()
            
            cara_min = None
            area_min = float('inf')
            
            for cara in caras:
                area = cara.getArea()
                if area < area_min:
                    area_min = area
                    cara_min = cara
            
            centroide = celda.getCentroid()
            print(f"    Celda ID {celda.getId()} - Z = {centroide.z:.3f} - Angulo = {obtener_angulo_xy(centroide):.2f} rad - Cara minima ID {cara_min.getId()} - Área: {area_min:.6f}")
            
            _target = apex.EntityCollection()
            _target.append(celda)
            
            _sweepFace = apex.EntityCollection()
            _sweepFace.append(cara_min)
            
            # Mallado desde la cara mas pequena
            result = apex.mesh.createHexMesh(
                name = "",
                target = _target,
                meshSize = tamano_malla_PiezaInferior,
                surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
                mappedMeshDominanceLevel = 2,
                elementOrder = apex.mesh.ElementOrder.Linear,
                refineMeshUsingCurvature = False,
                elementGeometryDeviationRatio = 0.10,
                elementMinEdgeLengthRatio = 0.20,
                createFeatureMeshOnWashers = False,
                createFeatureMeshOnArbitraryHoles = False,
                preserveWasherThroughMesh = True,
                sweepFace = _sweepFace,
                hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
                projectMidsideNodesToGeometry = True
            )




#####################################################

#                   Tornillo

#####################################################


_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = tamano_malla_tornillo,
    surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    refineMeshUsingCurvature = False,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    createFeatureMeshOnWashers = False,
    createFeatureMeshOnArbitraryHoles = False,
    preserveWasherThroughMesh = True,
    sweepFace = _SweepFace,
    hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
    projectMidsideNodesToGeometry = True
)

#####################################################

#             Rosca Pieza Inferior

#####################################################

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = tamano_malla_RoscaPInferior,
    surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    refineMeshUsingCurvature = False,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    createFeatureMeshOnWashers = False,
    createFeatureMeshOnArbitraryHoles = False,
    preserveWasherThroughMesh = True,
    sweepFace = _SweepFace,
    hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
    projectMidsideNodesToGeometry = True
)

#####################################################

#                   Helicoil

#####################################################

_target = apex.EntityCollection()
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = tamano_malla_Helicoil,
    surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    refineMeshUsingCurvature = False,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    createFeatureMeshOnWashers = False,
    createFeatureMeshOnArbitraryHoles = False,
    preserveWasherThroughMesh = True,
    sweepFace = _SweepFace,
    hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
    projectMidsideNodesToGeometry = True
)

#####################################################

#                Rosca Tornillo

#####################################################

_target = apex.EntityCollection()
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = tamano_malla_RoscaTornillo,
    surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    refineMeshUsingCurvature = False,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    createFeatureMeshOnWashers = False,
    createFeatureMeshOnArbitraryHoles = False,
    preserveWasherThroughMesh = True,
    sweepFace = _SweepFace,
    hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
    projectMidsideNodesToGeometry = True
)

















#####################################################

#       ARANDELA - pieza inf - pieza sup
#                 todas a la vez

#####################################################


#### ARANDELA - PIEZA SUPERIOR - PIEZA INFERIOR MISMO CODIGO DE MALLADO ####

# # Lista de rutas a los solidos que quieres mallar
# solidos_a_mallar = [
#     # Arandela
#     {
#         "path": "/Union_Apex/Arandela/PartBody",
#         "name": "PartBody"
#     },
#     # Pieza Superior
#     {
#         "path": "/Union_Apex/PiezaSuperior1/PartBody",
#         "name": "PartBody"
#     },
#     # Pieza Inferior Top
#     {
#         "path": "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior",
#         "name": "Original_PSuperior"
#     }
# ]

# # Procesar cada solido
# for entrada in solidos_a_mallar:
#     print(f"\nProcesando solido: {entrada['name']}")
    
#     part = apex.getPart(pathName=apex.currentModel().name + entrada["path"])
#     solid = part.getSolid(name=entrada["name"])
    
#     celdas = solid.getCells()
#     print(f"  -> Celdas encontradas: {len(celdas)}")
    
#     # Agrupar celdas por Z redondeado (para considerar un mismo "nivel")
#     z_groups = {}
#     for celda in celdas:
#         z = celda.getCentroid().z
#         z_rounded = round(z, 2)  # Puedes ajustar la precision
#         if z_rounded not in z_groups:
#             z_groups[z_rounded] = []
#         z_groups[z_rounded].append(celda)
    
#     # Ordenar niveles descendentes en Z
#     z_niveles_ordenados = sorted(z_groups.keys(), reverse=True)

#     # Recorrer por niveles (de arriba a abajo)
#     for z_key in z_niveles_ordenados:
#         grupo = z_groups[z_key]

#         # Ordenar celdas en el nivel por angulo (sentido horario)
#         grupo_ordenado = sorted(grupo, key=lambda c: obtener_angulo_xy(c.getCentroid()))

#         for celda in grupo_ordenado:
#             caras = celda.getFaces()
            
#             cara_min = None
#             area_min = float('inf')
            
#             for cara in caras:
#                 area = cara.getArea()
#                 if area < area_min:
#                     area_min = area
#                     cara_min = cara
            
#             centroide = celda.getCentroid()
#             print(f"    Celda ID {celda.getId()} - Z = {centroide.z:.3f} - Angulo = {obtener_angulo_xy(centroide):.2f} rad - Cara minima ID {cara_min.getId()} - Área: {area_min:.6f}")
            
#             _target = apex.EntityCollection()
#             _target.append(celda)
            
#             _sweepFace = apex.EntityCollection()
#             _sweepFace.append(cara_min)
            
#             # Mallado desde la cara más pequena
#             result = apex.mesh.createHexMesh(
#                 name = "",
#                 target = _target,
#                 meshSize = 0.2,
#                 surfaceMeshMethod = apex.mesh.SurfaceMeshMethod.Auto,
#                 mappedMeshDominanceLevel = 2,
#                 elementOrder = apex.mesh.ElementOrder.Linear,
#                 refineMeshUsingCurvature = False,
#                 elementGeometryDeviationRatio = 0.10,
#                 elementMinEdgeLengthRatio = 0.20,
#                 createFeatureMeshOnWashers = False,
#                 createFeatureMeshOnArbitraryHoles = False,
#                 preserveWasherThroughMesh = True,
#                 sweepFace = _sweepFace,
#                 hexMeshMethod = apex.mesh.HexMeshMethod.Auto,
#                 projectMidsideNodesToGeometry = True
#             )