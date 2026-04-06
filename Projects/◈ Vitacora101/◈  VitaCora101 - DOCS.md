# VitaCora101 - Documentación del Producto

## Visión General
**VitaCora101** es un sistema de productividad personal diseñado para la productividad y enfoque diario, compuesto por dos servicios independientes pero interoperables:

- **VitaCora** (Frontend): Dashboard visual, intuitivo y gamificado en SvelteKit 5 + Supabase. Rastrea objetivos, tareas, eventos, hábitos y progreso con XP.
- **vitacora-core** (Backend): Cerebro agente en Spring Boot + Java 21. Procesa comandos conversacionales vía Telegram, automatiza tareas, sincroniza datos y amplía capacidades del dashboard.

**Narrativa del producto:**
"VitaCora es el dashboard que ves y usas; vitacora-core es el agente inteligente que actúa por ti."

## Problema que Resuelve
Personas que luchan contra la procrastinación, dificultad para priorizar o con TDA, necesitan:
- **Capturar ideas rápido** sin abrir apps.
- **Visualización simple** de lo *importante*.
- **Automatización** de hábitos y recordatorios.
- **Control financiero** integrado en el flujo diario.

## La Idea Detrás
Como persona he experimentado dificultad para sostener hábitos o recordar eventos, incluso con apps destinadas a mejorar la **productividad** y la mejora en diferentes ámbitos de la vida: Personal, Laboral, Emocional.
Bajo este enfoque, mi primera idea era centralizar todo en un dashboard sencillo y gamificado (conceptos de RPG) donde sume puntos de 'experiencia' para hacerlo más _familiar, intuitivo y, sobretodo, divertido_.

>"Para mí, me acostumbraría mejor si veía este proyecto más similar a un **juego** que un sistema de gestión."

Luego, entendí que lo que más me suele costar es anotar mis actividades diarias, así como recordar fechas o eventos y mantener un control de mi vida financiera, aún cuando existen apps que facilitan estos problemas de forma efectiva, surgió una idea: ¿Y si pudiese tener un agente personal que me ayude con esto sin tener que abrir **distintas apps**?

Así llegué a la conclusión de **VitaCora** un sistema híbrido que combina **UI gamificada** con **agente conversacional**, compartiendo una base de datos Supabase. El frontend da control visual; el backend reduce fricción conversacional.

> "Si quería que esto funcionase, tendría que eliminar toda fricción. Una frase simple es mejor que navegar entre apps".
> Una frase corta -> Acción del agente -> Modificación de datos -> Ver mi progreso en el dashboard.

## Reto (Portfolio-Friendly)
**Desafío:** Unificar frontend moderno (SvelteKit + Supabase realtime) con backend enterprise (Spring Boot + Kafka) en arquitectura separada, sin duplicar lógica ni acoplar servicios.  
**Solución:** Tablas compartidas + API clara + eventos asíncronos.

## Principios de Diseño
1. **Servicios independientes:** Cada repo se puede correr solo.
2. **Supabase como fuente de verdad:** Tablas compartidas, RLS para seguridad.
3. **Core como agente:** No reemplaza frontend, solo amplía capacidades.
4. **Event-driven:** Kafka para sincronización sin polling.
5. **100% gratuito:** Render, Cloudflare, Supabase free tiers.

## Modelo de Datos (vitacora-core)
Esquema compartido `vitacore`:
- users (id, telegram_id, preferences)
- tasks (id, title, due_date, status, priority, created_via_agent)
- calendar_events (id, title, date, description, reminder_sent)
- expenses (id, amount, category, date, note)
- habits (id, name, streak, last_completed)
- ...

**RLS (Row-Level Security):** Frontend lee/escribe propio user_id; core usa service role.

## Responsabilidades Exactas

### VitaCora (SvelteKit + Supabase)
✅ Dashboard, gráficos, XP, filtros, edición manual  
✅ Realtime updates via Supabase subscriptions  
✅ Auth (Supabase Auth)  
✅ Gamificación (progreso, rachas visuales)  
❌ No lógica de parsing, automatización ni bots
| **Deploy:** Cloudflare Pages

### VitaCora-core (Spring Boot)
✅ Agente Telegram: parsea comandos ("tarea dentista mañana")  
✅ Automatización: crea tasks/events en Supabase  
✅ Jobs: resúmenes semanales, recordatorios  
✅ Eventos Kafka para notificar frontend  
❌ No UI, no gamificación
| **Deploy:** Render Docker

## Diagrama de Flujo de Datos
```
Usuario Telegram ──> [vitacora-core: /api/telegram/webhook]  
	↓  
	[Parsea comando]  
		↓  
		[Supabase: tasks/calendar_events] ←── [Kafka: task.created]  
			↓  
			[VitaCora Dashboard] ── Realtime subscription ── [Supabase]  
				↓  
				[Usuario ve nueva task]
```

## Endpoints / Eventos (vitacora-core)

### API REST
- POST /api/telegram/webhook # Recibe mensajes, responde  
- GET /api/agent/health # Status agente  
- POST /api/agent/sync # Fuerza sync manual

### Kafka Topics

task.created → VitaCora realtime  
habit.completed → XP update  
summary.weekly → Notificación


## Flujo Típico
1. Usuario: "tarea gym 19:00" → Telegram → vitacora-core.
2. Core: Parsea → Crea `task` en Supabase → Emite Kafka.
3. VitaCora: Suscripción Supabase detecta cambio → Actualiza dashboard + XP.
4. Usuario abre dashboard → Ve task nueva con gamificación. [web:100][web:110][web:115]

## Tech Stack
**VitaCora:**
- SvelteKit 5 (runes), Supabase, Tailwind, Cloudflare Pages.

**vitacora-core:**
- Spring Boot 3.x, Java 21, Gradle, Kafka (Docker), Postgres (Supabase JDBC), TelegramBots, Render Docker.

## Por qué esta arquitectura gana
- **Escalabilidad:** Backend maneja carga conversacional.
- **Mantenibilidad:** Frontend ligero, backend enfocado.
- **Portfolio:** Demuestra servicios separados, eventos, realtime, agent design.

---
## Próximos Pasos Recomendados
1. Crear repo `vitacora-core`.
2. Implementar webhook Telegram + parsing básico.
3. Conectar Supabase service role.
4. Probar flujo end-to-end.

