> Nivel: Intermedio/Avanzado
---

# Preguntas y respuestas
## Java as a Language

> Diferencia entre comparar con `==` y usando `equals()`?

**R/**
El operador `==` compara valores primitivos, teniendo en cuenta su *referencia* en memoria.
```java
int a = 5;
int b = 5;
System.out.println(a == b); // true (mismo valor), compara su contenido
```
Sin embargo, cuando trabajamos con objetos es diferente. La función `equals()` se usa con *objetos*, y compara su *contenido*
```java
Persona p = new Persona("cecilio");
Persona p1 = new Persona("cecilio");
// Esto compara las referencias de los objetos, no su contenido
System.out.println(p == p1); // false, ya que son diferentes instancias

// Si quieres comparar el contenido (el nombre), usa equals()
System.out.println(p.equals(p1)); // false, a menos que sobrescribas equals()
```
¿En qué casos, comparando objetos, el operador `==` devolvería **true**?
```java
Persona p = new Persona("cecilio");
Persona p1 = p; // p1 apunta al mismo objeto que p
// Esto comparará las referencias de los objetos, no el contenido
System.out.println(p == p1); // true, pues apuntan al mismo objeto en memoria
```
En resumen:
- Usa `==` → para **primitivos**
- Usa `equals()` → para **objetos**

>Desde el punto de vista de un backend en Java 11+ (Spring Boot), ¿qué tres cambios **estructurales** importantes distinguirías entre Java 8, Java 11 y Java 17 que realmente afectan al día a día de un desarrollador backend (no solo “nuevos métodos” sino cómo cambia el ecosistema)?  
>Enuméralos y explica brevemente para cada uno:
>	- uno que cambie cómo se trabaja con el lenguaje o el runtime,
>	- uno que afecte directamente a Spring Boot o librerías típicas.

Mientras que **es muy habitual usar el operador == para comparar tipos básicos no es tan habitual usarlo a la hora de comparar objetos ya que no tiene sentido a nivel de reglas de negocio**.
Algo que nos permite la función `equals()` que no puede hacerse con el operador `==` es ser modificable. Por ejemplo, a nivel de negocio consideraremos dos objetos iguales si tienen el mismo nombre. Por lo tanto deberemos sobreescribir el método equals y hashcode  de una clase Persona y hacer que dos objetos  Persona **sean iguales si su nombre coincide**:
```java
public class Persona {
	// Código de la clase Persona
	
	@Override  // Sobreescribimos equals
	public boolean equals(Object obj) {
	// Verificar si es el mismo objeto
	if (this == obj) {
		return true;
	}
	
	// Verificar si el objeto es nulo o no es de la misma clase
	if (obj == null || getClass() != obj.getClass()) {
		return false;
	}
	
	// Realizar el casting seguro y comparar los nombres
	Persona p = (Persona) obj;
	return Objects.equals(nombre, p.getNombre()); // equals() maneja nulls
	}

} 
```

**R/**
 **Nuevas APIs y runtime del lenguaje (Java 11 / 17)**
- Java 11 trajo el cliente HTTP estándar (`java.net.http.HttpClient`), y métodos de `String` como `isBlank()`, `lines()`, `stripIndent()`, que cambian el día a día (menos dependencias de Apache Commons‑Lang para trivialidades).
- Java 17 añade `records`, `sealed classes` y mejoras de `instanceof` con pattern matching, que permiten simplificar modelos de datos y DTOs, reduciendo código verboso y errores de copia‑pega en entidades/DTOs.

**Impacto en Spring Boot y librerías (Java 11+)**
- Spring Boot 2.1+ soporta Java 11 y Spring Boot 3+ asume Java 17 como base, lo que implica que ciertas librerías casadas con Java 8 se quedan atrás o requieren actualización.
- Además, el ecosistema se mueve hacia runtime más ligeros (menos clases en el classpath, GCs más modernos, mejor performance de arranque), lo que cambia decisiones de arquitectura (microservicios, contenedores, Kubernetes) y hace que “seguir en Java 8” se sienta cada vez más como un tech‑debt.*

---

> ¿Por qué subir a Java 11/17 en un entorno Spring Boot?

**R/** Por la estabilidad de un JDK LTS moderno, con un classpath más limpio (módulos), APIs estándar (HTTP Client) y mejoras de GC, además de features del lenguaje (`records`, `sealed class`, [pattern matching, instanceof](https://asjordi.dev/blog/pattern-matching-en-java/)) que ayudan a mantener código backend más limpio y seguro en equipos grandes

---

> En Java 11+ puedes usar `var` para inferir tipos locales.  
>Piensa en un backend real con Spring Boot, servicios, DTOs, repositorios, etc.
>**Te pregunto:**
>- ¿Qué aporta realmente `var` hoy frente a no usarlo (solo `String s = "..."`, `List<Foo> foos = ...`, etc.)?
>- ¿Qué riesgos o desventajas de mantenibilidad introduce si se usa de forma indiscriminada?
>- Propón **dos casos concretos** en tu día a día (por ejemplo inicialización de un `List`, un `Map` intermedio en un servicio, o un flujo de Streams) donde usar `var` mejora la legibilidad y no es “mágico”, y **un tercer caso** donde lo usarías conscientemente aunque sea menos explícito (por ejemplo un stream complejo con varios mapeos).

**R/**
Uso `var` sobre todo para mejorar la legibilidad cuando los tipos son muy verbosos, por ejemplo listas, mapas o streams complejos. En esas situaciones, evitar repetir `List<Usuario>`, `Map<Clave, Valor>`, etc., hace que el código sea más limpio y menos ruidoso.

En tipos simples como `String` o `Integer`, no veo tanto beneficio porque la declaración no es tan larga, así que ahí suelo dejar el tipo explícito salvo que el contexto sea muy obvio.

El riesgo de usar `var` de forma indiscriminada es que el tipo de lo que se crea no queda tan claro para alguien que lee el código, sobretodo si la inicialización es compleja (por ejemplo un stream anidado o una llamada a un método genérico poco conocido). Eso puede dificultar el mantenimiento, porque el desarrollador tiene que ir al IDE o al código de la inicialización para saber qué tipo realmente tiene la variable.

Un buen uso de `var` sería, por ejemplo:
- `var tareas = new ArrayList<Task>();`
- `var usuariosActivos = service.buscarUsuariosActivos(); // donde el tipo está claro en el nombre del método`  
    Un caso donde lo usaría incluso aunque el tipo no sea trivial es cuando manejo un stream complejo con varios mapeos, porque el foco está en la lógica del flujo y no en el tipo intermedio:
- `var resultados = repository.findAll().stream().map(...).filter(...).collect(toList());`  
    Aquí el tipo inferido es probablemente `List<Algo>`, pero el nombre `resultados` y el contexto del método ya lo dejan claro, así que `var` ayuda a no repetir el tipo genérico.

---

> Imagina un servicio REST de Spring Boot que recibe un JSON con campos de texto (por ejemplo `description`, `instructions`, `markdownContent`).  
> Tu objetivo es:
> - validar que ciertos campos no estén “vacíos” de verdad,
> - procesar texto multilinea (por ejemplo, markdown o instrucciones largas),
> - limpiar texto que viene de un editor o de un copy‑paste mal cuidado.
> 1. ¿Cuándo usarías `String.isBlank()` frente a `== null` o `String.isEmpty()`?    
	- ¿Qué problema de negocio estarías evitando con `isBlank()` en un campo obligatorio?
> 2. Describe un caso concreto donde usarías `lines()` en un backend (por ejemplo, un campo de “pasos” o “instrucciones” que llega como texto multilinea).
	- ¿Qué cuidado tendrías con líneas vacías o espacios?
> 3. - ¿En qué escenario real te interesa `stripIndent()` y por qué no usarías simplemente `trim()`?
    - Pon un ejemplo de texto que llega con indentación y cómo afectaría eso a la lógica de tu servicio.
>No hace falta código exacto, pero sí que seas concreto y razonable para un entorno real.

**R/**
1 .Uso `String.isBlank()` para campos obligatorios donde el usuario puede rellenar solo espacios, porque `isEmpty()` no protege contra espacios.
- Si dejaran pasar un campo `description.isBlank()` en un campo obligatorio, estaría dejando datos inconsistentes en la base (por ejemplo, filtrados que fallan, validaciones que no se disparan) y podrían generar efecto dominó en otros procesos.
```java
if (descripcion.isBlank()) {
    throw new ValidationException("El campo 'descripcion' es obligatorio y no puede ser solo espacios");
}
```

2 .Uso `lines()` sobre todo para procesar texto multilinea, como `instructions` o `markdownContent`, normalmente dentro de un Stream para filtrar líneas vacías o transformarlas.
- Las líneas vacías no son malas per se, pero en algunos casos de uso exijo que cada línea tenga contenido; en otros simplemente normalizo o dejo pasar según el negocio.
```text
Paso 1: Abrir la aplicación
Paso 2: Seleccionar perfil
Paso 3: Guardar configuración
```
```java
List<String> pasosValidos = instructions.lines()
    .map(String::trim)
    .filter(linea -> !linea.isBlank())
    .collect(Collectors.toList());
```
3.`trim()` me sirve para limpiar espacios al inicio y final, pero `stripIndent()` es clave cuando trato texto multilinea con indentación, porque elimina el nivel común de sangría de todas las líneas dejando el formato más limpio, sin perder el contenido útil.
- Es muy útil, por ejemplo, para normalizar markdown o plantillas que llegan de un editor con sangrías desiguales.
```markdown
    # Título
        - Punto 1
        - Punto 2
```
```java
String limpiado = markdownContent.trim(); // Devuelve texto sin identación
String limpiado = markdownContent.stripIndent(); // Mantiene identación
```

> Imagina un sistema de pedidos con DTOs, comandos y eventos. ¿Dónde pondrías `record` y dónde seguirías usando clases normales? ¿Por qué?

**R/**
Utilizaría record para DTOs y para cualquier clase de transporte que quiera que sea **inmutable**, es decir, donde necesito definir datos pero no modificarlos después de crearlos.
Los record me generan automáticamente el constructor, los métodos de acceso (`getters`), equals, hashCode y toString, reduciendo bastante el código repetitivo.
En comandos y eventos también los usaría cuando solo representen información que se crea y se lee, pero no se modifica.

Me interesa especialmente cuando el objeto **solo representa datos** y no necesita identidad ni comportamiento complejo. No lo usaría en entidades JPA ni en modelos con mutabilidad, porque ahí necesito más control sobre el ciclo de vida y el estado.

> En Spring Boot, cuando usarías un `record` como DTO de entrada o salida, y qué problemas podrías encontrar si intentas usarlo directamente como entidad JPA?

En APIs, usar `record` como DTO (tanto de entrada como de salida) tiene bastante sentido cuando solo quieres **transportar datos de forma clara e inmutable**, sin añadir lógica extra. Lo mismo aplica para comandos y eventos, que suelen ser simplemente “bolsas de datos” que se crean una vez y se consumen en otro punto.

Sin embargo, cuando el objeto requiere **validaciones complejas**, transformación hacia un modelo de negocio o **cambios de estado durante el flujo**, resulta más práctico usar una clase normal. Los `record` son inmutables por diseño, y eso no encaja bien en esos escenarios.

Con entidades JPA pasa algo parecido: una entidad representa algo que **evoluciona en el tiempo**, mientras que un `record` está pensado para datos fijos. Mezclar ambos conceptos suele generar fricción. Además, frameworks como Hibernate suelen necesitar modificar el estado (`setters`), y los `record` no están pensados para eso.

Por eso, una separación clara suele funcionar mejor:
- `record` → DTOs, comandos y eventos simples
- clases normales → entidades JPA y modelos con estado mutable

> Imagina un backend Spring Boot con servicios, repositorios y controladores. En muchos sitios ves `Optional<T>` por defecto, incluso en campos, parámetros o en APIs REST.
	1 . - ¿Cuál es el **propósito principal** de `Optional<T>` en Java?
    - ¿Qué problema está diseñado para resolver (y cuál **no** está diseñado para resolver).        
    2 . - Da **dos ejemplos concretos** donde usar `Optional` encaja muy bien en un backend (por ejemplo un método de servicio, un repositorio, algo de búsqueda).
    - Da **un ejemplo donde usar `Optional` sería un mal uso** (por ejemplo en un campo, parámetro, o en la firma de un controlador).
    3 . - Si alguien te dice: “Uso `Optional` siempre que algo puede ser `null` para evitar NPE”, ¿qué le dirías?
    - ¿Cuándo realmente conviene usar `Optional` y cuándo mejor devolver `null` (o lanzar excepción) con contrato claro?

**R/**
`Optional<T>` sirve para dejar explícito que un valor puede estar ausente, no solo que “puede ser null”. La idea es que el método exprese claramente que puede devolver **algo o nada**, obligando al que lo usa a manejar ese caso.

En backend, encaja bien en:
- **Repositorios**: por ejemplo, `Optional<User> findById(Long id);`, donde puede no existir el dato y el servicio decide qué hacer.
- **Servicios de búsqueda**: como `Optional<Match> findMatch(String query);`, cuando “no hay resultado” forma parte del contrato.

Donde suele usarse mal es en **parámetros de métodos o controladores REST**. Ahí normalmente es más claro:
- usar tipos normales y validar si son obligatorios
- o permitir `null` de forma explícita si son opcionales

Usar `Optional` en parámetros rara vez aporta claridad y puede complicar el diseño.
Si alguien lo usa “para evitar `NullPointerException` en todos lados”, el problema real no es `null`, sino el diseño. Muchas veces es mejor:
- devolver colecciones vacías
- usar valores por defecto
- o lanzar excepciones claras.

## Spring Boot / Spring MVC

> Imagina un endpoint para obtener y crear usuarios en una API REST.
	1 . ¿Cuál es la diferencia práctica entre `@Controller` y `@RestController`?
    2 . ¿Cuándo usarías `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PathVariable` y `@RequestParam`?
    3 . Si tienes un endpoint como:
	    - `GET /usuarios/10`
	    - `GET /usuarios?activo=true`
	    - `POST /usuarios`
	    ¿Qué código HTTP devolverías en cada caso y por qué?
    4 . Pregunta trampa: si un `POST /usuarios` recibe un JSON inválido por validación, ¿deberías devolver `400`, `409` o `422`? Explica tu criterio.

**R/**
1. La diferencia entre `@Controller` y `@RestController` es que `@Controller` está pensado para web MVC (vistas HTML, JSP, Thymeleaf, etc.), mientras que `@RestController` es específico para APIs REST y aplica `@ResponseBody` por defecto en todos sus métodos. Esto significa que devuelves directamente el body (JSON/XML) sin necesidad de añadir `@ResponseBody` en cada método.
2. Normalmente:
    - Uso `@RequestMapping` para definir la ruta base del controlador.
    - `@GetMapping` para respuestas `GET`, `@PostMapping` para `POST`, etc.
    - `@PathVariable` para parámetros en la ruta, como `id` en `/usuarios/{id}`.
    - `@RequestParam` para parámetros de consulta, como filtros, paginación o flags de negocio.
3. Para:
    - `GET /usuarios/10` devolvería `200` si el usuario existe, y `404` si no existe.
    - `GET /usuarios?activo=true` devolvería `200` con la lista de usuarios activos.
    - `POST /usuarios` devolvería `201 Created` al crear un nuevo recurso.
    - `DELETE /usuarios/10` devolvería `204 No Content` si no hay body (por ejemplo, solo confirmación de eliminación).
4. Para un `POST` con JSON inválido, usaría `400` si el problema es de estructura o formato básico (JSON malformado, campos mal tipados).
    - `409 Conflict` lo reservo para conflictos de negocio, como intentar crear un recurso que ya existe o violar reglas de negocio específicas.
    - `422 Unprocessable Entity` lo usaría cuando el JSON es válido, pero la entidad no puede procesarse por reglas de negocio o formato (por ejemplo, un campo de imagen que no cumple el formato esperado).

> Imagina que estás diseñando un repositorio para `Pedido` (o `User` si te resulta más cómodo). Responde en español, en lenguaje natural, como si estuvieras en una entrevista:
	1 . - ¿Qué significa `@Entity` y `@Repository` en el contexto de JPA / Spring Data?
	    - ¿Dónde pondrías cada anotación y por qué no mezclarías ambos roles en la misma clase? 
	2 . - ¿Qué diferencia práctica hay entre `CrudRepository` y `JpaRepository`?    
	    - ¿En qué escenarios te conviene `JpaRepository` y cuándo sería suficiente `CrudRepository`?
	3 . - Explica brevemente:
        - qué son las **consultas derivadas** (derived queries),
        - y qué es `@Query` y por qué lo usarías en vez de una consulta derivada.
	    - Da un ejemplo de cada uno (no hace falta código exacto, pero sí que el ejemplo sea razonable para un backend real).
    4 . **Pregunta trampa**: 
	    ¿Es correcto hacer una consulta como `@Query("SELECT * FROM pedido ...")` con SQL literal en JPA?  
	    ¿Qué podrías hacer mejor para mantener el código portable y mantenible?

**R/**
 1. `@Entity` indica que una clase representa una entidad JPA, es decir, un mapeo de una tabla de base de datos a nivel de objetos.  
     - `@Repository` marca una interfaz o clase de acceso a datos, siguiendo el patrón Repository, para abstraer el acceso a la base de datos y desacoplar la lógica de negocio.
     - No combino ambos roles en la misma clase porque `@Entity` describe el modelo de datos, y `@Repository` describe el acceso a ese modelo.
 2. `CrudRepository` ofrece métodos CRUD básicos (`save`, `findById`, `findAll`, `delete`, etc.).
     - `JpaRepository` extiende `CrudRepository` y añade operaciones de JPA como paginación, sorting, flush, y operaciones de lote.
     - Si solo necesito operaciones CRUD básicas, `CrudRepository` es suficiente; si quiero aprovechar características de JPA, uso `JpaRepository`.
 3. Las consultas derivadas (derived queries) son métodos cuyo nombre define la consulta automáticamente (`findByNombreContaining`, `findByActivoTrue`, etc.).
     - Son muy legibles y útiles para casos comunes. 
     - `@Query` permite definir una consulta manual con JPQL o SQL nativo, lo que da más control para casos complejos, joins, proyecciones, o queries de rendimiento.
 4. No es correcto usar `@Query("SELECT * FROM pedido ...")` como SQL literal si quiero mantener portabilidad, porque `*` depende de la tabla y de la base de datos concreta.
     - Lo mejor es usar JPQL: `SELECT p FROM Pedido p WHERE ...`, que trabaja con la entidad y sus propiedades.
     - Si necesito SQL nativo, lo reservo para casos específicos del motor, manteniendo nombres claros, contrato explícito y consultas simples y legibles.

Ejemplo de @Query:
```java
@Repository
public interface PedidoRepository extends JpaRepository<Pedido, Long> {
    // 1. Consulta derivada (muy limpia, pero limitada)
    List<Pedido> findByEstadoAndClienteId(String estado, Long clienteId);
    
    // 2. @Query con JPQL (mejor control)
    @Query("SELECT p FROM Pedido p WHERE p.estado = :estado AND p.cliente.id = :clienteId")
    List<Pedido> findByEstadoAndClienteIdJPQL(@Param("estado") String estado, @Param("clienteId") Long clienteId);
    
    // 3. @Query con SQL nativo (para casos muy específicos del motor)
    @Query(value = "SELECT p.* FROM pedido p WHERE p.estado = :estado AND p.cliente_id = :clienteId", nativeQuery = true)
    List<Pedido> findByEstadoAndClienteIdNative(@Param("estado") String estado, @Param("clienteId") Long clienteId);
}
```

> Imagina un backend Spring Boot con un servicio PedidoService con un método @Transactional que crea un pedido y guarda un movimiento de inventario, y un método interno loggingService.guardarLog() que también está anotado con @Transactional.
> 
>	1. ¿Qué hace @Transactional en un método de servicio?
>         Si tu PedidoService.crearPedido() llama a loggingService.guardarLog(), ¿en qué momento se inicia y se cierra la transacción, y qué pasa si guardarLog() dispara una excepción?
> 	2. Explica breve pero concretamente:
> 		qué es la propagación de transacciones,
> 		cuál es la propagación por defecto (Propagation.REQUIRED)
> 		y cuándo usarías REQUIRES_NEW (trampa: no solo “para logs”).
> 		Pon un ejemplo de un caso real de negocio donde REQUIRES_NEW tenga sentido.
>     3. Explica qué es el aislamiento (isolation) de una transacción a alto nivel.
> 	       ¿Cuál es el nivel de aislamiento típico en muchas bases de datos (por ejemplo, READ_COMMITTED)?
>         ¿Qué riesgos de concurrencia evita y cuáles todavía pueden ocurrir?
>     Pregunta trampa de razonamiento:
>         Si configuras @Transactional(propagation = Propagation.REQUIRES_NEW) en guardarLog(), ¿qué ocurre si:
>             crearPedido() lanza RuntimeException después de que guardarLog() termine?
> 	        ¿El log queda guardado o se borra?
> 	        ¿Y si en cambio el rollback del pedido no afectara al log?

**R/**
1. @Transactional marca que un método debe ejecutarse dentro de una transacción única: o se guardan todos los cambios, o se deshacen todos.
	Si crearPedido() llama a loggingService.guardarLog(), ambos usan la misma transacción si guardarLog() tiene propagación REQUIRED.
	Si guardarLog() lanza una excepción no controlada, se hace rollback de toda la transacción: ni el pedido ni el log se guardan.
2. La propagación define qué pasa con una transacción cuando un método @Transactional es llamado desde otro @Transactional.
	REQUIRED (por defecto) reutiliza la transacción del padre, o crea una nueva si no existe.
	REQUIRES_NEW crea una transacción nueva e independiente, incluso si ya hay una.
	Uso REQUIRES_NEW cuando quiero que una operación (por ejemplo, un log de auditoría) se guarde incluso si el pedido principal falla.
3. El aislamiento define cómo distintas transacciones concurrentes ven el estado de la base de datos.
	El nivel típico es READ_COMMITTED, que solo permite leer datos commiteados, evitando lecturas sucias, pero no garantiza que una fila sea igual en todas las lecturas dentro de la misma transacción.
	REPEATABLE_READ ofrece más consistencia interna, reduciendo lecturas inconsistentes y registros fantasmas en algunos motores.
4. Con REQUIRES_NEW en guardarLog():
	Si el log hace commit y luego crearPedido() lanza RuntimeException, el pedido se hace rollback, pero el log se queda guardado porque estaba en su propia transacción.
	Solo se perdería el log si también esa transacción interna lanzara excepción y se hiciera rollback.

## Spring Security
>Imagina una API REST moderna con Spring Boot + Spring Security.  
	1 . - ¿Qué papel cumplen `UserDetailsService` y `UserDetails` en Spring Security?
	    - ¿Por qué normalmente se implementa `UserDetailsService` en lugar de “hardcodear” usuarios?
	2 . - Explica brevemente:
        - qué es **autenticación básica** (`Basic Auth`),
        - y qué es **JWT** (JSON Web Token) en este contexto.            
    - ¿Cuándo preferirías JWT frente a sesión server‑side con cookies, y por qué?
	3 .   - ¿Qué hace `@PreAuthorize` y qué ventaja tiene frente a solo proteger a nivel de `@RequestMapping` con roles?        
    - Da un ejemplo concreto donde usarías `@PreAuthorize` en un **servicio** (no solo en un controlador) para checks de negocio. 
    4 . **Pregunta trampa**:
    - Si tu controlador recibe un JWT, pero el `UserDetailsService` carga el usuario desde la base de datos, ¿qué información de JWT y qué información de `UserDetails` considerarías “de confianza”?
    - ¿Qué seguridad mínima debería tener el mecanismo de verificación de tokens para que no sea un punto débil?

**R/**
1. `UserDetailsService` es el servicio que carga la información de usuario (por ejemplo, desde base de datos) para que Spring Security pueda hacer login y gestión de permisos.  
     - `UserDetails` es el modelo de datos que representa ese usuario, con campos como `username`, `password`, `authorities`, etc.     
 2. **Autenticación básica** (`Basic Auth`) es un método de autenticación simple con `usuario:contraseña` en el header `Authorization: Basic ...`.
        - El **JWT** es un token firmado que contiene claims de usuario, expiración, roles, etc., y se usa en `Authorization: Bearer ...`.     
     - Prefiero JWT para APIs REST modernas, donde quiero:    
         - stateless      
         - escalabilidad
         - y fácil integración con front‑end SPA.
 3. `@PreAuthorize` permite proteger métodos según roles, permisos, o expresiones de negocio.
     - Por ejemplo, proteger un método de servicio para que solo lo pueda usar un administrador o el usuario que coincida con el `id` del token.
 4. Considero de confianza el **JWT** si está firmado correctamente y no ha expirado, y el **`UserDetailsService`** carga la información “canónica” del usuario desde la base de datos.
     - La seguridad mínima es usar JWT firmado, validar el issuer, expiration, audience, y claims importantes, y no almacenar información sensible en el JWT.


> 1 . Explica brevemente qué son las fases principales del ciclo de vida de Maven: `compile`, `test`, `package`, `install`.    
    - Si tu equipo ejecuta `mvn install`, ¿qué fases se ejecutan en orden y por qué normalmente no haces `mvn package` seguido de `mvn install` como pasos separados?
>2. ¿Qué es `pom.xml` y qué papel cumple `dependencies` frente a `plugins`?
    - Pon un ejemplo concreto de una dependencia típica de un proyecto Spring Boot y de un plugin típico (por ejemplo, `spring-boot-maven-plugin`).
>3. Explica los scopes `compile`, `provided`, `runtime` y `test`.
    - ¿En qué caso usarías `provided` (por ejemplo, servidor de aplicaciones) y `runtime` (por ejemplo, JDBC drivers)?
>4. **Pregunta trampa de razonamiento**:
    - Si una dependencia está en `scope="test"`, ¿puede usarse dentro de `src/main/java`?
    - Si una dependencia de pruebas aparece en `scope="compile"`, ¿qué problema de mantenimiento puede causar?

---
# Recursos útiles:
1. [Blog Java Asjordi](https://asjordi.dev/blog/)
2. [[Spring Component Annotations]]
3. [[POST example]]
