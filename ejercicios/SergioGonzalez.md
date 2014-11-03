
Ejercicios de Sergio González
==============================

### Ejercicio 1:

SERVIDOR HP PROLIANT ML350P G8 XEON E5-2609 2.4 GHz 4GB DISCO DURO HDD 2.5" SFF P420I 512MB FBWC 460W CS GOLD

* Precio con IVA: 1744,00€
* Precio sin IVA: 1441,00€

* A cuatro años: 360,25€ anuales.
* A siete años: 205,857 anuales.


### Ejercicio 2:

| Servicio | vCores | HDD (GB) | RAM (GB) | Factura/año ($)   | Factura/h  ($) |
|----------|--------|----------|----------|-------------------|----------------|
|Azure     | 4      | 120      | 7        |     1771.56    	  | 0.1983         |
|Amazon    | 4 	    | 80	   | 7.5      |  	333     	  | 0.186          |
|Google    | 4 	    | -	       | 14       |  	2207.52       | 0.252          |

* Para el 1% del año (3,65 dias, 88 horas):

| Servicio | Precio ($) |
|----------|------------|
|Azure     | 17,45      | 
|Amazon    | 16,368 	|
|Google    | 22,176 	|

* Para el 10% del año (36,5 dias, 88 horas):

| Servicio | Precio ($) |
|----------|------------|
|Azure     | 174,5      | 
|Amazon    | 163,68 	|
|Google    | 221,76 	|


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



### Ejercicio 7:

Mi instalación es un Ubuntu 14.04 y efectivamente se ha instalado cgroups con ella. Se ha montado en /sys/fs/cgroup. Ahí solo encontraremos systemd y dentro:
cgroup.clone_children  cgroup.procs          notify_on_release  tasks
cgroup.event_control   cgroup.sane_behavior  release_agent      user


### Ejercicio 8:

  	sudo su
	cd /sys/fs/cgroup/
    mkdir group1 group2 group3
 
 Cuando realizo esto, no genera los archivos que debería, por lo que añadir los ficheros con el echo no tiene mucho sentido, aun así intentandolo obtengo un error de disco lleno. Probando intenté hacerlo en systemd, ya que pensé que quizás solo podría realizarlo ahí. Al generar los nuevos subdirectorios es cierto que sí generaba lo ficheros correctos. Pero no me permite configurarlo indicandome que no tengo permisos para ello, cuando estoy trabajando desde el root.


### Ejercicio 9:


### Ejercicio 10:

Actualmente estoy trbajando en una máquina virtual por lo que la sentencia  egrep '^flags.*(vmx|svm)' /proc/cpuinfo no la puedo utilizar, ya que no me mostrará dichas flags.

Inspeccionando cpuinfo, puedo obtener el modelo de mi cpu: Intel(R) Core(TM) i5-2415M CPU @ 2.30GHz

Y las flags:  fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx hypervisor lahf_lm ida arat epb pln pts dtherm tsc_adjust

En el mac, usando la siguiente sentencia sysctl -a | grep machdep.cpu.features, extraeremos las diferentes flags de la cpu.
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX EST TM2 SSSE3 CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC POPCNT AES PCID XSAVE OSXSAVE TSCTMR AVX1.0

Como vemos el procesador realmente incluye y está activada la opción de virtualización.


### Ejercicio 11:


### Ejercicio 12:




