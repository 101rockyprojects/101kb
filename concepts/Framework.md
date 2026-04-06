# Framework

Un framework es una estructura de software reutilizable que define **una arquitectura base**, reglas y herramientas para acelerar el desarrollo. En general:

- El framework define el "camino feliz" (estructura, convenciones, lifecycle).
- Tu aplicacion se adapta al framework (inversion de control).

## Framework vs Libreria

- **Framework**: "call me" (tu codigo vive dentro del flujo del framework).
- **Libreria**: "I call you" (tu codigo llama funciones cuando quiere).

## Beneficios

- Reutilizacion de soluciones comunes (routing, DI, ORM, seguridad).
- Convenciones y estructura (mantenibilidad, onboarding).
- Comunidad y ecosistema.

## Riesgos

- Curva de aprendizaje y opinionated choices.
- Lock-in en patrones, APIs y versiones.

## Ejemplos (PHP)

- [[tools/Laravel]]
- [[tools/CodeIgniter]]
- Symfony (sin nota aun)

## Related

- [[concepts/Modelo-Vista-Controlador (MVC)]]
