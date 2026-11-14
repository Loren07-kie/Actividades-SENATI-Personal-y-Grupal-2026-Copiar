# Caso práctico 03: Registro visual de hojas

**Situación:** Un grupo de estudiantes documenta hojas con diferentes apariencias. Desarrolla una página que clasifique el aspecto visible y registre cada consulta.

**Clases:** Verde, Amarilla, Seca.

**Encargo:** Entrena tres clases, identifica hojas en fotografías y muestra los cinco últimos resultados guardados.

## Producto que debes entregar

1. Capturas del entrenamiento con las clases y los datos usados.
2. Exportación real de `keras_model.h5` y `labels.txt`.
3. `app.py`, plantilla HTML y CSS (opcional en el primer caso); no usar JavaScript.
4. Una tabla con al menos cinco predicciones sobre fotos nuevas, incluyendo errores encontrados.
5. Explicación breve: qué hace cada importación, cómo recibe Flask una foto, por qué se usa NumPy y qué significa la confianza.

## Ruta sugerida

Utiliza el Proyecto 05 como referencia para guardar fecha, clase prevista y confianza en SQLite.

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

**Nota:** Solo describe el aspecto visual de las hojas; no diagnostica enfermedades, falta de nutrientes ni calidad agronómica.