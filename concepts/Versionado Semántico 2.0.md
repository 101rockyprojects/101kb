Dado un número de versión MAYOR.MENOR.PARCHE, se incrementa:
1. La versión MAYOR cuando realizas un cambio incompatible en el API,
2. La versión MENOR cuando añades funcionalidad compatible con versiones anteriores, y
3. La versión PARCHE cuando reparas errores compatibles con versiones anteriores.
Hay disponibles etiquetas para prelanzamiento y metadata de compilación como extensiones al formato MAYOR.MENOR.PARCHE.

#### ¿Por qué debo usarlo?
Un simple ejemplo demuestra cómo el Versionado Semántico puede hacer el Infierno de Dependencias una cosa del pasado. Considera una librería llamada “Camión de bomberos”. Este requiere un paquete versionado semánticamente llamado “Escalera”. Al mismo tiempo que el “Camión de bomberos” es creado, “Escalera” está en su versión 3.1.0. Dado que “Camión de bomberos” usa una funcionalidad que fue introducida en 3.1.0, puedes especificar con seguridad la dependencia “Escalera” igual o mayor a 3.1.0 pero menor a 4.0.0. Ahora, cuando la versión “Escalera” 3.1.1 y 3.2.0 se hagan disponibles, puedes recibirlas en tu gestor de paquetes y saber que son compatibles con tu software existente.

Como desarrollador responsable vas a querer verificar, como deberías, que cada actualización de paquetes funciona como se indica. El mundo real es un lugar desordenado; no hay nada que podamos hacer excepto estar atentos. Lo que puedes hacer es dejar que el Versionado Semántico te otorgue una sana manera de publicar y actualizar paquetes sin tener que crear nuevas versiones de paquetes dependientes, ahorrándote tiempo y molestias.

Para más información: https://semver.org/lang/es/