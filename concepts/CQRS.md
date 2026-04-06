# CQRS (Command Query Responsibility Segregation)

CQRS es un patrón arquitectónico que **separa la escritura (Commands)** de la **lectura (Queries)**. En vez de tener un único modelo/diseño para todo, defines flujos distintos para:

- **Commands**: cambian estado (crear, actualizar, borrar).
- **Queries**: solo leen estado (listar, buscar, obtener detalles).

## Cuándo usar CQRS

- Cuando las necesidades de lectura y escritura son muy diferentes (rendimiento, datos, permisos).
- Cuando quieres optimizar lecturas con modelos "denormalizados" (read models) sin tocar el dominio de escritura.
- Cuando trabajas con sistemas **event-driven** y quieres proyectar eventos a vistas de lectura.

## Beneficios

- Modelos más simples: el modelo de escritura se centra en invariantes y negocio; el de lectura en queries rápidas.
- Escalado independiente: puedes escalar la parte de lectura sin escalar escritura, y viceversa.

## Costes / Tradeoffs

- Mayor complejidad: más piezas, más sincronización, más "moving parts".
- Consistencia eventual: si la lectura se alimenta de eventos/cola, puede haber un pequeño desfase.

## Related

- [[concepts/Event Driven]]
- [[concepts/Colas]]
- [[concepts/Idempotencia]]
