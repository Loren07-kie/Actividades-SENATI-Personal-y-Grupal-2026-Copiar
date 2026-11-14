"""Predicción educativa usando el modelo real entrenado (no ficticio)."""
import os
from pathlib import Path
import joblib,pandas as pd
from flask import Flask,render_template,request
BASE=Path(__file__).resolve().parent
paquete=joblib.load(BASE/'modelo_entrenado.joblib')
RANGOS={'visitas_mes': [2.0, 18.0], 'gasto_mes_soles': [21.88, 314.91]}
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def inicio():
    resultado=None;error=None
    if request.method=='POST':
        try:
            valores={}
            for c in paquete['columnas']:
                v=float(request.form.get(c,''))
                minimo,maximo=RANGOS[c]
                if not (minimo<=v<=maximo):raise ValueError(f'{c} fuera de rango educativo [{minimo:g},{maximo:g}]')
                valores[c]=v
            d=pd.DataFrame([valores],columns=paquete['columnas'])
            y=int(paquete['modelo'].predict(paquete['escalador'].transform(d))[0])
            resultado=(f'Grupo {y}' if paquete['algoritmo']=='kmeans' else ('Registro poco habitual (-1)' if y==-1 else 'Registro dentro de patrón (1)'))
        except (ValueError,TypeError) as exc:error=str(exc)
    return render_template('index.html',titulo='Reto 01 — Agrupación de clientes de papelería',columnas=paquete['columnas'],rangos=RANGOS,entradas=request.form,resultado=resultado,error=error)
if __name__=='__main__':app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')))