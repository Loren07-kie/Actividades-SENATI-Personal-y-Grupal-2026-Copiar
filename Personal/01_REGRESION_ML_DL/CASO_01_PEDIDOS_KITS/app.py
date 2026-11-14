"""Aplicación Flask sin JavaScript para el caso CASO_01_PEDIDOS_KITS."""
import json, os
from pathlib import Path
from flask import Flask, render_template, request
BASE = Path(__file__).resolve().parent
CONFIG=json.loads((BASE/'modelo.json').read_text(encoding='utf-8'))
RANGOS={'consultas_web': [5, 70], 'inversion_publicidad_soles': [0, 1100], 'campana_escolar': [0, 1]}
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def inicio():
    mensaje=None; error=None
    if request.method=='POST':
        try:
            valores=[]
            for nombre in CONFIG['columnas']:
                numero=float(request.form.get(nombre, ''))
                bajo,alto=RANGOS[nombre]
                if not (bajo<=numero<=alto):
                    raise ValueError(f'{nombre} debe estar entre {bajo} y {alto}')
                if nombre in ('campana_escolar','via_no_asfaltada') and numero not in (0,1):
                    raise ValueError('El indicador debe ser 0 o 1')
                valores.append(numero)
            prediccion=CONFIG['intercepto']+sum(a*b for a,b in zip(CONFIG['coeficientes'],valores))
            mensaje=f'{prediccion:.2f}'
        except (ValueError, TypeError) as exc:
            error=str(exc)
    return render_template('index.html', mensaje=mensaje,error=error, entradas=request.form, titulo='Sistema de estimación de pedidos de kits de robótica',unidades='pedidos estimados',campos=[('consultas_web', 'Consultas web', (5, 70)), ('inversion_publicidad_soles', 'Publicidad (S/)', (0, 1100)), ('campana_escolar', 'Campaña escolar (0 o 1)', (0, 1))],mae=CONFIG['mae'],r2=CONFIG['r2'])
if __name__=='__main__':app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')))