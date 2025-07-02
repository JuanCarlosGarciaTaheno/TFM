import pandas as pd

# Leer el archivo Excel (ajusta la ruta y nombre de archivo)
excel_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/LongitudRosca.xlsx"
df = pd.read_excel(excel_path)

# Convertir columnas numéricas (reemplaza comas por puntos y convierte a float)
numeric_cols = ['l_nominal', 'l_min', 'l_max'] + \
               [f"{m}_{t}" for m in ['M1_6', 'M2', 'M2_5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 
                                    'M12', 'M14', 'M16', 'M20', 'M24', 'M30', 'M36', 'M42', 
                                    'M48', 'M56', 'M64'] 
                for t in ['ls_min', 'lg_max']]

for col in numeric_cols:
    if col in df.columns:
        # Reemplazar comas por puntos y convertir a float
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# Lista de todas las métricas disponibles en la tabla
metricas = [
    'M1_6', 'M2', 'M2_5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12',
    'M14', 'M16', 'M20', 'M24', 'M30', 'M36', 'M42', 'M48', 'M56', 'M64'
]

# Generar el texto con las reglas CATIA para longitudes de rosca
lines = ["Rule Longitud_Rosca_Rule"]

for i, row in df.iterrows():
    prefix = "if" if i == 0 else "else if"
    
    # Formatear valores numéricos asegurando que sean floats
    try:
        l_nominal = float(row['l_nominal'])
        lines.append(f"{prefix} LongitudNominal == {l_nominal:.2f} {{")
    except (ValueError, TypeError):
        lines.append(f"{prefix} LongitudNominal == {row['l_nominal']} {{")
    
    try:
        l_min = float(row['l_min'])
        lines.append(f"   l_min = {l_min:.2f}mm")
    except (ValueError, TypeError):
        lines.append(f"   l_min = {row['l_min']}mm")
    
    try:
        l_max = float(row['l_max'])
        lines.append(f"   l_max = {l_max:.2f}mm")
    except (ValueError, TypeError):
        lines.append(f"   l_max = {row['l_max']}mm")
    
    for metrica in metricas:
        ls_min_col = f"{metrica}_ls_min"
        lg_max_col = f"{metrica}_lg_max"
        
        if ls_min_col in df.columns and lg_max_col in df.columns:
            try:
                ls_min = float(row[ls_min_col])
                ls_min_str = f"{ls_min:.2f}mm"
            except (ValueError, TypeError):
                ls_min_str = f"{row[ls_min_col]}mm"
            
            try:
                lg_max = float(row[lg_max_col])
                lg_max_str = f"{lg_max:.2f}mm"
            except (ValueError, TypeError):
                lg_max_str = f"{row[lg_max_col]}mm"
            
            # Solo incluir si hay valores diferentes de cero o no son NaN
            if pd.notna(row[ls_min_col]) and (float(row[ls_min_col]) != 0 or 
               (pd.notna(row[lg_max_col]) and float(row[lg_max_col]) != 0)):
                lines.append(f"   {ls_min_col} = {ls_min_str}")
                lines.append(f"   {lg_max_col} = {lg_max_str}")
    
    lines.append("}")

# Añadir un caso else por defecto al final
lines.append("else {")
lines.append("   // Valores por defecto cuando no hay coincidencia")
lines.append("   l_min = 0.00mm")
lines.append("   l_max = 0.00mm")
for metrica in metricas:
    lines.append(f"   {metrica}_ls_min = 0.00mm")
    lines.append(f"   {metrica}_lg_max = 0.00mm")
lines.append("}")

# Unir todas las líneas
rules_text = "\n".join(lines)

# Guardar a archivo
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/CATIA_Reglas_Longitud_Rosca.txt"
with open(output_path, "w", encoding='utf-8') as f:
    f.write(rules_text)

print(f"Archivo generado exitosamente en: {output_path}")