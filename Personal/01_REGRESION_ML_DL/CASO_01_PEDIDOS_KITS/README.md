# Sistema de estimación de pedidos de kits de robótica

Autoría: **COCA CCORPA LORENA ABIGAIL** · SENATI 2026.

Se conservó el nombre original del cuaderno **01_Caso_para_desarrollar.ipynb** y el dataset de clase. El sistema implementa regresión lineal múltiple 80/20 (`random_state=42`).

## Ejecutar

```bash
pip install -r requirements.txt
python entrenar.py
python app.py
```

Visitar `http://localhost:5000`. En Render: **Root Directory** debe apuntar a esta carpeta y utilizar `gunicorn app:app` como comando de inicio.

**Evidencia:** la métrica, las predicciones exigidas y el CSV están en `PRUEBAS_Y_RESULTADOS.md` y `predicciones_prueba.csv`. Las capturas de navegador no están verificadas desde este entorno.