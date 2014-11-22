#Sesion del 17 de Octubre

##Ejercicio 01

El Servidor escogido para el coste de amortización se puede encontrar en la siguiente url[Servidor](http://www.dynos.es/servidor-hp-proliant-ml350p-g8-xeon-e5-2609-2.4-ghz-4gb-disco-duro-hdd-2.5-sff-p420i-512mb-fbwc-460w-cs-gold--887111139054__470065-666.html)

1441,32 es el precio del Servidor sin iva.

La amortización a cuatro años es: 360,33€ por año
La amortización a siete años es: 205,90€ por año

##Ejercicio 2

Los servicios escogidos son el A4 de Azure y el Permonce L de 1&1.

El precio por hora de azure es 0,5362.

El precio con un uso del 1% del servicio de Azure es: 47€
Por tanto el precio con un uso del 10% es: 470€

El precio por mes de 1&1 es de 79,99€/mes por lo que serían unos 960€ al año.


##Ejercicio 3

**Comentario Foro**

* Al igual que el resto pienso que para alojar varios clientes en un servidor, lo mas adecuado sería la utilización de una virtualización a nivel de sistema operativo. De esta manera el administrador solo se encarga de las tareas de administración dejando al resto de los usuarios fuera de esta labor y centrandose en el uso que le quieran dar.

* Para crear un sistema eficiente de web + middleware + base de datos, utilizaría una virtualización plena ya que de esta manera tendríamos un sistema mas potente que nos permitiría poder realizar las tareas de una manera mas rápida y eficiente.

* Para un sistema de prueba de software e integración continua utilizaría la virtualización de entornos de desarrollo, de esta manera podríamos probar en diferentes versiones de una manera rápida y fácil

**Empaquetado con CDE**

Para poder realizara el ejercicio se siguio el siguiente [tutorial](http://terminus.ignaciocano.com/k/2012/06/11/cde-creando-aplicaciones-portables-en-gnulinux/) pero usando el programa gedit.

##Ejercicio 4
Realizado el tutorial indicado.

##Ejercicio 5
Git instalado **git version 1.9.1**

##Ejercicio 6
 Ejercicio Realizado.

##Ejercicio 7
jorge@jorge-MacBookPro:/sys/fs/cgroup$ ls
blkio  cpuacct  devices  hugetlb  perf_event
cpu    cpuset   freezer  memory   systemd

##Ejercicio 8
**Ejercicio8.1**
Se han creado tres grupos:
	- **Buenos:** ejecutarán el navegador. (cpu usage:323429397 )
	- **Regulares:** ejecutarán el gimp. (cpu usage:129458 )
	- **Malos:** ejecutarán gedit. (cpu usage: 304051)

##Ejercicio 9
No se ha realizado por ahora.

### Ejercicio 9.2

Para realizar el ejercicio se debe de crear un archivo llamado /etc/cgconfig.conf donde se debe escribir lo siguiente :

mount {
	cpu = /cgroup/cpu
}

group usuario {
	cpu {
		cpu.shares="600";
	}
}

group sistema {
	cpu {
		cpu.shares="400";
	}
}

##Ejercicio 9.4

mount {
	blkio = /cgroup/blkio
}

group servidor {
	blkio {
		blkio.weight="600";
	}
}

group other {
	blkio {
		blkio.weight="400";
	}
}

##Ejercicio 10
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm sse4_1 xsave lahf_lm dtherm tpr_shadow vnmi flexpriority
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe nx lm constant_tsc arch_perfmon pebs bts aperfmperf pni dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm sse4_1 xsave lahf_lm dtherm tpr_shadow vnmi flexpriority

El modelo de procesador es un **Intel® Core™2 Duo CPU P8700 @ 2.53GHz × 2**.

##Ejercicio 11
El programa «kvm» no está instalado. Puede instalarlo escribiendo:
sudo apt-get install qemu-kvm

##Ejercicio 12
Las aplicaciones que se ejecutan en servidores remotos son Saas. Un ejemplo de estos son el WebMail de gmail o Google Docs. La principal ventaje que tiene este tipo de servicio es que puedes acceder a este desde cualquier punto siempre que tengas acceso a internet. De esta manera se ahorran costes y tiempos de instalación. Sin embargo tienen una gran desventaje y es el tema de la seguridad, ya que la información se encuentra alojada en un servidor remoto al que las compañias tienen acceso, si lo desean, y pueden observar lo que haces. Además estos servicios suelen ser atacados muy a menudo por hackers para intentar obtener información de los usuarios.

#Tema 2

#Sesion del 7 de Noviembre

##Ejercicio 1

jorge@jorge-MacBookPro:~/Escritorio$ sudo pip install virtualenv
Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/local/lib/python2.7/dist-packages
Cleaning up...

#Sesion del 10 de Noviembre

##Ejercicio 2
Registrado en OpenShift

##Ejercicio 3
php-jorgeles.rhcloud.com

##Ejercicio 4

[Enlace](https://script.google.com/d/1IKzOI9_kknCZkqV5QqBuOaPlqFLDsJtZfTnPqrEAe5L2Yuo_ht3FrSqa/edit?usp=sharing) que redirige al archivo script que está en Drive

##Ejercicio 5

Make para la compilación de programas en C/C++. Este nos permite contruir de una manera muy automática nuestro programa en C/C++ y disponer los archivos del programa donde queramos.
 
##Ejercicio 6


##Ejercicio 7
Este plugin permite realizar pruebas funcionalidades a aplicaciones web.
[Automatizacion Selenium IDE + Python](http://www.taringa.net/posts/info/14190878/Automatizacion-Selenium-IDE-Python.html)









