SET NASTRAN="C:\Program Files\MSC.Software\MSC_Nastran\2024.2\bin\nastran.exe"

: --------------------------------------------------

::      Termoelasticos solo con BCBODY
:: ------------- MINX SEP -----------------------

:: MAS DE 24 Horas
::ECHO A5
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
::%NASTRAN% Cabecero_contacto.dat


::ECHO A9
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
::%NASTRAN% Cabecero_contacto.dat





:: ------------- MAX SEP -----------------------





::ECHO A5 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
::%NASTRAN% Cabecero_contacto.dat

:: 10 HORAS desde las 11.00 a las 21.00
::ECHO A7
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A7_x3_BCBODY_Termo170k"
::%NASTRAN% Cabecero_contacto.dat


::ECHO A9
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
::%NASTRAN% Cabecero_contacto.dat




::

:: :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Media Separacion

::ECHO A5
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
::%NASTRAN% Cabecero_contacto.dat

::desde las 18 h un dia entero y 8 horas
::ECHO A7 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A7_x3_BCBODY_Termo170k"
::%NASTRAN% Cabecero_contacto.dat

ECHO A9 
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
%NASTRAN% Cabecero_contacto.dat

:: ---------------------------------------------------

::------------------------------------------------------
