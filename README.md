## Repository Structure

### Códigos
Contains scripts for:
- Creating if-rules in CATIA.
- Automating the parameter selection process using the script `SelectorParametros_GUI.py`, which communicates with the Excel file `Param_Union_TornHelic.xlsx` (located outside the repository) and the file `parametros_seleccionados`, allowing parameters to be directly set in CATIA.

### Excel y Documentación
- `Iteraciones_cell.xlsx`:  
  Sheet 2 documents the analyses performed and the parameters modified in each iteration.
  
- `Paneles_1al7_Bolts_2024_Template.xlsx`:  
  Analytical template for stress and margin of safety calculation in bolted joints.

- `Param_Union_TornHelic.xlsx`:  
  File with parameters linked to the CATIA design tables.

### Macros (3 folders)

1. `PiezasSeparadas`  
   Macros for generating APEX models with automatically separated parts.

2. `UnionPiezas`  
   Macros for creating models with joined parts.

3. `Pruebas`  
   Folder for experimental code and preliminary versions.

### Material_properties
Excel files with thermal expansion coefficients for:
- Aluminum
- Steel
- Titanium

### ModelosApexFinales
Contains the final APEX models for the three separation cases:
- Minimum
- Medium
- Maximum

Also includes the BDF files extracted from Apex.

Important:  
The script `SepararBDF_SolidosMin.py` is highlighted as it allows splitting a BDF file by solid components to facilitate handling and later analysis.

### Analisis
Includes results and tools for processing FEM analyses performed with NASTRAN:

- `extraccionResultadosprt.py`:  
  Merges results from multiple `.rpt` files.

- `medias.py`:  
  Computes the average of extracted values and exports them to a new sheet in a specified Excel file.

- `.bat` files:  
  Allow running multiple NASTRAN analyses sequentially and in order.

Note:  
Due to space limitations, only the headers of the analyses performed are included.

### Sketchs_Apex
Contains:
- Individual CAD files of the parts.
- The product file that allows opening the model assembly in APEX.

## Additional Notes

This repository has been prepared to facilitate the automation of design, simulation, and post-processing of parametrized bolted joints with HeliCoil in CAD environments.

## References

### DIN and ISO Standards on Threads and Screws

1. DIN Deutsches Institut für Normung. (1999). *DIN 13-1: ISO metric threads - Part 1: Basic profile dimensions*.
2. DIN Deutsches Institut für Normung. (2004). *DIN 76-1: Thread run-outs and thread undercuts for ISO metric threads as in DIN 13-1*.
3. International Organization for Standardization. (1973). *ISO 2857: Screws and nuts — Symbols and designations of dimensions*.
4. International Organization for Standardization. (1979). *ISO 273: Fasteners — Clearance holes for bolts and screws*.
5. International Organization for Standardization. (1992). *ISO 3353: Aerospace — Rolled threads — Metric*.
6. International Organization for Standardization. (1998). *ISO 965-1: General purpose metric screw threads — Tolerances — Part 1: Principles and basic data*.
7. International Organization for Standardization. (2006). *ISO 7089: Plain washers — Normal series — Product grade A*.
8. International Organization for Standardization. (n.d.). *ISO 4762 (DIN 912): Cylindrical head screw with internal hexagon — Grade 12.9*.

### Manuals and Other Documents

9. NASA. (1990). *Fastener Design Manual* (NASA Reference Publication 1228).
10. Böllhoff GmbH. (n.d.). *HELICOIL® plus: Secure thread assembly* (Technical catalog, p. 47).
11. Tornillería Online. (2012). *Technical sheet screw DIN 912 / ISO 4762 — Steel 12.9*.
12. ESA. (2010). *Threaded Fasteners Handbook* (ECSS-E-HB-32-23A, July 6, 2010). European Cooperation for Space Standardization (ECSS).
13. Siemens Digital Industries Software. (2023). *APEX CAE - User Scripting Manual* (internal documentation).
14. NASTRAN. (2024). *NASTRAN 2024.2 Quick Reference Guide*.
15. Sampedro Roncero, M. (n.d.). *Generation of CDM applied to the structural pre-design of models* [Bachelor’s Thesis, Universidad Politécnica de Madrid]. GitHub. https://github.com/mariasamp/TFG

### Manuals for Future Work

16. International Organization for Standardization. (1999). *ISO 5855-1: Aerospace — MJ threads — Part 1: General requirements*.
17. International Organization for Standardization. (1999). *ISO 5855-2: Aerospace — MJ threads — Part 2: Limit dimensions for plugs and gauges*.
18. International Organization for Standardization. (1988). *ISO 5855-3: Aerospace — MJ threads — Part 3: Limit dimensions for bolts and nuts*.
