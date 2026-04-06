Darle instrucciones muy precisas a un modelo (como Claude o ChatGPT) para que genere exactamente el HTML que quieres.

Incluso para generar un proyecto simple, son necesarias buenas prácticas para que el modelo tenga un enfoque y dirección que se alinee con el resultado que buscamos.

## Better prompts Tips:
1. Task: Small, concrete and as descriptive as possible.
2. Criteria of acceptance: Check all the important aspects to validate the tasks.
3. Background info: Add files (skills.md / llm.txt), images, documentation, links, etc, needed to specify the output.
4. 'DO NOT' section: Everything you DO NOT WANT, *'don't modify'*, *'don´t do this'*. Simple and effective.
5. Tell the model to REMEMBER: Use files or skills (agents.md) that contains the most helpful information: project info, what's about, tech stack, commands, workflow, etc.
6. MCPs: Integrate MCPs to improve the performance and get the project to the next level: context7, language MCPs, chrome devtools, Canva, Obsidian, etc , all you find helpful.
7. Tests: Let the model run tests (made manually or by itself): running app, pipelines, CLI commands, CD/CI, etc. The best strategy is using TDD architecture.
8. GOOD HABITS: Use the model with an goal and a strategy. Try to be as specific as you can, provide context and give information about what you need, not what it has to do (unless you are pretty sure about what are you doing).

## Better use Tips:
1. Ejecutar IA en modo ==Plan==, es decir, que primero evalue las herramientas y el workflow ideal para el proyecto, esto lo podemos guardar como archivos markdown `.md` en la carpeta `/docs`
2. Archivo mermaid para generar gráficas y diagramas visuales que simplifique la comprensión de la arquitectura, esquema de base de datos, etc.
3. MCP con Excalidraw para generar diagramas editables que sirvan como bocetos o mapas simplificados.
4. Chrome Dev Tools para probar de forma programática el front-end: interfaz de usuario, accesibilidad, animaciones, etc.
5. SEO con [Claude SEO](https://github.com/AgriciDaniel/claude-seo) con el comando `/seo`
6. Skills para configurar de forma más específica y profesional distintas tareas. Recursos de [Skills.sh](https://skills.sh/)
7. Despliegues hacia servicios cloud por medio del CLI oficial o por SSH.

==IMPORTANTE==: Delimitar las tareas que se delegan a la IA, para evitar el uso excesivo de tokens.