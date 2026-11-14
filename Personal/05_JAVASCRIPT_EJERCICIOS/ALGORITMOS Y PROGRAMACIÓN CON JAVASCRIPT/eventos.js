"use strict";
const pruebas={
  1:[[],[],[],[],[],[]],
  2:[[6],[17],[3],[-5],[8,10],[18],[19]],
  3:[[],[],[],[],[],[],[],[[2,5,8,10,15]],[],[5]],
  4:[['Lorena'],[8,3],[9],[10,8],[12,16,18],[24],[19],[5],[7],[17]]
};
document.querySelectorAll('[data-run]').forEach(b=>b.addEventListener('click',()=>{
 const key=Number(b.dataset.run),grupo=key===1?ex01:key===2?ex02:key===3?ex03:ex04,args=pruebas[key];
 document.getElementById('salida'+key).textContent=Object.keys(grupo).map((k,i)=>`${key}.${k} → ${JSON.stringify(grupo[k](...(args[i]||[])))}`).join('\n');
}));
const el=id=>document.getElementById(id);const v=id=>Number(el(id).value);
const salida=s=>{el('eventOutput').textContent=String(s);};
el('hola').addEventListener('click',()=>salida('¡Hola mundo!'));
el('sumar').addEventListener('click',()=>salida(`Suma: ${v('ent1')+v('ent2')}`));
el('par').addEventListener('click',()=>salida(Number.isInteger(v('ent1'))?(v('ent1')%2?'Impar':'Par'):'Debe ser entero'));
el('texto').addEventListener('keydown',e=>{if(e.key==='Enter')salida(`Texto enviado: ${e.currentTarget.value}`);});
el('area').addEventListener('click',()=>salida(v('ancho')>0&&v('alto')>0?`Área: ${v('ancho')*v('alto')}`:'Ingresa dimensiones positivas'));
el('color').addEventListener('click',()=>{document.body.style.background='linear-gradient(130deg,#153c44,#3a3263)';salida('Color de fondo cambiado');});
el('imagen').addEventListener('click',()=>{el('imagen').hidden=true;salida('Imagen ocultada');});
el('reaparecer').addEventListener('click',()=>{el('imagen').hidden=false;salida('Imagen restaurada');});
let clics=0;el('clics').addEventListener('click',()=>salida(`Clics: ${++clics}`));