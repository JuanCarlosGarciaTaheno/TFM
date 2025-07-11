# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 09:28:48
# 
# Macro Name = MeshSeed_PiezaSup
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

geomes_1 = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_1 = part_1.getSolid( name = "PartBody" )
_ids = '110114'
geomes_1.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_1,
    numberElementEdges = 6
)

geomes_2 = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_1 = part_1.getSolid( name = "PartBody" )
_ids = '3969168, 3969167, 110028, 110022, 110117, 110114, 110204, 110207'
geomes_2.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_2,
    numberElementEdges = 6
)

geomes_3 = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_1 = part_1.getSolid( name = "PartBody" )
_ids = '19931'
geomes_3.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_3,
    numberElementEdges = 3
)

part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
part_2.hide()

part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
part_3.hide()

geomes_4 = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_1 = part_1.getSolid( name = "PartBody" )
_ids = '3969104'
geomes_4.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_4,
    numberElementEdges = 6
)

geomes_5 = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_1 = part_1.getSolid( name = "PartBody" )
_ids = '3969133, 3969104, 110024, 110025, 110111, 110115, 110205, 110201'
geomes_5.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_5,
    numberElementEdges = 6
)

# 
# Macro recording stopped on Jun 12, 2025 at 09:30:19
# 
