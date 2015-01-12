#Sesión del 17 de Octubre
##Ejercicio 01

Servidor en la dirección [Servidor](http://www.dell.com/es/empresas/p/poweredge-t630/pd?~ck=anav)
Precio 5007€, precio sin IVA 4138.016
Amortización a 4 años --> 1034.50
Amortización a 7 años --> 591.145

##Ejercicio 02
AMAZON (AWS)
c3.2xlarge	8 núcleos	15 GiB de RAM	2x80GB de almacenamiento SSD -->  0.468$ por hora en la tarifa por un año
En este caso, el precio por el uso del servicio durante un 1% de un año sería de 40.99$, que al cambio son 32.127€
Por otro lado, el precio del uso correspondiente a un 10% del año, sería 409.96$ que al cambio son 321.319€.


AZURE
A4	8 núcleos	14,00 GB RAM	605 GB	de disco --> 0,5362€ por hora

En el servicio de Microsoft, el precio por el uso durante un 1% del año sería 46.97€.
Por lo tanto, el precio por el servicio durante un 10% del año es 469.71€.

Correción por parte de Jesús Maillo:
Por un error de comprensión común en la mayoría de la clase paso a comparar tu máquina de Azure con una de pago por mensualidades de características similares.

Mirando en la [calculadora de precios de Azure](http://azure.microsoft.com/es-es/pricing/calculator/?scenario=cloud) he comprobado que el pago anual de la máquina A4 es de 354€ lo que lleva a:
* El precio por el uso durante un 1% del año sería 46.97€ + 354 = 400.97€.
* El precio por el servicio durante un 10% del año es 469.71€ + 354 = 823.71€.

El servidor encontrado es: [OVZ-12GB](https://demonvps.com/vps-hosting/)

Tiene 8 cores, 12 de Ram y un almacenamiento similar sale por 47.94€ mensuales o si se paga anualmente por un total de 558.04€

Merece la pena en ambos casos, sin tener en cuenta que tiene menos capacidad de memoria.



##Ejercicio 03
Tipo de virtualización que utilizaría en cada caso y por qué

- Como la mayoría de mis compañeros, para alojar varios clientes en un mismo servidor, la virtualización sería a nivel de sistema operativo. De esta forma, cada cliente es completamente independiente del resto.

- Para un sistema eficiente de web + middleware + base de datos, la virtualización sería plena.  De esta forma, el sistema resultante será más potente y facilitará la ejecución de todas las apliaciones.

- Por último, para un sistema de prueba de software e integración continua, sería una virtualización de entornos de desarrollo ya que esta tipo de virtualización está especialmente preparado para esta tarea.

Para instalar CDE seguir el siguiente [tutorial](http://www.pgbovine.net/cde.html)



##Ejercicio 04

**Descarga e instalación de docker**
Instrucciones para [descargar e instalar docker](https://docs.docker.com/installation/ubuntulinux/#ubuntu-precise-1204-lts-64-bit)

Una vez que hemos instalado docker, podemos instalar una aplicación siguiendo los pasos del [tutorial](https://www.docker.com/tryit/#1)
	1- docker search tutorial
	2- docker pull learn/tutorial
	3- docker run learn/turorkal echo 'Hello World'
	4- docker run learn/tutorial apt-get install -y ping
	5- docker commit *ContainerID* learn/ping (docker ps -l para encontrar el ID de nuestro contenedor)
	6- docker run learn/ping www.google.es
	7- Para obtener información acerca de nuestros contenedores en funcionamiento
		- docker ps (para obtener los IDs)
		- docker inspect
	8- docker push learn/ping

Todos estos pasos los he seguido en mi ordenador, he instalado dockers y he seguido el tutorial completo del enlace que se facilita en el enunciado del ejercicio.


##Ejercicio 05
[Instalación y configuración ubuntu 12.04](http://www.liquidweb.com/kb/how-to-install-git-on-ubuntu-12-04/)
Instalar el sistema de gestión de fuentes **git** es tan sencillo como introducir dos líneas de comando:
	1- apt-get update
	2- apt-get install git-core

Una vez que lo tenemos instalado, hay que configurarlo, asignándote un usuario y un correo que te identifiquen y ayuden a prevenir errores de commit. Este proceso es igualmente sencillo:
	1- git config --global user.name "Tu Usuario"
	2- git config --global user.email "tucorreo@ejemplo.com"

Puedes comprobar los datos de configuración de tu git de la siguiente forma:
	- git config --list


##Ejercicio 06
Para crear un nuevo proyecto o repositorio en gitHub, pinchamos en la pestaña **Create New --> New Repository** al lado de nuestro nombre de usuario en la web de GitHub. Nos pide un nombre para el proyecto y nos da la opción de inicializarlo con un fichero README.
	Una vez creado el nuevo repositorio, lo clonamos a nuestro directorio de trabajo git con el comando  **git clone *url_proyecto*
	Cuando se ha modificado el README como pide el ejercicio, hay que formalizar dicho cambio. Para ello hay que hacer un **commit** de la siguiente forma --> **git commit -a -m "comentario que define el cambio realizado"**.
	Ya que se ha formalizado el cambio, solo queda subir dicho cambio al repositorio de GitHub haciendo un **git push**.




##Ejercicio 07
En mi instalación de Ubuntu 12.04 LTS se hizo la instalación de cgroups en el punto **/sys/fs/cgroup/ y contiene los siguientes directorios:
		- blkio
		- cpu
		- cpuacct
		- cpuset
		- devices
		- freezer
		- hugetlb
		- memory
		- perf_event

Dentro de estos directorios se encuentran los ficheros que se muestran como ejemplo en el fichero de objetivos y muchos más.







##Ejercicio 08

Para este ejercicio se han creado tres grupos de control *good*, *regular* y *bad* dentro del directorio cgroup. Para ello se ha utilizado las líneas de comandos:

	- **sudo cgcreate -g memory,cpu,cpuacct:good**
	- **sudo cgcreate -g memory,cpu,cpuacct:regular**
	- **sudo cgcreate -g memory,cpu,cpuacct:bad**

Una vez creados los grupos de control, se han lanzado procesos en cada uno de ellos con los siguientes comandos:
	- **sudo cgexec -g memory,cpu,cpuacct:good firefox &**
	- **sudo cgexec -g memory,cpu,cpuacct:resgular lowriter &**
	- **sudo cgexec -g memory,cpu,cpuacct:bad gimp &**


Los resultados obtenidos de uso de cpu, consultando en cada grupo control: **cat /sys/fs/cgroup/cpuacct/good|regular|bad/cpuacct.usage** son los siguientes:

	- grupo **good** ejecutando firefox, uso de cpu 3161809980
	- grupo **regular** ejecutando libreoffice, uso de cpu 2969369788
	- grupo **bad** ejecutando el editor de imágenes gimp, uso de cpu 4422939045



##Ejercicio 09

**Apartado 9.1**


**Apartado 9.2**


**Apartado 9.3**


**Apartado 9.4**

##Ejercicio 10
	**Modelo de procesado:** Intel® Core™ i5-2450M CPU @ 2.50GHz × 4
	**Salida por pantalla:** flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse 					sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc 					aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 					x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi 					flexpriority ept vpid



 eso

##Ejercicio 11

Salida tras ejecutar el comand *kvm-ok*:
	INFO: /dev/kvm does not exist
	HINT:   sudo modprobe kvm_intel
	INFO: For more detailed results, you should run this as root
	HINT:   sudo /usr/sbin/kvm-ok

Tras ejecutar el comando que se sugiere (sudo modprobe kvm_intel) y volver a consultar (kvm-ok), la salida es:
	INFO: /dev/kvm exists
	KVM a-cceleration can be used


##Ejercicio 12

Una aplicación SaaS es aquella en la que el soporte lógico y los datos que se manejan se alojan en el servidor que proporciona el servicio. Por esto, normalmente el usuario no tiene que instalar nada en su ordenador, bastando con un navegador web para hacer uso de dicho servicio. Algunos ejemplos de este tipo de software es la gama de servicios que ofrece Google tales como Gmail, Google Maps, Google Drive, etc. También son de este tipo los servicios de almacenamiento en la nube como Dropbox o Mega.




#Sesión del 3 de Noviembre
##Ejercicio 01

He escogido instalar **virtualenv** para python. Los pasos que he seguido han sido:
	- $ [sudo] pip install virtualenv para instalar virtualenv en mi equipo.
	- $ virtualenv ENV para crear el directorio ENV, donde se almacenarán todas las librerías que instale.


##Ejercicio 02
He escogido [Openshift](https://www.openshift.com/)

##Ejercicio 03

Para instalar wordpress en una aplicación de OpenShift, lo primero es crear la aplicación. Para ello, desde la interfaz web de OpenShift, en la pestaña *Applications* se escoge la opción de añadir una nueva aplicación o crear tu primera aplicación (si es el caso).
Dentro de las opciones, escoger una aplicación de tipo *Wordpress 4* y se configura, entre otras cosas, dándole una URL con la que acceder al wordpress. Por último, se crea un blog y una entrada para comprobar que funciona.
	[Enlace a mi blog](https://php-crixo24.rhcloud.com/) creado desde la aplicación hecha en Openshift.

##Ejercicio 04

js:

	function CrearDocumento() {
		// Crea el documento con el nombre 'Hello, world!'
		var doc = DocumentApp.create('Hello, world!');

		// Accede al fichero y escribe en él
		doc.getBody().appendParagraph('This document was created by Google Apps Script.');

		// Obtiene la url del fichero creado
		var url = doc.getUrl();

		// Obtiene la dirección de correo del usuario que crea este script (yo)
		var email = Session.getActiveUser().getEmail();

		// Coge el nombre del fichero para usarlo como asunto en el correo que va a mandar
		var subject = doc.getName();

		// Añade texto al email
		var body = 'Link to your doc: ' + url;

		// Envía el email con el enlace al fichero creado.
		GmailApp.sendEmail(email, subject, body);
	}
[highlight.js]: http://softwaremaniacs.org/soft/highlight/en/

[Enlace al documento creado con el script](https://docs.google.com/open?id=1wuByz3d-V16syNIh-RxfgqSTx4Cl3dnrnetZLfNDzfo)


##Ejercicio 05

El software que he encontrado para el proceso de autmatización de la construcción para Python (Build automation) es [PyBuilder](http://pybuilder.github.io/). Está escrito completamente en Python y orientado principalmente para aplicaciones Python. Está basado en el concepto de programación basado en dependencias, pero además incluye una gran cantidad de plugins, que permiten la creación de ciclos de construcción, similar al funcionamiento de las herramientas de este tipo para Java. En este repositorio de [GitHub](https://github.com/pybuilder/pybuilder) se explica cómo instalarlo y algunos de los plugins más usados.


## Ejercicio 06
En OpenShift, la herramienta que se utiliza para la automatización de la construcción de las aplicacioens es [Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Meet+Jenkins). Es una aplicación con dos funciones principales:
	1- Construir/testear proyectos software constantemente
	2- Monitorizar ejecuciones de tareas externas.

Para inicializar la aplicación, OpenShift busca por defecto un fichero llamado **server.js**.


## Ejercicio 07
Python incluye una gran cantidad de [módulos](https://wiki.python.org/moin/PythonTestingToolsTaxonomy) para realizar tests, entre los que destacan:

- [unittest](https://docs.python.org/2/library/unittest.html): Fue el primer marco de trabajo para realizar tests incluido en la librería estandard de Python.
- [doctest](https://docs.python.org/2/library/doctest.html): Busca trozos de texto interactivo en sesiones de Python y los ejecuta para comprobar su correcto funcionamiento.
- [pytest](http://pytest.org/latest/): Módulo para buscar y ejecutar tests. Se caracteriza por parar en el primer fallo que encuentre y lanzar **pdb** (python debbuger), etc.

**Habitualmente, en el entorno python, se utiliza [nose](https://nose.readthedocs.org/en/latest/) que ejecuta los test de forma automática y los resultados se dan en OK o No Ok, si se han pasado o no.**

***

#Sesión del 24 de Noviembre

##Ejercicio 01

Para crear el espacio de nombres hay que poner lo siguiente:
**sudo unshare -m /bin/bash**

La opción **-m** indica que se va a crear un *namespace* de tipo montaje (mount).

Para montar la imagen.iso:
**mount -o loop imagen.iso /mnt**

Haciendo esto, se puede comprobar que desde fuera del *namespace* que hemos creado, no se pueden ver los archivos que haya dentro de la imagen que hemos montado.


##Ejercicio 02

**Primer apartado**

Aquí se muestran los puentes configurados en mi máquina:

daniel@daniel-Aspire-5750G:~/Dropbox/GitHub/CloudComputing$ brctl show

bridge name	bridge id		STP enabled	interfaces
alcantara		8000.dc0ea1221919	no		eth0

**Segundo apartado**

Para crear el nuevo puente: **sudo brctl addbr CloudComputing**

Para añadir el puente creado a un interfaz: **sudo brctl addif CloudComputing eth0**

Consulta de puentes configurados en mi máquina: **ip addr show**

eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000

***

#Sesión del 28 de Noviembre

##Ejercicio 03

El primer apartado no se ha podido realizar, porque el enlace a la distro no está disponible, por lo que no se puede descargar.

En el segugundo apartado, para crear un sistema Fedora con Rinse, primero se instala Rinse con:

**sudo apt-get install rinse**

Una vez instalado, se comprueban las verisones que se pueden instalar:

**rinse --list-distribution**

Para terminar, se crea el el sistema Fedora con el comando:

**sudo rinse --arch=i386 --distribution fedora-core-10 --directory /home/jaulas/fedora/**


##Ejercicio 04

Para no instalar otra jaula ḿas en mi equipo, he utilizado la máquina de Fedora instalada en el ejercicio anterior.
Para entrar en la jaula, se introduce el siguiente comando:

**sudo chroot /home/jaulas/fedora**

Una vez en la jaula de fedora, he hecho **mount** para montar el sistema de ficheros y así poder trabajar desde ahí. Después, para comprobar que la jaula es funcional, he hecho dos pruebas:

- La primera ha sido ejecutar la orden **top**.
- La segunda, ha sido crear un fichero con un texto de prueba y leerlo.

Ambas pruebas han funcionado sin problema ninguno dentro de la jaula de Fedora instalada.


##Ejercicio 05

Para este ejercicio, he instalado una jaula de debian con el comando:

**sudo debootstrap --arch=i386 wheezy /home/jaulas/debian http://ftp.us.debian.org/debian**

El primer pado ha sido montar el sistema de archivos: **mount -t proc proc /proc**

A continuación, se instala el servidor web de altas prestaciones *nginx* con la orden ** apt-get install nginx**

Por último, se ha ejecutado *nginx*. Para comprobar que efectivamente se ha ejecutado, se escribe el comando **ps -ax | grep nginx**, lo cuál nos muestra los procesos de nginx en ejecución. El resultado obtenido ha sido el siguiente:

20481 ?        Ss     0:00 nginx: master process nginx
20482 ?        S      0:00 nginx: worker process
20483 ?        S      0:00 nginx: worker process
20484 ?        S      0:00 nginx: worker process
20485 ?        S      0:00 nginx: worker process
20640 ?        S+     0:00 grep nginx


##Ejercicio 06

Para realizar este ejercicio, lo primero ha sido instalar **jailkit**. Para ver los pasos que he seguido pinchar [aquí](http://www.binarytides.com/install-jailkit-ubuntu-debian/).

Siguiendo los pasos que se explican, he creado un sistema de ficheros poesído por *root*:

**mkdir -p /seguro/jaulas/dorada
chown -R root:root /seguro**

Una vez creado, se instalan una serie de editores y sus dependencias:

**jk_init -v -j /seguro/jaulas/dorada jk_lsh basicshell netutils editors**

Por último, se añade el usuario que se desee a la jaula:
**sudo jk_jailuser -m -j /seguro/jaulas/dorada alguien**

Y se configura el fichero /etc/passwd para que pueda acceder desde su shell, quedando el fichero de la siguiente forma:

root:x:0:0:root:/root:/bin/bash
daniel:x:1000:1000:Daniel,,,:/home/daniel:/bin/bash

***

#Sesión del 1 de Diciembre

##Ejercicio 01

Para instalar la herramienta LXC para la creación de contenedores:
**sudo apt-get install lxc**


##Ejercicio 02

He creado un contenedor llamado *ubuntuContenedor* con la orden **sudo lxc-create -t ubuntu -n contenedorUbuntu**

Una vez creada, la he iniciado de la siguiente forma: **sudo lxc-start -n contenedorUbuntu**

Los puentes creados son los siguientes:

ubuntu@contenedorUbuntu:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 00:16:3e:a1:03:5a  
          inet addr:10.0.3.200  Bcast:10.0.3.255  Mask:255.255.255.0
          inet6 addr: fe80::216:3eff:fea1:35a/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:48 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:7944 (7.9 KB)  TX bytes:2781 (2.7 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)



##Ejercicio 03

El ejercicio pide en general, crear dos contenedores: uno basado en mi distribución y otro en otra distinta. Como para el ejercicio anterior ya creé un conteneder basado en mi distribución (*contenedorUbuntu*), ahora sólo queda crear un contenedor en otra distribución.
He creado un contenedor basado en Debian con la orden: 

**sudo lxc-create -t debian -n contenedorDebian**

Una vez instalado, compruebo que están los dos contendores:

[daniel: ~/Dropbox/GitHub/CloudComputing ]$ sudo lxc-list
RUNNING

FROZEN

STOPPED
  contendorDebian
  contenedorUbuntu


##Ejercicio 04

Para instalar lxc-webpanel lo único que hay que hacer es seguir las instrucciones de la [página oficial](https://lxc-webpanel.github.io/install.html)

Aquí muestro una captura de pantalla de mi **Web Panel**:
![captura web panel](http://fotos.subefotos.com/d0d4f1019916541e32c67f90352fa86eo.png "Web Panel")


Para el segundo apartado he iniciado el contenedor de Debian y le he limitado un poco la memoria que puede usar. En la siguiente imagen se puede ver que el contenedor está iniciado y que la memoria y está al máximo, como viene por defecto. Una vez hechos los cambios hay que darle al botón **Aplicar** que está situado al final de la página de Web Panel y no se ve en la captura.

![Captura contenedorDebian](http://fotos.subefotos.com/02a2ad546d23b56fae2877f99cf4ff3eo.png "Contenedor Debian modificado")



##Ejercicio 05

Para comparar las prestaciones en ambas situaciones, se ha aplicado en ambas un benchmark de apache con la siguiente orden
**ab -n 1000000 -c 10 http: //localhost/index.html**

Los resultados para el contenedor han sido:
	
	Server Software:        nginx/1.1.19
	Server Hostname:        localhost
	Server Port:            80

	Document Path:          /index.html
	Document Length:        151 bytes

	Concurrency Level:      10
	Time taken for tests:   64.304 seconds
	Complete requests:      1000000
	Failed requests:        0
	Write errors:           0
	Total transferred:      362000000 bytes
	HTML transferred:       151000000 bytes
	Requests per second:    15551.08 [#/sec] (mean)
	Time per request:       0.643 [ms] (mean)
	Time per request:       0.064 [ms] (mean, across all concurrent requests)
	Transfer rate:          5497.55 [Kbytes/sec] received

	Connection Times (ms)
	              min  mean[+/-sd] median   max
	Connect:        0    0   0.1      0      10
	Processing:     0    0   0.3      0      50
	Waiting:        0    0   0.3      0      50
	Total:          0    1   0.3      1      50

	Percentage of the requests served within a certain time (ms)
	  50%      1
	  66%      1
	  75%      1
	  80%      1
	  90%      1
	  95%      1
	  98%      1
	  99%      1
	 100%     50 (longest request)

Y aquí muestro los resultados del mismo test para la jaula:

	Server Software:        nginx/1.2.1
	Server Hostname:        127.0.0.1
	Server Port:            80

	Document Path:          /index.html
	Document Length:        151 bytes

	Concurrency Level:      10
	Time taken for tests:   55.696 seconds
	Complete requests:      1000000
	Failed requests:        0
	Write errors:           0
	Total transferred:      361000000 bytes
	HTML transferred:       151000000 bytes
	Requests per second:    17954.49 [#/sec] (mean)
	Time per request:       0.557 [ms] (mean)
	Time per request:       0.056 [ms] (mean, across all concurrent requests)
	Transfer rate:          6329.66 [Kbytes/sec] received

	Connection Times (ms)
	              min  mean[+/-sd] median   max
	Connect:        0    0   0.1      0       7
	Processing:     0    0   0.2      0      22
	Waiting:        0    0   0.2      0      22
	Total:          0    1   0.2      1      23

	Percentage of the requests served within a certain time (ms)
	  50%      1
	  66%      1
	  75%      1
	  80%      1
	  90%      1
	  95%      1
	  98%      1
	  99%      1
	 100%     23 (longest request)

Como se puede ver, aunque los resultados no difieren mucho, son mejores para la jaula. El tiempo de ejecución del test es menor (tanto en general como individual por cada petición). Además, el ratio de transferencia de datos es mayor en la jaula y el número de peticiones por segundo también es mayor.