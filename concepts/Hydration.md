# Hydration (SSR -> Cliente)

La hidratacion (hydration) es el proceso por el cual **HTML renderizado en el servidor** se convierte en una aplicacion interactiva en el cliente (React/Next.js, etc.).

Cuando una aplicación web se renderiza en el servidor, se genera HTML estático que se envía al navegador. Este HTML contiene la estructura básica de la página y puede incluir datos iniciales necesarios para la aplicación. Una vez que el navegador recibe este HTML, la aplicación se "hidrata", es decir, se convierte en una aplicación interactiva en el cliente. Durante la hidratación, el framework de JavaScript toma el HTML generado en el servidor y lo convierte en una representación virtual del DOM en el cliente. Luego, el framework añade interactividad a la página, como manejo de eventos, actualización dinámica de contenido y enlaces de navegación sin recargar la página.

La hidratación es importante porque permite que las aplicaciones web construidas con frameworks de JavaScript ofrezcan una experiencia interactiva y dinámica sin sacrificar la indexación por los motores de búsqueda y la velocidad de carga inicial. Al renderizar la aplicación en el servidor y luego hidratarla en el cliente, se obtiene lo mejor de ambos mundos: la capacidad de crear aplicaciones interactivas complejas con JavaScript y la capacidad de proporcionar una experiencia inicial rápida y accesible.

## Errores comunes

- **Hydration mismatch**: el HTML del servidor no coincide con el render del cliente (fechas, random, diferencias por locale).
- Render condicional dependiente de `window`/`document` (solo existe en cliente).

## Nota (Next.js)

Si necesitas renderizar un componente que depende del cliente, suele ser mejor usar componentes client-only o lazy loading en vez de forzar hacks.

Related:
- [[concepts/Framework]]
