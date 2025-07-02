# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 13, 2025 at 14:13:26
# 
# Macro Name = RBE3_PiezaInfTop
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

# Cargar la pieza inferior top
part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name="Original_PSuperior")

# Obtener todas las celdas
celdas = solid.getCells()

# Ordenar celdas por Z descendente y seleccionar las 8 mas altas
celdas_superiores = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)[:8]

# Región de attachment (caras mas alejadas del origen en cada celda)
_attachmentRegion = apex.EntityCollection()

# Para calcular z medio de las 8 celdas superiores
z_total = 0.0

for celda in celdas_superiores:
    centroide_celda = celda.getCentroid()
    z_total += centroide_celda.z

    # Obtener la cara mas alejada del origen (en XY)
    cara_mas_lejana = max(
        celda.getFaces(),
        key=lambda cara: cara.getCentroid().x**2 + cara.getCentroid().y**2
    )

    _attachmentRegion.append(cara_mas_lejana)

# Calcular z medio SOLO de las 8 celdas seleccionadas
z_medio = z_total / len(celdas_superiores)

# Crear nodo independiente en (0, 0, z_medio)
nodo_rbe3 = apex.mesh.createNodeByLocation(
    coordinates=apex.Coordinate(0.0, 0.0, z_medio),
    pathName=part.getPath()
)

# Crear region de referencia
_referenceRegion = nodo_rbe3

# Crear el RBE3
nodetie = apex.attribute.createNodeTie(
    distributionType=apex.attribute.DistributionType.Compliant,
    distributionMode=apex.attribute.DistributionMode.Auto,
    dofDefinitionMode=apex.attribute.DOFDefinitionMode.All,
    referencePoint=_referenceRegion,
    attachmentRegions=_attachmentRegion,
)

apex.endUndoIndent(description="RBE3 - Pieza Inferior Top")
