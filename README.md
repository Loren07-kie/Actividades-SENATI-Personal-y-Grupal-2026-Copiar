# ACTIVIDADES SENATI — Personal y Grupal (2026)

**Autora académica / organización:** COCA CCORPA LORENA ABIGAIL.

Se inspeccionaron **12 archivos RAR y 2 PDF** entregados por el estudiante, incluyendo el PDF de JavaScript contenido dentro de `SEMANA 3 y 4.rar` y las diapositivas del taller de visión computacional. Se suprimieron copias de archivo duplicadas (p. ej., `FRONTEND (1)` y `(2)`, y `SENATI_ML_NoSupervisado` y `SENATI_ML_NoSupervisado (1)`).

## Cómo localizar una actividad

- `Personal/01_REGRESION_ML_DL/`: 2 casos, cuadernos y aplicaciones Flask, entrenamiento y pruebas reproducibles.
- `Personal/02_EVALUACION_FUNDAMENTOS/`: caso evaluado de impresión 3D en cuaderno original.
- `Personal/03_NO_SUPERVISADO_1/`: papelería y laboratorio, cuestionario 45 preguntas y ejercicios A–E.
- `Personal/04_NO_SUPERVISADO_2/`: biblioteca y sensores, cuestionario 28 preguntas.
- `Personal/05_JAVASCRIPT_EJERCICIOS/`: 41 ejercicios explícitos resueltos del PDF, interfaz JavaScript.
- `Personal/06_VISION_COMPUTACIONAL/`: siete cuadernos originales con retos ejecutados, gráficos e imágenes de salida.
- `Grupal/01_FUNDAMENTOS_EN_PAREJAS/`: asistencia a talleres y predicción de energía, mismo cuaderno original.
- `Grupal/02_JAVASCRIPT_TRABAJO_EN_EQUIPO/`: cuatro apps de los ejercicios finales del PDF.
- `Grupal/03_GIT_GITHUB/`: solo el Word **`GIT - PROYECTO SENATI (1).docx`**, sin rehacer el trabajo de Computadora 1 y 2 porque la estudiante indica que ya lo terminó.
- `Grupal/04_TEACHABLE_MACHINE/`: tres encargos de clasificación con formulario y carga de modelo real, **pendientes de fotografías, entrenamiento y pruebas reales**.
- `Grupal/05_VISION_COMPUTACIONAL_EN_PAREJAS/`: propuesta de caso industrial en el cuaderno 04 original.

Todos los **17 cuadernos** tienen el **nombre original** y un bloque **amarillo** de inicio del desarrollo justo junto al enunciado; las respuestas cortas se leen junto a las preguntas originales. También se completaron 73 preguntas dentro de los archivos `.md` originales. Las imágenes en cuadernos incluyen logo SENATI cuando estaba disponible en el material; las webs llevan su logo institucional. No se han generado capturas ficticias, resultados de Teachable Machine ni historial GitHub.

## Repositorio GitHub publicado

**Repositorio oficial:** https://github.com/Loren07-kie/Actividades-SENATI-Personal-y-Grupal-2026-Copiar

Este repositorio contiene 17 cuadernos Jupyter originales, material personal y grupal y recursos de las aplicaciones. Los bloques amarillos se encuentran en el lugar donde se desarrolla cada actividad; las respuestas cortas aparecen junto a las preguntas.

## Portal web en Render

**URL pública:** https://senati-actividades-lorena-2026.onrender.com

El portal usa un solo servicio Python en Render: monta seis aplicaciones de datos (dos regresiones y cuatro retos de aprendizaje no supervisado), muestra dos páginas JavaScript y enlaza los cuadernos. En el build, `bash Sitio_SENATI/build.sh` instala las dependencias y entrena los cuatro modelos no supervisados a partir de los CSV originales. Arranca con `gunicorn Sitio_SENATI.app:app --bind 0.0.0.0:$PORT`.

**Comprobación al 14/11/2026:** Render informó el despliegue como `live` y registró HTTP 200 para la página principal. Esto no sustituye pruebas de usuario de cada formulario. Los tres casos de Teachable Machine siguen pendientes de fotografías y modelos entrenados reales.
