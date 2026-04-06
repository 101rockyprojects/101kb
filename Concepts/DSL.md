## ¿Qué son los Lenguajes de dominio específico (DSL)?

Un Lenguaje de dominio específico es un lenguaje de programación con un nivel superior de abstracción optimizado para una clase específica de problemas. Un DSL usa los conceptos y reglas de su campo o dominio. Es como "mi propio lenguaje SQL".

## ¿En qué se diferencian los Lenguajes de dominio específico de los lenguajes de programación "reales"?

Un lenguaje de dominio específico normalmente es menos complejo que un lenguaje de propósito general, como Java, C o Ruby. Generalmente, los DSL se desarrollan en estrecha coordinación con los expertos del campo para el que se diseña. En muchos casos, los DSL están destinados no para ser usados por expertos en software, sino por no programadores que son versados en el dominio de aplicación del DSL.

## ¿Cuáles son los beneficios de los Lenguajes de dominio específico? ¿Por qué debería importarme?

Usar DSL ofrece múltiples beneficios. El beneficio más evidente de usar DSL es que, una vez que tiene un lenguaje y un motor de transformación, su trabajo en el aspecto particular del desarrollo de software cubierto por el DSL se vuelve mucho más **eficiente**, simplemente porque no tiene que hacer el trabajo pesado manualmente. Si está generando código fuente desde su programa DSL (a diferencia de interpretarlo), puede usar abstracciones agradables y específicas para el dominio sin **pagar con sobrecargas en tiempo de ejecución**, porque el generador, al igual que un compilador, puede quitar las abstracciones y generar código eficiente.

Si tiene una forma de expresar cuestiones sobre un dominio en un lenguaje que está estrechamente alineado con el dominio, sus **pensamientos se vuelven más claros**, porque el código que escribe no está saturado con detalles de implementación. En otras palabras, usar DSL le permite separar lo esencial de la complejidad incidental.

Los DSL, cuyo dominio, abstracciones y notaciones están íntimamente alineados con la forma en que los expertos del dominio (es decir, no programadores) se expresan, permiten una excelente **integración entre los expertos en TI y los expertos en el dominio**.

Usar DSL y un motor de ejecución permite que la lógica de aplicación expresada en el código DSL sea **independiente de la plataforma de destino**. Usar DSL puede mejorar la **calidad** del producto creado: menos errores, mejor cumplimiento de la arquitectura y un mantenimiento más sencillo. Este es el resultado de eliminar grados (innecesarios) de libertad, evitar la duplicación de código