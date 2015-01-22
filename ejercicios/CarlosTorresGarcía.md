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
	

###Ejercicio 8.1 Crear diferentes grupos de control sobre un sistema operativo Linux. Ejecutar en uno de ellos el navegador, en otro un procesador #antiPostureode textos y en uno último cualquier otro proceso. Comparar el uso de recursos de unos y otros durante un tiempo determinado.
		
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

	gedit &
	firefox &
	libreoffice &
	
	
	
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
```
sudo su
```
 2. Se crea un directorio en el cual se montará el fichero .iso
```
mkdir /mnt/ej1t3cc
```
 3. Se monta el fichero .iso con la orden "mount" seguida de los siguientes argumentos
```
mount -o loop -t iso9660 ubuntu14.04.iso /mnt/ej1t3cc
```

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

 1. debootstrap ya viene instalado en Ubuntu 14.04
 2. Se crea un directorio donde se instalará es SO
 ```
 sudo mkdir ubuntu
 ```
 3. Se instala la versión en el directorio que se ha creado (en este caso he instalado Ubuntu 14.04 con 64 bits)
 ```
 sudo debootstrap  --arch=amd64 trusty ./ubuntu http://archive.ubuntu.com/ubuntu/
 ```
####Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.
 1. Se instala rinse
 ```
 sudo apt-get install rinse
 ```
 2. Al igual que en el caso anterior, se crea un directorio donde se instalará nuestro SO
 ```
 sudo mkdir opensuse
 ```
 3. Se instala la versión del SO (la última versión de opensuse que permite instalar Rinse es la 11.1 aunque actualmente existe hasta la 13.2)
 ```
 sudo rinse --arch amd64 --distribution opensuse-11.1 --directory ./opensuse
 ``` 

###Ejercicio 4 Instalar alguna sistema debianita y configurarlo para su uso. Trabajando desde terminal, probar a ejecutar alguna aplicación o instalar las herramientas necesarias para compilar una y ejecutarla.
 He decidido utilizar la versión de Ubuntu instalada en el ejercicio anterior sobre la que he instalado "g++" y "nano" para crear y compilar
 un programa en C++. 
 ```
 sudo su
 chroot /home/carlos/ubuntu
 apt-get install g++
 apt-get install nano
 g++ -o hola hola.cpp
 ./hola
 ```
 Funciona perfectamente.

###Ejercicio 5 Instalar una jaula chroot para ejecutar el servidor web de altas prestaciones nginx
 Voy a utilizar la jaula ya creada en el ejercicio 3 que contiene Ubuntu 14.04:
 1. Accedemos a la jaula
 ```
 sudo su
 chroot /home/carlos/ubuntu
 ```
 2. Actualizamos el repositorio
 ```
 apt-get update
 ```
 3. Instalamos las dependencias necesarias
 ```
 apt-get install build-essential libssl-dev libpcre3-dev wget
 ```
 4. Descargamos la última versión disponible (1.7.9-diciembre de 2014) y la descomprimimos
 ```
 wget http://nginx.org/download/nginx-1.7.9.tar.gz
 tar xzvf nginx-1.7.9.tar.gz
 ```
 5. Antes de compilar lo ideal sería cambiar valores del código fuente como medida de seguridad pero, dado que no voy a utilizar el servidor web,
 omito este paso.

 6. Compilamos
 ```
 ./configure
 make -j 4 && make install
 ```
 7. Descargamos un script que nos permite iniciar, detener, reiniciar y recargar nginx mediante el comando service.
 ```
 wget https://raw.github.com/JasonGiedymin/nginx-init-ubuntu/master/nginx
 ```
 8. Copiamos el script a /etc/init.d y le damos permiso de ejecución
 ```
 mv nginx /etc/init.d/nginx
 chmod +x /etc/init.d/nginx
 ```
 9. Ejecutamos el servicio
 ```
 service nginx start
 ```
 10. Verificamos que todo ha salido bien accediendo desde cualquier a localhost.

###Ejercicio 6 Crear una jaula y enjaular un usuario usando `jailkit`, que previamente se habrá tenido que instalar.
 1. Lo primero que hay que hacer es instalar jailkit. Para ello:
 - Instalamos las dependencias
 ```
 sudo su
 apt-get install build-essential debhelper autoconf automake libtool flex bison binutils-gold
 ```
 - Descargamos la versión más reciente de jailkit (2.17) y descomprimimos
 ```
 wget http://olivier.sessink.nl/jailkit/jailkit-2.17.tar.gz
 tar -vxzf jailkit-2.17.tar.gz
 ```
 - Compilamos
 ```
 cd jailkit-2.17
 ./debian/rules binary
 ```
 - Instalamos el DEB generado
 ```
 cd ..
 dpkg -i jailkit_2.17-1_amd64.deb
 ```
 2. Creamos la jaula
 ```
 mkdir -p /seguro/jaulas/jaula1
 chown -R root:root /seguro
 jk_init -v -j /seguro/jaulas/jaula1 jk_lsh basicshell netutils editors 
 ```
 3. Se crea el usuario y se enjaula en la jaula
 ```
 useradd usuarionormal
 passwd usuarionormal
 jk_jailuser -m -j /seguro/jaulas/jaula1 usuarionormal
 ```

Tema 4
-----

###Ejercicio 1 Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.
1. Instalamos lxc
```
sudo apt-get install lxc
```
2. Comprobamos que nuestro equipo está preparado para utilizar contenedores
```
lxc-checkconfig
```

###Ejercicio 2 Comprobar qué interfaces puente se han creado y explicarlos.
Para comprobar las interfaces que existen actualmente en el sistema basta con utilizar el comando "ifconfig".
La salida es la siguiente:
```
docker0   Link encap:Ethernet  direcciónHW ea:7d:75:72:b8:9a  
          Direc. inet:172.17.42.1  Difus.:0.0.0.0  Másc:255.255.0.0
          Dirección inet6: fe80::e87d:75ff:fe72:b89a/64 Alcance:Enlace
          ACTIVO DIFUSIÓN FUNCIONANDO MULTICAST  MTU:1500  Métrica:1
          Paquetes RX:0 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:52 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:0 
          Bytes RX:0 (0.0 B)  TX bytes:7934 (7.9 KB)

eth0      Link encap:Ethernet  direcciónHW 70:5a:b6:89:29:74  
          ACTIVO DIFUSIÓN MULTICAST  MTU:1500  Métrica:1
          Paquetes RX:0 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:0 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:1000 
          Bytes RX:0 (0.0 B)  TX bytes:0 (0.0 B)

lo        Link encap:Bucle local  
          Direc. inet:127.0.0.1  Másc:255.0.0.0
          Dirección inet6: ::1/128 Alcance:Anfitrión
          ACTIVO BUCLE FUNCIONANDO  MTU:65536  Métrica:1
          Paquetes RX:416 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:416 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:0 
          Bytes RX:39981 (39.9 KB)  TX bytes:39981 (39.9 KB)

lxcbr0    Link encap:Ethernet  direcciónHW 1a:03:c0:77:c8:39  
          Direc. inet:10.0.3.1  Difus.:10.0.3.255  Másc:255.255.255.0
          Dirección inet6: fe80::1803:c0ff:fe77:c839/64 Alcance:Enlace
          ACTIVO DIFUSIÓN FUNCIONANDO MULTICAST  MTU:1500  Métrica:1
          Paquetes RX:0 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:58 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:0 
          Bytes RX:0 (0.0 B)  TX bytes:9173 (9.1 KB)

wlan0     Link encap:Ethernet  direcciónHW 70:f1:a1:48:be:ed  
          Direc. inet:192.168.1.101  Difus.:192.168.1.255  Másc:255.255.255.0
          Dirección inet6: fe80::72f1:a1ff:fe48:beed/64 Alcance:Enlace
          ACTIVO DIFUSIÓN FUNCIONANDO MULTICAST  MTU:1500  Métrica:1
          Paquetes RX:9831 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:6511 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:1000 
          Bytes RX:6275520 (6.2 MB)  TX bytes:1328958 (1.3 MB)

```
Como se puede comprobar, la interfaz que se ha creado al instalar lxc ha sido lxcbr0 la cual es una interfaz puente para trabajar con jaulas.

###Ejercicio 3 
####Crear y ejecutar un contenedor basado en Debian.
1. Pasamos a superusuario
```
sudo su
```
2. Creamos el contenedor basado en Debian
```
lxc-create -t ubuntu -n ubuntuContenedor
```
3. Ejecutamos el contenedor
```
sudo lxc-start -n ubuntuContenedor
```

####Crear y ejecutar un contenedor basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya. Fedora, al parecer, tiene problemas si estás en Ubuntu 13.04 o superior, así que en tal caso usa cualquier otra distro.
1. Pasamos a superusuario
```
sudo su
```
2. Creamos un contenedor basado en Redhat (opensusue)
```
lxc-create -t fedora -n fedoraContenedor
```
3. Ejecutamos el contenedor
```
sudo lxc-start -n fedoraContenedor
```

###Ejercicio 4
####Instalar lxc-webpanel y usarlo para arrancar, parar y visualizar las máquinas virtuales que se tengan instaladas.
1. Pasamos a superusuario
```
sudo su
```
2. Descargamos el script que instala lxc-webpanel y lo ejecutamos
```
wget http://lxc-webpanel.github.com/tools/install.sh -O - | bash
```
3. Abrimos un navegador y vamos a localhost:5000. Tanto para nombre de usuario como para contraseña utilizamos "admin".
####Desde el panel restringir los recursos que pueden usar: CPU shares, CPUs que se pueden usar (en sistemas multinúcleo) o cantidad de memoria.
 1. Abrimos lxc-webpanel tal accediendo desde un navegador a localhost:5000 y usando "admin" como usuario y contraseña.
 2. Se selecciona el contenedor a limitar.
 3. Se especifican las limitaciones.
 4. Se pulsa sobre el botón verde "Apply".

###Ejercicio 5 Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx.

###Ejercicio 6
####Instalar juju.
1. Pasamos a superusuario
```
sudo su
```
2. Tal y como se indica en la página de la asignatura, añadimos y actualizamos el repositorio e instalamos juju
```
add-apt-repository ppa:juju/stable
apt-get update && apt-get install juju-core
```
####Usándolo, instalar MySQL en un táper.
1. Dejamos de ser superusuario
```
exit
```
2. Accedemos a /.juju/environments.yaml y sustituimos la línea "default:amazon" por "default:local"
3. Instalamos MongoDB
```
apt-get install mongodb-server
```
4. Instalamos juju-local
```
apt-get install juju-local
```
5. Creamos el táper
```
juju bootstrap
```
6. Desplegamos MySQL
```
juju deploy mysql
```
###Ejercicio 7
####Destruir toda la configuración creada anteriormente
Lo más rápido es destruir el entorno completo
```
sudo juju destroy-environment local
```
####Volver a crear la máquina anterior y añadirle mediawiki y una relación entre ellos.
Creamos el táper y desplegamos mediawiki y MySQL y especificamos su relación (ya que mediawiki utiliza MySQL)
```
juju bootstrap
juju deploy mysql
juju deploy mediawiki
juju add-relation mediawiki:db mysql
juju expose mediawiki
```
####Crear un script en shell para reproducir la configuración usada en las máquinas que hagan falta.

###Ejercicio 8 Instalar libvirt
1. Pasamos a superusuario
```
sudo su
```
2. Instalamos libvirt tal y como se indica en su página
```
apt-get install kvm libvirt-bin
```
3. Si el usuario que utilizamos habitualmente  no forma parte del grupo "libvirt", lo añadimos
```
adduser carlos libvirtd
```
###Ejercicio 9 Instalar un contenedor usando virt-install
1. Pasamos a superusuario
```
sudo su
```
2. Instalamos virtinst y virt-viewer
```
apt-get install virtinst virt-viewer
```
3. Creamos el directorio donde se instalará el contenedor
```
mkdir /vir
```
3. Instalamos con virt-install una ISO que hemos descargado previamente (el contenedor ocupará 5GB)
```
virt-install -r 1024 --accelerate -n LinuxMint17 --disk /virt/mint17_64.img,size=5 --cdrom linuxmint17.1_64.is
```
###Ejercicio 10 Instalar docker.
1. Pasamos a superusuario
```
sudo su
```
2. Actualizamos el repositorio
```
apt-get update
```
3. Instalamos y configuramos Docker
```
apt-get install docker.io
source /etc/bash_completion.d/docker.io
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
```
###Ejercicio 11
####Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.
1. Pasamos a superusuario
```
sudo su
```
2. Buscamos las versiones de centos que se encuentran disponibles en el repositorio de docker
```
docker search centos
```
3. Instalamos la versión que consideremos más oportuna (la última)
```
docker pull centos
```
####Buscar e instalar una imagen que incluya MongoDB
1. Pasamos a superusuario
```
sudo su
```
2. Instalamos alguna imagen que incluya MongoBD
```
docker pull dockerfile/mongodb
```


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

