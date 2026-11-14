# Caso práctico 02: Clasificador de materiales de taller

**Situación:** Para ordenar una mesa de taller, queremos distinguir tres piezas pequeñas. Debes mostrar el nombre de la pieza y un porcentaje de confianza.

**Clases:** Tornillo, Tuerca, Arandela.

**Encargo:** Crea tres clases, prepara una foto bien iluminada por prueba y muestra la clase y su confianza.

## Producto que debes entregar

1. Capturas del entrenamiento con las clases y los datos usados.
2. Exportación real de `keras_model.h5` y `labels.txt`.
3. `app.py`, plantilla HTML y CSS (opcional en el primer caso); no usar JavaScript.
4. Una tabla con al menos cinco predicciones sobre fotos nuevas, incluyendo errores encontrados.
5. Explicación breve: qué hace cada importación, cómo recibe Flask una foto, por qué se usa NumPy y qué significa la confianza.

## Ruta sugerida

Toma el Proyecto 02 como referencia. Si deseas, agrega una recomendación siguiendo el Proyecto 03.

## Requisitos mínimos

- El formulario permite elegir la imagen.
- La imagen se envía con POST a Flask.
- El modelo identifica una de las clases entrenadas.
- La página muestra el resultado en texto legible.
- Se incluyen instrucciones para ejecutar la aplicación.

## Preguntas para la exposición

1. ¿Qué fotos usaste para entrenar y cuáles reservaste para probar?
2. ¿Qué hace `request.files`?
3. ¿Qué significa `modelo.predict`?
4. ¿Cómo comprobaste un error real de tu modelo?
5. ¿Qué podrías mejorar con más ejemplos?

**Nota:** Es un ejercicio de aprendizaje, no un instrumento profesional certificado.