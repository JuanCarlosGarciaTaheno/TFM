# coding: utf-8

import apex
from apex.construct import Point3D, Point2D


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

print(f"Celda mas alta: ID {celda_max_z.getId()} con Z = {z_max}")

# Paso 2: Obtener las 6 caras mas pequenas de esa celda
caras = celda_max_z.getFaces()

caras_ordenadas = sorted(caras, key=lambda cara: cara.getArea())
caras_menores = caras_ordenadas[:6]

# Crear coleccion de caras para el attachment
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


