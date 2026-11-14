# Tornillo / Tuerca / Arandela

**Autora académica:** COCA CCORPA LORENA ABIGAIL. El enunciado pide clases **Tornillo, Tuerca, Arandela**.

**Implementado:** `app.py` (carga real de Keras), formulario HTML, CSS con logo SENATI, validación de archivos, lectura de `labels.txt`; predicción en pantalla.

**Pendiente de trabajo de campo real:** preparar fotografías de los objetos/hojas, separar imágenes de entrenamiento de imágenes nuevas de prueba, entrenar en Teachable Machine, exportar `modelo/keras_model.h5` y `modelo/labels.txt`, ejecutar y registrar **cinco pruebas reales**. En el caso de útiles: 40 fotos por clase y 10 nuevas por clase según enunciado.

**Sin inventar evidencias:** mientras falte `.h5`, la página muestra un aviso explícito y no una predicción falsa.

**Uso local recomendado:** Python 3.10; `pip install -r requirements.txt`; `python app.py`. TensorFlow en hosting puede requerir memoria considerable; primero hay que entrenar y validar el modelo.