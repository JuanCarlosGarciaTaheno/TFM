# coding: utf-8

import apex
from apex.construct import Point3D, Point2D
import math

# Cargar la pieza inferior top
part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )

# Obtener todas las celdas
celdas = solid.getCells()

# Region de attachment (caras mas alejadas de cada celda)
_attachmentRegion = apex.EntityCollection()

# Para calcular el centro global y z media
z_max = -float('inf')
z_min = float('inf')

for celda in celdas:
    # Obtener el centroide de la celda
    centroide_celda = celda.getCentroid()
    z_max = max(z_max, centroide_celda.z)
    z_min = min(z_min, centroide_celda.z)
    
    # Obtener las caras de la celda
    caras = celda.getFaces()
    
    # Buscar la cara mas alejada del centro (0,0)
    max_dist = -1
    cara_mas_lejana = None
    for cara in caras:
        centroide_cara = cara.getCentroid()
        dist = math.sqrt(centroide_cara.x**2 + centroide_cara.y**2)
        if dist > max_dist:
            max_dist = dist
            cara_mas_lejana = cara

    # Añadir la cara mas lejana al attachment
    if cara_mas_lejana:
        _attachmentRegion.append(cara_mas_lejana)

# Calcular z medio de la pieza
z_medio = 0.5 * (z_max + z_min)

# Crear nodo independiente en el centro de masa en altura (0,0,zmedio)
nodo_rbe3 = apex.mesh.createNodeByLocation(
    coordinates = apex.Coordinate(0.0, 0.0, z_medio),
    pathName = part.getPath()
)

# Crear region de referencia
_referenceRegion = nodo_rbe3

# Crear el RBE3
nodetie = apex.attribute.createNodeTie(
    distributionType  = apex.attribute.DistributionType.Compliant,
    distributionMode  = apex.attribute.DistributionMode.Auto,
    dofDefinitionMode = apex.attribute.DOFDefinitionMode.All,
    referencePoint    = _referenceRegion,
    attachmentRegions = _attachmentRegion,
)

apex.endUndoIndent(description="RBE3 - Pieza Inferior Top")
