"""Portal único Render: aplicaciones de los casos originales + acceso a cuadernos.

Los notebooks mantienen su nombre original y cada aplicación vive en su
carpeta de origen. DispatcherMiddleware monta las aplicaciones sin reescribirlas.
"""
from __future__ import annotations
import importlib.util
import sys
from pathlib import Path
from urllib.parse import quote
from flask import Flask, render_template_string, send_from_directory, redirect, url_for, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware

BASE=Path(__file__).resolve().parent.parent
REPO='https://github.com/Loren07-kie/Actividades-SENATI-Personal-y-Grupal-2026-Copiar'

ACTIVIDADES=[
    ('Personal','Regresión · Pedidos de kits de robótica','/pedidos-kits','Personal/01_REGRESION_ML_DL/CASO_01_PEDIDOS_KITS','01_Caso_para_desarrollar.ipynb','Predice pedidos según consultas web, publicidad y campaña escolar.'),
    ('Personal','Regresión · Transporte agrícola','/transporte-agricola','Personal/01_REGRESION_ML_DL/CASO_02_TRANSPORTE_AGRICOLA','02_Caso_para_desarrollar.ipynb','Estima resultados de transporte mediante regresión.'),
    ('Personal','Reto · Clientes de papelería','/papeleria','Personal/03_NO_SUPERVISADO_1/01_RETO_PAPELERIA','RETO_GUIADO.ipynb','Agrupa clientes en segmentos con K-Means.'),
    ('Personal','Reto · Laboratorio','/laboratorio','Personal/03_NO_SUPERVISADO_1/02_RETO_LABORATORIO','RETO_GUIADO.ipynb','Identifica registros poco habituales con Isolation Forest.'),
    ('Personal','Reto · Biblioteca','/biblioteca','Personal/04_NO_SUPERVISADO_2/RETO_01_BIBLIOTECA','Cuaderno_reto_estudiantes.ipynb','Clasifica patrones de préstamo de libros.'),
    ('Personal','Reto · Sensores','/sensores','Personal/04_NO_SUPERVISADO_2/RETO_02_SENSORES','Cuaderno_reto_estudiantes.ipynb','Detecta lecturas inusuales de sensores.'),
    ('Personal','JavaScript · Ejercicios','/javascript/personal/','Personal/05_JAVASCRIPT_EJERCICIOS/ALGORITMOS Y PROGRAMACIÓN CON JAVASCRIPT',None,'Ejercicios de algoritmos y programación JavaScript.'),
    ('Grupal','JavaScript · Trabajo en equipo','/javascript/grupal/','Grupal/02_JAVASCRIPT_TRABAJO_EN_EQUIPO/ALGORITMOS Y PROGRAMACIÓN CON JAVASCRIPT',None,'Calculadora, edad, promedio e IMC.'),
]
CUADERNOS=[
    ('Personal','Evaluación de impresión 3D','Personal/02_EVALUACION_FUNDAMENTOS/01_Enunciado_Para_Estudiantes.ipynb'),
    ('Personal','Visión · Importancia','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/01_Importancia_Vision_Computacional/01_Importancia_de_VC.ipynb'),
    ('Personal','Visión · Detección','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/02_Fundamentos_Deteccion_Objetos/02_Deteccion_Objetos.ipynb'),
    ('Personal','Visión · Segmentación','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/03_Segmentacion_y_Patrones/03_Segmentacion_y_Reconocimiento.ipynb'),
    ('Personal','Visión · Industria','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/04_Aplicaciones_Principales/04_Aplicaciones_en_la_Industria.ipynb'),
    ('Personal','Visión · Semáforo','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/05_App_01_Semaforo_Color/05_App_01_Semaforo.ipynb'),
    ('Personal','Visión · Contador','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/06_App_02_Contador_Objetos/06_App_02_Contador.ipynb'),
    ('Personal','Visión · Reconocedor','Personal/06_VISION_COMPUTACIONAL/Vision_Computacional/07_App_03_Reconocedor_Patrones/07_App_03_Reconocedor.ipynb'),
    ('Grupal','Fundamentos en parejas','Grupal/01_FUNDAMENTOS_EN_PAREJAS/06_Dos_Casos_Propuestos_Para_Estudiantes.ipynb'),
    ('Grupal','Teachable Machine (pendiente entrenar)','Grupal/04_TEACHABLE_MACHINE/06_CASOS_PRACTICOS/06_Cuaderno_tres_casos.ipynb'),
    ('Grupal','Industria en parejas','Grupal/05_VISION_COMPUTACIONAL_EN_PAREJAS/Vision_Computacional/04_Aplicaciones_Principales/04_Aplicaciones_en_la_Industria.ipynb'),
]

def ghlink(p:str)->str:
    return REPO+'/blob/main/'+quote(p,safe='/')

site=Flask('portal_senati')
@site.get('/health')
def health(): return jsonify({'status':'ok','author':'COCA CCORPA LORENA ABIGAIL'})
@site.get('/javascript/personal/')
def jsp():return redirect('/javascript/personal/index.html')
@site.get('/javascript/grupal/')
def jsg():return redirect('/javascript/grupal/index.html')
@site.get('/javascript/<scope>/<path:asset>')
def files_js(scope,asset):
    dirs={'personal':'Personal/05_JAVASCRIPT_EJERCICIOS/ALGORITMOS Y PROGRAMACIÓN CON JAVASCRIPT',
          'grupal':'Grupal/02_JAVASCRIPT_TRABAJO_EN_EQUIPO/ALGORITMOS Y PROGRAMACIÓN CON JAVASCRIPT'}
    if scope not in dirs:return 'No encontrado',404
    return send_from_directory(BASE/dirs[scope],asset)

PAGE='''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Actividades SENATI · Lorena Abigail</title>
<style>
:root{--bg:#091b29;--blue:#08b8ee;--yellow:#ffc837;--text:#edf9ff;--mute:#abc2d0}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:radial-gradient(circle at 8% 8%,#133b55 0%,transparent 40%),radial-gradient(circle at 90% 5%,#113746 0%,transparent 25%),var(--bg);color:var(--text);font-family:system-ui,-apple-system,Segoe UI,sans-serif;min-height:100vh}
a{color:inherit;text-decoration:none}.shell{max-width:1220px;padding:25px;margin:auto}
nav{display:flex;align-items:center;justify-content:space-between;gap:20px}.logo{font-weight:1000;letter-spacing:.14em;font-size:1.27rem;color:var(--yellow)}.minitag{font-size:.77rem;letter-spacing:.08em;color:#b7cedd;text-transform:uppercase}
.navlink{background:#123448;padding:10px 17px;border-radius:999px;border:1px solid #2b6178;font-weight:700}
header{padding:75px 0 36px;max-width:900px}.eyebrow{font-size:.77rem;color:var(--yellow);text-transform:uppercase;font-weight:800;letter-spacing:.2em}h1{font-size:clamp(2.3rem,6vw,5rem);line-height:1.06;letter-spacing:-.05em;margin:12px 0 21px}h1 strong{color:var(--yellow)}.lead{max-width:780px;font-size:1.09rem;line-height:1.7;color:var(--mute)}
.summary{display:flex;gap:12px;flex-wrap:wrap;margin:25px 0 45px}.chip{background:#112f43;border:1px solid #285168;padding:10px 16px;border-radius:18px;color:#d4eaf3;font-size:.84rem}.chip strong{color:var(--yellow)}
.sectionhead{display:flex;align-items:baseline;justify-content:space-between;gap:15px;margin:46px 0 18px}h2{font-size:1.55rem;letter-spacing:-.03em;margin:0}.hint{font-size:.88rem;color:var(--mute)}.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}.card{border:1px solid #244f66;background:linear-gradient(145deg,#16384c,#0c2637);border-radius:22px;padding:22px;min-height:225px;display:flex;flex-direction:column;transition:transform .2s,border-color .2s}.card:hover{transform:translateY(-4px);border-color:var(--blue)}.tag{font-size:.72rem;color:#7fe0ff;letter-spacing:.12em;text-transform:uppercase;font-weight:900}.tag.group{color:#ffcf64}.card h3{margin:13px 0 8px;font-size:1.19rem}.card p{font-size:.86rem;color:var(--mute);line-height:1.55;margin:0 0 18px;flex:1}.buttons{display:flex;flex-wrap:wrap;gap:10px}.btn{display:inline-flex;align-items:center;justify-content:center;min-height:37px;padding:8px 12px;border-radius:11px;background:var(--yellow);color:#1c2935;font-size:.79rem;font-weight:900}.btn.alt{border:1px solid #42718a;background:transparent;color:#daefff}.notebooks{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px}.nb{border:1px solid #21475c;border-radius:15px;padding:14px 16px;background:#102d3e;display:flex;justify-content:space-between;gap:10px;align-items:center;font-size:.9rem}.nb:hover{border-color:#63bfdf}.nb small{display:block;font-size:.72rem;color:var(--mute);margin-top:4px}.nb .open{font-weight:800;color:var(--yellow);white-space:nowrap;font-size:.82rem}.note{margin:50px 0;border-left:4px solid var(--yellow);padding:17px 20px;background:#142d3c;color:#d7e6ef;border-radius:0 13px 13px 0;line-height:1.6}footer{padding:35px 0 25px;border-top:1px solid #234e60;color:#a7c0d0;font-size:.83rem}
@media(max-width:500px){.shell{padding:18px}header{padding-top:54px}nav{align-items:flex-start}.minitag{max-width:180px}.notebooks{grid-template-columns:1fr}}
</style></head><body><div class="shell">
<nav><div><div class="logo">SENATI<span style="color:var(--blue)"> / ACTIVIDADES</span></div><div class="minitag">Portafolio académico · 2026</div></div><a class="navlink" href="{{ repo }}" target="_blank" rel="noopener">GitHub ↗</a></nav>
<header><div class="eyebrow">Machine Learning · Deep Learning · Desarrollo web</div><h1>Aprender, desarrollar <strong>y demostrar.</strong></h1><p class="lead">Actividades personales y grupales, proyectos en Python y JavaScript y cuadernos Jupyter conservados con sus nombres originales. Autora: <b>COCA CCORPA LORENA ABIGAIL</b>.</p></header>
<div class="summary"><div class="chip"><strong>17</strong> cuadernos originales</div><div class="chip"><strong>6</strong> demos ML ejecutables</div><div class="chip"><strong>2</strong> webs JavaScript</div><div class="chip">Desarrollos señalados en <strong>amarillo</strong> dentro de los cuadernos</div></div>
<div class="sectionhead"><h2>Proyectos interactivos</h2><span class="hint">Prueba las aplicaciones web</span></div><section class="cards">
{% for a in actividades %}<div class="card"><span class="tag {{ 'group' if a[0]=='Grupal' else '' }}">{{ a[0] }}</span><h3>{{ a[1] }}</h3><p>{{ a[5] }}</p><div class="buttons"><a class="btn" href="{{ a[2] }}">Abrir aplicación ↗</a>{% if a[4] %}<a class="btn alt" target="_blank" rel="noopener" href="{{ gh(a[3]+'/'+a[4]) }}">Cuaderno Jupyter</a>{% endif %}</div></div>{% endfor %}</section>
<div class="sectionhead" id="cuadernos"><h2>Cuadernos Jupyter</h2><span class="hint">Nombres oficiales preservados</span></div><section class="notebooks">{% for n in notebooks %}<a class="nb" href="{{ gh(n[2]) }}" target="_blank" rel="noopener"><span>{{ n[1] }}<small>{{ n[2].split('/')[-1] }}</small></span><span class="open">Ver ↗</span></a>{% endfor %}</section>
<div class="note"><b>Actividad Teachable Machine:</b> sus casos y cuaderno están documentados, pero faltan fotografías y entrenamiento del modelo real. La práctica de Git y GitHub de las computadoras 1 y 2 está documentada en Word y no se ha repetido.</div>
<footer>© 2026 · SENATI · COCA CCORPA LORENA ABIGAIL · Portafolio académico</footer>
</div></body></html>'''
@site.get('/')
def home():return render_template_string(PAGE,repo=REPO,actividades=ACTIVIDADES,notebooks=CUADERNOS,gh=ghlink)

MOUNTS={}
for i,(_,name,url,directory,nb,description) in enumerate(ACTIVIDADES[:6]):
    module_path=BASE/directory/'app.py'
    spec=importlib.util.spec_from_file_location(f'senati_case_{i}',module_path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    MOUNTS[url]=module.app

app=DispatcherMiddleware(site,MOUNTS)