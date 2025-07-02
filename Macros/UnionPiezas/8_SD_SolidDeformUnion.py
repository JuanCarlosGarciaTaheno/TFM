# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 14:51:21
# 
# Macro Name = SD_SolidDeform
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

contactbodyproperty_1 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_1 = apex.EntityCollection()
propertieselement3d_1 = apex.catalog.getPropertiesElement3D( name = "Tornillo" )
entities_1.append(propertieselement3d_1)
_target.extend( entities_1 )
contactbody_1 = apex.attribute.createContactBody(
    name = 'SDTornillo',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_1,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)

contactbodyproperty_2 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_2 = apex.EntityCollection()
propertieselement3d_2 = apex.catalog.getPropertiesElement3D( name = "Arandela" )
entities_2.append(propertieselement3d_2)
_target.extend( entities_2 )
contactbody_2 = apex.attribute.createContactBody(
    name = 'SD_Arandela',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_2,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)

contactbodyproperty_3 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_3 = apex.EntityCollection()
propertieselement3d_3 = apex.catalog.getPropertiesElement3D( name = "PiezaSuperior" )
entities_3.append(propertieselement3d_3)
_target.extend( entities_3 )
contactbody_3 = apex.attribute.createContactBody(
    name = 'SD_PiezaSuperior',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_3,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)



contactbodyproperty_5 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_5 = apex.EntityCollection()
propertieselement3d_5 = apex.catalog.getPropertiesElement3D( name = "PiezaInferior" )
entities_5.append(propertieselement3d_5)
_target.extend( entities_5 )
contactbody_5 = apex.attribute.createContactBody(
    name = 'SD_PiezaInferior',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_5,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)



contactbodyproperty_10 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_10 = apex.EntityCollection()
propertieselement3d_10 = apex.catalog.getPropertiesElement3D( name = "Helicoil" )
entities_10.append(propertieselement3d_10)
_target.extend( entities_10 )
contactbody_10 = apex.attribute.createContactBody(
    name = 'SD_Helicoil',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_10,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)

contactbodyproperty_11 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_11 = apex.EntityCollection()
propertieselement3d_11 = apex.catalog.getPropertiesElement3D( name = "RoscaTornillo" )
entities_11.append(propertieselement3d_11)
_target.extend( entities_11 )
contactbody_11 = apex.attribute.createContactBody(
    name = 'SD_RoscaTornillo',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_11,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)

contactbodyproperty_12 = apex.attribute.createContactBodyProperty(
    smoothingState = False,
    shellLayer = apex.attribute.ShellLayer.TopAndButtom,
    ignoreShellThickness = False,
)
_target = apex.EntityCollection()
entities_12 = apex.EntityCollection()
propertieselement3d_12 = apex.catalog.getPropertiesElement3D( name = "RoscaPiezaInferior" )
entities_12.append(propertieselement3d_12)
_target.extend( entities_12 )
contactbody_12 = apex.attribute.createContactBody(
    name = 'SD_RoscaPiezaInferior',
    description = '',
    bodyType = apex.attribute.ContactBodyType.Deform,
    target = _target,
    bodyProperty = contactbodyproperty_12,
    contactResultCalculation = apex.attribute.ContactResultCalculation.EstimatedCentroid,
)

# 
# Macro recording stopped on Jun 13, 2025 at 14:54:33
# 
