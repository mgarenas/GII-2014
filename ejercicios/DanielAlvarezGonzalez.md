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
:::js
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
	
	[Enlace al documento creado con el script](https://docs.google.com/open?id=1wuByz3d-V16syNIh-RxfgqSTx4Cl3dnrnetZLfNDzfo)
	

