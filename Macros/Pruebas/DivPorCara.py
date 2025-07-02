# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 14, 2025 at 12:28:20
# 
# Macro Name = DivPorCara
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 



# 
# Start of recorded operations
# 

import apex
from apex import EntityCollection, ColorRGB
from apex.geometry import GeometrySplitBehavior, split
import math

# Obtener la pieza y sus celdas
part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")
celdas = solid.getCells()

def obtener_celdas_izquierda_ordenadas_por_z(celdas):
    celdas_izq = []

    # Recorremos todas las celdas
    for celda in celdas:
        centroide = celda.getCentroid()
        print(f"Centroide celda: X={centroide.x:.3f}, Y={centroide.y:.3f}, Z={centroide.z:.3f}")
        
        if centroide.y > 0:
            celdas_izq.append((celda, centroide.z))

    # Ordenamos por Z descendente (de mayor a menor Z)
    celdas_izq.sort(key=lambda x: x[1], reverse=True)

    if len(celdas_izq) != 3:
        raise ValueError("Se esperaban exactamente 3 celdas en el lado izquierdo.")

    # Extraemos las celdas en orden superior, media, inferior
    izq_sup, izq_med, izq_inf = [celda for celda, _ in celdas_izq]

    return izq_sup, izq_med, izq_inf



# Ordenar celdas por X y coger las 3 más a la izquierda
# celdas_ordenadas_x = sorted(celdas, key=obtener_celdas_izquierda_ordenadas_por_z)
# izq_inf, izq_med, izq_sup = celdas_ordenadas_x[:3]


izq_sup, izq_med, izq_inf = obtener_celdas_izquierda_ordenadas_por_z(celdas)


highlight_color = ColorRGB(255, 0, 0)
izq_inf.highlight(highlight_color, lineWidth=2, pointSize=5)


highlight_color = ColorRGB(0, 255, 0) 
izq_med.highlight(highlight_color, lineWidth=2, pointSize=5)


highlight_color = ColorRGB(0, 0, 255)   
izq_sup.highlight(highlight_color, lineWidth=2, pointSize=5)






def calcular_normal(cara):
    # Sacamos 3 vértices para calcular vector normal
    vertices = cara.getVertices()
    p1 = vertices[0].getLocationCartesian()
    p2 = vertices[1].getLocationCartesian()
    p3 = vertices[2].getLocationCartesian()

    # Vectores en la cara
    v1 = [p2[i] - p1[i] for i in range(3)]
    v2 = [p3[i] - p1[i] for i in range(3)]

    # Producto cruz para normal
    normal = [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

    # Normalizamos
    norm = (normal[0]**2 + normal[1]**2 + normal[2]**2)**0.5
    normal = [n / norm for n in normal]

    return normal

def es_horizontal(normal, tolerancia=1e-3):
    # La cara es horizontal si su normal apunta casi paralela al eje Z (±Z)
    # Normal Z cerca de 1 o -1 → horizontal
    return abs(abs(normal[2]) - 1.0) < tolerancia

def obtener_cara_no_horizontal_menor_area(celda):
    caras = celda.getFaces()
    cara_min = None
    area_min = float('inf')

    for cara in caras:
        normal = calcular_normal(cara)
        if not es_horizontal(normal):
            area = cara.getArea()
            if area < area_min:
                area_min = area
                cara_min = cara

    return cara_min, area_min

def obtener_cara_objetivo(celda, tolerancia_x=1e-2):
    centroide_celda = celda.getCentroid()
    x_celda = centroide_celda.x
    
    caras = celda.getFaces()
    cara_objetivo = None
    area_min = float('inf')
    
    for cara in caras:
        normal = calcular_normal(cara)
        if not es_horizontal(normal):
            centroide_cara = cara.getCentroid()
            # Comprobar que el centroide Z de la cara esté cerca del centroide Z de la celda
            if abs(centroide_cara.x - x_celda) < tolerancia_x:
                area = cara.getArea()
                if area < area_min:
                    area_min = area
                    cara_objetivo = cara

    return cara_objetivo, area_min


cara_obj, area = obtener_cara_objetivo(izq_med, tolerancia_x=0.1)  # Ajusta la tolerancia a lo que necesites
print(f"Cara objetivo: área={area}, centroide Z cercano a {izq_med.getCentroid().z}")


highlight_color = ColorRGB(100, 100, 255)   
cara_obj.highlight(highlight_color, lineWidth=2, pointSize=5)

# Preparar colecciones para el split
_target = apex.EntityCollection()
_target.append(izq_inf)

_splitter = apex.EntityCollection()
_splitter.append(cara_obj)

# Realizar el split
result = apex.geometry.split(
    target = _target,
    splitter = _splitter,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("Split realizado correctamente.")

def obtener_celdas_derecha_ordenadas_por_z(celdas):
    celdas_der = []

    for celda in celdas:
        centroide = celda.getCentroid()
        print(f"Centroide celda: X={centroide.x:.3f}, Y={centroide.y:.3f}, Z={centroide.z:.3f}")
        
        if centroide.y < 0:  # Aquí filtramos las celdas del lado derecho (Y negativo)
            celdas_der.append((celda, centroide.z))

    # Ordenamos por Z descendente (de mayor a menor altura)
    celdas_der.sort(key=lambda x: x[1], reverse=True)

    if len(celdas_der) != 3:
        raise ValueError("Se esperaban exactamente 3 celdas en el lado derecho.")

    der_sup, der_med, der_inf = [celda for celda, _ in celdas_der]

    return der_sup, der_med, der_inf


# Obtener celdas del lado derecho ordenadas
der_sup, der_med, der_inf = obtener_celdas_derecha_ordenadas_por_z(celdas)

# Resaltar para verificar visualmente
der_inf.highlight(ColorRGB(255, 128, 0), lineWidth=2, pointSize=5)
der_med.highlight(ColorRGB(255, 255, 0), lineWidth=2, pointSize=5)
der_sup.highlight(ColorRGB(128, 0, 255), lineWidth=2, pointSize=5)

# Obtener la cara objetivo en la celda intermedia derecha
cara_obj_der, area_der = obtener_cara_objetivo(der_med, tolerancia_x=0.1)
print(f"Cara objetivo derecha: área={area_der}, centroide Z cercano a {der_med.getCentroid().z}")

cara_obj_der.highlight(ColorRGB(0, 255, 255), lineWidth=2, pointSize=5)

# Preparar colecciones para el split
_target_der = apex.EntityCollection()
_target_der.append(der_inf)

_splitter_der = apex.EntityCollection()
_splitter_der.append(cara_obj_der)

# Realizar el split
result_der = apex.geometry.split(
    target = _target_der,
    splitter = _splitter_der,
    splitBehavior = apex.geometry.GeometrySplitBehavior.Partition
)

print("Split realizado correctamente en el lado derecho.")


part = apex.getPart(pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior")
solid = part.getSolid(name = "Original_PSuperior")

# Crear una colección de entidades con el sólido
_target = EntityCollection()
_target.append(solid)



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