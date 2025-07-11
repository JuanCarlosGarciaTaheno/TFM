# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 11, 2025 at 21:00:42
# 
# Macro Name = 
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

# import apex
# from apex.construct import Point3D, Point2D

# apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N-K''')
# applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
# applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
# applicationSettingsGeometry.geometryTessellationIsWatertight = True
# applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
# applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
# apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
# applicationSettingsStudy = apex.setting.ApplicationSettingsStudy(useNewScenario = False,displayPrereleaseScenario = False)
# apex.setting.setApplicationSettingsStudy(applicationSettingsStudy = applicationSettingsStudy)
# model_1 = apex.currentModel()

# # 
# # Start of recorded operations
# # 

# _target = apex.EntityCollection()
# part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca.1" )
# solid_1 = part_1.getSolid( name = "PartBody" )
# _target.append( solid_1 )
# part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo.2" )
# solid_2 = part_2.getSolid( name = "PartBody" )
# _target.append( solid_2 )
# curve_1 = part_2.getCurve( name = "EjeReferencia" )
# _target.append( curve_1 )
# curve_2 = part_2.getCurve( name = "Rosca" )
# _target.append( curve_2 )
# curve_3 = part_2.getCurve( name = "Rosca (2)" )
# _target.append( curve_3 )
# curve_4 = part_2.getCurve( name = "Rosca (3)" )
# _target.append( curve_4 )
# curve_5 = part_2.getCurve( name = "Rosca (4)" )
# _target.append( curve_5 )
# part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil.1" )
# solid_3 = part_3.getSolid( name = "PartBody" )
# _target.append( solid_3 )
# curve_6 = part_3.getCurve( name = "Helicoil" )
# _target.append( curve_6 )
# curve_7 = part_3.getCurve( name = "Helicoil (2)" )
# _target.append( curve_7 )
# curve_8 = part_3.getCurve( name = "Helicoil (3)" )
# _target.append( curve_8 )
# curve_9 = part_3.getCurve( name = "Helicoil (4)" )
# _target.append( curve_9 )
# curve_10 = part_3.getCurve( name = "Helicoil (5)" )
# _target.append( curve_10 )
# curve_11 = part_3.getCurve( name = "Helicoil (6)" )
# _target.append( curve_11 )
# curve_12 = part_3.getCurve( name = "Helicoil (7)" )
# _target.append( curve_12 )
# curve_13 = part_3.getCurve( name = "Helicoil (8)" )
# _target.append( curve_13 )
# curve_14 = part_3.getCurve( name = "Helicoil (9)" )
# _target.append( curve_14 )
# curve_15 = part_3.getCurve( name = "Helicoil (10)" )
# _target.append( curve_15 )
# curve_16 = part_3.getCurve( name = "Helicoil (11)" )
# _target.append( curve_16 )
# part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
# solid_4 = part_4.getSolid( name = "PartBody" )
# _target.append( solid_4 )
# part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
# solid_5 = part_5.getSolid( name = "PartBody" )
# _target.append( solid_5 )
# part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RoscaPiezaInferior" )
# solid_6 = part_6.getSolid( name = "PartBody" )
# _target.append( solid_6 )
# curve_17 = part_6.getCurve( name = "RoscaExterior" )
# _target.append( curve_17 )
# curve_18 = part_6.getCurve( name = "RoscaExterior (2)" )
# _target.append( curve_18 )
# curve_19 = part_6.getCurve( name = "RoscaExterior (3)" )
# _target.append( curve_19 )
# curve_20 = part_6.getCurve( name = "RoscaExterior (4)" )
# _target.append( curve_20 )
# part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
# solid_7 = part_7.getSolid( name = "Original_PSuperior" )
# _target.append( solid_7 )
# solid_8 = part_7.getSolid( name = "P_InterMed" )
# _target.append( solid_8 )
# solid_9 = part_7.getSolid( name = "P_Inferior_Exterior" )
# _target.append( solid_9 )
# curve_21 = part_7.getCurve( name = "Curve.3" )
# _target.append( curve_21 )
# _location = apex.Coordinate( -8.000000000000000, 0.0, -7.999999999740801e-01 )
# part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
# solid_5 = part_5.getSolid( name = "PartBody" )
# _snapEntity = solid_5.getEdge( id = 3899168 )
# result = apex.geometry.splitOnFeaturePlane(
#     target = _target,
#     location = _location,
#     snapEntity = _snapEntity,
#     splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
# )

# 
# Macro recording stopped on Jun 11, 2025 at 21:01:34
# 


import apex
from apex.construct import Point3D

apex.setScriptUnitSystem(unitSystemName='mm-kg-s-N-K')
model = apex.currentModel()

# Obtener sólido base para snapEntity
part_ref = apex.getPart(pathName=model.name + "/Union_Apex/PiezaSuperior")
solid_ref = part_ref.getSolid(name="PartBody")
snap_entity = solid_ref.getEdge(id=3899168)

# Coordenadas de corte (puedes cambiar estas)
cut_locations = [
    apex.Coordinate(-8.0, 0.0, 0),  # la que ya funcionó
    apex.Coordinate(0.0, 8.0, 0.0),
    apex.Coordinate(4.0, 4.0, 0.0),
    apex.Coordinate(-4.0, 4.0, 0.0),
]

# Cargar todos los sólidos objetivo
def get_solid(model_path, solid_name="PartBody"):
    part = apex.getPart(pathName=model.name + model_path)
    return part.getSolid(name=solid_name)

solids = [
    get_solid("/Union_Apex/Tornillo_Sin_Rosca.1"),
    get_solid("/Union_Apex/Rosca_Exterior_Tornillo.2"),
    get_solid("/Union_Apex/Helicoil.1"),
    get_solid("/Union_Apex/Arandela.1"),
    get_solid("/Union_Apex/PiezaSuperior"),
    get_solid("/Union_Apex/Product1.1/RoscaPiezaInferior"),
    get_solid("/Union_Apex/Product1.1/RestoPiezaInferior", "Original_PSuperior"),
    get_solid("/Union_Apex/Product1.1/RestoPiezaInferior", "P_InterMed"),
    get_solid("/Union_Apex/Product1.1/RestoPiezaInferior", "P_Inferior_Exterior")
]

# Inicializar la colección target
target = apex.EntityCollection()
for solid in solids:
    target.append(solid)

# Aplicar los cortes uno por uno
for idx, location in enumerate(cut_locations):
    try:
        print(f"Haciendo corte {idx+1} en {location}")
        target = apex.geometry.splitOnFeaturePlane(
            target=target,
            location=location,
            snapEntity=snap_entity,
            splitBehavior=apex.geometry.GeometrySplitBehavior.Partition
        )
    except RuntimeError as e:
        print(f"⚠️ Error en corte {idx+1}: {e}")
        # Continuamos con los sólidos que sí se puedan
        continue
