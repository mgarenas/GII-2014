# Ejercicios

__Ejercicio 1__ 

La máxima amortización sería del 25%. Luego si tenemos un servidor de 7500 € sin IVA, a 4 años sería por año unos 1875 €.

Si queremos que sea a 7 años tendriamos, variando el porcentaje de amortización (opcional), entonces por ejemplo:
1. el primer año el 20%: 1500.0 €. 

2. el segundo año el 15%: 1125.0 €.

3. el tercer año el 10%: 750.0 €

4. el cuarto y el quito al 15%: 1125.0 €
(Lo que hace un total de 5625.0 €)

5. el sexto año al 20% con un total de 7125.0 €.

6. y el último año al 5% con una suma de 375.0 €
.........
---------

__Ejercicio 2__

Podemos encontrar:
- **City Network (Servidor Cloud):** 0.11 $ / hora.
- **AWS | Amazon EC2 (m3.medium):**  0.07 $ / hora.

Un año tiene 24 h/dia * 365 dia/año = **8760 horas / año**

Por un lado al *1%* tenemos:
- **City Network (Servidor Cloud):** 0.11 $ / hora * 0.01 * 8760 horas = **9.636 $**
- **AWS | Amazon EC2 (m3.medium):** 0.07 $ / hora * 0.01 * 8760 horas = **6.132 $**

Por otro lado al *10%* sería:
- **City Network (Servidor Cloud):** 0.11 $ / hora * 0.1 * 8760 horas = **96.36 $**
- **AWS | Amazon EC2 (m3.medium):** 0.07 $ / hora * 0.1 * 8760 horas = **61.32 $**


**Referencias:**
  
  * https://www.citynetwork.es/
  * http://aws.amazon.com/es/ec2/pricing/

.........
---------
__Ejercicio 3__
- **Alojamiento de varios clientes en un servidor:** 
Optaría por la *virtualización a nivel de sistema operativo* ya que con esta opción la capa de virtualización se ejecuta como una aplicación en el sistema operativo. De este modo el núcleo del sistema operativo se ejecuta sobre el nodo de hardware con varias máquinas virtuales invitadas aisladas puesto que están instaladas sobre el mismo. De esta manera no hay sobrecarga alguna asociada con tener a cada huésped ejecutando un sistema operativo totalmente instalado. Mejorando así el rendimiento.
- **Sistema *web + middleware + BD*:**
Escogería la *virtualización completa*, esta opción no necesita de modificaciones en el sistema operativo host. Se vale de traducción binaria combinando con la ejecución directa. El sistema opertavido se desacopla en su totalidad del hardware que hay por debajo. 
- **Prueba de software e integración continua:**
Elegiría la *virtualización por entornos de desarrollo* ya que nos permite reproducir entornos lo más similar que puede. Se pueden realizar distintas ejecuciones de multiples aplicaciones en distintos lenguajes. 
