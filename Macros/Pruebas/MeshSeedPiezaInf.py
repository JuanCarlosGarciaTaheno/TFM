# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 18:02:03
# 
# Macro Name = 
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

part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
part_1.show()

geomes_1 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '23411'
geomes_1.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_1,
    numberElementEdges = 10
)

geomes_2 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '1615'
geomes_2.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_2,
    numberElementEdges = 6
)

geomes_3 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '38111, 38141, 1344, 1342, 1438, 1434, 1525, 1521,' \
       '1611, 1615'
geomes_3.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_3,
    numberElementEdges = 6
)

geomes_4 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '38173'
geomes_4.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_4,
    numberElementEdges = 6
)

geomes_5 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '38174, 38173, 1432, 1436, 1523, 1527, 1617, 1614'
geomes_5.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_5,
    numberElementEdges = 6
)

geomes_6 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '846'
geomes_6.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_6,
    numberElementEdges = 6
)

geomes_7 = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_1 = part_2.getSolid( name = "P_InterMed" )
_ids = '846, 818, 1431, 1437, 1524, 1528, 1618, 1612'
geomes_7.extend( solid_1.getEdges( ids = _ids ) )
result = apex.mesh.createEdgeSeedUniformByNumber(
    target = geomes_7,
    numberElementEdges = 6
)

# 
# Macro recording stopped on Jun 12, 2025 at 18:02:41
# 
