Ejercicios
============================
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
