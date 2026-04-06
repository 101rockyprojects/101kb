# Pirámide de Testing

La piramide de testing es una guia para equilibrar tipos de pruebas:

- Muchas **unitarias** (rapidas, baratas).
- Algunas **integracion** (tocan base de datos, red, colas).
- Pocas **end-to-end** (lentas, fragiles, caras).

La idea no es un porcentaje exacto, sino evitar el anti-patron "ice cream cone" (demasiadas E2E, pocas unitarias).

## Por que importa

- Feedback rapido en CI.
- Menos flakiness.
- Cambios mas seguros (refactors).

## Related

- [[concepts/Framework]] (test tooling suele depender del stack)
- [[concepts/Arquitectura de Microservicios]] (integracion y contract tests)

Referencia visual:
![Piramide de Testing](https://quabu.eu/wp-content/uploads/2023/09/unnamed-1024x536.png)
