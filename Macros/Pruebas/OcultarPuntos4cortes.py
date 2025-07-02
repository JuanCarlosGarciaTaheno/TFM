# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 08:54:47
# 
# Macro Name = Puntos
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

def doSketch_1():
    part_1 = model_1.getCurrentPart()
    if part_1 is None:
        part_1 = model_1.createPart()
    sketch_1 = part_1.createSketchOnGlobalPlane(
        name = 'Sketch 1',
        plane = apex.construct.GlobalPlane.XY,
        alignSketchViewWithViewport = True
    )


    sketchpoint_1 = sketch_1.createPoint(
        name = "Sketchpoint 1",
        location = Point2D( 2.000000000000000e+01, 0.0 )
    )

    sketchpoint_2 = sketch_1.createPoint(
        name = "Sketchpoint 2",
        location = Point2D( 2.000000000000000e+01, 2.000000000000000e+01 )
    )

    sketchpoint_3 = sketch_1.createPoint(
        name = "Sketchpoint 3",
        location = Point2D( 0.0, 2.000000000000000e+01 )
    )

    sketchpoint_4 = sketch_1.createPoint(
        name = "Sketchpoint 4",
        location = Point2D( -2.000000000000000e+01, 2.000000000000000e+01 )
    )

    sketchpoint_5 = sketch_1.createPoint(
        name = "Sketchpoint 5",
        location = Point2D( -2.000000000000000e+01, 0.0 )
    )

    sketchpoint_6 = sketch_1.createPoint(
        name = "Sketchpoint 6",
        location = Point2D( -2.000000000000000e+01, -2.000000000000000e+01 )
    )

    sketchpoint_7 = sketch_1.createPoint(
        name = "Sketchpoint 7",
        location = Point2D( 0.0, -2.000000000000000e+01 )
    )

    sketchpoint_8 = sketch_1.createPoint(
        name = "Sketchpoint 8",
        location = Point2D( 2.000000000000000e+01, -2.000000000000000e+01 )
    )

    return sketch_1.completeSketch( fillSketches = True )

newbodies = doSketch_1()


def doSketch_2():
    part_1 = model_1.getCurrentPart()
    if part_1 is None:
        part_1 = model_1.createPart()
    sketch_2 = part_1.createSketchOnGlobalPlane(
        name = 'Sketch 2',
        plane = apex.construct.GlobalPlane.ZX,
        alignSketchViewWithViewport = True
    )


    sketchpoint_9 = sketch_2.createPoint(
        name = "Sketchpoint 9",
        location = Point2D( -4.000000000000000e+01, 0.0 )
    )

    return sketch_2.completeSketch( fillSketches = True )

newbodies = doSketch_2()


part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
part_2.hide()

solid_1 = apex.getSolid( pathName = apex.currentModel().name+"/Union_Apex/Product1.1/RestoPiezaInferior/P_Inferior_Interior" )
solid_1.hide()

solid_2 = apex.getSolid( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca.1/Body.6" )
solid_2.hide()

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca.1" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo.2" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil.1" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
solid_6 = part_6.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_7 = part_7.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RoscaPiezaInferior" )
solid_8 = part_8.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
solid_9 = part_9.getSolid( name = "Original_PSuperior" )
_target.append( solid_9 )
solid_10 = part_9.getSolid( name = "P_InterMed" )
_target.append( solid_10 )
solid_11 = part_9.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_11 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca.1" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo.2" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil.1" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
solid_6 = part_6.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_7 = part_7.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RoscaPiezaInferior" )
solid_8 = part_8.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
solid_9 = part_9.getSolid( name = "Original_PSuperior" )
_target.append( solid_9 )
solid_10 = part_9.getSolid( name = "P_InterMed" )
_target.append( solid_10 )
solid_11 = part_9.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_11 )
_locations = [
    apex.Coordinate( 0.0, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca.1" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo.2" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil.1" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
solid_6 = part_6.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_7 = part_7.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RoscaPiezaInferior" )
solid_8 = part_8.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
solid_9 = part_9.getSolid( name = "Original_PSuperior" )
_target.append( solid_9 )
solid_10 = part_9.getSolid( name = "P_InterMed" )
_target.append( solid_10 )
solid_11 = part_9.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_11 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca.1" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo.2" )
solid_4 = part_4.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil.1" )
solid_5 = part_5.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela.1" )
solid_6 = part_6.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior" )
solid_7 = part_7.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RoscaPiezaInferior" )
solid_8 = part_8.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
solid_9 = part_9.getSolid( name = "Original_PSuperior" )
_target.append( solid_9 )
solid_10 = part_9.getSolid( name = "P_InterMed" )
_target.append( solid_10 )
solid_11 = part_9.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_11 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, -2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 2.000000000000000e+01, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
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
# Macro recording stopped on Jun 12, 2025 at 09:02:18
# 



_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1.1/RestoPiezaInferior" )
solid_1 = part_1.getSolid( name = "P_Inferior_Interior" )
_target.append( solid_1 )
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 0.0, 0.0, -4.000000000000000e+01 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)