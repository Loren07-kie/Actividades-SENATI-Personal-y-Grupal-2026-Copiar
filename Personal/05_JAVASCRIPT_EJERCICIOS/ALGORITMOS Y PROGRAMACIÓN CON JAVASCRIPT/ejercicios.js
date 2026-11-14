"use strict";
/* ALGORITMOS Y PROGRAMACIÓN CON JAVASCRIPT — ejercicios propuestos, páginas 1 a 6. */
/* Autora académica: COCA CCORPA LORENA ABIGAIL | SENATI 2026 */
// 01 VARIABLES — 6 ejercicios
const ex01={
  1:()=>{let nombre="Lorena Abigail";return nombre;},
  2:()=>{let edadEjemplo=20,carreraEjemplo="Tecnologías de la Información",ciudadEjemplo="Satipo";return {edadEjemplo,carreraEjemplo,ciudadEjemplo};},
  3:()=>{const pi=3.1416;return pi;},
  4:()=>{const nombre="Juan",edad=20,ciudad="Lima";return `Hola, mi nombre es ${nombre}, tengo ${edad} años y vivo en ${ciudad}`;},
  5:()=>{const a=12,b=8;return a+b;},
  6:()=>{const nombre="Ana",edad=18,activo=true;return {nombre,edad,activo,tipos:[typeof nombre,typeof edad,typeof activo]};}
};
// 02 CONDICIONALES — 7 ejercicios
const ex02={
  1:n=>n%2===0?'Par':'Impar',
  2:n=>n>=18?'Mayor de edad':'Menor de edad',
  3:n=>['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'][n-1]??'Valor inválido (1–7)',
  4:n=>n>0?'Positivo':n<0?'Negativo':'Cero',
  5:(a,b)=>a>b?'Primero mayor':a<b?'Segundo mayor':'Iguales',
  6:n=>n>=18?'Puede votar según este criterio de edad':'No cumple el criterio de edad',
  7:n=>n>18?'Excelente':n>=14&&n<18?'Buena':n>=11&&n<14?'Regular':n>=0&&n<10?'Mala':n===10||n===18?'Sin categoría explícita en el PDF':'Nota inválida'
};
// Nota: el PDF deja los valores 10 y 18 sin categoría explícita; se informan como ambiguos.
// 03 BUCLES — 10 ejercicios
const rango=(a,b)=>Array.from({length:b-a+1},(_,i)=>a+i);
const factorial=n=>{if(!Number.isInteger(n)||n<0)throw Error('n debe ser entero no negativo');let f=1;for(let i=2;i<=n;i++)f*=i;return f;};
const ex03={
  1:()=>rango(1,10),
  2:()=>rango(1,100).reduce((a,b)=>a+b,0),
  3:()=>rango(1,20).filter(n=>n%2===0),
  4:()=>rango(1,10).map(n=>`5 x ${n} = ${5*n}`),
  5:()=>rango(1,50).filter(n=>n%3===0),
  6:()=>rango(1,10).reverse(),
  7:()=>rango(1,100).filter(n=>n%2===0).reduce((a,b)=>a+b,0),
  8:(numeros=[2,5,8,10,15])=>{if(numeros.length!==5)throw Error('Se requieren cinco números');return numeros.reduce((a,b)=>a+b,0)/5;},
  9:()=>rango(1,10).map(n=>n*n),
 10:n=>factorial(n)
};
// 04 FUNCIONES — 10 ejercicios
const ex04={
  1:nombre=>`Hola, ${nombre}`,
  2:(a,b)=>a+b,
  3:n=>n%2===0?'Par':'Impar',
  4:(base,altura)=>base*altura/2,
  5:(a,b,c)=>(a+b+c)/3,
  6:c=>(c*9/5)+32,
  7:edad=>edad>=18?'Puede votar por edad':'No puede votar por edad',
  8:n=>factorial(n),
  9:n=>Array.from({length:Math.max(0,Math.floor(n))},(_,i)=>(i+1)*2),
 10:n=>{if(!Number.isInteger(n)||n<2)return false;for(let i=2;i*i<=n;i++)if(n%i===0)return false;return true;}
};
if(typeof module!=='undefined'&&module.exports)module.exports={ex01,ex02,ex03,ex04};