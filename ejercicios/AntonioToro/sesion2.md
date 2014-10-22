Sesión 2
========

## Ejercicio 1
Consultar en el catálogo de alguna tienda de informática el precio de un 
ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. 
Consultar [este artículo en Infoautónomos sobre el tema](http://www.infoautonomos.com/consultas-a-la-comunidad/988/).

- [Servidor torre PowerEdge T620](http://www.dell.com/es/empresas/p/poweredge-t620/pd)
- 579€ Sin IVA
- Amortización a cuatro años: 144.75€ por año.
- Amortización a siete años: 82.72€ por año.

## Ejercicio 2
Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, 
comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo 
tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro 
equivalente a transferencia de disco duro) si la infraestructura comprada se usa sólo el 1% o el 10% del tiempo.

Un año son _24 * 365 = 8760 horas_.

Se han elegido los servicios de [Microsoft Azure](http://azure.microsoft.com/es-es/pricing/details/cloud-services/) y [Google Compute Engine](https://cloud.google.com/compute/#pricing),
ambos alojados en Europa, en concreto, los paquetes __A5__ y __n1-highmem-2__, respectivamente.

Para un __1%__ de uso:
- __Microsoft Azure__: 0.01 * 8760 * _0,35$/h_ = __30.66 $__
- __Google Compute Engine__: 0.01 * 8760 * _0,18$/h_ = __15.768 $__

Para un __10%__ de uso:
- __Microsoft Azure__: 0.1 * 8760 * _0,35$/h_ = __306.6 $__
- __Google Compute Engine__: 0.1 * 8760 * _0,18$/h_ = __157.68 $__

## Ejercicio 3
¿Qué tipo de virtualización usarías en cada caso?

- __Alojamiento de varios clientes en un servidor__: Utilizaría una __virtualización a nivel de sistema operativo__ para que los clientes compartieran el _SO_ a la vez que cada uno estuviera aislado de los demás.
- __Sistema web + middleware + BD__: En este caso utilizaría una __virtualización plena__ para separar este sistema completamente del resto.
- __Sistema de prueba de software e integración continua__: Para este supuesto elegiría una __virtualización de entornos de desarrollo__ para reproducir de la manera más precisa posible entornos concretos.


