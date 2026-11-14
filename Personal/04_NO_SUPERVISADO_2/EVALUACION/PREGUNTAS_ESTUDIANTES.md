# Evaluación — Aprendizaje no supervisado

**Responde con tus palabras.**

1. ¿Qué diferencia un problema supervisado de uno no supervisado?
   > 🟨 **Respuesta:** Supervisado aprende relaciones con una variable objetivo; no supervisado identifica patrones sin etiquetas de respuesta.

2. ¿Para qué sirve `pd.read_csv()`?
   > 🟨 **Respuesta:** Lee un archivo CSV y crea un DataFrame.

3. ¿Qué significa X?
   > 🟨 **Respuesta:** `X` es la matriz de variables predictoras o descriptivas usadas para entrenar.

4. ¿Es necesario definir y para K-Means?
   > 🟨 **Respuesta:** No; K-Means no necesita variable `y` para entrenar.

5. ¿Qué hace `fit_predict()`?
   > 🟨 **Respuesta:** Ajusta el algoritmo y devuelve grupos o alertas sobre el conjunto analizado.

6. ¿Cuál es el significado del número de un grupo?
   > 🟨 **Respuesta:** Es un identificador arbitrario de un conjunto de observaciones, no una calificación.

7. ¿Qué cambia con `n_clusters=3`?
   > 🟨 **Respuesta:** Cambia el número de centroides buscados y potencialmente el significado de cada grupo.

8. ¿Qué es un centroide?
   > 🟨 **Respuesta:** Es el centro medio de un grupo en el espacio de características del modelo.

9. ¿Para qué sirve `random_state`?
   > 🟨 **Respuesta:** Fija la semilla aleatoria para reproducir resultados cuando el método incluye aleatoriedad.

10. ¿Por qué normalizamos precio y stock?
   > 🟨 **Respuesta:** Porque precio y stock tienen escalas diferentes y pueden dominar las distancias.

11. ¿Qué hace `StandardScaler.fit_transform()`?
   > 🟨 **Respuesta:** Ajusta medias/desviaciones estándar sobre entrenamiento y devuelve los datos escalados.

12. ¿Qué hace `StandardScaler.transform()`?
   > 🟨 **Respuesta:** Escala nuevos registros usando las estadísticas ya aprendidas, sin reajustar el escalador.

13. ¿Qué representa `eps` en DBSCAN?
   > 🟨 **Respuesta:** En DBSCAN, `eps` es el radio máximo de vecindad para buscar puntos vecinos.

14. ¿Qué representa `min_samples`?
   > 🟨 **Respuesta:** `min_samples` define cuántos puntos son necesarios dentro de una vecindad para considerar un punto núcleo.

15. ¿Qué quiere decir -1 en DBSCAN?
   > 🟨 **Respuesta:** El valor `-1` en DBSCAN identifica puntos etiquetados como ruido en ese ajuste.

16. ¿DBSCAN dispone de `.predict()` para datos nuevos?
   > 🟨 **Respuesta:** No; DBSCAN estándar de Scikit-learn no expone `predict()` para registros nuevos.

17. ¿Qué hace Isolation Forest?
   > 🟨 **Respuesta:** Busca observaciones poco habituales aislándolas con particiones aleatorias de datos.

18. ¿Qué significa -1 en Isolation Forest?
   > 🟨 **Respuesta:** `-1` en Isolation Forest significa predicción de registro atípico bajo el modelo.

19. ¿Para qué se usa `contamination`?
   > 🟨 **Respuesta:** `contamination` especifica la proporción esperada de valores atípicos usada para fijar el umbral.

20. ¿Un valor inusual implica necesariamente un error de sensor?
   > 🟨 **Respuesta:** No; requiere revisar el contexto y la medición antes de declarar fallo.

21. ¿Cómo trabaja el agrupamiento jerárquico aglomerativo?
   > 🟨 **Respuesta:** Agrupa iterativamente los grupos más similares según un criterio de enlace.

22. ¿AgglomerativeClustering tiene `.predict()`?
   > 🟨 **Respuesta:** No; AgglomerativeClustering estándar no tiene método `predict()` para registros nuevos.

23. ¿Por qué usar un CSV simulado?
   > 🟨 **Respuesta:** Para practicar sin divulgar datos privados o atribuir resultados a empresas reales.

24. ¿Para qué sirve `joblib.dump()`?
   > 🟨 **Respuesta:** Serializa el modelo entrenado para poder cargarlo en una aplicación.

25. ¿Qué archivo contiene el formulario web?
   > 🟨 **Respuesta:** `templates/index.html` contiene el formulario principal de Flask.

26. ¿Qué hace Flask con los datos de entrada?
   > 🟨 **Respuesta:** Flask recibe los campos con `request.form`, los valida y los pasa al modelo o preprocesador.

27. ¿Cómo evitamos instalar librerías de nuevo cada clase?
   > 🟨 **Respuesta:** Usar un entorno virtual persistente e instalar una vez los paquetes de `requirements.txt`.

28. ¿Qué debes demostrar al concluir la tarea?
   > 🟨 **Respuesta:** Código ejecutable, explicación, datos, ajuste y resultados, formulario funcional y límites del método.