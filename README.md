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

## Repositorio GitHub propuesto

**Nombre exacto para crear:** `Actividades-SENATI-Personal-y-Grupal-2026`

**Descripción para copiar:** Actividades personales y grupales SENATI 2026: Python, regresión ML, aprendizaje no supervisado, visión computacional, JavaScript, Git/GitHub y Teachable Machine, con cuadernos Jupyter originales documentados y aplicaciones web.

Crear como **público**, preferiblemente sin archivos iniciales porque este paquete ya incluye README. Los nombres de las carpetas de cada actividad se conservan. Comparte la URL del repositorio para preparar la publicación.

## Render

Se incluye `render.yaml` de referencia para aplicaciones que disponen de código, CSV y modelo guardado: 2 proyectos de regresión, 4 de no supervisado y 2 webs estáticas de JavaScript. Se recomienda desplegar **solo las actividades que te hayan solicitado**, para evitar crear muchos servicios. `rootDir` de cada servicio apunta a la carpeta de su aplicación. Teachable Machine no se incluye en despliegue hasta entrenar con fotos propias y exportar los modelos de TensorFlow / Keras.

**No se ha subido contenido a GitHub o Render.** Las apps Flask no se han arrancado en este entorno porque Flask no está instalado aquí; los notebooks de datos y visión computacional sí han sido ejecutados y guardados con resultados. Los comandos de arranque se deben comprobar en el servicio real.

Para utilizar un cuaderno, abre su carpeta en VS Code/Jupyter y el notebook del **mismo nombre que indica el material**. Para Flask, instala `requirements.txt` y ejecuta `python app.py` o `gunicorn app:app` en hosting.