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
Se han comparado una instancia virtual de **Google Compute Ingine** con una de **Amazon Web Service**. Ambas poseen 4 nucleos virtuales de procesadores similares al Intel Xeon E5-2670 con 16GB de RAM.

La instancia de Google es la **n1-standard-4** que cuesta 0,276$/h
La instancia de Amazon es la **m3.xlarge** que cuesta un primer pago anticipado $439 mas una cuota de 0,308$/h

Teniendo esto en cuenta realizamos los calulos para
**1%**
-Amazon: 439$ + 87,6h * 0,308$/h = 465,98$
-Google: 87,6h * 0,276$/h = 24,17 $

**10%**
-Amazon: 439$ + 876h * 0,308$/h =4659,8 $
-Google: 876h * 0,276$/h = 241,77 $

### Ejercicio 3

1. Alojar varios clientes en un sólo servidor. Utilizaria un sistema de virtualizacion a nivel de sistema operativo para que cada cliente pudiese realizar sus tareas independientemente del número de clientes alojados en el servidor, ya que estos se encuentran aislados unos de otros.

2. Crear un sistema eficiente de web + middleware + base de datos. Utilizaría un sistema de virtualización pleno porque me permitirá virtualizar un sistema completo. Gracias a los programas de control se abarcarían las necesidades de crear un sistema web, middleware y una base de datos. 

3. Sistema de prueba de software de integración continua. La virtualización de entornos de desarrollo nos permitiría abordar el supuesto sistema, ya que nos facilita la labor de verificación de una aplicación en distintas versiones con una sola orden, así como, reescribirlo en diferentes lenguajes.

### Ejercicio 4

Para realizar el ejercicio se han introducido dentro del simulador, se han seguido los siguientes:
- docker version
- docker search tutorial
- docker pull learn/tutorial
- docker run learn/tutorial apt-get install -y ping
- docker ps -l
- docker commit 6982 learn/ping
- docker ps -l
- docker run learn/ping ping google.com
- docker ps -l
- docker inspect efe

### Ejercicio 5

Se ha instalado el sistema de gestión de fuentes git con el commando:
- sudo apt-get install git

### Ejercicio 6

Para realizar este ejercicio se han seguido las siguientes órdenes.
- He creado en GitHub un nuevo repositorio con el nombre "MiProyecto" junto con el archivo README
- git clone https://github.com/Georgevik/MiProyecto.git
- cd MiProyecto
- gedit README.md
- git commit -m "Primera modificacion"

### Ejercicio 7
- apt-get install cgroup-lite
- ls blkio cpuacct devices hugetlb perf_event cpu cpuset freezer memory systemd

### Ejercicio 8

No he podido realizarlo porque al intentar montar el cgroup me dice que ya se encuentra montado y no me crea los subdirectorios que debería.


### Ejercicio 9
**Parte 1**
La limitacion de recursos o de asignación puede ser muy útil en el momento en el que tenemos que tenemos que modificar partes de un servicio que no puede pararse. Podemos poner por ejemplo un servidor que esta dando soporte a aplicaciones Android. Es clave que el servicio no se interrumpa, sin embargo podemos realizar tareas bajando el rendimiento a este servicio. De este modo, podemos modificar la parte del servidor necesaria sin tener que interrumpir el servicio.

Otro escenerio es cuando dos usuarios interactúan con los recursos de un mismo ordenador. Esto permite que ambos usuarios puedan trabajar sin "molestarse" entre ellos.

Tambien es util en el momento de proveer una granja de hosting. Con un solo ordenador particionamos los recursos y se lo vendemos a los clientes.

**Parte 2**

No he podido hacer el ejercicio ya que no me deja montar el cgroup. No obstante, en teoria una vez creado los procesos, la prioridad se estableceria de la siguiente forma en el fichero "cgconfig.conf"

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

**Parte 3, 4**

No he podido realizarlo por el problema que he tenido en el Ejercicio 8.


### Ejercicio 10

El modelo de procesador es: Intel(R) Core(TM) i5-3427U CPU @ 1.80GHz

La salida que obtengo con el comando es:
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor **vmx** ds_cpl smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm ida arat xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms

Como podemos ver, mi procesador tiene activado el flag de vmx

### Ejercicio 11

He tenido que instalar el paquete cpu-checker y la salida al comando "kvm-ok" es la siguiente:
INFO: /dev/kvm exists
KVM acceleration can be used





