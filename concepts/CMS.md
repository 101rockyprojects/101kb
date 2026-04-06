# CMS (Content Management System)

Un CMS es un sistema para **crear, editar, versionar y publicar contenido** (paginas, posts, productos, etc.) sin tener que tocar el codigo para cada cambio.

Normalmente incluye:

- Panel de administracion (usuarios, roles, permisos).
- Base de datos para el contenido.
- Flujos de publicacion (borrador -> publicado).

## CMS tradicional vs Headless CMS

- **Tradicional**: el CMS renderiza el sitio (backend + templates + contenido en un solo lugar).
- **Headless**: el CMS solo gestiona contenido y lo expone via API (REST/GraphQL); el front-end puede ser web, app, etc.

Ejemplo: [[Strapi]] es un headless CMS (nota pendiente).

## Cuándo usarlo

- Sitios donde el contenido cambia con frecuencia y lo gestiona gente no tecnica.
- Proyectos donde quieres desacoplar el front del back.

## Related

- [[concepts/Modelo-Vista-Controlador (MVC)]]
- [[concepts/Framework]]
