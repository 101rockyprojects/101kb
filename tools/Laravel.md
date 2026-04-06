Laravel es un framework de codigo abierto para desarrollar aplicaciones y servicios web con PHP. Fue creado por Taylor Otwell y se lanzo por primera vez en 2011. Laravel se basa en el patron [[concepts/Modelo-Vista-Controlador (MVC)]] y proporciona una sintaxis elegante y expresiva para crear codigo de forma eficiente. Algunas caracteristicas clave incluyen routing, ORM (Eloquent), plantillas (Blade), colas y tareas programadas, y un ecosistema grande. Laravel se ha convertido en uno de los frameworks PHP mas populares.


# REST API
Iniciar con:  `php artisan serve`
Para el archivo api.php, en Laravel 11 se debe ejecutar:  `php artisan install:api`
Para crear un Resource para cada Model de la Api se debe ejecutar:  `php artisan make:resource version\ModelResource`
*Ejemplo:*
Para los datos de una REST API, se espera que los datos JSON tengan sus atributos en camelCase, por lo tanto hacer un Resource es muy util para formatear los nombres y elegir qué enviar a la API:
```php
return [
   'representativeId' => $this->representative_id,
   'documentType' => $this->document_type,
   'documentNumber' => $this->document_number,
   'phoneNumber' => $this->phone_number,
   'email' => $this->email,
   'number' => $this->number
];
```
Para crear una Collection para cada Model de la Api se debe ejecutar:  `php artisan make:resource version\ModelCollection`
*Nota:* La Collection asume que existe un Resource para interpretar los datos, por lo que el Resource que se genere será el que determine el formato.

## Related

- [[concepts/Framework]]
- [[concepts/Modelo-Vista-Controlador (MVC)]]
