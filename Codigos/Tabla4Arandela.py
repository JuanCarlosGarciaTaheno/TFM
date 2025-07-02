import pandas as pd

# Ruta del archivo Excel 
excel_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Param_Union_TornHelic.xlsx"

df = pd.read_excel(excel_path, sheet_name="ISO_7089_Arandela")


# Generar el texto con las reglas CATIA
lines = ["Rule Arandela_Rule"]
for i, row in df.iterrows():
    prefix = "if" if i == 0 else "else if"
    lines.append(f"{prefix} Metrica_Seleccionada == {row['`Nominal Size (d)`']:.2f}mm {{")
    for col in df.columns[1:]:
        lines.append(f"   {col} = {row[col]:.3f}mm")
    lines.append("}")

# Unir todas las líneas
rules_text = "\n".join(lines)

# Guardar a archivo
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/CATIA_Reglas_Arandelas.txt"
with open(output_path, "w") as f:
    f.write(rules_text)

output_path



















# Datos de la tabla de arandelas
# data = {
#     "`Nominal Size (d)`": [1.60, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00, 10.00, 12.00, 16.00, 20.00, 24.00, 30.00, 36.00, 42.00, 48.00, 56.00, 64.00],
#     "`Clearance Hole d1 (min)`": [1.70, 2.20, 2.70, 3.20, 4.30, 5.30, 6.40, 8.40, 10.50, 13.00, 17.00, 21.00, 25.00, 31.00, 37.00, 45.00, 52.00, 62.00, 70.00],
#     "`Clearance Hole d1 (max)`": [1.84, 2.34, 2.84, 3.38, 4.48, 5.48, 6.62, 8.62, 10.77, 13.27, 17.27, 21.33, 25.33, 31.39, 37.62, 45.62, 52.74, 62.74, 70.74],
#     "`Outside d2 (nom)`": [4.00, 5.00, 6.00, 7.00, 9.00, 10.00, 12.00, 16.00, 20.00, 24.00, 30.00, 37.00, 44.00, 56.00, 66.00, 78.00, 92.00, 105.00, 115.00],
#     "`d2 (min)`": [3.70, 4.70, 5.70, 6.64, 8.64, 9.64, 11.57, 15.57, 19.48, 23.48, 29.48, 36.38, 43.38, 55.26, 64.80, 76.80, 90.60, 103.60, 113.60],
#     "`Thickness h (nom)`": [0.30, 0.30, 0.50, 0.50, 0.80, 1.00, 1.60, 1.60, 2.00, 2.50, 3.00, 3.00, 4.00, 4.00, 5.00, 8.00, 8.00, 10.00, 10.00],
#     "`h (max)`": [0.35, 0.35, 0.55, 0.55, 0.90, 1.10, 1.80, 1.80, 2.20, 2.70, 3.30, 3.30, 4.30, 4.30, 5.60, 9.00, 9.00, 11.00, 11.00],
#     "`h (min)`": [0.25, 0.25, 0.45, 0.45, 0.70, 0.90, 1.40, 1.40, 1.80, 2.30, 2.70, 2.70, 3.70, 3.70, 4.40, 7.00, 7.00, 9.00, 9.00]
# }