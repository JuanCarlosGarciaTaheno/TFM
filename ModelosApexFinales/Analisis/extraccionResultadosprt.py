import re
import pandas as pd
import numpy as np
import os
from openpyxl import load_workbook

# Lista de archivos RPT
archivos_rpt = [
    "AnilloExterior.prt",
    "AnilloInterior.prt",
    "AnilloIntermedio.prt",
    "CuerpoTornillo.prt"

]


regex_bloque = re.compile(
    r"^\s*(\d+)\s+(\d+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s+([\d\.\-E+]+)\s*\n"
    r"\s*([\-\d\.\+E]+)\s+([\d\.\-E+]+)\s+([\d\.\-E]+)",
    re.MULTILINE
)

columnas = [
    "Entity ID",
    "El. Pos. ID",
    "von Mises",
    "X Component",
    "Y Component",
    "Z Component",
    "XY Component",
    "YZ Component",
    "ZX Component",
    "XY Engr. Component",
    "YZ Engr. Component",
    "ZX Engr. Component"
]

archivo_excel = "resultados_tensores.xlsx"

with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
    for archivo in archivos_rpt:
        if not os.path.isfile(archivo):
            print(f"⚠️ Archivo no encontrado: {archivo}")
            continue

        with open(archivo, "r") as f:
            contenido = f.read()

        bloques = regex_bloque.findall(contenido)
        datos = []
        for bloque in bloques:
            # Convertir la tupla de strings a tipos adecuados
            fila = [int(bloque[0]), int(bloque[1])] + [float(x) for x in bloque[2:]]
            datos.append(fila)

        df = pd.DataFrame(datos, columns=columnas)

        # Calcular SigmaVonMises2D
        df['SigmaVonMises2D'] = np.sqrt(
            df['X Component']**2
            - df['X Component'] * df['Y Component']
            + df['Y Component']**2
            + 3 * (df['XY Component']**2)
        )

        # Calcular medias
        medias = df.iloc[:, 2:].mean()
        fila_media = ["Media", ""] + medias.tolist()
        df_final = pd.concat([df, pd.DataFrame([fila_media], columns=df.columns)], ignore_index=True)

        nombre_hoja = os.path.splitext(os.path.basename(archivo))[0]
        df_final.to_excel(writer, sheet_name=nombre_hoja[:31], index=False)

print(f"✅ Todos los datos han sido procesados y exportados a '{archivo_excel}'")



