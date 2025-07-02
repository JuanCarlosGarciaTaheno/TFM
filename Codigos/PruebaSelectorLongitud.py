import tkinter as tk
from tkinter import ttk
import pandas as pd

# Cargar Excel
ruta_excel = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/Param_Union_TornHelic.xlsx"
hoja = "Long_Roscado"
df = pd.read_excel(ruta_excel, sheet_name=hoja)

# Lista de métricas válidas y longitudes nominales
metricas_disponibles = ['M2_5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12', 'M16']
longitudes_nominales = [2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 45, 50,
                        55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160,
                        180, 200, 220, 240, 260, 280, 300]

opciones_columna = {
    "Opcion_longitud_nominal": "ls_min",
    "Opcion_longitud_max": "ls_max",
    "Opcion_longitud_min": "ls_min"
}

def obtener_valores():
    metrica = combo_metrica.get()
    longitud = float(combo_longitud.get())
    opcion = combo_opcion.get()

    sufijo_ls = opciones_columna[opcion]
    columna_ls = f"{metrica}_{sufijo_ls}"
    columna_lg = f"{metrica}_lg_max"

    # Filtrar por longitud
    fila = df[df['l_nominal'] == longitud]

    try:
        valor_ls = fila[columna_ls].values[0]
    except KeyError:
        valor_ls = "No encontrado"
    except IndexError:
        valor_ls = "Longitud no encontrada"

    try:
        valor_lg = fila[columna_lg].values[0]
    except KeyError:
        valor_lg = "No encontrado"
    except IndexError:
        valor_lg = "Longitud no encontrada"

    # Mostrar resultados
    resultado.config(text=f"ls: {valor_ls}\nlg: {valor_lg}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Selector de Métrica y Longitud")
ventana.geometry("400x300")

# Widgets
tk.Label(ventana, text="Selecciona la métrica:").pack()
combo_metrica = ttk.Combobox(ventana, values=metricas_disponibles)
combo_metrica.set("M4")
combo_metrica.pack()

tk.Label(ventana, text="Selecciona la longitud nominal:").pack()
combo_longitud = ttk.Combobox(ventana, values=longitudes_nominales)
combo_longitud.set("30")
combo_longitud.pack()

tk.Label(ventana, text="Selecciona la opción de longitud:").pack()
combo_opcion = ttk.Combobox(ventana, values=list(opciones_columna.keys()))
combo_opcion.set("Opcion_longitud_nominal")
combo_opcion.pack()

btn_calcular = tk.Button(ventana, text="Obtener valores", command=obtener_valores)
btn_calcular.pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

ventana.mainloop()