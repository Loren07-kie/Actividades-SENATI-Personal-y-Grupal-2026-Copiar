# Portal Render — Actividades SENATI 2026

**Autora:** COCA CCORPA LORENA ABIGAIL.

Este portal monta en un servicio Render seis aplicaciones Flask originales, publicadas en rutas separadas, y sirve los dos proyectos JavaScript originales. Los cuadernos Jupyter aparecen enlazados con sus nombres sin cambios.

## Comandos

```bash
bash Sitio_SENATI/build.sh
gunicorn Sitio_SENATI.app:app --bind 0.0.0.0:$PORT
```

Para desarrollo local después de instalar las dependencias: `flask --app Sitio_SENATI.app:site run --debug` permite revisar el portal; para montar todas las aplicaciones utiliza Gunicorn.

**Nota:** Los cuatro modelos de aprendizaje no supervisado se entrenan con sus CSV existentes durante el build de Render; los archivos `modelo_entrenado.joblib` grandes no se mantienen en Git. La información de Teachable Machine es demostrativa y precisa imágenes y modelos propios.