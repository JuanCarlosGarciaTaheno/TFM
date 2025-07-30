import pandas as pd

# Ruta del archivo Excel que contiene la hoja "Rosca"
excel_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Param_Union_TornHelic.xlsx"

# Leer la hoja llamada "Rosca0"
df = pd.read_excel(excel_path, sheet_name="Rosca0")

# Lista de columnas que deben mostrarse en mm²
columnas_mm2 = ["Area_Tension", "Area_Corte"]  # ← Ajusta estos nombres a los reales en tu hoja

# Generar el texto con las reglas CATIA
lines = ["Rule Tornillo_Metrico_Rule"]
for i, row in df.iterrows():
    prefix = "if" if i == 0 else "else if"
    lines.append(f"{prefix} Metrica_Seleccionada == {row['Metrica']}mm {{")
    lines.append(f"   Metrica = {row['Metrica']:.3f}mm")  # Línea adicional
    for col in df.columns[1:]:
        try:
            valor = float(row[col])
            unidad = "mm2" if col in columnas_mm2 else "mm"
            lines.append(f"   {col} = {valor:.3f}{unidad}")
        except (ValueError, TypeError):
            lines.append(f"   {col} = {row[col]}")
    lines.append("}")

# Unir todas las líneas
rules_text = "\n".join(lines)

# Guardar a archivo
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/CATIA_Reglas_Metricas.txt"
with open(output_path, "w") as f:
    f.write(rules_text)

print(f"Archivo generado correctamente en: {output_path}")
