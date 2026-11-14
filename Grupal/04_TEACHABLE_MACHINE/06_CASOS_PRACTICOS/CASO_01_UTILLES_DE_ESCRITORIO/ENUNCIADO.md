# Caso práctico 01: Clasificador de útiles de escritorio

**Situación:** En el laboratorio se mezclan objetos de trabajo. Tu aplicación debe distinguir una regla de una tijera mediante fotografías.

**Clases:** Regla, Tijera.

**Encargo:** Crea dos clases, 40 fotos variadas de cada objeto, 10 fotos nuevas por clase, formulario y resultado.

## Producto que debes entregar

1. Capturas del entrenamiento con las clases y los datos usados.
2. Exportación real de `keras_model.h5` y `labels.txt`.
3. `app.py`, plantilla HTML y CSS (opcional en el primer caso); no usar JavaScript.
4. Una tabla con al menos cinco predicciones sobre fotos nuevas, incluyendo errores encontrados.
5. Explicación breve: qué hace cada importación, cómo recibe Flask una foto, por qué se usa NumPy y qué significa la confianza.

## Ruta sugerida

Toma al Proyecto 01 como referencia. Entrega solo el nombre de la clase reconocida.

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

**Nota:** No uses esta clasificación para tomar decisiones de seguridad sobre herramientas cortantes.