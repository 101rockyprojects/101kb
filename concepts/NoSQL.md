# ¿Qué es y por qué existe?

**NoSQL** no es un único producto, sino una familia de bases de datos que:
- No usan SQL estándar.
- No siempre son relacionales.
- Priorizan escalabilidad, simplicidad de schema o latencia muy baja.

Las dos que más interesa entender:
- **[[MongoDB]]** → DB documental (akin a “JSON en la base”).
- **[[Redis]]** → DB en memoria clave‑valor, muy rápida, orientada a caché, sesiones, colas, etc.

## ¿Cuándo usar qué?

|Caso de uso|SQL (JPA, MySQL, PostgreSQL)|MongoDB|Redis|
|---|---|---|---|
|CRUD típico, relaciones fuertes, reporting|✅ Ideal|⚠️ posibles JOINs lógicos en código|❌ no es para almacenar fuente de verdad|
|Esquema flexible, objetos complejos “de una sola pieza”|⚠️ posible con `JSON` en alguna columna, pero limitado|✅ Perfecto|❌ no es para estructura profunda|
|Configuraciones por usuario, drafts, contenido dinámico|⚠️ posible, pero conjoins|✅ Muy útil|⚠️ si solo quieres cachear|
|Caché, sesiones, colas, locks, counters, rate limiting|⚠️ posible, pero lento|⚠️ posible, pero no es su propósito|✅ Ideal|

**Regla sencilla de pulgar**:
- **JPA / SQL**: para tu **fuente de verdad** del negocio, con relaciones fuertes (pedidos, usuarios, inventario, facturación, etc.).
- **MongoDB**: para datos que son más documentos JSON‑like, con schema flexible, o que quieres evitar JOINS complejos.
- **Redis**: para caché, sesiones, colas, locks, flags, etc.; **no para tu fuente de verdad**, sino para **acelerar** o coordinar.

---

## 6. ¿Qué haces tú con ellos en práctica?

Un patrón muy común en backends modernos:
- **JPA + MySQL/PostgreSQL** para:
    - Usuarios, pedidos, inventario, pagos, audit.
- **MongoDB** para:
    - Configuraciones por usuario, logs estructurados, drafts, eventos enriquecidos, metadata.
- **Redis** para:
    - Caché de catálogos, sesiones, rate limit, locks distribuidos, pub/sub de eventos.

Eso te da un sistema:
- **Consistente** en el core de negocio (SQL),
- **Flexible** para configuraciones y contenido dinámico (Mongo),
- **Rápido** y resiliente en concurrencia y distribución (Redis).