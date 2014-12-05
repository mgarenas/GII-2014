#Ejercicios de Jesús Maillo Hidalgo
##Tema 1
###Ejercicio1
**Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años.**

El servidor seleccionado ha sido [este](http://www.dell.com/es/empresas/p/poweredge-t110-2/pd?oc=pet1102bu&model_id=poweredge-t110-2)

Servidor orientado para pequeñas empresas. Tiene un coste de 699 € sin IVA incluido.

Para facilitar los cálculos, en el supuesto se parte de que el producto ha sido comprado a día no de enero, ya que si no se tendría que periodificar.

* Amortización a cuatro años:

 En base a la tabla, los sistemas informáticos tienen una porcentaje máximo de amortización del 26% anual a un máximo de 10 años.

 Sujeto a esta restricción y utilizando un criterio constante de amortización, impondré el 20% del precio de adquisición sin IVA en cada año. (Puesto que el IVA se puede deducir al 100% en el primer trimestre). [139.80 € cada año]. A los cuatro años el servidor tendría un valor de 139.8 € con una amortización acumulada de 559.20 €.

* Amortización a siete años:

 En el quinto año estaría totalmente amortizado, de manera que poseería el servidor en el activo pero su amortización acumulada conlleva a que el servidor no tenga valor para la empresa.

###Ejercicio 2
** Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, Comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo. **

Los servidores que voy a comparar son de Amazon y Azure respectivamente.

El primero podemos encontrarlo [aqui](http://aws.amazon.com/es/ec2/pricing/) con unas características:

4 CPU, 15 GB Ram, 80 SSD

439€ el pago del servicio anual y un costo de 0.308€ la hora.

El tiempo por horas utilizado al 1% es de 26.31552€. Hacen un total de 465,315€

El tiempo por horas utilizado al 10% es de 269,808€. Haven un total de 708,808€

El segundo lo podemos encontrar [aqui](http://azure.microsoft.com/es-es/pricing/calculator/?scenario=cloud) con unas características:

>4 CPU, 14 G Ram, 250 SSD.
>
>352,39€ el pago del servicio anual y un costo de 0.474€ la hora.
>
>El tiempo por horas utilizado al 1% es de 41,5224€. Hacen un total de 393,9124€
>
>El tiempo por horas utilizado al 10% es de 415,224€. Haven un total de 767,614€
>
>Para unas características similares, incluso Azure posee algo más de disco SSD, los precios son muy similares, lo suficiente como para tener que centrarse realmente en la funcionalidad y las características que deseemos más que en las diferencias en precio ya se con un uso del 1% o del 10%.


*Corrección de Luis Baca Ruiz*

Si cogemos el primer caso que expones

* 4 CPU, 15 GB Ram, 80 SSD

* 439€ el pago del servicio anual y un costo de 0.308€ la hora.

* El tiempo por horas utilizado al 1% es de 26.31552€. Hacen un total de 465,315€

* El tiempo por horas utilizado al 10% es de 269,808€. Hacen un total de 708,808€

Podemos encontrar en la siguiente url:

https://www.ovh.es/vps/vps-classic.xml

el siguiente servidor:

  * VPS Classic 4.
  * 18.14 € IVA incl / mes.
  * 4 vCores.
  * 8 GB.
  * 100 GB Raid 10.

que es muy similar al que expones. Lo que tenemos que hacer es 18.14 * 12 = **217.68 € / año.**

El caso que tú expones sería de **465,315 € / año** que sale más caro.


###Ejercicio 3:
**1 -¿Qué tipo de virtualización usarías en cada caso? Comentar en el foro.**

La respuesta comentada en el foro ha sido:

* Alojamiento de varios clientes en un solo servidor: La más adecuada es la virtualización de sistema operativo. Con ella el administrador tiene un control total de los usuarios, permitiendo y denegando las operaciones y permisos que pueden realizar para definir qué tipo de usuarios son.

* Creación de un sistema eficiente de web + middleware + base de datos: La más adecuada es la virtualización completa. De esta manera podremos modificar características del kernel para ganar en eficiencia, algo fundamental en un sistema web con base de datos.

* Sistema de prueba de software e integración continua: La virtualización de entornos de desarrollo es la opción más adecuada por permitirnos reproducir de forma precisa los distintos entornos. Esta virtualización está orienta al propósito que se desea.

**2 - Crear un programa simple en cualquier lenguaje interpretado para Linux, empaquetarlo con CDE y probarlo en diferentes distribuciones.**

He seguido el siguiente [tutorial](http://blog.desdelinux.net/como-crear-aplicaciones-portables-de-linux/)

En lugar de hacer sobre la aplicación xclock lo hice sobre un script que mostraba hola mundo. Fue probado en Ubuntu y Fedora.

###Ejercicio 4:
**Hacer el tutorial de línea de órdenes de docker para comprender cómo funciona.**

Tutorial realizado.

###Ejercicio 5:

**Instala el sistema de gestión de fuentes git**

Instalado git con el comando:

    $ yum install git

Comprobado que versión ha sido instalada con:

    $ git --version
    git version 1.9.3

###Ejercicio 6:
**1 - Crear un proyecto y descargárselo con git. Al crearlo se marca la opción de incluir el fichero README**

Creamos el repositorio desde la web aprovechando que ya estamos autenticados.
Desde el terminal creamos el archivo README.md y lo subimos:

    touch README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/JMailloH/prueba.git
    git push -u origin master

**2 - Modificar el readme y subir el fichero modificado.**

Para actualizar el archivo README.md podríamos hacer:

Modificamos el archivo con el editor que más nos guste.

    git add README.md
    git commit -m "Commit de prueba"
    git push

###Ejercicio 7:
**Comprobar si en la instalación hecha se ha instalado cgroups y en qué punto está montado, así como qué contiene.**

La instalación por defecto si tiene instalado cgroups. La distribución de Linux que estoy utilizando es Fedora 20. Está montado en /sys/fs/cgroup al igual que pasa con Ubuntu 14.04. El contenido es:

* blkio
* cpuacct
* cpuset
* freezer
* memory
* perf_event
* cpu
* cpu,cpuacct
* devices
* hugetlb
* net_cls
* systemd

###Ejercicio 8:
**1 - Crear diferentes grupos de control sobre un sistema operativo Linux. Ejecutar en uno de ellos el navegador, en otro un procesador de textos y en uno último cualquier otro proceso. Comparar el uso de recursos de unos y otros durante un tiempo determinado.**

Nos situamos en la carpeta

    cd /sys/fs/cgroup

Creamos una carpeta para cada grupo de control. Se llamarán navegador, textos y libreoffice:

    mkdir navegador textos libreoffice

Asignamos CPUs y memoria por defecto (para cada carpeta):

    echo 0 > cpuset.cpus
    echo 0 > cpuset.mems

Asignamos el PID de cada proceso a los grupos creados (para cada carpeta):

    echo XXX > tasks

Ya podemos consultar con el archivo cpuacct.usage su uso.

###Ejercicio 9:
**2 - Implementar usando el fichero de configuración de cgcreate una política que dé menos prioridad a los procesos de usuario que a los procesos del sistema (o viceversa).**

Modificaremos el fichero etc/cgconfig.conf para que se cumplan los requisitos especificados.

    mount { cpu = /cgroup/cpu }

    group sistema {
        cpu { cpu.shares="750"; }
    }

    group usuarios {
        cpu { cpu.shares="250"; }
    }

**3 - Usar un programa que muestre en tiempo real la carga del sistema tal como htopy comprobar los efectos de la migración en tiempo real de una tarea pesada de un procesador a otro (si se tiene dos núcleos en el sistema).**

Para el estudio de la migración se ha utilizado el editor de textos libre office.
El grupo ejer9 tiene dentro los subgrupos prueba y migracion. Prueba será ejecutado en el núcleo 0 y migración en el núcleo 3.

Asignamos el proceso como se ha realizado en el ejercicio anterior y observamos que su uso es aproximadamente del 1%.

 Posteriormente se le pasa la tarea migracion con el comando cgclassify -g memory,cpu:migraion 2211 (Que es el PID). Observamos como el núcleo 3 usa el 2.3%.

**4 - Configurar un servidor para que el servidor web que se ejecute reciba mayor prioridad de entrada/salida que el resto de los usuarios.**

Igual que el apartado dos, pero sobre la prioridad de salida.

    mount { blkio = /cgroup/blkio }

    group servidor {
        blkio { blkio.weight="750"; }
    }

    group demas {
        blkio { blkio.weight="250"; }
    }

###Ejercicio 10:
**Comprobar si el procesador o procesadores instalados tienen estos flags. ¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden?**

Como salida a la instrucción egrep '^flags.*(vmx|svm)' /proc/cpuinfo no se obtiene nada. Lo cual indica que no está activa la virtualización

Realizando un cat del fichero /proc/cpuinfo vemos que el procesador es:

    Intel(R) Core(TM) i7-4700HQ CPU @ 2.40GHz

Y que los flags activos son:

    flags : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc aperfmperf eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm ida arat epb xsaveopt pln pts dtherm fsgsbase smep

###Ejercicio 11:
**Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden kvm-ok.**

Puesto que no soporta virtualización hardware, lo otra opción es instalar la virtualización por software.

    sudo yum install qemu-kvm

###Ejercicio 12:
**Comentar diferentes soluciones de Software as a Service de uso habitual.**

Existen numerosas aplicaciones que pueden ser incluidas dentro del concepto SaaS. Veamos con algunos ejemplos de los más conocidos a que se refiere:

Gestores de correo electrónico como Gmail, Outlook y Yahoo también son ejemplos de aplicaciones SaaS.
Google Docs permite trabajar con un editor de textos desde la web.

Todas ellas son consideradas como SaaS (Software as a Service – Software como servicio) por cumplir unas características básicas:

* El cliente disfruta del servicio mediante internet.
* El servidor es el encargado del mantenimiento, copias de respaldo, configuración, actualización, etc.
* El cliente solo se debe de preocupar de la configuración personal sobre las características del servicio que va a utilizar, pero no debe hacerlo de instalaciones, mantenimiento, etc.

*Corrección de sergiogvz: Los servicios de almacenamiento suele no considerarse SaaS, ya que proveen eso, solo almacenamiento. Los SaaS son más aquellos servicios encontrados normalmente en aplicaciones de escritorio, por ejemplo, como bien has indicado: gestores de correo o aplicaciones de ofimática.*

- - -

##Tema 2

###Ejercicio 1:
**Instalar un entorno virtual para tu lenguaje de programación favorito (uno de los mencionados arriba, obviamente).**

He decidido instalar virtualenv para Python, por tener algo más de conocimiento sobre Python que sobre los demás lenguajes.

###Ejercicio 2:
**Darse de alta en algún servicio PaaS tal como Heroku, Nodejitsu u OpenShift.**

He decidido hacerme la cuenta en Heroku. También me la he hecho en OpenShift puesto que lo pide el siguiente ejercicio.

###Ejercicio 3:
**Crear una aplicación en OpenShift y dentro de ella instalar WordPress.**

Ya he creado el WordPress. En el siguiente enlace se puede ver. Lo he realizado con OpenShift

https://jmailloh-wpejercicio3.rhcloud.com/

###Ejercicio 4:
**Crear un script para un documento Google y cambiarle el nombre con el que aparece en el menú, así como la función a la que llama.**

El siguiente script modifica el nombre del archivo que abrimos.

```
function ejer4(){
  var doc = DocumentApp.getActiveDocument();
  doc.setName("Ejercicio4")
}
```


###Ejercicio 5:
**Buscar un sistema de automatización de la construcción para el lenguaje de programación y entorno de desarrollo que usemos habitualmente.**

El sistema que se ha visto en el desarrollo de los estudios universitarios es make (para lenguaje C y C++) mediante los ficheros makefile. Un ejemplo lo podemos ver [aqui](http://www.cplusplus.com/forum/unices/12499/)

El TFG lo he realizado en Java utilizando Ant, y actualmente estamos viendo el uso Maven.

Para Python existe [Pynt](http://pynt.sourceforge.net/), el cual no he llegado a utilizar pero se encarga de las dependencias y posibilita el uso de parámetros en línea de comandos.

###Ejercicio 6:
**Identificar, dentro del PaaS elegido o cualquier otro en el que se dé uno de alta, cuál es el fichero de automatización de construcción e indicar qué herramienta usa para la construcción y el proceso que sigue en la misma.**

En el ejercicio tercero elegí OpenShift, el cual provee la integración continua mediante [Jenkins](http://jenkins-ci.org/).

No lo hace de forma directa, para ello hay que instalar cartuchos propios para cada uno de los proyectos, dependiendo del lenguaje utilizado.

Si algún compañero quiere completar como lo realiza Jenkins sería perfecto.

###Ejercicio 7:
**Buscar un entorno de pruebas para el lenguaje de programación y entorno de desarrollo que usemos habitualmente.**

Para python se puede utilizar el módulo [unittest](https://docs.python.org/2/library/unittest.html).
En [este](http://pythontesting.net/framework/unittest/unittest-introduction/) enlace se puede ver un tutorial sobre su uso.

<<<<<<< HEAD
Sí es cierto que para programar los tests en python, se puede usar [unittest](https://docs.python.org/2/library/unittest.html), pero para ejecutarlos no se suele hacer a mano. Habitualmente, en el entorno python, se utiliza [nose](https://nose.readthedocs.org/en/latest/) que ejecuta los test de forma automática y los resultados se dan en OK o No Ok, si se han pasado o no.
=======
Sí es cierto que para programar los tests en python, se puede usar [unittest](https://docs.python.org/2/library/unittest.html), pero para ejecutarlos no se suele hacer a mano. Habitualmente, en el entorno python, se utiliza nose que ejecutalos de forma automática y los resultados se dan en OK o No Ok, si se han pasado o no.

- - -

##Tema 3

###Ejercicio 1:
**Crear un espacio de nombres y montar en él una imagen ISO de un CD de forma que no se pueda leer más que desde él. Pista: en ServerFault nos explican como hacerlo, usando el dispositivo loopback**

Comenzamos creando el espacio de nombre UTS, con la instrucción:

```
sudo unshare -u /bin/bash
```

El siguiente paso sería montar la iso:

```
mount -o loop -t iso9660 mi_archivo.iso /mnt/test
```

Donde loop indica que el comando mount use el primer /dev/loopX disponible

>>>>>>> 55a69c4b3d82551622826284b1c0381862e0e557
