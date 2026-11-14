"""Entrena y exporta modelo para Detección de registros inusuales de sensores."""
import pandas as pd, joblib
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
D=Path(__file__).resolve().parent
columnas=['temperatura_c', 'vibracion_mm_s', 'corriente_a']
datos=pd.read_csv(D/'datos_sensores.csv')
escalador=StandardScaler()
X=escalador.fit_transform(datos[columnas])
modelo=IsolationForest(n_estimators=150,contamination=0.09,random_state=42)
datos['resultado']=modelo.fit_predict(X)
joblib.dump({'modelo':modelo,'escalador':escalador,'columnas':columnas,'algoritmo':'isolation'},D/'modelo_entrenado.joblib')
datos.to_csv(D/'resultados.csv',index=False)
print(datos['resultado'].value_counts().sort_index())