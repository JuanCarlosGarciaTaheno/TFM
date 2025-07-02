# coding: utf-8

import apex
from apex.construct import Point3D, Point2D
import math
from apex import mesh


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

################################################

#         MESH SEED  ---  TORNILLO

################################################

# Obtener ensamblajes y solido
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo")
assembly_2.show()

part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name="PartBody")

# Clasificar celdas por Z del centroide
celdas = solid.getCells()
celdas_ordenadas = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)
celdas_superiores = celdas_ordenadas[:3]
celdas_inferiores = celdas_ordenadas[3:]

# Listas clasificadas
verticales_superiores = []
verticales_inferiores = []
arcos_superiores = []
arcos_inferiores = []
radiales_superiores = []
radiales_inferiores = []

# Funciones auxiliares
def vector_subtract(a, b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def vector_length(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vector_dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def angle_between_vectors(a, b):
    dot = vector_dot(a, b)
    len_a = vector_length(a)
    len_b = vector_length(b)
    if len_a == 0 or len_b == 0:
        return 0
    cos_angle = dot / (len_a * len_b)
    cos_angle = max(min(cos_angle, 1), -1)
    return math.acos(cos_angle)

# Clasificar aristas
edges = solid.getEdges()

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    es_superior = any(edge in celda.getEdges() for celda in celdas_superiores)

    # Vertical
    if dz > dx and dz > dy:
        if es_superior:
            verticales_superiores.append(edge)
        else:
            verticales_inferiores.append(edge)
        continue

    # Arco
    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()
        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)
        angle = angle_between_vectors(vec0, vec1)
        if 0.087 < angle < math.pi+0.1:
            if es_superior:
                arcos_superiores.append(edge)
            else:
                arcos_inferiores.append(edge)
            continue

    # Si no es vertical ni arco, es radial
    if es_superior:
        radiales_superiores.append(edge)
    else:
        radiales_inferiores.append(edge)

#  Semillado por tipo y altura

# Arcos
# if arcos_superiores:
#     print(f"Semillando {len(arcos_superiores)} arco(s) superiores con 6 elementos")
#     for edge in arcos_superiores:
#         collection = apex.EntityCollection()
#         collection.append(edge)
#         apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=6*4)

if arcos_inferiores:
    print(f"Semillando {len(arcos_inferiores)} arco(s) inferiores con {n_elementos_arcos_Tornillo} elementos")
    for edge in arcos_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_arcos_Tornillo)

# Verticales
if verticales_superiores:
    print(f"Semillando {len(verticales_superiores)} vertical(es) superiores con {n_elementos_verticales_CABEZA} elementos")
    for edge in verticales_superiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_verticales_CABEZA)

if verticales_inferiores:
    print(f"Semillando {len(verticales_inferiores)} vertical(es) inferiores con {n_elementos_verticales_CuerpoTorn} elementos")
    for edge in verticales_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_verticales_CuerpoTorn)

# Radiales
# if radiales_superiores:
#     print(f"Semillando {len(radiales_superiores)} radial(es) superiores con 10 elementos")
#     for edge in radiales_superiores:
#         collection = apex.EntityCollection()
#         collection.append(edge)
#         apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=5)

if radiales_inferiores:
    print(f"Semillando {len(radiales_inferiores)} radial(es) inferiores con {n_elementos_radiales_Tornillo} elementos")
    for edge in radiales_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_radiales_Tornillo)
        #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)










#########################  MESH SEED Pieza Inf ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()



part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )


# # Clasificar celdas por Z del centroide
# celdas = solid.getCells()
# celdas_ordenadas = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)
# celdas_superiores = celdas_ordenadas[:1]
# celdas_inferiores = celdas_ordenadas[1:]
celdas = solid.getCells()
celdas_ordenadas = sorted(celdas, key=lambda c: c.getCentroid().z, reverse=True)

# Mostrar centroides con su indice
print("Centroides ordenados por Z (de mayor a menor):")
for i, celda in enumerate(celdas_ordenadas):
    centroide = celda.getCentroid()
    print(f"Celda {i+1}: x = {centroide.x:.3f}, y = {centroide.y:.3f}, z = {centroide.z:.3f}")

# Clasificacion superior/inferior
celdas_superiores = celdas_ordenadas[:7]
celdas_inferiores = celdas_ordenadas[7:]
# Listas clasificadas
verticales_superiores = []
verticales_inferiores = []
arcos_superiores = []
arcos_inferiores = []
radiales_superiores = []
radiales_inferiores = []

# Funciones auxiliares
def vector_subtract(a, b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def vector_length(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vector_dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def angle_between_vectors(a, b):
    dot = vector_dot(a, b)
    len_a = vector_length(a)
    len_b = vector_length(b)
    if len_a == 0 or len_b == 0:
        return 0
    cos_angle = dot / (len_a * len_b)
    cos_angle = max(min(cos_angle, 1), -1)
    return math.acos(cos_angle)

# Clasificar aristas
edges = solid.getEdges()

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    es_superior = any(edge in celda.getEdges() for celda in celdas_superiores)

    # Vertical
    if dz > dx and dz > dy:
        if es_superior:
            verticales_superiores.append(edge)
        else:
            verticales_inferiores.append(edge)
        continue

    # Arco
    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()
        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)
        angle = angle_between_vectors(vec0, vec1)
        if 0.087 < angle < math.pi:
            if es_superior:
                arcos_superiores.append(edge)
            else:
                arcos_inferiores.append(edge)
            continue

    # Si no es vertical ni arco, es radial
    if es_superior:
        radiales_superiores.append(edge)
    else:
        radiales_inferiores.append(edge)

#  Semillado por tipo y altura

# Arcos
if arcos_superiores:
    print(f"Semillando {len(arcos_superiores)} arco(s) superiores con {n_elementos_arcos_PiezaInferior} elementos")
    for edge in arcos_superiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_arcos_PiezaInferior)

if arcos_inferiores:
    print(f"Semillando {len(arcos_inferiores)} arco(s) inferiores con {n_elementos_arcos_PiezaInferior} elementos")
    for edge in arcos_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_arcos_PiezaInferior)

# Verticales
if verticales_superiores:
    print(f"Semillando {len(verticales_superiores)} vertical(es) superiores con elementos de {tamano_elementos_verticales_PiezaInferiorRosca} mm")
    for edge in verticales_superiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        # apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=3)
        apex.mesh.createEdgeSeedUniformByLength(target=collection,elementEdgeLength = tamano_elementos_verticales_PiezaInferiorRosca)

if verticales_inferiores:
    print(f"Semillando {len(verticales_inferiores)} vertical(es) inferiores con {n_elementos_verticales_PiezaInferior} elementos")
    for edge in verticales_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_verticales_PiezaInferior)

# Radiales
if radiales_superiores:
    print(f"Semillando {len(radiales_superiores)} radial(es) superiores con {n_elementos_radiales_PiezaInferior} elementos")
    for edge in radiales_superiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_radiales_PiezaInferior)

if radiales_inferiores:
    print(f"Semillando {len(radiales_inferiores)} radial(es) inferiores con {n_elementos_radiales_PiezaInferior} elementos")
    for edge in radiales_inferiores:
        collection = apex.EntityCollection()
        collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=collection, numberElementEdges=n_elementos_radiales_PiezaInferior)
        #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)
#Para radiales (10 elementos)

# if len(radiales) > 0:
#     print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
#     for edge in radiales:
#         edges_collection = apex.EntityCollection()
#         edges_collection.append(edge)
#         apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# # Para arcos (6 elementos)
# if len(arcos) > 0:
#     print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
#     for edge in arcos:
#         edges_collection = apex.EntityCollection()
#         edges_collection.append(edge)
#         apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6) #CAMBIO AQUI, para que la parte de la pieza de la rosca sea mejor
#         #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)


# # Para verticales (3 elementos)
# if len(verticales) > 0:
#     print(f"Semillando {len(verticales)} vertical(es) con 0.2mm elementos")
#     for edge in verticales:
#         edges_collection = apex.EntityCollection()
#         edges_collection.append(edge)
#         #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)
#         apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)

















#########################  MESH SEED PIEZA SUPERIOR ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/PiezaSuperior1")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/PiezaSuperior1/PartBody")
solid = part.getSolid(name="PartBody")

# Obtener aristas
edges = solid.getEdges()



def vector_subtract(a, b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def vector_length(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vector_dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def angle_between_vectors(a, b):
    dot = vector_dot(a, b)
    len_a = vector_length(a)
    len_b = vector_length(b)
    if len_a == 0 or len_b == 0:
        return 0
    cos_angle = dot / (len_a * len_b)
    cos_angle = max(min(cos_angle, 1), -1)  # clamp to avoid numerical issues
    return math.acos(cos_angle)  # en radianes

verticales = []
arcos = []
radiales = []

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    if dz > dx and dz > dy:
        verticales.append(edge)
        continue

    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()

        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)

        angle = angle_between_vectors(vec0, vec1)  # radianes

        # Si el angulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es linea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con {n_elementos_radiales_PiezaSuperior} elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_radiales_PiezaSuperior)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con {n_elementos_arcos_PiezaSuperior} elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_arcos_PiezaSuperior)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con {n_elementos_verticales_PiezaSuperior} elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_verticales_PiezaSuperior)




#########################  MESH SEED ARANDELA ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Arandela")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Arandela/PartBody")
solid = part.getSolid(name="PartBody")

# Obtener aristas
edges = solid.getEdges()

verticales = []
arcos = []
radiales = []

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    if dz > dx and dz > dy:
        verticales.append(edge)
        continue

    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()

        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)

        angle = angle_between_vectors(vec0, vec1)  # radianes

        # Si el angulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es linea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con {n_elementos_radiales_Arandela} elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_radiales_Arandela)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con {n_elementos_arcos_Arandela} elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_arcos_Arandela)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con {n_elementos_verticales_Arandela} elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_verticales_Arandela)




#########################  MESH SEED Rosca Pieza Inf  ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()




part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RoscaPiezaInferior/PartBody" )
solid = part.getSolid( name = "PartBody" )



# Obtener aristas
edges = solid.getEdges()



verticales = []
arcos = []
radiales = []

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    if dz > dx and dz > dy:
        verticales.append(edge)
        continue

    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()

        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)

        angle = angle_between_vectors(vec0, vec1)  # radianes

        # Si el angulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es linea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (3 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con {n_elementos_radiales_RoscaPInf} elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_radiales_RoscaPInf)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con {n_elementos_arcos_RoscaPInf} elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_arcos_RoscaPInf)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con {n_elementos_verticales_RoscaPInf} elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_verticales_RoscaPInf)

#########################  MESH SEED Rosca Tornillo  ##########################


# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo")
assembly_2.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Rosca_Exterior_Tornillo/PartBody" )
solid = part.getSolid( name = "PartBody" )



# Obtener aristas
edges = solid.getEdges()


verticales = []
arcos = []
radiales = []

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    if dz > dx and dz > dy:
        verticales.append(edge)
        continue

    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()

        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)

        angle = angle_between_vectors(vec0, vec1)  # radianes

        # Si el angulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es linea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (3 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con {n_elementos_radiales_RoscaTorn} elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_radiales_RoscaTorn)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con {n_elementos_arcos_RoscaTorn} elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_arcos_RoscaTorn)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con {n_elementos_verticales_RoscaTorn} elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=n_elementos_verticales_RoscaTorn)


#########################  MESH SEED Helicoill  ##########################

# Cargar pieza 

assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Helicoil")
assembly_2.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Helicoil/PartBody" )
solid = part.getSolid( name = "PartBody" )

# Obtener aristas
edges = solid.getEdges()


verticales = []
arcos = []
radiales = []

for edge in edges:
    vertices = edge.getVertices()
    v0 = vertices[0].getLocationCartesian()
    v1 = vertices[1].getLocationCartesian()

    dx = abs(v1[0] - v0[0])
    dy = abs(v1[1] - v0[1])
    dz = abs(v1[2] - v0[2])

    if dz > dx and dz > dy:
        verticales.append(edge)
        continue

    try:
        arc_center = edge.getArcCenter()
    except Exception:
        arc_center = None

    if arc_center is not None:
        center_xyz = arc_center.getLocationCartesian()

        vec0 = vector_subtract(v0, center_xyz)
        vec1 = vector_subtract(v1, center_xyz)

        angle = angle_between_vectors(vec0, vec1)  # radianes

        # Si el angulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es linea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (2 elementos) - 0.1 mm
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con elementos de {tamano_elementos_radiales_Helicoil} mm")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=2)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = tamano_elementos_radiales_Helicoil)
# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con {n_elementos_arcos_Helicoil} elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges = n_elementos_arcos_Helicoil)



# Para verticales (2 elementos) --- 0.1 mm
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con elementos de {tamano_elementos_verticales_Helicoil}mm")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=2)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = tamano_elementos_verticales_Helicoil)






