# coding: utf-8
# Macro created by MSC Apex 2024.2 GA - Version CLR:014231-5fbf2aff
# Macro created on Jun 12, 2025 at 10:03:22
# 
# Macro Name = StepMeshSeed
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

# import apex
# from apex.construct import Point3D, Point2D

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



####################################################################

######################################################################

######################################################################

####################################################################


import apex
import math
#apex.disableShowOutput()

# Configuraciones básicas 
apex.setScriptUnitSystem(unitSystemName='mm-kg-s-N-K')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = True
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry=applicationSettingsGeometry)



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)




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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)


#########################  MESH SEED Pieza Inf Med ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()



part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_InterMed" )
solid = part.getSolid( name = "P_InterMed" )



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)



#########################  MESH SEED Pieza Inf Inf Ext ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()



part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Exterior" )
solid = part.getSolid( name = "P_Inferior_Exterior" )



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)



#########################  MESH SEED Pieza Inf Inf Intt ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()



part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/P_Inferior_Interior" )
solid = part.getSolid( name = "P_Inferior_Interior" )



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (24 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 24 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=24)

# Para arcos (24 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 24 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=24)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)




#########################  MESH SEED Pieza Inf TOP ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()



part_1 = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
part_1.show()


part = apex.getPart( pathName = apex.currentModel().name + "/Union_Apex/Product1/RestoPiezaInferior/Original_PSuperior" )
solid = part.getSolid( name = "Original_PSuperior" )



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (10 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 10 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=10)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6) #CAMBIO AQUI, para que la parte de la pieza de la rosca sea mejor
        #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)


# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 0.2mm elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)



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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (3 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 3 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)

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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (3 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 3 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)

# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 3 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)


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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (2 elementos) - 0.1 mm
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 2 elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=2)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.1)
# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (2 elementos) --- 0.1 mm
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 2 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=2)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.1)
        
        
        
        


#########################  MESH SEED Cuerpo Tornillo Exterior ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/PartBody")
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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (5 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 0.2 mm elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=5)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)
# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 50 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=50)
        #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)




#########################  MESH SEED Cuerpo Tornillo Interior ##########################

# Cargar pieza 
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca")
assembly_2.show()



part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Tornillo_Sin_Rosca/Body.6")
solid = part.getSolid(name="Body.6")

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

        # Si el ángulo es mayor de 5 grados (~0.087 rad) y menor de 180 grados (pi),
        # asumimos arco. Si no, es línea recta.
        if 0.087 < angle < math.pi:
            arcos.append(edge)
            continue

    radiales.append(edge)

# Para radiales (5 elementos)
if len(radiales) > 0:
    print(f"Semillando {len(radiales)} radial(es) con 0.2 mm elementos")
    for edge in radiales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=5)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)
# Para arcos (6 elementos)
if len(arcos) > 0:
    print(f"Semillando {len(arcos)} arco(s) con 6 elementos")
    for edge in arcos:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=6)



# Para verticales (3 elementos)
if len(verticales) > 0:
    print(f"Semillando {len(verticales)} vertical(es) con 50 elementos")
    for edge in verticales:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=50)
        #apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.2)


#########################  MESH SEED Cabeza Tornillo ###############################




# Cargar y mostrar solo la cabeza del tornillo
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.hide()

assembly_2 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo")
assembly_2.show()

# Obtener el sólido
part = apex.getPart(pathName=apex.currentModel().name + "/Union_Apex/Cabeza_Tornillo/PartBody")
solid = part.getSolid(name="PartBody")

# Obtener aristas
edges = solid.getEdges()
print(f"🔍 Total de aristas detectadas: {len(edges)}")

# Malla de elementos 1D de 1 mm en cada edge
for edge in edges:
        edges_collection = apex.EntityCollection()
        edges_collection.append(edge)
        #apex.mesh.createEdgeSeedUniformByNumber(target=edges_collection, numberElementEdges=3)
        apex.mesh.createEdgeSeedUniformByLength(target=edges_collection,elementEdgeLength = 0.4)
