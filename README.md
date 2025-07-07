# Proyecto de Unión Atornillada con Tornillo + HeliCoil

Este repositorio contiene todos los códigos, macros, plantillas y modelos necesarios para automatizar el análisis de una unión atornillada en entornos como CATIA, Siemens APEX y NASTRAN, integrando parametrización, automatización de modelos y extracción de resultados.

---

## Estructura del Repositorio

### Códigos
Contiene scripts necesarios para:
- La creación de if-rules en CATIA.
- Automatización del proceso de selección de parámetros con el script `SelectorParametros_GUI.py`, que se comunica con el Excel `Param_Union_TornHelic.xlsx` (ubicado fuera del repositorio) y el archivo `parametros_seleccionados`, permitiendo fijar parámetros directamente en CATIA.

---

### Excel y Documentación
- `Iteraciones_cell.xlsx`:  
  En la hoja 2 se documentan los análisis realizados y los parámetros modificados en cada iteración.
  
- `Paneles_1al7_Bolts_2024_Template.xlsx`:  
  Plantilla analítica para el cálculo de tensiones y márgenes de seguridad en uniones atornilladas.

- `Param_Union_TornHelic.xlsx`:  
  Archivo con parámetros vinculados a las tablas de diseño en CATIA.

---

### Macros (3 carpetas)

1. `PiezasSeparadas`  
   Macros para generar modelos de APEX con las piezas separadas automáticamente.

2. `UnionPiezas`  
   Macros para crear modelos con piezas unidas.

3. `Pruebas`  
   Carpeta de código experimental y versiones preliminares.

---

### Material_properties
Excels con los coeficientes de expansión térmica para:
- Aluminio
- Acero
- Titanio

---

### ModelosApexFinales
Contiene los modelos finales en APEX para los tres casos de separación:
- Mínima
- Media
- Máxima

También se incluyen los archivos BDF extraídos de Apex.

Importante:  
Se destaca el script `SepararBDF_SolidosMin.py` que permite dividir un archivo BDF por componentes sólidos para facilitar su manejo y análisis posterior.

---

### Analisis
Incluye los resultados y utilidades para el procesamiento de análisis FEM realizados con NASTRAN:

- `extraccionResultadosprt.py`:  
  Une los resultados de múltiples archivos `.rpt`.

- `medias.py`:  
  Calcula la media de los valores extraídos y los exporta a una nueva hoja en un Excel indicado.

- Archivos `.bat`:  
  Permiten ejecutar múltiples análisis NASTRAN de forma secuencial y ordenada.

Nota:  
Por limitaciones de espacio, solo se incluyen los cabeceros de los resultados.

---

### Sketchs_Apex
Contiene:
- Archivos CAD individuales de las piezas.
- El product completo que permite abrir el conjunto del modelo en APEX.

---

## Notas adicionales

Este repositorio ha sido preparado para facilitar la automatización del diseño, simulación y postprocesado de uniones atornilladas parametrizadas con HeliCoil en entornos CAD y CAE.  
Es necesario tener acceso a las licencias de CATIA, APEX y NASTRAN para ejecutar el flujo completo.

---

## Referencias útiles

1. NASA (1990). *Fastener Design Manual*. NASA Reference Publication 1228.  
2. Böllhoff GmbH. *HELICOIL® plus: Ensamblaje seguro de roscas*.  
3. Tornillería Online (2012). *Ficha técnica tornillo DIN 912 / ISO 4762 — Acero 12.9*.  
4. ESA (2010). *Threaded Fasteners Handbook (ECSS-E-HB-32-23A)*.  
5. Siemens (2023). *APEX CAE - User Scripting Manual*.  
6. NASTRAN (2024). *Quick Reference Guide*.
