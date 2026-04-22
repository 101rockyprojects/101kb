## 🧩 Diferencias entre `@Component`, `@Service`, `@Repository`, `@Controller` y `@Bean`

### 🔹 `@Component`

- Es la **anotación base** de Spring.
- Marca una clase como **bean gestionado por el contenedor**.
- Se usa cuando no encaja en una categoría más específica.

👉 Es el “genérico”.

---

### 🔹 `@Service`

- Especialización de `@Component`.
- Se usa en la **lógica de negocio**.
```java
@Service  
public class UserService { }
```

👉 No añade comportamiento extra, pero **da semántica** (deja claro el rol).

---

### 🔹 `@Repository`

- Especialización de `@Component`.
- Se usa en la **capa de acceso a datos** (DAO, JPA, etc.).
- Añade algo importante: **traducción de excepciones** de base de datos a excepciones de Spring.
```java
@Repository  
public class UserRepository { }
```

👉 Indica que trabaja con persistencia.

---

### 🔹 `@Controller`

- Especialización de `@Component`.
- Se usa en la **capa web (MVC)** para manejar peticiones HTTP.
```java
@Controller  
public class UserController { }
```

👉 En APIs REST suele usarse `@RestController` (que incluye `@Controller + @ResponseBody`).

---

### 🔹 `@Bean`

- **No se pone en la clase**, sino en un método dentro de una clase `@Configuration`.
- Sirve para **crear y registrar manualmente un bean**.
```java
@Configuration  
public class AppConfig {  
    @Bean  
    public UserService userService() {  
        return new UserService();  
    }  
}
```

👉 Se usa cuando:
- no controlas la clase (librerías externas)
- necesitas configuración manual

---

## 🧠 Resumen rápido

|Anotación|Uso principal|Tipo|
|---|---|---|
|`@Component`|Genérico|Base|
|`@Service`|Lógica de negocio|Especialización|
|`@Repository`|Acceso a datos|Especialización|
|`@Controller`|Capa web (MVC)|Especialización|
|`@Bean`|Crear beans manualmente|Método (no clase)|

---

## ✔️ Regla práctica

- Usa **especializadas** (`@Service`, `@Repository`, etc.) siempre que puedas
- Usa `@Component` solo si no hay mejor opción
- Usa `@Bean` cuando necesites **control manual** sobre la creación