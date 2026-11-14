# SENATI — Preguntas y actividades (Machine Learning y Deep Learning)

## Fundamentos de inteligencia artificial
1. ¿Qué relación hay entre IA, ML y DL?
   > 🟨 **Respuesta:** IA es el campo amplio; ML aprende patrones a partir de datos; DL es ML basado en redes neuronales de varias capas.
2. Menciona tres características de un sistema de ML.
   > 🟨 **Respuesta:** Aprende de ejemplos, necesita evaluación con datos no vistos y puede generalizar con errores.
3. ¿Qué significa que un modelo dependa de sus datos?
   > 🟨 **Respuesta:** Los ejemplos y su calidad condicionan patrones, sesgos y precisión de sus predicciones.
4. ¿En qué se diferencian supervisado y no supervisado?
   > 🟨 **Respuesta:** Supervisado aprende con objetivo conocido (`y`); no supervisado explora estructuras sin una etiqueta objetivo.
5. ¿Qué significa aprendizaje por refuerzo?
   > 🟨 **Respuesta:** Aprende una política mediante recompensas y penalizaciones asociadas a acciones.
6. ¿Qué columna **no** necesitamos al aplicar K-Means sin etiquetas?
   > 🟨 **Respuesta:** No se utiliza una columna de respuesta o etiqueta `y`.

## Python
7. ¿Para qué sirve una lista?
   > 🟨 **Respuesta:** Una lista almacena valores en orden y permite acceder por índice.
8. ¿En qué se diferencia un diccionario de una lista?
   > 🟨 **Respuesta:** Un diccionario asocia claves con valores; una lista se accede principalmente por posición.
9. ¿Qué hace `if`?
   > 🟨 **Respuesta:** `if` ejecuta un bloque cuando la condición es verdadera.
10. ¿Qué realiza `elif`?
   > 🟨 **Respuesta:** `elif` comprueba otra condición cuando las anteriores resultaron falsas.
11. ¿Qué hace un bucle `for`?
   > 🟨 **Respuesta:** `for` recorre elementos de una colección o secuencia.
12. ¿Por qué un `while` puede quedar ejecutándose sin parar?
   > 🟨 **Respuesta:** Porque su condición puede no cambiar a falsa; se debe actualizar o interrumpir explícitamente.
13. ¿Para qué se utiliza `def`?
   > 🟨 **Respuesta:** `def` declara una función reutilizable.
14. ¿Qué hace `return`?
   > 🟨 **Respuesta:** `return` entrega el resultado de una función y termina su ejecución.

## Librerías y CSV
15. ¿Para qué sirve NumPy?
   > 🟨 **Respuesta:** NumPy permite cálculos eficientes con arreglos y matrices numéricas.
16. ¿Qué devuelve `np.array()`?
   > 🟨 **Respuesta:** `np.array()` construye un arreglo multidimensional de NumPy.
17. ¿Qué hace `pd.read_csv()`?
   > 🟨 **Respuesta:** `pd.read_csv()` lee un CSV y devuelve normalmente un DataFrame.
18. ¿Cuál es la diferencia entre `head()` y `shape`?
   > 🟨 **Respuesta:** `head()` presenta las primeras filas; `shape` indica número de filas y columnas.
19. ¿Por qué debemos revisar los encabezados de un CSV?
   > 🟨 **Respuesta:** Para identificar variables, tipos y nombres correctos antes de elegir características.
20. ¿Qué muestra un gráfico de dispersión?
   > 🟨 **Respuesta:** La posición conjunta de observaciones en dos variables y posibles tendencias o agrupaciones.
21. ¿Cuál es una diferencia práctica entre Matplotlib y Seaborn?
   > 🟨 **Respuesta:** Matplotlib da control directo de gráficos; Seaborn ofrece gráficos estadísticos de alto nivel sobre Matplotlib.
22. ¿Qué tipo de funciones ofrece SciPy?
   > 🟨 **Respuesta:** SciPy facilita optimización, estadística, integración y métodos científicos.
23. ¿Qué función cumple Scikit-learn?
   > 🟨 **Respuesta:** Proporciona algoritmos de entrenamiento, transformaciones y métricas de ML.

## Matemáticas y estadística
24. ¿Qué es un vector? Proporciona uno de tres valores.
   > 🟨 **Respuesta:** Un vector es una lista ordenada de componentes, por ejemplo `[2,5,9]`.
25. ¿Qué es una matriz 2 × 3?
   > 🟨 **Respuesta:** Es una tabla numérica con 2 filas y 3 columnas; por ejemplo `[[1,2,3],[4,5,6]]`.
26. ¿Qué calcula `np.dot()` en el ejemplo de inventario?
   > 🟨 **Respuesta:** Calcula el producto punto o producto matricial según las dimensiones.
27. Calcula la mediana de 2, 4, 7, 10 y 12.
   > 🟨 **Respuesta:** La mediana es **7**, el valor central ordenado.
28. ¿Qué diferencia hay entre media y mediana cuando existe un valor extremo?
   > 🟨 **Respuesta:** La media es sensible a valores extremos; la mediana suele ser más resistente.
29. ¿Qué representa la varianza?
   > 🟨 **Respuesta:** Mide la dispersión promedio de los cuadrados de las desviaciones respecto a la media.
30. ¿Por qué la desviación estándar utiliza la raíz de la varianza?
   > 🟨 **Respuesta:** Porque devuelve la dispersión a la misma unidad de medida de los datos.
31. ¿Cuándo usarías `ddof=1` en una varianza muestral?
   > 🟨 **Respuesta:** Cuando los valores son una muestra y queremos la varianza muestral con divisor `n−1`.
32. Si 3 de 10 pedidos son urgentes, ¿qué frecuencia relativa observas?
   > 🟨 **Respuesta:** Frecuencia relativa observada: `3/10 = 0.30 = 30 %`.

## Aprendizaje no supervisado
33. ¿Qué función cumple `fit()` en K-Means?
   > 🟨 **Respuesta:** `fit()` ajusta los centroides y aprende agrupamientos a partir de los datos de entrenamiento.
34. ¿Qué representa `n_clusters=3`?
   > 🟨 **Respuesta:** Se solicitan 3 grupos; no significa que existan necesariamente 3 categorías reales.
35. ¿Qué significa el número de grupo 0?
   > 🟨 **Respuesta:** El 0 es solo un identificador arbitrario del grupo, sin orden de calidad.
36. ¿Por qué necesitamos escalar si las columnas están en escalas muy distintas?
   > 🟨 **Respuesta:** Para evitar que una variable con unidad o magnitud grande domine las distancias.
37. ¿Por qué el escalador usado en la web debe ser el mismo que entrenamos?
   > 🟨 **Respuesta:** Porque sus medias y escalas fueron estimadas durante entrenamiento y deben mantenerse.
38. ¿Para qué utilizamos `modelo.predict()`?
   > 🟨 **Respuesta:** Aplica el modelo entrenado a observaciones nuevas para obtener un grupo o etiqueta de anomalía.
39. ¿Qué significa `-1` en Isolation Forest?
   > 🟨 **Respuesta:** En Isolation Forest, `-1` identifica un registro inusual según el modelo.
40. ¿Por qué «poco habitual» no equivale automáticamente a «falla»?
   > 🟨 **Respuesta:** Un valor poco habitual podría ser legítimo, un error de sensor, estacionalidad u otra causa.
41. ¿Qué archivos necesita nuestra web Flask para mostrar un formulario?
   > 🟨 **Respuesta:** La app necesita `app.py`, `templates/index.html`, archivos CSS y un modelo/pipeline si aplica.
42. ¿Para qué sirve `request.form`?
   > 🟨 **Respuesta:** `request.form` extrae los valores recibidos desde un formulario HTML.
43. ¿Por qué guardamos el modelo con Joblib?
   > 🟨 **Respuesta:** Para persistir el modelo y reutilizar exactamente el mismo ajuste fuera del cuaderno.
44. ¿Qué ocurre si enviamos las columnas al modelo en un orden diferente?
   > 🟨 **Respuesta:** Podrían intercambiarse los atributos y producir salidas erróneas o incompatibilidad.
45. ¿Por qué los CSV están identificados como simulados?
   > 🟨 **Respuesta:** Porque no son datos reales y sus resultados no deben presentarse como diagnósticos o cifras oficiales.

## Ejercicios cortos en el aula
A. Lee el CSV de ventas y muestra sus primeras ocho filas.
   > 🟨 **Respuesta breve:** Lee el CSV con `pd.read_csv()` y muestra `head(8)`; el script `ejercicios_aula.py` realiza el cálculo.
B. Calcula media, mediana, varianza y desviación estándar de cinco valores.
   > 🟨 **Respuesta breve:** Para 2, 4, 7, 10 y 12: media 7, mediana 7, varianza muestral 17 y desviación muestral ≈ 4.12.
C. Construye una matriz de 2 × 3 y calcula la suma de cada fila.
   > 🟨 **Respuesta breve:** Matriz `[[1,2,3],[4,5,6]]`: las sumas por fila son 6 y 15.
D. Cambia el número de grupos de 3 a 2 y explica cómo cambia la salida.
   > 🟨 **Respuesta breve:** Con 2 grupos se obtienen 2 centroides, en vez de 3; los grupos pueden reorganizarse.
E. Ingresa tres registros en los formularios y compara las salidas.
   > 🟨 **Respuesta breve:** Debes probar 3 registros en la web y anotar capturas reales; las pruebas de navegador no están documentadas.