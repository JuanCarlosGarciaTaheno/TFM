import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
ruta_excel = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Param_Union_TornHelic.xlsx"  # Cambia esta ruta por la de tu archivo
hoja = "Long_Roscado"  # Especifica el nombre de la hoja que deseas cargar

# Cargar los datos de la hoja específica del archivo Excel
df = pd.read_excel(ruta_excel, sheet_name=hoja)

# Mostrar las primeras filas del DataFrame para verificar los datos
print(df.head())




# Ahora, proceder con la selección de la métrica y la longitud
metrica_seleccionada = "M4_ls_min"  # Ejemplo de métrica
longitud_seleccionada = 30  # Ejemplo de longitud seleccionada

# Filtrar los datos con la longitud seleccionada
longitud_datos = df[df['l_nominal'] == longitud_seleccionada]

# Intentar obtener el valor de 'ls' de la columna seleccionada
try:
    valor_ls = longitud_datos[metrica_seleccionada].values[0]  # Asumiendo que solo hay un valor
except KeyError:
    print(f"Columna {metrica_seleccionada} no encontrada.")
    valor_ls = None

valor_ls = longitud_datos[metrica_seleccionada].values[0]  # p.ej., M1_6_ls_min
metrica_lg = metrica_seleccionada.replace('ls_min', 'lg_max')  # M1_6_lg_max
valor_lg = longitud_datos[metrica_lg].values[0]
try:
    valor_lg = longitud_datos[metrica_lg].values[0]  # Intentamos obtener el valor de 'lg'
except KeyError:
    print(f"Columna {metrica_lg} no encontrada.")
    valor_lg = None

# Imprimir los resultados
print(f"Para la métrica {metrica_seleccionada} y longitud {longitud_seleccionada}:")
if valor_ls is not None:
    print(f"ls: {valor_ls}")
if valor_lg is not None:
    print(f"lg: {valor_lg}")