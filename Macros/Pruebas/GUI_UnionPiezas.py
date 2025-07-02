import tkinter as tk
from tkinter import filedialog, messagebox

def guardar_variables():
    try:
        globals()['ruta_step'] = entry_vars['ruta_step'].get()

        for nombre, entry in entry_vars.items():
            if nombre == 'ruta_step':
                continue
            valor = float(entry.get()) if '.' in entry.get() else int(entry.get())
            globals()[nombre] = valor

        messagebox.showinfo("Éxito", "Variables guardadas en el entorno global.")
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar las variables:\n{e}")

root = tk.Tk()
root.title("Configuración de Variables de Mallado y Seed")
root.geometry("600x800")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(frame, yscrollcommand=scroll.set)
scroll.config(command=canvas.yview)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

entry_vars = {}

variables = {
    'ruta_step': 'Ruta del archivo STEP',
    'tamano_malla_tornillo': 'Tamaño malla Tornillo (mm)',
    'tamano_malla_PiezaInferior': 'Tamaño malla Pieza Inferior (mm)',
    'tamano_malla_PiezaSuperior': 'Tamaño malla Pieza Superior (mm)',
    'tamano_malla_Arandela': 'Tamaño malla Arandela (mm)',
    'tamano_malla_RoscaTornillo': 'Tamaño malla Rosca Tornillo (mm)',
    'tamano_malla_RoscaPInferior': 'Tamaño malla Rosca P. Inferior (mm)',
    'tamano_malla_Helicoil': 'Tamaño malla Helicoil (mm)',

    'n_elementos_arcos_Tornillo': 'Elementos arco Tornillo',
    'n_elementos_verticales_CABEZA': 'Elementos verticales Cabeza',
    'n_elementos_verticales_CuerpoTorn': 'Elementos verticales Cuerpo Tornillo',
    'n_elementos_radiales_Tornillo': 'Elementos radiales Tornillo',

    'n_elementos_arcos_PiezaInferior': 'Elementos arco P. Inferior',
    'tamano_elementos_verticales_PiezaInferiorRosca': 'Tamaño verticales P. Inf. Rosca (mm)',
    'n_elementos_verticales_PiezaInferior': 'Elementos verticales P. Inferior',
    'n_elementos_radiales_PiezaInferior': 'Elementos radiales P. Inferior',

    'n_elementos_arcos_PiezaSuperior': 'Elementos arco P. Superior',
    'n_elementos_verticales_PiezaSuperior': 'Elementos verticales P. Superior',
    'n_elementos_radiales_PiezaSuperior': 'Elementos radiales P. Superior',

    'n_elementos_arcos_Arandela': 'Elementos arco Arandela',
    'n_elementos_verticales_Arandela': 'Elementos verticales Arandela',
    'n_elementos_radiales_Arandela': 'Elementos radiales Arandela',

    'n_elementos_arcos_RoscaPInf': 'Elementos arco Rosca P. Inf.',
    'n_elementos_verticales_RoscaPInf': 'Elementos verticales Rosca P. Inf.',
    'n_elementos_radiales_RoscaPInf': 'Elementos radiales Rosca P. Inf.',

    'n_elementos_arcos_RoscaTorn': 'Elementos arco Rosca Torn.',
    'n_elementos_verticales_RoscaTorn': 'Elementos verticales Rosca Torn.',
    'n_elementos_radiales_RoscaTorn': 'Elementos radiales Rosca Torn.',

    'n_elementos_arcos_Helicoil': 'Elementos arco Helicoil',
    'tamano_elementos_verticales_Helicoil': 'Tamaño verticales Helicoil (mm)',
    'tamano_elementos_radiales_Helicoil': 'Tamaño radiales Helicoil (mm)',
}

for i, (var, label_text) in enumerate(variables.items()):
    label = tk.Label(inner_frame, text=label_text)
    label.grid(row=i, column=0, sticky='w', pady=2)
    entry = tk.Entry(inner_frame, width=30)
    entry.grid(row=i, column=1, pady=2)
    entry_vars[var] = entry

    # Default values (can be modified)
    if 'tamano' in var:
        entry.insert(0, '0.2')
    elif 'ruta_step' in var:
        entry.insert(0, '')
    else:
        entry.insert(0, '6')

# Botón para seleccionar ruta del archivo STEP

def seleccionar_ruta():
    ruta = filedialog.askopenfilename(filetypes=[("STEP files", "*.step;*.stp"), ("All files", "*.*")])
    if ruta:
        entry_vars['ruta_step'].delete(0, tk.END)
        entry_vars['ruta_step'].insert(0, ruta)

btn_ruta = tk.Button(inner_frame, text="Seleccionar archivo STEP", command=seleccionar_ruta)
btn_ruta.grid(row=len(variables)+1, column=0, columnspan=2, pady=10)

btn_guardar = tk.Button(inner_frame, text="Guardar y cerrar", command=guardar_variables)
btn_guardar.grid(row=len(variables)+2, column=0, columnspan=2, pady=10)

inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
