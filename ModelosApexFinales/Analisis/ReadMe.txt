Códigos:

" extraccionResultadosprt.py "

Una vez extraidos los reports del análisis que se requiera, se puede usar este código para poder agruparlos todos en un único excel.
Actualmente, esta dirigido para que extraiga los siguientes resultados:

columnas = [
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

de los archivos:

archivos_rpt = [
 ... ,
 ...
]


" medias.py "
Una vez agrupado todos los resultados en un único excel, se puede realizar la media de cada elemento y luego agruparlo todo en una nueva hoja
con este código.

Archivos " ---.bat "
Archivos en los que puedes correr de manera secuencial varios análisis, pudiendo realizar cambios de los análisis a realizar a futuro mientras 
se ejecuta otro:
SET NASTRAN="C:\Program Files\MSC.Software\MSC_Nastran\2024.2\bin\nastran.exe"  # Aquí, seleccionas donde se ejecuta Nastran en tu PC

ECHO A4  #Nombre asignado en el cmd durante la ejecución
cd "C:\Users\------ ruta a la carpeta donde va a estar el archivo de análisis"
%NASTRAN% Cabecero_contacto.dat  # nombre del archivo en la carpeta anterior para analizar



Carpeta "Cabeceros"
Análisis recomendados para su realización tanto solo la precarga para BCGRID como BCBODY como los caso termo-elásticos.

Existe una carpeta extra, no de análisis, llamada "Inicio" - la cual sirve para importar el modelo 

Alphas.txt -- son los coeficientes de expansión térmica usados en los RBE3, meramente informativo

Rotación_Ses.01 archivo para automatizar el giro a aplicar (Nota-- según el giro sera necesario modificar el documento)
