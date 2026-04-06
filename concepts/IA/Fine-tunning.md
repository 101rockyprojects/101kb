# Fine-tuning (IA)

El fine-tuning consiste en **ajustar un modelo** entrenandolo con ejemplos tuyos para que aprenda un comportamiento especifico (estilo, formato, clasificacion, etc.).

## Cuándo tiene sentido

- Formato de salida estable y repetible (por ejemplo un JSON especifico).
- Clasificacion o extraccion con etiquetas bien definidas.
- Cuando el prompt por si solo no logra consistencia y ya tienes dataset.

## Cuándo NO (o mejor otra cosa)

- Si el problema es "no sabe" por falta de conocimiento: suele ser mejor [[concepts/IA/RAG (Retrieval-Augmented Generation)]].
- Si necesitas solo cambiar estilo/tono: a veces basta con prompt + ejemplos.

## Riesgos / Costes

- Necesitas datos de calidad (y cuidar PII).
- Puede sobreajustar: funciona en tus ejemplos pero falla fuera.
- Hay que evaluar: no es "entrenar y ya".

## Related

- [[concepts/IA/RAG (Retrieval-Augmented Generation)]]
