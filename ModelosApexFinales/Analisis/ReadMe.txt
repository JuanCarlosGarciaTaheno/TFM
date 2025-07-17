### Included Scripts

`extraccionResultadosprt.py`

This script allows you to extract and combine results from multiple `.rpt` output files into a single Excel file after running the desired analysis.  
It is currently set up to extract the following fields:

columns = [
    "Entity ID",
    "El. Pos. ID",
    "von Mises",
    "X Component",
    "Y Component",
    "Z Component",
    "XY Component",
    "YZ Component",
    "ZX Component",
    "XY Engr. Component",
    "YZ Engr. Component",
    "ZX Engr. Component"
]

from the following files:

archivos_rpt = [
    ...,
    ...
]

`medias.py`

Once all result data has been collected into a single Excel file, this script can be used to compute the average values for each element and save them into a new sheet in the same workbook.

### Batch Files (.bat)

Batch files included in this repository allow you to run multiple analyses sequentially. You can even edit future analysis runs while one is already executing.

Example usage inside a `.bat` file:

SET NASTRAN="C:\Program Files\MSC.Software\MSC_Nastran\2024.2\bin\nastran.exe"  :: Path to your Nastran installation

ECHO A4  :: Console label during execution
cd "C:\Users\--- path to your analysis folder"
%NASTRAN% Cabecero_contacto.dat  :: Analysis file to run

### Folder: Cabeceros

Contains recommended setups for:
- Preload-only analyses with BCGRID and BCBODY
- Thermoelastic cases

## Subfolder: Inicio

This is not an analysis folder, but used to import and initialize the model structure.

## Other Files

- Alphas.txt: Contains thermal expansion coefficients used in RBE3 definitions. For reference only.
- Rotación_Ses.01: Automates the rotation applied to the model (Note: the rotation applied must match the use case; manual adjustments may be required).
