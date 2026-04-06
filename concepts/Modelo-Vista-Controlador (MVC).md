# Modelo-Vista-Controlador (MVC)

MVC es un patron de diseno muy comun en apps web. Separa responsabilidades en tres piezas:

- **Modelo**: datos + reglas de negocio (o parte de ellas, segun el enfoque).
- **Vista**: presentacion (HTML, templates, UI).
- **Controlador**: recibe la peticion, coordina el flujo, llama al modelo y retorna la vista/respuesta.

## Flujo tipico

1. Llega una request.
2. El **Controller** valida/autoriza y delega.
3. El **Model** aplica reglas y persiste/lee datos.
4. Se retorna una **View** (o JSON si es API).

## Beneficios

- Organizacion clara del codigo.
- Facilita pruebas por capas (hasta cierto punto).
- Escala bien para CRUD y apps tradicionales.

## Pitfalls comunes

- "Fat controllers" o "fat models": demasiada logica en una sola capa.
- Mezclar logica de negocio con templates.

## Ejemplos

- [[tools/Laravel]]
- [[tools/CodeIgniter]]

## Related

- [[concepts/Framework]]
