# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 09:20:15
# 
# Macro Name = CorteCabeza
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
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
solid_1 = part_1.getSolid( name = "PartBody" )
_target.append( solid_1 )
_locations = [
    apex.Coordinate( 9.260726110075224e-01, 7.740631863809716e-02, 1.820000000000000 ),
    apex.Coordinate( 9.260726110075224e-01, 7.740631863809716e-02, 1.000182000000000e+04 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

# 
# Macro recording stopped on Jun 12, 2025 at 09:20:55
# 
