Ejercicios de Álvaro Muñoz
============================

TEMA 1
======

***
### Ejercicio 1

Según la [tabla de amortizaciones simplificada](http://www.infoautonomos.com/informacion-al-dia/fiscalidad/gastos-deducibles-autonomos-irpf-estimacion-directa/) la amortización anual no puede superar el 26% de la base imponible.

El servidor elegido ha sido un [HP ProLiant ML310e G8 XE E3-1220/8GB/2TB](http://www.pccomponentes.com/hp_proliant_ml310e_g8_xe_e3_1220_8gb_2tb.html), cuyo precio sin IVA es de **532.23€**

* Coste amortización a 4 años:
	* Cuatro años al 25%: 532.23€ x 0.25 = 133.06€/año 

* Coste amortización a 7 años
	* Cuatro años al 10% (2 primeros y 2 últimos): 532.23 x 0.1 = 53.23€/año
	* Cuatro años al 20% (los restantes): 532.23 x 0.2 = 106.46€/año

***
### Ejercicio 2

| Máquina/Modelo | vCores | HDD (GB) | RAM (GB) | Factura/año (€) | Factura/hora (€) |
|----------------|--------|----------|----------|-------------------|------------|
|[OVH VPS Cloud 2](https://www.ovh.es/vps/vps-cloud.xml) | 4      |      50  | 6        | 		232.2	    |  0.21 	 |
|[Amazon c3.xlarge](http://aws.amazon.com/es/ec2/pricing/)| 4 	  | 80	     | 7.5      |  	1454.5104   	| 0.166040   |

- Uso del 1% (entre 3 y 4 días al año):
	- OVH VPS Cloud 2: 18.40 €
	- Amazon c3.xlarge: 14.54 €

- Uso del 10% (entre 36 y 37 días al año):
	- OVH VPS Cloud 2: 184 €
	- Amazon c3.xlarge: 145 €

*Nota: la conversión entre $ y € se hizo el día 23/10/2014 con 0.21USD = 0.166040EUR*
*Aclaración: el servidor escogido de OVH es de tipo VPS, dedicado, que se paga con mensualidades, que es la comparación que el ejercicio pedía.*

***
### Ejercicio 3.1

Lo comentado en el foro ha sido:

- **Alojar varios clientes en un sólo servidor**: para este caso tan común usaría *virtualización a nivel de SO*. De hecho, es la técnica que usan los llamados [VPS](http://es.wikipedia.org/wiki/Servidor_virtual_privado), ya que permite que los usuarios accedan al servidor con la sensación de que disponen de sus recursos de forma íntegra.

- **Crear un sistema eficiente de web + middleware + base de datos**: como se ha comentado anteriormente, en este caso usaría una *virtualización plena*, ya que uno de los requisitos del sistema es la eficiencia. Además, queda descartada la virtualización a nivel de SO debido a que no podemos arriesgarnos a que otros usuarios nos agoten sin recursos.

- **Sistema de software e integración continua**: coincido con el resto y diría que lo más adecuado es una *virtualización de entorno de desarrollo*, debido a las ventajas que esta técnica presenta (como la posibilidad de probar una aplicación en diferentes versiones).


### Ejercicio 3.2

El script (en *bash*) ha sido el siguiente:

	#!usr/bin/bash
	echo "Adios mundo!"

Los pasos seguidos para *enjaularlo* han sido:

1. Descargar el binario desde la página de CDE.
2. Renombrarlo a *cde* y colocarlo junto a nuestro script
3. Darle permisos de ejecución con `chmod +x cde` (tanto a cde como a nuestro script)
4. Ejecutar `./cde ./script`

Se creará una estructura de directorios denominada **cde-package**. Para ejecutar nuestro script en cualquier plataforma de forma *enjaulada*, debemos invocar el binario **cde-exec** y la ruta relativa a nuestro script (`cde-package/cde-root/home/user/script/`).

***
### Ejercicio 4

Los comandos introducidos durante el tutorial han sido:

	docker version
	docker search tutorial
	docker pull learn/tutorial
	docker run learn/tutorial echo "hello world"
	docker run learn/tutorial apt-get install -y ping
	docker commit 698 learn/ping
	docker run learn/ping ping www.google.com
	docker inspect efe
	docker push learn/ping

***
### Ejercicio 5

Bastaría con ejecutar `apt-get install git`.

***
### Ejercicios 6.1 y 6.2

1. Crear un nuevo repositorio desde nuestro perfil de *GitHub* a través de la web
2. Ejecutar el comando `git clone https://github.com/usuario/repositorio`, donde *usuario* es el nombre de nuestro usuario de *GitHub* y *repositorio* el nombre del proyecto. Se creará una carpeta con el nombre del proyecto en el directorio de trabajo actual
3. Acceder a la carpeta creada y modificar el archivo *README.md*
4. Ejecutar `git commit -m "Modificado README.md"`
5. Ejecutar `git push`


***
### Ejercicio 7

En *Fedora release 19* viene instalado por defecto en */sys/fs/cgroup/*. El contenido del directorio contiene:

	drwxr-xr-x. 2 root root  0 oct 23 21:42 blkio
	lrwxrwxrwx. 1 root root 11 oct 23 21:42 cpu -> cpu,cpuacct
	lrwxrwxrwx. 1 root root 11 oct 23 21:42 cpuacct -> cpu,cpuacct
	drwxr-xr-x. 3 root root  0 oct 23 21:42 cpu,cpuacct
	drwxr-xr-x. 2 root root  0 oct 23 21:42 cpuset
	drwxr-xr-x. 2 root root  0 oct 23 21:42 devices
	drwxr-xr-x. 2 root root  0 oct 23 21:42 freezer
	drwxr-xr-x. 2 root root  0 oct 23 21:42 hugetlb
	drwxr-xr-x. 2 root root  0 oct 23 21:42 memory
	drwxr-xr-x. 2 root root  0 oct 23 21:42 net_cls
	drwxr-xr-x. 2 root root  0 oct 23 21:42 perf_event
	drwxr-xr-x. 5 root root  0 oct 23 21:42 systemd


***
### Ejercicio 8.1

1. Para cada grupo de control debemos crear una carpeta en el directorio `/sys/fs/cgroup`
2. Les asignamos CPUs y memoria por defecto con los comandos `echo 0 > cpuset.cpus` y `echo 0 > cpuset.mems`
3. En cada grupo de control (carpetas anteriormente creadas) hacemos un `echo xxx > tasks`, donde *xxx* es el *PID* del proceso que queremos asignar. De esta forma el proceso cuyo *PID* es *xxx* quedará asignado a ese *cgroup*.

Para ver cualquier información sobre el uso de cada *cgroup* podemos mostrar los ficheros que empiecen por *cpuacct*. Por ejemplo, el archivo *cpuacct.usage* mostrará el uso de CPU del grupo de control en el que se encuentre.


### Ejercicio 8.2


***
### Ejercicio 9.1

El enlace no funciona.


### Ejercicio 9.2

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


### Ejercicio 9.3

Durante la migración de procesos livianos no se nota gran variabilidad en cuanto al uso de las CPU. La migración de procesos más contundentes se observa en el aumento de uso de la CPU.


### Ejercicio 9.4

Similar al ejercicio 9.2 pero cambiando el nombre del recurso al que le damos prioridad:

	mount { blkio = /cgroup/blkio }

	group httpd { 
		blkio { 
			blkio.weight="700"; 
		} 
	}

	group users { 
		blkio { 
			blkio.weight="300"; 
		} 
	}

***
### Ejercicio 10

El procesador sí tiene activados los flags de virtualización a nivel de hardware (flag *vmx*). 
El modelo de procesador es *Intel(R) Core(TM) i7-3930K CPU @ 3.20GHz* (información extraída del archivo */proc/cpuinfo*).
La salida del comando (por cada núcleo) es:

	flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov
	pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb 
	rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology 
	nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est 
	tm2 ssse3 cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic popcnt 
	tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dtherm 
	tpr_shadow vnmi flexpriority ept vpid


***
### Ejercicio 11

El paquete **kvm-ok** no existe en *Fedora* pero el archivo */dev/kvm* existe, por lo que el núclo del *kernel* actual sí contiene el módulo KVM.


***
### Ejercicio 12

Lo comentado en el foro ha sido:

Los sistemas [SaaS](http://es.wikipedia.org/wiki/Software_como_servicio), como Gmail, Google Docs, Google Calendar, [www.imedicplus.com](http://www.imedicplus.com), Salesforce o Basecamp son un modelo de distribución de software donde una empresa sirve el mantenimiento, soporte y operación que usará el cliente durante el tiempo que haya contratado el servicio. Algunas de sus ventajas son:

- Se puede pagar por cuota de uso, no por acceso.
- El cliente suele acceder mediante un navegador web, por lo que suelen ser servicios multiplataforma.
- La actualización de los productos corre por cuenta de la empresa, siendo totalmente transparente al usuario.

Algunos inconvenientes podrían ser:

- Necesidad de conexión a Internet.
- Posible exposición de datos sensibles por accesos indebidos de terceros (políticas de seguridad pobres).
- Necesidad de confianza en la empresa, ya que tienen la posibilidad de usar los datos del usuario.


TEMA 2 
======

* * *
### Ejercicio 1

* * *
### Ejercicio 2

* * *
### Ejercicio 3

* * *
### Ejercicio 4

* * *
### Ejercicio 5

* * *
### Ejercicio 6

* * *
### Ejercicio 7


