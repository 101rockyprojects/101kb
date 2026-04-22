## 1. Ciclo de vida de Maven

Maven define un **ciclo de vida** con fases estándar:
- `compile`:
    - Compila el código de `src/main/java` a `.class`.
- `test`:
    - Compila las pruebas (`src/test/java`) y las ejecuta.
- `package`:
    - Empaqueta el proyecto (por ejemplo, `.jar` o `.war`).
- `install`:
    - Instala ese artefacto en el **repositorio local** (`.m2/repository`) para que otros proyectos puedan usarlo como dependencia.

Cuando haces `mvn install`, Maven ejecuta **todas las fases anteriores en orden**: `compile` → `test` → `package` → `install`.  
No sueles hacer `mvn package` y luego `mvn install` por separado porque `install` ya incluye `package`.

---

## 2. `pom.xml`, `dependencies`, `plugins`

- `pom.xml` es el **descriptor del proyecto** de Maven:
    - Declara nombre, versión, dependencias, plugins, etc.
- `dependencies` son las **librerías** que tu proyecto necesita:
    - Ejemplo típico en Spring Boot:
    ```xml
    <dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-web</artifactId>
	</dependency>
    ```
- `plugins` son las **herramientas** que Maven ejecuta:
    - Ejemplo típico:
    ```xml
    <plugin>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-maven-plugin</artifactId>
	</plugin>
    ```
    - Este plugin genera un JAR ejecutable con todas las dependencias empaquetadas.

---

## 3. Scopes: `compile`, `provided`, `runtime`, `test`
- `compile` (por defecto):
    - Está disponible en fase de compilación, test y runtime.
- `provided`:
    - Necesario en compilación, pero **no** se incluye en el paquete.
    - Ejemplo: `javax.servlet-api` cuando usas Tomcat o Jetty (el servidor ya lo tiene).
- `runtime`:
    - No es necesario para compilar, pero sí para ejecutar.
    - Ejemplo: un driver de base de datos (`mysql-connector-java`).
- `test`:
    - Solo para compilar y ejecutar tests (`src/test/java`).

---

## 4. Diferencia: `scope="test"` y `scope="compile"`

- Una dependencia en `scope="test"` **no debería usarse en `src/main/java`**, porque solo está disponible para tests.
    - Si la usas en el código principal, romperás compile en el entorno de producción.
- Si una dependencia de pruebas (por ejemplo, `junit` o `assertj`) está en `scope="compile"`:
    - Se incluye en el paquete, lo que aumenta el peso del JAR.
    - No es un problema crítico, pero es un mal uso de `scope` y puede confundir a otros desarrolladores.

---

## Versión modelo de respuesta (para entrevista)

> 1. Maven tiene un ciclo de vida con fases como `compile`, `test`, `package` e `install`.
>     - `mvn install` ejecuta todas las fases en orden, así que no hace falta ejecutar `package` por separado.
> 2. `pom.xml` es el descriptor del proyecto, donde declaro dependencias y plugins.
>     - Las dependencias son las librerías que mi proyecto necesita (por ejemplo, `spring-boot-starter-web`).
>     - Los plugins son herramientas que Maven ejecuta (por ejemplo, `spring-boot-maven-plugin` para generar un JAR ejecutable).
> 3. Los scopes `compile`, `provided`, `runtime` y `test` definen cuándo una dependencia está disponible.
>     - `provided` para cosas que el servidor ya tiene, `runtime` para cosas que no se usan al compilar, `test` para tests.
> 4. OJO: Una dependencia en `scope="test"` no debería usarse en `src/main/java`.
>     - Si una dependencia de pruebas está en `scope="compile"`, se incluye en el paquete, lo que no es un problema grave, pero es un mal uso de `scope`.
