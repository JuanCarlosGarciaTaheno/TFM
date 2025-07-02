import pandas as pd

# Datos de la tabla de longitudes de rosca (ajusta los valores según tu tabla exacta)
data = {
    "l_nominal": [2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 240, 260, 280, 300],
    "l_min": [2.3, 2.8, 3.76, 4.76, 5.76, 7.71, 9.71, 11.65, 15.65, 19.58, 24.58, 29.58, 34.5, 39.5, 44.5, 49.5, 54.4, 59.4, 64.4, 69.4, 79.4, 89.3, 99.3, 109.3, 119.3, 129.2, 139.2, 149.2, 159.2, 179.2, 199.07, 219.07, 239.07, 258.95, 278.95, 298.95],
    "l_max": [2.7, 3.2, 4.24, 5.24, 6.24, 8.29, 10.29, 12.35, 16.35, 20.42, 25.42, 30.42, 35.5, 40.5, 45.5, 50.5, 55.6, 60.6, 65.6, 70.6, 80.6, 90.7, 100.7, 110.7, 120.7, 130.8, 140.8, 150.8, 160.8, 180.8, 200.92, 220.92, 240.92, 261.05, 281.05, 301.05],
    "M1_6_ls_min": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "M1_6_lg_max": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "M2_ls_min": [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "M2_lg_max": [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ... (completar con el resto de columnas de la tabla)
    # Ejemplo de cómo continuarías con las otras métricas
    "M2_5_ls_min": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5.75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "M2_5_lg_max": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # Continuar con todas las métricas necesarias
}

df = pd.DataFrame(data)

# Lista de métricas disponibles (ajusta según tus columnas)
metricas = ['M1_6', 'M2', 'M2_5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12', 
             'M14', 'M16', 'M20', 'M24', 'M30', 'M36', 'M42', 'M48', 'M56', 'M64']

# Generar el texto con las reglas CATIA para longitudes de rosca
lines = ["Rule Longitud_Rosca_Rule"]

for i, row in df.iterrows():
    prefix = "if" if i == 0 else "else if"
    lines.append(f"{prefix} LongitudNominal == {row['l_nominal']:.2f} {{")
    lines.append(f"   l_min = {row['l_min']:.2f}mm")
    lines.append(f"   l_max = {row['l_max']:.2f}mm")
    
    for metrica in metricas:
        ls_min = row[f"{metrica}_ls_min"]
        lg_max = row[f"{metrica}_lg_max"]
        if ls_min != 0 or lg_max != 0:  # Solo incluir si hay valores diferentes de cero
            lines.append(f"   {metrica}_ls_min = {ls_min:.2f}mm")
            lines.append(f"   {metrica}_lg_max = {lg_max:.2f}mm")
    
    lines.append("}")

# Unir todas las líneas
rules_text = "\n".join(lines)

# Guardar a archivo (ajusta la ruta según necesites)
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Codigos/CATIA_Reglas_Longitud_Rosca.txt"
with open(output_path, "w") as f:
    f.write(rules_text)

print(f"Archivo generado exitosamente en: {output_path}")