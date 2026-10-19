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
- [[Temperature]]

```cardlink
url: https://www.datalytyx.com/rag-for-dummies/
title: "RAG For Dummies - Datalytyx"
host: www.datalytyx.com
favicon: https://www.datalytyx.com/wp-content/uploads/2016/08/cropped-cropped-favicon-32x32.png
image: https://www.datalytyx.com/wp-content/uploads/2023/12/rag-for-dummies.jpg
```
