Actúa como un router utilizando la indirección para manejar las distintas acciones o peticiones que lleguen y enviarlas a aquellos servicios interesados.

##### CommandDispatcher
Asíncrono, no espera respuesta, 1 a muchos.
- DDL, modificar los datos (INSERT, UPDATE, ETC)
- Necesita un objeto tipado para enlazarlo
##### EventDispatcher
Asíncrono, no espera respuesta, 1 a muchos.

##### QueryDispatcher
Síncrono, espera respuesta, 1 a 1.
- Búsqueda de datos (SELECT)

##### Handler
Se usa para sistemas síncronos de forma interna y debe usarse al recibir mensajes de forma externa puesto que debe controlar los datos hacia qué comando irán

##### Shared
Clases que puedo usar en toda la aplicación, un módulo puede acceder a sus propios elementos y a Shared

##### Serialized
Estado del agreggate. Array asociativo con los getter para manejar el evento

##### Eventos no procesados
DispatchAt para recrear el evento.
Se guardan, por lo general, en la bdd.