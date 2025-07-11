# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 18, 2025 at 13:19:16
# 
# Macro Name = NODOINTRBE
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

nodes_1 = apex.getNodes(
    [{"path": apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody", "ids": "701460-701460"}]
)
result = apex.mesh.renumberByStartId(
    target = nodes_1,
    startNodeId = 1,
    startElementId = 1,
    startCoordinateSystem = 1
)

assembly_1 = apex.getAssembly( pathName = apex.currentModel().name )
assembly_1.hide()

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Product1" )
assembly_2.show()

# 
# Macro recording stopped on Jun 18, 2025 at 13:20:28
# 
