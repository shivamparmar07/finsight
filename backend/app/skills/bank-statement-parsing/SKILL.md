---
name: bank-statement-parsing
description: Guidelines for parsing bank statements using YOLO layout detection + OCR + LLM.
compatibility: crewai>=1.0.0
---

# Bank Statement Parsing Guidelines

When processing bank statements, always follow these rules:

1. **Layout Detection First** — Use YOLO model to detect tables, headers, and transaction blocks before OCR.
2. **Multi-step Extraction** — Extract date, description, debit, credit, and balance columns separately when possible.
3. **Data Validation** — Cross-check extracted amounts with running balance when available.
4. **Output Format** — Always return clean structured JSON + pandas DataFrame.
5. **Error Handling** — If table detection fails, fall back to full-page OCR with LLM correction.