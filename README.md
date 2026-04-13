# Reto 3: Herencia vs Composición : 🧔 - > 🧑‍🦱
>El siguiente repositorio hace parte de la entrega del reto 3 donde se demuestra la utilidad de la herencia y composición en 
>contextos prácticos, uso de herencia para especificar y extender funciones y uso de objetos cómo parametros

## Tabla de contenidos ✔️
- [Parte 1: Geometrías Básicas](#geometrías-basicas-)
   - [Clase punto y Linea]()
   - [ Rectangulo y Cuadrado]()
     - [Diversidad de parametros]()
- [Parte 2: Restaurante]()
   - [Abstracción de elementos]()
   - [Clase Orden]()
   - [Menu Interactivo]()
- [Observaciones]()
- [Referencias]()
  
---

Una vez comprendido cómo funciona el paradigma orientado a objetos, se busca aplicar sus pilares fundamentales
a partir de problemas que los evidencien en contextos cotidianos.
- Inicialmente, se propone concebir geometrías simples a partir de la *Abstracción* de lineas y rectangulos en un plano cartesíano,
donde podremos obtener cualquiera de estos y relacionarlos entre ellos.
- Más adelante, se aplicarán los pilares a partir de un contexto de restaurante cotidiano, donde deberemos tomar una orden a partir 
de un menu, y socializar un costo.

Evidenciamos a partir de estos el uso de la **Abstracción** cómo medida para transformar elementos de la vida real en objetos
códificables por la computadora; de la **Herencia** y **Composición** en la generación de clases y métodos que pertenezcan y se
relacionen entre *superclases*

---

## Geometrías Basicas 📐 
  A partir de este ejercicio se busca formular una clase Rectangulo, capaz de inicializarse a partir de diferentes métodos;
  generar una subclase cuadrado y evaluar si un punto dado se encuentra en el interior o no de estos

### Formación plano cartesiano: 📋

Para formar cualquier geometría debemos partir de alguna referencia, un "campo de juego" donde podramos generar y manipularlas bajo diferentes parametros.

Cómo objeto que nos capacitara para poder crear cualquier geometría, se genero la clase **Point** con las coordenadas (x,y) cómo atributos asignables,
permitiendo asi *abstraer* un plano cartesiano al colocar cualquier numero real cómo parametro de estos.


