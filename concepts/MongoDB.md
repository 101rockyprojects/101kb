# Base de datos [[NoSQL]] **documental**.
- Cada “documento” es parecido a un JSON, y se agrupa en “colecciones” (parecido a tablas, pero sin esquema fijo).
- Muy útil cuando:
    - el esquema cambia mucho (campos opcionales, versiones, configuraciones por usuario, etc.).
    - quieres almacenar objetos complejos “tal cual” sin hacer montón de JOINS.
    - necesitas alta escalabilidad horizontal (sharding, replicación fácil).

## Ejemplo de caso real:

- **Configuración por usuario / feature flags:**
    - En lugar de tener `user_settings` + `user_features` + `user_permissions` con FK, en MongoDB podrías tener un solo documento:

```json
	{
		"userId": "123",
		"features": {
			"darkMode": true,
			"betaNotifications": false
		},
		"preferences": {
			"language": "es",
			"notifications": { "email": true, "push": false }
		}
	}
```

- Tienes todo el contexto de “configuración de usuario” en un solo documento, fácil de consultar, indexable, y evitas JOINs complejos.

## MongoDB + Spring Data Mongo:
```java
@Document(collection = "user_config")
public class UserConfig {
	@Id
	private String id;
	private Long userId;
	private Map<String, Object> features;
	private Map<String, Boolean> preferences;
	// getters / setters
}
```

```java
@Repository public interface UserConfigRepository extends MongoRepository<UserConfig, String> {
	List<UserConfig> findByUserId(Long userId);
	
	@Query("{ 'userId': ?0, 'features.betaNotifications': true }")
	List<UserConfig> findByUserAndBetaNotifications(Long userId);
}
```

Aquí:
- `@Document` marca el POJO.
- `@Query` usa **MongoDB Query Language** (no SQL ni JPQL), muy cercano al JSON.