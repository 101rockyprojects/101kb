# ESB (Enterprise Service Bus)

Un ESB es un **middleware** que actua como intermediario para **integrar aplicaciones** (normalmente en arquitecturas SOA). Centraliza capacidades como:

- Enrutamiento de mensajes entre sistemas.
- Transformacion de formatos (por ejemplo XML <-> JSON).
- Orquestacion y mediacion (aplicar reglas, validaciones, politicas).
- Observabilidad basica: trazas, errores, reintentos.

## Cuándo aparece

- Organizaciones con muchos sistemas legacy.
- Necesidad de integraciones "muchos a muchos" sin que cada sistema tenga que hablar con todos.

## Pros

- Reduce el acoplamiento punto-a-punto.
- Acelera integraciones si el ESB esta bien gobernado.

## Contras

- Riesgo de "monolito de integracion": el ESB se vuelve el cuello de botella y el lugar donde vive demasiada logica.
- Evolucion mas lenta si todo pasa por el bus (gobernanza, cambios, dependencias).

## Related

- [[concepts/Bus]]
- [[concepts/Colas]]
- [[concepts/Event Driven]]
