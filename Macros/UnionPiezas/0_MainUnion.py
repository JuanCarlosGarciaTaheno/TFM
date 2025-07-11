import apex
import math
import os
#apex.disableShowOutput()

# Configuraciones basicas 
apex.setScriptUnitSystem(unitSystemName='mm-kg-s-N-K')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = True
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Fine
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry=applicationSettingsGeometry)

# === CONFIGURACION INICIAL ===
#ruta_step = "C:\\Users\\jc.garcia-taheno\\Desktop\\CE_3_TahenoHijes\\Sketchs_Apex\\Product\\M4_SeparacionMedia.stp"
# M4_MaxSep_Apriete
# M4_MinimaSeparacionApriete.stp
# M4_SeparacionMedia

ruta_step = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/Product/Prueba.stp"


# === RUTA DE LAS MACROS ===
ruta_macros = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Macros/UnionPiezas"


def ejecutar_macro(nombre_macro):
    print(f"Ejecutando {nombre_macro}...")
    ruta_macro = os.path.join(ruta_macros, nombre_macro)
    with open(ruta_macro, "r", encoding="utf-8") as archivo:  # utf-8 o "latin-1" si da problemas
        codigo = archivo.read()
    exec(codigo, globals())
    

#########################################################
# === VARIABLES GLOBALES QUE USAN LOS SCRIPTS ===

globals()['ruta_step'] = ruta_step

#########################################################
#               VARIABLES Mallado
#########################################################

globals()['tamano_malla_tornillo'] = 0.5  # en mm 
globals()['tamano_malla_PiezaInferior'] = 0.2  # en mm 
globals()['tamano_malla_PiezaSuperior'] = 0.2  # en mm 
globals()['tamano_malla_Arandela'] = 0.2  # en mm 
globals()['tamano_malla_RoscaTornillo'] = 0.2  # en mm 
globals()['tamano_malla_RoscaPInferior'] = 0.2  # en mm 
globals()['tamano_malla_Helicoil'] = 0.2  # en mm 



#########################################################
#               VARIABLES Mesh Seed
#########################################################

globals()['n_elementos_arcos_Tornillo'] = 6
globals()['n_elementos_verticales_CABEZA'] = 3
globals()['n_elementos_verticales_CuerpoTorn'] = 50
globals()['n_elementos_radiales_Tornillo'] = 5

globals()['n_elementos_arcos_PiezaInferior'] = 6
globals()['tamano_elementos_verticales_PiezaInferiorRosca'] = 0.2  # mm
globals()['n_elementos_verticales_PiezaInferior'] = 3
globals()['n_elementos_radiales_PiezaInferior'] = 10

globals()['n_elementos_arcos_PiezaSuperior'] = 6
globals()['n_elementos_verticales_PiezaSuperior'] = 3
globals()['n_elementos_radiales_PiezaSuperior'] = 10

globals()['n_elementos_arcos_Arandela'] = 6
globals()['n_elementos_verticales_Arandela'] = 3
globals()['n_elementos_radiales_Arandela'] = 10

globals()['n_elementos_arcos_RoscaPInf'] = 6
globals()['n_elementos_verticales_RoscaPInf'] = 3
globals()['n_elementos_radiales_RoscaPInf'] = 3

globals()['n_elementos_arcos_RoscaTorn'] = 6
globals()['n_elementos_verticales_RoscaTorn'] = 3
globals()['n_elementos_radiales_RoscaTorn'] = 3

globals()['n_elementos_arcos_Helicoil'] = 6
#globals()['tamano_elementos_verticales_Helicoil'] = 0.1  # mm
globals()['n_elementos_verticales_Helicoil'] = 2  
globals()['tamano_elementos_radiales_Helicoil'] = 0.1  # mm

#########################################################

# === SECUENCIA DE MACROS ===

ejecutar_macro("1_Importacion.py")
ejecutar_macro("2_UnionDivisionGeometria.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("3_MeshSeed_UnionPiezas.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("4_MeshUnion.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("5_RBE3_CABEZA_Union.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("6_RBE3_PiezaInf_Union.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("7_PropiedadesUnion.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("8_SD_SolidDeformUnion.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()
ejecutar_macro("9_Renumeracion.py")
assembly_1 = apex.getAssembly(pathName=apex.currentModel().name + "/Union_Apex")
assembly_1.show()

print("Proceso completo.")
