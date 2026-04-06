# Event Driven (Arquitectura Orientada a Eventos)

Una arquitectura event-driven modela el sistema como un conjunto de componentes que **publican eventos** cuando ocurre algo relevante, y otros componentes **reaccionan** a esos eventos.

Un evento suele representar un hecho pasado: "OrderCreated", "PaymentFailed", "UserRegistered".

## Piezas tipicas

- **Producer**: emite el evento (cuando cambia el estado).
- **Broker / Bus**: distribuye eventos (colas, topics, routing).
- **Consumers**: procesan eventos (side-effects, proyecciones, integraciones).

## Cuándo usarlo

- Integraciones entre microservicios o bounded contexts.
- Flujos asíncronos (emails, notificaciones, pipelines, audit).
- Sistemas donde quieres desacoplar productores de consumidores.

## Riesgos a vigilar

- Duplicados: diseña consumidores idempotentes. Ver [[concepts/Idempotencia]].
- Observabilidad: necesitas trazas, reintentos, DLQs.
- Consistencia eventual: acepta que la informacion puede "llegar despues".

## Related

- [[concepts/Colas]]
- [[tools/RabbitMQ]]
- [[concepts/CQRS]]
