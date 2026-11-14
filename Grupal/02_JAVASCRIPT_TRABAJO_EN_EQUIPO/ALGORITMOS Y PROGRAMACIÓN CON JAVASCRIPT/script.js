"use strict";
const $ = id => document.getElementById(id);
const valor = id => {const x=Number($(id).value);if($(id).value.trim()===''||!Number.isFinite(x))throw Error('Introduce un número válido.');return x;};
const mostrar = (id, callback)=>{try{$(id).textContent=callback();}catch(e){$(id).textContent=e.message;}};
document.querySelectorAll('[data-op]').forEach(b=>b.addEventListener('click',()=>mostrar('calcOut',()=>{
 const a=valor('numA'),c=valor('numB');const op=b.dataset.op;
 if(op==='dividir'&&c===0)throw Error('No se puede dividir entre cero.');
 const r=op==='sumar'?a+c:op==='restar'?a-c:op==='multiplicar'?a*c:a/c;
 return `Resultado: ${Number(r.toFixed(5))}`;
})));
$('clasificarEdad').addEventListener('click',()=>mostrar('edadOut',()=>{
 const edad=valor('edad');if(!Number.isInteger(edad)||edad<0||edad>125)throw Error('Ingresa una edad entera entre 0 y 125.');
 // Rangos educativos propuestos, no un estándar médico o legal universal.
 return `Clasificación didáctica: ${edad<12?'Niño':edad<18?'Adolescente':edad<60?'Adulto':'Adulto mayor (anciano)'}`;
}));
$('promediar').addEventListener('click',()=>mostrar('notaOut',()=>{
 const nombre=$('nombre').value.trim();if(!nombre)throw Error('Escribe un nombre.');
 const xs=['nota1','nota2','nota3'].map(valor);if(xs.some(x=>x<0||x>20))throw Error('Cada nota debe estar entre 0 y 20.');
 const promedio=xs.reduce((s,x)=>s+x,0)/3;
 return `${nombre}: promedio ${promedio.toFixed(2)} — ${promedio>=14?'APROBÓ':'NO APROBÓ'}`;
}));
$('imcBtn').addEventListener('click',()=>mostrar('imcOut',()=>{
 const p=valor('peso'),h=valor('altura');if(p<=0||h<=0||p>500||h>2.5)throw Error('Revisa peso y altura.');
 const imc=p/(h*h);const grupo=imc<18.5?'Bajo peso':imc<25?'Normal':imc<30?'Sobrepeso':'Obesidad';
 return `IMC ${imc.toFixed(2)} — ${grupo}. Categorías para adultos, orientativas; no son diagnóstico.`;
}));