Ejercicios
======

Tema1
======

1 Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. Consultar este artículo en Infoautónomos sobre el tema. 

	Servidor Dell PowerEdge T110 II: 329€ 
	(http://www.dell.com/es/empresas/p/poweredge-t110-2/pd)

	Para amortizarlo en cuatro años, su coste de amortización es de 6'86€/mes, lo que supone un coste de amortización de 82'25€ al año (un 		25% del precio).

	Para amortizarlo en siete años, su coste de amortización es de 3'92€/mes, 47€ al año, un 14'29% al año.

2 Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, Comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo
	
3.1 ¿Qué tipo de virtualización usarías en cada caso? Comentar en el foro

Alojar varios clientes en un sólo servidor: A nivel de Sistema Operativo, ya que permite que los todos invitados posean cuentas totalmente independientes unas de otras y, como han comentado mis compañeros, al utilizar el mismo sistema operativo que el anfitrión, éstos pueden despreocuparse de las actualizaciones y demás tareas de administración, las cuales serían llevadas por el administrador.

Crear un sistema eficiente de web + middleware + base de datos: Al igual que DavidGSola, utilizaría una virtualización a nivel de aplicación, dado que considero esencial reducir al máximo el uso de los recursos y, en el caso de una virtualización plena o de sistema operativo, es necesario consumir gran cantidad de recursos.

Sistema de prueba de software e integración continua: Virtualización de entornos para así poder probar el comportamiento del software generado en los distintos entornos que se deseen probar.

3.2Crear un programa simple en cualquier lenguaje interpretado para Linux, empaquetarlo con CDE y probarlo en diferentes distribuciones.



4.1 Hacer el tutorial de línea de órdenes de docker para comprender cómo funciona.
4.2Avanzado Instalarlo y crear una aplicación contenedorizada.

5.Instala el sistema de gestión de fuentes git
	sudo apt-get install git

6.1 Crear un proyecto y descargárselo con git. Al crearlo se marca la opción de incluir el fichero README.
6.2 Modificar el readme y subir el fichero modificado


7.Comprobar si en la instalación hecha se ha instalado cgroups y en qué punto está montado, así como qué contiene.


 8.1Crear diferentes grupos de control sobre un sistema operativo Linux. Ejecutar en uno de ellos el navegador, en otro un procesador de textos y en uno último cualquier otro proceso. Comparar el uso de recursos de unos y otros durante un tiempo determinado.

 8.2Calcular el coste real de uso de recursos de un ordenador teniendo en cuenta sus costes de amortización. Añadir los costes eléctricos correspondientes.



9.1Discutir diferentes escenarios de limitación de uso de recursos o de asignación de los mismos a una u otra CPU.
9.2Implementar usando el fichero de configuración de cgcreate una política que dé menos prioridad a los procesos de usuario que a los procesos del sistema (o viceversa).
9.3Usar un programa que muestre en tiempo real la carga del sistema tal como htopy comprobar los efectos de la migración en tiempo real de una tarea pesada de un procesador a otro (si se tiene dos núcleos en el sistema).
9.4Configurar un servidor para que el servidor web que se ejecute reciba mayor prioridad de entrada/salida que el resto de los usuarios.

10.1Comprobar si el procesador o procesadores instalados tienen estos flags. ¿Qué modelo de procesador es? 
Intel Core i5 <....>
10.2¿Qué aparece como salida de esa orden?

11.Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden kvm-ok

12.Comentar diferentes soluciones de Software as a Service de uso habitual

Seminario Ruby
======
1 Instalar Ruby y usar ruby –version
	ruby 1.9.3p484 (2013-11-22 revision 43786) [x86_64-linux]
	Los paquetes irb, rubygems y rdoc ya se instalaron con el paquete ruby.


2 Crear un programa en Ruby que imprima los números desde el 1 hasta otro contenido en una variable
	#!/usr/bin/ruby 
	numero = 10 
	i = 1 
	while (i <= 10) 
		puts i 
		i +=1 
	end

3 ¿Se pueden crear estructuras de datos mixtas en Ruby? Crear un array de hashes de arrays e imprimirlo.
