# Clave‑valor, en memoria, ultra‑rápido

**Redis** es una base de datos [[NoSQL]] **clave‑valor** en memoria, pero persistente opcionalmente.
Es muy útil para:
- **Caché** de respuestas HTTP o de consultas pesadas.
- **Sesiones** compartidas entre nodos.
- **Colas de mensajería** (pub/sub, listas, etc.).
- **Contadores, rate limiters, locks distribuidos.**

Ejemplos de casos reales:
## 1. Caché de productos (evitar ir a MySQL en cada request)

```java
@Service public class ProductoService {
	@Autowired
	private ProductoRepository repository;

	@Autowired
	private RedisTemplate<String, ProductoDto> redisTemplate;
	
	public ProductoDto getProduct(Long id) {
		String key = "producto:" + id;
		ProductoDto cached = redisTemplate.opsForValue().get(key);
		
		if (cached != null) { return cached; }
		
		ProductoDto dto = convert(repository.findById(id).orElseThrow());
		redisTemplate.opsForValue().set(key, dto, Duration.ofMinutes(10));
		return dto;
	}
}
```

- Si la key está en Redis, responde en milisegundos.
- Solo si “miss”, va a la base de datos y luego guarda en Redis.

## 2. Control de sesión compartida

- En una app con varios nodos, almacenas la sesión en Redis mediante `spring-session-data-redis`.
- Todos los nodos comparten `SecurityContext` y todo el estado de login.

## 3. Pub/Sub para notificaciones
```java
@Configuration public class RedisConfig {
	@Bean
	public MessageListenerContainer messageListenerContainer() {
		RedisMessageListenerContainer container = new RedisMessageListenerContainer();
		container.setConnectionFactory(connectionFactory());
		container.addMessageListener(
			listenerAdapter(),
			new PatternTopic("eventos.*")
		);
		return container;
	}
}
```

```java
@Service public class EventPublisher {
	@Autowired
	private RedisTemplate<String, String> redisTemplate;
	
	public void publish(String topic, String mensaje) {
		redisTemplate.convertAndSend(topic, mensaje);
	}
}
```

- Un microservicio publica `eventos.pedido.confirmado`, otros servicios se suscriben y reaccionan (notificar, actualizar caché, etc.).