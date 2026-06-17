---
name: pii-handling
description: Strict PII detection and redaction rules for financial documents.
---

# PII Handling Rules (Strict)

- Detect and redact: Account numbers, names, addresses, phone numbers, emails, and transaction references.
- **Redaction Format**: Replace with `[REDACTED-ACCOUNT-XXXX]` or `[REDACTED-NAME]`.
- **Before Embedding**: All PII must be redacted before storing in vector database.
- **Audit Log**: Record what PII was detected (without storing the actual values).
- Never store raw PII in Chroma/FAISS or any vector store.
- For Hong Kong bank statements, pay special attention to 10–16 digit account numbers.