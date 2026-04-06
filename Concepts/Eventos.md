#### Definición
Respuestas asíncronas a un suceso que realiza el usuario, y se captura con la escucha.
Estos eventos son capturados, comunicados, procesados y persistidos en la arquitectura basada en eventos. Pueden encadenarse.
#### Escucha
Capacidad de un programa o sistema para detectar y responder a eventos específicos que ocurren dentro de su entorno.
Pueden ir en la parte de arquitectura de la aplicación, pues puede escuchar eventos tanto dentro como fuera de la aplicación.

Por ejemplo, en un caso de uso de creación de usuario (registrarlo en bdd), el principio Single Responsability me dice que, si debo notificar al usuario la correcta creación a través de email.
El principio Open-Close me dice que debo crear el escucha aparte de tal caso de uso, de forma que escucha "usuario creado correctamente" para poder ejecutar el proceso de enviar notificación de email. Lo mismo pasaría en el caso de tener que enviar otro email al administrador para que conozca el usuario creado. 

### Php

###### config.php
`<?php
` 'events' => array(
`   UserCreated::class => array(
`     EmailSenderCreatedUserListener::class
`  )
`)

###### IEventDispatcher.php
`<?php
`namespace App\Shared\Domain;

`inteface IEventDispatcher
`{
` @param object
` @return object
` public function dispatch(Event $event);
`}

###### EventDispatcher.php
`<?php
`namespace App\Shared\Infrastructure
`use App\Shared\Domain\IEventDispatcher;

`class EventDispatcher implements Dispatcher extends IEventDispatcher {
`}

###### Event.php
`<?php
`namespace App\Shared\Domain;

`abstract class Event {
`{
` public $createdAt;
` public $name;
` public $body;

` public function __construct($name, $body) {
`  $this->createdAt = new DateTime();
`  $this->name = $name;
`  $this->body = $body;
` }
`}

###### UserCreated.php
`<?php
`namespace App\Shared\Domain;

`class UserCreated extends Event {
`{

` public function __construct() {
`  parent::__construct('user.created', $body)
` }
`}

###### CreateUserCaseUse.php
`<?php
`namespace App\Shared\Domain;

`class UserCreated extends Event {
`{

` public function create() 
`{
`  // lógica
`  $this->dispatcher(new UserCreated($user))
` }
`}



