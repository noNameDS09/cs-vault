# Step 1 — Architecture Contracts & Infrastructure Setup

**Status**: ✅ Completed  
**Date**: 2026-07-20  

---

## Objective

Establish all design contracts (System Overview, Request Flows, Database Schema, API Specifications, C4 Diagrams, and ADRs) and configure Docker Compose infrastructure before writing any business logic.

---

## Tasks Completed

- [x] **System Overview** — [docs/system-overview.md](file:///d:/Programming/enterprise-rag/docs/system-overview.md)
  - Defined platform goals, multi-tenancy requirements, subsystem architecture (Auth, Document Ingestion, Hybrid Search, Memory, LLM Router, Observability), technology stack matrix, and non-functional requirements (latency, scalability, security).

- [x] **Request & Data Flow Specifications** — [docs/request-flow.md](file:///d:/Programming/enterprise-rag/docs/request-flow.md)
  - Documented end-to-end dataflows for:
    - Document Upload & Async Ingestion (Upload → MinIO → Celery → Parser → Chunker → BGE-M3 → Qdrant/PostgreSQL).
    - Hybrid Search & Reranking (Query → BM25 + Dense → RRF Fusion → BGE Reranker v2).
    - Streaming Chat Response Generation (WebSocket → Memory → Retrieval → LLM → Token Streaming).
    - Feedback & Memory Consolidation (Rating → Fact Extraction → Semantic Memory Upsert).

- [x] **Data Model & Schema Specifications** — [docs/data-model.md](file:///d:/Programming/enterprise-rag/docs/data-model.md)
  - PostgreSQL DDL for 10 core tables: `tenants`, `users`, `roles`, `permissions`, `user_roles`, `role_permissions`, `collections`, `documents`, `document_chunks`, `conversations`, `messages`, `citations`, `jobs`.
  - Qdrant collection specs: `enterprise_documents` (1024-dim BGE-M3, tenant payload filtering) and `semantic_memories`.
  - MinIO bucket layout: `enterprise-rag-storage/tenants/{tenant_id}/raw/` and `/processed/`.

- [x] **REST & WebSocket API Specifications** — [docs/api-design.md](file:///d:/Programming/enterprise-rag/docs/api-design.md)
  - Standard JSON response envelopes (success & error).
  - REST endpoint reference matrix for Auth, Collections, Documents, Search, Chat, Conversations, Memory, Prompts, Jobs, Admin, and Monitoring.
  - WebSocket streaming protocols for `/ws/chat` (token streaming) and `/ws/jobs/{job_id}` (job progress).

- [x] **C4 Architecture Diagrams** — [docs/diagrams.md](file:///d:/Programming/enterprise-rag/docs/diagrams.md)
  - C4 Level 1: System Context Diagram — [c4-level1-context.mmd](file:///d:/Programming/enterprise-rag/docs/diagrams/c4-level1-context.mmd)
  - C4 Level 2: Container Diagram — [c4-level2-container.mmd](file:///d:/Programming/enterprise-rag/docs/diagrams/c4-level2-container.mmd)
  - C4 Level 3: Component Diagram — [c4-level3-component.mmd](file:///d:/Programming/enterprise-rag/docs/diagrams/c4-level3-component.mmd)
  - C4 Level 4: Code Structure — [c4-level4-code.mmd](file:///d:/Programming/enterprise-rag/docs/diagrams/c4-level4-code.mmd)

- [x] **Architectural Decision Record (ADR 0001)** — [docs/decisions/0001-architecture-pattern.md](file:///d:/Programming/enterprise-rag/docs/decisions/0001-architecture-pattern.md)
  - Recorded decision for Modular Monolith → Clean Architecture → Microservices evolution path and locked the full technology stack.

- [x] **Docker Compose Infrastructure** — [deployments/docker-compose.yml](file:///d:/Programming/enterprise-rag/deployments/docker-compose.yml)
  - Configured 5 backing services: PostgreSQL 16, Qdrant 1.9.2, MinIO, Redis 7, Keycloak 24.
  - All services have health checks, named volumes, and configurable ports via env vars.

- [x] **Environment Template** — [.env.example](file:///d:/Programming/enterprise-rag/.env.example)
  - Default configuration variables for all local services, database connections, and LLM providers.

---

## Key Decisions Made

| Decision | Choice |
| :--- | :--- |
| Architecture Pattern | Modular Monolith → DDD → Clean Architecture → Microservices |
| Multi-Tenancy | Shared PostgreSQL DB + `tenant_id` isolation |
| Vector Indexing | Single Qdrant collection + `tenant_id` payload filter |
| Search Pipeline | Hybrid (Dense BGE-M3 + BM25) + RRF + BGE Reranker v2 |
| Conversation Memory | 3-tier: Redis (short-term) + PostgreSQL (long-term) + Qdrant (semantic) |
| LLM Routing | Ollama (local primary) → OpenRouter (cloud fallback) |
| Authentication | Keycloak (OIDC + OAuth2 + JWT) with RBAC + ABAC |
