Lanzar eventos, encolarlos y se consumen desde otra aplicación.
Escalado en paralelo, con instancias. Ejemplo: Una instancia es un *cajero*, tengo una cola de personas que van a pagar, si pongo 5 *cajeros* solo voy administrando hacia cual *cajero* se envía la petición que sigue.
#### Funcionalidad
Dos actores: Consumidor y Proveedor

###### Diferencia con API REST:
API REST es una petición a respuesta, es síncrono y devuelve datos en formato JSON. Maneja errores con HTTPS headers.

Lectura: Debe ser síncrona.
Escritura: Puede ser síncrona o asíncrona.

Infraestructura
- Listener

Dominio
- Consultas