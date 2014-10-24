Ejercicio Jorge Gonzalez Peregrin
=================================

## 17-oct-2014

### Ejercicio 1

https://www.mountain.es/servidores/zircon-40
**Precio**
Con IVA: 1919€
Sin IVA: 1585,95€

**Amortizacion**
Cuatro años: 396,49€ por año
Siete años: 226,56€ por año

### Ejercicio 2
Se han comparado una instancia virtual de **Google Compute Ingine** con una de **Amazon Web Service**. Ambas poseen 4 nucleos virtuales de procesadores similares al Intel Xeon E5-2670 con 16GB de RAM.

La instancia de Google es la **n1-standard-4** que cuesta 0,276$/h
La instancia de Amazon es la **m3.xlarge** que cuesta un primer pago anticipado $439 mas una cuota de 0,308$/h

Teniendo esto en cuenta realizamos los calulos para
**1%**
-Amazon: 439$ + 87,6h * 0,308$/h = 465,98$
-Google: 87,6h * 0,276$/h = 24,17 $

**10%**
-Amazon: 439$ + 876h * 0,308$/h =4659,8 $
-Google: 876h * 0,276$/h = 241,77 $

### Ejercicio 3

1. Alojar varios clientes en un sólo servidor. Utilizaria un sistema de virtualizacion a nivel de sistema operativo para que cada cliente pudiese realizar sus tareas independientemente del número de clientes alojados en el servidor, ya que estos se encuentran aislados unos de otros.

2. Crear un sistema eficiente de web + middleware + base de datos. Utilizaría un sistema de virtualización pleno porque me permitirá virtualizar un sistema completo. Gracias a los programas de control se abarcarían las necesidades de crear un sistema web, middleware y una base de datos. 

3. Sistema de prueba de software de integración continua. La virtualización de entornos de desarrollo nos permitiría abordar el supuesto sistema, ya que nos facilita la labor de verificación de una aplicación en distintas versiones con una sola orden, así como, reescribirlo en diferentes lenguajes.

### Ejercicio 4

Para realizar el ejercicio se han introducido dentro del simulador, se han seguido los siguientes:
- docker version
- docker search tutorial
- docker pull learn/tutorial
- docker run learn/tutorial apt-get install -y ping
- docker ps -l
- docker commit 6982 learn/ping
- docker ps -l
- docker run learn/ping ping google.com
- docker ps -l
- docker inspect efe

### Ejercicio 5

Se ha instalado el sistema de gestión de fuentes git con el commando:
- sudo apt-get install git

### Ejercicio 6

Para realizar este ejercicio se han seguido las siguientes órdenes.
- He creado en GitHub un nuevo repositorio con el nombre "MiProyecto" junto con el archivo README
- git clone https://github.com/Georgevik/MiProyecto.git
- cd MiProyecto
- gedit README.md
- git commit -m "Primera modificacion"

### Ejercicio 7




