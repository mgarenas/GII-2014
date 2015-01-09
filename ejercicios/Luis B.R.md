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

- - - 
## Ejercicio 11.

Lo primero que vamos a hacer es instalar