# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 12:28:32
# 
# Macro Name = Mesh
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


# Lista de rutas a los sólidos que quieres mallar
solidos_a_mallar = [
    # Arandela
    {
        "path": "/Union_Apex/Arandela/PartBody",
        "name": "PartBody"
    },
    # Pieza Superior
    {
        "path": "/Union_Apex/PiezaSuperior1/PartBody",
        "name": "PartBody"
    },
    # Pieza Inferior Top
    {
        "path": "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior",
        "name": "Original_PSuperior"
    },
    # Pieza Inferior Media
    {
        "path": "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed",
        "name": "P_InterMed"
    },
    # Pieza Inferior Inferior
    {
        "path": "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior",
        "name": "P_Inferior_Exterior"
    }
]

# Procesar cada sólido
for entrada in solidos_a_mallar:
    print(f"\nProcesando sólido: {entrada['name']}")
    
    part = apex.getPart(pathName=apex.currentModel().name + entrada["path"])
    solid = part.getSolid(name=entrada["name"])
    
    celdas = solid.getCells()
    print(f"  → Celdas encontradas: {len(celdas)}")
    
    for celda in celdas:
        caras = celda.getFaces()
        
        cara_min = None
        area_min = float('inf')
        
        for cara in caras:
            area = cara.getArea()
            if area < area_min:
                area_min = area
                cara_min = cara
        
        print(f"    Celda ID {celda.getId()} - Cara mínima ID {cara_min.getId()} - Área: {area_min:.6f}")
        
        _target = apex.EntityCollection()
        _target.append(celda)
        
        _sweepFace = apex.EntityCollection()
        _sweepFace.append(cara_min)
        
        # Mallado desde la cara más pequeña
        result = apex.mesh.createHexMesh(
            name = "",
            target = _target,
            meshSize = 0.2,
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



_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
solid_1 = part_1.getSolid( name = "P_Inferior_Interior" )
_target.append( solid_1 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.5,
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

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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

_target = apex.EntityCollection()
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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

_target = apex.EntityCollection()
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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

_target = apex.EntityCollection()
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_6 = part_6.getSolid( name = "PartBody" )
_target.append( solid_6 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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

_target = apex.EntityCollection()
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_7 = part_7.getSolid( name = "Body.6" )
_target.append( solid_7 )
_SweepFace = apex.EntityCollection()
result = apex.mesh.createHexMesh(
    name = "",
    target = _target,
    meshSize = 0.2,
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