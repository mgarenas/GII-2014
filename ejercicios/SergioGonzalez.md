
Ejercicios de Sergio González
=============================

##TEMA 1:

### Ejercicio 1:

SERVIDOR HP PROLIANT ML350P G8 XEON E5-2609 2.4 GHz 4GB DISCO DURO HDD 2.5" SFF P420I 512MB FBWC 460W CS GOLD

* Precio con IVA: 1744,00€
* Precio sin IVA: 1441,00€

* A cuatro años: 360,25€ anuales.
* A siete años: 205,857 anuales.


### Ejercicio 2:

| Servicio | vCores | HDD (GB) | RAM (GB) | Factura/mes ($)   | Factura/h  ($) | Pago anticipado ($) |
|----------|--------|----------|----------|-------------------|----------------|---------------------|
|1and1     | 4      | 1000     | 16       |     100     	  | -              |     -      	     |
|Amazon    | 4 	    | 800	   | 30.5     |  	-       	  | 0.369          |     644    	     |

* Para el 1% del año (3,65 dias, 88 horas) y 10% del año (36,5 dias, 880 horas):

| Servicio | Precio ($)/1% año  | Precio ($)/10% año |
|----------|--------------------|--------------------|
|VPS 1and1 | 1200               | 1200  	         |
|Amazon    | 676,47 	        | 968,72 	         |


### Ejercicio 3:

### Ejercicio 3.1:

* Alojar varios clientes en un mismo servidor: Para ello, utilizaría una virtualización a nivel de sistema operativo, ya que, de esta manera, los clientes podrán acceder al sistema, quedando de manera independiente unos de otros y dando la sensación de que cada uno posee su sistema.

* Sistema eficiente de web+middleware+base de datos: Lo más adecuado de usar sería una virtualización plena, ya que dicho sistema requiere todos los recursos de la máquina, y es la manera más propia de crear un sistema eficiente.

* Sistema de prueba de software e integración continua: Usaría una virtualización de entornos de desarrollo que está centrado principalemente en objetivos relacionados con el desarrollo de software como el de pruebas, permitiendo la ejecución de diferentes versiones del mismo software. 

### Ejercicio 3.2:
He seguido un tutorial en español que ha dejado uno de mis compañeros: [Cómo crear aplicaciones portables de Linux](http://blog.desdelinux.net/como-crear-aplicaciones-portables-de-linux/)


### Ejercicio 4:

Comandos:
1. docker version
2. docker search tutorial
3. docker pull learn/tutorial
4. docker run learn/tutorial echo "hello world"
5. docker run learn/tutorial apt-get install -y ping
6. docker commit 6982a9948422 learn/ping
7. docker run learn/ping ping www.google.com
8. docker inspect efefdc
9. docker push learn/ping


### Ejercicio 5:

En Ubuntu, basta con ejecutar sudo apt-get install git.
Para el mac, lo he instalado descargandolo de http://git-scm.com/downloads


### Ejercicio 6:

El repositorio generado se puede encontrar en el siguiente [enlace](https://github.com/sergiogvz/prueba) y el archivo README, [aquí](https://github.com/sergiogvz/prueba/blob/master/README.md).


### Ejercicio 7:

Mi instalación es un Ubuntu 14.04 y efectivamente se ha instalado cgroups con ella. Se ha montado en /sys/fs/cgroup. Ahí solo encontraremos systemd y dentro:
cgroup.clone_children  cgroup.procs          notify_on_release  tasks
cgroup.event_control   cgroup.sane_behavior  release_agent      user


### Ejercicio 8:

  	sudo su
	cd /sys/fs/cgroup/
    mkdir group1 group2 group3
 
 Cuando realizo esto, no genera los archivos que debería, por lo que añadir los ficheros con el echo no tiene mucho sentido, aun así intentandolo obtengo un error de disco lleno. Probando intenté hacerlo en systemd, ya que pensé que quizás solo podría realizarlo ahí. Al generar los nuevos subdirectorios es cierto que sí generaba lo ficheros correctos. Pero no me permite configurarlo indicandome que no tengo permisos para ello, cuando estoy trabajando desde el root.

 Aunque estés trabajando como super usuario, prueba a invocar las órdenes con el comando `sudo` delante. Por ejemplo: `sudo mkdir grupo1`


### Ejercicio 9:

Una vez creados los dos grupos, debemos modificar el fichero `etc/cgconfig.conf`, añadiendo:

	mount { cpu = /cgroup/cpu }

	group system {
	        cpu {
	                cpu.shares="600";
	        }
	}

	group users {
	        cpu {
	                cpu.shares="400";
	        }
	}

### Ejercicio 10:

Actualmente estoy trabajando en una máquina virtual por lo que la sentencia  egrep '^flags.*(vmx|svm)' /proc/cpuinfo no la puedo utilizar, ya que no me mostrará dichas flags.

Inspeccionando cpuinfo, puedo obtener el modelo de mi cpu: Intel(R) Core(TM) i5-2415M CPU @ 2.30GHz

Y las flags:  fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx hypervisor lahf_lm ida arat epb pln pts dtherm tsc_adjust

En el mac, usando la siguiente sentencia sysctl -a | grep machdep.cpu.features, extraeremos las diferentes flags de la cpu.
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX EST TM2 SSSE3 CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC POPCNT AES PCID XSAVE OSXSAVE TSCTMR AVX1.0

Como vemos el procesador realmente incluye y está activada la opción de virtualización.


### Ejercicio 11:

kvm-ok no estaba instalado de serie, en parte por estar trabajando en virtual. Para instalarlo, he usado sudo apt-get install qemu-kvm. Al ejecularlo como cabía esperar, lo que nos devuelve kvm-ok es lo siguiente:
	INFO: Your CPU does not support KVM extensions
	INFO: For more detailed results, you should run this as root
	HINT:   sudo /usr/sbin/kvm-ok


### Ejercicio 12:

Un SaaS o Software as a Service es una aplicación normalmente de escritorio que se lleva a internet, con el objetivo de permitir al usuario deshacerse de tareas tan engorrosas como la instalación, mantenimiento propio, actualización, etc. Así como ofreciendo la gran ventaja de poder acceder a dicha aplicación y al trabajo relacionado con esta en cualquier tipo de dispositivo.

Un gran ejemplo de estos SaaS son las aplicaciones de ofimática en la nube que todas las grandes empresas ya han incorporado como Microsoft office 365, Google Docs, writer y iCloud Pages, Keynote y Numbers de Apple.

Unas de las aplicaciones que me han parecido bastante interesantes dentro de este sector son las aplicaciones web para el desarrollo del software. Son aplicaciones que no uso muy habitualmente pero cuando necesito de ellas no me apetece instalarlas ya que son para un momento, cómo desarrollar un diagrama de flujo o un diagrama UML  para algún ejercicio. Y estas son igual de potentes que las que vayamos a instalar.


- - - - 

##TEMA 2:

### Ejercicio 1: 

Instalación de virtualenv en Mac os x:
	sudo easy_install pip
	sudo pip install virtualenv
Para más dudas seguir los enlaces: [enlace1](http://hackercodex.com/guide/python-development-environment-on-mac-osx/) y [enlace2](http://jamie.curle.io/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/)


### Ejercicio 2:

Me he dado de alta en OpenShift.


### Ejercicio 3:

Mi blog de WordPress instalado en OpenShift se puede encontrar [aquí](https://php-sergiogvzblog.rhcloud.com)


### Ejercicio 4:

Esta función de Google AS nos permite crear un documento nuevo, nombrarlo e introducir texto en el dicho documento. 

```
function crearDocumento() {
  
  //Crear documento
  var doc = DocumentApp.create('Ejercicio 4');

  //Modificar su contenido
  doc.getBody().appendParagraph('Esto es la creción de el documento ejercicio 4 para CC');
  

}
```

### Ejercicio 5:

Los sistemas de automitazación de construcción para lenguajes de programación que he usado anteriormente han sido:

- make para C y C++, haciendo uso de ficheros makefile. Un ejemplo extraido de [cplusplus.com](http://www.cplusplus.com/forum/unices/12499/) es el siguiente:

```
SOURCE=octhecdec.cpp octhecdec.h
MYPROGRAM=octhecdec
MYINCLUDES=/home/scale/g++Projects/gLib/

MYLIBRARIES=fltk
CC=g++



all: $(MYPROGRAM)



$(MYPROGRAM): $(SOURCE)

    $(CC) -I$(MYINCLUDES) $(SOURCE) -o$(MYPROGRAM) -l$(MYLIBRARIES)

clean:

    rm -f $(MYPROGRAM)
```
Como se ve, se pueden generar macros o flags para indicar la instrucción del compilador (CC), los ficheros de códigos (SOURCE),...

Para definir las tareas, se mencionará la tarea, dos puntos y los ficheros o tareas que han de ser completadas antes de proceder con la que se define. A continuación, tabulado, el comando para completar dicha tarea.

- Maven para Java. Se está utilizando actualmente en la asigtura DSS (desarrollo de software basado en componetes) para facilitar la compilación de JSF. Se ha instalado en eclipse y despues se ha definido el proyecto como proyecto Maven. Este se puede descargar y serguir en la web de [Maven](http://maven.apache.org/download.cgi).

- Para el lenguaje Python, existen varios como [PyBuilder](http://pybuilder.github.io) o [Pynt](https://github.com/rags/pynt) que nos ayuda con las dependencias de nuestros programas.

### Ejercicio 6:



### Ejercicio 7:

Actualmente estoy trabajando con python, principalmente para la asignatura con GAE. Para el entorno de pruebas, estamos pensando usar, lanzándolo con integración continua con Shipabble, pruebas de unitarias con el módulo [unittest](https://docs.python.org/2/library/unittest.html). Así también es posible usar [nose](https://nose.readthedocs.org/en/latest/), que nos permite reconocer los diferentes test que hemos implementado, lanzarlos y comprobar sus resultados automáticamente.
