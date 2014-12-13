# Introducción a la infraestructura virtual: concepto y soporte físico

__Ejercicio 1__

La máxima amortización sería del 25%. Luego si tenemos un servidor de 7500 € sin IVA, a 4 años sería por año unos 1875 €.

Si queremos que sea a 7 años tendriamos, variando el porcentaje de amortización (opcional), entonces por ejemplo:
1. el primer año el 20%: 1500.0 €.

2. el segundo año el 15%: 1125.0 €.

3. el tercer año el 10%: 750.0 €

4. el cuarto y el quito al 15%: 1125.0 €
(Lo que hace un total de 5625.0 €)

5. el sexto año al 20% con un total de 7125.0 €.

6. y el último año al 5% con una suma de 375.0 €
.........
---------

__Ejercicio 2__

Podemos encontrar:
- **City Network (Servidor Cloud):** 0.11 $ / hora.
- **AWS | Amazon EC2 (m3.medium):**  0.07 $ / hora.

Un año tiene 24 h/dia * 365 dia/año = **8760 horas / año**

Por un lado al *1%* tenemos:
- **City Network (Servidor Cloud):** 0.11 $ / hora * 0.01 * 8760 horas = **9.636 $**
- **AWS | Amazon EC2 (m3.medium):** 0.07 $ / hora * 0.01 * 8760 horas = **6.132 $**

Por otro lado al *10%* sería:
- **City Network (Servidor Cloud):** 0.11 $ / hora * 0.1 * 8760 horas = **96.36 $**
- **AWS | Amazon EC2 (m3.medium):** 0.07 $ / hora * 0.1 * 8760 horas = **61.32 $**


**Referencias:**

  * https://www.citynetwork.es/
  * http://aws.amazon.com/es/ec2/pricing/

.........
---------
__Ejercicio 3__

- **Alojamiento de varios clientes en un servidor:**
Optaría por la *virtualización a nivel de sistema operativo* ya que con esta opción la capa de virtualización se ejecuta como una aplicación en el sistema operativo. De este modo el núcleo del sistema operativo se ejecuta sobre el nodo de hardware con varias máquinas virtuales invitadas aisladas puesto que están instaladas sobre el mismo. De esta manera no hay sobrecarga alguna asociada con tener a cada huésped ejecutando un sistema operativo totalmente instalado. Mejorando así el rendimiento.
- **Sistema *web + middleware + BD*:**
Escogería la *virtualización completa*, esta opción no necesita de modificaciones en el sistema operativo host. Se vale de traducción binaria combinando con la ejecución directa. El sistema opertavido se desacopla en su totalidad del hardware que hay por debajo.
- **Prueba de software e integración continua:**
Elegiría la *virtualización por entornos de desarrollo* ya que nos permite reproducir entornos lo más similar que puede. Se pueden realizar distintas ejecuciones de multiples aplicaciones en distintos lenguajes.

.........
---------
__Ejercicio 4__

Lista de comandos realizados:
- docker version
- docker search tutorial
- docker run learn/tutorial echo "Hello world!"
- docker run learn/tutorial apt-get install -y ping
- docker commit 698 learn/ping
- docker run learn/ping ping google.com
- docker inspect efe
- docker push learn/ping

Resultado final:



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

.........
---------
__Ejercicio 5__

Instalado con el siguiente comando desde la shell de Ubuntu:
> sudo apt-get instal git

.........
---------
__Ejercicio 6__

Descargamos el repositorio a nuestro ordenador con la siguiente orden:
> git clone https://github.com/eleion/CloudComputing

Una vez realizadas todas las modificaciones a un fichero, se ejecuta el siguiente comando:
> git add .

Se puede comprobar el estado del respositorio por si hemos cambiado algo con:
> git status

Veremos que lo que hemos modificado aparece en la salida del anterior comando. A continuación utilizamos el comando:
> git commit

Para hacer válido el cambio. Y por último utilizamos:
> git push origin master

Este útlimo comando nos permite subirlo al repositorio original.

.........
---------
__Ejercicio 7__

Una vez instalado el `cgroup-lite`, enn la carpeta `/sys/fs/cgroup` podemos encontrar el siguiente contenido:
`blkio, cpu, cpuacct, cpuset, devices, freezer, hugetlb, memory, perf_event, systemd`

.........
---------
__Ejercicio 8__

Al crear el directorio no se genera automáticamente los subdirectorios que deberían, luego esta parte no se ha podido realizar.

He estado mirando distintas páginas pero no ha habido manera posible de encontrar el fallo, por ejemplo se ha intentado seguir también esta página:

  * http://www.janoszen.com/2013/02/06/limiting-linux-processes-cgroups-explained/
  * http://linuxaria.com/article/introduction-to-cgroups-the-linux-conrol-group

Corrección: Me sucedía el mismo problema. En ubuntu 14.04 parece ser que se tiene que instalar cgroup-bin y crear los frupos usando el comando cgcreate.
Por ejemplo, el ejercicio se haría:
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

.........
---------
__Ejercicio 9__

**Corrección del ejercicio.**

1. Es interesante limitar los recursos para evitar modificaciones de un servicio establecido para no realizar ningún *halt* en la misma. Se podría establecer un servidor para dar servicio a aplicaciones IOS. Para ello es imporante no interrumpir la ejecución de la aplicación.

2. También en la interacción de varios usuario que hacen uso de una serie de recursos compartidos. De esta forma el trabajo de ambos usuarios se realiza interrumpidamente.

__Ejercicio 9.2__

Una vez creado el archivo de configuración `/etc/cgconfig.conf`. Se podría dar priorirdad a los procesos de la siguiente manera:

```
mount { cpu = /cgroup/cpu }
group my_user { cpu { cpu.shares = "500"; } }
group my_user2 { cpu { cpu.shares = "400"; } }
```

.........
---------
__Ejercicio 10__

Para ver el modelo del procesador podemos ir a `/proc/cpuinfo` y allí lo tenemos.

* **Modelo del procesador:** Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz.
* **Salida del comando:** ```flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm ida arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid```

.........
---------
__Ejercicio 11__

Comprobamos si está instalado `kvm-ok` y nos dice en este caso que no: `El programa «kvm-ok» no está instalado. Puede instalarlo escribiendo: sudo apt-get install cpu-checker`

.........
---------
__Ejercicio 12__

El _software como servicio (SaaS)_ es un modelo de soporte lógico. El cliente accede a un servidor por medio de Internet y este servidor se encarga del mantenimiento y soporte del software que el cliente utiliza. Con el modelo _SaaS_ el cliente se despreocupa de instalaciones, configuraciones, etc.

Ejemplos podrían ser _Google Apps, Microsoft Office 365, Gmail, Yahoo mail..._ Puesto que todos estos servicios se encuentran hospedados en un servidor que no es el nuestro y nosostros accedemos sin necesidad de instalar nada a estas aplicaciones mediante Internet.



-------------

# Creando aplicaciones en la nube: Uso de PaaS y SaaS

- - -
## Ejercicio 1.

Se ha instalado el entorno virtual **virtualenv para Python**. Mediante el comando:

> sudo apt-get install python-virtualenv

Para generar un proyecto se usa la siguiente instrucción:

> virtualenv <NOMBRE>

- - -
## Ejercicio 2.

Me he dado de alta en **Heroku**. Y lo he instalado en Ubuntu para poder ejecutar comandos desde la línea de ordenes con el siguientes comando:

> wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

- - -
## Ejercicio 3.

Como he elegido **Heroku** voy a realizar la [instalación de Wordpress](https://github.com/mhoofman/wordpress-heroku) allí.


- - -
## Ejercicio 4.

Se ha creado una función con un código de prueba que aparece en el tutorial de [GoogleDrive](https://developers.google.com/apps-script/overview).

```js

function fucncionDePrueba() {
  // Creamos un nuevo documento de Google llamado 'hola mundo'
  var doc = DocumentApp.create("Hola mundo");

  // Accedemos al cuerpo del documento.
  doc.getBody().appendParagraph('Este documento ha sido creado por un Script.');

  // Obtenemos la URL del documento.
  var url = doc.getUrl();

  // Obtenemos el correo del usuario activo (el mío).
  var email = Session.getActiveUser().getEmail();

  // Obtenemos el nombre del documento.
  var subject = doc.getName();

  // Juntamos el nombre del documento con la url.
  var body = 'Enlace del documento: ' +  url;

  // Nos enviamos a nosostros mismos el documento.
  GmailApp.sendEmail(email, subject, body);
}
```

- - -
## Ejercicio 5.

* En el lenguaje de **Python** que es el que utilizo normalmente. [Pynt](https://github.com/rags/pynt) nos ofrece un sistema de automatización para construir tareas y funcionalidades de *python*. Sirve para manejar dependencias entre tareas, genera automáticamente una interfaz de línea de comandos. Este sistema soporta *python 2.7 y python 3.x*.
* También es muy utilizado y he usado en muchas ocasiones **make** para C/C++. [Makefile](http://mrbook.org/tutorials/make/)


- - -
## Ejercicio 6.

Con **Heroku** las dependencias vienen gestionadas vía [pip](https://devcenter.heroku.com/articles/python-pip) para Python para especificar las dependencias de un módulo de Python se añade un fichero de *requerimientos* llamado **requirements.txt** a la raiz del respositorio.

En cuanto a el lenguaje **PHP** las dependencias vienen en el fichero [composer.json](https://devcenter.heroku.com/articles/getting-started-with-php#declare-app-dependencies).

- - -
## Ejercicio 7.

* En **python** podemos encontar [unittest](https://docs.python.org/3.2/library/unittest.html) es un módulo estándar que quien dispone de python 2.1 o superior puede tener acceso a él. Apoya la automatización de pruebas, el intercambio de configuración y código para pruebas. Permite la agregación de pruebas de la estructura de informaicón. El módulo *unittest* ofrece clases que hacen que sea más simple el soporte de estas cualidades para un conjunto de pruebas.
* También podemos encontrar [doctest](https://docs.python.org/3.2/library/doctest.html). El módulo de *doctest* realiza búsquedas por fragmentos de texto que se asimilan mucho a las sesiones de *python* para verificar que funcionan correctamente. Existen varias formas de utilizar *doctest*.
* Entre otros tenemos:
    * [py.test](http://codespeak.net/py/current/doc/test.html).
    * [nose](http://nose.readthedocs.org/en/latest/).
    * [testify](https://github.com/Yelp/Testify/).
    * [Trial](http://twistedmatrix.com/trac/wiki/TwistedTrial).


-------------


# Técnicas de virtualización

- - -
## Ejercicio 1.

Lo primero que vamos a realizar es *crear el espacio de nombres*:

:pushpin:
```bash
# Esta llamada da una copia de su espacio de nombres montado.
#  Deja de compratir su directorio raíz el directorio actual.
su
sudo unshare -m /bin/bash
```

Después procedemos a crear dónde queremos realizar el punto de montaje:

:pushpin:
```bash
# Creamos el directorio.
mkdir -p /mnt/<mi_disco>
# Procedemos a montar la imagen ISO.
mount -o loop <mi_imagen.iso>

# Para comprobar que se ha montado (aparecerá al final).
mount
```

- - -
## Ejercicio 2.

Para crear la interfaz virtual procedemos a introducir los siguientes comandos:

:pushpin:
```bash
# Lo creamos.
sudo brctl addbr <Nombre>

# Podemos mostrar la configuración.
ip addr show
# Mostramos alguna información sobre los puentes y sus puertos.
sudo brctl show
```

La salida de estos comandos ha sido la siguiente:


:pushpin:
```bash
lewis@Inspiron:~/CloudComputing$ sudo brctl addbr BigKing
lewis@Inspiron:~/CloudComputing$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN qlen 1000
    link/ether 74:86:7a:62:d3:5c brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 48:5a:b6:11:98:bd brd ff:ff:ff:ff:ff:ff
    inet 172.20.50.46/23 brd 172.20.51.255 scope global wlan0
       valid_lft forever preferred_lft forever
    inet6 fe80::4a5a:b6ff:fe11:98bd/64 scope link
       valid_lft forever preferred_lft forever
4: BigKing: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN
    link/ether 66:e2:78:eb:4a:8b brd ff:ff:ff:ff:ff:ff
lewis@Inspiron:~/CloudComputing$ sudo brctl show
bridge name	bridge id		STP enabled	interfaces
BigKing		8000.000000000000	no
```

- - -
## Ejercicio 3.

Puesto que no tenemos instalado, procedemos a instalarlo:

:pushpin:
```bash
# Instalamos el paquete.
sudo apt-get install debootstrap
```
A continuación procedemos a crear el sistema que queremos.


:pushpin:
```bash
# Indicamos la arquitectura, el sistema, el directorio y de dónde se va a descargar.
sudo debootstrap --arch=amd64 saucy /home/lewis/Escritorio/CC/saucy/ http://archive.ubuntu.com/ubuntu
# Tardará un rato... pero la salida final será el algo así.
(...)
I: Configuring dmsetup...
I: Configuring eject...
I: Configuring ureadahead...
I: Configuring kbd...
I: Configuring ubuntu-minimal...
I: Configuring libc-bin...
I: Configuring initramfs-tools...
I: Base system installed successfully.
```

Continuamos con la creación de un sistema **Fedora** dentro de Debian usando **Rinse**.


:pushpin:
```bash
# Instalamos el paquete.
sudo apt-get install rinse

# Ejecutamos la orden para crearnos el sistema.
# Similar a la que introducimos antes.
sudo rinse --arch=i386 --distribution fedora-core-7 --directory ~/Escritorio/CC/fedora/

# Al igual que antes tarda un rato.
(...)
Running post-install script post-install.sh:
  Setting up YUM cache
  Creating yum.conf
  Bootstrapping yum
  Cleaning up
Failed to set locale, defaulting to C
  Final tidy...
Installation complete.
```

Si comprobamos el contenido de las carpetas en ellas obtendríamos el siguiente listado de directorios:

:pushpin:
```bash
[ lewis: ~/Escritorio/CC ]$ ls saucy/
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
[ lewis: ~/Escritorio/CC ]$ ls fedora/
bin   dev  home  media  opt   root  selinux  sys  usr
boot  etc  lib   mnt    proc  sbin  srv      tmp  var

```
- - -
## Ejercicio 4.

Lo primero que vamos a hacer es entrar en la jaula:


:pushpin:
```bash
# Entramos en la jaula.
sudo chroot /home/lewis/Escritorio/CC/<sistema>

# Tendríamos el siguiente resultado.
[ lewis: ~/Escritorio/CC ]$ sudo chroot saucy/
root@Inspiron:/#
```

Procedemos a montar el sistema de archivos (*file system*) y realizamos algunas tareas:


:pushpin:
```bash
# Montamos el file system.
mount -t proc proc /proc

# Instalamos alguna aplicación, por ejemplo vim y nano.
apt-get install vim
apt-get install nano
```

Como tenemos **python** instalado en el sistema, ejecutamos nano y creamos el siguiente código con editor *nano* (Que por cierto si creas un fichero de *python* .py y lo editas, te lo colorea el editor):
```py
print("Hola!")
```

El resultado sería el siguiente:

:pushpin:
```bash
# Editamos el fichero para meter el código de antes.
nano "programa.py"

# Ejecutamos el código del programa para ejecutarlo.
root@Inspiron:/# python3 "programa.py"
Hola!
# También se puede ejecutar la orden top para ver los procesos.
top

# Obtendríamos la siguiente salida en mi caso.
'
top - 19:08:06 up 19 min,  0 users,  load average: 0.47, 0.34, 0.26
Tasks: 219 total,   1 running, 218 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.7 us,  0.7 sy,  0.1 ni, 93.5 id,  3.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   8055272 total,  2213864 used,  5841408 free,    76612 buffers
KiB Swap:  1999868 total,        0 used,  1999868 free,   981772 cached

  PID USER      PR  NI  VIRT  RES  SHR S  %CPU %MEM    TIME+  COMMAND
 1143 root      20   0  438m 126m  90m S   6.3  1.6   0:24.06 Xorg
    1 root      20   0 27216 2964 1416 S   0.0  0.0   0:01.26 init
    2 root      20   0     0    0    0 S   0.0  0.0   0:00.00 kthreadd
    3 root      20   0     0    0    0 S   0.0  0.0   0:00.00 ksoftirqd/0
    5 root       0 -20     0    0    0 S   0.0  0.0   0:00.00 kworker/0:0H
    6 root      20   0     0    0    0 S   0.0  0.0   0:00.87 kworker/u16:0
    7 root      rt   0     0    0    0 S   0.0  0.0   0:00.00 migration/0
    8 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcu_bh
    9 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/0
   10 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/1
   11 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/2
   12 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/3
   13 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/4
   14 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/5
   15 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/6
   16 root      20   0     0    0    0 S   0.0  0.0   0:00.00 rcuob/7
'  
```

- - -
## Ejercicio 5.

En el mismo *saucy* que hemos ejecutado las ordenes anteriores, insertamos los repositoros de **nginx** dentro del fichero `/etc/apt/sources.list`:


:pushpin:
```bash
deb "http://archive.ubuntu.com/ubuntu" saucy main
deb "http://nginx.org/packages/ubuntu" saucy nginx
deb-src "http://nginx.org/packages/ubuntu" saucy nginx
```

Una vez hecho esto obtenemos la *clave* del repositorio **nginx**:

:pushpin:
```bash
# Instalamos el paquete para descargarnos la llave con la url.
apt-get install wget

# Nos descargamos la clave.
wget http://nginx.org/keys/nginx_signing.key

# Añadimos la clave.
apt-key add nginx_signing.key

# Si todo ha ido bien aparecerá un:
"OK"
```

Ahora procedemos a instalar el programa propiamente dicho:

:pushpin:
```bash
# Actualizamos.
apt-get update

# Instalamos el programa.
apt-get install nginx
```

Para arrancar el servidor procedemos como sigue:

:pushpin:
```bash
# Arrancamos el servicio.
service nginx start

# Para comprobar que está todo correctamente
service --status-all

# Como resultaod obtenemos la siguiente salida:
'
 [ + ]  console-font
 [ + ]  console-setup
 [ + ]  cron
 [ ? ]  killprocs
 [ + ]  kmod
 [ ? ]  networking
 [ + ]  nginx          <------
 [ ? ]  ondemand
 [ - ]  procps
 [ ? ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsyslog
 [ ? ]  sendsigs
 [ + ]  setvtrgb
 [ - ]  sudo
 [ - ]  udev
 [ ? ]  umountfs
 [ ? ]  umountnfs.sh
 [ ? ]  umountroot
 [ - ]  urandom
'
```

- - -
## Ejercicio 6.

A continuación vamos a proceder a crear una jaula y enjaular un usuario usando `jailkit`.


:pushpin:
```bash
# Lo primero que haces es descargarnos jailkit.
wget "http://olivier.sessink.nl/jailkit/jailkit-2.17.tar.gz"

# Lo descomprimimos.
tar -xzvf "jailkit-2.17.tar.gz"

# Nos vamos a la carpeta que lo contiene.
cd jailkit-2.17/

# Procedemos a crear la configuración para instalarlo.
./configure

# Se preparan los archivos.
make

# Se instala finalmente.
sudo make install
```

Después procedemos a crear la jaula y a enjaular al usuario:


:pushpin:
```bash
# Creamos el directorio que contendra la jaula.
mkdir Cataplasma

# Configuramos el directorio como root.
sudo chown root:root "Cataplasma/"

# Creamos el entorno .
sudo jk_init -v "Cataplasma/" basicshell
sudo jk_init -v "Cataplasma/" editors
sudo jk_init -v "Cataplasma/" extendedshell
sudo jk_init -v "Cataplasma/" netutils
sudo jk_init -v "Cataplasma/" ssh
sudo jk_init -v "Cataplasma/" sftp

# Creamos un usuario.
sudo adduser Luis

# Lo enjaulamos.
sudo jk_jailuser -m -j "Cataplasma/" Luis
```

Podemos comprobar que está correctamente realizado porque en el fichero `/etc/passwd` encontramos la siguiente línea:

:pushpin:
```bash
Luis:x:1001:500::/home/lewis/Escritorio/CC/Cataplasma/./home/Luis:/usr/sbin/jk_chrootsh

# Se puede asignar una contraseña al usuario.
sudo passwd Luis

# Se puede configurar el directorio home del usuario.
sudo mkdir -p /home/lewis/Escritorio/CC/Cataplasma/home/Luis

```

-------------


# Virtualización ligera usando contenedores

- - -
## Ejercicio 1.

Instalamos el *Linux Containers* (LXC):

:floppy_disk:

```bash
#Instalamos LXC.
sudo apt-get install "lxc"

# El resultado sería el siguiente.
(...)
Configurando python-distro-info (0.11) ...
Configurando qemu-utils (1.5.0+dfsg-3ubuntu5.4) ...
Configurando sharutils (1:4.11.1-1ubuntu2) ...
Configurando cloud-image-utils (0.27-0ubuntu4.1) ...
Procesando disparadores para ureadahead ...
Configurando lxc-templates (1.0.0~alpha1-0ubuntu14.1) ...
Procesando disparadores para libc-bin ...
```

Podemos comprobar que todo está correcto:

:white_check_mark:

```bash
# Insertamos la siguiente orden.
lxc-checkconfig

# Obtenemos el siguiente resultado.
Kernel configuration not found at /proc/config.gz; searching...
Kernel configuration found at /boot/config-3.11.0-26-generic
--- Namespaces ---
Namespaces: "enabled"
Utsname namespace: "enabled"
Ipc namespace: "enabled"
Pid namespace: "enabled"
User namespace: missing
Network namespace: "enabled"
Multiple /dev/pts instances: "enabled"

--- Control groups ---
Cgroup: "enabled"
Cgroup clone_children flag: "enabled"
Cgroup device: "enabled"
Cgroup sched: "enabled"
Cgroup cpu account: "enabled"
Cgroup memory controller: "enabled"
Cgroup cpuset: "enabled"

--- Misc ---
Veth pair device: "enabled"
Macvlan: "enabled"
Vlan: "enabled"
File capabilities: "enabled"

Note : Before booting a new kernel, you can check its configuration
usage : CONFIG=/path/to/config /usr/bin/lxc-checkconfig
```

- - -
## Ejercicio 2.

Para comprobar qué interfaces se han creado podemos hacer lo siguiente:

:pushpin:

```bash
# Mostramos todos los parámetros de las interfaces de redes.
ifconfig

# El resultado sería el siguiente.
(...)
lxcbr0    Link encap:Ethernet  direcciónHW f2:cc:dc:f8:1d:bf  
          Direc. inet:10.0.3.1  Difus.:10.0.3.255  Másc:255.255.255.0
          Dirección inet6: fe80::f0cc:dcff:fef8:1dbf/64 Alcance:Enlace
          ACTIVO DIFUSIÓN FUNCIONANDO MULTICAST  MTU:1500  Métrica:1
          Paquetes RX:0 errores:0 perdidos:0 overruns:0 frame:0
          Paquetes TX:58 errores:0 perdidos:0 overruns:0 carrier:0
          colisiones:0 long.colaTX:0
          Bytes RX:0 (0.0 B)  TX bytes:9697 (9.6 KB)

(...)

# O bien podríamos utilizar la orden.
brctl show
```

Se podría asociar una interfaz como que tenemos creada al puente.

:pushpin:
```bash
# Asociar una interfaz al puente.
sudo brctl addif <interfaz> <puente>
```

- - -
## Ejercicio 3.

Vamos a instalar *debootstrap*.

:dvd:

```bash
# Creamos el contenedor.
sudo lxc-create -t deina -n DebanContenedor
```

Tardará un rato :sleeping:...
