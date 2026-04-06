[[Laravel]], al ser un [[framework]] más completo que otros similares; esto significa que tiene muchos más componentes con los cuales trabajar; se da por hecho que el lector tiene cierto conocimiento básico sobre cómo funciona este tipo de frameworks, como el uso o teoría de para qué funcionan las migraciones, el MVC, rutas, entre otras; no es necesario que sepas cómo manejarlas, pero sí que entiendas la lógica detrás de todo esto; si no los tienes, te recomiendo que veas mi primer libro de programación web en el cual damos los primeros pasos con [[CodeIgniter]], el cual es un framework estupendo con muchas coincidencias con Laravel, y al ser un framework más pequeño y sencillo de manejar resulta más fácil de iniciar tu aprendizaje.

**Alcance**
Esta guía tiene la finalidad de dar los primeros pasos con Laravel; con esto, vamos a plantear dos cosas:

1. No es un curso que tenga por objetivo conocer al 100% Laravel, o de cero a experto, ya que, sería un objetivo demasiado grande para el alcance de esta guía, si no conocer su ecosistema, que nos ofrece y cómo funciona el mismo en base a varios ejemplos y/o aplicaciones pequeñas con alcances limitados.
2. Se da por hecho de que el lector tiene conocimientos al menos básicos sobre la estructura del framework; por el alcance que tiene Laravel como framework, aunado a las tecnologías relacionadas que siempre forman parte importante del mismo (como Node, Vue, Tailwind.css, Alpine.js, HTML, y relacionados) en comparación con otros frameworks como CodeIgniter, resulta muy difícil hacer la convivencia con todas estas tecnologías en un solo escrito; en varias partes del libro, mencionaré cuando sería recomendable que consultes otras fuentes para que al menos conozcas los aspectos básicos de dichas tecnologías; en mi canal de YouTube, al igual mi blog y plataforma de academia digital, cuento con múltiples recursos que podrán ayudarte en estas introducciones; recuerda que el objetivo del libro es introducir a Laravel más no sus tecnologías asociadas.

**Para quién es este curso**
Este curso está dirigido a cualquiera que quiera comenzar a desarrollar con Laravel, aunque no se recomienda a aquellas personas que no hayan trabajado con otros frameworks PHP, si es tu caso, te aconsejo, que primero conozcas y practiques con frameworks similares, pero más sencillos, como es el caso de CodeIgniter 4, del cual dispongo de muchos recursos que pueden servirte para introducirte en este mundo de frameworks PHP, en mi sitio web encontrarás más información.

- Laravel es un framework avanzado, aunque en el libro hago todo lo posible para mantener el desarrollo sencillo, recuerda puedes practicar con frameworks similares, como el de CodeIgniter, del cual también cuento con un libro y un curso; que es ideal para conocer un framework para dar los primeros pasos con este tipo de tecnologías, ya que Laravel, tiende a tener una curva de aprendizaje más elevada al tener más componentes y más abstracción al emplear los mismos.
- Para aquellos que quieran conocer el framework y que conozcan otros frameworks similares en PHP, pero no tienen los conocimientos necesarios para aventurarse en estos por no conocer las bases que los sustentan
- Para aquellas personas que quieran aprender algo nuevo, conocer sobre un framework que, aunque tiene mucha documentación, la mayoría está en inglés y al estar el framework en constante evolución, tiende a quedar desactualizada.
- Para las personas que quieran mejorar una habilidad en el desarrollo web, que quiera crecer como desarrollador y que quiera seguir escalando su camino con otros frameworks superiores a este; con que te identifiques al menos con alguno de los puntos señalados anteriormente, este libro es para ti.

Este libro tiene un total de 19 capítulos, se recomienda que leas en el orden en el cual están dispuestos y a medida que vayamos explicando los componentes del framework, vayas directamente a la práctica, repliques, pruebes y modifiques los códigos que mostramos en este libro.

1. Capítulo 1: Se explica cuál es el software necesario, y la instalación del mismo para desarrollar en Laravel en Windows con Laragon o Laravel Herd o en MacOS Laravel Herd y MacOS y Linux con Laravel Sail y Docker.
2. Capítulo 2: Hablaremos sobre Laravel, crearemos un proyecto, configuraremos la base de datos, conoceremos aspectos básicos del framework y finalmente conoceremos el elemento principal que son las rutas.
3. Capítulo 3: Daremos los primeros pasos con las rutas y las vistas, para empezar a ver pantallas mediante el navegador; también abordaremos el uso de los controladores con las vistas; redirecciones, directivas y blade como motor de plantilla.
4. Capítulo 4: Conoceremos el uso de las migraciones, como elemento central para poder crear los modelos, que son la capa que se conecta a la base de datos, a una tabla en particular; y, para tener esta tabla, necesitamos las migraciones.
5. Capítulo 5: Conoceremos el MVC, que es el corazón y las bases del framework y, realizaremos unos pocos ejemplos que nos servirán para seguir avanzando.
6. Capítulo 6: Crearemos una sencilla app tipo CRUD, aprenderemos a trabajar con el MVC, controladores de tipo recurso, listados, paginación, validaciones de formulario, acceso a la base de datos entre otros aspectos relacionados.
7. Capítulo 7: Conoceremos cómo enviar mensajes por sesión tipo flash las cuales usaremos para confirmación de las operaciones CRUD y el uso de la sesión.
8. Capítulo 8: Este capítulo está orientado a aprender el uso de las rutas; que en Laravel son muy extensibles y llenas de opciones para agrupamientos, tipos y opciones.
9. Capítulo 9: En este capítulo, vamos a crear un sistema de autenticación y todo lo que esto conlleva para nuestra aplicación instalando Laravel Breeze, el cual también configura Tailwind.css en el proyecto y Alpine.js. También vamos a expandir el esquema que nos provee Laravel Breeze para la autenticación, creando una protección en base a roles, para manejar distintos tipos de usuarios en módulos específicos de la aplicación.
10. Capítulo 10: En este capítulo, vamos a conocer algunas operaciones comunes con Eloquent aplicados a la base de datos mediante los query builders.
11. Capítulo 11: Vamos a presentar el uso de los componentes en Laravel como un elemento central para crear una aplicación modular.
12. Capítulo 12: Aprenderemos a generar datos de prueba mediante clases usando el sistema de seeders que incorpora el framework.
13. Capítulo 13: Aprenderemos a crear una Rest Api de tipo CRUD y métodos adicionales para realizar consultas adicionales, también vamos a proteger la Rest Api de tipo CRUD con Sanctum, empleando la autenticación de tipo SPA y por tokens.
14. Capítulo 14: Vamos a consumir la Rest Api mediante una aplicación tipo CRUD en Vue 3 empleando peticiones axios y componentes web con Oruga UI; también veremos el proceso de carga de archivos. También protegeremos la aplicación en Vue con login requerido para acceder a sus distintos módulos empleando la autenticación SPA o por tokens de Laravel Sanctum.
15. Capítulo 15: Vamos a aprender a manejar la caché, para guardar datos de acceso para mejorar el desempeño de la aplicación y evitar cuellos de botellas con la base de datos.
16. Capítulo 16: Vamos a aprender a manejar las políticas de acceso para agregar reglas de acceso a ciertos módulos de la aplicación mediante los Gate y Policies.
17. Capítulo 17: Veremos cómo manejar los permisos y roles a un usuario para autorizar ciertas partes de la aplicación con un esquema flexible y muy utilizado en las aplicaciones web de todo tipo usando Spatie, en esta capítulo conoceremos cómo realizar esta integración y desarrollaremos un módulo para manejar esta permisología.
18. Capítulo 18: Veremos cómo manejar las relaciones polimorfismo para reutilizar modelos que tengan un mismo comportamiento.
19. Capítulo 19: Pruebas unitarias **(Pendiente)**

#### Lo que aprenderás

- Emplear Laravel de manera fluida y conocer sus componentes fundamentales
- Desarrollar aplicaciones de gestión de datos
- Organización en la programación de múltiples módulos
- Una aplicación web básica con funciones de CRUD desde cero
- Una web SPA de cara al usuario final (Blog)
- Enviar Emails
- Login con protección en el password, recuperación de credenciales, distintos niveles de acceso entre usuarios
- Aprender a crear, validar y procesar formularios
- Cargar, validar y redimensionar imágenes en el servidor
- Redirecciones y rooteo
- Aprender a trabajar con tecnologías punteras en conjunto: HTML, CSS, JavaScript, Tailwind, PHP, MYSQL y Vue
- Crear componentes con Vue
- Laravel Livewire (básico)
- Laravel Inertia (básico)
- Laravel 11

#### ¿Hay requisitos para realizar el curso?

- Nociones básicas de PHP
- Nociones básicas en SQL
- Nociones básicas sobre HTML y CSS
- Conocer el patrón Modelo Vista Controlador
- Nociones básicas de programación orientada a objetos
- Algo de Node, NPM sería recomendado
- Navegar con la terminal o la CDM de Windows

#### ¿Para quién es este curso?

- Desarrolladores en PHP
- Desarrolladores en Laravel
- Desarrolladores en CodeIgniter
- Programadores que quieran adquirir nuevos conocimientos y habilidades
- Desarrolladores web del fullstack
- Desarrolladores que quieran mejorar sus posibilidades laborales
- Apasionados por las tecnologías y la programación