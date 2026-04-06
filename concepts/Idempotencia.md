# Idempotencia

La idempotencia es la propiedad de ejecutar una operacion **varias veces** y obtener **el mismo resultado final** que si se ejecutara una sola vez.

En terminos practicos: si por red, reintentos o duplicados llega la misma peticion 2-3 veces, el sistema no deberia "duplicar efectos" (por ejemplo, cobrar dos veces).

## En APIs HTTP

- Metodos como `GET`, `PUT` y `DELETE` se consideran idempotentes por diseno.
- `POST` normalmente **no** es idempotente, pero puede hacerse idempotente con:
  - **Idempotency Key** (un header o token) y deduplicacion en servidor.
  - Un identificador de operacion (por ejemplo `orderId`) que "ancla" el efecto.

## En sistemas con colas

En mensajeria (por ejemplo con [[tools/RabbitMQ]]), lo tipico es "at-least-once delivery": un mensaje puede procesarse mas de una vez. Por eso:

- Los consumidores deben ser idempotentes (deduplicar por `messageId`, version, etc.).
- Evita side-effects no controlados (enviar emails duplicados, crear registros duplicados).

## Related

- [[concepts/Colas]]
- [[concepts/Event Driven]]
- [[tools/Stripe]] (idempotency keys suelen ser clave en pagos)
