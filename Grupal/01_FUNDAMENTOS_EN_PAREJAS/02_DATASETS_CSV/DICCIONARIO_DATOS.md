# Diccionario de datasets CSV — SENATI
**Instructor: Ing. Gunar Castro Iñigo**

**ORIGEN:** Los datos son **sintéticos generados mediante un generador aleatorio con semilla fija** (20261012) y reglas que crean relaciones plausibles entre las variables. **NO son registros reales** de SENATI, comercios, aulas, instituciones, máquinas o estudiantes. Los identificadores (`registro_id`, `codigo`, `proyecto`) son ficticios y no contienen datos personales. Eviten su uso para decisiones operativas.

Todos los archivos son CSV con encabezados, delimitador coma, codificación UTF-8 con BOM (`utf-8-sig`) y decimales con punto. Su ubicación debe mantenerse junto a los notebooks.

| Archivo | Filas | Variables principales | Objetivo / uso didáctico |
|---|---:|---|---|
| `inventario_componentes.csv` | 120 | código, categoría, costo unitario, precio de venta, stock actual/mínimo, ventas últimos 30 días | reglas, condiciones, funciones, media/mediana, exportación CSV |
| `costos_proyectos_robotica.csv` | 72 | motores, sensores, horas, costo de cada recurso, precio presupuestado | vectores, matrices, costos, ecuaciones y márgenes |
| `demanda_kits_robotica.csv` | 1000 | mes, día, kit, precio, descuento, campaña, asistentes | regresión para `unidades_vendidas`; también modelo Flask |
| `incidencias_sensores.csv` | 850 | temperatura, vibración, antigüedad, horas, mantenimientos | clasificación de `falla_prox_30d` (etiqueta simulada) |
| `asistencia_sesiones.csv` | 500 | grado, modalidad, sesiones, asistencias, tardanzas, entregas | práctica autónoma de estadística, probabilidad empírica y CSV |
| `consumo_energia_aulas.csv` | 650 | laboratorio, computadores, horas, días, otros equipos, temperatura | práctica autónoma de regresión `consumo_kwh` |
| `evaluacion_costos_impresion3d.csv` | 700 | impresora, peso, horas, material, calidad | evaluación de regresión `costo_total_soles` |

### Unidades y convenciones
- **Soles:** montos numéricos expresados en S/ sin símbolo en el CSV para facilidad de cálculo.
- **Mes:** 1–12; **día:** 1–7, lunes–domingo; **campana:** 1 si existe campaña, 0 si no.
- **Descuento:** porcentaje 0–20 como número; por ejemplo `10` significa 10 % y no 0.10.
- **falla_prox_30d:** etiqueta binaria *ficticia*, no diagnóstico ni certificación de fallos.
- **consumo_kwh:** kilovatios-hora al mes simulados; no es consumo medido.
- **Peso impresión:** gramos; **horas:** duración del trabajo; **costos:** soles.

### Limitaciones
Las relaciones de los CSV fueron generadas a partir de fórmulas y ruido. Una métrica elevada en el mismo conjunto sintético no prueba generalización al mundo real. Para proyectos reales habría que registrar datos con consentimiento cuando corresponda, documentar variables, evaluar calidad, sesgos, cambios en el tiempo y desempeño fuera de la muestra.