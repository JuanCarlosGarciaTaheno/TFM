# import math
# import re

# def convertir_float_campos_nastran(valor_str):
#     valor_str = valor_str.strip()
#     if valor_str.startswith('.'):
#         valor_str = '0' + valor_str

#     match = re.match(r'^([+-]?\d+)\.([+-]?\d+)$', valor_str)
#     if match:
#         base, exponente = match.groups()
#         valor_str = f"{base}E{exponente}"

#     if re.match(r'^[+-]?\d*\.?\d+[+-]\d+$', valor_str):
#         for i in range(1, len(valor_str)):
#             if valor_str[i] in '+-' and valor_str[i-1].isdigit():
#                 valor_str = valor_str[:i] + 'E' + valor_str[i:]
#                 break

#     try:
#         return float(valor_str)
#     except ValueError:
#         print(f"¡Error al convertir '{valor_str}' a float! Se devuelve 0.0")
#         return 0.0

# def float_a_nastran_corto(valor):
#     for decimales in range(5, 2, -1):
#         s = f"{valor:.{decimales}E}"
#         base, exp = s.split('E')
#         signo_exp = '+' if int(exp) >= 0 else '-'
#         exp_abs = str(abs(int(exp)))
#         compact = f"{base}{signo_exp}{exp_abs}"
#         if len(compact) <= 8:
#             return compact.rjust(8)
#     return f"{valor:.1E}".replace('E', '').rjust(8)

# def float_a_nastran_largo(valor):
#     for decimales in range(12, 5, -1):
#         s = f"{valor:.{decimales}E}"
#         base, exp = s.split('E')
#         signo_exp = '+' if int(exp) >= 0 else '-'
#         exp_abs = f"{abs(int(exp)):02}"
#         sin_e = f"{base}{signo_exp}{exp_abs}"
#         if len(sin_e) <= 16:
#             return sin_e.rjust(16)
#     return f"{valor:.7E}".replace('E', '').rjust(16)

# def rotar_xy(x, y, angulo_grados):
#     theta = math.radians(angulo_grados)
#     x_rot = x * math.cos(theta) + y * math.sin(theta)
#     y_rot = -x * math.sin(theta) + y * math.cos(theta)
#     return x_rot, y_rot

# def rotar_grid_en_bdf(archivo_entrada, archivo_salida, angulo_grados, formato='corto'):
#     with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
#         line_buffer = ""
#         for linea in f_in:
#             if linea.strip().startswith('GRID*'):  # Formato largo
#                 line_buffer = linea.rstrip()
#                 continue
#             elif line_buffer.startswith('GRID*') and linea.strip().startswith('*'):
#                 segunda_linea = linea.rstrip()

#                 id_nodo = int(line_buffer[8:16].strip())
#                 x = convertir_float_campos_nastran(line_buffer[32:48])
#                 y = convertir_float_campos_nastran(line_buffer[48:64])
#                 z = convertir_float_campos_nastran(segunda_linea[8:24])

#                 x_rot, y_rot = rotar_xy(x, y, angulo_grados)

#                 nueva_linea1 = (
#                     "GRID*   " + f"{id_nodo:>8}" + "                        " +
#                     float_a_nastran_largo(x_rot) + float_a_nastran_largo(y_rot)
#                 )
#                 nueva_linea2 = "*       " + float_a_nastran_largo(z)

#                 f_out.write(nueva_linea1 + '\n')
#                 f_out.write(nueva_linea2 + '\n')

#                 line_buffer = ""
#                 continue

#             elif linea.strip().startswith('GRID'):  # Formato corto
#                 try:
#                     # Extraer números reales de la línea con regex para evitar problemas si están pegados
#                     numeros = re.findall(r'[+-]?\d*\.\d+|[+-]?\d+', linea)
#                     # Extraer el ID del nodo (primer entero que aparezca)
#                     id_nodo_match = re.search(r'GRID\s+(\d+)', linea)
#                     if id_nodo_match:
#                         id_nodo = int(id_nodo_match.group(1))
#                     else:
#                         raise ValueError("No se encontró ID de nodo")

#                     if len(numeros) < 3:
#                         raise ValueError(f"No hay suficientes coordenadas en la línea: {linea.strip()}")

#                     x = float(numeros[0])
#                     y = float(numeros[1])
#                     z = float(numeros[2])

#                     x_rot, y_rot = rotar_xy(x, y, angulo_grados)

#                     if formato == 'corto':
#                         # Reconstruir la línea manteniendo el formato original excepto las coordenadas
#                         # Esto asume que el ID y los campos antes de x están fijos o al menos se mantienen
#                         # Aquí simplificamos y reescribimos la línea completa:
#                         campos = linea.rstrip('\n').split()
#                         # campos[0] = 'GRID', campos[1] = id_nodo
#                         # Las coordenadas suelen estar en campos[2], [3], [4]
#                         if len(campos) >= 5:
#                             campos[2] = float_a_nastran_corto(x_rot).strip()
#                             campos[3] = float_a_nastran_corto(y_rot).strip()
#                             campos[4] = float_a_nastran_corto(z).strip()
#                             nueva_linea = '{:<8}{:>8}{:>8}{:>8}{:>8}'.format(
#                                 campos[0], int(campos[1]), campos[2], campos[3], campos[4]
#                             )
#                         else:
#                             # Si no están todos los campos, escribir con espacios mínimos
#                             nueva_linea = f"GRID    {id_nodo:<8}{float_a_nastran_corto(x_rot)}{float_a_nastran_corto(y_rot)}{float_a_nastran_corto(z)}"
#                         f_out.write(nueva_linea + '\n')

#                     elif formato == 'largo':
#                         nueva_linea1 = (
#                             "GRID*   " + f"{id_nodo:>8}" + " " * 24 +
#                             float_a_nastran_largo(x_rot) + float_a_nastran_largo(y_rot)
#                         )
#                         nueva_linea2 = "*       " + float_a_nastran_largo(z)
#                         f_out.write(nueva_linea1 + '\n')
#                         f_out.write(nueva_linea2 + '\n')

#                 except Exception as e:
#                     print(f"Error en línea GRID ID {linea}: {e}")
#                     f_out.write(linea)
#             else:
#                 f_out.write(linea)







# entrada_01 = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/01_Tornillo.bdf"
# entrada_06 = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/06_Rosca_Tornillo.bdf"

# salida_largo_1x = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/01_Tornillo_1x.bdf"
# salida_largo_3x = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/01_Tornillo_3x.bdf"

# salida_largo1x = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/06_Rosca_Tornillo_1x.bdf"
# salida_largo3x = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/06_Rosca_Tornillo_3x.bdf"


# #rotar_grid_en_bdf(entrada, salida_corto, 2.09, formato='corto')
# rotar_grid_en_bdf(entrada_06, salida_largo1x, 2.09, formato='corto')
# rotar_grid_en_bdf(entrada_06, salida_largo3x, 6.28, formato='corto')


# rotar_grid_en_bdf(entrada_01, salida_largo_1x, 2.09, formato='corto')
# rotar_grid_en_bdf(entrada_01, salida_largo_3x, 6.28, formato='corto')


# def extraer_y_guardar_numeros(archivo_entrada, archivo_debug):
#     with open(archivo_entrada, 'r') as f_in, open(archivo_debug, 'w') as f_debug:
#         for linea in f_in:
#             if linea.strip().startswith('GRID'):
#                 # Extraemos números con regex
#                 numeros = re.findall(r'[+-]?\d*\.\d+|[+-]?\d+', linea)
#                 f_debug.write(f"Línea original:\n{linea}")
#                 f_debug.write(f"Números extraídos: {numeros}\n\n")
#             else:
#                 # Si quieres puedes escribir también las líneas que no son GRID para contexto
#                 f_debug.write(f"No GRID: {linea}")

# # Uso de la función
# extraer_y_guardar_numeros(entrada_01, 'C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/debug_numeros_extraidos.txt')






import math
import re

def parse_nastran_float(value):
    """Convierte un número en formato NASTRAN a float."""
    value = value.strip()
    if not value:
        return 0.0
    match = re.fullmatch(r'([+-]?[\d\.]+)([+-]\d+)', value)
    if match:
        base, exp = match.groups()
        return float(base + 'e' + exp)
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Formato no válido: '{value}'")

def format_nastran_field(value):
    """
    Formatea un float al estilo NASTRAN (8 caracteres, sin 'E').
    """
    if value == 0.0:
        return "0.       "
    abs_val = abs(value)
    if 1e-4 <= abs_val < 1e+4:
        s = f"{value:.7f}".rstrip('0').rstrip('.')
        return s.rjust(8)
    else:
        s = f"{value:.5e}".replace('e', '')
        base = s[:-3].rstrip('0').rstrip('.')
        exp = int(s[-3:])
        return f"{base}{exp:+}".rjust(8)

# Rotación
angle_deg = -2.09
angle_rad = math.radians(angle_deg)
cos_theta = math.cos(angle_rad)
sin_theta = math.sin(angle_deg * math.pi / 180)


# Leer archivo BDF original
input_path =  "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/01_Tornillo.bdf"
output_path = "C:/Users/jc.garcia-taheno/Desktop/CE_3_TahenoHijes/ModelosApexFinales/BDF/M4_MinimaSeparacionFinal.bd/01_Tornillo_1x.bdf"

with open(input_path, "r") as f:
    bdf_content = f.readlines()

rotated_grid_lines = []
for line in bdf_content:
    if line.startswith("GRID"):
        fields = [line[i:i+8] for i in range(0, len(line.rstrip()), 8)]
        if len(fields) >= 6:
            node_id = int(fields[1])
            x = parse_nastran_float(fields[3])
            y = parse_nastran_float(fields[4])
            z = parse_nastran_float(fields[5])

            # Rotar en Z
            x_rot = x * cos_theta - y * sin_theta
            y_rot = x * sin_theta + y * cos_theta

            # Formato original
            line_fmt = (
                f"{'GRID':<8}"
                f"{str(node_id).ljust(8)}"
                f"{'':8}"
                f"{format_nastran_field(x_rot)}"
                f"{format_nastran_field(y_rot)}"
                f"{format_nastran_field(z)}"
            )
            rotated_grid_lines.append(line_fmt + "\n")
        else:
            rotated_grid_lines.append(line)
    else:
        rotated_grid_lines.append(line)

# Guardar nuevo archivo
with open(output_path, "w") as f:
    f.writelines(rotated_grid_lines)

print(f"Archivo rotado exportado correctamente a: {output_path}")