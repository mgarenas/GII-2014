Ejercicios de Jose Manuel Rosell Sánchez
========================================

## Sesión 17-octubre-2014

###Ejercicio 1

El servidor ha sido sacado de la página web de *PcComponentes*, y se puede consultar [aquí.](http://www.pccomponentes.com/fujitsu_primergy_rx300_s8_formato_rack.html)

* La amortización a 4 años sería:
	* 627,27€ * 0,25 = 156,8175€ al año.

* La amortización a 7 años sería:
	* 627,27€ * 0,10 = 62,727€ primer y segundo año
	* 627,27€ * 0,20 = 125,534€ tercer, cuarto y quinto año
	* 627,27€ * 0,10 = 62,727€ sexto y séptimo año

La amortización nunca puede superar el 25% de la base imponible (base sin IVA) del servidor

###Ejercicio 2

Máquina | Cores CPU | RAM (GB) | Almacenamiento (GB) | Precio/año
--- | --- | --- | --- | ---
Amazon m3.large | 2 | 7.5 | 32 SSD | 959,95€
HP ProDesk 600 G1 | 4 | 4 | 500 S-ATA | 639€

- Si se usa el 1% del tiempo:
	* Amazon = 365 dias * 0,01 = 4 días * 2,63€/día = 10,52€/año
	* HP = 4 días * 1,75€/día = 7€/año

- Si se usa el 10% del tiempo:
	* Amazon = 365 dias * 0,1 = 37 días * 2,63€/día = 97,31€/año
	* HP = 37 días * 1,75€/día = 64,75€/año

###Ejercicio 3

####Apartado 1

* Para alojar varios clientes en un sólo servidor utilizaría virualización a nivel de sistema operativo, ya que como el anfitrión y el cliente utilizan el mismo sistema operativo, la comunicación entre ambos es mucho más fácil.

* Para crear un sistema eficiente de web + middleware + base de datos utilizaría una virtualización de aplicaciones, debido a que una base de datos consume muchos recursos y si se quiere que sea eficiente lo mejor es utilizar una virtualización a nivel de aplicación.

* Para un sistema de prueba de software e integración continua utilizaría una virtualización de entornos de desarrollo para reproducir los entornos de desarrollo fielmente.

####Apartado 2

```
#!/bin/bash
VARIABLE=Hola
SALUDO=mundo
echo
echo "$VARIABLE "" $SALUDO" 
echo
```

Para empaquetarlo se descarga el directorio y se hace `make`. Despues, se accede al directorio y se ejecuta `cde <ruta_del_archivo_a_empaqutar`. El portable del script tiene el nombre de `<nombre_del_scritp.cde>`.

###Ejercicio 4

Comandos del tutorial:
	* docker version
	* docker search tutorial
	* docker pull learn/tutorial
	* docker run learn/tutorial echo "hello world"
	* docker run learn/tutorial apt-get install -y ping
	* docker commit 698 learn/ping
	* docker run learn/ping ping google.com
	* docker inspect efe
	* docker push learn/ping

###Ejercicio 5

Para instalar con el comando `sudo apt-get install git` se instala git. Con el comando `git --version` se puede ver la versión instalad de Git.

###Ejercicio 6

####Apartado 1

Para crear un repositorio vamos a GitHub y lo creamos pulsando sobre el simbolo "+" que hay al lado de nuestro nombre de usuario. Para clonar el repositorio, copiamos la dirección que aparece en el menú de la derecha y desde línea de comandos escribimos: `git clone <dirección repositorio>`

####Apartado 2

Para modificar el archivo README, nos colocamos en el directorio clonado anteriormente he iniciamos Git utilizando `git init`. Modificamos el archivo README. Una vez modificado, utilizamos `git add README` y posteriorment `git commit -m "Un comentario"`. Ya esta listo para sincronizarlo con el servidor, para ello ejecutamos `git push origin master`. Si recargamos la página de GitHub nos aparecera el fichero README con la modificación realizada.

###Ejercicio 7

Sí esta instalado por defecto, y el directorio contiene:

```
blkio	cpuacct     devices	hugetlb	      perf_event
cpu 	cpuset	    freezer	memory	      systemd
``` 

###Ejercicio 8

####Apartado 1

Creamos tres grupos de control utilizando `mkdir`en el directorio `/sys/fs/cgroup`.

Creamos en el directorio `/sys/fs/cgroup/cpuset` el usuario *buenos*. Buscamos los procesos que hay mediante `ps` y el proceso de firefox se lo asignamos al usuario mediante el comando `echo xxx > /cgroup/buenos/tasks`, donde *xxx* se sustituye por el PID del proceso del navegador.

Repetimos el proceso cambiando el nombre de usuario por *regular* al que le asignamos la tarea del procesador de textos. Y al último usuario le ponemos el nombre *malos* y le asignamos la tarea bash.

Uso de cada usuario con su tarea:
	* **Buenos** = 1014638829
	* **Regular** = 135538
	* **Malos** = 37121973

####Apartado 2

###Ejercicio 9

####Apartado 2

Para crear el fichero *cgconfig.conf* se utiliza el comando `mount {<controller> = <path>}`. Para asignar la prioridad se utiliza
```
group <name> {
       	[permissions]
       		<controller> {
       	         <param name> = <param value>;
		}
	}
```

Un ejemplo donde se da menos prioridad a los procesos de usuario sería:
```
mount {cpu = /cgroup/cpu}

group usuario { 
	cpu { 
		cpu.shares="10"; 
            } 
	}

group sistema 
	{ cpu { 
		cpu.shares="20"; 
	      } 
	}
```

####Apartado 3

Se ha utilizado el navegador Firefox para comprobar los efectos de migración. Se utilizan los subgrupos *buenos* y *malos* pertenecientes al grupo *teestoyviendo*. Al primer subgrupo se le asigna el núcleo 0 y al segundo grupo se le asigna el grupo 4. Se le asigna el proceso del navegador al subgrupo *buenos* y teniendo un uso de un 0.7% de uso del procesador. Posteriormente se le pasa la tarea al subgrupo *malos* con el comando `cgclassify -g memory,cpu:malos 3369`. En el cambio, el núclo 4 usa un 2% de la CPU.

###Ejercicio 10

* **Modelo de procesador**: Intel(R) Core(TM) i3 CPU M 350 @ 2.27GHz
* **Salida de la orden**: flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 popcnt lahf_lm arat dtherm tpr_shadow vnmi flexpriority ept vpid

###Ejercicio 11

El nçucleo instalado en mi ordenador contiene el módulo KVM. El resultado de la ejecución del comando `kmv-ok`es:

```
INFO: /dev/kvm exists
KVM acceleration can be used
```

###Ejercicio12

Un ejemplo de Saas sería la web de [phixr](http://es.phixr.com/photo/userindex), que es un editor de fotos online. No necesitas instalar nada en la máquina local, solo tienes que acceder a la web y subir la foto que deseas modificar. Esto tiene evidentes problemas de privacidad y la incertidumbre de como la web puede utilizar las fotos que edites desde su web.

## Sesión 7-Noviembre-2014

###Ejercicio 1

Se instala **virtualenv** para Python con la orden `sudo apt-get install libc6-dev python-dev python-virtualenv`.

###Ejercicio 2

He creado una cuenta gratuita en **OpenShift**, con mi dirección de correo electrónico.

###Ejercicio 3

Se puede acceder al blog creado en WordPress desde OpenShift [en la esta URL](http://php-primeraapp.rhcloud.com/).

###Ejercicio 4

Para crear un script para un documento desde la dirección [script.google.com](script.google.com), de elige la opción *Drive* del menu que aparece. Se abre una ventana de script con dos funciones por defecto: 
```
function listFilesInFolder(id) {
  var folder = DriveApp.getFolderById(id);
  var contents = folder.getFiles();
  var file;
  var name;

  while(contents.hasNext()) {
    file = contents.next();
    name = file.getName();
    Logger.log(name);
  }
};

function moveFileToFolder(fileId, targetFolderId) {
  var targetFolder = DriveApp.getFolderById(targetFolderId);
  var file = DriveApp.getFileById(fileId);
  var currentFolders = file.getParents();
  while (currentFolders.hasNext()) {
    var currentFolder = currentFolders.next();
    currentFolder.removeFile(file);
  }
  targetFolder.addFile(file);
};
```
Se puede cambiar el nombre del proyecto en la parte superior izquierda pinchando y poniendo el nombre que se desee. En la parte de debajo de la barra de herramientas, donde aparece el simbolo del play, a la derecha de esta posición se puede seleccionar la función que se va a ejecutar.

###Ejercicio 5

El lenguaje de programación que utilizo habitualmente es **JAVA** y el sistema de automatización para la construcción que utilizo es **ant**. Para compilar un proyecto en JAVA utilizando ant se puede utilizar la instrucción: `ant -buildfile build.xml`.

###Ejercicio 6

###Ejercicio 7

El entorno de pruebas para el lenguaje de programación *Python* es *UnitTest*, aunque comúnmente se denomina *PyUnit*. [En este enlace](http://magmax.org/blog/2011/09/27/python-pruebas-2/) podemos encontrar un pequeño ejemplo de como hacer pruebas a una función en Python, codificado desde cualquier editor de texto y ejecutado desde la línea de comandos.








