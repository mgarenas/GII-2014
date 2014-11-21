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
Se van a comparar un servidor VPS de **1&1 Hosting** con un servidor cloud de **Google Compute Ingine**. Elegimos dos servidores de caracteristicas parecidas y hacemos los siguientes calculos

La instancia de Google es la **n1-standard-1**
El servido VPS de de 1&1 Hosting equivalente sería el **Servidor Virtual XL** 

Teniendo esto en cuenta realizamos los calulos para
**1%**
- Google: 87,6h * 0.0551€/h = 4,83€
- 1&1 Hosting: 20€/mes * 12 meses = 240€
- 1&1 Hosting: 10€/mes * 12 meses = 120€ (con la oferta del primer año de descuento)

**10%**
- Google: 876h * 0.0551€/h = 48.34 €
- 1&1 Hosting: 20€/mes * 12 meses = 240€
- 1&1 Hosting: 10€/mes * 12 meses = 120€ (con la oferta del primer año de descuento)

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
- apt-get install cgroup-lite
- ls blkio cpuacct devices hugetlb perf_event cpu cpuset freezer memory systemd

### Ejercicio 8

No he podido realizarlo porque al intentar montar el cgroup me dice que ya se encuentra montado y no me crea los subdirectorios que debería.


#####Corrección de Daniel Díaz Salas

A mí tambien me pasaba esto. En Ubuntu se montan por defecto en _/sys/fs/cgroup_. Mira a ver si tienes todos los subdirectorios ahí.


### Ejercicio 9
**Parte 1**
La limitacion de recursos o de asignación puede ser muy útil en el momento en el que tenemos que tenemos que modificar partes de un servicio que no puede pararse. Podemos poner por ejemplo un servidor que esta dando soporte a aplicaciones Android. Es clave que el servicio no se interrumpa, sin embargo podemos realizar tareas bajando el rendimiento a este servicio. De este modo, podemos modificar la parte del servidor necesaria sin tener que interrumpir el servicio.

Otro escenerio es cuando dos usuarios interactúan con los recursos de un mismo ordenador. Esto permite que ambos usuarios puedan trabajar sin "molestarse" entre ellos.

Tambien es util en el momento de proveer una granja de hosting. Con un solo ordenador particionamos los recursos y se lo vendemos a los clientes.

**Parte 2**

No he podido hacer el ejercicio ya que no me deja montar el cgroup. No obstante, en teoria una vez creado los procesos, la prioridad se estableceria de la siguiente forma en el fichero "cgconfig.conf"

group procesos_usuario{ 
    cpu{
       cpu.shares = "200"; 
    } 
 } 
group procesos_sistema{ 
    cpu{ 
       cpu.shares = "800"; 
    }
}

**Parte 3, 4**

No he podido realizarlo por el problema que he tenido en el Ejercicio 8.


### Ejercicio 10

El modelo de procesador es: Intel(R) Core(TM) i5-3427U CPU @ 1.80GHz

La salida que obtengo con el comando es:
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor **vmx** ds_cpl smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm ida arat xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms

Como podemos ver, mi procesador tiene activado el flag de vmx

### Ejercicio 11

He tenido que instalar el paquete cpu-checker y la salida al comando "kvm-ok" es la siguiente:
INFO: /dev/kvm exists
KVM acceleration can be used

### Ejercicio 12

Un ejemplo claro de de SaaS son los servicios de correo como Gmail, Yahoo o Hotmail. Además de servicios de correo electrónico tambien herramientas como Drive o incluso Dropbox, en algunos aspectos, también podemos considerarlo ejemplos de servicios SaaS de almacenamiento en la "nube".

Últimamente se han añadido servicios SaaS para la generación de documentos en línea como puede ser GitHub o para la gestión de nominas como los distintos ERP

#### Creando aplicaciones en la nube: Uso de PaaS y SaaS

### Ejercicio 1
Se va a instalar un entrono virtual para Python. Para ello, se han utilizado los siguientes comandos
- sudo apt-get install python-pip
- sudo pip install https://github.com/pypa/virtualenv/tarball/develop
- sudo apt-get install curl
- curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz
- tar xvfz virtualenv-1.9.tar.gz
- cd virtualenv-1.9
- sudo python setup.py install

Ejecutamos el entorno usando
- virtualenv ENV
y creamos el ejecutable 
New python executable in ENV/bin/python
Installing setuptools............done.
Installing pip...............done.

### Ejercicio 2
Me he registrado en **Heroku**

### Ejercicio 3
Me he registrado en **OpenShift**
Nos logueamos en la cuenta y seleccionamos la opción de **WordPress 4** en el submenu de "Instant App"
Introducimos en el browser la siguiente dirección e instalamos WordPress
- php-manoletes.rhcloud.com

Rellenamos la información, necesaria y accedemos a nuestro WordPress. Podemos loguearnos en el WordPress pinchando [aqui](https://php-manoletes.rhcloud.com/wp-login.php) o visitar la página en este [enlace](http://php-manoletes.rhcloud.com/). Una vez logueados ya estamos en dispositición de gestionar y personalizar nuestro WordPress

### Ejercicio 4
Nos vamos a la web https://script.google.com/
Una vez dentro, indicamos que vamos a realizar un script para "Documents". Ahí, cambiamos el nombre del proyecto y seleccionamos, por ejemplo, la función "showAlert".

### Ejercicio 5
Un sistema de automatización de la contrucción de ficheros C/C++ sería **make**.
Como entorno de desarrollo uso habitualmente NetBeans o AndroidStudio

### Ejercicio 6
El PaaS elegido es **Heroku** y hemos seleccionado una aplicación en PHP. Como podemos ver [aqui](https://devcenter.heroku.com/articles/getting-started-with-php#declare-app-dependencies) nos indica que se necesita un archivo llamado **composer.json** que se encarga de analizar las dependencias para poder construir el fichero.

### Ejercicio 7
Tanto en NetBeans, Eclipse o Android Studio que son los entornos de desarrollo con los que trabajo usualmente, he estado como sistema de tester JUnit 4 sobre Java. Con el entorno de desarrollo Xcode para iOS también he utilizado el sistema de testeo TDD pero en menor medida



