from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

base = Path(__file__).resolve().parent
ventas = pd.read_csv(base / '06_ventas_practica_estadistica.csv')
print('A:', ventas.head(8))
valores = np.array([2, 4, 7, 10, 12], dtype=float)
print('B:', valores.mean(),np.median(valores),valores.var(ddof=1),valores.std(ddof=1))
matriz = np.array([[1,2,3],[4,5,6]])
print('C:',matriz.sum(axis=1))
clientes=pd.read_csv(base/'04_clientes_papeleria_practica.csv')
columnas=['visitas_mes','gasto_mes_soles']
X=StandardScaler().fit_transform(clientes[columnas])
print('D, con 2 grupos:',np.unique(KMeans(n_clusters=2,n_init=10,random_state=42).fit_predict(X),return_counts=True))
print('D, con 3 grupos:',np.unique(KMeans(n_clusters=3,n_init=10,random_state=42).fit_predict(X),return_counts=True))