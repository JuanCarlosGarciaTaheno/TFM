from collections import defaultdict
import os
import re

nombres_partes = {
    1: "Tornillo",
    2: "Arandela",
    3: "Pieza_Superior",
    4: "Pieza_Inferior", 
    5: "Helicoil",
    6: "Rosca_Tornillo",
    7: "RoscaPiezaInferior"
}

materiales = """
$ Referenced Material Records
$ Material Record : Aluminio
$ Description of Material : Date: 25-Apr-25           Time: 11:52:45
MAT1*    1               6.8900004+10    2.5902256+10    .33
*        2700.           2.3500001-5     19.85
$ Material Record : Acero
$ Description of Material : Date: 25-Apr-25           Time: 11:52:45
MAT1*    3               2.+11           7.751938+10     .29
*        8000.           1.6800001-5     19.85
$ Material Record : Helicoil
$ Description of Material : Date: 25-Apr-25           Time: 11:52:45
MAT1*    2               1.18+11         4.402985+10     .34
*        8800.           1.8000001-5     19.85
"""

material_por_parte = {
    1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 3, 7: 1
}

def separar_combinar_materiales_rbes(ruta_entrada, carpeta_salida):
    if not os.path.isfile(ruta_entrada):
        print("La ruta proporcionada no corresponde a un archivo existente.")
        return

    os.makedirs(carpeta_salida, exist_ok=True)
    chexas_por_parte = defaultdict(list)
    nodos_por_parte = defaultdict(set)
    rbes = []
    nodos_usados_rbes = set()
    grids = {}

    with open(ruta_entrada, 'r') as archivo:
        lineas = archivo.readlines()

    # Recolectar todos los GRID del archivo
    for linea in lineas:
        if linea.strip().startswith('GRID'):
            match = re.match(r'GRID\s+(\d+)', linea.strip())
            if match:
                grid_id = int(match.group(1))
                grids[grid_id] = linea

        # Recolectar CHEXA y CPENTA, y nodos por parte - Versión generalizada
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if any(linea.strip().startswith(elem) for elem in ['CHEXA', 'CPENTA']):
            partes_linea = re.split(r'[,\s]+', linea.strip())
            try:
                tipo_elem = partes_linea[0]
                part_id = int(partes_linea[2])
                bloque_elem = [linea]

                # Extraer nodos de la línea inicial
                nodos = list(map(int, [n for n in partes_linea[3:] if n.isdigit()]))

                # Procesar líneas de continuación
                j = i + 1
                while j < len(lineas) and lineas[j].strip().startswith('+'):
                    cont_linea = lineas[j]
                    bloque_elem.append(cont_linea)
                    cont_nodos = re.findall(r'\d+', cont_linea)
                    nodos.extend(map(int, cont_nodos))
                    j += 1

                # Asignar a la parte correspondiente
                nodos_por_parte[part_id].update(nodos)
                chexas_por_parte[part_id].extend(bloque_elem)  # puedes cambiar el nombre si ahora contiene ambos
                i = j
                continue
            except (ValueError, IndexError):
                pass
        i += 1


    # Recolectar RBE2/RBE3 - Versión mejorada
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if linea.strip().startswith(('RBE2', 'RBE3')):
            bloque = [linea]
            # Extraer nodos de la línea principal
            partes_linea = re.split(r'[,\s]+', linea.strip())
            nodos = list(map(int, [n for n in partes_linea[1:] if n.isdigit()]))
            nodos_usados_rbes.update(nodos)
            
            # Procesar líneas de continuación
            j = i + 1
            while j < len(lineas) and (lineas[j].strip().startswith('+') or lineas[j].strip().startswith('*')):
                cont_linea = lineas[j]
                bloque.append(cont_linea)
                cont_nodos = re.findall(r'\d+', cont_linea)
                nodos_usados_rbes.update(map(int, cont_nodos))
                j += 1
            
            rbes.extend(bloque)
            i = j
            continue
        i += 1

    resumen_path = os.path.join(carpeta_salida, 'resumen_solidos.txt')
    combinado_path = os.path.join(carpeta_salida, 'partes_combinadas.bdf')
    materiales_path = os.path.join(carpeta_salida, 'materiales_propiedades.bdf')
    rbe3_path = os.path.join(carpeta_salida, 'RBE3.bdf')

    with open(resumen_path, 'w') as resumen, \
         open(combinado_path, 'w') as combinado, \
         open(materiales_path, 'w') as matfile, \
         open(rbe3_path, 'w') as rbeout:

        resumen.write("Resumen de archivos generados por parte:\n\n")
        matfile.write(materiales.strip() + "\n\n")

        for part_id in sorted(chexas_por_parte.keys()):
            if part_id in nombres_partes:
                nombre = nombres_partes[part_id]
                nombre_base = f'{part_id:02d}_{nombre}'
                ruta_bdf = os.path.join(carpeta_salida, f'{nombre_base}.bdf')
                ruta_txt = os.path.join(carpeta_salida, f'{nombre_base}.txt')
                chexas = chexas_por_parte[part_id]
                nodos = nodos_por_parte[part_id]
                
                # Asegurarse de incluir todos los nodos necesarios
                grids_usados = []
                for nid in sorted(nodos):
                    if nid in grids:
                        grids_usados.append(grids[nid])
                    else:
                        print(f"Advertencia: Nodo {nid} referenciado en parte {part_id} no encontrado en GRIDs")

                with open(ruta_bdf, 'w') as f_bdf, open(ruta_txt, 'w') as f_txt:
                    f_bdf.writelines(chexas)
                    f_bdf.write("\n")
                    f_bdf.writelines(grids_usados)
                    f_txt.writelines(chexas)
                    f_txt.write("\n")
                    f_txt.writelines(grids_usados)

                combinado.write(f"$ Parte {part_id} : {nombre}\n")
                combinado.writelines(chexas)
                combinado.write("\n")
                combinado.writelines(grids_usados)
                combinado.write("\n\n")

                resumen.write(f"{nombre_base}.bdf y .txt\n")

                id_prop = part_id
                id_mat = material_por_parte.get(part_id, 1)
                nombre_prop = f"$3D_{nombre}"
                matfile.write(f"PSOLID,{id_prop},{id_mat},,,,,{nombre_prop}\n")

        # Escribir nodos usados en RBE2/RBE3
        rbeout.write("$ NODOS USADOS EN RBE2/RBE3\n")
        for nid in sorted(nodos_usados_rbes):
            if nid in grids:
                rbeout.write(grids[nid])
            else:
                print(f"Advertencia: Nodo {nid} usado en RBE2/RBE3 no encontrado en GRIDs")
        rbeout.write("\n$ RBE2 / RBE3 encontrados:\n")
        rbeout.writelines(rbes)

    return resumen_path, combinado_path, materiales_path, rbe3_path

#C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\Sketchs_Apex\ApexImport\Patran\M4_MaxSepElimRosca\TratamientoBDF
# Rutas

# ruta_bdf = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bdf"
# carpeta_salida = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd"

ruta_bdf = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MediaSeparacionFinal.bdf"
carpeta_salida = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MediaSeparacionFinal.bd"

separar_combinar_materiales_rbes(ruta_bdf, carpeta_salida)



#C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/ApexImport/Patran/Mod_2_MinimaSeparacion

#c:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/ApexImport/Patran/Mod_2_MaximaSeparacion/M4_MaximaSeparacion.bdf


#c:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Sketchs_Apex/ApexImport/Patran/Mod_2_MaximaSeparacion/M4_MaximaSeparacion_RBE3.bdf
