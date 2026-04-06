## **Tecnológico**
Examina el impacto de las innovaciones tecnológicas en la industria y cómo estas pueden alterar la forma en que las empresas operan. Incluye el desarrollo de nuevas tecnologías, automatización, investigación y desarrollo (I+D), y la adopción de tecnologías digitales.
## **Innovación y Oportunidades** 
Hoy en día, ya existen soluciones similares, las llamadas *'Plataformas de Soluciones Tecnológicas para el Tercer Sector'*.
#### Proyectos
El **Servicio Nacional de Aprendizaje (SENA)** está desarrollando programas de capacitación en el uso de tecnologías aplicadas al bienestar animal, incluyendo formación en telemedicina veterinaria y gestión digital de refugios. Estas iniciativas buscan preparar a los profesionales del sector para adoptar nuevas tecnologías.  
    Fuente: [SENA](https://www.sena.edu.co)

Se están promoviendo iniciativas para crear aplicaciones móviles que faciliten la adopción y donación a refugios animales, así como el seguimiento del bienestar animal mediante tecnología IoT (Internet de las Cosas), que permitirá monitorear la salud y condiciones de vida de los animales rescatados.  
    Fuente: [Innovación Tecnológica - Proyectos Futuros](https://www.innovacion.gov.co)
#### [Wingu](https://www.kiva.org/)
Es una plataforma que ofrece soluciones tecnológicas específicamente diseñadas para organizaciones del tercer sector. Facilita la gestión de los negocios dentro de esta industria mediante apoyo técnico y metodológico, así como investigación e innovación.

Colaborar con Wingu podría permitir a Cuida optimizar procesos como la visibilidad de los refugios, la recaudación de fondos y mejorar el CEO (posicionamiento en resultados de búsqueda) y con ello la transparencia en las operaciones.
#### [Kiva](https://www.kiva.org/)
Kiva es una plataforma de microfinanzas que permite a personas de todo el mundo prestar pequeñas cantidades de dinero a emprendedores y proyectos en países en desarrollo. Su objetivo es reducir la pobreza y fomentar el desarrollo económico a través de la financiación colectiva. Los prestatarios, que suelen ser individuos o pequeñas empresas, utilizan estos préstamos para iniciar o expandir sus negocios, mejorar su educación o financiar necesidades esenciales.

Inspirarse de Kiva podría ser beneficioso para Cuida, ya que se podría explorar opciones de microfinanciamiento para refugios y programas de bienestar animal. Esto para ayudar a cubrir costos operativos, fomentar la adopción de animales y fortalecer la capacidad financiera de los refugios que trabajan en la protección y cuidado de los animales en situación de calle.
#### Desarrollo de una Aplicación Móvil
Formar alianzas con empresas especializadas en el desarrollo de aplicaciones móviles podría ser una gran oportunidad para Cuida, o en su defecto contratar talento para desarrollar una app que facilite la adopción y el rescate de animales en situación de calle, así como poder publicar animales en adopción, lo que aumentaría la accesibilidad, participación y compromiso de la comunidad hacia la causa.
#### Inteligencia Artificial y Análisis de Datos
La colaboración con startups que se enfocan en inteligencia artificial puede ofrecer a Cuida herramientas para analizar datos relacionados con adopciones y donaciones. Este tipo de análisis proporcionaría información valiosa para mejorar las estrategias de captación y retención de donantes, como la posibilidad de predecir tendencias en adopción o identificar perfiles de donantes potenciales.
#### Telemedicina y Bienestar Animal
Asociarse con empresas que ofrecen soluciones de telemedicina puede facilitar el acceso a atención veterinaria para los animales en refugios. Esta opción es especialmente beneficiosa en áreas rurales, donde el acceso a veterinarios es limitado, garantizando así un mejor cuidado y bienestar para los animales.

- En 2023, la Alcaldía de Medellín implementó **tecnología 3D** para realizar cirugías en animales de compañía, permitiendo una mayor precisión en las intervenciones y reduciendo los tiempos quirúrgicos. Este avance se utilizó en casos como el de un perro llamado "Majin Buu", donde se imprimieron modelos 3D de sus extremidades para guiar la cirugía. En 2023, tan solo en Medellín, cerca de 500 animales de compañía del Centro de Bienestar Animal han requerido procedimientos quirúrgicos.
    Fuente: [Alcaldía de Medellín](https://www.medellin.gov.co/es/sala-de-prensa/noticias/medellin-aplica-tecnologia-3d-para-mejorar-la-calidad-de-vida-de-los-animales-de-compania/)

## **Tecnologías y Herramientas**
#### Frontend con Next.js y TypeScript
- **Next.js**: Se está usando para crear una interfaz de usuario rápida y optimizada para SEO. Su capacidad para renderizar en el servidor (SSR) mejora la visibilidad de los refugios en los motores de búsqueda.
- **TypeScript**: Proporcionará tipado estático, lo que ayudará a prevenir errores comunes y mejorará la mantenibilidad del código, sobre todo a la hora de recibir los datos de la API.
#### Backend con Node.js y PostgreSQL
- **Node.js**: Se usa como backend para manejar las solicitudes de la API, gestionar las rutas, controladores y variables de entorno.
- **PostgreSQL**: Almacena la información sobre los refugios, animales y donaciones de forma persistente. Para las imágenes, se piensa almacenar las rutas de las imágenes en un sistema de almacenamiento externo.
- **Supabase**: Se considera usar Amazon S3 para almacenar fotos de animales. Se guardan solo las URLs en PostgreSQL, lo que optimiza el rendimiento al evitar almacenar grandes archivos directamente en la base de datos.
#### Almacenamiento en la Nube
- **Google Cloud:** Se considera usar Google Cloud, pues ofrece una amplia variedad de servicios, uno de ellos son las máquinas virtuales, que permiten tener un entorno Linux que podemos utilizar para manejar el proyecto de forma sencilla y que solo consumirá lo necesario, siendo una alternativa económica.
- **Supabase** y **Vercel** ofrecen también sus propios servicios en la nube de forma gratuita. Son otras opciones que no está de más considerar, aunque dividiría la infraestructura del proyecto y el trabajo de despliegue.
#### Implementación de Funcionalidades Clave
- **Sistema de Autenticación**: Implementa autenticación JWT (JSON Web Tokens) para que los refugios puedan registrarse e iniciar sesión fácilmente hacia el panel. Esto se logra con ayuda de Supabase.
- **Panel de Administración**: Se desarrolla un panel donde los administradores de cada refugio puedan gestionar los datos del refugio, sus animales y necesidades.
- **Funcionalidad de Búsqueda Avanzada**: Permite a los usuarios animales según diferentes criterios (tipo de animal, posibilidad de adoptar, tamaño, etc).
#### Integración con APIs Externas
- **API de Mensajería**: Se utiliza la API de Whatsapp para la comunicación directa entre usuarios y refugios.
- **API de Pagos**: En un futuro, se busca integrar una API de pagos (como Stripe, PayU o PayPal) para facilitar donaciones directas a los refugios. Por ahora, se comunican directamente desde Whatsapp para donaciones o adoptar.

## **Estrategias para Mejorar la Visibilidad**
1. **SEO Optimizado**: Asegurarse de que cada refugio tenga su propia página optimizada con metadatos relevantes, descripciones y contenido visual atractivo.
2. **Blog Educativo**: Se pretende tener un blog dentro de la plataforma donde se publiquen artículos sobre cuidado animal, historias de adopción exitosas, eventos y consejos.
3. **Campañas en Redes Sociales**: Utiliza plataformas como Facebook e Instagram para promocionar eventos, animales disponibles para adopción y campañas de donación.
	
- ¿Qué ventajas ofrece este tipo de iniciativas hacia el tercer sector y cuánto podría afectar positivamente?
	- **Adopción de Nuevas Tecnologías**:
		La adopción de tecnologías innovadoras está en aumento, pero enfrenta desafíos como la resistencia al cambio y los costos iniciales de implementación. Las organizaciones deben invertir en capacitación y recursos para facilitar esta transición [](https://ingenierosdemarketing.com.co/los-retos-de-la-adopcion-de-las-nuevas-tecnologias/). Para "Cuida", esto significa que se debe planificar adecuadamente la capacitación del personal y los usuarios para maximizar el uso de la plataforma.
	    
	- **Costos y Recursos**:
		La inversión en tecnología puede ser significativa, incluyendo costos de desarrollo, mantenimiento y formación. Sin embargo, al implementar soluciones digitales, se pueden reducir costos operativos a largo plazo mediante la automatización de procesos y la mejora en la eficiencia [Fuente](https://ingenierosdemarketing.com.co/los-retos-de-la-adopcion-de-las-nuevas-tecnologias/).
	    
	- **Seguridad y Privacidad**:
	    A medida que se incrementa el uso de tecnologías digitales, también surgen preocupaciones sobre la seguridad y privacidad de los datos. Implementar medidas robustas de ciberseguridad es crucial para proteger la información sensible de los usuarios y las transacciones realizadas en la plataforma. [Fuente](https://ingenierosdemarketing.com.co/los-retos-de-la-adopcion-de-las-nuevas-tecnologias/)
	    
	- **Tendencias Tecnológicas Emergentes**:
	    En 2024, tendencias como la inteligencia artificial generativa, tecnologías sostenibles y soluciones sin código están ganando relevancia. Estas tecnologías pueden ser aprovechadas por Cuida para mejorar la experiencia del usuario, optimizar procesos internos y fomentar prácticas sostenibles [Fuentes](https://www.auraquantic.com/es/top-tendencias-tecnologicas/)[](https://www.computing.es/informes/las-tecnologias-para-2024-que-revolucionaran-el-mercado/).
	    
	- **Sostenibilidad y Responsabilidad Social**:
	    La tecnología también juega un papel importante en el cumplimiento de los Objetivos de Desarrollo Sostenible (ODS). Las iniciativas que promueven el bienestar animal pueden alinearse con estos objetivos al fomentar prácticas responsables y sostenibles [](https://www.auraquantic.com/es/top-tendencias-tecnologicas/). Cuida podría destacar su compromiso con la sostenibilidad al utilizar tecnologías que minimicen el impacto ambiental.
	    
	- **Interacción Comunitaria y Redes Sociales**:
	    Las plataformas digitales permiten una mayor interacción entre refugios, adoptantes y donantes a través de redes sociales. Esto puede aumentar el compromiso comunitario y facilitar campañas de sensibilización sobre adopción responsable [Fuente](https://expeditiorepositorio.utadeo.edu.co/bitstream/handle/20.500.12010/32220/Tesis%20-%20Javier%20Sarmiento.pdf?isAllowed=y&sequence=1)
	    
	- **Financiamiento y Apoyo Gubernamental**:
	    Existen oportunidades para recibir financiamiento o apoyo gubernamental para proyectos tecnológicos que aborden problemáticas sociales. Esto puede incluir subsidios o alianzas estratégicas con entidades públicas que buscan promover el bienestar animal. [Fuente](https://www.telefonica.com/es/sala-comunicacion/blog/afecta-tecnologia-medioambiente/)
	    Puede ser mediante **Contenido Generado por Usuarios (UGC)**, **Interacción orgánica** entre la plataforma Cuida y las redes de los refugios, o **eventos y colaboraciones** que se desarrollen en la ciudad y permitan hacer llegar Cuida a más usuarios, y con ello las necesidades de los refugios que confían en nosotros.
	