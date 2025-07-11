# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 13:31:07
# 
# Macro Name = ImportacionModelo
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

# _geometryFileNames = [
#     "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/Product/M4_SeparacionMedia.stp"
# ]
_importFilter = {
    
}
model_1.importGeometry(
    geometryFileNames = [ruta_step],
    importSolids = True,     #defaults to True
    importSurfaces = True,     #defaults to True
    importCurves = True,     #defaults to True
    importPoints = True,     #defaults to True
    importGeneralBodies = True,     #defaults to True
    importHiddenGeometry = False,     #defaults to False
    importCoordinate = False,     #defaults to True
    importDatumPlane = False,     #defaults to True
    cleanOnImport = True,     #defaults to True
    removeRedundantTopoOnimport = True,     #defaults to False
    loadCompleteTopology = True,     #defaults to True
    sewOnImport = False,     #defaults to False
    skipUnmodified = False,     #defaults to False
    importFilter = _importFilter,
    preview = False,     #defaults to False
    importReviewMode3dxmlCleanOnImport = True,     #defaults to True
    importReviewMode3dxmlSplitOnFeatureVertexAngle = True,     #defaults to True
    importReviewMode3dxmlFeatureAngle = 4.000000000000000e+01,     #defaults to 40.0 degrees
    importReviewMode3dxmlVertexAngle = 4.000000000000000e+01,     #defaults to 40.0 degrees
    importReviewMode3dxmlDetectMachinedFaces = False,     #defaults to False
    importAttributes = False,     #defaults to False
    importPublications = False     #defaults to False
)

# 
# Macro recording stopped on Jun 13, 2025 at 13:31:26
# 
