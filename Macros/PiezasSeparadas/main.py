import apex
import math
import os
#apex.disableShowOutput()

# Configuraciones básicas 
apex.setScriptUnitSystem(unitSystemName='mm-kg-s-N-K')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = True
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry=applicationSettingsGeometry)

# === CONFIGURACIÓN INICIAL ===
#ruta_step = "C:\\Users\\jc.garcia-taheno\\Desktop\\CE_3_TahenoHijes\\Sketchs_Apex\\Product\\M4_SeparacionMedia.stp"

# M4 MEDIA SEP
#ruta_step = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/Product/M4_SeparacionMedia.stp" 
# M8 MEDIA SEP

ruta_step = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/Product/Prueba.stp"
tamano_malla = 0.2  # en mm 
usar_refinamiento = True

# === RUTA DE LAS MACROS ===

ruta_macros = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Macros/PiezasSeparadas"

def ejecutar_macro(nombre_macro):
    print(f"Ejecutando {nombre_macro}...")
    ruta_macro = os.path.join(ruta_macros, nombre_macro)
    with open(ruta_macro, "r", encoding="latin-1") as archivo:  # utf-8 o "latin-1" si da problemas
        codigo = archivo.read()
    exec(codigo, globals())
    
#########################################################
# === VARIABLES GLOBALES QUE USAN LOS SCRIPTS ===

globals()['ruta_step'] = ruta_step

#########################################################
#               VARIABLES Mallado
#########################################################

globals()['tamano_malla_tornillo_exterior'] = 0.2  # en mm 
globals()['tamano_malla_tornillo_interior'] = 0.2  # en mm 
globals()['tamano_malla_Cabeza'] = 0.5  # en mm 

globals()['tamano_malla_PiezaInferior_TOP'] = 0.2  # en mm 
globals()['tamano_malla_PiezaInferior_Medio'] = 0.2  # en mm 
globals()['tamano_malla_PiezaInferior_BOT'] = 0.2  # en mm 
globals()['tamano_malla_PiezaInferior_Cilindro'] = 0.2  # en mm 

globals()['tamano_malla_PiezaSuperior'] = 0.2  # en mm 
globals()['tamano_malla_Arandela'] = 0.2  # en mm 
globals()['tamano_malla_RoscaTornillo'] = 0.2  # en mm 
globals()['tamano_malla_RoscaPInferior'] = 0.2  # en mm 
globals()['tamano_malla_Helicoil'] = 0.2  # en mm 



#########################################################
#               VARIABLES Mesh Seed
#########################################################

globals()['n_elementos_arcos_CuerpoTorn_Ext'] = 6
globals()['n_elementos_verticales_CuerpoTorn_Ext'] = 50

globals()['n_elementos_arcos_CuerpoTorn_Int'] = 6
globals()['n_elementos_verticales_CuerpoTorn_Int'] = 50

globals()['n_elementos_arcos_Cabeza'] = 6
globals()['n_elementos_verticales_Cabeza'] = 3

#
globals()['n_elementos_arcos_PiezaInferior_TOP'] = 6
globals()['tamano_elementos_verticales_PiezaInferior_TOP'] = 0.2  # mm
globals()['n_elementos_radiales_PiezaInferior_TOP'] = 10

globals()['n_elementos_arcos_PiezaInferior_Medio'] = 6
globals()['n_elementos_verticales_PiezaInferior_Medio'] = 3  # mm
globals()['n_elementos_radiales_PiezaInferior_Medio'] = 10

globals()['n_elementos_arcos_PiezaInferior_BOT'] = 6
globals()['n_elementos_verticales_PiezaInferior_BOT'] = 3  # mm
globals()['n_elementos_radiales_PiezaInferior_BOT'] = 10

globals()['n_elementos_arcos_PiezaInferior_Cilindro'] = 6
globals()['n_elementos_verticales_PiezaInferior_Cilindro'] = 3  # mm
globals()['n_elementos_radiales_PiezaInferior_Cilindro'] = 24

#
globals()['n_elementos_arcos_PiezaSuperior'] = 6
globals()['n_elementos_verticales_PiezaSuperior'] = 3
globals()['n_elementos_radiales_PiezaSuperior'] = 10
#
globals()['n_elementos_arcos_Arandela'] = 6
globals()['n_elementos_verticales_Arandela'] = 3
globals()['n_elementos_radiales_Arandela'] = 10
#
globals()['n_elementos_arcos_RoscaPInf'] = 6
globals()['n_elementos_verticales_RoscaPInf'] = 3
globals()['n_elementos_radiales_RoscaPInf'] = 3
#
globals()['n_elementos_arcos_RoscaTorn'] = 6
globals()['n_elementos_verticales_RoscaTorn'] = 3
globals()['n_elementos_radiales_RoscaTorn'] = 3
#
globals()['n_elementos_arcos_Helicoil'] = 6
globals()['tamano_elementos_verticales_Helicoil'] = 0.1  # mm
globals()['n_elementos_verticales_Helicoil'] = 2 
globals()['tamano_elementos_radiales_Helicoil'] = 0.1  # mm

#########################################################

# === SECUENCIA DE MACROS ===
ejecutar_macro("1_Importacion.py")
ejecutar_macro("2_DivisionesGeometria.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("3_MeshSeed.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("4_Mesh.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("5_RBE3_Cabeza.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("6_RBE3_PiezaInf.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("7_Propiedades.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("8_SD_SolidDeform.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("9_Renumber.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
print(" Proceso completo.")
