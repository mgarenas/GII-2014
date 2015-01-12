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

Ya teníamos instalado *debootstrap*. Y además en ejercicios anteriores instalamos tambien otras distribuciones tales como **saucy** y **fedora** en el **ejercicio 3** del tema anterior.

:dvd:

```bash
# Creamos el contenedor.
sudo lxc-create -t debian -n DebianContenedor

# El resultado sería algo así.
(...)
	LC_IDENTIFICATION = "en_GB.UTF-8",
	LC_MEASUREMENT = "en_GB.UTF-8",
	LC_TIME = "en_GB.UTF-8",
	LC_NAME = "en_GB.UTF-8",
	LANG = "es_ES.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
update-rc.d: using dependency based boot sequencing
Root password is 'root', please change !

# El contenedor se creará en `/var/lib/lxc/
sudo ls /var/lib/lxc/
DebianContenedor

```

Tardará un rato :sleeping:... Pero como decíamos se pude instalar con *debootstrap*. Que ya lo teníamos hecho.

:exclamation: :repeat:
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

La creación de un sistema **Fedora** dentro de Debian usando **Rinse**.

:exclamation: :repeat:
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

- - -
## Ejercicio 4.

En [LXC Web Panel](http://lxc-webpanel.github.io/install.html) podemos encontrar cómo instalarlo. De modo que procedemos:

:floppy_disk:
```bash
# Nos descargamos lo necesario y lo instalamos.
wget "http://lxc-webpanel.github.io/tools/install.sh" -O - | bash

# Y nos indicará al final dónde podemos conectarnos.
(...)
Checking connectivity... done

Installation complete!


Adding /etc/init.d/lwp...
Done
Starting server...done.
Connect you on "http://your-ip-address:5000/"
```

En el navegador escribimos la dirección `http://localhost:5000` para acceder a la página de acceso y nos pedirá:
  * **Usuario**: admin
  * **Contraseña**: admin

En mi caso aparece que tenemos 1 solo contenedor que está parado y que se llama **DebianContenedor**. Tal y como lo indicamos anteriormente.
Podemos hacer uso de los botones **start** y cuando lo hemos iniciado podemos pararlo **stop** o pausarlo **freeze**.

:arrow_right: Podemos pulsar en el contenedor y ver la información que tiene y también modificarlo.

Para restringir los recursos nos vamos a la **parte inferior** de la pantalla que acabamos de describir y nos aparecerá:
  - **Memory limit**. Límite de memoria total.
  - **Memory + Swap limit**. Límite de memoria total junto con la de intercambio.
  - **CPUs**. Número de procesadores que podrá usar.
  - **CPU Shares**. Cantidad de procesamiento que puede utilizar de la/s CPU/s.
  
Ahí lo podemos modificar todo.

- - - 
## Ejercicio 5. 

Lo primero que hemos de hacer es acceder a la jaula:

:pushpin:

```bash
# Accedemos a la jaula.
sudo chroot "saucy/"

# Comprobamos si está el servicio ejecutandose.
service nginx status
# Salida.
 * nginx is not running
```

Como no está funcionando, lo que tenemos que hacer es arrancarlo.

:pushpin:

```bash
# Arrancamos el servicio.
service nginx start

# Y ya podemos comprobar que está arrancado.
service nginx status
# Salida.
 * nginx is running
```

Consultamos con `ifconfig -a` qué página es en la que está asociada *nginx* y podemos ver en nuestro caso que está en `10.0.3.1` en el caso del contenedor. Y `127.0.0.1` en el caso de la jaula. Nos aparece un mensaje en el navegador así como:

:arrow_lower_right:
```
Welcome to nginx!

If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx.
```

Para comparar las prestaciones vamos a utilizar un **Apache Benchmark** con la siguiente orden (desde fuera):

:pushpin:

```bash
# Benchmark para la jaula.
ab -n 1000000 -c 10 http://127.0.0.1/index.html

# Benchmark para el contenedor.
ab -n 1000000 -c 10 http://10.0.3.1/index.html
```

El resultado del primero sería el que sigue:

:arrow_lower_right:

```
Server Software:        nginx/1.6.0
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /index.html
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   35.691 seconds
Complete requests:      1000000
Failed requests:        0
Write errors:           0
Total transferred:      844000000 bytes
HTML transferred:       612000000 bytes
Requests per second:    28018.04 [#/sec] (mean)
Time per request:       0.357 [ms] (mean)
Time per request:       0.036 [ms] (mean, across all concurrent requests)
Transfer rate:          23092.99 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     0    0   1.0      0     242
Waiting:        0    0   1.0      0     242
Total:          0    0   1.0      0     242
```

Y el del segundo sería:

:arrow_lower_right:

```
Server Software:        nginx/1.6.0
Server Hostname:        10.0.3.1
Server Port:            80

Document Path:          /index.html
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   35.632 seconds
Complete requests:      1000000
Failed requests:        0
Write errors:           0
Total transferred:      844000000 bytes
HTML transferred:       612000000 bytes
Requests per second:    28064.29 [#/sec] (mean)
Time per request:       0.356 [ms] (mean)
Time per request:       0.036 [ms] (mean, across all concurrent requests)
Transfer rate:          23131.11 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     0    0   3.3      0    1045
Waiting:        0    0   3.3      0    1045
Total:          0    0   3.3      0    1045
```

No existe mucha diferencia, en tiempos más o menos es el mismo qel que se ha tomado tanto un **benchmark** como el otro. En cuanto a las *peticiones por segundo* puede notarse también que son muy similares, pero la jaula obtiene unos peores resultados. También si nos fijamos en la *tasa de transferencia* puede verse que es un poco más alta en el contenedor que en la jaula. 

>Estos resultados no deben ser muy concluyentes (puesto que se han realizado solo 1 vez), se debería contrastar un poco más con alguna medida tal como la media, desviación típica de varias pruebas realizadas, etcétera. 

- - - 
## Ejercicio 6.

Seguimos el guión del tema para instalarlo, para ello:

:floppy_disk:

```bash
# Añadimos el repositorio.
sudo add-apt-repository ppa:juju/stable

# Salida.
 Stable release of Juju fo Ubuntu 12.04 and above.
 Más información: https://launchpad.net/~juju/+archive/ubuntu/stable
Pulse [Intro] para continuar o ctrl-c para cancelar

gpg: anillo «/tmp/tmpq5o0z3/secring.gpg» creado
gpg: anillo «/tmp/tmpq5o0z3/pubring.gpg» creado
gpg: solicitando clave C8068B11 de hkp servidor keyserver.ubuntu.com
gpg: /tmp/tmpq5o0z3/trustdb.gpg: se ha creado base de datos de confianza
gpg: clave C8068B11: clave pública "Launchpad Ensemble PPA" importada
gpg: Cantidad total procesada: 1
gpg:               importadas: 1  (RSA: 1)
OK

```

Actualizamos e instalamos.

:floppy_disk:

```bash
# Actualizamos el respositorio.
sudo apt-get update

# Instalamos.
sudo apt-get install juju-core

# Salida.
(...)
(Leyendo la base de datos ... 295389 ficheros o directorios instalados actualmente.)
Desempaquetando juju-core (de .../juju-core_1.20.1-0ubuntu1~13.10.1~juju1_amd64.deb) ...
Configurando juju-core (1.20.1-0ubuntu1~13.10.1~juju1) ...
update-alternatives: utilizando /usr/lib/juju-1.20.1/bin/juju para proveer /usr/bin/juju (juju) en modo automático
```

A continuación vamos a proceder a usarlo e instalar MySQL en un táper. Lo primero que vamos a hacer es ejecutarlo:

:pushpin:

```bash
# Lo inicializamos.
sudo juju init

# Salida.
A boilerplate environment configuration file has been written to "/home/lewis/.juju/environments.yaml".
Edit the file to configure your juju environment and run bootstrap.
```

Aquí nos indica que se ha creado el archivo con la información de entornos en `/home/lewis/.juju/environments.yaml`. Antes de poder instalar nada, y trabajar en local, nos exige que tengamos instalado el `juju-local`. Pues procedemos a instalarlo *(tarda bastante y es bastante pesado)*:

:floppy_disk:

```bash
# Instalamos el juju local.
sudo apt-get install juju-local

# Salida.
(...)
Añadiendo un nuevo usuario mongodb' (UID 117) con grupo nogroup' ...
No se crea el directorio personal /home/mongodb'.
Añadiendo el grupo mongodb' (GID 126) ...
Hecho.
Añadiendo al usuario mongodb' al grupo mongodb' ...
Añadiendo al usuario mongodb al grupo mongodb
Hecho.
mongodb start/running, process 4853
Configurando rsyslog-gnutls (5.8.11-2ubuntu4) ...
Procesando disparadores para ureadahead ...
Configurando juju-local (1.20.1-0ubuntu1~13.10.1~juju1) ...
Procesando disparadores para libc-bin ...
```

:pushpin:

```bash
# Podemos ver los contenedores que tenemos en el sistema.
sudo lxc-ls

# Creamos el táper.
juju bootstrap

# Instalamos MySQL.
juju deploy mysql
```

- - -
## Ejercicio 7

:one: Lo primero de todo que vamos a realizar es borrar toda la configuración que hasta ahora se ha creado:

:pushpin:

```bash
# Destruimos el servicio de mysql
sudo juju destroy-service mysql
# También el servicio de mediawiki
sudo juju destroy-service mediakiki
# Podemos también destruir el entorno local.
sudo juju destroy-environment local

#Salida
WARNING! this command will destroy the "local" environment (type: local)
This includes all machines, services, data and other resources.

Continue [y/N]? y
```

:two: Ahora volvemos a crear la máquina anterior y añadirle *mediawiki* y una relación entre ellos. Para esto, lo que tenemos que hacer primero es seguir los mismos pasos que antes:

:pushpin:

```bash
# Hacemos bootstrap.
sudo juju bootstrap

# Desplegamos mediawiki y mysql.
sudo juju deploy mediawiki
sudo juju deploy mysql

# Establecemos la relación.
sudo juju add-relation mediawiki:db mysql

# Exponemos el servicio y listo
sudo juju expose mediawiki
```

:three: Lo último que vamos a hacer es crear un script en *shell* para reproducir la configuración usada en las máquina que haga falta. Básicamente lo que tenemos que hacer es agrupar en un *script* el código anteriormente expuesto.

:pushpin:

```bash
#!/bin/bash
# Ejercicio 7
# -----------
# Configura juju con MySQL y mediawiki.

# Inicializamos juju.
juju init

# Escogemos el entorno.
juju switch local
# Creamos el contenedor.
juju bootstrap

# Desplegamos los servicios que queremos.
juju deploy mediawiki
juju deploy mysql

# Establecemos la relación entre los dos servicios.
juju add-relation mediawiki:db mysql

# Exponemos el servicio.
juju expose mediawiki
```

- - - 
## Ejercicio 8.

Vamos a proceder a instalar según el tutorial que se nos proprociona.

:pushpin:

```bash
# Comprobamos que nuestro sistema soporta las extensiones de virtualización para KVM.
kvm-ok

# Salida.
INFO: /dev/kvm exists
KVM acceleration can be used
```

Puesto que es compatible procedemos a realizar la instalación.

:floppy_disk:

```bash
# Instalamos el software.
sudo apt-get install kvm libvirt-bin

# Añadimos el usuario que va a manejar las máquinas virtuales.
sudo adduser $USER libvirtd

# Accedemos una vez instalado el paquete.
virsh
```

- - - 
## Ejercicio 9.

Procedmos a instalar **virt-install** de la siguiente manera:

:floppy_disk:

```bash
# Instalamos el paquete de 'virt-install'.
sudo apt-get install virtinst

# Salida.
(...)
Seleccionando el paquete virtinst previamente no seleccionado.
Desempaquetando virtinst (de .../virtinst_0.600.4-2ubuntu2.1_all.deb) ...
Procesando disparadores para man-db ...
Configurando python-libvirt (1.1.1-0ubuntu8.11) ...
Configurando python-urlgrabber (3.9.1-4ubuntu2) ...
Configurando virtinst (0.600.4-2ubuntu2.1) ...
```

:floppy_disk:

```bash
# Instalamos el paquete 'vrt-viewer' para acceder a 
#   la consola de la máquina usando la interfaz gráfica.
sudo apt-get install virt-viewer

# Salida.
(...)
Configurando libspice-client-gtk-3.0-4:amd64 (0.20-0nocelt3) ...
Configurando libgvnc-1.0-0 (0.5.2-1ubuntu2) ...
Configurando libgtk-vnc-2.0-0 (0.5.2-1ubuntu2) ...
Configurando virt-viewer (0.5.6-2) ...
update-alternatives: utilizando /usr/bin/spice-xpi-client-remote-viewer para proveer /usr/bin/spice-xpi-client (spice-xpi-client) en modo automático
Procesando disparadores para libc-bin ...
```

Una vez hecho esto necesitamos una imagen **iso** del sistema operativo que vamos a descargar y con la imagen descargada se realiza la instalación:

:dvd:

```bash
# Instalamos la máquina virtual con las siguientes opciones:
#   1) -n virt-ubuntuserver : Nombre de la máquina virtual.
#   2) -r 512 : Cantidad de memoria RAM (MB).
#   3) --disk path=/var/lib/libvirt/images/virt-ubuntuserver.img,bus=virtio,size=5 : La ruta donde se almacenarán recursos que usará el sistema.
#   4) -c miISO.iso : Imagen ISO que vamos a instalar.
#   5) --accelerate : Indica que se utilizará aceleración del kernel.
#   6) --network network=default,model=virtio : Interfaz y modelo de red.
#   7) --connect=qemu:///system : Indica el hipervisor.
#   8) --vnc : Para exportar la consola usando VNC.
#   9) --noautoconsole : Para que no se conecte automáticamente a la consola de la máquina virtual.
#  10) -v : Que la máquina esté totalmente virtualizada.
#
#   Para ver todas estas opciones consultar el manual: 'man virt-install'
sudo virt-install -n virt-ubuntuserver -r 512 --disk path=/var/lib/libvirt/images/virt-ubuntuserver.img,bus=virtio,size=5 -c miISO.iso --accelerate --network network=default,model=virtio --connect=qemu:///system --vnc --noautoconsole -v

# Podemos ver las máquinas virtuales instaladas.
sudo virsh -c qemu:///system list

# Salida.
 Id    Nombre                         Estado
----------------------------------------------------
 1     virt-ubuntuserver              ejecutando
```

- - -
## Ejercicio 10.

Vamos ahora a instalar **Docker**, existen varias formas de realizar la instalación una de ellas es mediante el *script* que nos proporcionan en la siguiente url: 

[https://get.docker.com/ubuntu/](https://get.docker.com/ubuntu/)

:floppy_disk:

```bash
#Descargamos el script y lo ejecutamos.
curl -sSL https://get.docker.com/ubuntu/ | sudo sh

# Salida.
(...)
Desempaquetando lxc-docker (de .../lxc-docker_1.4.1_amd64.deb) ...
Procesando disparadores para man-db ...
Procesando disparadores para ureadahead ...
ureadahead will be reprofiled on next reboot
Configurando aufs-tools (1:3.2+20130722-1ubuntu1) ...
Configurando lxc-docker-1.4.1 (1.4.1) ...
docker start/running, process 4745
Procesando disparadores para ureadahead ...
Configurando lxc-docker (1.4.1) ...
Procesando disparadores para libc-bin ...
```

Tardará un rato para realizar la instalación :sleeping:... También podemos ver el contenido del script que acabamos de ejecutar que sería el siguiente:

:pushpin:

```bash
# Check that HTTPS transport is available to APT
if [ ! -e /usr/lib/apt/methods/https ]; then
  apt-get update
  apt-get install -y apt-transport-https
fi

# Add the repository to your APT sources
echo deb https://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list

# Then import the repository key
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9

# Install docker
apt-get update
apt-get install -y lxc-docker

#
# Alternatively, just use the curl-able install.sh script provided at https://get.docker.com
#
```

Y listo, ahora simplemente para ejecutar el servicio **docker** tenemos que ejecutar el siguiente comando:

:pushpin:

```bash
# Ejecutamos el servicio docker.
sudo docker -d

# Salida.
INFO[0000] +job serveapi(unix:///var/run/docker.sock)   
INFO[0000] +job init_networkdriver()                    
INFO[0000] Listening for HTTP on unix (/var/run/docker.sock) 
INFO[0000] -job init_networkdriver() = OK (0)           
INFO[0000] WARNING: Your kernel does not support cgroup swap limit. 
INFO[0000] Loading containers: start.                   

INFO[0000] Loading containers: done.                    
INFO[0000] docker daemon: 1.4.1 5bc2ff8; execdriver: native-0.2; graphdriver: aufs 
INFO[0000] +job acceptconnections()                     
INFO[0000] -job acceptconnections() = OK (0)    
```