Una arquitectura de microservicios divide una aplicación en una serie de servicios implementables de forma independiente que se comunican a través de API, como un conjunto de servicios pequeños, independientes y autónomos. Cada uno de estos servicios se encarga de una funcionalidad específica y se comunica con otros servicios a través de APIs bien definidas.
A diferencia de una aplicación monolítica, una arquitectura de microservicios permite a los equipos implementar nuevas funciones y hacer cambios más rápido, sin tener que volver a escribir una gran parte del código existente.

#### **Características Principales**
1. **Varios servicios de componentes**: Los microservicios se componen de servicios de componentes individuales y poco vinculados que se pueden desarrollar, implementar, operar, cambiar y volver a implementar sin afectar al funcionamiento de otros servicios o a la integridad de una aplicación. Esto permite una implementación rápida y fácil de cada una de las funciones de una aplicación.
2. **Escalabilidad**: La arquitectura de microservicios permite escalar cada servicio de forma individual, lo que es más eficiente en comparación con el escalado de una aplicación monolítica. Esto es especialmente útil en situaciones de alta demanda, ya que se pueden aumentar los recursos de un servicio específico sin afectar a toda la infraestructura.
3. **Flexibilidad Tecnológica**: Los equipos pueden elegir diferentes tecnologías y lenguajes de programación para cada microservicio, lo que les permite utilizar las herramientas más adecuadas para cada tarea. Esto fomenta la innovación y la experimentación dentro del desarrollo de software.
4. **Facilidad de Mantenimiento y Pruebas**: Al estar desacoplados, los microservicios son más fáciles de mantener y probar. Los equipos pueden realizar pruebas unitarias y de integración de manera más efectiva, lo que mejora la calidad del software y reduce el tiempo de desarrollo. Además, simplifica el proceso de aislamiento y corrección de fallos y errores en los servicios individuales.
5. **Se organizan en torno a capacidades empresariales**: Un enfoque de microservicios permite organizar los servicios en torno a las capacidades empresariales. Los equipos son multifuncionales, disponen de la gama completa de habilidades necesarias para el desarrollo y trabajan para crear una funcionalidad concreta.
## Ventajas
- **Desarrollo Ágil**: Los equipos pueden trabajar en paralelo en diferentes microservicios, lo que acelera el tiempo de desarrollo y permite una entrega continua de nuevas funcionalidades.
- **Resiliencia**: Si un microservicio falla, no necesariamente afecta a toda la aplicación, lo que mejora la disponibilidad general del sistema.
- **Adaptabilidad**: La arquitectura de microservicios es más adaptable a cambios en los requisitos del negocio, permitiendo a las organizaciones responder rápidamente a nuevas necesidades del mercado.
## Desafíos
Sin embargo, la arquitectura de microservicios también presenta ciertos desafíos:

- **Complejidad en la Gestión**: La administración de múltiples servicios puede ser compleja, requiriendo herramientas avanzadas para la monitorización y la orquestación.
- **Comunicación entre Servicios**: La interacción entre microservicios puede introducir latencias y complicaciones adicionales en la comunicación, lo que requiere un diseño cuidadoso de las APIs.
- **Costos de Implementación**: La implementación inicial de una arquitectura de microservicios puede ser más costosa debido a la necesidad de infraestructura y herramientas adecuadas para gestionar los servicios.

## Ejemplo de arquitectura de microservicios
---
Pongamos como ejemplo un hipotético proyecto de software de comercio electrónico. El siguiente diagrama es de un sitio de comercio electrónico con una aplicación web y una aplicación móvil que interactúan con varios microservicios, cada uno de los cuales proporciona funciones específicas para un dominio.

Las aplicaciones web modernas se ejecutan en navegadores y, a menudo, se sirven desde una red de distribución de contenido (CDN). Las CDN proporcionan la ventaja de poder distribuir aplicaciones web a servidores de todo el mundo, para que los navegadores web las puedan descargar rápidamente. También se utilizan para ofrecer recursos multimedia, como imágenes, audio y vídeo. Por ejemplo, en este sistema las imágenes y los vídeos de los productos a la venta se sirven desde la CDN.

![Diagrama de microservicios webfront](https://wac-cdn.atlassian.com/dam/jcr:d76e535a-b5ad-473a-b697-26dab8b73c18/microservice_architecture_v2.png?cdnVersion=2037)

##### **Los microservicios de este gráfico son los siguientes:**
##### Servicio de cuentas
El servicio de cuentas proporciona información sobre la cuenta del cliente, como la dirección y la información de pago.
##### Servicio de inventario
Ofrece información de inventario actualizada sobre los bienes que el cliente puede comprar.
##### Servicio de carrito de la compra
Los clientes lo usan para seleccionar los productos del inventario que quieren comprar.
##### Servicio de pago
Los clientes lo usan para pagar por los productos que han añadido al carrito de la compra.
##### Servicio de envío
Programa el embalaje y la entrega de los bienes adquiridos.

Las aplicaciones interactúan con los microservicios a través de las API de REST que publica cada uno de los microservicios. Una puerta de enlace de API permite que las aplicaciones se basen en las API proporcionadas por los microservicios y permite que se intercambien unos microservicios por otros con la misma API.

Cada microservicio se compone de un servicio y una base de datos. Los servicios gestionan la API de REST, implementan la lógica empresarial y almacenan datos en una base de datos. Los recursos de los distintos microservicios, como bases de datos y colas, se aíslan siguiendo el contrato de [12 Factor App](https://12factor.net/).

## Cómo crear microservicios
---
Muchas organizaciones empiezan con una arquitectura monolítica. Luego, hay que dividir una base de código en varios servicios, implementar los patrones correctos para fallar de forma limpia y recuperarte de las incidencias en la red, lidiar con la coherencia de los datos, supervisar la carga de servicio, etc. Y esto teniendo en cuenta solo la parte técnica. También hay que reorganizar los equipos y, muy probablemente, adoptar una cultura de DevOps.

Luego viene la parte difícil: descomponer el monolito en microservicios. La refactorización de un esquema de base de datos monolítico puede ser una operación delicada. Es importante determinar con claridad qué conjuntos de datos necesita cada servicio y las superposiciones. La entrega continua ayuda a reducir los riesgos de fallos de publicación, así como a conseguir que el equipo se centre en crear y ejecutar la aplicación, en lugar de quedarse atascado en implementarla.

[Aprender a crear microservicios](https://www.atlassian.com/es/microservices/microservices-architecture/building-microservices)


## Arquitectura distribuida
---
Los microservicios entran en la categoría de sistema distribuido. Un sistema distribuido es un conjunto de programas informáticos que utilizan recursos computacionales en varios nodos de cálculo distintos para lograr un objetivo compartido común. Estos sistemas consiguen mayor fiabilidad, rendimiento y facilidad de escalabilidad.

Los nodos de un sistema distribuido ofrecen redundancia, de modo que, si un nodo falla, hay otros que pueden sustituirlos y reparar el error. Cada nodo se puede escalar de forma horizontal y vertical, lo que mejora el rendimiento. Si un sistema se somete a una carga extensiva, pueden añadirse nodos adicionales para ayudar a absorber dicha carga.