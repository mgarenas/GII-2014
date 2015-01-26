Ejercicios de Daniel Díaz Salas
===============================

#Tema 1

Ejercicio 1
-----------
Para este ejercicio he elegido el [Fujitsu Primergy TX300 S8 Formato Torre](http://www.pccomponentes.com/fujitsu_primergy_tx300_s8_formato_torre.html "PcComponentes").

El precio con IVA es de 899€, y sin IVA 742.98€. Por lo tanto se puede amortizar a 4 años a **185.75€** y  **106.14€** a 7 años.

Ejercicio 2
-----------

Para este ejercicio he elegido estos dos servicios:
###[Google Cloud Platform](https://cloud.google.com/products/calculator/ "Google Cloud")###
Un servidor con:
- 2 cores.
- 7.5 GB de RAM.
- Resto de opciones por defecto.
- Precio: 22.74$ al mes por un uso inferior al 25%.
Un disco persistente con:
- 100 GB de SSD.
- Resto de opciones por defecto.
- Precio: 32.50 al mes.

- Precio por usarlo un 1%:
    + Precio servidor por hora: 22.74 $/mes / (30 días/mes * 24 horas/día) = 0.03158 $/hora (Servidor de procesamiento)
    + Precio servidor por año: 0.03158 $/hora * 24 horas/día * 30 días/mes * 12 meses/año / 100 = 2.728512 $/año
    + Precio disco duro por año: 32.50 $/mes * 12 meses/año = 325 $/año
    + **Precio total: 325 $/año + 2.728512 $/año = 327.73 €/año**
- Precio por usarlo un 10%:
    + Precio servidor por año = 27.28512 $/año
    + **Precio total: 325 $/año + 27.28512 $/año = 352.29 €/año**    

###[Microsoft Azure](http://azure.microsoft.com/es-es/pricing/calculator/?scenario=cloud "Microsoft Azure")###
Una Instancia de rol web y de trabajo con un D2 que tiene:
- 2 cores.
- 7 GB de RAM.
- 100 GB de SSD.
**Precio: €0,237/hr**

- Precio por usarlo un 1%:
    + Precio servidor por año = 0.237 $/hora * 24 horas/día * 30 días/mes * 12 meses/año / 100 = **20.48 €/año**.
- Precio por usarlo un 10%:
    + Precio servidor por año = 20.48 €/año * 10 = **204.8€/año**.

Ejercicio 3
-----------
###Primera parte###
- **Varios clientes en un servidor**: usaría virtualización a nivel de sistema operativo, ya que aisla los invitados y el anfitrión.
- **Un sistema eficiente de web + middleware + base de datos**: como se necesita tanto espacio de disco, mucha memoria y un procesador para hacer las consultas no queda otra que utilizar virtualización plena.
- **Un sistema de prueba de software e integración continua**: usaría virtualización de entornos de desarrollo, de todas las opciones es la más obvia

###Segunda parte###
La segunda parte se tarda demasiado tiempo.

Ejercicio 4
------------
![El resultado del tutorial está guardado en la imagen DanielDíazSalas-Ejercicio4Tema1.jpg](/ejercicios/DanielDíazSalas-Ejercicio4Tema1.jpg)

Ejercicio 5
-----------
sudo apt-get install git

Ejercicio 6
-----------
###Primera parte###
Se ha creado [este](https://github.com/potray/Ejercicio6CC) repositorio.
###Segunda parte###
[El readme está aquí](https://github.com/potray/Ejercicio6CC/blob/master/README.md)

Ejercicio 7
-----------
Tras montarlo hay todo esto:

>blkio.io_merged                   cpuset.memory_pressure
blkio.io_merged_recursive         cpuset.memory_pressure_enabled
blkio.io_queued                   cpuset.memory_spread_page
blkio.io_queued_recursive         cpuset.memory_spread_slab
blkio.io_service_bytes            cpuset.mems
blkio.io_service_bytes_recursive  cpuset.sched_load_balance
blkio.io_serviced                 cpuset.sched_relax_domain_level
blkio.io_serviced_recursive       cpu.shares
blkio.io_service_time             cpu.stat
blkio.io_service_time_recursive   devices.allow
blkio.io_wait_time                devices.deny
blkio.io_wait_time_recursive      devices.list
blkio.leaf_weight                 hugetlb.2MB.failcnt
blkio.leaf_weight_device          hugetlb.2MB.limit_in_bytes
blkio.reset_stats                 hugetlb.2MB.max_usage_in_bytes
blkio.sectors                     hugetlb.2MB.usage_in_bytes
blkio.sectors_recursive           memory.failcnt
blkio.throttle.io_service_bytes   memory.force_empty
blkio.throttle.io_serviced        memory.kmem.failcnt
blkio.throttle.read_bps_device    memory.kmem.limit_in_bytes
blkio.throttle.read_iops_device   memory.kmem.max_usage_in_bytes
blkio.throttle.write_bps_device   memory.kmem.slabinfo
blkio.throttle.write_iops_device  memory.kmem.tcp.failcnt
blkio.time                        memory.kmem.tcp.limit_in_bytes
blkio.time_recursive              memory.kmem.tcp.max_usage_in_bytes
blkio.weight                      memory.kmem.tcp.usage_in_bytes
blkio.weight_device               memory.kmem.usage_in_bytes
cgroup.clone_children             memory.limit_in_bytes
cgroup.event_control              memory.max_usage_in_bytes
cgroup.procs                      memory.move_charge_at_immigrate
cgroup.sane_behavior              memory.numa_stat
cpuacct.stat                      memory.oom_control
cpuacct.usage                     memory.pressure_level
cpuacct.usage_percpu              memory.soft_limit_in_bytes
cpu.cfs_period_us                 memory.stat
cpu.cfs_quota_us                  memory.swappiness
cpuset.cpu_exclusive              memory.usage_in_bytes
cpuset.cpus                       memory.use_hierarchy
cpuset.mem_exclusive              notify_on_release
cpuset.mem_hardwall               release_agent
cpuset.memory_migrate             tasks

Ejercicio 8
-----------
###Primera parte###
**Crear grupos de control**
- mkdir patata
- mkdir cebolla
- mkdir zanahoria
**Poner los ceros necesarios**
- echo 0 >patata/cpuset.cpus
- echo 0 >cebolla/cpuset.cpus
- echo 0 >zanahoria/cpuset.cpus
- echo 0 >patata/cpuset.mems
- echo 0 >cebolla/cpuset.mems
- echo 0 >zanahoria/cpuset.mems
**Asignar tareas**
- Procesador de textos: echo 8017 > patata/tasks 
- Navegador: echo 2167 > cebolla/tasks
- Otro (Sublime Text 2): echo 7559 > zanahoria/tasks
**Uso de la CPU**
cat patata/cpuacct.usage;cat cebolla/cpuacct.usage;cat zanahoria/cpuacct.usage
>28005970
2857766542
128580041

Claramente el navegador usa más recursos, seguido de Sublime Text.

###Segunda parte###
Demasiado confusa.

Ejercicio 9
------------

###Primera parte###
404 not found

###Segunda parte###
mount {cpu = /cgroup/cpu}

group usuarios {
    cpu {
        cpu.shares="250";
    }
}

group sistema {
    cpu {
        cpu.shares="500";
    }
}

###Tercera parte###

Creé los grupos "teveo" y "usuarios" utilizando la órden cgcreate. A continuación edité los ficheros /sys/fs/cgroup/cpu/<grupo>/cpu.shares para cambiarle a 250 el de usuarios y a 750 el de teveo.

Para ejecutar el procesador de textos de OpenOffice bajo el grupo "usuarios":

>sudo cgexec -g memory,cpu,cpuacct:usuarios lowriter

Para cambiarlo:

>sudo cgclassify -g memory,cpu,cpuacct:teveo 10047

Se observa una diferencia mínima: del 1.2% ha pasado al 1.5%, siendo estos valores máximos alcanzados, ya que el uso de la CPU ha ido oscilando.

###Cuarta parte###

group servidorWeb {
    blkio{
        blkio.weigh="500";
    }
}

group otros {
    blkio{
        blkio.weigh="250";
    }
}

Ejercicio 10
------------

Mi procesador es un Intel(R) Core(TM) i5 CPU M 450  @ 2.40GHz. 

Los flags que tengo son los siguientes:
>fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt lahf_lm ida arat dtherm tpr_shadow vnmi flexpriority ept vpid

Ejercicio 11
------------

Esta es la salida de la orden:

>INFO: /dev/kvm exists
KVM acceleration can be used

Por lo que si que tiene el módulo.

Ejercicio 12
------------
El SaaS si lo pensamos es una forma de desarrollar software bastante diferente a la "normal". Cuando tú desarrollas un software para alguien, ese software es un **producto**, sin embargo SaaS es software como un servicio.

Uno de los inconvenientes de lo que no he visto que nadie haya comentado es el que no se puede cambiar el software que se te ofrece. Esto parece una perogrullada, pero muchas veces el software no hace exactamente lo necesario, y el no poder cambiar este hecho es un inconveniente bastante grande.

#Tema 2

Ejercicio 1
-----------
He elegido Virtualenv.  

Primero instalo python:
>sudo apt-get install python-pip

Después instalo Virutalenv:
>sudo pip install virtualenv

Ejercicio 2
-----------
Aprovecho que ya estaba dado de alta en **Heroku**.

Ejercicio 3
----------
Desaprovecho el que ya estaba dado de alta en **Heroku** y doy de alta en **Openshift**

[WordPress instalado](http://potray-wordpressejer3cc.rhcloud.com/)

Ejercicio 4
-----------
![El resultado del tutorial está guardado en la imagen DanielDíazSalas-Ejercicio4Tema2.jpg](/ejercicios/DanielDíazSalas-Ejercicio4Tema2.jpg)

Google Docs no deja añadir cosas al menú: la API nueva no es compatible y la vieja no funciona.

Ejercicio 5
-----------
Para Python (Django) se pueden usar Make.

Ejercicio 6
-----------
Google App Engine no tiene una herramienta para automatizar las construcciones, pero sí tiene una SDK que permite construir en local fácilmente.

Ejercicio 7
-----------
Habitualmente yo uso Java para programar cosas, y para realizar pruebas se usa JUnit.

Los test en Django se hacen usando el módulo [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) que está en la biblioteca estándar de Python.

#Tema 3

Ejercicio 1
-----------

>sudo unshare -u /bin/bash
>mount -o loop -t iso9660 ubuntu-14.04.1-desktop-amd64.iso /mnt/test

Ejercicio 2
-----------

###Primera parte###

>ip addr show
bridge name bridge id       STP enabled interfaces
alcantara       8000.c80aa9a0f0b7   no      eth0

###Segunda parte###
Crear una interfaz nueva
>sudo btctl addif ejercicio2

Asignarlo al interfaz de la tarjeta wifi
>sudo brctl addif ejercicio2 wlan0

Por desgracia no deja hacerlo:
>can't add wlan0 to bridge ejercicio2: Operation not supported

Ejercicio 3
-----------

Crear una carpeta donde va a ir la distro
>mkdir ~/CC
mkdir ~/CC/Tema3Ejer3

Crear el sistema con deboostrap
>sudo debootstrap --arch=amd64 saucy ~/CC/Tema3Ejer3/ http://archive.ubuntu.com/ubuntu

Ejercicio 4
-----------

Ejercicio 5
-----------

Ejercicio 6
-----------


#Tema 4

Ejercicio 1
-----------

>sudo apt-get install lxc

Ejercicio 2
-----------

> sudo lxc-create -t ubuntu -n una-caja
> sudo lxc-start -n una-caja
> ip addr show

4: lxcbr0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether fe:5c:a7:02:55:db brd ff:ff:ff:ff:ff:ff
    inet 10.0.3.1/24 brd 10.0.3.255 scope global lxcbr0
       valid_lft forever preferred_lft forever
    inet6 fe80::7cb9:4ff:fe29:5db0/64 scope link 
       valid_lft forever preferred_lft forever
6: vethAY1US6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master lxcbr0 state UP group default qlen 1000
    link/ether fe:5c:a7:02:55:db brd ff:ff:ff:ff:ff:ff
    inet6 fe80::fc5c:a7ff:fe02:55db/64 scope link 
       valid_lft forever preferred_lft forever


Ejercicio 3
-----------
###Primera parte###
> sudo lxc-create -t debian -n ejer3
> sudo lxc-start -n ejer3
 
###Segunda parte###
He usado el script del compañero.

Ejercicio 4
-----------
###Primera parte###
>wget http://lxc-webpanel.github.io/tools/install.sh -O - | bash

Al utilizar este comando me da el siguiente error:
> No se puede escribir a “-” (Tubería rota).

Que no he sido capaz de arreglar.

###Segunda parte###
Al no haber sido capaz de hacer la primera parte no puedo hacer la segunda.

Ejercicio 5
-----------
>sudo apt-get install nginx

Para ejecutarlo:
>service nginx start

Metiéndote en localhost:80 aparece la pantalla de nginx.
No sé qué más hacer.

Ejercicio 6
-----------
###Primera Parte###
>sudo add-apt-repository ppa:juju/stable
sudo apt-get update && sudo apt-get install juju-core

Cambiamos la línea
>default: Amazon

a

>default: local
###Segunda Parte###

Ejercicio 7
-----------

Ejercicio 8
-----------

Ejercicio 9
-----------

Ejercicio 10
------------

Ejercicio 11
------------



