# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 14, 2025 at 12:05:29
# 
# Macro Name = UnirCeldas
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

from apex import EntityCollection, geometry

# Seleccionar el sólido de la pieza ya dividida
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Obtener las celdas (tras divisiones, debe haber 6)
cells = solid.getCells()
print(f"Se encontraron {len(cells)} celdas.")

# Obtener centroides y agrupar celdas por coordenada Z (con tolerancia)
z_groups = {}
tolerance = 1e-5

for cell in cells:
    z = cell.centroid.z
    z_rounded = round(z / tolerance) * tolerance  # Agrupamos con tolerancia
    if z_rounded not in z_groups:
        z_groups[z_rounded] = []
    z_groups[z_rounded].append(cell)

# Confirmamos que hay 3 grupos
print(f"Grupos de Z encontrados: {len(z_groups)}")
for z_val, celdas in z_groups.items():
    print(f"Z={z_val:.4f} mm → {len(celdas)} celda(s)")

# Unir las celdas de cada grupo Z
for z_val, cell_list in z_groups.items():
    if len(cell_list) < 2:
        print(f"Advertencia: solo hay {len(cell_list)} celda(s) en Z={z_val:.4f}, se omite unión.")
        continue
    
    print(f"Uniendo {len(cell_list)} celdas en Z={z_val:.4f}...")

    _merge_target = EntityCollection()
    for c in cell_list:
        _merge_target.append(c)

    result = geometry.mergeBoolean(
        target = _merge_target,
        retainOriginalBodies = False,
        mergeSolidsAsCells = True  # Muy importante para mantener un solo solid
    )
