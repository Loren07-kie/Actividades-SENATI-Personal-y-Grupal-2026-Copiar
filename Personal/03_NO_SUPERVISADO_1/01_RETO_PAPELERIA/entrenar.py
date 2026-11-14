"""Entrena y exporta modelo para Reto 01 — Agrupación de clientes de papelería."""
import pandas as pd, joblib
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
D=Path(__file__).resolve().parent
columnas=['visitas_mes', 'gasto_mes_soles']
datos=pd.read_csv(D/'datos.csv')
escalador=StandardScaler()
X=escalador.fit_transform(datos[columnas])
modelo=KMeans(n_clusters=3,random_state=42,n_init=10)
datos['resultado']=modelo.fit_predict(X)
joblib.dump({'modelo':modelo,'escalador':escalador,'columnas':columnas,'algoritmo':'kmeans'},D/'modelo_entrenado.joblib')
datos.to_csv(D/'resultados.csv',index=False)
print(datos['resultado'].value_counts().sort_index())