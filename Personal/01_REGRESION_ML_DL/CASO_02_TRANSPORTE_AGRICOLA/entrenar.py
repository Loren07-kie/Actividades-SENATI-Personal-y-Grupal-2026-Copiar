"""Entrenamiento reproducible del caso; autoría COCA CCORPA LORENA ABIGAIL."""
import json
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
BASE = Path(__file__).resolve().parent
CARACTERISTICAS = ['distancia_km', 'carga_kg', 'via_no_asfaltada']
OBJETIVO = 'costo_transporte_soles'
d = pd.read_csv(BASE/'datos.csv')
Xtr, Xte, ytr, yte = train_test_split(d[CARACTERISTICAS],d[OBJETIVO],test_size=0.2,random_state=42)
modelo = LinearRegression().fit(Xtr,ytr)
salida = {'intercepto':float(modelo.intercept_), 'coeficientes':[float(a) for a in modelo.coef_], 'columnas': CARACTERISTICAS, 'objetivo':OBJETIVO, 'mae':float(mean_absolute_error(yte, modelo.predict(Xte))), 'r2':float(r2_score(yte, modelo.predict(Xte)))}
(BASE/'modelo.json').write_text(json.dumps(salida,indent=2,ensure_ascii=False),encoding='utf-8')
print(salida)