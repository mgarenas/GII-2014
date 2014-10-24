# Ejercicios

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



.........
---------
__Ejercicio 9__

Arrastramos el mismo problema que en el ejercicio 8 para realizarlo.

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


