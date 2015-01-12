Ejercicio Jorge Gonzalez Peregrin
=================================

## 17-oct-2014

### Ejercicio 1

https://www.mountain.es/servidores/zircon-40
**Precio**
Con IVA: 1919€
Sin IVA: 1585,95€

**Amortizacion**
Cuatro años: 396,49€ por año
Siete años: 226,56€ por año

### Ejercicio 2
Se van a comparar un servidor VPS de **1&1 Hosting** con un servidor cloud de **Google Compute Ingine**. Elegimos dos servidores de caracteristicas parecidas y hacemos los siguientes calculos

La instancia de Google es la **n1-standard-1**
El servido VPS de de 1&1 Hosting equivalente sería el **Servidor Virtual XL** 

Teniendo esto en cuenta realizamos los calulos para
**1%**
- Google: 87,6h * 0.0551€/h = 4,83€
- 1&1 Hosting: 20€/mes * 12 meses = 240€
- 1&1 Hosting: 10€/mes * 12 meses = 120€ (con la oferta del primer año de descuento)

**10%**
- Google: 876h * 0.0551€/h = 48.34 €
- 1&1 Hosting: 20€/mes * 12 meses = 240€
- 1&1 Hosting: 10€/mes * 12 meses = 120€ (con la oferta del primer año de descuento)

### Ejercicio 3

1. Alojar varios clientes en un sólo servidor. Utilizaria un sistema de virtualizacion a nivel de sistema operativo para que cada cliente pudiese realizar sus tareas independientemente del número de clientes alojados en el servidor, ya que estos se encuentran aislados unos de otros.

2. Crear un sistema eficiente de web + middleware + base de datos. Utilizaría un sistema de virtualización pleno porque me permitirá virtualizar un sistema completo. Gracias a los programas de control se abarcarían las necesidades de crear un sistema web, middleware y una base de datos. 

3. Sistema de prueba de software de integración continua. La virtualización de entornos de desarrollo nos permitiría abordar el supuesto sistema, ya que nos facilita la labor de verificación de una aplicación en distintas versiones con una sola orden, así como, reescribirlo en diferentes lenguajes.

### Ejercicio 4

Para realizar el ejercicio se han introducido dentro del simulador, se han seguido los siguientes:
> docker version
> docker search tutorial
> docker pull learn/tutorial
> docker run learn/tutorial apt-get install -y ping
> docker ps -l
> docker commit 6982 learn/ping
> docker ps -l
> docker run learn/ping ping google.com
> docker ps -l
> docker inspect efe

### Ejercicio 5

Se ha instalado el sistema de gestión de fuentes git con el commando:
- sudo apt-get install git

### Ejercicio 6

Para realizar este ejercicio se han seguido las siguientes órdenes.
> He creado en GitHub un nuevo repositorio con el nombre "MiProyecto" junto con el archivo README
> git clone https://github.com/Georgevik/MiProyecto.git
> cd MiProyecto
> gedit README.md
> git commit -m "Primera modificacion"

### Ejercicio 7
> apt-get install cgroup-lite
> ls blkio cpuacct devices hugetlb perf_event cpu cpuset freezer memory systemd

### Ejercicio 8

No he podido realizarlo porque al intentar montar el cgroup me dice que ya se encuentra montado y no me crea los subdirectorios que debería.


#####Corrección de Daniel Díaz Salas

A mí tambien me pasaba esto. En Ubuntu se montan por defecto en _/sys/fs/cgroup_. Mira a ver si tienes todos los subdirectorios ahí.


### Ejercicio 9
**Parte 1**
La limitacion de recursos o de asignación puede ser muy útil en el momento en el que tenemos que tenemos que modificar partes de un servicio que no puede pararse. Podemos poner por ejemplo un servidor que esta dando soporte a aplicaciones Android. Es clave que el servicio no se interrumpa, sin embargo podemos realizar tareas bajando el rendimiento a este servicio. De este modo, podemos modificar la parte del servidor necesaria sin tener que interrumpir el servicio.

Otro escenerio es cuando dos usuarios interactúan con los recursos de un mismo ordenador. Esto permite que ambos usuarios puedan trabajar sin "molestarse" entre ellos.

Tambien es util en el momento de proveer una granja de hosting. Con un solo ordenador particionamos los recursos y se lo vendemos a los clientes.

**Parte 2**

No he podido hacer el ejercicio ya que no me deja montar el cgroup. No obstante, en teoria una vez creado los procesos, la prioridad se estableceria de la siguiente forma en el fichero "cgconfig.conf"
```
group procesos_usuario{ 
    cpu{
       cpu.shares = "200"; 
    } 
 } 
group procesos_sistema{ 
    cpu{ 
       cpu.shares = "800"; 
    }
}
```
**Parte 3, 4**

No he podido realizarlo por el problema que he tenido en el Ejercicio 8.


### Ejercicio 10

El modelo de procesador es: Intel(R) Core(TM) i5-3427U CPU @ 1.80GHz

La salida que obtengo con el comando es:
```
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor **vmx** ds_cpl smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm ida arat xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms
```
Como podemos ver, mi procesador tiene activado el flag de vmx

### Ejercicio 11

He tenido que instalar el paquete cpu-checker y la salida al comando "kvm-ok" es la siguiente:
```
INFO: /dev/kvm exists
KVM acceleration can be used
```
### Ejercicio 12

Un ejemplo claro de de SaaS son los servicios de correo como Gmail, Yahoo o Hotmail. Además de servicios de correo electrónico tambien herramientas como Drive o incluso Dropbox, en algunos aspectos, también podemos considerarlo ejemplos de servicios SaaS de almacenamiento en la "nube".

Últimamente se han añadido servicios SaaS para la generación de documentos en línea como puede ser GitHub o para la gestión de nominas como los distintos ERP

## Creando aplicaciones en la nube: Uso de PaaS y SaaS

### Ejercicio 1
Se va a instalar un entrono virtual para Python. Para ello, se han utilizado los siguientes comandos
> sudo apt-get install python-pip
> sudo pip install https://github.com/pypa/virtualenv/tarball/develop
> sudo apt-get install curl
> curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz
> tar xvfz virtualenv-1.9.tar.gz
> cd virtualenv-1.9
> sudo python setup.py install

Ejecutamos el entorno usando
> virtualenv ENV
y creamos el ejecutable 
```
New python executable in ENV/bin/python
Installing setuptools............done.
Installing pip...............done.
```

### Ejercicio 2
Me he registrado en **Heroku**

### Ejercicio 3
Me he registrado en **OpenShift**
Nos logueamos en la cuenta y seleccionamos la opción de **WordPress 4** en el submenu de "Instant App"
Introducimos en el browser la siguiente dirección e instalamos WordPress
- php-manoletes.rhcloud.com

Rellenamos la información, necesaria y accedemos a nuestro WordPress. Podemos loguearnos en el WordPress pinchando [aqui](https://php-manoletes.rhcloud.com/wp-login.php) o visitar la página en este [enlace](http://php-manoletes.rhcloud.com/). Una vez logueados ya estamos en dispositición de gestionar y personalizar nuestro WordPress

### Ejercicio 4
Nos vamos a la web https://script.google.com/
Una vez dentro, indicamos que vamos a realizar un script para "Documents". Ahí, cambiamos el nombre del proyecto y seleccionamos, por ejemplo, la función "showAlert".

### Ejercicio 5
Un sistema de automatización de la contrucción de ficheros C/C++ sería **make**.
Como entorno de desarrollo uso habitualmente NetBeans o AndroidStudio

### Ejercicio 6
El PaaS elegido es **Heroku** y hemos seleccionado una aplicación en PHP. Como podemos ver [aqui](https://devcenter.heroku.com/articles/getting-started-with-php#declare-app-dependencies) nos indica que se necesita un archivo llamado **composer.json** que se encarga de analizar las dependencias para poder construir el fichero.

### Ejercicio 7
Tanto en NetBeans, Eclipse o Android Studio que son los entornos de desarrollo con los que trabajo usualmente, he estado como sistema de tester JUnit 4 sobre Java. Con el entorno de desarrollo Xcode para iOS también he utilizado el sistema de testeo TDD pero en menor medida


## Técnicas de virtualización

### Ejercicio 1
Entramos en un espacio de nombres con las siguientes sentencias
> sudo unshare -u /bin/bash
> hostname manolete

Creamos la ISO con el siguiente comando
> genisoimage -o myISO.iso text_iso.md 

Montamos la ISO con loopback 
> mkdir /mnt/myfolder/
> mount -o loop myISO.iso /mnt/myfolder/

### Ejercicio 2
#### 2.1
Vemos los puentes del sistema operativo con:
> ip addr show

#### 2.2
Creamos una interfaz virtual
> sudo brctl addbr manolete

Lo asignamos
> sudo brctl addif manolete wlan0

Al ejecutar la sentencia me indica que la operación no se puede realizar. Puede deberse a que se a que actualmente estoy utilizando dicha red. No puedo hacerle el bridge a otra red puesto que no tengo, ni siquiera la eth0

## Virtualización ligera usando contenedores

### Ejercicio 1
Se ha descargado e instalado la version 1.0.6 de [aqui](https://linuxcontainers.org/downloads/)
Seguimos las instrucciones del archivo INSTALL para instal LXC

### Ejercicio 2
Comprobamos las interfaces con
> ifconfig

Y vemos la nueva interfaz "lxcbr0". 

### Ejercicio 3
#### Ejercicio 3.1
Se ha instalado un ubuntu con la siguiente orden
> sudo lxc-create -t ubuntu -n micaja
> sudo lxc-start -n micaja

#### Ejercicio 3.2
Se ha instalado un fedora con la siguiente orden
> sudo lxc-create -t fedora -n mifedora
> sudo lxc-start -n mifedora

###Ejercicio 4
#### Ejercicio 4.1
Entramos como root con "sudo su" e instalamos con la sentencia "wget http://lxc-webpanel.github.io/tools/install.sh -O - | bash"

Entramos en el panel abriendo un browser con la direccion "http://localhost:5000/"

#### Ejercicio 4.2
![Imgur](http://i.imgur.com/h4KznGe.png)

###Ejercicio 5
Para un servidor web, la virtualización en jaulas puede resultar un tanto restrictivo, puesto que no se puede realizar nada sobre tu servidor que no este ya. Es decir, debido al tipo de virtualización la configuración que posea la jaula es la que tendrá el servidor web, por tanto, si se quieren instalar cosas nuevas o cambiar puertos este tipo de virtualización nos vendría demasiado limitada. Las jaulas se pueden utilizar como servicio web cuando no necesitamos en nuestro servicio web más allá de un Apache y una base de datos MySQL. En el momento que queramos modificar algo más interno las necesitamos pasarnos a contenedores.

Como servidor web, un contenedor puede ser util para albergar jaulas. Este negocio parte de comprar nosotros un contenedor en un servidor, de manera que podamos crear jaulas dentro de él y venderlas. Esto se debe a que este tipo de virtualización se enceuntra sobre el Sistema Operativo, por lo que nos permite instalar programas con libertad.


###Ejercicio 6
#### Ejercicio 6.1
Los pasos que he seguido para instalar juju han sido:
>sudo apt-get install juju
>sudo add-apt-repository ppa:juju/stable
>sudo apt-get update && sudo apt-get install juju-core
>sudo apt-get install juju-local

#### Ejercicio 6.2
Instalamos MySQL primero inicializacon del taper 
>juju bootstrap
y luego desplenado un MySQL
>juju deploy mysql 
Comprobamos que hemos instalado MySQL con:
>juju status
```shell
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
    charm: cs:trusty/mysql-14
    exposed: false
    relations:
      cluster:
      - mysql
    units:
      mysql/0:
        agent-state: pending
        machine: "1"
```

###Ejercicio 7
#### Ejercicio 7.1
>sudo juju destroy-unit mysql/0
>sudo juju destroy-machine 1
Si volvemos a hacer juju status vemos que hemos eliminado todo
```
georgevik@georgevik-K52JK:~$ juju status
environment: local
machines:
  "0":
    agent-state: started
    agent-version: 1.20.14.1
    dns-name: localhost
    instance-id: localhost
    series: trusty
    state-server-member-status: has-vote
services:
  mysql:
    charm: cs:trusty/mysql-14
    exposed: false
    relations:
      cluster:
      - mysql
```
#### Ejercicio 7.2
>juju deploy mysql
>juju deploy mediawiki
>juju add-relation mediawiki:db mysql
#### Ejercicio 7.3

### Ejercicio 8
>sudo apt-get install kvm libvirt-bin
>sudo adduser $USER libvirtd

### Ejercicio 9
>sudo apt-get install virtinst
Con este comando podemos instalar maquinas virtuales directamente. Para ello necesitamos una iso con el sistema operativo de la maquina virtual. En este caso hemos cogido el de Ubuntu 14.04 y con la siguiente orden creamos la maquina:
>sudo virt-install -n virt-ubuntu -r 512 --disk path=/var/lib/libvirt/images/ubuntuvirtual.img,bus=virtio,size=5 -c /home/georgevik/Escritorio/ubuntu-14.04.iso --accelerate --network network=default,model=virtio --connect=qemu:///system --vnc --noautoconsole -v

```
Empezando la instalación...
Creando dominio...                                       |    0 B     00:01     
La instalación del dominio continúa en progreso. Puede reconectarse a 
la consola para completar el proceso de instalación.
```

Vemos como se ha creado correctamente la máquina virtual y se encuentra en ejecución
```
georgevik@georgevik-K52JK:~$ sudo virsh -c qemu:///system list
 Id    Nombre                         Estado
----------------------------------------------------
 5     virt-ubuntu                    ejecutando
```

### Ejercicio 10
El siguiente enlace muestra los pasos para instalar Docker en Ubuntu. https://docs.docker.com/installation/ubuntulinux/
En nuestro caso, hemos utilizado los pasos para ubuntu 14.04 
>sudo apt-get install docker.io
>source /etc/bash_completion.d/docker.io
>echo deb https://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list
>apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
>apt-get update
>apt-get install -y lxc-docker

Con esto ya tenemos listo el docker para usarse. Con el siguiente comando ejecutamos el docker:
>sudo docker -d &

### Ejercicio 11
#### Ejercicio 11.1
Instalamos las dos imagene con los siguientes comandos
>sudo docker pull ubuntu
>sudo docker pull centos

Y nos devuelve salida de este tipo para ambos comandos
```
209ea56fda6d: Download complete 
607c5d1cca71: Download complete 
dbbd544a49e2: Download complete 
f62feddc05dc: Download complete 
98b540cf0569: Download complete 
ef70b517e969: Download complete 
dfaad36d8984: Download complete 
```

#### Ejercicio 11.2
Para instalar MongoDB utilizaremos la imagen de **codiez/mongodb** que se instala de la misma manera que ubuntu y centOS montrando como resultado la siguiente salida:
```
508e0c005e19: Pulling dependent layers 
8dbd9e392a96: Download complete 
f0ab8043e4e8: Downloading 9.709 MB/426.3 MB 11m37s
```
