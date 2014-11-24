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



