# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 10:29:19
# 
# Macro Name = MESHSIZE
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
assembly_1.show()

_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_1.getSolid( name = "P_Inferior_Exterior" )
_ids = '75, 1331, 1421, 1422, 1512, 1511, 1602, 1601'
_target.extend( solid_1.getCells( ids = _ids ) )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
solid_2 = part_2.getSolid( name = "P_Inferior_Interior" )
_ids = '1125, 1651'
_target.extend( solid_2.getCells( ids = _ids ) )
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_3 = part_3.getSolid( name = "P_InterMed" )
_ids = '85, 1341, 1431, 1432, 1522, 1521, 1612, 1611'
_target.extend( solid_3.getCells( ids = _ids ) )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_4 = part_4.getSolid( name = "Original_PSuperior" )
_ids = '95, 1351, 1441, 1442, 1532, 1531, 1622, 1621'
_target.extend( solid_4.getCells( ids = _ids ) )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_5 = part_5.getSolid( name = "PartBody" )
_ids = '25, 23029, 23016, 1304, 23015, 1305, 23017, 1306,' \
       '23018, 1307, 23019, 1308, 23020, 1309, 23021, 23010,' \
       '23022, 1301, 23026, 23011, 23023, 23012, 23027, 1302,' \
       '23024, 23013, 23025, 23014, 23028, 1303, 23928, 23917,' \
       '23914, 23918, 1392, 23919, 1393, 23920, 1394, 23921,' \
       '1395, 23922, 1396, 23923, 1397, 23915, 23911, 23924,' \
       '1398, 23925, 23912, 23916, 1399, 23926, 23910, 23927,' \
       '1391, 23913, 23929, 1484, 24816, 24818, 24815, 24819,' \
       '1485, 24820, 1486, 24821, 1487, 24822, 1488, 24823,' \
       '1489, 24824, 24810, 24829, 1481, 24825, 24811, 24826,' \
       '1482, 24830, 24812, 24827, 24813, 24828, 1483, 24817,' \
       '24814, 25728, 1571, 25715, 1572, 25716, 1573, 25717,' \
       '1574, 25718, 1575, 25719, 1576, 25720, 1577, 25721,' \
       '1578, 25722, 1579, 25723, 25710, 25724, 25711, 25725,' \
       '25712, 25726, 25713, 25727, 25714, 25729'
_target.extend( solid_5.getCells( ids = _ids ) )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_6 = part_6.getSolid( name = "PartBody" )
_ids = '1105, 1361, 1451, 1452, 1542, 1541, 1632, 1631'
_target.extend( solid_6.getCells( ids = _ids ) )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_7 = part_7.getSolid( name = "PartBody" )
_ids = '1115, 1371, 1461, 1462, 1552, 1551, 1641, 1642'
_target.extend( solid_7.getCells( ids = _ids ) )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_8 = part_8.getSolid( name = "PartBody" )
_ids = '5, 22920, 22911, 1291, 22912, 1292, 22913, 1293,' \
       '22914, 1294, 22915, 1295, 22916, 1296, 22910, 1297,' \
       '22917, 1298, 22918, 1299, 22919, 1389, 23821, 23813,' \
       '1381, 23814, 1382, 23815, 1383, 23816, 1384, 23811,' \
       '1385, 23812, 1386, 23817, 23810, 23818, 1387, 23819,' \
       '1388, 23820, 24720, 24710, 24721, 24711, 1471, 24712,' \
       '1472, 24713, 1473, 24714, 1474, 24715, 1475, 24716,' \
       '1476, 24717, 1477, 24718, 1478, 24719, 1479, 25620,' \
       '1561, 1562, 25612, 1563, 25613, 1564, 25614, 1565,' \
       '25615, 1566, 25616, 1567, 25617, 1568, 25618, 1569,' \
       '25619, 25610, 25621, 25611'
_target.extend( solid_8.getCells( ids = _ids ) )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_9 = part_9.getSolid( name = "PartBody" )
_ids = '35, 23126, 23114, 1311, 23115, 1312, 23113, 1313,' \
       '23116, 23112, 23117, 1314, 23118, 1315, 23119, 1316,' \
       '23120, 1317, 23121, 1318, 23122, 23125, 23111, 23124,' \
       '23110, 23123, 1319, 24022, 24014, 1404, 24015, 24012,' \
       '24016, 1405, 24013, 1406, 24017, 1407, 24018, 1408,' \
       '24019, 1409, 24020, 24010, 24021, 1401, 24011, 24025,' \
       '1403, 24024, 1402, 24023, 1491, 24917, 24920, 1492,' \
       '24921, 24912, 24922, 1493, 24918, 1494, 24919, 1495,' \
       '24923, 24911, 24924, 1496, 24925, 1497, 24926, 1498,' \
       '24915, 24910, 24914, 24913, 24916, 1499, 25822, 1582,' \
       '25814, 1583, 25815, 1584, 25816, 1585, 25817, 25812,' \
       '25818, 1586, 25813, 1587, 25819, 1588, 25820, 1589,' \
       '25821, 25810, 25823, 25825, 1581, 25824, 25811'
_target.extend( solid_9.getCells( ids = _ids ) )
part_10 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
solid_10 = part_10.getSolid( name = "PartBody" )
_ids = '55, 1852'
_target.extend( solid_10.getCells( ids = _ids ) )
part_11 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_11 = part_11.getSolid( name = "Body.6" )
_ids = '65'
_target.extend( solid_11.getCells( ids = _ids ) )
part_12 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_12 = part_12.getSolid( name = "PartBody" )
_ids = '45, 1321, 1411, 1412, 1502, 1501, 1591, 1592'
_target.extend( solid_12.getCells( ids = _ids ) )
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

# 
# Macro recording stopped on Jun 13, 2025 at 10:31:10
# 
