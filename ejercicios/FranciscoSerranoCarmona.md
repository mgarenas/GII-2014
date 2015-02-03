#Ejercicios de Francisco Serrano Carmona

##TEMA 1

###Ejercicio 1

Se ha seleccionado un [servidor] (http://www.alternate.es/ASUS/RS720-E7-RS12-E-+-PIKE2108/html/product/1135394?) de 2179 € (1721 € sin IVA).

* Amortización a cuatro años:

Porcentaje máximo de amortización del 26% anual a un máximo de 10 años.

Imponemos el 25% del precio de adquisición sin IVA en cada año. [430 € / año]. A los cuatro años el servidor tendría un valor de 1 € con una amortización acumulada de 1720 € (practicamente amortizado).

* Amortización a siete años:

 En el quinto año estaría totalmente amortizado, por lo que el servidor ya se habría desfasado para la empresa.

###Ejercicio 3

* Para alojar varios clientes en un servidor, utilizaría la virtualización parcial de la memora, para que cada usuario tenga su memoria y recursos asignados.

* Para crear un sistema eficiente de web + middleware + base de datos utilizaría la virtualización plena, ya que se necesita acceder a los recursos hardware de forma eficiente.

* Para un sistema de prueba de software e integración continua utilizaría la virtualización de aplicaciones, dado que permiten cambiar entre varios sistemas para probar que la aplicación funciona correctamente virtualizándola en dichos sistemas.

* Para empaquetar un programa (un Hola Mundo en Bash) en CDE, se ha seguido [este] (http://blog.desdelinux.net/como-crear-aplicaciones-portables-de-linux/) manual.

###Ejercicio 4

* docker version
* docker search tutorial
* docker pull learn/tutorial
* docker run learn/tutorial echo "hello world"
* docker run learn/tutorial apt-get install -y ping
* docker commit 6982a9948422 learn/ping
* docker run learn/ping ping google.com
* docker inspect efe
* docker push learn/ping

###Ejercicio 5

* sudo apt-get install git
* git config --global user.name "Francisco Serrano Carmona"
* git config --global user.email "frandai@correo.ugr.es"

###Ejercicio 6

* se crea el [repositorio] (https://github.com/frandai/prueba_frandai)
* git clone https://github.com/frandai/prueba_frandai
* (se edita el README.md)
* git add README.md
* git commit -m "Cambiado readme"
* git push origin master

###Ejercicio 7

* En Lubuntu 14.04 se encuentra instalado cgroups en /sys/fs/cgroups/systemd. Contiene:
cgroup.clone_children  cgroup.procs          notify_on_release  tasks
cgroup.event_control   cgroup.sane_behavior  release_agent      user

##Ejercicios Tema 2

###Ejercicio 1

* Instalo rbenv usando este [enlace] (https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-debian-7-wheezy)
* git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
* echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
* echo 'eval "$(rbenv init -)"' >> ~/.bashrc
* git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
* git clone https://github.com/sstephenson/rbenv-gem-rehash.git ~/.rbenv/plugins/rbenv-gem-rehash

###Ejercicio 2

* Me doy de alta en OpenShift (versión Online)

###Ejercicio 3

* Entro en la [consola web] (https://openshift.redhat.com/app/console/applications)
* Selecciono "Install App -> Wordpress 4"
* Configuro un namespace (frandai)
* La URL Pública es: https://blog–frandai.rhcloud.com

###Ejercicio 4



* Se crea la función en un archivo de Googe:

```
function onOpen() {
  // Add a menu with some items, some separators, and a sub-menu.
  DocumentApp.getUi().createMenu('Menu')
      .addItem('Alerta', 'showAlert')
      .addToUi();
}

function showAlert() {
    DocumentApp.getUi().alert('Una Alerta!');
}
```


###Ejercicio 5

* Se usa "Make" y Makefiles para construir con el lenguaje Python

###Ejercicio 6

* OpenShift dispone de un sistema llamado "Action Hooks", los cuales contienen Scripts de construcción. [Más Información] (https://developers.openshift.com/en/managing-action-hooks.html)

###Ejercicio 7

* Django usa el módulo [Unit Test] (https://docs.djangoproject.com/en/1.7/topics/testing/) para los Tests.

##Ejercicios Tema 3

###Ejercicio 1

```
unshare -u /bin/bash
mount -o loop -t iso9660 lubuntu-14.10-desktop-amd64.iso /mnt/lubuntu
```

###Ejercicio 2
```
ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 28:b2:bd:4c:7b:74 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.133/24 brd 192.168.1.255 scope global wlan0
       valid_lft forever preferred_lft forever
    inet6 fe80::2ab2:bdff:fe4c:7b74/64 scope link 
       valid_lft forever preferred_lft forever
3: alcantara: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default 
    link/ether 82:8c:1c:fc:23:2f brd ff:ff:ff:ff:ff:ff
```

###Ejercicio 3
```
mkdir -p ~/jaulas/saucy
sudo debootstrap --arch=i386 saucy ~/jaulas/saucy/ http://archive.ubuntu.com/ubuntu
```
####Para Rinse:
```
sudo rinse --distribution fedora-core-6 --arch amd64 --directory /tmp/test
```

###Ejercicio 4

* Entramos como CHROOT: sudo chroot /home/jaulas/raring
* Usamos una aplicación: 
```
root@fran-Asus:/# cat /etc/issue
Ubuntu 13.10 \n \l

```

###Ejercicio 5
```
#Añadir el repositorio de NGINX
echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list
#Añadir las claves del repositorio para que sea confiable
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C
#Actualizar repositorios
sudo apt-get update
#instalar NGINX
sudo apt-get install nginx
#iniciiar NGINX
sudo service nginx start
```

##Ejercicios Tema 4

###Ejercicio 1
* Instalamos LXC: sudo apt-get install lxc
* Nos aseguramos de que la versión es mayor que la 1.0: lxc-info --version -> 1.0.7

###Ejercicio 2
```
4: lxcbr0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether fe:20:13:6d:3f:e7 brd ff:ff:ff:ff:ff:ff
    inet 10.0.3.1/24 brd 10.0.3.255 scope global lxcbr0
       valid_lft forever preferred_lft forever
    inet6 fe80::30f0:2aff:feb2:c702/64 scope link 
       valid_lft forever preferred_lft forever
6: vethB81GC7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master lxcbr0 state UP group default qlen 1000
    link/ether fe:20:13:6d:3f:e7 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::fc20:13ff:fe6d:3fe7/64 scope link 
       valid_lft forever preferred_lft forever
```

* Ha creado los puentes lxcbr0 y vethB81GC7, necesarios para conectar la jaula a internet.

###Ejercicio 4

* Descargamos LXC WebPanel: wget http://lxc-webpanel.github.io/tools/install.sh 
* Instalamos LXC WebPanel: sudo ./install.sh
* Accedemos a través de: http://localhost:5000/ (Usuario/Pass: admin/admin)
* Desde la sección "Containers" se puede limitar el uso de CPU y Memoria.


#### Ejercicio 8

* Se Instala libvirt

```
sudo apt-get install kvm libvirt-bin
sudo adduser $USER libvirtd
```










