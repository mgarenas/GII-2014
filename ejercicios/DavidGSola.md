Ejercicios de David González Sola
=====================================

## Sesión 17-octubre-2014

### Ejercicio 1

- **Nombre:** HP ProLiant ML310e G8 XE
- **Precio (con IVA):** 833€
- **Precio (sin IVA):** 688.43€
- **Amortización en 4 años:** 172.11€ por año
- **Amortización en 7 años:** 98.35€ por año
- **Referencia:** http://www.pccomponentes.com/hp_proliant_ml310e_g8_xe_e3_1220_8gb_2tb___foundation_2012.html

### Ejercicio 2

Se han elegido:
- **Amazon Web Services:** paquete m3.2xlarge con 8 núcleos, 30GB de memoria a un precio de 0.616$ la hora.
- **Google Compute Engine:** paquete n1-standard-8 con 8 núcleos, 30GB de memoria a un precio de 0.616$ la hora.

En AWS es necesario un pago anticipado a sumar al coste por horas. Sin embargo, en GCE no es necesaria realizar ningún tipo de pago anticipado.

Coste usando el 1% del tiempo:
- **Amazon Web Services:** 0.616$/horas * 87.6 horas = 53.96 $ + 439$ (pago anticipado) = 492.96$
- **Google Compute Engine:** 0.616$/horas * 87.6 horas = 53.96 $

Coste usando el 10% del tiempo: 
- **Amazon Web Services:** 0.616$/horas * 876 horas = 539.6 $ + 439$ (pago anticipado) = 978.6$
- **Google Compute Engine:** 0.616$/horas * 876 horas = 539.6 $

### Ejercicio 3

- **Alojar varios clientes en un sólo servidor:** utilizaría una virtualización a nivel de SO con el fin de que cada cliente se encuentre aislado del resto.
- **Crear un sistema eficiente web + middleware + bd:** yo no utilizaría una virtualización plena ya que consume muchos recursos y la eficiencia se reduciría drasticamente. Utilizaría una virtualización a nivel de aplicación.
- **Sistema de pruebas software e integración continua:** utilizaría una virtualización de entornos de desarrollo pudiendo reproducir fielmente el entorno de producción.

### Ejercicio 4

Respuestas:

1. docker version
2. docker search tutorial
3. docker pull learn/tutorial
4. docker run learn/tutorial echo "hello world"
5. docker run learn/tutorial apt-get install -y ping
6. docker commit 698 learn/ping
7. docker run learn/ping www.google.com
8. 
	- docker ps 
	- docker inspect efefdc74a1d5
9. docker push learn/ping

### Ejercicio 5

apt-get install git

### Ejercicio 6

Se crea desde la web www.github.com el repositorio. Posteriormente es necesario descargarlo en local utilizando el comando 'git clone http://www.github.com/DavidGSola/CloudComputing.git'. Se modifica el fichero README con cualquier editor de textos y finalmente se vuelve a subir al repositorio en la nube utilizando el comando 'git commit' y 'git push'.

### Ejercicio 7

En Ubuntu 12.04 se encuentra montado en /sys/fs/cgroups. Contiene gran cantidad de archivos como por ejemplo:
blkio.io_merged                   cpuset.memory_spread_page
blkio.io_queued                   cpuset.memory_spread_slab
blkio.io_service_bytes            cpuset.mems
blkio.io_serviced                 cpuset.sched_load_balance
blkio.io_service_time             cpuset.sched_relax_domain_level

### Ejercicio 8.1

Se han creado tres grupos:
	- **Buenos:** ejecutarán el navegador. (cpu usage: 31107072)
	- **Regulares:** ejecutarán el procesador de textos. (cpu usage: 1094374)
	- **Malos:** ejecutarán gimp. (cpu usage: 176661809)

### Ejercicio 8.2


### Ejercicio 9.1

### Ejercicio 9.2

Se debe crear el archivo de configuración '/etc/cgconfig.conf'. Un ejemplo de este archivo donde se de prioridad a los procesos del usuario sería:

mount {
	cpu = /cgroup/cpu
}

group usuario {
	cpu {
		cpu.shares="900";
	}
}

group sistema {
	cpu {
		cpu.shares="100";
	}
}

### Ejercicio 9.3


