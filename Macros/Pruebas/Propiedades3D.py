# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 14:25:54
# 
# Macro Name = propiedades3D
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

propertyelement3d_1 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_1 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 1" )
propertyelement3d_1.update(
    name = 'Cabeza',
)

propertyelement3d_2 = apex.catalog.getPropertiesElement3D( name = "Cabeza" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_2 )

_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" ))
propertyelement3d_2.update(target = _target)

propertyelement3d_3 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_3 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 2" )
propertyelement3d_3.update(
    name = 'Arandela',
)

propertyelement3d_4 = apex.catalog.getPropertiesElement3D( name = "Arandela" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_4 )

propertyelement3d_5 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_5 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 3" )
propertyelement3d_5.update(
    name = 'PiezaSuperior',
)

propertyelement3d_6 = apex.catalog.getPropertiesElement3D( name = "PiezaSuperior" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_6 )

propertyelement3d_7 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_7 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 4" )
propertyelement3d_7.update(
    name = 'PiezaInferiorMed',
)

propertyelement3d_8 = apex.catalog.getPropertiesElement3D( name = "PiezaInferiorMed" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_8 )

_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_8 )

propertyelement3d_9 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_9 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 5" )
propertyelement3d_9.update(
    name = 'PiezaInferiorTop',
)

propertyelement3d_10 = apex.catalog.getPropertiesElement3D( name = "PiezaInferiorTop" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_10 )

propertyelement3d_11 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_11 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 6" )
propertyelement3d_11.update(
    name = 'PiezaInfLowCilindro',
)

propertyelement3d_12 = apex.catalog.getPropertiesElement3D( name = "PiezaInfLowCilindro" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_12 )

propertyelement3d_13 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_13 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 7" )
propertyelement3d_13.update(
    name = 'PiezaInfLow',
)

propertyelement3d_14 = apex.catalog.getPropertiesElement3D( name = "PiezaInfLow" )
_target = apex.EntityCollection()
_target.append( apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" ))
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_14 )

propertyelement3d_15 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_15 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 8" )
propertyelement3d_15.update(
    name = 'CuerpoExteriorTornillo',
)

assembly_1 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex" )
assembly_1.hide()

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca" )
assembly_2.show()

propertyelement3d_16 = apex.catalog.getPropertiesElement3D( name = "CuerpoExteriorTornillo" )
_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_1 = part_1.getSolid( name = "PartBody" )
_geoms.append( solid_1 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_16 )

propertyelement3d_17 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_17 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 9" )
propertyelement3d_17.update(
    name = 'CuerpoInteriorTornillo',
)

propertyelement3d_18 = apex.catalog.getPropertiesElement3D( name = "CuerpoInteriorTornillo" )
_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_2 = part_2.getSolid( name = "Body.6" )
_geoms.append( solid_2 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_18 )

_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_2 = part_2.getSolid( name = "Body.6" )
_geoms.append( solid_2 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_18 )

propertyelement3d_19 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_19 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 10" )
propertyelement3d_19.update(
    name = 'Helicoil',
)

assembly_3 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Helicoil" )
assembly_3.show()

propertyelement3d_20 = apex.catalog.getPropertiesElement3D( name = "Helicoil" )
_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_3 = part_3.getSolid( name = "PartBody" )
_geoms.append( solid_3 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_20 )

assembly_4 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo" )
assembly_4.show()

assembly_5 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior" )
assembly_5.show()

propertyelement3d_21 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_21 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 11" )
propertyelement3d_21.update(
    name = 'RoscaTornillo',
)

propertyelement3d_22 = apex.catalog.getPropertiesElement3D( name = "RoscaTornillo" )
_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_4 = part_4.getSolid( name = "PartBody" )
_geoms.append( solid_4 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_22 )

propertyelement3d_23 = apex.catalog.createPropertiesElement3D(
    name = '3D Element Property',
    primaryProperties3D = 'PSOLID',
)

propertyelement3d_23 = apex.catalog.getPropertiesElement3D( name = "3D Element Property 12" )
propertyelement3d_23.update(
    name = 'RoscaPiezaInferior',
)

propertyelement3d_24 = apex.catalog.getPropertiesElement3D( name = "RoscaPiezaInferior" )
_target = apex.EntityCollection()
_geoms = apex.EntityCollection()
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_5 = part_5.getSolid( name = "PartBody" )
_geoms.append( solid_5 )
_target.extend( _geoms )
apex.attribute.assignPropertiesElement3D(target = _target, property = propertyelement3d_24 )

# 
# Macro recording stopped on Jun 13, 2025 at 14:38:10
# 
