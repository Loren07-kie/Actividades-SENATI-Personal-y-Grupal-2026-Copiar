"""Teachable Machine: predicción solo con un modelo real exportado.
No se incluyen modelos o porcentajes fabricados.
"""
import os,sqlite3,io
from pathlib import Path
import numpy as np
from PIL import Image,ImageOps,UnidentifiedImageError
from flask import Flask,render_template,request
ROOT=Path(__file__).resolve().parent
MODELO=ROOT/'modelo'/'keras_model.h5'
ETIQUETAS=ROOT/'modelo'/'labels.txt'
ARCHIVO_DB=ROOT/'datos'/'historial.sqlite3'
app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=7*1024*1024

def cargar_modelo_real():
    if not MODELO.is_file() or not ETIQUETAS.is_file():
        raise FileNotFoundError('Antes de usar IA, entrena con fotos reales y coloca modelo/keras_model.h5 y modelo/labels.txt')
    from tensorflow.keras.models import load_model
    modelo=load_model(str(MODELO),compile=False)
    etiquetas=[x.strip().split(' ',1)[-1] for x in ETIQUETAS.read_text(encoding='utf-8').splitlines() if x.strip()]
    if not etiquetas:raise ValueError('Archivo labels.txt vacío')
    return modelo,etiquetas

def guardar_resultado(etiqueta,confianza):
    ARCHIVO_DB.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(ARCHIVO_DB) as con:
        con.execute('CREATE TABLE IF NOT EXISTS pruebas (id INTEGER PRIMARY KEY, fecha TEXT DEFAULT CURRENT_TIMESTAMP, etiqueta TEXT, confianza REAL)')
        con.execute('INSERT INTO pruebas (etiqueta, confianza) VALUES (?,?)',(etiqueta,confianza))
def historial():
    if not ARCHIVO_DB.exists():return []
    with sqlite3.connect(ARCHIVO_DB) as con:
        return con.execute('SELECT fecha, etiqueta, ROUND(confianza*100,1) FROM pruebas ORDER BY id DESC LIMIT 5').fetchall()

@app.route('/',methods=['GET','POST'])
def inicio():
    error=None;prediccion=None;confianza=None
    if request.method=='POST':
        try:
            archivo=request.files.get('foto')
            if not archivo or not archivo.filename:raise ValueError('Selecciona una imagen.')
            imagen=Image.open(io.BytesIO(archivo.read()))
            imagen=ImageOps.exif_transpose(imagen).convert('RGB')
            imagen=ImageOps.fit(imagen,(224,224),method=Image.Resampling.LANCZOS)
            x=(np.asarray(imagen,dtype=np.float32)/127.5)-1.0
            modelo,etiquetas=cargar_modelo_real()
            puntajes=modelo.predict(np.expand_dims(x,axis=0),verbose=0)[0]
            indice=int(np.argmax(puntajes))
            if indice>=len(etiquetas):raise ValueError('Etiquetas y modelo no coinciden.')
            prediccion=etiquetas[indice];confianza=round(float(puntajes[indice])*100,2)
            guardar_resultado(prediccion,float(puntajes[indice]))
        except (ValueError,FileNotFoundError,UnidentifiedImageError,OSError,ImportError) as ex:
            error=str(ex)
    return render_template('index.html',titulo='Aspecto visual de hojas',clases=['Verde', 'Amarilla', 'Seca'],prediccion=prediccion,confianza=confianza,error=error,historial=historial(),modelo_listo=MODELO.exists() and ETIQUETAS.exists())
if __name__=='__main__':app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')))