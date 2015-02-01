Introducción a la infraestructura virtual: concepto y soporte físico
====================================================================

## Ejercicio 1
_Consultar en el catálogo de alguna tienda de informática el precio de un
ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años.
Consultar [este artículo en Infoautónomos sobre el tema](http://www.infoautonomos.com/consultas-a-la-comunidad/988/)._

- [Servidor torre PowerEdge T620](http://www.dell.com/es/empresas/p/poweredge-t620/pd)
- 579€ Sin IVA
- Amortización a cuatro años: 144.75€ por año.
- Amortización a siete años: 82.72€ por año.

## Ejercicio 2
_Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube,
comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo
tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro
equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo._

Un año son _24 * 365 = 8760 horas_.

Se han elegido los servicios de [Microsoft Azure](http://azure.microsoft.com/es-es/pricing/details/cloud-services/) y [Google Compute Engine](https://cloud.google.com/compute/#pricing),
ambos alojados en Europa, en concreto, los paquetes __A5__ y __n1-highmem-2__, respectivamente.

Para un __1%__ de uso:
- __Microsoft Azure__: 0.01 * 8760 * _0,35$/h_ = __30.66 $__
- __Google Compute Engine__: 0.01 * 8760 * _0,18$/h_ = __15.768 $__

Para un __10%__ de uso:
- __Microsoft Azure__: 0.1 * 8760 * _0,35$/h_ = __306.6 $__
- __Google Compute Engine__: 0.1 * 8760 * _0,18$/h_ = __157.68 $__

## Ejercicio 3
_¿Qué tipo de virtualización usarías en cada caso?_

- __Alojamiento de varios clientes en un servidor__: Utilizaría una __virtualización a nivel de sistema operativo__ para que los clientes compartieran el _SO_ a la vez que cada uno estuviera aislado de los demás.
- __Sistema web + middleware + BD__: En este caso utilizaría una __virtualización plena__ para separar este sistema completamente del resto.
- __Sistema de prueba de software e integración continua__: Para este supuesto elegiría una __virtualización de entornos de desarrollo__ para reproducir de la manera más precisa posible entornos concretos.

## Ejercicio 4
_Hacer el [tutorial de línea de órdenes de docker](https://www.docker.com/tryit/) para comprender cómo funciona._

1. `~$ docker version`
2. `~$ docker search tutorial`
3. `~$ docker pull learn/tutorial`
4. `~$ docker run learn/tutorial echo "hello world"`
5. `~$ docker run learn/tutorial apt-get install -y ping`
6.
  + `~$ docker ps -l`
  + `~$ docker commit 698 learn/ping`
7. `~$ docker run learn/ping ping www.google.com`
8. `~$ docker inspect efe`
9. `~$ docker push learn/ping`

## Ejercicio 5
_Instala el sistema de gestión de fuentes **git**._

En Ubuntu se instala con la orden `sudo apt-get install git`.

## Ejercicio 6
1. _Crear un proyecto y descargárselo con git. Al crearlo se marca la opción de incluir el fichero README._
2. _Modificar el readme y subir el fichero modificado._

-  Creamos el proyecto desde la web de GitHub y pinchamos en la casilla de que nos dice si queremos incluir un README.
   A continuación, en nuestro ordenador, ejecutamos `git clone https://github.com/antorof/nombre-del-proyecto.git`.
-  Ya en nuestra máquina podemos modificar el README con un editor de texto. Despues confirmamos los cambios con
`git commit -a .m "mensaje del commit"` y los subimos con `git push origin master`.

## Ejercicio 7
_Comprobar si en la instalación hecha se ha instalado cgroups y en qué punto está montado, así como qué contiene._

En mi instalación de linux (Ubuntu 14.04) se encuentra en `/sys/fs/cgroup` y contiene una sola carpeta llamada `systemd`.

## Ejercicio 8
1. _Crear diferentes grupos de control sobre un sistema operativo Linux._
   _Ejecutar en uno de ellos el navegador, en otro un procesador de textos y en uno último cualquier otro proceso._      _Comparar el uso de recursos de unos y otros durante un tiempo determinado._
2. _Calcular el coste real de uso de recursos de un ordenador teniendo en cuenta sus costes de amortización._
   _Añadir los costes eléctricos correspondientes._

- Voy a la carpeta de `cgroup` (`/sys/fs/cgroup/`) y creo los grupos con `mkdir grupoff`, `mkdir grupotxt	`, `mkdir grupoaux`.
   _Se ve que no se crean los grupos y no me sale nada en las carpetas.
   Tampoco me deja lanzar los programas con `cgexec`_.
- _No he podido realizarlo, al igual que el apartado anterior_.

## Ejercicio 9
1. ~~Discutir diferentes escenarios de limitación de uso de recursos o de asignación de los mismos a una u otra CPU.~~
2. Implementar usando el fichero de configuración de `cgcreate` una política que dé menos prioridad a los procesos de usuario que
a los procesos del sistema (o viceversa).
3. Usar un programa que muestre en tiempo real la carga del sistema tal como `htop` y comprobar los efectos de la migración en tiempo
real de una tarea pesada de un procesador a otro (si se tiene dos núcleos en el sistema).
4. Configurar un servidor para que el servidor web que se ejecute reciba mayor prioridad de entrada/salida que el resto de los usuarios.

- ### Apartado 2
  > [DavidGSola](https://github.com/DavidGSola) dijo:

  > Te pongo un enlace por si te ayuda para hacer este ejercicio. [Link](http://docs.oracle.com/cd/E37670_01/E37355/html/ol_use_cases_cgroups.html)

  Con la ayuda del [enlace](http://docs.oracle.com/cd/E37670_01/E37355/html/ol_use_cases_cgroups.html), que son unos **casos de uso** de *Oracle*, asignamos baja prioridad al grupo "usuarios".

  ```
  mount {
  	cpu = /sys/fs/cgroup/cpu
  }

  group usuarios {
  	cpu {
  		cpu.shares="250";
  	}
  }

  group sistema {
  	cpu {
  		cpu.shares="750";
  	}
  }
  ```

## Ejercicio 10
_Comprobar si el procesador o procesadores instalados tienen estos_ flags. _¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden?_

- Procesador: __Intel(R) Core(TM) i3-3110M CPU @ 2.40GHz__ (máquina virtual)
- Salida de `flags`: `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss ht syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf eagerfpu pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt xsave avx f16c hypervisor lahf_lm arat epb xsaveopt pln pts dtherm fsgsbase smep`

## Ejercicio 11
_Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden `kvm-ok`._

El comando `kvm-ok` devuelve:

```
INFO: Your CPU does not support KVM extensions
INFO: For more detailed results, you should run this as root
HINT:   sudo /usr/sbin/kvm-ok
```

## Ejercicio 12
_Comentar diferentes soluciones de Software as a Service de uso habitual_

Son aplicaciones a las que accedemos por internet, y en la actualizad utilizamos Saas a diario, muchas veces sin tener constancia, ya que lo vemos cada vez más normal, pudiendo empezar por Gmail.
Existen muchas otras, como los editores de texto y de hojas de cálculo de Google Drive, Google calendar, Outlook.com, Yahoo! Mail, Hangouts, PDFscape (editor online de pdf), Autocad360...






Creando aplicaciones en la nube: Uso de PaaS y SaaS
===================================================

## Ejercicio 1
_Instalar un entorno virtual para tu lenguaje de programación favorito (uno de los mencionados arriba, obviamente)._

He elegido instalar un entorno virtual para __python__.

Para poder hacerlo he tenido que instalar primero _pip_. Se instala en Ubuntu con `sudo apt-get install python-pip`.

Después instalo el entorno: `sudo pip install virtualenv`

También he instalado _nodeenv_ para __NodeJS__: `sudo pip install nodeenv`

## Ejercicio 2
_Darse de alta en algún servicio PaaS tal como Heroku, Nodejitsu u OpenShift._

Registrado en _Openshift_ y _Heroku_.

## Ejercicio 3
_Crear una aplicación en OpenShift y dentro de ella instalar WordPress._

Creada y en marcha en https://wordpress-tfgos2.rhcloud.com/

## Ejercicio 4
_Crear un script para un documento Google y cambiarle el nombre con el que aparece en el menú, así como la función a la que llama._

Script creado: https://script.google.com/d/1CDot9JH09oTQa2WqSPx0kZmVN3wZ3TT8-ZZfCfMier6Gnh9sk9gdaQVK/edit?usp=sharing

## Ejercicio 5
_Buscar un sistema de automatización de la construcción para el lenguaje de programación y entorno de desarrollo que usemos habitualmente._

Aunque ya no lo empleo habitualmente, he utilizado **make** para C/C++. [Makefile](http://mrbook.org/tutorials/make/)

## Ejercicio 6
_Identificar, dentro del PaaS elegido o cualquier otro en el que se dé uno de alta, cuál es el fichero de automatización de
construcción e indicar qué herramienta usa para la construcción y el proceso que sigue en la misma._

(En _OpenShift_ se puede configurar el proceso de construcción de las aplicaciones mediante _Jenkins_.
El proceso de construcción comienza cuando el usuario realiza un `git push` hacia el repositorio de la aplicación
en _OpenShift_. Después, se realiza la construcción de la aplicación (que se puede personalizar con _Jenkins_).

Se puede ver de manera resumida en el [workflow de OpenShift](https://www.openshift.com/walkthrough/developer-workflow), y
más explicada [aquí](https://www.openshift.com/products/architecture).) <- Esto no es

## Ejercicio 7
_Buscar un entorno de pruebas para el lenguaje de programación y entorno de desarrollo que usemos habitualmente._

Para __NodeJS__ se pueden realizar test unitarios con [__Nodeunit__](https://github.com/caolan/nodeunit). También se pueden utilizar
una serie de herramientas, para realizar muchos tipos de pruebas, que están muy bien descritas [aquí](http://www.clock.co.uk/blog/tools-for-unit-testing-and-quality-assurance-in-node-js)

Para __python__ se puede utilizar el módulo __unittest__. [Aquí](http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html) se
puede ver un tutorial de TDD con __unittest__.

Para __Java__ existe __JUnit__, que nos permite la realización de test unitarios.






Técnicas de virtualización
==========================

## Ejercicio 1
_Crear un espacio de nombres y montar en él una imagen ISO de un CD de forma que no se pueda leer más que desde él._
Pista: _en [ServerFault](http://serverfault.com/questions/198135/how-to-mount-an-iso-file-in-linux) nos explican como
hacerlo, usando el dispositivo loopback._

He cogido una ISO que tenía y que he renombrado a _miiso.iso_.

Ahora creo un punto de montaje: `sudo mkdir /mnt/pto-montaje`.

Por último, para montar la imagen en su lugar utilizo la orden `sudo mount -o loop ~/Desktop/miiso.iso /mnt/pto-montaje`.

## Ejercicio 2
1. _Mostrar los puentes configurados en el sistema operativo._
2. _Crear un interfaz virtual y asignarlo al interfaz de la tarjeta wifi, si se tiene, o del fijo, si no se tiene._

- Uso `brctl show` para mostrar los puentes.

    ```
    bridge name     bridge id           STP enabled   interfaces
    ```
- Ahora creo un interfaz virtual con `sudo brctl addbr mipuente` y lo uno con `eth0` mediante `sudo brctl addif mipuente eth0`.

    ```
    bridge name     bridge id           STP enabled   interfaces
    mipuente        8000.000c2993c762   no            eth0
    ```






Virtualización ligera usando contenedores
=========================================

## Ejercicio 1
_Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en [GitHub](http://github.com/lxc/lxc)
como en el [sitio web](http://linxcontainers.com/) está bastante más avanzada; para evitar problemas sobre todo con las herramientas que
vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0._

Instalo LXC con `sudo apt-get install lxc` ya que se instala la versión 1.0.6 (>1.0).

## Ejercicio 2
_Comprobar qué interfaces puente se han creado y explicarlos._

Creamos un contenedor con `sudo lxc-create -t ubuntu -n una-caja`.

Una vez instalado vemos las interfaces puente creadas con `brctl show`, que nos muestra:
```
bridge name     bridge id           STP enabled   interfaces
lxcbr0          8000.000c2993c762   no            eth0

```

## Ejercicio 3
 - _Crear y ejecutar un contenedor basado en Debian._
 - _Crear y ejecutar un contenedor basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya. Fedora, al parecer, tiene problemas si estás en Ubuntu 13.04 o superior, así que en tal caso usa cualquier otra distro. Por ejemplo, Óscar Zafra ha logrado instalar Gentoo usando un script descargado desde su sitio, como indica en este comentario en el issue._

1. Ya he instalado anteriormente un contenedor con ubuntu y otro con ubuntu-cloud.
2. He instalado gentoo amd64 mediante el script provisto.

## Ejercicio 4
 - _Instalar lxc-webpanel y usarlo para arrancar, parar y visualizar las máquinas virtuales que se tengan instaladas._
 - _Desde el panel restringir los recursos que pueden usar: CPU shares, CPUs que se pueden usar (en sistemas multinúcleo) o cantidad de memoria._

1. En mi máquina, para ver por consola la lista de las máquinas virtualies emplear la orden `sudo lxc-ls -f` en vez de `sudo lxc-list`.

   Para utilizar _lxc-webpanel_ podemos descargar un script de la página de _lxc-webpanel_ en _github_ y ejecutarlo. Podemos hacerlo todo a la vez ejecutando en la consola, __siendo root__, lo siguiente: `wget http://lxc-webpanel.github.com/tools/install.sh -O - | bash`.

   El usuario y la clave por defecto son `admin` - `admin` y se despliega en http://localhost:5000.

2. En el panel _lxc-webpanel_, a la izquierda donde están los contenedores, si pinchamos en uno de ellos se pueden modificar algunos parámetros de configuración y los recursos de los mismos.

## Ejercicio 5
_Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx._


## Ejercicio 6
 - _Instalar juju._
 - _Usándolo, instalar MySQL en un táper._

1. Para instalarlo, primero tenemos que añadir el repositorio de _juju_ con la orden `sudo add-apt-repository ppa:juju/stable
sudo apt-get update`. Después lo instalamos con `sudo apt-get install juju-core`.

2. Creo un táper con `juju bootstrap`.

    Instalamos _mysql_ medianet la orden `juju deploy mysql`.

    Si ejecuto `juju status` se puede ver lo siguiente:
    ```
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
        agent-state: stopped
        agent-version: 1.20.14.1
        dns-name: 10.0.3.124
        instance-id: antonio-local-machine-1
        life: dead
        series: trusty
        hardware: arch=amd64
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

## Ejercicio 7
 - _Destruir toda la configuración creada anteriormente._
 - _Volver a crear la máquina anterior y añadirle mediawiki y una relación entre ellos._
 - _Crear un script en shell para reproducir la configuración usada en las máquinas que hagan falta._

1. Destruimos la configuración (_mysql_ y la máquina):
    - `sudo juju destroy-unit mysql/0`
    - `sudo juju destroy-machine 1`

2. Creamos la máquina con `sudo juju add-machine`.

    Ahora añadimos _mediawiki_ y la relación entre ellos (_mysql_ ya está de antes).

    `juju deploy mediawiki`

    `juju add-relation mediawiki:db mysql`

3. El script contendría las ordenes anteriores:
    ```shell
    #!/bin/bash

    juju deploy mediawiki
    juju deploy mysql
    juju add-relation mediawiki:db mysql
    ```

## Ejercicio 8
_Instalar libvirt. Te puede ayudar [esta guía para Ubuntu](https://help.ubuntu.com/12.04/serverguide/libvirt.html)._

Mi ordenador no soporta la virtualización. Si lanzo `kvm-ok` el resultado es:
```
INFO: Your CPU does not support KVM extensions
KVM acceleration can NOT be used
```
No obstante, lo que tendría que haccer es `sudo apt-get install kvm libvirt-bin`.

## Ejercicio 9
_Instalar un contenedor usando virt-install._

No puedo realizarlo ya que mi ordenador no soporta la virtualización.

Por eso copio aquí lo que ha hecho mi compañero [Jorge González](https://github.com/Georgevik/):
>`sudo apt-get install virtinst`
>
>Con este comando podemos instalar maquinas virtuales directamente. Para ello necesitamos una iso con el
>sistema operativo de la maquina virtual. En este caso hemos cogido el de Ubuntu 14.04 y con la siguiente
>orden creamos la maquina:
>`sudo virt-install -n virt-ubuntu -r 512 --disk path=/var/lib/libvirt/images/ubuntuvirtual.img,bus=virtio,size=5 -c /home/georgevik/Escritorio/ubuntu-14.04.iso --accelerate --network network=default,model=virtio --connect=qemu:///system --vnc --noautoconsole -v`
>```
>Empezando la instalación...
>Creando dominio...                                       |    0 B     00:01
>La instalación del dominio continúa en progreso. Puede reconectarse a
>la consola para completar el proceso de instalación.
>```

>Vemos como se ha creado correctamente la máquina virtual y se encuentra en ejecución
>```
>georgevik@georgevik-K52JK:~$ sudo virsh -c qemu:///system list
>Id    Nombre                         Estado
>----------------------------------------------------
>5     virt-ubuntu                    ejecutando
>```

## Ejercicio 10
_Instalar docker._

Instalamos _docker_ con `sudo apt-get install docker.io`.

Ya instalado, para lanzarlo lo único que tendremos que hacer es `sudo docker -d &`.

## Ejercicio 11
+  _Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS._
+  _Buscar e instalar una imagen que incluya MongoDB._

1. Voy a instalar la imagen de __Ubuntu__ de __partlab__, para eso utilizo la orden `sudo docker pull partlab/ubuntu`.
   ```
   Pulling repository partlab/ubuntu
   220f670a5152: Pulling image (latest) from partlab/ubuntu, endpoint: https://regi220f670a5152: Download complete
   511136ea3c5a: Download complete
   ef3ba9f35b97: Download complete
   36accde0a93b: Download complete
   ea198eaf8e7b: Download complete
   cfaba6b5fefe: Download complete
   7c25df13077f: Download complete
   fed5a2d85e04: Download complete
   14b33c345a2d: Download complete
   693448329de2: Download complete
   564941eb5df8: Download complete
   ```
   También voy a instalar __CentOS 5.11__ mediante `sudo docker pull centos:5.11`.
   ```
   Pulling repository centos
   c36ca560b9bf: Pulling image (5.11) from centos, endpoint: https://registry-1.docc36ca560b9bf: Download complete
   511136ea3c5a: Download complete
   5b12ef8fd570: Download complete
   ```
2. Ahora instalamos una imagen con __MongoDB__ con `sudo docker pull dockerfile/mongodb`.
   ```
   Pulling repository dockerfile/mongodb
   e8ddda3ca0be: Download complete
   511136ea3c5a: Download complete
   27d47432a69b: Download complete
   5f92234dcf1e: Download complete
   51a9c7c1f8bb: Download complete
   5ba9dab47459: Download complete
   5ac964b38b8b: Download complete
   8a75beb8c617: Download complete
   c240f95f9ab0: Download complete
   ed8bb587e39a: Download complete
   69151129842b: Download complete
   f89142985c75: Download complete
   e7fc98dc1b07: Download complete
   2de84ece3e3a: Download complete
   a4b705c39ab0: Download complete
   a7d5be1aea27: Download complete
   b22473a839df: Download complete
   2c0a430f3535: Download complete
   ```
