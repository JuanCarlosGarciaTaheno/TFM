# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 21:46:39
# 
# Macro Name = DivCabezaTornillo
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

print("División completada con plano horizontal en Z =", z_middle)



    
    
z_tol = 1e-3  # Tolerancia
#z_middle = 1.82  # Usa tu valor real aquí

# Obtener la parte y sólido
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")

# Obtener todas las curvas
all_edges = solid.getEdges()

# Almacén de curvas con sus alturas z muestreadas
edge_z_data = []

print("🔎 Z heights for curves (sampled at t = 0, 0.5, 1.0):")
print("------------------------------------------------------")

for edge in all_edges:
    try:
        samples = [edge.evaluatePosition(t) for t in z_sample_points]
        z_values = [round(p.z, 4) for p in samples]
        edge_z_data.append((edge, z_values))
        print(f"Curve: Z = {z_values}")
    except:
        print("⚠️  No se pudo muestrear una curva (posiblemente curva degenerada).")

print("\n✅ Total de curvas muestreadas:", len(edge_z_data))