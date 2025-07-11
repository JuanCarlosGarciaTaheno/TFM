# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 18, 2025 at 13:12:22
# 
# Macro Name = Renumber
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
entities_1 = apex.EntityCollection()
assembly_1 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex" )
entities_1.append(assembly_1)
result = apex.mesh.renumberByStartId(
    target = entities_1,
    startNodeId = 800000,
    startElementId = 800000
)

entities_1 = apex.EntityCollection()
assembly_1 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
entities_1.append(assembly_1)
result = apex.mesh.renumberByStartId(
    target = entities_1,
    startNodeId = 700000,
    startElementId = 700000
)

entities_2 = apex.EntityCollection()
assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Arandela" )
entities_2.append(assembly_2)
result = apex.mesh.renumberByStartId(
    target = entities_2,
    startNodeId = 600000,
    startElementId = 600000
)

entities_3 = apex.EntityCollection()
assembly_3 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1" )
entities_3.append(assembly_3)
result = apex.mesh.renumberByStartId(
    target = entities_3,
    startNodeId = 500000,
    startElementId = 500000
)

entities_4 = apex.EntityCollection()
assembly_4 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior" )
entities_4.append(assembly_4)
result = apex.mesh.renumberByStartId(
    target = entities_4,
    startNodeId = 400000,
    startElementId = 400000
)

entities_5 = apex.EntityCollection()
assembly_5 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Helicoil" )
entities_5.append(assembly_5)
result = apex.mesh.renumberByStartId(
    target = entities_5,
    startNodeId = 300000,
    startElementId = 300000
)

entities_6 = apex.EntityCollection()
assembly_6 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo" )
entities_6.append(assembly_6)
result = apex.mesh.renumberByStartId(
    target = entities_6,
    startNodeId = 200000,
    startElementId = 200000
)

entities_7 = apex.EntityCollection()
assembly_7 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior" )
entities_7.append(assembly_7)
result = apex.mesh.renumberByStartId(
    target = entities_7,
    startNodeId = 100000,
    startElementId = 100000,
    conflictResolveMethod = apex.mesh.IDConflictResolveMethod.ResolveAuto
)



