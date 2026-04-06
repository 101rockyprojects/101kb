# Colas (Queues)

Una cola es un mecanismo para **encolar mensajes** y procesarlos posteriormente (normalmente de forma asíncrona) por uno o varios consumidores.

Ejemplo mental: una cola de supermercado. Si pones 5 cajeros (consumidores), puedes procesar mas rapido en paralelo.

## Actores

- **Producer**: publica mensajes.
- **Consumer**: consume y procesa mensajes.
- (Opcional) **Broker**: infraestructura que gestiona colas, reintentos, DLQ, etc. Ej: [[tools/RabbitMQ]].

## Por qué se usan

- Desacoplar sistemas (quien produce no necesita saber quien consume).
- Absorber picos de trafico (buffer).
- Ejecutar tareas lentas fuera del request/response (emails, procesado, integraciones).

## Diferencia con API REST

- REST es tipicamente **sincrono** (request/response).
- Con colas sueles tener **asincronia** (eventual consistency).
- Lectura suele ser sincrona; escritura puede ser sincrona o asincrona segun el caso.

## Riesgos / Buenas practicas

- Duplicados: consumidores idempotentes. Ver [[concepts/Idempotencia]].
- Retries y DLQ: define politicas de reintento y mensajes "poison".
- Observabilidad: logs, correlacion, metrics.

## Related

- [[concepts/Event Driven]]
- [[concepts/CQRS]]
