# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 14, 2025 at 14:26:17
# 
# Macro Name = UnionCuerpoTornillo
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

import apex
from apex.construct import Point3D, Point2D
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

assembly_1 = apex.getAssembly( pathName = apex.currentModel().name )
assembly_1.hide()

assembly_2 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca" )
assembly_2.show()

_target = apex.EntityCollection()
part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6" )
solid_1 = part_1.getSolid( name = "Body.6" )
_target.append( solid_1 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
result = apex.geometry.mergeBoolean(
    target = _target,
    retainOriginalBodies = False,
    mergeSolidsAsCells = False
)
######################################################################

#       Division del cuerpo del tornillo en 4 planos

######################################################################

_target = apex.EntityCollection()
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


######################################################################

#       Union Cuerpo Tornillo - Cabeza

######################################################################

assembly_3 = apex.getAssembly( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo" )
assembly_3.show()

_target = apex.EntityCollection()
part_3 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody" )
solid_3 = part_3.getSolid( name = "PartBody" )
_target.append( solid_3 )
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody" )
solid_2 = part_2.getSolid( name = "PartBody" )
_target.append( solid_2 )
result = apex.geometry.mergeBoolean(
    target = _target,
    retainOriginalBodies = False,
    mergeSolidsAsCells = False
)


# #============================================================================================================0
######################################################################

#                   Divisiones Horizontales

######################################################################

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
if len(sorted_z_values) < 5:
    raise Exception("No se encontraron al menos 3 grupos distintos de altura Z")

# Paso 3: Elegir el grupo intermedio entre la cabeza y el cuerpo
z_middle = sorted_z_values[2]
middle_vertices = z_groups[z_middle]

Z_medio_cabeza =  sorted_z_values[3]

# PASO 4: Obtener la parte y sólido - DIVISION
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

print("✅ Corte realizado entre el cuerpo y la cabeza.")

# PASO 5: Obtener la parte y sólido - DIVISION de la Cabeza
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
_target.append( solid )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, Z_medio_cabeza )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("✅ Corte realizado en la cabeza.")


######################################################################

#        Divisiones Verticales de la Cabeza celda Inferior

######################################################################

# Paso 1: Obtener todos los vértices de la cabeza del tornillo
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name = "PartBody")
    
        
celdas = solid.getCells()

def obtener_celdas_ordenadas_por_z(celdas):
    # Creamos una lista con pares (celda, centroide.z)
    lista_celdas_z = [(celda, celda.getCentroid().z) for celda in celdas]

    # Ordenamos por Z descendente (de mayor a menor)
    lista_celdas_z.sort(key=lambda x: x[1], reverse=True)

    # Solo devolvemos la lista de celdas ordenadas
    return [celda for celda, z in lista_celdas_z]



celdas_ordenadas = obtener_celdas_ordenadas_por_z(celdas)

# Imprimir los centroides Z para verificar orden
for i, celda in enumerate(celdas_ordenadas):
    c = celda.getCentroid()
    print(f"Celda {i+1}: Centroide Z = {c.z:.3f}")


segunda_celda = celdas_ordenadas[1]
print("Centroide Z segunda celda:", segunda_celda.getCentroid().z)

_target.append( segunda_celda )

_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0,0.0 ),
    apex.Coordinate( 0.0, 0.0, 20.0 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)






######################################################################

# -----------------------------------------------------
# CORTES A CELDAS POR DEBAJO DE LA SEGUNDA CELDA (EN Z)
# -----------------------------------------------------

# 1. Obtener todas las celdas del sólido
celdas = solid.getCells()

# 2. Obtener la Z del centroide de la segunda celda
z_referencia = segunda_celda.getCentroid().z
print(f"Centroide Z segunda celda: {z_referencia:.6f}")

# 3. Filtrar solo celdas por debajo
celdas_debajo = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda < z_referencia - 0.5:  # Ajuste de margen
        celdas_debajo.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} >= {z_referencia:.3f}")

print(f"\n✅ Número de celdas por debajo: {len(celdas_debajo)}")
if len(celdas_debajo) == 0:
    raise RuntimeError("❌ No hay celdas válidas por debajo para aplicar los cortes.")

# 4. Definir los 4 cortes (cada uno con 3 puntos)
cortes_locations = [
    [apex.Coordinate(-20.0, 0.0, 0.0),  apex.Coordinate(20.0, 0.0, 0.0),  apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(0.0, -20.0, 0.0),  apex.Coordinate(0.0, 20.0, 0.0),  apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(-20.0, 20.0, 0.0), apex.Coordinate(20.0, -20.0, 0.0), apex.Coordinate(0.0, 0.0, -40.0)],
    [apex.Coordinate(-20.0, -20.0, 0.0), apex.Coordinate(20.0, 20.0, 0.0), apex.Coordinate(0.0, 0.0, -40.0)]
]

# 5. Aplicar cortes secuencialmente
celdas_actuales = celdas_debajo

for i, locations in enumerate(cortes_locations, start=1):
    _iphysicalCollection = apex.ILocationCollection()
    for punto in locations:
        _iphysicalCollection.append(punto)

    # Si no quedan celdas, detener y notificar
    if len(celdas_actuales) == 0:
        raise RuntimeError(f"❌ No quedan celdas que cortar antes del corte {i}")

    try:
        result = apex.geometry.splitOn3PointPlane(
            target=celdas_actuales,
            locations=_iphysicalCollection,
            splitBehavior=apex.geometry.GeometrySplitBehavior.Partition
        )
        celdas_actuales = result
  # Actualizar celdas para el siguiente corte
        print(f"✅ Corte {i} realizado correctamente. Nuevas celdas: {len(celdas_actuales)}")
    except Exception as e:
        print(f"❌ Error en corte {i}: {e}")
        break





# ---------------------------------------------------------
# UNIR CELDAS QUE ESTÁN POR ENCIMA DE LA SEGUNDA CELDA (Z)
# ---------------------------------------------------------

celdas = solid.getCells()

# 2. Usar Z de la segunda celda como referencia
z_referencia = segunda_celda.getCentroid().z

# 3. Filtrar las celdas que estén por encima
celdas_por_encima = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda > z_referencia - 0.1:
        celdas_por_encima.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} <= {z_referencia:.3f}")

print(f"\n✅ Número de celdas por encima: {len(celdas_por_encima)}")

# 4. Si hay varias, unirlas con mergeBoolean
if len(celdas_por_encima) > 1:
    _merge_target = apex.EntityCollection()
    for celda in celdas_por_encima:
        _merge_target.append(celda)

    try:
        resultado_union = apex.geometry.mergeBoolean(
            target=_merge_target,
            retainOriginalBodies=False,
            mergeSolidsAsCells=True  # Importante para que no cree cuerpos separados
        )
        print("✅ Celdas unidas correctamente en una única celda.")
        # Opcional: seleccionar y colorear el resultado
        apex.selection.set(resultado_union)
        resultado_union[0].setColor(apex.render.Color(255, 150, 150))
    except Exception as e:
        print(f"❌ Error al unir celdas: {e}")
elif len(celdas_por_encima) == 1:
    print("ℹ️ Solo hay una celda por encima, no es necesario unir.")
else:
    print("❌ No hay celdas por encima del plano para unir.")
    
# Dividir por un plano
_target  = celdas_por_encima
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, 0.0 ),
    apex.Coordinate( 2.000000000000000e+01, 0.0,0.0 ),
    apex.Coordinate( 0.0, 0.0, 20.0 )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)


# PASO 5: Obtener la parte y sólido - DIVISION de la Cabeza
celdas = solid.getCells()

# 2. Usar Z de la segunda celda como referencia
z_referencia = segunda_celda.getCentroid().z

# 3. Filtrar las celdas que estén por encima
celdas_por_encima = apex.EntityCollection()
for idx, celda in enumerate(celdas, start=1):
    z_celda = celda.getCentroid().z
    if z_celda > z_referencia - 0.1:
        celdas_por_encima.append(celda)
    else:
        print(f"Celda {idx} descartada con Z={z_celda:.3f} <= {z_referencia:.3f}")


_target  = celdas_por_encima
_locations = [
    apex.Coordinate( -2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 2.000000000000000e+01, 0.0, Z_medio_cabeza ),
    apex.Coordinate( 0.0, 2.000000000000000e+01, Z_medio_cabeza )
]
_iphysicalCollection = apex.ILocationCollection() 
for point in _locations :

    _iphysicalCollection.append(point)
result = apex.geometry.splitOn3PointPlane(
    target = _target,
    locations = _iphysicalCollection,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)