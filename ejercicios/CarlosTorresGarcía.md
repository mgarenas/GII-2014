Ejercicios
======

Tema1
-----

###Ejercicio 1 Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. Consultar este artículo en Infoautónomos sobre el tema. 

	Servidor Dell PowerEdge T110 II: 329€ 
	(http://www.dell.com/es/empresas/p/poweredge-t110-2/pd)

	Para amortizarlo en cuatro años, su coste de amortización es de 6'86€/mes, lo que supone un coste de amortización de 82'25€ al año (un 		25% del precio).

	Para amortizarlo en siete años, su coste de amortización es de 3'92€/mes, 47€ al año, un 14'29% al año.

###Ejercicio 2 Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, Comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo.

	1&1 Servidor VPS
		1 Servidor
		SO CentOS
		7 GB RAM
		HD 200GB
		29'99€/mes
	
	1&1 Servidor Cloud dinámico
		1 Servidor
		SO CentOS
		1 Core		0.01 €/h
		8 GB RAM	0.08 €/h
		HD 200GB	0.02 €/h
		79'20€/mes
		
	
###Ejercicio 3.1 ¿Qué tipo de virtualización usarías en cada caso? Comentar en el foro

-**Alojar varios clientes en un sólo servidor:** A nivel de Sistema Operativo, ya que permite que los todos invitados posean cuentas totalmente independientes unas de otras y, como han comentado mis compañeros, al utilizar el mismo sistema operativo que el anfitrión, éstos pueden despreocuparse de las actualizaciones y demás tareas de administración, las cuales serían llevadas por el administrador.

-**Crear un sistema eficiente de web + middleware + base de datos:** Al igual que DavidGSola, utilizaría una virtualización a nivel de aplicación, dado que considero esencial reducir al máximo el uso de los recursos y, en el caso de una virtualización plena o de sistema operativo, es necesario consumir gran cantidad de recursos.

-**Sistema de prueba de software e integración continua:** Virtualización de entornos para así poder probar el comportamiento del software generado en los distintos entornos que se deseen probar.

###Ejercicio 3.2 Crear un programa simple en cualquier lenguaje interpretado para Linux, empaquetarlo con CDE y probarlo en diferentes distribuciones.
	Instalar CDE: sudo apt-get install cde
	Programa a empaquetar: helloworld.py
		#!/usr/bin/python
		# Hello world python program
		print "Hello World!";
	Para generar el paquete:
	1. Descargar el binario cde de la página http://www.pgbovine.net/cde.html
	2. Se copia en el directorio del script
	3. Se asigna permiso de ejecución para ambos ficheros chmod +x ./*
	4. Se ejecuta ./cde_2011-08-15_64bit ./helloworld.py
	5. Automáticamente se generan el fichero "cde.options" y el directorio "cde-package"
	6. Ejecutar ./cde-package/cde-exec ./helloworld.py desde el directorio que contiene tanto al script como al paquete.
	

###Ejercicio 4.1 Hacer el tutorial de línea de órdenes de docker para comprender cómo funciona.
	Los comandos introducidos fueron:
	docker version
	docker search tutorial
	docker pull learn/tutorial
	docker run learn/tutorial echo "hello world"
	docker run learn/tutorial apt-get install -y ping
	docker commit 698 learn/ping
	docker run learn/ping ping www.google.com
	docker inspect efe
	docker push learn/ping

	![Imagen almacenada en /ejercicios/CarlosTorresGarcíaDocker.png]
###Ejercicio 4.2 Avanzado Instalarlo y crear una aplicación contenedorizada.
	sudo apt-get install docker.io
	

###Ejercicio 5 Instala el sistema de gestión de fuentes git
	sudo apt-get install git

###Ejercicio 6.1 Crear un proyecto y descargárselo con git. Al crearlo se marca la opción de incluir el fichero README.
###Ejercicio 6.2 Modificar el readme y subir el fichero modificado
	*Una vez creado se clona el repositorio: git clone git@github.com:Appsamblea/Appsamblea.git
	*Se edita el fichero
	*Se sube el fichero al repositorio local:
		1. git add README.md
		2. git commit
		3. git push
	*Se hace un pull request
		
###Ejercicio 7 Comprobar si en la instalación hecha se ha instalado cgroups y en qué punto está montado, así como qué contiene.
	Se encuentra en /sys/fs y contiene los siguientes directorios:
	
		blkio  cpuacct  devices  hugetlb  perf_event
		cpu    cpuset   freezer  memory   systemd
	

###Ejercicio 8.1 Crear diferentes grupos de control sobre un sistema operativo Linux. Ejecutar en uno de ellos el navegador, en otro un procesador de textos y en uno último cualquier otro proceso. Comparar el uso de recursos de unos y otros durante un tiempo determinado.
		
	sudo su	
	cd /sys/fs/cgroup
	apt-get install cgroup-bin
	cgcreate -a carlos -g cpuset:grupo1
	cgcreate -a carlos -g cpuset:grupo2
	cgcreate -a carlos -g cpuset:grupo3

	echo 0> cpuset/grupo1/cpuset.mems
	echo 0> cpuset/grupo2/cpuset.mems
	echo 0> cpuset/grupo3/cpuset.mems
	echo 0> cpuset/grupo1/cpuset.cpus
	echo 0> cpuset/grupo2/cpuset.cpus
	echo 0> cpuset/grupo3/cpuset.cpus

	<Incompleto>
	
	
	
###Ejercicio 8.2 Calcular el coste real de uso de recursos de un ordenador teniendo en cuenta sus costes de amortización. Añadir los costes eléctricos correspondientes.



###Ejercicio 9.1 Discutir diferentes escenarios de limitación de uso de recursos o de asignación de los mismos a una u otra CPU.
###Ejercicio 9.2 Implementar usando el fichero de configuración de cgcreate una política que dé menos prioridad a los procesos de usuario que a los procesos del sistema (o viceversa).
- Hay que generar el fichero gconfig.conf en el directorio /etc/ con el siguiente contenido:
```
mount {
	cpu = /cgroup/cpu
}

group usuario {
	cpu {
		cpu.shares="200";
	}
}

group sistema {
	cpu {
		cpu.shares="800";
	}
}
```

###Ejercicio 9.3 Usar un programa que muestre en tiempo real la carga del sistema tal como htopy comprobar los efectos de la migración en tiempo real de una tarea pesada de un procesador a otro (si se tiene dos núcleos en el sistema).



###Ejercicio 9.4 Configurar un servidor para que el servidor web que se ejecute reciba mayor prioridad de entrada/salida que el resto de los usuarios.

###Ejercicio 10.1 Comprobar si el procesador o procesadores instalados tienen estos flags. ¿Qué modelo de procesador es? 
	Intel Core i5 M 430

###Ejercicio 10.2¿Qué aparece como salida de esa orden?
	Aparece el siguiente mensaje repetido 4 veces (uno por cada núcleo del procesador):
	
	flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl vmx 
	est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 popcnt lahf_lm arat dtherm tpr_shadow vnmi flexpriority ept vpid
	
	Únicamente la fila de abajo aparece en color blanco, las otras dos líneas están en color rojo.	

###Ejercicio 11 Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden kvm-ok
	Sí lo tiene. Al ejecutar la orden kvm-ok me da el siguiente mensaje:

	INFO: /dev/kvm exists\n
	KVM acceleration can be used

###Ejercicio 12 Comentar diferentes soluciones de Software as a Service de uso habitual
	Cualquier servidor de correo electrónico es un SaS de uso habitual (hotmail, gmail, yahoo, etc.)
	Las aplicaciones de ofimática incluídas en Google Drive son otro ejemplo de SaS.

Tema 2
-----
###Ejercicio 1 Instalar un entorno virtual para tu lenguaje de programación favorito (uno de los mencionados arriba, obviamente)
- He descargado la última versión de virtualenv (1.9) de https://pypi.python.org/packages/source/v/virtualenv/
- Se descomprime el fichero
- cd virualenv-1.9
- sudo python setup.py install

###Ejercicio 2 Darse de alta en algún servicio PaaS tal como Heroku, Nodejitsu u OpenShift
- Me he dado de alta en Openshift

###Ejercicio 3 Crear una aplicación en OpenShift y dentro de ella instalar WordPress
- Antes de crearla, hice un fork al repositorio https://github.com/openshift/wordpress-example
- El repositorio de la aplicación es: https://github.com/carltorres/wordpress-example
- He generado directamente una aplicación Wordpress 4.0
- La URL de la aplicación es: http:blog-carltorres.rhcloud.com 

###Ejercicio 4 Crear un script para un documento Google y cambiarle el nombre con el que aparece en el menú, así como la función a la que llama


- Se abre un documento cualquiera en Drive -> Herramientas -> Editor de secuencia de comandos
-Sobre el script de Google-Doc:

```
function onOpen() {
  DocumentApp.getUi().createMenu('Pipas')
      .addItem('¿Quieres pipas?', 'quieresPipas')
      .addToUi();
}

function quieresPipas() {
  var result = DocumentApp.getUi().alert(
      'Dialog title',
      '¿Quieres pipas?',
      DocumentApp.getUi().ButtonSet.YES_NO);

  if (result == DocumentApp.getUi().Button.YES) {
    DocumentApp.getUi().alert('¡Pues no tengo!');
  } else {
    DocumentApp.getUi().alert('¡Tampoco te iba a dar!');
  }
}

```
- Una vez terminado -> Guardar -> Publicar
- Se abre un fichero cualquiera que utilice la hoja de cálculo.
- Aparece un menú llamado "Mis programas" en el cual está el ítem "alerta" que muestra un diálogo con un texto.

###Ejercicio 5 Buscar un sistema de automatización de la construcción para el lenguaje de programación y entorno de desarrollo que usemos habitualmente

	Para app engine y Phyton: appcfg

###Ejercicio 6 Identificar, dentro del PaaS elegido o cualquier otro en el que se dé uno de alta, cuál es el fichero de automatización de construcción e indicar qué herramienta usa para la construcción y el proceso que sigue en la misma
	Para Openshift se puede utilizar [Jenkins](https://developers.openshift.com/en/managing-continuous-integration.html)

###Ejercicio 7 Buscar un entorno de pruebas para el lenguaje de programación y entorno de desarrollo que usemos habitualmente
	Shippable


Tema 3
-----

###Ejercicio 1 Crear un espacio de nombres y montar en él una imagen ISO de un CD de forma que no se pueda leer más que desde él. Pista: en ServerFault nos explican como hacerlo, usando el dispositivo loopback
 1. Lo primero que hay que hacer es ser superusuario:
- sudo su
 2. Se crea un directorio en el cual se montará el fichero .iso
- mkdir /mnt/ej1t3cc
 3. Se monta el fichero .iso con la orden "mount" seguida de los siguientes argumentos
- mount -o loop -t iso9660 ubuntu14.04.iso /mnt/ej1t3cc


###Ejercicio 2
#### Mostrar los puentes configurados en el sistema operativo.
 1. Se instala brigde utils
```
sudo apt-get install bridge utils
```
 2. Se muestran los puentes exsitentes con brctl show
```
brctl show
```
```
bridge name	bridge id		STP enabled	interfaces
docker0		8000.000000000000	no
```
#### Crear un interfaz virtual y asignarlo al interfaz de la tarjeta wifi, si se tiene, o del fijo, si no se tiene.
 1. Hay que crear una interfaz virtual con "brctl addbr" siendo superusuario
```
sudo su
brctl addbr interfazvirtual
```
 2. Hay que unirla con eth0
```
brctl addif interfazvirtual eth0
```
 3. Ahora se comprueba si se ha creado la interfaz
```
brctl show
```

```
bridge name	bridge id		STP enabled	interfaces
docker0		8000.000000000000	no
interfazvirtual		8000.705ab6892974	no		eth0

```

###Ejercicio 3
####Usar debootstrap (o herramienta similar en otra distro) para crear un sistema mínimo que se pueda ejecutar más adelante.
####Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.


###Ejercicio 4 Instalar alguna sistema debianita y configurarlo para su uso. Trabajando desde terminal, probar a ejecutar alguna aplicación o instalar las herramientas necesarias para compilar una y ejecutarla.


###Ejercicio 5 Instalar una jaula chroot para ejecutar el servidor web de altas prestaciones nginx

###Ejercicio 6 Crear una jaula y enjaular un usuario usando `jailkit`, que previamente se habrá tenido que instalar.

Tema 4
-----

###Ejercicio 1 Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.

###Ejercicio 2 Comprobar qué interfaces puente se han creado y explicarlos.

###Ejercicio 3 
####Crear y ejecutar un contenedor basado en Debian.

####Crear y ejecutar un contenedor basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya. Fedora, al parecer, tiene problemas si estás en Ubuntu 13.04 o superior, así que en tal caso usa cualquier otra distro.

###Ejercicio 4
####Instalar lxc-webpanel y usarlo para arrancar, parar y visualizar las máquinas virtuales que se tengan instaladas.
####Desde el panel restringir los recursos que pueden usar: CPU shares, CPUs que se pueden usar (en sistemas multinúcleo) o cantidad de memoria.

###Ejercicio 5 Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx.

###Ejercicio 6
####Instalar juju.
####Usándolo, instalar MySQL en un táper.

###Ejercicio 7
####Destruir toda la configuración creada anteriormente
####Volver a crear la máquina anterior y añadirle mediawiki y una relación entre ellos.
####Crear un script en shell para reproducir la configuración usada en las máquinas que hagan falta.

###Ejercicio 8 Instalar libvirt

###Ejercicio 9 Instalar un contenedor usando virt-install

###Ejercicio 10 Instalar docker.
```
sudo apt-get update
sudo apt-get install docker.io
source /etc/bash_completion.d/docker.io
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
```


###Ejercicio 11
####Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.
####Buscar e instalar una imagen que incluya MongoDB

###Ejercicio 12 Crear un usuario propio e instalar nginx en el contenedor creado de esta forma.

###Ejercicio 13 Crear a partir del contenedor anterior una imagen persistente con commit.

###Ejercicio 14 Crear una imagen con las herramientas necesarias para el proyecto de la asignatura sobre un sistema operativo de tu elección.




Seminario Ruby
-----
###Ejercicio 1 Instalar Ruby y usar ruby –version
	ruby 1.9.3p484 (2013-11-22 revision 43786) [x86_64-linux]
	Los paquetes irb, rubygems y rdoc ya se instalaron con el paquete ruby.


###Ejercicio 2 Crear un programa en Ruby que imprima los números desde el 1 hasta otro contenido en una variable
		
	#!/usr/bin/ruby 
	numero = 10 
	i = 1 
	while (i <= 10) 
		puts i 
		i +=1 
	end
	
###Ejercicio 3 ¿Se pueden crear estructuras de datos mixtas en Ruby? Crear un array de hashes de arrays e imprimirlo.

	#!/usr/bin/ruby
	$array = [
	 	{ :a => ["a", "aa"], :b => ["b", "bb"] },

	 	{ :c => ["c", "cc"], :d => ["d", "dd"] }
		]

	$array.each do |item|
		item.each{|key, value| puts value}
	end

