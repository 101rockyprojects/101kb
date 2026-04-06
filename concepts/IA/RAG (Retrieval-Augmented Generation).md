# RAG (Retrieval-Augmented Generation)

RAG es un enfoque donde el modelo no depende solo de lo que "recuerda" del entrenamiento: primero **recuperas informacion relevante** de tus documentos y luego se la das como contexto para responder.

## Pipeline tipico

- Ingesta: PDFs, docs, wikis.
- Chunking: dividir en trozos pequeños.
- Embeddings + indexado: guardar en un vector store.
- Retrieval: buscar los chunks mas relevantes a la pregunta.
- Generation: el LLM responde usando esos chunks como contexto.

## Cuándo usarlo

- Documentacion interna (policies, guias, specs).
- Soporte: respuestas basadas en tu base de conocimiento.
- Cuando el problema es conocimiento cambiante o muy especifico.

## Pitfalls comunes

- Chunking malo -> retrieval malo -> respuesta mala.
- Alucinacion si el contexto no llega o llega irrelevante.
- Necesitas evaluacion (precision de retrieval, groundedness).

## Related

- [[concepts/IA/Fine-tunning]]
