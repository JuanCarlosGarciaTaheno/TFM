# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 18:20:25
# 
# Macro Name = MeshSeed_PinfTop_0p2mm
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

assembly_1 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex" )
assembly_1.hide()

part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
part_1.show()

geomes_1 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_1 = part_2.getSolid( name = "Original_PSuperior" )
_ids = '1357'
geomes_1.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_1,
    numberElementEdges = 10
)

geomes_2 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_1 = part_2.getSolid( name = "Original_PSuperior" )
_ids = '1625'
geomes_2.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_2,
    numberElementEdges = 6
)

geomes_3 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_1 = part_2.getSolid( name = "Original_PSuperior" )
_ids = '39143'
geomes_3.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_3,
    numberElementEdges = 6
)

geomes_4 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_1 = part_2.getSolid( name = "Original_PSuperior" )
_ids = '1351'
geomes_4.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByLength(
    target = geomes_4,
    elementEdgeLength = 0.2
)

# 
# Macro recording stopped on Jun 12, 2025 at 18:23:39
# 
