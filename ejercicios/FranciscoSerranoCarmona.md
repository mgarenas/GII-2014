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

##Ejercicios Práctica 2

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

