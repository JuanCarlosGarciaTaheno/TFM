# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 09:54:33
# 
# Macro Name = MacroParaStep
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D
import math
from collections import defaultdict

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
        location = Point2D( -2.000000000000000e+01, 2.000000000000000e+01 )
    )

    sketchpoint_2 = sketch_1.createPoint(
        name = "Sketchpoint 2",
        location = Point2D( 0.0, 2.000000000000000e+01 )
    )

    sketchpoint_3 = sketch_1.createPoint(
        name = "Sketchpoint 3",
        location = Point2D( 2.000000000000000e+01, 2.000000000000000e+01 )
    )

    sketchpoint_4 = sketch_1.createPoint(
        name = "Sketchpoint 4",
        location = Point2D( 2.000000000000000e+01, 0.0 )
    )

    sketchpoint_5 = sketch_1.createPoint(
        name = "Sketchpoint 5",
        location = Point2D( 2.000000000000000e+01, -2.000000000000000e+01 )
    )

    sketchpoint_6 = sketch_1.createPoint(
        name = "Sketchpoint 6",
        location = Point2D( 0.0, -2.000000000000000e+01 )
    )

    sketchpoint_7 = sketch_1.createPoint(
        name = "Sketchpoint 7",
        location = Point2D( -2.000000000000000e+01, -2.000000000000000e+01 )
    )

    sketchpoint_8 = sketch_1.createPoint(
        name = "Sketchpoint 8",
        location = Point2D( -2.000000000000000e+01, 0.0 )
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


assembly_1 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
assembly_1.hide()

part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
part_2.hide()

part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
part_3.hide()

_target = apex.EntityCollection()
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Part 1" )
curve_1 = part_4.getCurve( name = "Curve.3" )
_target.append( curve_1 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_5.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_1 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_2 = part_6.getSolid( name = "P_InterMed" )
_target.append( solid_2 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_3 = part_7.getSolid( name = "Original_PSuperior" )
_target.append( solid_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_2 = part_8.getCurve( name = "RoscaExterior" )
_target.append( curve_2 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_4 = part_9.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_10 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_5 = part_10.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_11 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_6 = part_11.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_12 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_3 = part_12.getCurve( name = "Helicoil" )
_target.append( curve_3 )
part_13 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_7 = part_13.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_14 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_4 = part_14.getCurve( name = "Rosca" )
_target.append( curve_4 )
part_15 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_5 = part_15.getCurve( name = "EjeReferencia" )
_target.append( curve_5 )
part_16 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_8 = part_16.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_17 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_9 = part_17.getSolid( name = "PartBody" )
_target.append( solid_9 )
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
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Part 1" )
curve_1 = part_4.getCurve( name = "Curve.3" )
_target.append( curve_1 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_5.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_1 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_2 = part_6.getSolid( name = "P_InterMed" )
_target.append( solid_2 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_3 = part_7.getSolid( name = "Original_PSuperior" )
_target.append( solid_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_2 = part_8.getCurve( name = "RoscaExterior" )
_target.append( curve_2 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_4 = part_9.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_10 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_5 = part_10.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_11 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_6 = part_11.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_12 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_3 = part_12.getCurve( name = "Helicoil" )
_target.append( curve_3 )
part_13 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_7 = part_13.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_14 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_4 = part_14.getCurve( name = "Rosca" )
_target.append( curve_4 )
part_15 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_5 = part_15.getCurve( name = "EjeReferencia" )
_target.append( curve_5 )
part_16 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_8 = part_16.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_17 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_9 = part_17.getSolid( name = "PartBody" )
_target.append( solid_9 )
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
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Part 1" )
curve_1 = part_4.getCurve( name = "Curve.3" )
_target.append( curve_1 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_5.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_1 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_2 = part_6.getSolid( name = "P_InterMed" )
_target.append( solid_2 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_3 = part_7.getSolid( name = "Original_PSuperior" )
_target.append( solid_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_2 = part_8.getCurve( name = "RoscaExterior" )
_target.append( curve_2 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_4 = part_9.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_10 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_5 = part_10.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_11 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_6 = part_11.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_12 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_3 = part_12.getCurve( name = "Helicoil" )
_target.append( curve_3 )
part_13 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_7 = part_13.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_14 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_4 = part_14.getCurve( name = "Rosca" )
_target.append( curve_4 )
part_15 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_5 = part_15.getCurve( name = "EjeReferencia" )
_target.append( curve_5 )
part_16 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_8 = part_16.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_17 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_9 = part_17.getSolid( name = "PartBody" )
_target.append( solid_9 )
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
part_4 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Part 1" )
curve_1 = part_4.getCurve( name = "Curve.3" )
_target.append( curve_1 )
part_5 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid_1 = part_5.getSolid( name = "P_Inferior_Exterior" )
_target.append( solid_1 )
part_6 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid_2 = part_6.getSolid( name = "P_InterMed" )
_target.append( solid_2 )
part_7 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid_3 = part_7.getSolid( name = "Original_PSuperior" )
_target.append( solid_3 )
part_8 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/RoscaExterior" )
curve_2 = part_8.getCurve( name = "RoscaExterior" )
_target.append( curve_2 )
part_9 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid_4 = part_9.getSolid( name = "PartBody" )
_target.append( solid_4 )
part_10 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody" )
solid_5 = part_10.getSolid( name = "PartBody" )
_target.append( solid_5 )
part_11 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Arandela/PartBody" )
solid_6 = part_11.getSolid( name = "PartBody" )
_target.append( solid_6 )
part_12 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/Helicoil" )
curve_3 = part_12.getCurve( name = "Helicoil" )
_target.append( curve_3 )
part_13 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid_7 = part_13.getSolid( name = "PartBody" )
_target.append( solid_7 )
part_14 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/Rosca" )
curve_4 = part_14.getCurve( name = "Rosca" )
_target.append( curve_4 )
part_15 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/EjeReferencia" )
curve_5 = part_15.getCurve( name = "EjeReferencia" )
_target.append( curve_5 )
part_16 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid_8 = part_16.getSolid( name = "PartBody" )
_target.append( solid_8 )
part_17 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_9 = part_17.getSolid( name = "PartBody" )
_target.append( solid_9 )
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

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex" )
assembly_2.hide()

part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
part_3.show()

point_1 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 1" )
point_1.show()

point_2 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 2" )
point_2.show()

point_3 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 3" )
point_3.show()

point_4 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 4" )
point_4.show()

point_5 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 5" )
point_5.show()

point_6 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 6" )
point_6.show()

point_7 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 7" )
point_7.show()

point_8 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 8" )
point_8.show()

point_9 = apex.getPoint( pathName = apex.currentModel().name+"/Union_Apex/Tornillo_Sin_Rosca/PartBody/Point 9" )
point_9.show()

_target = apex.EntityCollection()
part_18 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
solid_10 = part_18.getSolid( name = "P_Inferior_Interior" )
_target.append( solid_10 )
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

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex" )
assembly_2.show()


# ================================================================================
#
#
#
#                     ELIMINACION DE VERTICES FUERA DEL PLANO:
#
#                               Cuerpo del tornillo
#                                     Arandela
#                                  Pieza Inf Medio
#
#
#
# ================================================================================

def get_plane_normal(p1, p2, p3):
    """Devuelve el vector normal de un plano definido por tres puntos."""
    u = [p2.x - p1.x, p2.y - p1.y, p2.z - p1.z]
    v = [p3.x - p1.x, p3.y - p1.y, p3.z - p1.z]
    return [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ]

def point_plane_distance(p, plane_point, normal):
    """Calcula la distancia signed de un punto a un plano."""
    return (
        normal[0]*(p[0] - plane_point.x) +
        normal[1]*(p[1] - plane_point.y) +
        normal[2]*(p[2] - plane_point.z)
    )

# ---------------------- PLANOS ----------------------
planos = []
# Plano 1
plano_1_pts = [
    apex.Coordinate(-20.0, 0.0, 0.0),
    apex.Coordinate( 20.0, 0.0, 0.0),
    apex.Coordinate( 0.0, 0.0, -40.0)
]
planos.append((plano_1_pts[0], get_plane_normal(*plano_1_pts)))

# Plano 2
plano_2_pts = [
    apex.Coordinate(0.0, -20.0, 0.0),
    apex.Coordinate(0.0, 20.0, 0.0),
    apex.Coordinate(0.0, 0.0, -40.0)
]
planos.append((plano_2_pts[0], get_plane_normal(*plano_2_pts)))

# Plano 3
plano_3_pts = [
    apex.Coordinate(-20.0, 20.0, 0.0),
    apex.Coordinate( 20.0, -20.0, 0.0),
    apex.Coordinate( 0.0, 0.0, -40.0)
]
planos.append((plano_3_pts[0], get_plane_normal(*plano_3_pts)))

# Plano 4
plano_4_pts = [
    apex.Coordinate(-20.0, -20.0, 0.0),
    apex.Coordinate( 20.0,  20.0, 0.0),
    apex.Coordinate( 0.0,  0.0, -40.0)
]
planos.append((plano_4_pts[0], get_plane_normal(*plano_4_pts)))

# ---------------------- VÉRTICES ---------------------- #


############################# Cuerpo Tornillo ############################

part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid = part.getSolid( name = "PartBody" )
vertices = solid.getVertices()

tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vértice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Está en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vértice(s) que no pertenecen a ningún plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vértices a eliminar. Continuando con el siguiente código...")


################################ Arandela ##################################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Arandela")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Arandela/PartBody")
solid = part.getSolid(name="PartBody")
vertices = solid.getVertices()



tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vértice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Está en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vértice(s) que no pertenecen a ningún plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vértices a eliminar. Continuando con el siguiente código...")

#################### Pieza Inferior Intermedia ##############################

part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid = part.getSolid( name = "P_InterMed" )

vertices = solid.getVertices()



tolerance = 1e-6

vertices_a_eliminar = apex.EntityCollection()

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    punto = (coord[0], coord[1], coord[2])
    
    # Comprobamos si el vértice pertenece a alguno de los planos
    pertenece_a_alguno = False
    for plano_punto, normal in planos:
        distancia = point_plane_distance(punto, plano_punto, normal)
        if abs(distancia) <= tolerance:  # Está en el plano
            pertenece_a_alguno = True
            break
    
    # Si no pertenece a ninguno, se elimina
    if not pertenece_a_alguno:
        vertices_a_eliminar.append(vertex)

print(f"Eliminando {len(vertices_a_eliminar)} vértice(s) que no pertenecen a ningún plano...")
if len(vertices_a_eliminar) > 0:
    apex.deleteEntities(vertices_a_eliminar)
else:
    print("No se encontraron vértices a eliminar. Continuando con el siguiente código...")

# ================================================================================
#
#
#
#                        DIVISION DE LA CABEZA DEL TORNILLO
#                               
#
#
#
# ================================================================================



# Paso 1: Obtener todos los vértices de la cabeza del tornillo
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
vertices = solid.getVertices()

# Paso 2: Agrupar por coordenada Z (con tolerancia)
z_groups = defaultdict(list)
tolerance = 1e-3

for vertex in vertices:
    coord = vertex.getLocationCartesian()
    z = coord[2]
    
    # Normalizar con tolerancia
    matched = False
    for key in z_groups:
        if abs(z - key) < tolerance:
            z_groups[key].append(vertex)
            matched = True
            break
    if not matched:
        z_groups[z].append(vertex)

# Ordenar las alturas
sorted_z_values = sorted(z_groups.keys())
if len(sorted_z_values) < 3:
    raise Exception("No se encontraron al menos 3 grupos distintos de altura Z")

# Paso 3: Elegir el grupo intermedio
z_middle = sorted_z_values[1]
middle_vertices = z_groups[z_middle]

# # Paso 4: Crear plano horizontal con tres vértices del grupo intermedio
# if len(middle_vertices) < 3:
#     raise Exception("No hay suficientes vértices en la altura intermedia para definir un plano")

# p1 = middle_vertices[0].getLocation()
# p2 = middle_vertices[1].getLocation()
# p3 = middle_vertices[2].getLocation()

# # Crear el plano
# horizontal_plane = apex.utility.createPlaneFromPoints(p1, p2, p3)

# # Paso 5: Ejecutar la partición con este plano
# target = apex.EntityCollection()
# target.append(solid)

# result = apex.geometry.split(
#     target = target,
#     splitter = horizontal_plane,
#     splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
# )

# print("División completada con plano horizontal en Z =", z_middle)


_target = apex.EntityCollection()
# Obtener la parte y sólido
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
_target.append( solid )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, z_middle ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, z_middle ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, z_middle )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("✅ Corte realizado con éxito. El sólido fue dividido por el plano ZX (Y=0).")