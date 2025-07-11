# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 13:46:45
# 
# Macro Name = RBE3_CABEZA
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D

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

# 
# Start of recorded operations
# 

#############################
import apex
#apex.enableShowOutput()

model = apex.currentModel()
path_solid = model.name + "/Union_Apex/Cabeza_Tornillo/PartBody"
part = apex.getPart(pathName=path_solid)
solid = part.getSolid(name="PartBody")

# Paso 1: Obtener la celda con el mayor valor de coordenada Z (usando su centroide)
celdas = solid.getCells()

celda_max_z = None
z_max = float('-inf')

for celda in celdas:
    centroide = celda.getCentroid()
    if centroide.z > z_max:
        z_max = centroide.z
        celda_max_z = celda

print(f"Celda más alta: ID {celda_max_z.getId()} con Z = {z_max}")

# Paso 2: Obtener las 6 caras más pequeñas de esa celda
caras = celda_max_z.getFaces()

caras_ordenadas = sorted(caras, key=lambda cara: cara.getArea())
caras_menores = caras_ordenadas[:6]

# Crear colección de caras para el attachment
_attachmentRegion = apex.EntityCollection()
for cara in caras_menores:
    _attachmentRegion.append(cara)


# Paso 3: Crear nodo en (0, 0, Z_mitad)
centroide = celda_max_z.getCentroid()
z_mitad = centroide.z

nodo_creado = apex.mesh.createNodeByLocation(
    coordinates = apex.Coordinate(0.0, 0.0, z_mitad),
    pathName = path_solid
)

# Paso 4: Crear nodo tie (tipo RBE3) entre ese nodo y las caras
_referenceRegion = nodo_creado

nodetie = apex.attribute.createNodeTie(
    distributionType  = apex.attribute.DistributionType.Compliant,
    distributionMode  = apex.attribute.DistributionMode.Auto,
    dofDefinitionMode  = apex.attribute.DOFDefinitionMode.All,
    referencePoint  = _referenceRegion,
    attachmentRegions  = _attachmentRegion,
)

apex.endUndoIndent(description='created RBE3 at bolt head')


# apex.mesh.createNodeByLocation( coordinates = apex.Coordinate(-0.372719339794, 0.645564636216, 2.820000052452), pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )

# _geoms = apex.EntityCollection()
# part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
# solid_2 = part_2.getSolid( name = "PartBody" )
# _ids = '35142, 35172, 35202'
# _geoms.extend( solid_2.getFaces( ids = _ids ) )
# _attachmentRegion = apex.EntityCollection()
# _attachmentRegion.extend( _geoms )
# nodes_2 = apex.getNodes(
#     [{"path": apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody", "ids": "105269-105269"}]
# )
# _referenceRegion = nodes_2.list()[0]
# nodetie_2 = apex.attribute.createNodeTie(
#     distributionType  = apex.attribute.DistributionType.Compliant,
#     distributionMode  = apex.attribute.DistributionMode.Auto,
#     dofDefinitionMode  = apex.attribute.DOFDefinitionMode.All,
#     referencePoint  = _referenceRegion,
#     attachmentRegions  = _attachmentRegion,
# )

# apex.endUndoIndent(description='created node tie')
#############################

# 
# Macro recording stopped on Jun 13, 2025 at 13:48:03
# 
