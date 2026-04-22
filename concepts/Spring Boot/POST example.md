## Ejemplo representativo: validación en `@PostMapping`

Supón que tienes un endpoint para crear un usuario:
```java
@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {
	private final UsuarioService service;
	
	public UsuarioController(UsuarioService service) {
		this.service = service;
	}
	
	@PostMapping
	@Validated
	public ResponseEntity<UsuarioDto> crear(@Valid @RequestBody CrearUsuarioDto dto) {
		Usuario usuario = service.crearUsuario(dto);
		return ResponseEntity.ok(UsuarioDto.from(usuario));
	}
}
```

Y el DTO:
```java
public record CrearUsuarioDto(
	@NotBlank(message = "El nombre es obligatorio")
	@Size(min = 2, max = 50, message = "El nombre debe tener entre 2 y 50 caracteres")
	String nombre,
	
	@NotBlank(message = "El email es obligatorio")
	@Email(message = "El email debe ser válido")
	String email,
	
	@Min(value = 18, message = "La edad mínima es 18")
	Integer edad,
	
	@Size(min = 8, message = "La contraseña debe tener al menos 8 caracteres")
	String password
) {}
```

---

## Validación de duplicados (negocio, no solo DTO)

Para duplicados (por ejemplo, email único) la lógica suele ir en el **servicio**:
```java
@Service
public class UsuarioService {
	private final UsuarioRepository repository;
	
	public Usuario crearUsuario(CrearUsuarioDto dto) {
		if (repository.existsByEmail(dto.email())) {
			throw new ConflictException("Ya existe un usuario con este email");
		}
		Usuario usuario = new Usuario(
			dto.nombre(),
			dto.email(),
			dto.edad(),
			encriptarPassword(dto.password())
		);
		return repository.save(usuario);
	}
	
	// ...
}
```

Aquí:
- Las anotaciones del DTO (`@NotBlank`, `@Size`, `@Min`, `@Email`) se validan automáticamente al usar `@Valid` en el controlador.
- El problema de **duplicado** se maneja en el servicio con `existsByEmail` y se lanza una excepción de negocio (por ejemplo `ConflictException`), que luego tu controlador global (`@ControllerAdvice`) convierte en un `409 Conflict` o `422 Unprocessable Entity`.

---

## Buenas prácticas visibles en el ejemplo

- **Separar DTOs**:
    - `CrearUsuarioDto` es inmutable (`record`) y solo para entrada/validación.
- **Validación en contrato**:
    - `@Valid` en el `@RequestBody` lanza `MethodArgumentNotValidException` si falla, que puedes manejar con `@ExceptionHandler` o `@ControllerAdvice` para devolver `400 Bad Request` con detalles.   
- **Validación de negocio aparte**:
    - La API de validación de JSR‑303 cubre “formato” y “rango”;
    - duplicados, reglas de negocio, etc., van en el servicio, no en el DTO.

---

## Si quieres hacerlo un poco más rico (por memorizar)

- Añadir un `@ControllerAdvice` común (Excepción personalizada):
```java
@ControllerAdvice
public class RestExceptionHandler {
	
	@ExceptionHandler(MethodArgumentNotValidException.class)
	public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
		Map<String, String> errores = 
		ex.getBindingResult().getFieldErrors().stream()
			.collect(Collectors.toMap(
			FieldError::getField,
			FieldError::getDefaultMessage
		));
		return ResponseEntity.badRequest().body(errores);
	}
}
```

Esto da una respuesta JSON con los errores de cada campo, típica en APIs REST modernas.