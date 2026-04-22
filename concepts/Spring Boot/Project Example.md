# Estructura de Proyecto *MiEmpresaApp* | Spring Boot Empresarial (DDD/Hexagonal)

## Vista general de la estructura de carpetas

```
src
├── main
│   ├── java
│   │   └── com.miempresa.miapp
│   │       ├── MiappApplication.java
│   │       ├── configuration/
│   │       │   ├── SecurityConfig.java
│   │       │   ├── KafkaConfig.java
│   │       │   ├── WebMvcConfig.java
│   │       │   └── LoggingConfig.java
│   │       ├── presentation/
│   │       │   ├── web/
│   │       │   │   ├── dto/
│   │       │   │   │   ├── CreateUserDto.java
│   │       │   │   │   └── UserResponse.java
│   │       │   │   └── controller/
│   │       │   │       ├── UserControll1er.java
│   │       │   │       └── ErrorControllerAdvice.java
│   │       ├── application/
│   │       │   ├── service/
│   │       │   │   ├── UserService.java
│   │       │   │   └── UserEventService.java
│   │       │   ├── event/
│   │       │   │   ├── event/
│   │       │   │   │   ├── UserRegisteredEvent.java
│   │       │   │   │   └── OrderPlacedEvent.java
│   │       │   │   ├── dispatcher/
│   │       │   │   │   ├── EventDispatcher.java
│   │       │   │   │   └── KafkaEventDispatcher.java
│   │       │   │   └── handler/
│   │       │   │       └── UserRegisteredEventHandler.java
│   │       ├── domain/
│   │       │   ├── model/
│   │       │   │   ├── User.java
│   │       │   │   └── UserFactory.java
│   │       │   ├── repository/
│   │       │   │   └── UserRepository.java
│   │       │   ├── service/
│   │       │   │   └── UserDomainService.java
│   │       │   └── exception/
│   │       │       └── UserAlreadyExistsException.java
│   │       ├── infrastructure/
│   │       │   ├── persistence/
│   │       │   │   ├── entity/
│   │       │   │   │   └── UserEntity.java
│   │       │   │   └── jpa/
│   │       │   │       └── UserJpaRepository.java
│   │       │   └── messaging/
│   │       │       └── kafka/
│   │       │           ├── KafkaProducerConfig.java
│   │       │           ├── KafkaUserRegisteredProducer.java
│   │       │           └── KafkaEventConsumer.java
│   │       └── shared/
│   │           ├── logging/
│   │           │   └── LoggingAspect.java
│   │           └── response/
│   │               ├── ApiResponse.java
│   │               └── ErrorResponse.java
│   └── resources/
│       ├── application.yml
│       ├── logback-spring.xml
│       └── messages.properties

```
```


## 1. **Clase principal**

```java
// MiappApplication.java
@SpringBootApplication
@EnableJpaRepositories(basePackages = "com.miempresa.miapp.infrastructure.persistence")
public class MiappApplication {
    public static void main(String[] args) {
        SpringApplication.run(MiappApplication.class, args);
    }
}
```


## 2. **Controladores y DTOs**

### **`presentation/web/dto/UserResponse.java`**

```java
public record UserResponse(
	Long id,
	String name,
	String email,
	String status
) {}
```
### `presentation/web/dto/CreateUserDto.java

```java
public record CreateUserDto(
        @NotBlank String name,
        @NotBlank @Email String email
) {}
```


### `presentation/web/controller/UserController.java`

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;

    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<UserResponse> createUser(@RequestBody @Valid CreateUserDto dto) {
        UserResponse user = userService.createUser(dto);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

### `presentation/web/controller/ErrorControllerAdvice.java`

```java
@ControllerAdvice
public class ErrorControllerAdvice {
    @ExceptionHandler(UserAlreadyExistsException.class)
    public ResponseEntity<ErrorResponse> handleUserAlreadyExists(UserAlreadyExistsException ex) {
        ErrorResponse error = new ErrorResponse("USER_ALREADY_EXISTS", ex.getMessage());
        return ResponseEntity.status(HttpStatus.CONFLICT).body(error);
    }
}
```


## 3. **Dominio**

### `domain/model/User.java`

```java
public class User {
    private Long id;
    private String name;
    private String email;
    private UserStatus status;

    public User withStatus(UserStatus status) {
        this.status = status;
        return this;
    }
}
```


### `domain/exception/UserAlreadyExistsException.java`

```java
public class UserAlreadyExistsException extends RuntimeException {
    public UserAlreadyExistsException(String message) {
        super(message);
    }
}
```

## 4. **Servicios de aplicación**

### `application/service/UserService.java`

```java
@Service
@Transactional
public class UserService {
    private final UserRepository userRepository;
    private final EventDispatcher<UserRegisteredEvent> eventDispatcher;

    public UserResponse createUser(CreateUserDto dto) {
        User user = userDomainService.createNewUser(dto);
        UserEntity saved = userRepository.save(user);
        eventDispatcher.dispatch(new UserRegisteredEvent(saved.getId(), dto.email()));
        return UserResponse.from(saved);
    }
}
```


## 5. **Eventos y Kafka**

### `application/event/event/UserRegisteredEvent.java`

```java
public record UserRegisteredEvent(
        Long userId,
        String email,
        LocalDateTime timestamp
) implements DomainEvent {}
```


### `application/event/dispatcher/KafkaEventDispatcher.java`

```java
@Service
public class KafkaEventDispatcher implements EventDispatcher<UserRegisteredEvent> {
    private final KafkaTemplate<String, String> kafkaTemplate;

    @Override
    public void dispatch(UserRegisteredEvent event) {
        kafkaTemplate.send("user-registered", event.userId().toString(), JsonUtils.toJson(event));
    }
}
```


### `infrastructure/messaging/kafka/KafkaProducerConfig.java`

```java
@Configuration
@EnableKafka
public class KafkaProducerConfig {
    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = Map.of(
            "bootstrap.servers", "localhost:9092",
            "key.serializer", StringSerializer.class,
            "value.serializer", StringSerializer.class
        );
        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public KafkaTemplate<String, String> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}
```


## 6. **Persistencia JPA**

### `infrastructure/persistence/entity/UserEntity.java`

```java
@Entity
@Table(name = "users")
public class UserEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true)
    private String email;
    
    @Enumerated(EnumType.STRING)
    private UserStatus status;
}

enum UserStatus { UNVERIFIED, ACTIVE, UNACTIVE; }
```

### `infrastructure/persistence/jpa/UserJpaRepository.java`

```java
@Repository
public interface UserJpaRepository extends JpaRepository<UserEntity, Long> {
    @Query("SELECT u FROM UserEntity u WHERE u.email = :email")
    Optional<UserEntity> findByEmail(@Param("email") String email);
    
    boolean existsByEmail(@Param("email") String email);
}
```


## 7. **Seguridad**

### `configuration/SecurityConfig.java`

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/users/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()));
        return http.build();
    }
}
```


## 8. **Logs con AOP**

### `shared/logging/LoggingAspect.java`

```java
@Aspect
@Component
@Slf4j
public class LoggingAspect {
    @Around("@annotation(LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = joinPoint.proceed();
        log.info("Execution time of {} : {} ms", joinPoint.getSignature(), System.currentTimeMillis() - start);
        return result;
    }
}
```


## 9. **application.yml**

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/miapp
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: true

kafka:
  bootstrap-servers: localhost:9092

logging:
  level:
    com.miempresa.miapp: DEBUG
    org.springframework.security: DEBUG
```


## 🎯 **Cómo navegar el proyecto**

| Acción | Dónde buscar |
| :-- | :-- |
| Endpoints REST | `presentation/web/controller/` |
| DTOs | `presentation/web/dto/` |
| Lógica de negocio | `application/service/` |
| Modelos de dominio | `domain/model/` |
| Persistencia JPA | `infrastructure/persistence/` |
| Kafka y eventos | `infrastructure/messaging/kafka/` + `application/event/` |
| Seguridad | `configuration/SecurityConfig.java` |
| Logs y utilidades | `shared/` |
| Configuraciones | `resources/application.yml` |
