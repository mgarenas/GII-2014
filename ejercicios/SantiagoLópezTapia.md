Ejercicios
============================
###==================================================================================================
#Tema 1
###==================================================================================================
### 1)
Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. Consultar [este artículo en Infoautónomos sobre el tema](http://www.infoautonomos.com/consultas-a-la-comunidad/988/).

[Servidor](http://qloudea.com/catalog/product/view/id/2481?gclid=CK2Y3ca6u8ECFYzHtAodnl0A2A)
	
Modelo: N2800
Servidor NAS de 2 discos duros, dotado con un CPU Intel Atom D2700,2 GB de RAM DDR3, específico para entornos de trabajo de oficina.
	
Precio: 385,86 € IVA incluido. Sin IVA: 318,89€

(Suponiendo que se compra al inicio del año fiscal).

* Amortización en 4 años (25% del valor cada año):
   1. 79,72€
   2. 79,72€
   3. 79,72€
   4. 79,73€

* Amortización en 6 años (16,66% del valor cada año salvo el 6º, que es el 16,68%):
   1. 53,14€
   2. 53,14€
   3. 53,14€
   4. 53,14€
   5. 53,14€
   6. 53,19€

###==================================================================================================
### 2)
Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, Comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo.

*   Transferencia: 10 TB mes.

* 	Servidor dedicado:
   * 	Proveedor: CDMon.
   * 	[Página](https://www.cdmon.com/cas/servidores/administrados/)

   * 	Características:
       * CPU: AMD Opteron 2378. 4 núcleos.
       * RAM: 4GB
       * Disco: 1TB
       * Precio: 195,00 €/mes. 2340,00 €/año.

* Servidor virtual:
	* Proveedor: Acens.
	* [Página](https://www.acens.com/cloud/cloud-servers/precios/)

	* Características:
		* CPU: 2Ghz Xeon. 4 núcleos.
		* RAM: 4GB
		* Disco: 1TB
		
	* Precio: 0.66 €/hora.
		* 1% de uso: 57,816 €/año.
		* 10% de uso: 578,16 €/año.

###==================================================================================================
### 3)
1. 	[¿Qué tipo de virtualización usarías en cada caso? Comentar en el foro](https://github.com/JJ/GII-2014/issues/71).
Ya comentado.

2. 	Crear un programa simple en cualquier lenguaje interpretado para Linux, empaquetarlo con CDE y probarlo en diferentes distribuciones.
	
	He empaquetado un pequeño programa en python para hacer un Histogram Equalization.

	* 	Código: 

		```python
			# -*- coding: utf-8 -*-``
			import cv2

			#Read image
			src = cv2.imread("./lena.jpg", 0)
		
			#Apply Histogram Equalization
			dst = cv2.equalizeHist(src)

			#Display results
			source_window = "Source image"
			equalized_window = "Equalized Image"

			cv2.namedWindow(source_window, cv2.WINDOW_AUTOSIZE)
			cv2.namedWindow(equalized_window, cv2.WINDOW_AUTOSIZE)

			cv2.imshow(source_window, src)
			cv2.imshow(equalized_window, dst)

			#Wait until user exits the program
			cv2.waitKey(0)
			cv2.destroyWindow(source_window)
			cv2.destroyWindow(equalized_window)
		```

	* 	Comandos:
	
		* Empaquetar:
			./cde python tutoCC.py

		* Ejecutar:
			./cde-package/cde-exec python tutoCC.py

###==================================================================================================
### 4)

Hacer el [tutorial de línea de órdenes de docker](https://www.docker.com/tryit/) para comprender cómo funciona.

0. 
```
docker
docker version
```
1. ``docker search tutorial``
2. ``docker pull learn/tutorial``
3. ``docker run learn/tutorial echo hello world``
4. ``docker run learn/tutorial apt-get install -y ping``
5. 
```
docker ps -l
docker commit 6982a9948422 /learn/ping
```
6. ``docker run learn/ping ping www.google.com``
7. 
```
docker ps
docker inspect efefdc74a1d5
```
8. 
```
docker images
docker push learn/ping
```

```
              _ _       _                    _
__      _____| | |   __| | ___  _ __   ___  | |
\ \ /\ / / _ \ | |  / _` |/ _ \| '_ \ / _ \ | |
 \ V  V /  __/ | | | (_| | (_) | | | |  __/ |_|
  \_/\_/ \___|_|_|  \__,_|\___/|_| |_|\___| (_)
                                              
 
 
 
                        ##        .
                  ## ## ##       ==
               ## ## ## ##      ===
           /""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
           \______ o          __/
             \    \        __/
              \____\______/
 
              |          |
           __ |  __   __ | _  __   _
          /  \| /  \ /   |/  / _\ |
          \__/| \__/ \__ |\_ \__  |
 
``` 

Avanzado Instalarlo y crear una aplicación contenedorizada

```
silt@silt-Lenovo-Z50-70:~$ sudo docker run -i -t ubuntu /bin/bash
Unable to find image 'ubuntu' locally
ubuntu:latest: The image you are pulling has been verified sistema de gestión de fuentes git
sudo apt-get update
sudo apt-get
511136ea3c5a: Pull complete 
d497ad3926c8: Pull complete 
ccb62158e970: Pull complete 
e791be0477f2: Pull complete 
3680052c0f5c: Pull complete 
22093c35d77b: Pull complete 
5506de2b643b: Pull complete 
Status: Downloaded newer image for ubuntu:latest
root@9d1834f0e2cc:/# 
```

###==================================================================================================	
### 5)

Instala el sistema de gestión de fuentes git

```
sudo apt-get update
sudo apt-get install git	
```

###==================================================================================================
### 6)
1. Crear un proyecto y descargárselo con git. Al crearlo se marca la opción de incluir el fichero README.
```
git init
git remote add CC https://github.com/silt99/CC
git pull CC master
git status
```
2. Modificar el readme y subir el fichero modificado.
```
git add README.md
git config --global user.email "sltapia@gmail.com"
git config --global user.name "silt99"
git commit -m "Trying  how this works"
git push CC master
```

###==================================================================================================
### 7)
Comprobar si en la instalación hecha se ha instalado cgroups y en qué punto está montado, así como qué contiene.
```
ls /sys/fs/cgroup
	
blkio  cpuacct  devices  hugetlb  perf_event
cpu    cpuset   freezer  memory   systemd
```

###==================================================================================================
### 8)
1. Crear diferentes grupos de control sobre un sistema operativo Linux. Ejecutar en uno de ellos el navegador, en otro un procesador de textos y en uno último cualquier otro proceso. Comparar el uso de recursos de unos y otros durante un tiempo determinado.

```
sudo su
cd /sys/fs/cgroup/cpuset

#Crear los grupos
cgcreate -g cpu,cpuset,cpuacct:/malos
cgcreate -g cpu,cpuset,cpuacct:/regulares
cgcreate -g cpu,cpuset,cpuacct:/buenos

#Asignarles recursos
echo 0 > ./malos/cpuset.cpus
echo 0 > ./malos/cpuset.mems
echo 1 > ./regulares/cpuset.cpus
echo 0 > ./regulares/cpuset.mems
echo 2-3 > ./buenos/cpuset.cpus
echo 0 > ./buenos/cpuset.mems

#Lanzar los programas
gedit &
firefox &
spyder &

#Gedit
echo 3258 > ./malos/tasks
#Firefox
echo 3304 > ./regulares/tasks
#Spyder
echo 3376 > ./buenos/tasks

#Comprobar el uso de recursos
cat ./malos/cpuacct.usage
10751854
	
cat ./regulares/cpuacct.usage
7580394

cat ./buenos/cpuacct.usage
263514072
```

2. Calcular el coste real de uso de recursos de un ordenador teniendo en cuenta sus costes de amortización. Añadir los costes eléctricos correspondientes.

No se como hacerlo.

###==================================================================================================
### 9)
1. [Discutir diferentes escenarios de limitación de uso de recursos o de asignación de los mismos a una u otra CPU](https://github.com/IV-GII/GII-2014/issues/4). 
	* 	El enlace está roto.
2. Implementar usando el fichero de configuración de cgcreate una política que dé menos prioridad a los procesos de usuario que a los procesos del sistema (o viceversa).

	*	Se ha implementado una política que da más prioridad a los procesos del sistema para el uso de la cpu.

	*	Abrimos o creamos (en caso de no existir), el archivo /etc/cgconfig.conf.
	*	En el archivo, escribimos:

	```
		mount {
    		cpu = /sys/fs/cgroup/cpu;
		}

		# Grupo del usuario
		group users { 
			cpu {
				#Se le da un 40%
				cpu.shares="400"; 
			}
		}

		# Grupo del sistema
		group system { 
			cpu {
				#Se le da un 60%
				cpu.shares="600"; 
			}
		} 
	```
3. Usar un programa que muestre en tiempo real la carga del sistema tal como htopy comprobar los efectos de la migración en tiempo real de una tarea pesada de un procesador a otro (si se tiene dos núcleos en el sistema).
	* Se han creado 2 grupos, g1 y g2; ejecutándose en los núcleos 1 y 2 respectivamente.
	* He empleado el navegdor firefox conmuchas pestañas abiertas para hacer la prueba.
	* Comenzamos ejecutando firefox en g1 con cgexec -g memory,cpu,cpuset,cpuacct:g1 firefox. Luego migro la tarea a g2 usando cgclassify -g memory,cpu,cpuset,cpuacct:g2 10916 (el PID)
	* El uso del núcleo 1 es de un 2.5%, aumentando a 20% cuando se realizan peticiones con firefox.
	* Al realizar la migración, el uso del núcleo 2 se dispara de 1.3% a casi el 15%, para luego volver a una cifra de 5.6%. Cuando se hacen peticiones, ocurre lo mismo que anteriormente y el uso del núcleo aumenta hasta alrededor del 22%.
	
4. Configurar un servidor para que el servidor web que se ejecute reciba mayor prioridad de entrada/salida que el resto de los usuarios.

	* Creamos el grupo para el servidor server y modificamos el archivo /etc/cgconfig.conf.

	```
		mount {
    		blkio = /sys/fs/cgroup/blkio;
		}

		# Grupo del usuario
		group users { 
			blkio {
				#Se le da un 30%
				blkio.weight="300"; 
			}
		}

		# Grupo del servidor
		group sever { 
			blkio {
				#Se le da un 70%
				blkio.weight="700"; 
			}
		}
	```

###==================================================================================================
### 10)
Comprobar si el procesador o procesadores instalados tienen estos flags. 
* ¿Qué modelo de procesador es? Intel® Core™ i7-4500U CPU @ 1.80GHz × 4
* ¿Qué aparece como salida de esa orden?
```
egrep '^flags.*(vmx|svm)' /proc/cpuinfo
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid
```

###==================================================================================================
### 11)
Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden kvm-ok.
```
sudo kvm-ok

INFO: /dev/kvm exists
KVM acceleration can be used
```

###==================================================================================================
### 12)
[Comentar diferentes soluciones de Software as a Service de uso habitual](https://github.com/JJ/GII-2014/issues/72).

Ya lo he comentado.


###==================================================================================================
#Tema 2
###==================================================================================================
### 1)Instalar un entorno virtual para tu lenguaje de programación favorito (uno de los mencionados arriba, obviamente).
virtualenv:

Instalación:
```
pip install virtualenv
```

Uso:
```
virtualenv ENV

New python executable in ENV/bin/python
Installing setuptools, pip...done.
```

###==================================================================================================
### 2)Darse de alta en algún servicio PaaS tal como Heroku, [Nodejitsu](https://www.nodejitsu.com/) u OpenShift.
Dado de alta en Heroku y OpenShift.


###==================================================================================================
### 3)Crear una aplicación en OpenShift y dentro de ella instalar WordPress.


No usar(
He seguido este [tutorial](http://robertovg.com/hosting/getting-started-with-wordpress-in-openshift/)

Crear la aplicación:
```
rhc app create testWordPress php-5.4 mysql-5.5 --from-code=https://github.com/robertovg/wordpress-example

Application Options
-------------------
Domain:      silttest
Cartridges:  php-5.4, mysql-5.5
Source Code: https://github.com/robertovg/wordpress-example
Gear Size:   default
Scaling:     no

Creating application 'testWordPress' ... done

  MySQL 5.5 database added.  Please make note of these credentials:

       Root User: adminnwf2CFB
   Root Password: JiyK_6Mq_YfF
   Database Name: testwordpress

Connection URL: mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/

You can manage your new MySQL database by also embedding phpmyadmin.
The phpmyadmin username and password will be the same as the MySQL credentials above.

Waiting for your DNS name to be available ... done

Clonar en «testwordpress»...
The authenticity of host 'testwordpress-silttest.rhcloud.com (54.234.243.133)' can't be established.
RSA key fingerprint is cf:ee:77:cb:0e:fc:02:d7:72:7e:ae:80:c0:90:88:a7.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'testwordpress-silttest.rhcloud.com,54.234.243.133' (RSA) to the list of known hosts.


Your application 'testwordpress' is now available.

  URL:        http://testwordpress-silttest.rhcloud.com/
  SSH to:     5466393b5973ca00a9000034@testwordpress-silttest.rhcloud.com
  Git remote: ssh://5466393b5973ca00a9000034@testwordpress-silttest.rhcloud.com/~/git/testwordpress.git/
  Cloned to:  /home/silt/Documentos/OpensiftTest/testwordpress

git add --all .
git commit
git push
```

No añado las instrucciones de consiguración para lanzarlo.)

He seguido este [tutorial](http://www.hongkiat.com/blog/setup-wordpress-openshift/)
La aplicación se llama testWordPress4.

Crear copia local:
```
git clone ssh://54663cee4382eca86400012c@testwordpress4-silttest.rhcloud.com/~/git/testwordpress4.git/
cd testwordpress4/
```


###==================================================================================================
### 4) Crear un script para un documento Google y cambiarle el nombre con el que aparece en el menú, así como la función a la que llama.
(Añadir una función al menú).

```javascript
/**
 * The onOpen function runs automatically when the Google Docs document is
 * opened. Use it to add custom menus to Google Docs that allow the user to run
 * custom scripts. For more information, please consult the following two
 * resources.
 *
 * Extending Google Docs developer guide:
 *     https://developers.google.com/apps-script/guides/docs
 *
 * Document service reference documentation:
 *     https://developers.google.com/apps-script/reference/document/
 */
function onOpen() {
  // Añadir un menú de prueba.
  DocumentApp.getUi().createMenu("Test").addItem('Test', 'test').addToUi();
}

/**
 * Test
 */
function test(){
  // Muestra un diálogo con botones Yes/No.
  var alerta = DocumentApp.getUi().alert(
      'Test',
      '¿Quieres intentarlo?',
      DocumentApp.getUi().ButtonSet.YES_NO);

  // Procesa la respuesta del usuario.
  if(alerta == DocumentApp.getUi().Button.YES){
    // Si el usuario clickea Yes.
    DocumentApp.getUi().alert('Haciendo algo chulo...');
  } 
  else{
    // Si el usuario clickea No.
    DocumentApp.getUi().alert('Cancelado.');
  }
}
```

###==================================================================================================	
### 5)Buscar un sistema de automatización de la construcción para el lenguaje de programación y entorno de desarrollo que usemos habitualmente.
* Para c/c++: Make y CMake.

	* Make: Make es una utilidad de Unix que construye automáticamente el ejecutable del programa y librerías a partir del código fuente leyendo ficheros llamados makefiles que especifican como derivar el programa objetivo.

	* CMake: Es una herramienta multiplataforma de generación o automatización de código. El nombre es una abreviatura para "cross platform make" (make multiplataforma); más allá del uso de "make" en el nombre, CMake es una suite separada y de más alto nivel que el sistema make común de Unix, siendo similar a las autotools.


* Para Ruby: Rake.

	* Rake es un software para la administración de tareas. Te permite especificar tareeas y describir dependencias, así como agrupar las tareas en un namespace. Las tareas se escriben en rakefiles en sintasis de Ruby. Rake usa las funciones anónimas de Ruby para definir varias tareas.

* Para Python: 
	* PyBuilder es una herramienta de construcción de software escrita en puro Python cuyo objetivo es ser usada para aplicaciones en Python principalmente.

* A-A-P: Programa capaz de descargar, construir e instalar software. Ejecuta una serie de recetas y permite scripting en python.

###==================================================================================================
### 6)Identificar, dentro del PaaS elegido o cualquier otro en el que se dé uno de alta, cuál es el fichero de automatización de construcción e indicar qué herramienta usa para la construcción y el proceso que sigue en la misma.
Heroku usa distintos ficheros y herramientas de automatización según el lenguaje:
* Ruby: Emplea Bundler como herramienta y Gemfile como fichero.
* Python: Para instalar las dependencias, estas se declaran en un fichero requirements.txt de la siguiente forma:
	
	```
		Django==1.6.5
		dj-database-url==0.3.0
		dj-static==0.0.6
		django-toolbelt==0.0.1
		gunicorn==19.0.0
		psycopg2==2.5.3
		static3==0.5.1
		wsgiref==0.1.2
	```
	
	Heroku usa pip para instalarlas luego.
* PHP: Las dependencias se declaran en el archivo composer.json.
* En el fichero de texto Procfile se pueden introducir los comandos necesarios para ejecutar la aplicación. Esto se puede usar sea cual sea el lenguaje.

###==================================================================================================
### 7) Buscar un entorno de pruebas para el lenguaje de programación y entorno de desarrollo que usemos habitualmente.
He buscado para varios lenguajes:

* Python: Existen varios módulos para realizar test, como [unittest](https://docs.python.org/2/library/unittest.html) (pese al nombre, sus utilidades también se pueden usar en test de integración) o [doctest](https://docs.python.org/2/library/doctest.html) (este funciona de una forma curiosa, ya que busca en el código cadenas encerradas entre """ """, que se puedan interpretar como comandos en la shell interactiva de python y los ejecuta). [Pytest](http://pytest.org/latest/) tiene una sintaxis más simple que la de unittest y puede ejecutar los test directamente usando el comando py.test.
Por otro lado, tenemos a [nose](https://nose.readthedocs.org/en/latest/), una extensión de unittest que nos simplifica a creación de test. Para empezar,incluye la capacidad de descubrir automáticamente los test disponible, ahorrándonos el trabajo de tener que programar test suites nosotros mismos.
Por ultimo, señalar que [Django](https://www.djangoproject.com/) incluye ya una suite para programar pruebas basada en unittest. Con el comando python manage.py test se prueban todos los test disponibles para las aplicaciones del proyecto. Es necesario que los test estén en un archivo en la raíz de la aplicación llamado tests.py.

* Java: No hay mucho que escribir, como ya se comentó en la práctica lo más usado es [JUnit](http://junit.org/).

* C++: He comprobado varios:
	* [Microsoft Unit Testing Framework for C++](http://msdn.microsoft.com/en-us/library/hh598953.aspx): Framework de Microsoft para realizar pruebas unitarias de c++. No lo he usado, pero parece estar bien integrado con Visual Studio, así que lo pongo aquí por si alguien trabaja en Windows (aunque no es lo apropiado para desarrollar software libre).
	* [Googletest](https://code.google.com/p/googletest/): Framework de Google para construir test. Está basado en los xUnit. Entre otras cosas, soporta el descubrimiento automático de test y que el usuario defina sus propios asserts.
	* [CppUnit](http://cppunit.sourceforge.net/doc/cvs/cppunit_cookbook.html) Es una implementación para c++ de JUnit (según los propios autores). Sus características son prácticamente idénticas.


###==================================================================================================
#Tema 3
###==================================================================================================
### 1)Crear un espacio de nombres y montar en él una imagen ISO de un CD de forma que no se pueda leer más que desde él. Pista: en [ServerFault](http://serverfault.com/questions/198135/how-to-mount-an-iso-file-in-linux) nos explican como hacerlo, usando el dispositivo loopback.
Para empezar, nos hacemos root y creamos un mounts namespace (para aislar recursos declarados con mount):
	```
		su
		unshare --mount /bin/bash
	```

Luego podemos proceder a montar la imagen iso:
	```
		mkdir /mnt/temp
		mount -o loop -t iso9660 ubuntu14.04.iso /mnt/temp
	```

### 2)
1. Mostrar los puentes configurados en el sistema operativo.
	Normalmente, habría que crear algún puente con sudo brctl addbr <nombre>, pero en mi caso ya había uno creado por docker.
	
	```
		silt@silt-Lenovo-Z50-70:~$ brctl show
		bridge name	bridge id		STP enabled	interfaces
		docker0		8000.56847afe9799	no			
	```

2. Crear un interfaz virtual y asignarlo al interfaz de la tarjeta wifi, si se tiene, o del fijo, si no se tiene.
	Aunque tengo una tarjeta wifi, para evitar probemas suelo trabajar en una máquina virtual y esta cree que está conectada por cable.

	Creamos la interfaz virtual y le asignamos una interfaz (en este caso eth0):
	```
		sudo brctl addbr test-bridge
		ip addr show
		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
			link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
			inet 127.0.0.1/8 scope host lo
			   valid_lft forever preferred_lft forever
			inet6 ::1/128 scope host 
			   valid_lft forever preferred_lft forever
		2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
			link/ether 00:0c:29:f1:4c:81 brd ff:ff:ff:ff:ff:ff
			inet 172.16.122.128/24 brd 172.16.122.255 scope global eth0
			   valid_lft forever preferred_lft forever
			inet6 fe80::20c:29ff:fef1:4c81/64 scope link 
			   valid_lft forever preferred_lft forever
		3: test-bridge: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default 
    			link/ether 0e:b4:6a:c7:d4:0a brd ff:ff:ff:ff:ff:ff

		sudo brctl addif test-bridge eth0
		ip addr show

		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
			link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
			inet 127.0.0.1/8 scope host lo
			   valid_lft forever preferred_lft forever
			inet6 ::1/128 scope host 
			   valid_lft forever preferred_lft forever
		2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master test-bridge state UP group default qlen 1000
			link/ether 00:0c:29:f1:4c:81 brd ff:ff:ff:ff:ff:ff
			inet 172.16.122.128/24 brd 172.16.122.255 scope global eth0
			   valid_lft forever preferred_lft forever
			inet6 fe80::20c:29ff:fef1:4c81/64 scope link 
			   valid_lft forever preferred_lft forever
		3: test-bridge: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default 
    			link/ether 0e:b4:6a:c7:d4:0a brd ff:ff:ff:ff:ff:ff
	```

### 3)
1. Usar debootstrap (o herramienta similar en otra distro) para crear un sistema mínimo que se pueda ejecutar más adelante.
	He decidido instalar Lucid.

	```
		sudo debootstrap --arch=amd64 lucid /home/silt/ubuntu http://archive.ubuntu.com/ubuntu
	```

	Omito la salida ya que es muy larga.
2. Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.
	```
		sudo rinse --arch=amd64 --directory /home/silt/fedora8 --distribution fedora-core-8
	```

### 4)Instalar alguna sistema debianita y configurarlo para su uso. Trabajando desde terminal, probar a ejecutar alguna aplicación o instalar las herramientas necesarias para compilar una y ejecutarla.

Aprobechamos el sistema ubuntu que instalamos en el ejercicio anterior usando debootstrap.

	´´´
		silt@ubuntu:~$ sudo chroot /home/silt/ubuntu
		root@ubuntu:/#
		root@ubuntu:/# mount -t proc proc /proc
		root@ubuntu:/# sudo apt-get install language-pack-es
	´´´

Ahora, vamos a instalar el paquete de build-essential, instalar nano y crear un pequeño hello world en c++.

	´´´
		root@ubuntu:/# apt-get install build-essential
		root@ubuntu:/# apt-get install nano
		root@ubuntu:/# nano hello_world.cpp
	´´´
	
El código del programa es:
	
	´´´c++
		#include <iostream>

		using namespace std;

		int main(){
			cout << "Hello world!" << endl;

			return 0;
		}
	```

Ahora, lo compilamos y lo ejecutamos.

	```
		root@ubuntu:/# make hello_world
		g++     hello_world.cpp   -o hello_world
		root@ubuntu:/# ./hello_world
		Hello world!
	```

### 5) Instalar una jaula chroot para ejecutar el servidor web de altas prestaciones nginx.
Accedemos a la jaula ya creada en los ejercicios anteriores y ejecutamos los siguientes comandos para instalar nginx.

	´´´
		echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list
		sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
		sudo apt-get update
		sudo apt-get install nginx
	´´´

Por último, ejecutamos el siguiente comando para iniciar el servicio.

	```
		sudo service nginx start
	```

Para detenerlo.

	```
		sudo service nginx stop
	```
### 6) Crear una jaula y enjaular un usuario usando `jailkit`, que previamente se habrá tenido que instalar.
Instalamos jailkit.

	```
		silt@ubuntu:~$ cd jailkit-2.17
		silt@ubuntu:~/jailkit-2.17$ ./configure && make && sudo make install
	```

Tras innstalar, creamos la jaula,

	```
		root@ubuntu:/home/silt/jailkit-2.17# mkdir -p /seguro/jaulas/dorada
		root@ubuntu:/home/silt/jailkit-2.17# chown -R root:root /seguro
		root@ubuntu:/home/silt/jailkit-2.17# jk_init -v -j /seguro/jaulas/dorada jk_lsh basicshell netutils editors	
	```

Añadimos el usuario
	
	```
		root@ubuntu:/home/silt/jailkit-2.17# adduser test
		root@ubuntu:/home/silt/jailkit-2.17# sudo jk_jailuser -m -j /seguro/jaulas/dorada test
	```	

###==================================================================================================
#Tema 4
###==================================================================================================
### 1) Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en [GitHub](http://github.com/lxc/lxc) como en el [sitio web](http://linxcontainers.com/) está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.

Descargamos la última versión y la instalamos ejecutando los siguientes comandos;

	```
		./autogen.sh
		./configure
		make 
		sudo make install
	```

Si no tenemos aclocal ejecutamos:

	```
		sudo apt-get install autotools-dev
		sudo apt-get install automake
	```

Para poder usarlo con sudo:
	```
		sudo cp /usr/local/lib/liblxc* /usr/lib/x86_64-linux-gnu
	```

### 2) Comprobar qué interfaces puente se han creado y explicarlos.
```
	ifconfig
	lxcbr0    Link encap:Ethernet  direcciónHW fe:84:8a:f0:48:89  
		      Direc. inet:10.0.3.1  Difus.:10.0.3.255  Másc:255.255.255.0
		      Dirección inet6: fe80::54bb:68ff:fe89:7bf2/64 Alcance:Enlace
		      ACTIVO DIFUSIÓN FUNCIONANDO MULTICAST  MTU:1500  Métrica:1
		      Paquetes RX:77 errores:0 perdidos:0 overruns:0 frame:0
		      Paquetes TX:129 errores:0 perdidos:0 overruns:0 carrier:0
		      colisiones:0 long.colaTX:0 
		      Bytes RX:7572 (7.5 KB)  TX bytes:17455 (17.4 KB)

```

La nueva interfz creada, lxcbr0, es necesaria para poder dar conexión a internet a los contenedores a través de la conexión de la máquina anfitriona. Es un puente de red.

### 3)

1. Crear y ejecutar un contenedor basado en Debian.

Orden:
```
	sudo lxc-create -t ubuntu -n ubuntu
```

Resultado:
```
	Generation complete.
	Processing triggers for libc-bin (2.19-0ubuntu6.4) ...
	Processing triggers for initramfs-tools (0.103ubuntu4.2) ...
	Download complete
	Copy /usr/local/var/cache/lxc/trusty/rootfs-amd64 to /usr/local/var/lib/lxc/una-caja/rootfs ... 
	Copying rootfs to /usr/local/var/lib/lxc/una-caja/rootfs ...
	Generating locales...
	  es_ES.UTF-8... up-to-date
	Generation complete.
	Creating SSH2 RSA key; this may take some time ...
	Creating SSH2 DSA key; this may take some time ...
	Creating SSH2 ECDSA key; this may take some time ...
	Creating SSH2 ED25519 key; this may take some time ...
	update-rc.d: warning: default stop runlevel arguments (0 1 6) do not match ssh Default-Stop values (none)
	invoke-rc.d: policy-rc.d denied execution of start.

	Current default time zone: 'Europe/Madrid'
	Local time is now:      lun dic 15 17:38:02 CET 2014.
	Universal Time is now:  Mon Dec 15 16:38:02 UTC 2014.


	##
	# The default user is 'ubuntu' with password 'ubuntu'!
	# Use the 'sudo' command to run tasks as root in the container.
	##
```

Ejecutar:
```
	sudo lxc-start -n ubuntu
	Ubuntu 14.04.1 LTS ubuntu console

	ubuntu login: <4>init: setvtrgb main process (418) terminated with status 1
 	* Stopping save kernel messages   ...done.
	<4>init: plymouth-upstart-bridge main process ended, respawning
```


2. Crear y ejecutar un contenedor basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya. Fedora, al parecer, tiene problemas si estás en Ubuntu 13.04 o superior, así que en tal caso usa cualquier otra distro. Por ejemplo, [Óscar Zafra ha logrado instalar Gentoo usando un script descargado desde su sitio, como indica en este comentario en el issue](https://github.com/IV-GII/GII-2013/issues/87#issuecomment-28639976).

He instalado fedora.

```
	sudo lxc-create -t fedora -n fedora

	¡Listo!
	Fixing up rpm databases
	Download complete.
	Copy /var/cache/lxc/fedora/x86_64/20/rootfs to /var/lib/lxc/fedora/rootfs ... 
	Copying rootfs to /var/lib/lxc/fedora/rootfs ...
	Storing root password in '/var/lib/lxc/fedora/tmp_root_pass'
	Expirando contraseña para el usuario root.
	passwd: Éxito
	installing fedora-release package
	El paquete fedora-release-20-3.noarch ya se encuentra instalado con su versión más reciente
	Nada para hacer

	Container rootfs and config have been created.
	Edit the config file to check/enable networking setup.

	You have successfully built a Fedora container and cache.  This cache may
	be used to create future containers of various revisions.  The directory
	/var/cache/lxc/fedora/x86_64/bootstrap contains a bootstrap
	which may no longer needed and can be removed.

	A LiveOS directory exists at /var/cache/lxc/fedora/x86_64/LiveOS.
	This is only used in the creation of the bootstrap run-time-environment
	and may be removed.

	The temporary root password is stored in:

		    '/var/lib/lxc/fedora/tmp_root_pass'


	The root password is set up as expired and will require it to be changed
	at first login, which you should do as soon as possible.  If you lose the
	root password or wish to change it without starting the container, you
	can change it from the host by running the following command (which will
	also reset the expired flag):

		    chroot /var/lib/lxc/fedora/rootfs passwd

```

Ejecutar:
```
	sudo lxc-start -n fedora
```

### 4) 
1. Instalar lxc-webpanel y usarlo para arrancar, parar y visualizar las máquinas virtuales que se tengan instaladas.
Primero, instalar con:
	```
		wget http://lxc-webpanel.github.io/tools/install.sh -O - | bash
	```

Es necesarioser root.

Para poder usarlo, ponemos en el navegador http://localhost:5000. Para el login usar admin tanto para user como para password.
En las imágenes puede observarse su uso.

![Visualizar](https://github.com/silt99/CC/blob/master/web_panel2.png)
Format: ![Alt Text](url)

![Arrancar](https://github.com/silt99/CC/blob/master/web_panel1.png)
Format: ![Alt Text](url)

![Parar](https://github.com/silt99/CC/blob/master/web_panel3.png)
Format: ![Alt Text](url)



2. Desde el panel restringir los recursos que pueden usar: CPU shares, CPUs que se pueden usar (en sistemas multinúcleo) o cantidad de memoria.

Todo esto se puede hacer accediendo a las opciones del contenedor clickeando en su nombre en el panel de la izquierda. Justo debajo de IP adress, tenemos las opciones para limitar los recursos:
	
	* Memoria (Memory limit)
	* Memoria y Swap (Memory + Swap limit)
	* CPUs
	* CPU shares

### 5) Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx.

Primero, ejeutamos nginx en una jaula:
	Accedemos a una de las jaulas instaladas en el anterior tema:
	```silt@ubuntu:~$ sudo chroot /home/silt/ubuntu```

	Iniciamos nginx:
	```root@ubuntu:/# service nginx start```

Hacemos lo propio con uno de los contenedores anteriores:
	```
		sudo lxc-start -n ubuntu
		ubuntu@ubuntu sudo service nginx start
	```

Ahora, usar el benchmark para comparar ambas prestaciones. Usaré los parámetros -n 1000000 y -c 20.

Juala:
	```
		ab -n 1000000 -c 20 http://127.0.0.1/index.html
		
		Benchmarking 127.0.0.1 (be patient)


		Server Software:        nginx/1.4.1
		Server Hostname:        127.0.0.1
		Server Port:            80

		Document Path:          /index.html
		Document Length:        612 bytes

		Concurrency Level:      20
		Time taken for tests:   39.502 seconds
		Complete requests:      1000000
		Failed requests:        0
		Total transferred:      844000000 bytes
		HTML transferred:       612000000 bytes
		Requests per second:    25314.87 [#/sec] (mean)
		Time per request:       0.790 [ms] (mean)
		Time per request:       0.040 [ms] (mean, across all concurrent requests)
		Transfer rate:          20864.99 [Kbytes/sec] received

		Connection Times (ms)
				      min  mean[+/-sd] median   max
		Connect:        0    0   0.1      0       1
		Processing:     0    0   0.6      0     144
		Waiting:        0    0   0.6      0     144
		Total:          0    1   0.6      1     144

		Percentage of the requests served within a certain time (ms)
		  50%      1
		  66%      1
		  75%      1
		  80%      1
		  90%      1
		  95%      1
		  98%      1
		  99%      1
		 100%    144 (longest request)
	```

Contenedor:
	``` 
		ab -n 1000000 -c 20 http://10.0.3.1/index.html

		Benchmarking 10.0.3.1 (be patient)


		Server Software:        nginx/1.4.1
		Server Hostname:        10.0.3.1
		Server Port:            80

		Document Path:          /index.html
		Document Length:        612 bytes

		Concurrency Level:      20
		Time taken for tests:   40.386 seconds
		Complete requests:      1000000
		Failed requests:        0
		Total transferred:      844000000 bytes
		HTML transferred:       612000000 bytes
		Requests per second:    24761.07 [#/sec] (mean)
		Time per request:       0.808 [ms] (mean)
		Time per request:       0.040 [ms] (mean, across all concurrent requests)
		Transfer rate:          20408.54 [Kbytes/sec] received

		Connection Times (ms)
				      min  mean[+/-sd] median   max
		Connect:        0    0   0.0      0       1
		Processing:     0    0   2.1      0     486
		Waiting:        0    0   2.1      0     486
		Total:          0    1   2.1      1     487

		Percentage of the requests served within a certain time (ms)
		  50%      1
		  66%      1
		  75%      1
		  80%      1
		  90%      1
		  95%      1
		  98%      1
		  99%      1
		 100%    487 (longest request)
	```
	
	Aparentemente, la jaula funciona un mejor que el contenedor, concretamente tiene 400KB/s más de velocidad de transferencia y tarda casi un segundo menos en la prueba.

### 6) 
1. Instalar juju.
```
	sudo add-apt-repository ppa:juju/stable
	sudo apt-get update && sudo apt-get install juju-core juju-local
	sudo juju bootstrap
```

2. Usándolo, instalar MySQL en un táper.
```
	juju deploy mysql
	Added charm "cs:trusty/mysql-13" to the environment.

	juju status
	environment: local
	machines:
	  "0":
		agent-state: started
		agent-version: 1.20.14.1
		dns-name: localhost
		instance-id: localhost
		series: trusty
		state-server-member-status: has-vote
	  "1":
		instance-id: pending
		series: trusty
	services:
	  mysql:
		charm: cs:trusty/mysql-13
		exposed: false
		relations:
		  cluster:
		  - mysql
		units:
		  mysql/0:
		    agent-state: pending
		    machine: "1"
```


### 7)

1. Destruir toda la configuración creada anteriormente.

```
	sudo juju destroy-unit mysql/0
	sudo juju destroy-machine 1
	sudo juju remove-service mysql
```

o

```
	sudo juju destroy-environment local
```

2. Volver a crear la máquina anterior y añadirle mediawiki y una relación entre ellos.

```
	juju deploy mysql
	juju deploy mediawiki
	juju add-relation mediawiki:db mysql:db
	juju expose mediawiki
```

3. Crear un script en shell para reproducir la configuración usada en las máquinas que hagan falta.

```
	juju deploy mysql
	juju deploy mediawiki
	juju add-relation mediawiki:db mysql:db
```

### 8) Instalar libvirt. Te puede ayudar [esta guía para Ubuntu](https://help.ubuntu.com/12.04/serverguide/libvirt.html).

```
	sudo apt-get install kvm libvirt-bin
	sudo adduser $USER libvirtd
	sudo apt-get install virtinst
```

### 9) Instalar un contenedor usando virt-install.

```
	sudo virt-install -n web_devel -r 256 --disk path=/var/lib/libvirt/images/web_devel.img,bus=virtio,size=4 -c ubuntu.iso --accelerate --network network=default,model=virtio --connect=qemu:///system --vnc --noautoconsole -v
```

### 10) Instalar docker.

Ya lo tenía instalado desde el tema 1:

	```
		silt@silt-Lenovo-Z50-70:~$ sudo docker run -i -t ubuntu /bin/bash
		Unable to find image 'ubuntu' locally
		ubuntu:latest: The image you are pulling has been verified sistema de gestión de fuentes git
		sudo apt-get update
		sudo apt-get
		511136ea3c5a: Pull complete 
		d497ad3926c8: Pull complete 
		ccb62158e970: Pull complete 
		e791be0477f2: Pull complete 
		3680052c0f5c: Pull complete 
		22093c35d77b: Pull complete 
		5506de2b643b: Pull complete 
		Status: Downloaded newer image for ubuntu:latest
		root@9d1834f0e2cc:/# 
	```

### 11) 
1. Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.

Instalando ubuntu-upstart:

```
	sudo docker pull ubuntu-upstart 
	Pulling repository ubuntu-upstart
	cc5568b383b0: Pulling image (latest) from ubuntu-upstart, endpoint: https://regicc5568b383b0: Download complete 
	511136ea3c5a: Download complete alando
	3b363fd9d7da: Download complete 
	607c5d1cca71: Download complete 
	f62feddc05dc: Download complete 
	8eaa4ff06b53: Download complete 
	21caacb06f6e: Download complete 
	dc080c3e0a99: Download complete 
	e5c4145a245a: Download complete 
	d003a990b2c2: Download complete 
	eaab51298db4: Download complete 
	bd49bb7feba9: Download complete 
	b0fc60f5a210: Download complete 
	46f4a09f73a6: Download complete 
	5753b8f6c47f: Download complete 
	a25fe21a520b: Download complete 
	Status: Downloaded newer image for ubuntu-upstart:latest
```

Instalar CentOS:

```
	sudo docker pull centos
	Pulling repository centos
	8efe422e6104: Download complete 
	511136ea3c5a: Download complete 
	5b12ef8fd570: Download complete 
	Status: Downloaded newer image for centos:latest
```

2. Buscar e instalar una imagen que incluya MongoDB.

instalando dockerfile/mongodb:

```
	sudo docker pull dockerfile/mongodb
	Pulling repository dockerfile/mongodb
	0980bbd7909c: Download complete 
	511136ea3c5a: Download complete 
	3b363fd9d7da: Download complete 
	607c5d1cca71: Download complete 
	f62feddc05dc: Download complete 
	8eaa4ff06b53: Download complete 
	6208e07d879f: Download complete 
	c20edc7e0d45: Download complete 
	b7e60ab5525f: Download complete 
	d6bd9059d33b: Download complete 
	86b06feccb1a: Download complete 
	37f261a144df: Download complete 
	fe5bad1d1ac4: Download complete 
	86481127ffdc: Download complete 
	e30c891ea0ca: Download complete 
	a86afe494f70: Download complete 
	6c89a74b2fcc: Download complete 
	cc9891f92d78: Download complete 
	Status: Downloaded newer image for dockerfile/mongodb:latest
```

### 12) Crear un usuario propio e instalar nginx en el contenedor creado de esta forma.

### 13) Crear a partir del contenedor anterior una imagen persistente con commit.

### 14) Crear una imagen con las herramientas necesarias para el proyecto de la asignatura sobre un sistema operativo de tu elección.
