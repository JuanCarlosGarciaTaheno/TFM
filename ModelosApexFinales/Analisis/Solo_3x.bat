SET NASTRAN="C:\Program Files\MSC.Software\MSC_Nastran\2024.2\bin\nastran.exe"






:: Media Separacion
:: tardo 11 h y termino con fatal
::ECHO A3
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A3_x3_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

ECHO A4
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A4_x3_BCGRID"
%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat








:: ------------------------------------
:: min sep mucho tiempo
::ECHO A3
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A3_x3_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

ECHO A4
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A4_x3_BCGRID"
%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat




::: Max Separacion
::ECHO A3
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A3_x3_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

ECHO A4
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A4_x3_BCGRID"
%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat



::::::::::::::::::::::::::::::::::
::          BCBODY              ::
::::::::::::::::::::::::::::::::::

:: Media Separacion
:: tardo 11 h y termino con fatal
ECHO A3
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A3_x3_BCBODY"
%NASTRAN% Cabecero_contacto.dat

::ECHO A4
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A4_x3_BCGRID"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat








:: ------------------------------------
:: min sep mucho tiempo
ECHO A3
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A3_x3_BCBODY"
%NASTRAN% Cabecero_contacto.dat

::ECHO A4
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A4_x3_BCGRID"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat




::: Max Separacion
ECHO A3
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A3_x3_BCBODY"
%NASTRAN% Cabecero_contacto.dat

::ECHO A4
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A4_x3_BCGRID"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

::ECHO A2
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat

















: --------------------------------------------------

::      Termoelasticos solo con BCBODY
:: ------------- MAX SEP -----------------------


ECHO A5
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
%NASTRAN% Cabecero_contacto.dat


::ECHO A9
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
%NASTRAN% Cabecero_contacto.dat





:: ------------- MAX SEP -----------------------





::ECHO A5 
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
%NASTRAN% Cabecero_contacto.dat

:: 10 HORAS desde las 11.00 a las 21.00
ECHO A7
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A7_x3_BCBODY_Termo170k"
%NASTRAN% Cabecero_contacto.dat


ECHO A9
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
%NASTRAN% Cabecero_contacto.dat




::

:: :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Media Separacion

ECHO A5
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A5_x3_BCBODY_TermoOrig"
%NASTRAN% Cabecero_contacto.dat

ECHO A7
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A7_x3_BCBODY_Termo170k"
%NASTRAN% Cabecero_contacto.dat

ECHO A9 7:15 -- 11:00 No finalizado
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A9_x3_BCBODY_Termo220k"
%NASTRAN% Cabecero_contacto.dat

:: ---------------------------------------------------

::------------------------------------------------------








































































































:: GIRO 1X
::::::::::::::::::::::::::::::::::
::          BCGRID              ::
::::::::::::::::::::::::::::::::::

:: Media Separacion


::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

ECHO A2 
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A2_x1_BCGRID"
%NASTRAN% Cabecero_contacto.dat








:: ------------------------------------
:: min sep mucho tiempo

::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A1_x1_BCBODY"
::%NASTRAN% Cabecero_contacto.dat

ECHO A2 
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A2_x1_BCGRID"
%NASTRAN% Cabecero_contacto.dat




::: Max Separacion


::ECHO A1
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A1_x1_BCBODY%NASTRAN% Cabecero_contacto.dat
::%NASTRAN% Cabecero_contacto.dat

ECHO A2
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A2_x1_BCGRID"
%NASTRAN% Cabecero_contacto.dat


::::::::::::::::::::::::::::::::::
::          BCBODY              ::
::::::::::::::::::::::::::::::::::

:: Media Separacion


ECHO A1
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A1_x1_BCBODY"
%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MediaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat


:: ------------------------------------
:: min sep mucho tiempo

ECHO A1
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A1_x1_BCBODY"
%NASTRAN% Cabecero_contacto.dat

::ECHO A2 
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MinimaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat


::: Max Separacion


ECHO A1
cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A1_x1_BCBODY
%NASTRAN% Cabecero_contacto.dat


::ECHO A2
::cd "C:\Users\jc.garcia-taheno\Desktop\CE_3_TahenoHijes\ModelosApexFinales\Analisis\M4_MaximaSeparacion_Junto\A2_x1_BCGRID"
::%NASTRAN% Cabecero_contacto.dat
