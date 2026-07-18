| Decision                     | Selected Option                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| Frontend                     | Next.js + TypeScript + Tailwind CSS + shadcn/ui                                                      |
| Backend                      | FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic v2                                                     |
| Authentication               | Keycloak (OIDC + OAuth2 + JWT)                                                                       |
| Multi-Tenancy                | Shared PostgreSQL Database + `tenant_id` Isolation                                                   |
| Object Storage               | MinIO (S3 Compatible)                                                                                |
| Primary Database             | PostgreSQL                                                                                           |
| Vector Database              | Qdrant                                                                                               |
| Cache                        | Redis + Local LRU Cache                                                                              |
| Background Jobs              | Celery + Redis                                                                                       |
| Scheduler                    | Celery Beat                                                                                          |
| Embedding Model              | BAAI BGE-M3                                                                                          |
| Reranker                     | BGE-Reranker-v2-M3                                                                                   |
| LLM Providers                | Ollama (Primary) + OpenRouter (Fallback)                                                             |
| LLM Orchestration            | Custom Orchestrator + LlamaIndex Workflows + LangGraph (for agentic workflows)                       |
| API Design                   | gRPC for internal communication + REST (via FastAPI) with WebSockets for external clients            |
| Document Parsing             | Docling + PyMuPDF + Unstructured + PaddleOCR (Fallback)                                              |
| Chunking Strategy            | Recursive + Parent-Child + Metadata-aware Chunking                                                   |
| Metadata Strategy            | Tenant-aware metadata with hierarchical document structure                                           |
| Conversation Memory          | Short-term (Redis) + Long-term (PostgreSQL) + Semantic Memory (Qdrant)                               |
| Retrieval Strategy           | Hybrid Search (Dense + BM25 + RRF + BGE Reranker)                                                    |
| Query Rewriting              | LLM-based Query Rewriting + Multi-Query Retrieval                                                    |
| Context Compression          | Contextual Compression Retriever                                                                     |
| Citation Strategy            | Page-level + Chunk-level Citations                                                                   |
| Authorization                | RBAC + ABAC                                                                                          |
| Prompt Management            | Database-backed Prompt Store with Versioning                                                         |
| LLM Routing                  | Automatic Provider Routing (Ollama → OpenRouter)                                                     |
| Prompt Guardrails            | Llama Guard + Custom Guardrails                                                                      |
| Output Validation            | Pydantic + JSON Schema Validation                                                                    |
| Evaluation Framework         | RAGAS + DeepEval                                                                                     |
| Observability                | Langfuse + OpenTelemetry                                                                             |
| Metrics                      | Prometheus + Grafana                                                                                 |
| Logging                      | Loguru + OpenTelemetry                                                                               |
| Distributed Tracing          | Jaeger + OpenTelemetry                                                                               |
| Rate Limiting                | Redis Sliding Window                                                                                 |
| Search Index Synchronization | Event-driven with Celery                                                                             |
| Secrets Management           | `.env` (Development) → HashiCorp Vault (Production)                                                  |
| Feature Flags                | Unleash                                                                                              |
| CI/CD                        | GitHub Actions                                                                                       |
| Containerization             | Docker Compose (Development) → Kubernetes (Production)                                               |
| Package Management           | uv                                                                                                   |
| Testing                      | pytest + Playwright + Locust                                                                         |
| Code Quality                 | Ruff + mypy + pre-commit                                                                             |
| Backup Strategy              | Automated PostgreSQL + MinIO Backups                                                                 |
| Infrastructure as Code       | Terraform                                                                                            |
| Future Message Broker        | Apache Kafka                                                                                         |
| Future Workflow Engine       | Temporal                                                                                             |
| Database Migrations          | Alembic                                                                                              |
| Deployment Strategy          | Docker → Kubernetes                                                                                  |
| Architecture Pattern         | Modular Monolith → DDD → Clean Architecture → Microservices → Event-Driven Architecture              |
| Documentation                | C4 Model (Context, Container, Component, Code)                                                       |
| Design Goal                  | Enterprise-grade Multi-Tenant AI Knowledge Platform with Production-ready RAG and Agentic AI Support |
