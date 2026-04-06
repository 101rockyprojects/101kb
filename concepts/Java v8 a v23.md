# Java 8 → 23: Features clave y ejemplos prácticos  

## Chatgpt
  
## 1️⃣ Records  
Clases inmutables para transportar datos, como DTOs o respuestas de APIs.  
  
```java  
record Persona(String nombre, int edad) {}  
  
Persona p = new Persona("Ana", 30);  
System.out.println(p.nombre()); // Ana
```

## 2️⃣ Pattern Matching con `instanceof` y `switch`

Evita castings repetitivos y limpia el código.
```java  
Object obj = "Hola";  
  
if (obj instanceof String s) {   
    System.out.println(s.toUpperCase());   
}  
  
// Switch expression  
int day = 2;  
String nombreDia = switch(day) {  
    case 1 -> "Lunes";  
    case 2 -> "Martes";  
    default -> "Otro día";  
};  
System.out.println(nombreDia); // Martes
```
## 3️⃣ Sealed Classes

Controla qué clases pueden extender tu clase base. Útil en jerarquías de negocio.

```java  
sealed interface Shape permits Circle, Square {}  
  
final class Circle implements Shape {}  
final class Square implements Shape {}

## 4️⃣ Nuevos métodos en Collections y Streams

List<String> nombres = List.of("Ana", "Luis", "Pedro");  
List<String> mayus = nombres.stream()  
                            .map(String::toUpperCase)  
                            .toList();  
System.out.println(mayus); // [ANA, LUIS, PEDRO]  
  
Map<String, Integer> edades = Map.of("Ana", 30, "Luis", 25);  
Set<String> frutas = Set.of("Manzana", "Pera");
```
## 5️⃣ Nuevos métodos en String
```java  
String texto = "  hola\nmundo  ";  
System.out.println(texto.isBlank()); // false  
texto.lines().forEach(System.out::println); // hola\nmundo  
System.out.println(texto.strip()); // "hola\nmundo"  
System.out.println("x".repeat(5)); // xxxxx  
System.out.println("abc".indent(2)); // "\n  abc"
```
## 6️⃣ Instant::toEpochMilli
```java  
Convierte un `Instant` a milisegundos desde 1970, útil para timestamps.

Instant now = Instant.now();  
long ms = now.toEpochMilli();  
System.out.println(ms);
```
## 7️⃣ Colectores de basura útiles

- **G1 GC** → predeterminado, balance general, buena para apps con poca pausa.
    
- **ZGC** → baja latencia, apps con millones de objetos grandes.
    
- **Shenandoah** → pausas muy cortas, apps en tiempo real.
    
```java  
java -XX:+UseG1GC App.java  
java -XX:+UseZGC App.java
```
## 8️⃣ JEPs clave

- **JEP 376: Hidden Classes** → clases internas para frameworks y proxies dinámicos.
    
- **JEP 420: Pattern Matching para switch** → simplifica `switch` con tipos y valores.
    
- **JEP 436/444: Scoped Values y Virtual Threads** → reemplaza ThreadLocal y thread pools en concurrencia masiva.
    

## 9️⃣ Virtual Threads (Java 21)

Threads ligeros que permiten millones de hilos sin saturar la JVM.
```java  
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {  
    executor.submit(() -> System.out.println("Hola virtual thread"));  
}
```
## 🔟 Structured Concurrency

Agrupa tareas concurrentes y maneja excepciones de forma centralizada.
```java  
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {  
    Future<Integer> f1 = scope.fork(() -> 10);  
    Future<Integer> f2 = scope.fork(() -> 20);  
    scope.join(); // espera todos  
    int suma = f1.resultNow() + f2.resultNow();  
    System.out.println(suma); // 30  
}
```
## 1️1 Flow / Reactive Streams

Manejo de datos asincrónicos y backpressure, útil en APIs reactivas.
```java  
Flow.Publisher<Integer> publisher = subscriber -> {  
    subscriber.onSubscribe(new Flow.Subscription() {  
        public void request(long n) { subscriber.onNext(42); subscriber.onComplete(); }  
        public void cancel() {}  
    });  
};  
  
publisher.subscribe(new Flow.Subscriber<>() {  
    public void onSubscribe(Flow.Subscription s) {}  
    public void onNext(Integer item) { System.out.println(item); }  
    public void onError(Throwable t) {}  
    public void onComplete() { System.out.println("Done"); }  
});
```

## Deepseek
# 📘 Java Moderno (21/23) - Guía Rápida Laboral
## 1. Records (JEP 395)
Clases de datos inmutables sin boilerplate.
```java
// Antes (Java 8)
public class Persona {
    private final String nombre;
    private final int edad;
    // constructor, getters, equals, hashCode...
}
// Ahora (Java 14+)
public record Persona(String nombre, int edad) {}
// Uso
var p = new Persona("Ana", 30);
System.out.println(p.nombre());  // getter automático

**💡 Caso real**: DTOs para APIs, eventos, valores de retorno.
```
## 2. Pattern Matching

### Instanceof + Binding

```java

// Antes
if (obj instanceof String) {
    String s = (String) obj;
    System.out.println(s.length());
}
// Ahora
if (obj instanceof String s) {
    System.out.println(s.length());  // s ya está en scope
}
```
### Switch Expressions (→) y Pattern Matching


```java
// Switch como expresión (devuelve valor)
String tipo = switch (diasRestantes) {
    case 0 -> "vencido";
    case 1, 2, 3 -> "próximo";
    default -> "lejano";
};
// Pattern matching en switch (Java 17+)
String formato = switch (obj) {
    case Integer i -> "Número: " + i;
    case String s && s.length() > 5 -> "Texto largo: " + s;
    case null -> "es nulo";
    default -> "otro tipo";
};
```

## 3. Sealed Classes (JEP 409)

Jerarquías de clases cerradas y controladas.

```java

public sealed interface Resultado 
    permits Exito, Error, Cargando {}
public final class Exito implements Resultado {
    public final String data;
    public Exito(String data) { this.data = data; }
}
public final class Error implements Resultado {
    public final String mensaje;
    public Error(String mensaje) { this.mensaje = mensaje; }
}
public final class Cargando implements Resultado {}
// Uso ideal con switch exhaustivo
String mensaje = switch (resultado) {
    case Exito e -> "OK: " + e.data;
    case Error er -> "Error: " + er.mensaje;
    case Cargando c -> "Cargando...";
};
```
## 4. String Utilities (Java 11+)

```java

String texto = "  Hola\nMundo  ";
// Limpieza
texto.isBlank();              // true si vacío o solo espacios
texto.strip();                 // "Hola\nMundo" (trim unicode-aware)
texto.stripLeading();          // "Hola\nMundo  "
texto.stripTrailing();         // "  Hola\nMundo"
// Repetición y líneas
"0".repeat(5);                 // "00000"
texto.lines()                  // Stream<String> con cada línea
     .map(String::strip)
     .toList();                 // ["Hola", "Mundo"]
// Indentación
"linea1\nlinea2".indent(2);    // "  linea1\n  linea2\n"
```
## 5. Collections & Streams Mejoras

```java

// List.of / Set.of / Map.of (inmutables)
List<String> lista = List.of("a", "b", "c");
Set<Integer> set = Set.of(1, 2, 3);
Map.of("key1", "val1", "key2", "val2");
// copyOf (defiende contra mutaciones)
List<String> copiaDefensiva = List.copyOf(otraLista);
// Stream.toList() (Java 16)
List<String> result = stream.filter(x -> x.length() > 2)
                            .toList();  // más corto que .collect(Collectors.toList())
// Stream.mapMulti (alternativa a flatMap para 0..n elementos)
list.stream()
    .mapMulti((item, consumer) -> {
        if (item.isValid()) consumer.accept(item);
    });
```
## 6. Tiempo (Instant)

```java

// Timestamp para bases de datos/APIs
Instant ahora = Instant.now();
long milis = ahora.toEpochMilli();  // Unix timestamp
// Parseo desde timestamp
Instant instant = Instant.ofEpochMilli(1678900000000L);
```
## 7. Garbage Collectors

**Los más usados en producción:**

|GC|Cuándo usar|
|---|---|
|**G1GC** (default)|Uso general, balance throughput/latencia|
|**ZGC** (Java 15+)|Bajísima latencia (<10ms), grandes heaps (TB)|
|**Shenandoah**|Similar a ZGC, pausas cortas|

```bash

# Activar en JVM
-XX:+UseZGC
-XX:+UseShenandoahGC
```
## 8. JEPs Importantes

- **JEP 376 (ZGC)** ✅: GC concurrente, pausas <10ms.
    
- **JEP 420 (Pattern Matching switch)** ✅: Mejoras en switch con patrones.
    
- **JEP 436/444 (Virtual Threads)** ✅: Hilos virtuales para concurrencia masiva.
    

## 9. Virtual Threads (JEP 444)

```java

// Para I/O intensivo (APIs, DB, files)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<Resultado>> futures = tareas.stream()
        .map(t -> executor.submit(() -> procesar(t)))
        .toList();
    
    for (var future : futures) {
        results.add(future.get());
    }
}
// O directamente
Thread.startVirtualThread(() -> {
    llamadaBloqueante();  // no bloquea thread del SO
});
```
**💡 Regla**: Usar para tareas bloqueantes (I/O). No para CPU-bound.

## 10. Structured Concurrency (JEP 453 - Preview)

```java

// Manejo estructurado de tareas concurrentes
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Future<String> user = scope.fork(() -> fetchUser());
    Future<List<Order>> orders = scope.fork(() -> fetchOrders());
    
    scope.join();            // espera todas
    scope.throwIfFailed();   // lanza si alguna falla
    
    return new Response(user.resultNow(), orders.resultNow());
}
```
## 11. Flow (Reactive Streams - Java 9+)

```java

// Publisher - Suscriptor simple
SubmissionPublisher<String> publisher = new SubmissionPublisher<>();
publisher.subscribe(new Subscriber<>() {
    public void onNext(String item) { 
        System.out.println("Procesando: " + item); 
    }
    // ... otros métodos
});
publisher.submit("dato1");  // asíncrono
publisher.close();
```
# Consejos prácticos para entornos laborales

## ✅ Qué usar en producción vs curiosidad

| Feature | Uso en producción | Comentario |
|---------|-----------------|-----------|
| Records | Sí | DTOs, respuestas de APIs, clases inmutables. |
| Pattern Matching (`instanceof`) | Sí | Reduce castings y mejora legibilidad. |
| Switch expressions | Sí | Limpia lógica de decisiones; menos boilerplate. |
| Sealed Classes | Sí | Buen control de jerarquías cerradas de negocio. |
| Text Blocks | Sí | SQL, HTML, JSON embebido. |
| Virtual Threads | Sí, experimental estable en Java 21 | Ideal para microservicios con alta concurrencia. |
| Structured Concurrency | Sí | Mejora manejo de errores en tareas paralelas. |
| Flow / Reactive Streams | Sí | APIs reactivas, integración con WebFlux o RxJava. |
| String Templates | No (preview) | Útil pero depende de preview. |
| Sequenced Collections | No (preview) | Solo para curiosidad, usar List/Set inmutables. |

---

## 🔹 Tips de estilo profesional
1. **Usar `var` con cuidado**: limpia código pero mantener claridad de tipos.  
2. **Streams + Collectors**: preferir `.toList()`, `.toSet()` para colecciones inmutables.  
3. **String.format o Text Blocks**: mensajes legibles, logs consistentes.  
4. **Evitar features preview en producción**: salvo que sea un proyecto experimental.  
5. **Virtual Threads + Structured Concurrency**: reemplaza `ThreadPoolExecutor` en apps concurrentes modernas.

---

## 🔹 Ejemplo completo laboral
Supongamos que procesamos empleados y generamos un reporte:

```java id="emp-report"
record Empleado(String nombre, int departamento, double salario) {}

List<Empleado> empleados = List.of(
    new Empleado("Ana", 1, 1200),
    new Empleado("Luis", 2, 1500),
    new Empleado("Pedro", 1, 1100)
);

// Filtrar y mapear usando streams
Map<Integer, List<String>> porDept = empleados.stream()
    .filter(e -> e.salario() > 1000)
    .collect(Collectors.groupingBy(
        Empleado::departamento,
        Collectors.mapping(Empleado::nombre, Collectors.toList())
    ));

porDept.forEach((dep, nombres) -> 
    System.out.println("Departamento " + dep + ": " + nombres)
);
```

💡 Resultado:
```java
Departamento 1: [Ana, Pedro]  
Departamento 2: [Luis]
```