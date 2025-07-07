## Estructura del Repositorio

### Códigos
Contiene scripts necesarios para:
- La creación de if-rules en CATIA.
- Automatización del proceso de selección de parámetros con el script `SelectorParametros_GUI.py`, que se comunica con el Excel `Param_Union_TornHelic.xlsx` (ubicado fuera del repositorio) y el archivo `parametros_seleccionados`, permitiendo fijar parámetros directamente en CATIA.


### Excel y Documentación
- `Iteraciones_cell.xlsx`:  
  En la hoja 2 se documentan los análisis realizados y los parámetros modificados en cada iteración.
  
- `Paneles_1al7_Bolts_2024_Template.xlsx`:  
  Plantilla analítica para el cálculo de tensiones y márgenes de seguridad en uniones atornilladas.

- `Param_Union_TornHelic.xlsx`:  
  Archivo con parámetros vinculados a las tablas de diseño en CATIA.


### Macros (3 carpetas)

1. `PiezasSeparadas`  
   Macros para generar modelos de APEX con las piezas separadas automáticamente.

2. `UnionPiezas`  
   Macros para crear modelos con piezas unidas.

3. `Pruebas`  
   Carpeta de código experimental y versiones preliminares.


### Material_properties
Excels con los coeficientes de expansión térmica para:
- Aluminio
- Acero
- Titanio


### ModelosApexFinales
Contiene los modelos finales en APEX para los tres casos de separación:
- Mínima
- Media
- Máxima

También se incluyen los archivos BDF extraídos de Apex.

Importante:  
Se destaca el script `SepararBDF_SolidosMin.py` que permite dividir un archivo BDF por componentes sólidos para facilitar su manejo y análisis posterior.


### Analisis
Incluye los resultados y utilidades para el procesamiento de análisis FEM realizados con NASTRAN:

- `extraccionResultadosprt.py`:  
  Une los resultados de múltiples archivos `.rpt`.

- `medias.py`:  
  Calcula la media de los valores extraídos y los exporta a una nueva hoja en un Excel indicado.

- Archivos `.bat`:  
  Permiten ejecutar múltiples análisis NASTRAN de forma secuencial y ordenada.

Nota:  
Por limitaciones de espacio, solo se incluyen los cabeceros de los análisis realizados.


### Sketchs_Apex
Contiene:
- Archivos CAD individuales de las piezas.
- El product que permite abrir el conjunto del modelo en APEX.


## Notas adicionales

Este repositorio ha sido preparado para facilitar la automatización del diseño, simulación y postprocesado de uniones atornilladas parametrizadas con HeliCoil en entornos CAD.


## Referencias

### Normas DIN e ISO sobre roscas y tornillos

1. DIN Deutsches Institut für Normung. (1999). *DIN 13-1: Métricas ISO - Parte 1: Dimensiones del perfil básico*.
2. DIN Deutsches Institut für Normung. (2004). *DIN 76-1: Thread run-outs and thread undercuts for ISO metric threads as in DIN 13-1*.
3. International Organization for Standardization. (1973). *ISO 2857: Screws and nuts — Symbols and designations of dimensions*.
4. International Organization for Standardization. (1979). *ISO 273: Fasteners — Clearance holes for bolts and screws*.
5. International Organization for Standardization. (1992). *ISO 3353: Aerospace — Rolled threads — Metric*.
6. International Organization for Standardization. (1998). *ISO 965-1: General purpose metric screw threads — Tolerances — Part 1: Principles and basic data*.
7. International Organization for Standardization. (2006). *ISO 7089: Plain washers — Normal series — Product grade A*.
8. International Organization for Standardization. (n.d.). *ISO 4762 (DIN 912): Tornillo de cabeza cilíndrica con hexágono interior — Grado 12.9*.

### Manuales y otros documentos

9. NASA. (1990). *Fastener Design Manual* (NASA Reference Publication 1228).
10. Böllhoff GmbH. (n.d.). *HELICOIL® plus: Ensamblaje seguro de roscas* (Catálogo técnico, pág. 47).
11. Tornillería Online. (2012). *Ficha técnica tornillo DIN 912 / ISO 4762 — Acero 12.9*.
12. ESA. (2010). *Threaded Fasteners Handbook* (ECSS-E-HB-32-23A, July 6, 2010). European Cooperation for Space Standardization (ECSS).
13. Siemens Digital Industries Software. (2023). *APEX CAE - User Scripting Manual* (documentación interna).
14. NASTRAN. (2024). *NASTRAN 2024.2 Quick Reference Guide*.
15. Sampedro Roncero, M. (s.f.). *Generación de CDM aplicado al pre-diseño de cálculo estructural de modelos* [Trabajo de Fin de Grado, Universidad Politécnica de Madrid]. GitHub. https://github.com/mariasamp/TFG

### Manuales para trabajos futuros

16. International Organization for Standardization. (1999). *ISO 5855-1: Aerospace — MJ threads — Part 1: General requirements*.
17. International Organization for Standardization. (1999). *ISO 5855-2: Aerospace — MJ threads — Part 2: Limit dimensions for plugs and gauges*.
18. International Organization for Standardization. (1988). *ISO 5855-3: Aerospace — MJ threads — Part 3: Limit dimensions for bolts and nuts*.

