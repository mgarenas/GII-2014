Ejercicios de David González Sola
=====================================

## Sesión 17-octubre-2014

### Ejercicio 1

- **Nombre:** HP ProLiant ML310e G8 XE
- **Precio (con IVA):** 833€
- **Precio (sin IVA):** 688.43€
- **Amortización en 4 años:** 172.11€ por año
- **Amortización en 7 años:** 98.35€ por año
- [**Referencia**](http://www.pccomponentes.com/hp_proliant_ml310e_g8_xe_e3_1220_8gb_2tb___foundation_2012.html)

### Ejercicio 2

Se han elegido:
- **Amazon Web Services:** paquete m3.2xlarge con 8 núcleos, 30GB de memoria a un precio de 0.616$ la hora.
- **Google Compute Engine:** paquete n1-standard-8 con 8 núcleos, 30GB de memoria a un precio de 0.616$ la hora.

En AWS es necesario un pago anticipado a sumar al coste por horas. Sin embargo, en GCE no es necesaria realizar ningún tipo de pago anticipado.

Coste usando el 1% del tiempo:
- **Amazon Web Services:** 0.616$/horas * 87.6 horas = 53.96 $ + 439$ (pago anticipado) = 492.96$
- **Google Compute Engine:** 0.616$/horas * 87.6 horas = 53.96 $

Coste usando el 10% del tiempo: 
- **Amazon Web Services:** 0.616$/horas * 876 horas = 539.6 $ + 439$ (pago anticipado) = 978.6$
- **Google Compute Engine:** 0.616$/horas * 876 horas = 539.6 $

### Ejercicio 3

- **Alojar varios clientes en un sólo servidor:** utilizaría una virtualización a nivel de SO con el fin de que cada cliente se encuentre aislado del resto.
- **Crear un sistema eficiente web + middleware + bd:** yo no utilizaría una virtualización plena ya que consume muchos recursos y la eficiencia se reduciría drasticamente. Utilizaría una virtualización a nivel de aplicación.
- **Sistema de pruebas software e integración continua:** utilizaría una virtualización de entornos de desarrollo pudiendo reproducir fielmente el entorno de producción.

### Ejercicio 4

Respuestas:

1. docker version
2. docker search tutorial
3. docker pull learn/tutorial
4. docker run learn/tutorial echo "hello world"
5. docker run learn/tutorial apt-get install -y ping
6. docker commit 698 learn/ping
7. docker run learn/ping www.google.com
8. 
	- docker ps 
	- docker inspect efefdc74a1d5
9. docker push learn/ping

### Ejercicio 5

> apt-get install git

### Ejercicio 6

Se crea desde la web www.github.com el repositorio. Posteriormente es necesario descargarlo en local utilizando el comando:
> git clone http://www.github.com/DavidGSola/CloudComputing.git

Se modifica el fichero README con cualquier editor de textos y finalmente se vuelve a subir al repositorio en la nube utilizando los comandos: 
> git commit -m 'comentario'

> git push

## Sesión 20-octubre-2014

### Ejercicio 7

En Ubuntu 12.04 se encuentra montado en /sys/fs/cgroups. Contiene gran cantidad de archivos como por ejemplo:
```
blkio.io_merged                   cpuset.memory_spread_page
blkio.io_queued                   cpuset.memory_spread_slab
blkio.io_service_bytes            cpuset.mems
blkio.io_serviced                 cpuset.sched_load_balance
blkio.io_service_time             cpuset.sched_relax_domain_level
```
### Ejercicio 8.1

Se han creado tres grupos:
- **Buenos:** ejecutarán el navegador. (cpu usage: 31107072)
- **Regulares:** ejecutarán el procesador de textos. (cpu usage: 1094374)
- **Malos:** ejecutarán gimp. (cpu usage: 176661809)

### Ejercicio 8.2


### Ejercicio 9.1

### Ejercicio 9.2

Se debe crear el archivo de configuración '/etc/cgconfig.conf'. Un ejemplo de este archivo donde se de prioridad a los procesos del usuario sería:

```
mount {
	cpu = /cgroup/cpu
}

group usuario {
	cpu {
		cpu.shares="900";
	}
}

group sistema {
	cpu {
		cpu.shares="100";
	}
}
```
### Ejercicio 9.3

He utilizado el programa GIMP para comprobar los efectos de la migración del proceso.
Se han utilizado dos grupos, el grupo *bueno* se ejecutará en el núcleo 1 y el grupo *malo* en el núcleo 7. Se empieza a ejecutar en el grupo *bueno* y el núcleo 7 se encuentra totalmente ocioso. Una vez se realiza el intercambio con el comando 'cgclassify -g memory,cpu:malos 8031' el núcleo 7 empieza a ser usado un poco más (~2.5%) pero si se empieza a utilizar GIMP esta cantidad sube hasta el ~20%. Si se vuelve a intercambiar al núcleo 1 con el comando 'cgclassify -g memory,cpu:buenos 8031' el núcleo 7 vuelve a estar practicamente ocioso y el uso del núcleo 1 sube hasta el ~20%.

### Ejercicio 9.4

Utilizando el fichero de configuración /etc/cgconfig.conf podemos obligar al sistema a darle mayor prioridad entrada/salida al servidor. En este caso, se crean dos grupos (servidor y otros. El parámetro weight del subdirectorio blkio controla la proporción de acceso al sistema de entrada/salida. Con un número mayor, mayor prioridad de entrada/salida tendrá el grupo.


```
mount {
	blkio = /cgroup/blkio;
}

group servidor {
	blkio {
		blkio.weight="900"
	}
}

group others {
	blkio {
		blkio.weight="100"
	}
}
```
### Ejercicio 10

- **Modelo de procesador:** Intel® Core™ i7-3630QM CPU @ 2.40GHz x 8
- **Salida por pantalla:** `flags`: `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms`

### Ejercicio 11

Tras ejecutar el comando 'kvm-ok' aparece la siguiente información en la consola:
```
	INFO: /dev/kvm exists
	KVM acceleration can be used
```

## Sesión 24-octubre-2014

### Ejercicio 12

Un ejemplo de Saas al que accede a diario gran parte de la población *conectada* es Facebook. No es necesaria ningún tipo de instalación en el ordenador personal del cliente y simplemente utilizando el navegador web (siempre que el servicio se encuentre disponible en ese país) se podrá utilizar este. Por supuesto, esta libertad a la hora de acceder al servicio tiene sus incovenientes, como por ejemplo la falta de poder sobre tus propios datos y los problemas de privacidad que conlleva.

## Sesión 7-noviembre-2013

## Tema 2

### Ejercicio 1

Se ha instalado utilizando aptitude:
> apt-get install phyton-virtualenv

### Ejercicio 2

Registrado correctamente en [OpenShift](https://www.openshift.com/).

### Ejercicio 3

Se ha creado la aplicación de WordPress desde la web de OpenShift.
[Enlace](https://php-davidgsola.rhcloud.com/)

### Ejercicio 4

Creado el script correctamente. Le proporciono un enlace para que lo compruebe:
[Enlace](https://script.google.com/d/1LLGse1RZyNFlgqg172FNTtUR2PhH2RY1cS83XOmighXdMWGjwC2kidLY/edit?usp=sharing)

### Ejercicio 5

Uno de los lenguajes que utilizo habitualmente es C++. Para C++ existen los ficheros Makefile, que permiten automatizar la compilación, así como el enlazado de las librerías y la creación del ejecutable.

### Ejercicio 6



### Ejercicio 7

El lenguaje que utilizo habitualmente suele ser Java para desarrollar aplicaciones Android. Existe un entorno de pruebas para este caso específico que se llama Android JUnit.
Funciona de la siguiente manera:
1. Añadir un proyecto de Test a un proyecto ya existente.
2. Configurar el proyecto de Test seleccionando un nombre, la versión Android para la cual se construirá, etc.
3. Crear un JUnit Test Case.
4. Modificar el constructor y el método setUp de la clase Test creada.
5. Añadir el método de test.
6. Ejecutar test.

## Tema 3 Técnicas de Virtualización

### Ejercicio 1 

Lo primero que se ha hecho es generar un archivo *ISO* en Linux con el programa **genisoimage**:
> genisoimage -o isoPrueba.iso proyectos.md
Creamos el hostname:
> hostname probandoIso
Ahora creamos un lugar donde montarlo:
> mkdir /mnt/isoimage
Una vez creado el archivo *ISO* es hora de montarlo:
> mount -o loop -t iso9660 example.iso /mnt/isoimage
Y la salida es:
> mount: block device /home/david/Documentos/FacultadLinux/Master/CloudComputing/isoPrueba.iso is write-protected, mounting read-only

### Ejercicio 2

1. Utilizando el comando:

> ip addr show

![Puentes configurados](http://i.imgur.com/cXTNDzF.jpg)

2. Con el *wlan0* no me permite realizar el puente ni a mi ni a algunos de mis compañeros. Otros han podido realizarlo con el *eth0* pero no cuento con interaz *eth0* en mi portatil.

## Tema 4 Virtualización ligera usando contenedores

### Ejercicio 1

> sudo apt-get install lxc

### Ejercicio 2

Al instalar lxc se han creado y configurado un *bridge* y un *virtual ethernet device* para que los contenedores tengan acceso al *host* y a internet.

![Listado bridges](http://i.imgur.com/DZVBu1G.jpg)

### Ejercicio 3

Lo primero que he hecho ha sido crear dos contenedores, uno de cada manera, utilizando *ubuntu* y *ubuntu-cloud*. Una vez creados ambos procedo a listar los contenedores mediante la orden:

> sudo lxc-list 

Aparecen ambos contenedores en el estado **STOPPED**.
Ahora podemos ejecutar uno de los contenedores y los volvemos a listar.

> sudo lxc-start -n nubecilla

![Listado contenedores](http://i.imgur.com/9i0SGii.jpg)

Por último podemos utilizar el contenedor *nubecilla* de manera autónoma.

![Contenedor nubecilla](http://i.imgur.com/uUkGYUV.jpg)

### Ejercicio 4

Se ha descargado de github el script de instalación y se manda al bash para que lo ejecute mediante la opción -O  y el pipeline:

> wget http://lxc-webpanel.github.com/tools/install.sh -O - | bash

Accediendo desde un navegador a la dirección *http://localhost:5000* se accede al webpanel de lxc. Dentro de uno de los contenedores se cambia de manera muy sencilla el número de cpus, cpushares, etc.

![Webpanel](http://i.imgur.com/bIdxRej.jpg)

### Ejercicio 5

### Ejercicio 6

Primero se ha añadido el repositorio para que se instale la última versión. Se ha instalado correctamente *juju* con el comando:

> sudo apt-get install juju

### Ejercicio 7

Se ha intentando utilizar *juju* en local. Lo primero fue modificar el fichero enviroments.yaml para que utilizará por defecto **local** en lugar de **amazon**. Pero al intentar lanzar el comando *juju bootstrap* me aparece un fallo que trás buscar en internet he sido incapaz de resolver.

### Ejercicio 8

Se ha instalado correctamente utilizando el comando de la guía:

> sudo apt-get install kvm libvirt-bin

Se ha intentado añadir el usuario al grupo de *libvirt* pero aparece un mensaje avisando que ya existía previamente el usuario.

### Ejercicio 9

He instalado un contenedor del SO Ubuntu con el comando:

> sudo virt-install --name ubuntu --ram 512 --vcpu 1 --disk path=/home/ubuntu,size=2 -c /home/David/Descargas/lubuntu-14.10-desktop-i386.iso

Se le ha asignado 512 MB de RAM, una sola CPU virtual y 2 GB. Por último, la localización de la imagen a partir de la cual se va a crear el contenedor.

### Ejercicio 10

Tengo instalado Ubuntu 12.04 por lo que la instalación de *Docker* no es trivial:

1. Lo primero es instalar el *backported kernel*

> sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring

2. Se reinicia el SO.
3. Se añade el respositorio fuente de *Docker*:

> sudo apt-get install python-software-properties && sudo add-apt-repository ppa:dotcloud/lxc-docker

4. Se actualizan los repositorios de aptitude *apt-get update*.
5. Finalmente se instala *Docker*:

> sudo apt-get install lxc-docker	

### Ejercicio 11

Para la instalación de Ubuntu:

> sudo docker pull partlab/ubuntu

Cuya salida por consola ha sido: 

```
Pulling repository partlab/ubuntu
Pulling image 220f670a5152a192ee6b58d585f66305b5711f91a83f35b2652e12b910e6fd1d (latest) from partlab/ubuntu
Pulling 220f670a5152a192ee6b58d585f66305b5711f91a83f35b2652e12b910e6fd1d metadata
Pulling 220f670a5152a192ee6b58d585f66305b5711f91a83f35b2652e12b910e6fd1d fs layer
Downloading     32 B/32 B (100%)
Pulling 564941eb5df86253d0701832918eb7c479e0e7690158dee5c785cb6178c9b0ca metadata
Pulling 564941eb5df86253d0701832918eb7c479e0e7690158dee5c785cb6178c9b0ca fs layer
Downloading 2.454 MB/24.27 MB (10%)
...
```


