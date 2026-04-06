Sistema de colas para designar orden de petición para comunicar distintos microservicios entre sí de forma asíncrona mediante varios protocolos.
Envío un mensaje con un Binding key y me multiplexa a cada cola interesada. Lo que cumple con el principio Open-Close, pues puedo escalar sin tocar la aplicación.

![[Pasted image 20240723132843.png]]
Entre las formas de enviarlo existe DIRECT (cola específica), TOPICS (grupo de colas con cierto patrón) y FANOUT (todos).

RabbitMQ opta por delegarle más responsabilidades a la parte del Broker (infraestructura), más lógica, que hace que el Consumer (implementación) sea más sencillo de realizar.
![[Pasted image 20240723134022.png]]
Por ejemplo, para enviar un email de bienvenida a un usuario, este sería el paso a paso.
![[Pasted image 20240723134452.png]]