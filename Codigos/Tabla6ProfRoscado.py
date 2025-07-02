import pandas as pd

# Ruta del archivo Excel
excel_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Param_Union_TornHelic.xlsx"

df = pd.read_excel(excel_path, sheet_name="e1_ProfRoscado")

# Eliminar espacios en los encabezados 
df.columns = df.columns.str.strip()

# Generar las líneas para la regla
lines = ["Rule Empiece_Rosca_Rule"]
for i, row in df.iterrows():
    prefix = "if" if i == 0 else "else if"
    lines.append(f"{prefix} Paso == {float(row['Thread pitch, P']):.2f} {{")
    for col in df.columns[1:]:
        try:
            value = float(row[col])
            lines.append(f"   {col.replace(' ', '')} = {value:.3f}mm")
        except (ValueError, TypeError):
            lines.append(f"   {col.replace(' ', '')} = 0.000mm  // Valor inválido en Excel")
    lines.append("}")

# Unir y guardar
rules_text = "\n".join(lines)
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/CATIA_Reglas_ProfRoscado.txt"
with open(output_path, "w") as f:
    f.write(rules_text)

print("Archivo generado correctamente:", output_path)

















# # # Datos de la tabla de empieces de rosca
# # data = {
# #     "Thread pitch, P": [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.75, 0.8, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
# #     "e1_Normal": [1.3, 1.5, 1.8, 2.1, 2.3, 2.6, 2.8, 3.4, 3.8, 4.0, 4.2, 5.1, 6.2, 7.3, 8.3, 9.3, 11.2, 13.1, 15.2, 16.8, 18.4, 20.8, 22.4, 24],
# #     "e2_Short": [0.8, 1, 12, 1.3, 1.5, 1.6, 1.8, 2.1, 2.4, 2.5, 2.7, 3.2, 3.9, 4.6, 5.2, 5.8, 7, 8.2, 9.5, 10.5, 11.5, 13, 14, 15],
# #     "e3_Long": [2, 2.4, 2.9, 3.3, 3.7, 4.1, 4.5, 5.4, 6.1, 6.4, 6.8, 8.2, 10, 11.6, 13.3, 14.8, 17.9, 21, 24.3, 26.9, 29.4, 33.3, 35.8, 38.4]
# # }
