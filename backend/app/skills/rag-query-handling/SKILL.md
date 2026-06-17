---
name: rag-query-handling
description: Best practices for answering financial questions using RAG over bank statement data.
compatibility: crewai>=1.0.0
---

# RAG Query Handling Guidelines

When answering user questions about bank statements:

1. **Always retrieve first** — Use vector search before answering.
2. Cite specific transactions (date + amount + description) as evidence.
3. For trend questions, aggregate data by month or category.
4. If the answer cannot be found in retrieved documents, clearly state that.
5. Never hallucinate transaction details.
6. Prefer structured output (tables or bullet points) for financial summaries.