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


##Ejercicio 03
Tipo de virtualización que utilizaría en cada caso y por qué

- Como la mayoría de mis compañeros, para alojar varios clientes en un mismo servidor, la virtualización sería a nivel de sistema operativo. De esta forma, cada cliente es completamente independiente del resto.

- Para un sistema eficiente de web + middleware + base de datos, la virtualización sería plena.  De esta forma, el sistema resultante será más potente y facilitará la ejecución de todas las apliaciones.

- Por último, para un sistema de prueba de software e integración continua, sería una virtualización de entornos de desarrollo ya que esta tipo de virtualización está especialmente preparado para esta tarea.

Para instalar CDE seguir el siguiente [tutorial](http://www.pgbovine.net/cde.html)



##Ejercicio 04
Instrucciones para [descargar e instalar docker](https://docs.docker.com/installation/ubuntulinux/#ubuntu-precise-1204-lts-64-bit)



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
	Para crear un nuevo proyecto o repositorio en gitHub, pinchamos en la pestaña **Create New --> New Repository** al lado de nuestro nombre de usuario. Nos pide un nombre para el proyecto y nos da la opción de inicializarlo con un fichero README.
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

grupo **good** ejecutando firefox, uso de cpu 3161809980
grupo **regular** ejecutando libreoffice, uso de cpu 2969369788
grupo **bad** ejecutando el editor de imágenes gimp, uso de cpu 4422939045

















