Ejercicios de Daniel Díaz Salas
===============================
Ejercicio 1
-----------
Para este ejercicio he elegido el [Fujitsu Primergy TX300 S8 Formato Torre](http://www.pccomponentes.com/fujitsu_primergy_tx300_s8_formato_torre.html "PcComponentes").

El precio con IVA es de 899€, y sin IVA 742.98€. Por lo tanto se puede amortizar a 4 años a **185.75€** y  **106.14€** a 7 años.

Ejercicio 2
-----------

Para este ejercicio he elegido estos dos servicios:
[### Google Cloud Platform ###](https://cloud.google.com/products/calculator/ "Google Cloud")
Un servidor con:
- 2 cores.
- 7.5 GB de RAM.
- Resto de opciones por defecto.
- Precio: 22.74$ al mes por un uso inferior al 25%.
Un disco persistente con:
- 100 GB de SSD.
- Resto de opciones por defecto.
- Precio: 32.50 al mes.

- Precio por usarlo un 1%:
    + Precio servidor por hora: 22.74 $/mes / (30 días/mes * 24 horas/día) = 0.03158 $/hora (Servidor de procesamiento)
    + Precio servidor por año: 0.03158 $/hora * 24 horas/día * 30 días/mes * 12 meses/año / 100 = 2.728512 $/año
    + Precio disco duro por año: 32.50 $/mes * 12 meses/año = 325 $/año
    + **Precio total: 325 $/año + 2.728512 $/año = 327.73 €/año**
- Precio por usarlo un 10%:
    + Precio servidor por año = 27.28512 $/año
    + **Precio total: 325 $/año + 27.28512 $/año = 352.29 €/año**      
[### Microsoft Azure ###](http://azure.microsoft.com/es-es/pricing/calculator/?scenario=cloud "Microsoft Azure")
Una Instancia de rol web y de trabajo con un D2 que tiene:
- 2 cores.
- 7 GB de RAM.
- 100 GB de SSD.
**Precio: €0,237/hr**

- Precio por usarlo un 1%:
    + Precio servidor por año = 0.237 $/hora * 24 horas/día * 30 días/mes * 12 meses/año / 100 = **20.48 €/año**.
- Precio por usarlo un 10%:
    + Precio servidor por año = 20.48 €/año * 10 = **204.8€/año**.

Ejercicio 3
-----------
- **Varios clientes en un servidor**: usaría virtualización a nivel de sistema operativo, ya que aisla los invitados y el anfitrión.
- **Un sistema eficiente de web + middleware + base de datos**: como se necesita tanto espacio de disco, mucha memoria y un procesador para hacer las consultas no queda otra que utilizar virtualización plena.
- **Un sistema de prueba de software e integración continua**: usaría virtualización de entornos de desarrollo, de todas las opciones es la más obvia.