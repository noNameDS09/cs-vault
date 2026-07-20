
Based on what I know about your background (AI/DS student, React/Next.js, FastAPI, ML, and your goal of landing an SDE/AI internship), this is a significantly stronger resume project than a typical chatbot.

However, I would **not** build it exactly as described. I would build it as a production-grade AI system similar to what companies like OpenAI, Anthropic, Microsoft, Notion, Glean, and Atlassian deploy internally.

If you follow the right roadmap, this single project can demonstrate:

- LLM Engineering
    
- Retrieval-Augmented Generation (RAG)
    
- Backend Engineering
    
- Distributed System Design
    
- Authentication & Authorization
    
- Vector Databases
    
- Docker
    
- CI/CD
    
- Cloud Deployment
    
- Evaluation of AI Systems
    

This is much more valuable than having several small AI projects.

---

# My role

For the next 4–6 months, I'll mentor you as if you're a junior AI engineer on a production team.

That means:

- no copy-paste tutorials
    
- no "just use LangChain"
    
- understand every component
    
- build everything incrementally
    
- discuss engineering trade-offs
    
- write production-quality code
    
- document the architecture
    
- prepare for interview questions
    

---

# Phase 0 — Before Writing Any Code

Most students skip this phase.

Professional teams don't.

First understand **why RAG exists**.

Without that, you'll build a project without understanding its architecture.

We'll cover:

Week 1:

- Why LLMs hallucinate
    
- Why context windows are limited
    
- Why fine-tuning isn't enough
    
- Why embeddings work
    
- Dense retrieval
    
- Sparse retrieval
    
- Hybrid retrieval
    
- Vector databases
    
- Similarity search
    
- Metadata filtering
    
- Prompt construction
    
- Context injection
    

Only after understanding these concepts will we write code.

---

# What we'll build

Not a chatbot.

We'll build an AI platform.

```
                React Frontend

                     │

                FastAPI Backend

                     │

          Authentication Service

                     │

          Conversation Service

                     │

          Retrieval Service

         ┌───────────────┐
         │               │
         │ Hybrid Search │
         │               │
         └───────────────┘

      BM25         Vector Search

         │              │

      PostgreSQL     Qdrant

         │              │

         └────Document Store────┐

                                │

                     LLM Gateway

            GPT / Claude / Gemini

                                │

                    Final Response
```

Notice this is composed of independent services rather than one large script.

---

# Technology Stack

I recommend the following.

Frontend:

- Next.js 15
    
- TypeScript
    
- Tailwind CSS
    
- shadcn/ui
    

Backend:

- FastAPI
    
- SQLAlchemy
    
- Alembic
    
- Pydantic
    

AI:

- LangChain (only where appropriate)
    
- LlamaIndex (selectively)
    
- Instructor
    
- OpenAI SDK
    

Embeddings:

- BAAI BGE-M3
    

Vector DB:

- Qdrant
    

Database:

- PostgreSQL
    

Authentication:

- JWT
    
- OAuth (Google)
    

Storage:

- MinIO
    

Queue:

- Redis
    
- Celery
    

Deployment:

- Docker
    
- Docker Compose
    
- GitHub Actions
    

Monitoring:

- Prometheus
    
- Grafana
    

Logging:

- Loguru
    

---

# We will NOT use LangChain for everything

One mistake beginners make:

```
Everything = LangChain
```

Professional systems don't.

We'll write our own:

- retrieval pipeline
    
- prompt pipeline
    
- metadata filters
    
- reranking
    
- citations
    
- orchestration
    

LangChain will only help where it genuinely reduces boilerplate.

---

# Folder Structure

Instead of:

```
frontend/
backend/
```

We'll use:

```
enterprise-rag/

frontend/

backend/

    app/

        api/

        auth/

        chat/

        documents/

        embeddings/

        retrieval/

        llm/

        database/

        vector/

        storage/

        middleware/

        services/

        models/

        schemas/

        workers/

        utils/

tests/

docker/

scripts/

docs/

architecture/

prompts/

evaluation/
```

This resembles a production repository.

---

# Features (MVP)

We'll first build a minimal production system.

- User authentication
    
- Upload PDF
    
- Parse PDF
    
- Chunk text
    
- Create embeddings
    
- Store vectors
    
- Ask question
    
- Retrieve chunks
    
- Generate answer
    
- Show citations
    

Nothing else.

---

# Phase 2

Then we'll add:

- DOCX
    
- PPTX
    
- Excel
    
- OCR
    
- Conversation memory
    
- Metadata filtering
    
- Multi-document retrieval
    
- Streaming responses
    
- Source highlighting
    
- Chat history
    

---

# Phase 3

Then advanced AI.

- Hybrid Search
    
- BM25
    
- Cross-encoder reranking
    
- Query rewriting
    
- Self-RAG
    
- Context compression
    
- Parent-child retrieval
    
- Multi-query retrieval
    

---

# Phase 4

Enterprise features.

- RBAC
    
- Department permissions
    
- Admin dashboard
    
- Analytics
    
- Audit logs
    
- Versioned documents
    
- Background indexing
    
- Redis queue
    
- Rate limiting
    

---

# Phase 5

Research-level features.

- GraphRAG
    
- Agentic RAG
    
- Multi-agent routing
    
- Knowledge graph
    
- Tool calling
    
- Structured outputs
    
- Long-term memory
    

---

# Interview preparation

Every module will include discussion of questions such as:

- Why did you choose Qdrant over Pinecone?
    
- Why chunk by tokens instead of paragraphs?
    
- Why BGE instead of OpenAI embeddings?
    
- Why cosine similarity?
    
- Why not fine-tune the model?
    
- Why use reranking?
    
- Why hybrid search?
    
- How do you prevent hallucinations?
    
- How do you evaluate retrieval quality?
    
- Why PostgreSQL in addition to a vector database?
    

By the end, you should be able to answer these confidently.

---

# What I expect from you

- Spend 1–2 hours daily.
    
- Build every component yourself.
    
- Read the underlying papers or documentation when assigned.
    
- Avoid copying complete implementations from YouTube or GitHub.
    
- Maintain clean Git history with meaningful commits.
    
- Document architectural decisions.
    

---

# Final deliverables

By completion, you'll have:

- A production-quality GitHub repository.
    
- A deployed application.
    
- Comprehensive documentation.
    
- Architecture diagrams.
    
- API documentation.
    
- Dockerized services.
    
- CI/CD pipeline.
    
- Evaluation benchmarks.
    
- A resume-ready project with substantial interview depth.
    

---

## First milestone (Week 1)

Do **not** write code yet.

We'll build the conceptual foundation in this order:

1. How LLMs work and why they hallucinate.
    
2. Why Retrieval-Augmented Generation was invented.
    
3. What embeddings are and why they capture semantic similarity.
    
4. How vector databases index and search embeddings.
    
5. The complete lifecycle of a RAG query—from user question to cited answer.
    
6. Common failure modes in RAG systems and how modern techniques address them.
    

This foundation will make the implementation decisions much easier to understand.

I recommend treating this as your flagship portfolio project. If executed well, it is strong enough to be the centerpiece of your resume for AI Engineer, GenAI Engineer, ML Engineer, and many SDE internship applications.

Yes. If you've already spent the past few days learning the theory and you're comfortable with the core concepts, we can skip the dedicated theory phase.

Before we do, make sure you can confidently explain these without referring to notes:

- Why RAG is needed instead of only using an LLM.
    
- How embeddings work conceptually.
    
- Why vector databases are used.
    
- Chunking strategies and their trade-offs.
    
- Similarity search (cosine vs. dot product vs. Euclidean distance).
    
- Top-k retrieval.
    
- Basic prompt construction for RAG.
    
- Hallucinations and how citations reduce them.
    
- The end-to-end RAG pipeline.
    

If you can explain those, we'll move directly into implementation.

### Phase 2: Project Planning & Environment Setup

We'll first design the architecture before writing any business logic.

1. Create the repository and folder structure.
    
2. Set up Docker and Docker Compose.
    
3. Configure FastAPI.
    
4. Configure PostgreSQL.
    
5. Configure Qdrant.
    
6. Configure MinIO.
    
7. Set up the Next.js frontend.
    
8. Establish communication between frontend and backend.
    
9. Add GitHub Actions for linting and testing.
    
10. Verify that every service starts correctly.
    

At the end of this phase, you'll have a production-style development environment ready for feature development.

After that, we'll implement features in this order:

1. Authentication (JWT + RBAC)
    
2. Document upload
    
3. Document parsing
    
4. Chunking
    
5. Embedding generation
    
6. Vector indexing
    
7. Retrieval service
    
8. LLM integration
    
9. Citations
    
10. Chat interface
    
11. Conversation memory
    
12. Evaluation
    
13. Deployment
    

One suggestion: rather than building exactly the project description you shared, let's build it the way an AI startup would. That means emphasizing clean architecture, modular services, observability, testing, and evaluation—not just making the chatbot work. Those aspects make the project much stronger in interviews.

Our next task will be **designing the complete system architecture** (high-level architecture, service boundaries, database schema, and API contracts) before we write the first line of code.

I read the uploaded mentorship document. It establishes a clear philosophy: prioritize engineering judgment, requirements-driven decisions, production trade-offs, and systems thinking over tutorials or framework-specific guidance. It also emphasizes building a production-grade RAG system rather than a demo. We'll use that as the context for this mentorship going forward.

I do want to make one change to that approach.

The document explicitly forbids writing any implementation code.

I don't recommend following that restriction for this project.

The reason is simple: your objective is to produce a flagship resume project. Understanding architecture is essential, but recruiters and interviewers will ultimately evaluate the repository you've built. So our approach will be:

- First understand _why_ we're making a design decision.
    
- Then design it.
    
- Then implement it ourselves.
    
- Then test it.
    
- Then measure it.
    
- Then improve it.
    

That mirrors how engineering teams work.

---

# Our Development Process

Every major feature will follow the same cycle.

```
Problem
        ↓
Requirements
        ↓
Architecture
        ↓
Technology Selection
        ↓
Implementation
        ↓
Testing
        ↓
Evaluation
        ↓
Optimization
        ↓
Documentation
```

No shortcuts.

---

# One More Goal

I don't want this project to look like another GitHub RAG chatbot.

I want someone opening your repository to think:

> "This looks like something an AI startup could actually deploy."

That means we'll emphasize:

- Clean Architecture
    
- SOLID principles
    
- Modular services
    
- Design patterns where appropriate
    
- Production logging
    
- Metrics
    
- Evaluation
    
- Security
    
- Scalability
    
- CI/CD
    
- Documentation
    

---

# Phase 0 (Project Definition)

Before creating a repository, every engineering team writes an architecture specification.

We're going to create one.

Not because it's academic—but because changing architecture after implementation is expensive.

We'll define:

## 1. Functional Requirements

Examples:

- User authentication
    
- Upload documents
    
- Chat with documents
    
- Citations
    
- Conversation history
    
- Role-based access
    
- Admin dashboard
    
- Feedback
    

---

## 2. Non-Functional Requirements

Examples:

- Response latency
    
- Availability
    
- Scalability
    
- Security
    
- Cost constraints
    
- Maintainability
    
- Observability
    

---

## 3. High-Level Architecture

Every service.

Example:

```
Browser

↓

Frontend (Next.js)

↓

API Gateway (FastAPI)

↓

Authentication

↓

Chat Service

↓

Retrieval Service

↓

Embedding Service

↓

Document Service

↓

Storage
```

---

## 4. Data Flow

We'll map every workflow.

For example:

Document Upload

```
Upload

↓

Validation

↓

Storage

↓

Parsing

↓

Chunking

↓

Embedding

↓

Vector DB

↓

Metadata DB
```

Chat Query

```
Question

↓

Authentication

↓

Embedding

↓

Hybrid Retrieval

↓

Reranker

↓

Prompt Builder

↓

LLM

↓

Citation Generator

↓

Response
```

---

## 5. Database Design

We'll define:

- PostgreSQL schema
    
- Qdrant collections
    
- MinIO buckets
    

before implementation.

---

## 6. API Contracts

Every endpoint will be designed before coding.

Examples:

- Authentication
    
- Upload
    
- Search
    
- Chat
    
- Feedback
    
- Admin
    

---

## 7. Folder Structure

We'll justify every directory.

No "utils" dumping ground.

---

# First Engineering Decision

This is the first decision you'll make as the system architect.

**Question: What is our target deployment?**

Choose one.

**Option A — Portfolio Scale (Recommended)**

- 10–100 users
    
- Hundreds of documents
    
- Single organization
    
- Docker Compose
    
- Single VM/cloud instance
    
- Optimized for learning and interviews
    

**Option B — Startup Scale**

- 1,000–10,000 users
    
- Hundreds of thousands of documents
    
- Multiple organizations (multi-tenant)
    
- Kubernetes
    
- Background workers
    
- Horizontal scaling
    
- Production architecture
    

**Option C — Enterprise Scale**

- 50,000+ users
    
- Millions of documents
    
- Multi-region deployment
    
- Microservices
    
- Distributed indexing
    
- High availability
    
- Disaster recovery
    

---

## My recommendation

Choose **Option B (Startup Scale)**.

Why?

- It demonstrates architecture beyond a CRUD application.
    
- It's realistic for interviews at startups and larger tech companies.
    
- It introduces concepts like asynchronous processing, queues, RBAC, multi-tenancy, and scalable indexing without the operational complexity of a full enterprise deployment.
    
- You can still run it locally with Docker during development, while the design remains scalable enough to evolve.
    

We'll design for startup-scale constraints while implementing a version that runs comfortably on your machine. That's a common and practical engineering approach.

Good. We'll do both, but in the correct order.

```
Phase 1 (Development)
        ↓
Modular Monolith
        ↓
DDD
        ↓
Clean Architecture
        ↓
Production Ready
        ↓
Phase 2 (System Design)
        ↓
Microservices Migration
        ↓
Service Communication
        ↓
Event-Driven Architecture
        ↓
Scalability
```

Reason:

- Learn DDD and Clean Architecture without distributed systems complexity.
    
- Build a working application.
    
- Then refactor selected modules into microservices. This demonstrates architectural evolution, which interviewers value more than starting with microservices.
    

Final architecture target:

```
Presentation
        │
Application
        │
Domain
        │
Infrastructure

                ↓

Auth Service
Document Service
Ingestion Service
Retrieval Service
LLM Service
Chat Service
Evaluation Service
```

This gives you:

- ✅ DDD
    
- ✅ Clean Architecture
    
- ✅ Modular Monolith
    
- ✅ Microservices Migration
    
- ✅ Event-Driven Design
    
- ✅ Production Architecture
    

Next question:

**Backend: FastAPI or ASP.NET Core?** (Recommendation: **FastAPI** for this project.)

Noted.

**Current stack (locked):**

|Layer|Technology|
|---|---|
|Frontend|Next.js + TypeScript + Tailwind + shadcn/ui|
|Backend|FastAPI|
|Database|PostgreSQL|
|Vector DB|Qdrant|
|Object Storage|MinIO|
|Cache|Redis|
|Queue|Celery + Redis|
|AI|LlamaIndex (retrieval) + native SDKs|
|Embeddings|BAAI BGE-M3|
|Reranker|BGE Reranker|
|LLM|GPT-5 / Claude (pluggable)|
|Auth|JWT + OAuth|
|Deployment|Docker + Docker Compose|
|CI/CD|GitHub Actions|
|Architecture|DDD + Clean Architecture + Modular Monolith → Microservices|

Next question:

**Database ORM: SQLAlchemy 2.0 + Alembic?** (Recommended: **Yes**.)

Agreed. That's a better learning path.

### Stack (v1.0)

|Layer|Technology|
|---|---|
|Frontend|Next.js, TypeScript, TailwindCSS, shadcn/ui|
|Backend|FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2|
|Vector DB|Qdrant|
|Database|PostgreSQL|
|Object Storage|MinIO|
|Cache|Redis|
|Queue|Celery + Redis|
|Document Parsing|Unstructured, PyMuPDF, Docling|
|OCR|Tesseract + PaddleOCR|
|Embeddings|**BAAI BGE-M3**|
|Reranker|**BAAI BGE-Reranker-v2-M3**|
|LLM|**Qwen 3 / Llama 3.x (self-hosted)**|
|Inference|vLLM|
|Retrieval|LlamaIndex (only where beneficial) + custom pipeline|
|Observability|OpenTelemetry + Prometheus + Grafana + Loki|
|Testing|Pytest|
|API Docs|OpenAPI (FastAPI)|
|Auth|Keycloak + JWT/OAuth2|
|Containers|Docker + Docker Compose|
|CI/CD|GitHub Actions|

### Principles

- ✅ Open source first
    
- ✅ Self-host wherever practical
    
- ✅ Avoid vendor lock-in
    
- ✅ Replace framework abstractions with custom implementations once concepts are understood
    
- ✅ Production-grade architecture
    

**Exception:** We may temporarily use a hosted API during development if your hardware cannot comfortably run a large model locally. The architecture will remain provider-agnostic so switching to a local model is just a configuration change.

---

**Next question:**

**Do you have an NVIDIA GPU (and VRAM size), or should we assume CPU-only development?**

Perfect.

Updated constraints:

- GPU: **RTX 4050 Laptop (6 GB VRAM)** ✅
    
- Local inference: **Ollama** ✅
    
- Cloud fallback: **OpenRouter (free models)** ✅
    

We'll use a **provider abstraction**:

```text
LLM Interface
      │
 ┌────┴────┐
 │         │
Ollama   OpenRouter
(Local)   (Cloud)
```

Local (default):

- Qwen 3 (4B/8B depending on VRAM)
    
- Llama 3.2 3B
    
- Gemma 3 4B
    
- DeepSeek-R1 Distill (small variants)
    

Cloud (fallback):

- Free OpenRouter models for benchmarking and comparison.
    

This also lets us evaluate different models on the same RAG pipeline.

---

**One recommendation:** don't use Ollama for embeddings.

Use **Sentence Transformers** directly for:

- BGE-M3
    
- BGE-Reranker-v2-M3
    

Reason: lower latency, more control, and it's the standard approach in production.

---

## Current Architecture Status: 10%

The next milestone is **Architecture Specification v1**:

1. Functional Requirements
    
2. Non-Functional Requirements
    
3. C4 Context Diagram
    
4. C4 Container Diagram
    
5. Database Design
    
6. Domain Model
    
7. API Contracts
    

**Next question:**

**Do you want to document the architecture using the C4 Model (recommended), or traditional block diagrams?** (Recommendation: **C4 Model**.)

Locked. ✅

```text
Document Upload

User
  │
  ▼
Upload API
  │
  ▼
MinIO
  │
  ▼
Celery Queue
  │
  ▼
Parser
  │
  ▼
Chunker
  │
  ▼
Embedding
  │
  ▼
Qdrant + PostgreSQL
```

Benefits:

- Non-blocking uploads
    
- Retry support
    
- Parallel processing
    
- Scalable workers
    
- Better UX
    

**Architecture progress:** ~20%

---

### Next Question

**Vector indexing strategy?**

- **Single Qdrant collection + tenant_id payload filter** (**Recommended**)
    
- Separate collection per tenant
    
- Separate Qdrant instance per tenant

Locked. ✅

```text
Qdrant
└── enterprise_documents
      ├── tenant_id
      ├── document_id
      ├── chunk_id
      ├── department
      ├── access_level
      ├── document_type
      ├── language
      └── metadata...
```

Reason:

- Lower operational complexity
    
- Efficient payload filtering
    
- Easier backups/migrations
    
- Scales well for our target architecture
    

**Architecture progress:** ~25%

---

### Next Question

**Search pipeline?**

- **Hybrid Search (BM25 + Dense Retrieval + Reranker)** **(Recommended)**
    
- Dense Retrieval only

Locked. ✅

```text
Query
  │
  ▼
Query Rewriter (future)
  │
  ▼
BM25 + Dense Retrieval (BGE-M3)
  │
  ▼
Reciprocal Rank Fusion (RRF)
  │
  ▼
BGE-Reranker
  │
  ▼
Context Builder
  │
  ▼
LLM
  │
  ▼
Citations
```

We'll implement incrementally:

1. Dense Retrieval
    
2. BM25
    
3. Hybrid (RRF)
    
4. Reranker
    
5. Query Rewriting
    

**Architecture progress:** ~30%

---

### Next Question

**Chunking strategy?**

- **Recursive + Parent-Child + Metadata-aware** (**Recommended**)
    
- Fixed-size chunks
    
- Semantic chunking only

Locked. ✅

```text
Document
    │
    ▼
Structure Extraction
    │
    ▼
Metadata Extraction
    │
    ▼
Parent Sections
    │
    ▼
Recursive Chunking
    │
    ▼
Child Chunks
    │
    ▼
Embeddings
```

Metadata per chunk:

- tenant_id
    
- document_id
    
- parent_id
    
- chunk_id
    
- page_no
    
- section_heading
    
- document_type
    
- department
    
- language
    
- access_level
    
- version
    
- created_at
    

We'll also preserve the document hierarchy for future:

- Context Expansion
    
- Parent Retrieval
    
- GraphRAG
    

**Architecture progress:** ~35%

---

### Next Question

**Document parsing framework?**

**Recommendation:** **Docling + PyMuPDF + Unstructured + PaddleOCR (fallback)**

This gives excellent support for PDFs, Office documents, tables, images, and scanned documents.


Locked. ✅

```text
Document Processing

            Upload
               │
               ▼
          Docling (Primary)
               │
      ┌────────┴────────┐
      ▼                 ▼
 PyMuPDF          Unstructured
      │                 │
      └────────┬────────┘
               ▼
      PaddleOCR (Fallback)
               │
               ▼
      Unified Document Model
```

Processing order:

1. Docling
    
2. PyMuPDF (PDF-specific enhancements)
    
3. Unstructured (edge cases)
    
4. PaddleOCR (scanned pages/images)
    

This stack is currently among the strongest open-source choices for enterprise document ingestion.

**Architecture progress:** ~40%

---

### Next Question

**Conversation memory strategy?**

- **Short-term (Redis) + Long-term (PostgreSQL) + Semantic Memory (Qdrant)** **(Recommended)**

Conversation memory is how the system remembers previous interactions at different time horizons. For an enterprise RAG system, I recommend **three layers**:

```text
User
  │
  ▼
Short-Term Memory (Redis)
- Current conversation
- Recent turns
- Fast expiry

        │
        ▼
Long-Term Memory (PostgreSQL)
- Chat history
- Sessions
- Audit trail

        │
        ▼
Semantic Memory (Qdrant)
- Important facts/preferences
- Retrieved only when relevant
```

Purpose:

- **Redis:** Low-latency conversational context.
    
- **PostgreSQL:** Persistent history and compliance.
    
- **Qdrant:** Semantic recall without sending entire chat history to the LLM.
    

For our project: **Yes, we'll implement all three.**

---

**Next question:**

**LLM orchestration?**

- **Custom orchestration (Recommended)**
    
- LlamaIndex Agents
    
- LangGraph

Locked. ✅

```text
Memory

Redis
├── Active conversation
├── Session state
└── TTL

PostgreSQL
├── Chat history
├── Sessions
├── Feedback
└── Audit logs

Qdrant
├── Semantic memories
├── Long-term retrieval
└── Context recall
```

**Architecture progress:** ~45%

---

### Next Question

**LLM orchestration?**

- **Custom orchestration (Recommended)** → Maximum learning, no framework lock-in
    
- LangGraph
    
- LlamaIndex Workflows

Locked. ✅

```text
LLM Orchestration

               Request
                  │
                  ▼
        Custom Orchestrator
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 LlamaIndex Workflows   LangGraph
        │                   │
        └─────────┬─────────┘
                  ▼
             Provider Layer
        (Ollama/OpenRouter)
```

Rules:

- **LlamaIndex Workflows** → RAG pipeline (ingestion, retrieval, indexing)
    
- **LangGraph** → Agentic workflows (future)
    
- **Custom Orchestrator** → Business logic, routing, retries, observability, provider abstraction
    

This gives us the best of all three while keeping our core logic independent of any framework.

**Architecture progress:** ~50%

---

## Next Question

**API Design?**

- **REST (FastAPI) + WebSockets (Streaming Chat)** **(Recommended)**
    
- GraphQL
    
- gRPC (internal) + REST (external)

Locked. ✅ This is the architecture I'd choose for a production-grade enterprise platform.

```text
                    External Clients
         (Web, Mobile, Desktop, CLI)
                    │
         REST + WebSockets (FastAPI)
                    │
          ┌─────────┴─────────┐
          │                   │
     API Gateway         Authentication
                              │
                          Keycloak
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
     RAG Service                         Document Service
          │                                       │
          ├──────────── gRPC ─────────────────────┤
          │                                       │
    Memory Service                       Search Service
          │                                       │
          ├──────────── gRPC ─────────────────────┤
          │                                       │
     Worker Service                      Notification Service
```

### Communication Strategy

|Layer|Protocol|Reason|
|---|---|---|
|Browser ↔ API|REST|Simple, standard, OpenAPI support|
|Browser ↔ API|WebSockets|Streaming LLM tokens, live progress, notifications|
|Service ↔ Service|gRPC|High performance, strongly typed, HTTP/2|
|Background Jobs|Celery + Redis|Asynchronous processing|
|Event Distribution (future)|Kafka/NATS|Event-driven architecture|

### Benefits

- Clear separation between external and internal APIs.
    
- Automatic OpenAPI documentation through FastAPI.
    
- Bidirectional streaming for chat responses.
    
- Efficient binary serialization with Protocol Buffers for internal communication.
    
- Easier migration to Kubernetes and microservices.
    
- Independent scaling of each service.
    

---

## Architecture Progress

```text
██████████░░░░░░░░░░ 50%
```

The remaining 50% will cover the implementation-oriented decisions:

1. Authorization model (RBAC/ABAC/ReBAC)
    
2. Prompt management
    
3. Retrieval pipeline details
    
4. Evaluation framework (RAGAS, DeepEval, etc.)
    
5. Guardrails and safety
    
6. Observability (OpenTelemetry, Langfuse, Prometheus, Grafana)
    
7. Caching strategy
    
8. Rate limiting and quotas
    
9. CI/CD pipeline
    
10. Kubernetes deployment
    
11. Monitoring and alerting
    
12. Testing strategy
    
13. Disaster recovery and backups
    
14. Multi-region scalability
    
15. Cost optimization
    
16. Security and compliance
    
17. Production folder structure
    
18. Database schema
    
19. C4 diagrams
    
20. Complete implementation roadmap
    

At this point, the architecture has moved beyond a basic RAG application and into the design of a production-ready AI platform suitable for enterprise deployment and as a strong flagship portfolio project.

Good idea. At this point, the remaining decisions are mostly independent, so it's more efficient to decide them in one pass.

Copy this list and reply with your choices (or edit my recommendations).

|#|Decision|Options|Recommended|
|---|---|---|---|
|1|Authorization Model|RBAC / ABAC / ReBAC / **RBAC + ABAC**|⭐ RBAC + ABAC|
|2|Prompt Management|Hardcoded / YAML / Database / **Database + Versioning**|⭐ Database + Versioning|
|3|Query Rewriting|None / LLM Rewrite / HyDE / Multi-Query / **LLM + Multi-Query**|⭐ LLM + Multi-Query|
|4|Retrieval Strategy|Dense / BM25 / Hybrid / **Hybrid + RRF + Reranker**|⭐ Hybrid + RRF + Reranker|
|5|Context Compression|None / LLM Compression / Contextual Compression Retriever|⭐ Contextual Compression|
|6|Citation Strategy|Chunk / Page / Paragraph / **Page + Chunk**|⭐ Page + Chunk|
|7|LLM Provider Routing|Fixed / Manual / **Automatic (Ollama → OpenRouter)**|⭐ Automatic|
|8|Prompt Guardrails|None / Regex / Llama Guard / NeMo Guardrails / **Llama Guard + Custom**|⭐ Llama Guard + Custom|
|9|Output Validation|None / JSON Schema / Pydantic / Guardrails AI / **Pydantic + JSON Schema**|⭐ Pydantic + JSON Schema|
|10|Evaluation Framework|Manual / RAGAS / DeepEval / Phoenix / **RAGAS + DeepEval**|⭐ RAGAS + DeepEval|
|11|Observability|Basic Logs / LangSmith / Langfuse / OpenTelemetry / **Langfuse + OpenTelemetry**|⭐ Langfuse + OpenTelemetry|
|12|Metrics Storage|PostgreSQL / Prometheus / **Prometheus + Grafana**|⭐ Prometheus + Grafana|
|13|Logging|print / logging / structlog / **Loguru + OpenTelemetry**|⭐ Loguru + OpenTelemetry|
|14|Distributed Tracing|None / Jaeger / Zipkin / **Jaeger + OpenTelemetry**|⭐ Jaeger + OpenTelemetry|
|15|API Rate Limiting|FastAPI only / Redis / **Redis Sliding Window**|⭐ Redis Sliding Window|
|16|Caching|Redis only / Multi-layer / **Redis + Local LRU**|⭐ Redis + Local LRU|
|17|Background Queue|Celery / Dramatiq / RQ / Arq / **Celery**|⭐ Celery|
|18|Scheduling|Cron / Celery Beat / APScheduler / **Celery Beat**|⭐ Celery Beat|
|19|Secrets Management|.env / Vault / Doppler / **.env → Vault later**|⭐ .env → Vault|
|20|Feature Flags|None / LaunchDarkly / Unleash / **Unleash**|⭐ Unleash|
|21|Object Storage|Local FS / MinIO / S3 / **MinIO (S3 Compatible)**|⭐ MinIO|
|22|Search Index Sync|Manual / Event-based / **Celery Events**|⭐ Celery Events|
|23|CI/CD|GitHub Actions / GitLab CI / Jenkins / **GitHub Actions**|⭐ GitHub Actions|
|24|Container Orchestration|Docker Compose / Kubernetes / **Compose → Kubernetes**|⭐ Compose → Kubernetes|
|25|Package Management|pip / Poetry / uv / **uv**|⭐ uv|
|26|Testing|pytest / unittest / **pytest + Playwright + Locust**|⭐ pytest + Playwright + Locust|
|27|Code Quality|Black / Ruff / mypy / **Ruff + mypy + pre-commit**|⭐ Ruff + mypy + pre-commit|
|28|Backup Strategy|DB Dump / Snapshot / **Automated PostgreSQL + MinIO Backups**|⭐ Automated|
|29|Deployment|VM / Docker / Kubernetes / **Docker → Kubernetes**|⭐ Docker → Kubernetes|
|30|Infrastructure as Code|None / Terraform / Pulumi / **Terraform**|⭐ Terraform|
|31|Message Broker (Future)|Redis / RabbitMQ / Kafka / NATS / **Kafka**|⭐ Kafka|
|32|Workflow Engine (Future)|Celery / Temporal / Prefect / **Temporal**|⭐ Temporal|
|33|Authentication|JWT / OAuth2 / OIDC / **Keycloak (OIDC + OAuth2 + JWT)**|✅ Already chosen|
|34|Database Migration|SQLAlchemy only / Alembic / **Alembic**|⭐ Alembic|
|35|Database Schema|Single DB / Multi DB / **Shared DB + tenant_id**|✅ Already chosen|
|36|Vector DB|Pinecone / Weaviate / Milvus / **Qdrant**|✅ Already chosen|
|37|Embedding Model|OpenAI / E5 / **BGE-M3**|✅ Already chosen|
|38|Reranker|Cohere / Jina / **BGE-Reranker-v2-M3**|✅ Already chosen|
|39|Memory|Redis / PostgreSQL / Vector / **All Three**|✅ Already chosen|
|40|Internal Communication|REST / gRPC / **gRPC**|✅ Already chosen|

After these decisions are finalized, the design phase is essentially complete. The remaining work is implementation: designing the folder structure, defining database schemas and APIs, creating the C4 diagrams, and building each service incrementally. This will give you an architecture comparable to modern enterprise AI platforms rather than a typical tutorial RAG application.

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

### C4 Level 1 — System Context

```text
                    ┌──────────────────────┐
                    │      End Users       │
                    │ Employees/Admin/API  │
                    └──────────┬───────────┘
                               │
                               ▼
                 Enterprise AI Knowledge Platform
                               │
        ┌───────────┬──────────┼──────────┬──────────┐
        ▼           ▼          ▼          ▼          ▼
   Keycloak     Ollama    OpenRouter    MinIO     PostgreSQL
 (Identity)      (LLM)      (LLM)      (Files)     (Metadata)
                               │
                               ▼
                            Qdrant
                      (Vector Database)
                               │
                               ▼
                             Redis
                    (Cache & Session Memory)
```

### External Systems

|System|Purpose|
|---|---|
|Keycloak|Authentication & Authorization|
|Ollama|Local LLM inference|
|OpenRouter|Cloud LLM fallback|
|PostgreSQL|Structured data|
|Qdrant|Vector search|
|MinIO|Document storage|
|Redis|Cache, sessions, Celery broker|

---

**Next:** C4 Level 2 (Container Diagram), where we'll define the internal containers/modules and their interactions.

## C4 Level 2 — Container Diagram

```text
                          Users
                            │
          REST / WebSocket (FastAPI)
                            │
                    API Gateway
                            │
      ┌───────────┬──────────┼───────────┬───────────┐
      ▼           ▼          ▼           ▼           ▼
 Auth Module  Document    RAG Core   Memory     Admin Module
              Module                  Module
                  │          │           │
                  ▼          ▼           ▼
             Search Module  LLM Module  Worker Module
                  │          │           │
                  └──────┬───┴──────┬────┘
                         ▼          ▼
                  PostgreSQL   Redis
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           Qdrant                MinIO
```

---

# C4 Level 3 — Component Diagram

```text
API Gateway
│
├── Auth Controller
├── Chat Controller
├── Document Controller
├── Search Controller
├── Admin Controller
└── WebSocket Controller

RAG Core
│
├── Query Rewriter
├── Hybrid Retriever
├── RRF Fusion
├── BGE Reranker
├── Context Builder
├── Prompt Builder
├── LLM Orchestrator
└── Citation Generator

Document Module
│
├── Upload Manager
├── Parser
├── OCR
├── Metadata Extractor
├── Chunker
├── Embedding Generator
└── Indexing Pipeline

Memory Module
│
├── Redis Memory
├── Chat History
├── Semantic Memory
└── Context Recall

Search Module
│
├── BM25
├── Dense Search
├── Hybrid Fusion
└── Metadata Filter

LLM Module
│
├── Provider Router
├── Ollama Adapter
├── OpenRouter Adapter
├── Prompt Manager
└── Output Validator

Worker Module
│
├── Document Processing
├── Embedding Jobs
├── Reindex Jobs
├── Cleanup Jobs
└── Scheduled Jobs
```

---

# C4 Level 4 — Code Structure

```text
src/
│
├── api/
│   ├── routes/
│   ├── websocket/
│   ├── middleware/
│   └── dependencies/
│
├── auth/
│   ├── keycloak/
│   ├── permissions/
│   └── policies/
│
├── document/
│   ├── parser/
│   ├── chunking/
│   ├── metadata/
│   ├── indexing/
│   └── services/
│
├── rag/
│   ├── retrieval/
│   ├── reranking/
│   ├── prompts/
│   ├── orchestration/
│   ├── citations/
│   └── pipeline/
│
├── memory/
│   ├── redis/
│   ├── postgres/
│   ├── vector/
│   └── services/
│
├── llm/
│   ├── providers/
│   ├── ollama/
│   ├── openrouter/
│   └── router/
│
├── search/
│   ├── bm25/
│   ├── dense/
│   ├── hybrid/
│   └── filters/
│
├── workers/
│   ├── celery/
│   ├── tasks/
│   └── scheduler/
│
├── storage/
│   ├── postgres/
│   ├── qdrant/
│   ├── redis/
│   └── minio/
│
├── observability/
│   ├── logging/
│   ├── metrics/
│   └── tracing/
│
├── common/
│   ├── config/
│   ├── exceptions/
│   ├── utils/
│   └── constants/
│
└── tests/
```

---

## Implementation Order

1. Repository & Project Setup
    
2. Configuration Management
    
3. Database & Alembic
    
4. Keycloak Authentication
    
5. MinIO Integration
    
6. Document Ingestion Pipeline
    
7. Embedding Pipeline
    
8. Qdrant Integration
    
9. Hybrid Retrieval
    
10. Reranker
    
11. LLM Orchestration
    
12. Streaming Chat
    
13. Conversation Memory
    
14. Evaluation Framework
    
15. Observability
    
16. CI/CD
    
17. Docker Compose
    
18. Kubernetes Deployment
    

This completes the **C4 architecture**. The next phase is the **low-level system design** (ER diagrams, database schema, API contracts, gRPC contracts, and detailed folder structure) before implementation.

**Next phase first. Don't create folders yet.**

A common mistake is creating a folder structure before the design is stable. As the schema and APIs evolve, you'll end up renaming and moving many directories.

Follow this order instead:

|Step|Status|
|---|---|
|High-Level Architecture|✅|
|C4 Diagrams|✅|
|Database Schema (ERD)|⏭️ Next|
|API Contracts (REST)|⏭️|
|gRPC Contracts|⏭️|
|Event Contracts|⏭️|
|Folder Structure|⏭️|
|Repository Initialization|⏭️|
|Implementation|⏭️|

I recommend designing these before writing any code:

1. **Database Schema**
    
    - Tables
        
    - Relationships
        
    - Indexes
        
    - `tenant_id`
        
    - UUID strategy
        
2. **REST API Specification**
    
    - Endpoints
        
    - Request/Response models
        
    - Error format
        
    - Streaming APIs
        
3. **gRPC Services**
    
    - `.proto` files
        
    - Messages
        
    - Service definitions
        
4. **Event Model**
    
    - `DocumentUploaded`
        
    - `DocumentIndexed`
        
    - `EmbeddingGenerated`
        
    - `ChatCompleted`
        
    - etc.
        
5. **Folder Structure**
    
    - Now you'll know exactly why each folder exists.
        
6. **Initialize Repository**
    
    - `uv`
        
    - Docker Compose
        
    - Alembic
        
    - FastAPI
        
    - Celery
        
    - Redis
        
    - PostgreSQL
        
    - MinIO
        
    - Qdrant
        

Only then start implementing features.

This approach is much closer to how large engineering teams work: **design contracts first, then build against those contracts.**


Below is a complete REST API contract (v1) for the platform. It is organized by domain rather than implementation, making it suitable for OpenAPI generation.

|Method|Endpoint|Description|
|---|---|---|
|**Authentication**|||
|GET|`/api/v1/auth/login`|Login via Keycloak|
|POST|`/api/v1/auth/refresh`|Refresh access token|
|POST|`/api/v1/auth/logout`|Logout|
|GET|`/api/v1/auth/me`|Current user profile|
|GET|`/api/v1/auth/permissions`|User permissions|
|**Users**|||
|GET|`/api/v1/users`|List users|
|GET|`/api/v1/users/{id}`|User details|
|POST|`/api/v1/users`|Create user|
|PATCH|`/api/v1/users/{id}`|Update user|
|DELETE|`/api/v1/users/{id}`|Delete user|
|**Tenants**|||
|GET|`/api/v1/tenants`|List tenants|
|POST|`/api/v1/tenants`|Create tenant|
|GET|`/api/v1/tenants/{id}`|Tenant details|
|PATCH|`/api/v1/tenants/{id}`|Update tenant|
|DELETE|`/api/v1/tenants/{id}`|Delete tenant|
|**Documents**|||
|POST|`/api/v1/documents/upload`|Upload document|
|GET|`/api/v1/documents`|List documents|
|GET|`/api/v1/documents/{id}`|Document metadata|
|GET|`/api/v1/documents/{id}/status`|Processing status|
|GET|`/api/v1/documents/{id}/chunks`|Document chunks|
|GET|`/api/v1/documents/{id}/download`|Download original|
|PATCH|`/api/v1/documents/{id}`|Update metadata|
|DELETE|`/api/v1/documents/{id}`|Delete document|
|POST|`/api/v1/documents/{id}/reindex`|Re-index document|
|POST|`/api/v1/documents/{id}/reembed`|Regenerate embeddings|
|**Collections**|||
|GET|`/api/v1/collections`|List collections|
|POST|`/api/v1/collections`|Create collection|
|GET|`/api/v1/collections/{id}`|Collection details|
|PATCH|`/api/v1/collections/{id}`|Update collection|
|DELETE|`/api/v1/collections/{id}`|Delete collection|
|POST|`/api/v1/collections/{id}/documents`|Add document|
|DELETE|`/api/v1/collections/{id}/documents/{documentId}`|Remove document|
|**Search**|||
|POST|`/api/v1/search`|Hybrid search|
|POST|`/api/v1/search/semantic`|Dense search|
|POST|`/api/v1/search/keyword`|BM25 search|
|POST|`/api/v1/search/hybrid`|Hybrid + RRF|
|POST|`/api/v1/search/rerank`|Rerank results|
|**Chat / RAG**|||
|POST|`/api/v1/chat`|Generate answer|
|WS|`/ws/chat`|Streaming chat|
|POST|`/api/v1/chat/continue`|Continue conversation|
|POST|`/api/v1/chat/regenerate`|Regenerate answer|
|POST|`/api/v1/chat/feedback`|Rate response|
|**Conversations**|||
|GET|`/api/v1/conversations`|List conversations|
|GET|`/api/v1/conversations/{id}`|Conversation details|
|DELETE|`/api/v1/conversations/{id}`|Delete conversation|
|POST|`/api/v1/conversations/{id}/archive`|Archive conversation|
|**Memory**|||
|GET|`/api/v1/memory`|User memories|
|POST|`/api/v1/memory`|Create memory|
|PATCH|`/api/v1/memory/{id}`|Update memory|
|DELETE|`/api/v1/memory/{id}`|Delete memory|
|POST|`/api/v1/memory/rebuild`|Rebuild semantic memory|
|**Prompts**|||
|GET|`/api/v1/prompts`|List prompt templates|
|POST|`/api/v1/prompts`|Create template|
|GET|`/api/v1/prompts/{id}`|Prompt details|
|PATCH|`/api/v1/prompts/{id}`|Update prompt|
|DELETE|`/api/v1/prompts/{id}`|Delete prompt|
|POST|`/api/v1/prompts/{id}/publish`|Publish version|
|**LLM Providers**|||
|GET|`/api/v1/providers`|Available providers|
|GET|`/api/v1/models`|Available models|
|POST|`/api/v1/providers/test`|Test provider|
|**Jobs**|||
|GET|`/api/v1/jobs`|Background jobs|
|GET|`/api/v1/jobs/{id}`|Job details|
|POST|`/api/v1/jobs/{id}/retry`|Retry job|
|DELETE|`/api/v1/jobs/{id}`|Cancel job|
|**Files**|||
|GET|`/api/v1/files/{id}`|File metadata|
|GET|`/api/v1/files/{id}/download`|Download file|
|DELETE|`/api/v1/files/{id}`|Delete file|
|**Admin**|||
|GET|`/api/v1/admin/dashboard`|Dashboard metrics|
|GET|`/api/v1/admin/health`|System health|
|GET|`/api/v1/admin/metrics`|Platform metrics|
|GET|`/api/v1/admin/logs`|Logs|
|POST|`/api/v1/admin/reindex`|Global reindex|
|POST|`/api/v1/admin/cache/clear`|Clear cache|
|POST|`/api/v1/admin/workers/restart`|Restart workers|
|**Monitoring**|||
|GET|`/health`|Health check|
|GET|`/ready`|Kubernetes readiness|
|GET|`/live`|Kubernetes liveness|
|GET|`/metrics`|Prometheus metrics|

### WebSocket Endpoints

|Endpoint|Purpose|
|---|---|
|`/ws/chat`|Token streaming|
|`/ws/jobs/{jobId}`|Background job progress|
|`/ws/documents/{documentId}`|Document indexing progress|
|`/ws/notifications`|Real-time notifications|
|`/ws/admin/events`|System events (admin only)|

### Standard Response

```json
{
  "success": true,
  "message": "Operation successful",
  "data": {},
  "metadata": {
    "request_id": "...",
    "timestamp": "...",
    "pagination": {}
  }
}
```

### Standard Error

```json
{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "Document not found",
    "details": {}
  },
  "request_id": "..."
}
```

This API surface is sufficient for an enterprise-grade multi-tenant RAG platform and provides a stable contract before implementation.

Below is a production-ready logical database schema. It is normalized for PostgreSQL, multi-tenant aware, and aligned with the architecture we've finalized.

## Core Tables

|Table|Purpose|
|---|---|
|tenants|Organization/workspace|
|users|User profile (mapped to Keycloak)|
|roles|RBAC roles|
|permissions|Permissions|
|user_roles|User ↔ Role mapping|
|role_permissions|Role ↔ Permission mapping|

---

## Knowledge Base

|Table|Purpose|
|---|---|
|collections|Document collections|
|documents|Uploaded document metadata|
|document_versions|Version history|
|document_chunks|Chunk metadata|
|document_embeddings|Vector metadata (Qdrant references only)|
|document_tags|Tags|
|document_tag_map|Document ↔ Tag mapping|

---

## Chat & Memory

|Table|Purpose|
|---|---|
|conversations|Chat sessions|
|messages|User/Assistant messages|
|semantic_memories|Long-term memories|
|citations|Chunk citations used in responses|

---

## Search & Retrieval

|Table|Purpose|
|---|---|
|search_logs|Search analytics|
|retrieval_logs|Retrieved chunks|
|reranker_logs|Reranker scores|

---

## Prompt Management

|Table|Purpose|
|---|---|
|prompt_templates|Prompt definitions|
|prompt_versions|Version history|

---

## AI & Models

|Table|Purpose|
|---|---|
|llm_models|Available models|
|provider_configs|Ollama/OpenRouter configs|

---

## Background Processing

|Table|Purpose|
|---|---|
|jobs|Celery jobs|
|job_logs|Job execution logs|

---

## Observability

|Table|Purpose|
|---|---|
|api_logs|API audit|
|audit_logs|Security audit|
|feedback|User feedback|
|notifications|Notifications|

---

# Main Relationships

```text
Tenant
│
├── Users
│    ├── UserRoles
│    ├── Conversations
│    ├── Documents
│    ├── Collections
│    ├── SemanticMemories
│    └── Feedback
│
├── Collections
│    └── Documents
│          ├── Versions
│          ├── Chunks
│          │      ├── Embeddings
│          │      └── Citations
│          └── Tags
│
└── PromptTemplates
```

---

# Primary Keys

Every table uses

```
id UUID PRIMARY KEY
```

---

# Common Columns

Almost every table contains

|Column|Type|
|---|---|
|id|UUID|
|tenant_id|UUID|
|created_at|TIMESTAMP|
|updated_at|TIMESTAMP|
|created_by|UUID|
|updated_by|UUID|

---

# Documents

```
documents
---------
id
tenant_id
collection_id
filename
storage_path
mime_type
size
checksum
language
status
document_type
version
metadata(JSONB)
created_by
created_at
updated_at
```

---

# Document Chunks

```
document_chunks
---------------
id
tenant_id
document_id
parent_chunk_id
chunk_index
page_number
section_title
content
token_count
metadata(JSONB)
created_at
```

---

# Qdrant Mapping

No vectors are stored in PostgreSQL.

```
document_embeddings
-------------------
id
tenant_id
chunk_id
qdrant_point_id
embedding_model
embedding_version
created_at
```

Actual embeddings remain inside **Qdrant**.

---

# Conversations

```
conversations
-------------
id
tenant_id
user_id
title
model
status
created_at
updated_at
```

---

# Messages

```
messages
--------
id
conversation_id
role
content
token_input
token_output
latency_ms
provider
model
metadata(JSONB)
created_at
```

---

# Semantic Memory

```
semantic_memories
-----------------
id
tenant_id
user_id
memory_type
summary
importance
qdrant_point_id
created_at
```

---

# Jobs

```
jobs
----
id
tenant_id
type
status
progress
payload(JSONB)
result(JSONB)
started_at
completed_at
```

---

# Prompt Templates

```
prompt_templates
----------------
id
tenant_id
name
description
current_version
created_at
```

```
prompt_versions
---------------
id
template_id
version
template
variables(JSONB)
created_at
```

---

# Search Logs

```
search_logs
-----------
id
tenant_id
user_id
query
retrieval_time_ms
rerank_time_ms
llm_time_ms
total_time_ms
created_at
```

---

# Feedback

```
feedback
---------
id
tenant_id
message_id
rating
comment
created_at
```

---

# Audit Logs

```
audit_logs
----------
id
tenant_id
user_id
action
resource
resource_id
ip_address
user_agent
metadata(JSONB)
created_at
```

---

# Recommended PostgreSQL Indexes

|Index|Purpose|
|---|---|
|`tenant_id`|Multi-tenancy isolation|
|`user_id`|User queries|
|`document_id`|Chunk lookup|
|`conversation_id`|Chat history|
|`created_at`|Time-based sorting|
|`status`|Job filtering|
|`GIN(metadata)`|JSONB filtering|
|`(tenant_id, document_id)`|Composite lookup|
|`(tenant_id, user_id)`|User isolation|
|`(tenant_id, created_at)`|Tenant dashboards|

---

# Data Ownership

```text
Tenant
│
├── Users
├── Collections
├── Documents
│     ├── Chunks
│     ├── Embeddings (Qdrant reference)
│     └── Versions
├── Conversations
│     └── Messages
├── Semantic Memories
├── Jobs
├── Prompt Templates
└── Search Logs
```

### Final Schema Summary

- **Database:** PostgreSQL
    
- **Vector Storage:** Qdrant (embeddings only)
    
- **Object Storage:** MinIO
    
- **Cache & Session:** Redis
    
- **Primary Keys:** UUID
    
- **Tenant Isolation:** `tenant_id` on all tenant-owned tables
    
- **Metadata:** JSONB for extensibility
    
- **Auditability:** Created/updated fields and audit logs throughout
    
- **Scalability:** Normalized relational schema with vector references kept outside PostgreSQL, ready for migration from a modular monolith to microservices without major schema changes.

# Event Contracts

We'll use **Domain Events** internally (Celery now, Kafka later). Every event follows the same envelope.

## Standard Event Envelope

```json
{
  "event_id": "uuid",
  "event_type": "DocumentUploaded",
  "version": "v1",
  "tenant_id": "uuid",
  "timestamp": "ISO-8601",
  "source": "document-service",
  "correlation_id": "uuid",
  "user_id": "uuid",
  "payload": {}
}
```

---

## Authentication Events

|Event|Published By|Consumed By|
|---|---|---|
|UserCreated|Auth|Audit|
|UserUpdated|Auth|Audit|
|UserLoggedIn|Auth|Audit|
|UserLoggedOut|Auth|Audit|
|RoleAssigned|Auth|Authorization|

---

## Document Events

|Event|Published By|Consumed By|
|---|---|---|
|DocumentUploaded|Document|Worker|
|DocumentValidated|Worker|Parser|
|DocumentParsed|Parser|Chunker|
|MetadataExtracted|Parser|Indexer|
|DocumentChunked|Chunker|Embedding|
|EmbeddingsGenerated|Embedding|Qdrant|
|DocumentIndexed|Indexer|Search|
|DocumentDeleted|Document|Qdrant, MinIO|
|DocumentReindexed|Document|Search|

---

## Collection Events

|Event|Published By|Consumed By|
|---|---|---|
|CollectionCreated|Collection|Audit|
|CollectionUpdated|Collection|Audit|
|CollectionDeleted|Collection|Cleanup|

---

## Search Events

|Event|Published By|Consumed By|
|---|---|---|
|SearchStarted|Search|Monitoring|
|SearchCompleted|Search|Analytics|
|SearchFailed|Search|Monitoring|
|RerankingCompleted|Search|RAG|

---

## Chat Events

|Event|Published By|Consumed By|
|---|---|---|
|ChatStarted|Chat|Monitoring|
|PromptBuilt|RAG|LLM|
|LLMGenerationStarted|LLM|Monitoring|
|LLMGenerationCompleted|LLM|Memory|
|ResponseStreamCompleted|Chat|Analytics|
|ChatCompleted|Chat|Memory|
|FeedbackSubmitted|Chat|Analytics|

---

## Memory Events

|Event|Published By|Consumed By|
|---|---|---|
|MemoryCreated|Memory|Qdrant|
|MemoryUpdated|Memory|Qdrant|
|MemoryDeleted|Memory|Qdrant|
|MemoryRebuilt|Memory|Monitoring|

---

## Background Job Events

|Event|Published By|Consumed By|
|---|---|---|
|JobQueued|Worker|Monitoring|
|JobStarted|Worker|Monitoring|
|JobProgressUpdated|Worker|WebSocket|
|JobCompleted|Worker|Notification|
|JobFailed|Worker|Notification|
|JobRetried|Worker|Monitoring|

---

## Storage Events

|Event|Published By|Consumed By|
|---|---|---|
|FileUploaded|MinIO|Document|
|FileDeleted|MinIO|Cleanup|
|VectorInserted|Qdrant|Search|
|VectorDeleted|Qdrant|Cleanup|

---

## System Events

|Event|Published By|Consumed By|
|---|---|---|
|CacheInvalidated|Cache|API|
|ConfigUpdated|Admin|All Services|
|ServiceStarted|Service|Monitoring|
|ServiceStopped|Service|Monitoring|
|HealthCheckFailed|Monitoring|Notification|

---

## Notification Events

|Event|Published By|Consumed By|
|---|---|---|
|NotificationCreated|Notification|WebSocket|
|NotificationRead|User|Notification|

---

## Event Flow

```text
DocumentUploaded
        │
        ▼
DocumentValidated
        │
        ▼
DocumentParsed
        │
        ▼
MetadataExtracted
        │
        ▼
DocumentChunked
        │
        ▼
EmbeddingsGenerated
        │
        ▼
DocumentIndexed
        │
        ▼
SearchAvailable
```

```text
ChatStarted
      │
      ▼
PromptBuilt
      │
      ▼
SearchCompleted
      │
      ▼
LLMGenerationStarted
      │
      ▼
LLMGenerationCompleted
      │
      ▼
ChatCompleted
      │
      ▼
MemoryCreated
```

## Event Naming Convention

- Use **Past Tense**.
    
- Format: `<Entity><PastVerb>`
    

Examples:

- `DocumentUploaded`
    
- `DocumentIndexed`
    
- `ChatCompleted`
    
- `MemoryCreated`
    
- `JobFailed`
    

Avoid command-style names like:

- ❌ `UploadDocument`
    
- ❌ `GenerateEmbedding`
    
- ❌ `StartChat`
    

---

## Transport Strategy

|Phase|Transport|
|---|---|
|Development|Celery + Redis|
|Production (Modular Monolith)|Celery + Redis|
|Microservices|Apache Kafka|
|Critical Workflows (Future)|Temporal|

This event contract provides a stable event-driven foundation that can evolve from the current modular monolith to a Kafka-based microservices architecture without changing the event payloads.


For a project of this scale, I would organize it as a **Modular Monolith** from day one. Each module should own its API, business logic, models, repositories, and services. This makes extracting a module into a microservice later straightforward.

```text
enterprise-rag/
│
├── apps/
│   ├── api/                        # FastAPI Entry Point
│   │   ├── main.py
│   │   ├── lifespan.py
│   │   ├── dependencies.py
│   │   ├── middleware/
│   │   ├── routers/
│   │   └── websocket/
│   │
│   └── worker/                     # Celery Entry Point
│       ├── celery_app.py
│       └── tasks.py
│
├── modules/
│   ├── auth/
│   ├── tenant/
│   ├── user/
│   ├── collection/
│   ├── document/
│   ├── search/
│   ├── rag/
│   ├── llm/
│   ├── memory/
│   ├── conversation/
│   ├── prompt/
│   ├── notification/
│   ├── job/
│   ├── analytics/
│   └── admin/
│
├── infrastructure/
│   ├── database/
│   ├── redis/
│   ├── qdrant/
│   ├── minio/
│   ├── keycloak/
│   ├── ollama/
│   ├── openrouter/
│   ├── celery/
│   ├── grpc/
│   └── events/
│
├── shared/
│   ├── config/
│   ├── constants/
│   ├── exceptions/
│   ├── logging/
│   ├── security/
│   ├── schemas/
│   ├── utils/
│   └── types/
│
├── proto/                          # gRPC Protobuf Files
│
├── scripts/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── api/
│   ├── e2e/
│   └── performance/
│
├── deployments/
│   ├── docker/
│   ├── compose/
│   ├── kubernetes/
│   └── terraform/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── api/
│   ├── diagrams/
│   └── runbooks/
│
├── .github/
│
├── pyproject.toml
├── uv.lock
├── .env.example
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## Module Structure (Every Module)

Every module follows the same internal layout.

```text
modules/document/
│
├── api/
│   ├── router.py
│   ├── requests.py
│   └── responses.py
│
├── domain/
│   ├── entities.py
│   ├── value_objects.py
│   ├── events.py
│   └── interfaces.py
│
├── application/
│   ├── commands.py
│   ├── queries.py
│   ├── handlers.py
│   └── services.py
│
├── infrastructure/
│   ├── repository.py
│   ├── storage.py
│   ├── parser.py
│   ├── chunker.py
│   ├── embedding.py
│   └── qdrant.py
│
├── models.py
├── schemas.py
├── enums.py
└── exceptions.py
```

---

## Infrastructure Layout

```text
infrastructure/
│
├── database/
│   ├── session.py
│   ├── base.py
│   ├── models/
│   └── migrations/
│
├── redis/
│
├── qdrant/
│
├── minio/
│
├── keycloak/
│
├── grpc/
│   ├── generated/
│   └── services/
│
├── celery/
│
└── events/
```

---

## Documentation Layout

```text
docs/
│
├── architecture/
│   ├── c4-level1.md
│   ├── c4-level2.md
│   ├── c4-level3.md
│   └── c4-level4.md
│
├── adr/
│   ├── 0001-use-qdrant.md
│   ├── 0002-use-keycloak.md
│   └── ...
│
├── api/
│
├── diagrams/
│
└── runbooks/
```

---

## Testing Layout

```text
tests/
│
├── unit/
├── integration/
├── api/
├── e2e/
├── performance/
└── fixtures/
```

---

## Deployment Layout

```text
deployments/
│
├── docker/
├── compose/
├── kubernetes/
└── terraform/
```

---

## Design Principles

|Principle|Choice|
|---|---|
|Architecture|Modular Monolith|
|Pattern|DDD + Clean Architecture|
|Module Isolation|High|
|Dependency Direction|API → Application → Domain → Infrastructure|
|Shared Code|`shared/` only|
|External Integrations|`infrastructure/`|
|Future Migration|Module → Microservice with minimal changes|

This structure is maintainable for a single developer, supports growth to a multi-developer team, and allows individual modules (e.g., `rag`, `search`, or `document`) to be extracted into independent microservices later with minimal refactoring.


Correct. That folder structure is **backend only**.

Since we're building an enterprise platform, I recommend a **monorepo**.

```text
enterprise-rag/
│
├── apps/
│   ├── web/                 # Next.js Frontend
│   ├── api/                 # FastAPI Backend
│   └── worker/              # Celery Worker
│
├── packages/
│   ├── ui/                  # Shared UI components
│   ├── types/               # Shared TypeScript types
│   ├── api-client/          # OpenAPI generated client
│   ├── config/              # Shared configs
│   └── eslint-config/
│
├── modules/                 # Backend modules
│
├── infrastructure/
│
├── proto/
│
├── deployments/
│
├── docs/
│
├── tests/
│
├── docker-compose.yml
├── pnpm-workspace.yaml
├── pyproject.toml
├── turbo.json
└── README.md
```

---

## Frontend (`apps/web`)

```text
apps/web/
│
├── app/                     # App Router
│   ├── (auth)/
│   ├── (dashboard)/
│   ├── api/
│   ├── layout.tsx
│   └── page.tsx
│
├── components/
│   ├── ui/
│   ├── chat/
│   ├── documents/
│   ├── search/
│   ├── dashboard/
│   ├── settings/
│   └── common/
│
├── features/
│   ├── auth/
│   ├── chat/
│   ├── documents/
│   ├── search/
│   ├── collections/
│   ├── memory/
│   ├── admin/
│   └── settings/
│
├── hooks/
│
├── lib/
│   ├── api/
│   ├── auth/
│   ├── websocket/
│   └── utils/
│
├── providers/
│
├── stores/                  # Zustand
│
├── styles/
│
├── types/
│
├── middleware.ts
└── next.config.ts
```

---

## Shared Packages

```text
packages/
│
├── ui/
│   ├── button/
│   ├── modal/
│   ├── table/
│   ├── markdown/
│   └── index.ts
│
├── api-client/
│   ├── generated/
│   └── client.ts
│
├── types/
│
└── config/
```

---

## Final Repository

```text
enterprise-rag/
│
├── apps/
│   ├── web/
│   ├── api/
│   └── worker/
│
├── packages/
│
├── modules/
│
├── infrastructure/
│
├── proto/
│
├── deployments/
│
├── docs/
│
├── tests/
│
└── configs...
```

### Tech Stack

|Layer|Technology|
|---|---|
|Frontend|Next.js 15 + TypeScript + Tailwind CSS + shadcn/ui|
|State|Zustand + TanStack Query|
|Backend|FastAPI|
|Workers|Celery|
|Package Manager|pnpm (frontend), uv (backend)|
|Monorepo|Turborepo|
|API Client|OpenAPI-generated TypeScript client|

This is the structure I'd use for an enterprise-grade project. It keeps the frontend and backend in a single repository while allowing them to evolve independently and share types, UI components, and generated clients where appropriate.

At this point, you've completed almost all of the architecture and design work. The remaining phases are implementation and operations.

|Phase|Deliverable|Status|
|---|---|---|
|Requirements|Functional & Non-functional Requirements|✅|
|Technology Stack|Complete stack selection|✅|
|Architecture|High-Level Architecture|✅|
|C4 Model|Level 1–4|✅|
|Database Design|Schema & Relationships|✅|
|API Design|REST Contracts|✅|
|Event Design|Event Contracts|✅|
|Folder Structure|Monorepo Structure|✅|
|**gRPC Design**|`.proto` Contracts|⏳|
|**OpenAPI Design**|API Specification|⏳|
|**Sequence Diagrams**|Upload, Chat, Search, Login|⏳|
|**Deployment Architecture**|Docker, Kubernetes, Networking|⏳|
|**Security Design**|Encryption, RBAC, ABAC, Threat Model|⏳|
|**Configuration Design**|Environment Variables & Settings|⏳|
|**Observability Design**|Logs, Metrics, Traces|⏳|
|**CI/CD Pipeline**|GitHub Actions Workflow|⏳|
|**Testing Strategy**|Unit, Integration, E2E, Load|⏳|
|**Coding Standards**|Linting, Formatting, Git Workflow|⏳|
|**Implementation Roadmap**|Feature-by-feature Build Plan|⏳|
|**Repository Initialization**|Create project & dependencies|⏳|
|**Implementation**|Develop modules|⏳|
|**Documentation**|README, ADRs, API Docs|⏳|
|**Production Deployment**|VPS/Kubernetes|⏳|

---

## Recommended Implementation Order

### Phase 1 — Foundation

- Repository initialization
    
- Turborepo
    
- uv + pnpm
    
- Docker Compose
    
- Environment configuration
    
- Logging
    
- Configuration management
    

### Phase 2 — Infrastructure

- PostgreSQL
    
- Alembic
    
- Redis
    
- MinIO
    
- Qdrant
    
- Keycloak
    
- Celery
    

### Phase 3 — Core Backend

- Authentication
    
- Tenant Management
    
- Users & Roles
    
- Collections
    
- Document Upload
    
- Parser Pipeline
    
- Chunking
    
- Embeddings
    
- Indexing
    

### Phase 4 — AI/RAG

- Hybrid Search
    
- Query Rewriting
    
- Reranker
    
- Prompt Management
    
- LLM Router
    
- Streaming Responses
    
- Citations
    

### Phase 5 — Memory

- Conversations
    
- Chat History
    
- Semantic Memory
    
- Memory Retrieval
    

### Phase 6 — Frontend

- Authentication
    
- Dashboard
    
- Document Management
    
- Collections
    
- Chat UI
    
- Search
    
- Admin Panel
    
- Settings
    

### Phase 7 — Production

- Observability
    
- Evaluation (RAGAS + DeepEval)
    
- Rate Limiting
    
- Caching
    
- CI/CD
    
- Docker
    
- Kubernetes
    
- Terraform
    
- Security Hardening
    

---

## Remaining Design Documents

These are useful but can be created alongside development rather than before it:

- gRPC `.proto` contracts
    
- OpenAPI specification
    
- Sequence diagrams
    
- Deployment diagram
    
- Security architecture
    
- Monitoring architecture
    
- CI/CD workflow
    
- ADRs (Architecture Decision Records)
    

---

### What I recommend next

**Stop designing.**

The architecture is now sufficiently complete. Additional design work will have diminishing returns.

Start building with this order:

1. Initialize the monorepo.
    
2. Set up the infrastructure (Docker Compose, PostgreSQL, Redis, MinIO, Qdrant, Keycloak).
    
3. Implement authentication.
    
4. Build the document ingestion pipeline.
    
5. Implement hybrid retrieval.
    
6. Add the chat/RAG pipeline.
    
7. Build the frontend alongside the backend.
    
8. Finish with observability, evaluation, CI/CD, and Kubernetes.
    

This follows the same progression used in many production systems: establish a solid foundation, deliver core functionality, then add operational and scalability features.


You've reached the point where most people make a mistake: they immediately start implementing features (authentication, uploads, chat, etc.) without first designing the system. Since your goal is to build an **enterprise-grade RAG platform**, the next phase should be **Architecture & Infrastructure**, followed by **Core Platform**, and only then **Business Features**.

I would structure the remaining work like this.

# Phase 2 — Architecture & Infrastructure (Current Phase)

Before writing more code, establish the technical foundation.

## 2.1 Define the Architecture

Create an `ARCHITECTURE.md` documenting:

- High-level system architecture
    
- Request flow
    
- Document ingestion flow
    
- Query flow
    
- Background job flow
    
- Component interaction
    
- Database relationships
    
- Security boundaries
    

Also create diagrams (Mermaid is sufficient initially):

- Overall system
    
- Sequence diagram for document upload
    
- Sequence diagram for query execution
    
- Deployment diagram
    

Deliverable:

```
docs/
    architecture.md
    diagrams.md
```

---

## 2.2 Shared Packages

Your monorepo currently has an empty `packages/` directory. This should become the shared foundation.

```
packages/
    config/
    logger/
    types/
    auth/
    clients/
```

Examples:

`config`

- Environment loading
    
- Settings
    
- Secrets
    

`logger`

- Structured logging
    
- Correlation IDs
    

`types`

- Shared DTOs
    
- Enums
    
- Constants
    

`clients`

- Qdrant client
    
- Redis client
    
- MinIO client
    
- PostgreSQL client
    

---

## 2.3 Configuration System

Instead of scattered `.env` usage, create:

```
apps/api/src/api/core/config.py

apps/worker/src/worker/core/config.py
```

using Pydantic Settings.

Support:

- dev
    
- test
    
- staging
    
- production
    

---

## 2.4 Logging

Before writing APIs:

Implement structured logging.

Prefer

- Structlog
    

or

- Loguru
    

Features:

- JSON logs
    
- request_id
    
- user_id
    
- trace_id
    

---

## 2.5 Error Handling

Global exception middleware.

Custom exceptions:

```
ValidationException

NotFoundException

UnauthorizedException

VectorStoreException

StorageException
```

Consistent error response:

```json
{
  "success": false,
  "error": {
    "code": "...",
    "message": "...",
    "details": {}
  }
}
```

---

# Phase 3 — Infrastructure

Only after the architecture is defined.

Bring up:

```
PostgreSQL

Redis

Qdrant

MinIO
```

Then integrate them one by one.

---

## PostgreSQL

First create the database schema.

Entities:

```
users

organizations

documents

chunks

conversations

messages

jobs

api_keys
```

Design this before writing SQLAlchemy models.

---

## Redis

Use it for

- caching
    
- session storage
    
- background queues
    
- rate limiting
    

---

## MinIO

Object storage only.

Never store PDFs inside PostgreSQL.

---

## Qdrant

Collections

```
documents

chunks
```

Metadata:

```
document_id

user_id

organization_id

filename

chunk_index

page

tags

created_at
```

---

# Phase 4 — Authentication

Don't just build login.

Design the identity model.

```
User

Role

Permission

Organization
```

Authentication:

- JWT
    
- Refresh token
    
- RBAC
    

---

# Phase 5 — Document Pipeline

This is the heart of the platform.

Pipeline:

```
Upload

↓

Virus Scan

↓

Store in MinIO

↓

Extract Text

↓

Clean

↓

Chunk

↓

Metadata Extraction

↓

Embedding

↓

Store in Qdrant

↓

Update PostgreSQL
```

Worker performs all heavy processing.

---

# Phase 6 — Retrieval

Implement retrieval as a service.

```
Retriever

↓

Metadata Filter

↓

Similarity Search

↓

Re-ranking

↓

Context Builder
```

---

# Phase 7 — LLM Layer

Create an abstraction instead of calling providers directly.

```
LLMProvider

OpenAIProvider

AnthropicProvider

OllamaProvider

AzureOpenAIProvider
```

Then

```
PromptBuilder

ConversationManager

CitationFormatter
```

---

# Phase 8 — API

Suggested endpoints:

```
POST /auth/login

POST /documents

GET /documents

DELETE /documents/{id}

POST /chat

GET /jobs/{id}

GET /health

GET /metrics
```

---

# Phase 9 — Frontend

Pages:

```
Login

Dashboard

Documents

Upload

Search

Chat

Settings

Admin
```

---

# Phase 10 — Worker

Responsibilities:

- embedding
    
- OCR
    
- parsing
    
- indexing
    
- cleanup
    
- scheduled jobs
    

---

# Phase 11 — Observability

Implement:

- Prometheus metrics
    
- OpenTelemetry traces
    
- Structured logs
    
- Health checks
    
- Readiness checks
    
- Liveness checks
    

---

# Phase 12 — CI/CD

GitHub Actions:

```
Lint

Type Check

Tests

Docker Build

Security Scan

Coverage

Deploy
```

---

# Phase 13 — Production

Deploy using:

- Docker Compose (development)
    
- Kubernetes (production)
    

Add:

- Nginx
    
- HTTPS
    
- Secrets management
    
- Horizontal scaling
    
- Backups
    

---

## Recommended Immediate Milestone

I recommend **not** starting with authentication or document upload yet.

The next milestone should be:

1. Finalize the architecture documentation (diagrams, data flow, API boundaries).
    
2. Design the PostgreSQL schema and ER diagram.
    
3. Define the shared packages (`config`, `logger`, `clients`, `types`).
    
4. Integrate PostgreSQL, Redis, MinIO, and Qdrant through Docker Compose.
    
5. Verify connectivity from both the API and worker.
    

Only after those foundations are in place should you begin implementing the document ingestion and RAG pipeline. This approach minimizes rework and results in a codebase that scales cleanly as features are added.


Agreed. This is the right point to pause feature development and design the system. In production teams, architecture is typically settled before implementing core business logic because it reduces rework and establishes consistent patterns.

I propose we treat this as **Phase 2: Architecture & System Design**. By the end of this phase, we should be able to hand the documentation to another engineer and they could implement the platform without guessing.

## Deliverables

We'll create these documents in `docs/`:

```text
docs/
├── architecture.md
├── system-overview.md
├── request-flow.md
├── data-model.md
├── api-design.md
├── deployment.md
├── decisions/
│   ├── adr-001-monorepo.md
│   ├── adr-002-fastapi.md
│   ├── adr-003-qdrant.md
│   └── ...
└── diagrams/
    ├── system.mmd
    ├── upload-flow.mmd
    ├── query-flow.mmd
    ├── auth-flow.mmd
    ├── deployment.mmd
    └── er-diagram.mmd
```

We'll also maintain Architecture Decision Records (ADRs). These explain _why_ a technology or pattern was chosen, which becomes invaluable as the project grows.

## Step 1: System Overview

We'll define:

- Vision and goals
    
- High-level architecture
    
- Major components
    
- Technology choices
    
- System boundaries
    
- External dependencies
    
- Scalability goals
    
- Security principles
    

## Step 2: High-Level Architecture

We'll define every service and its responsibility.

```text
                        ┌─────────────────────────┐
                        │       Next.js Web       │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                           ┌────────────────────┐
                           │    FastAPI API     │
                           └───────┬────────────┘
                                   │
         ┌──────────────┬──────────┼──────────────┬─────────────┐
         ▼              ▼          ▼              ▼             ▼
   PostgreSQL        Redis      MinIO         Qdrant        Worker
                                                 ▲             │
                                                 │             ▼
                                          Embeddings      Document Processing
```

This diagram will later become a Mermaid diagram in the repository.

## Step 3: Request Flows

We'll document each major workflow separately.

- User authentication
    
- Document upload
    
- Document indexing
    
- Query execution
    
- Background processing
    
- Chat conversation
    
- Admin operations
    

Each workflow will include:

- Sequence diagram
    
- Component interactions
    
- Database operations
    
- Failure scenarios
    
- Retry strategy
    

## Step 4: API Boundaries

Instead of immediately writing endpoints, we'll define the API surface.

For example:

```text
/auth
/users
/documents
/chunks
/search
/chat
/jobs
/admin
/health
/metrics
```

Each endpoint will later have:

- Request schema
    
- Response schema
    
- Error responses
    
- Authentication requirements
    
- Rate limiting
    
- Versioning
    

## Step 5: Data Flow

We'll define how data moves through the system.

For example, document ingestion:

```text
User Upload
      │
      ▼
FastAPI
      │
      ▼
MinIO
      │
      ▼
Background Job
      │
      ▼
Text Extraction
      │
      ▼
Cleaning
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Qdrant
      │
      ▼
PostgreSQL Metadata
```

And query execution:

```text
Question
     │
     ▼
Embedding
     │
     ▼
Vector Search
     │
     ▼
Re-ranking
     │
     ▼
Prompt Builder
     │
     ▼
LLM
     │
     ▼
Response + Citations
```

## Step 6: Database Design

Before writing SQLAlchemy models, we'll produce:

- ER diagram
    
- Tables
    
- Relationships
    
- Indexing strategy
    
- Constraints
    
- Soft deletion policy
    
- Audit fields
    
- Multi-tenancy considerations
    

## Step 7: Deployment Architecture

We'll document:

- Local development (Docker Compose)
    
- Production deployment
    
- Environment variables
    
- Secrets management
    
- Networking
    
- Persistent volumes
    
- Reverse proxy
    
- Health checks
    

## Step 8: Architecture Decision Records (ADRs)

We'll capture decisions such as:

- Why FastAPI instead of Django
    
- Why Qdrant instead of pgvector
    
- Why MinIO instead of storing files in PostgreSQL
    
- Why Redis for caching and queues
    
- Why a monorepo
    
- Why `pnpm` and `uv`
    

Each ADR will record:

- Context
    
- Decision
    
- Consequences
    
- Alternatives considered
    

## Development Sequence

After the documentation phase, implementation will proceed in this order:

1. Shared infrastructure (`config`, `logger`, `clients`, `types`)
    
2. PostgreSQL schema and migrations
    
3. Docker service integration
    
4. Authentication
    
5. Document ingestion
    
6. Embedding pipeline
    
7. Retrieval
    
8. LLM orchestration
    
9. Frontend
    
10. Observability
    
11. CI/CD
    
12. Production deployment
    

This sequence ensures that each new layer builds on a stable foundation rather than requiring redesign later.



following is the folder structure for the same project:

```Powershell
PS D:\Programming\enterprise-rag> $exclude = @('.venv','venv','node_modules','.git','__pycache__','dist','build','coverage')
>> $root = (Get-Location).Path
>> 
>> Get-ChildItem -Recurse -Force |
>> Where-Object {
>>     $parts = $_.FullName.Substring($root.Length).Split('\')
>>     -not ($parts | Where-Object { $_ -in $exclude })
>> } |
>> ForEach-Object {
>>     $_.FullName.Substring($root.Length + 1)
>> }
```

```Powershell
.github
.husky
.turbo
.vscode
apps
deployments
docs
infrastructure
modules
packages
proto
tests
.editorconfig
.gitattributes
.gitignore
.npmrc
.prettierignore
.prettierrc
commitlint.config.mjs
package.json
pnpm-lock.yaml
pnpm-workspace.yaml
README.md
turbo.json
.github\workflows
.github\workflows\ci.yml
.husky\_
.husky\pre-commit
.husky\_\.gitignore
.husky\_\applypatch-msg
.husky\_\commit-msg
.husky\_\h
.husky\_\husky.sh
.husky\_\post-applypatch
.husky\_\post-checkout
.husky\_\post-commit
.husky\_\post-merge
.husky\_\post-rewrite
.husky\_\pre-applypatch
.husky\_\pre-auto-gc
.husky\_\pre-commit
.husky\_\pre-merge-commit
.husky\_\pre-push
.husky\_\pre-rebase
.husky\_\prepare-commit-msg
.turbo\cache
.turbo\cache\0b9b03fa9c291454-manifest.json
.turbo\cache\0b9b03fa9c291454-meta.json
.turbo\cache\0b9b03fa9c291454.tar.zst
.turbo\cache\0c642ae914acfe0f-manifest.json
.turbo\cache\0c642ae914acfe0f-meta.json
.turbo\cache\0c642ae914acfe0f.tar.zst
.turbo\cache\361126dfa3e9aefe-manifest.json
.turbo\cache\361126dfa3e9aefe-meta.json
.turbo\cache\361126dfa3e9aefe.tar.zst
.turbo\cache\4499c47da64959d5-manifest.json
.turbo\cache\4499c47da64959d5-meta.json
.turbo\cache\4499c47da64959d5.tar.zst
.turbo\cache\4e8a91aeba584658-manifest.json
.turbo\cache\4e8a91aeba584658-meta.json
.turbo\cache\4e8a91aeba584658.tar.zst
.turbo\cache\53e8fb973c44097a-manifest.json
.turbo\cache\53e8fb973c44097a-meta.json
.turbo\cache\53e8fb973c44097a.tar.zst
.turbo\cache\6915afe317a58553-manifest.json
.turbo\cache\6915afe317a58553-meta.json
.turbo\cache\6915afe317a58553.tar.zst
.turbo\cache\8166618178e2f5c2-manifest.json
.turbo\cache\8166618178e2f5c2-meta.json
.turbo\cache\8166618178e2f5c2.tar.zst
.turbo\cache\870c2602ef8b7edf-manifest.json
.turbo\cache\870c2602ef8b7edf-meta.json
.turbo\cache\870c2602ef8b7edf.tar.zst
.turbo\cache\92668e9858c27143-manifest.json
.turbo\cache\92668e9858c27143-meta.json
.turbo\cache\92668e9858c27143.tar.zst
.turbo\cache\9a4e4bbfad8cd879-manifest.json
.turbo\cache\9a4e4bbfad8cd879-meta.json
.turbo\cache\9a4e4bbfad8cd879.tar.zst
.turbo\cache\9c3d7a0215970bab-manifest.json
.turbo\cache\9c3d7a0215970bab-meta.json
.turbo\cache\9c3d7a0215970bab.tar.zst
.turbo\cache\a09b079b341636d2-manifest.json
.turbo\cache\a09b079b341636d2-meta.json
.turbo\cache\a09b079b341636d2.tar.zst
.turbo\cache\ae2a85afa6422a72-manifest.json
.turbo\cache\ae2a85afa6422a72-meta.json
.turbo\cache\ae2a85afa6422a72.tar.zst
.turbo\cache\d147728bf1ca1fce-manifest.json
.turbo\cache\d147728bf1ca1fce-meta.json
.turbo\cache\d147728bf1ca1fce.tar.zst
.turbo\cache\d1ac6d832ef6c265-manifest.json
.turbo\cache\d1ac6d832ef6c265-meta.json
.turbo\cache\d1ac6d832ef6c265.tar.zst
.turbo\cache\d2f28923dee08e54-manifest.json
.turbo\cache\d2f28923dee08e54-meta.json
.turbo\cache\d2f28923dee08e54.tar.zst
.turbo\cache\d4c20f48453043be-manifest.json
.turbo\cache\d4c20f48453043be-meta.json
.turbo\cache\d4c20f48453043be.tar.zst
.turbo\cache\db86d649a536c363-manifest.json
.turbo\cache\db86d649a536c363-meta.json
.turbo\cache\db86d649a536c363.tar.zst
.turbo\cache\f02e56d1dd20ea65-manifest.json
.turbo\cache\f02e56d1dd20ea65-meta.json
.turbo\cache\f02e56d1dd20ea65.tar.zst
.turbo\cache\f78399e0df17848c-manifest.json
.turbo\cache\f78399e0df17848c-meta.json
.turbo\cache\f78399e0df17848c.tar.zst
.vscode\extensions.json
.vscode\settings.json
apps\api
apps\web
apps\worker
apps\api\.mypy_cache
apps\api\.pytest_cache
apps\api\.ruff_cache
apps\api\.turbo
apps\api\src
apps\api\tests
apps\api\.dockerignore
apps\api\.python-version
apps\api\Dockerfile
apps\api\mypy.ini
apps\api\package.json
apps\api\pyproject.toml
apps\api\README.md
apps\api\ruff.toml
apps\api\uv.lock
apps\api\.mypy_cache\3.11
apps\api\.mypy_cache\.gitignore
apps\api\.mypy_cache\CACHEDIR.TAG
apps\api\.mypy_cache\3.11\cache.0.db
apps\api\.mypy_cache\3.11\cache.1.db
apps\api\.mypy_cache\3.11\cache.10.db
apps\api\.mypy_cache\3.11\cache.11.db
apps\api\.mypy_cache\3.11\cache.12.db
apps\api\.mypy_cache\3.11\cache.13.db
apps\api\.mypy_cache\3.11\cache.14.db
apps\api\.mypy_cache\3.11\cache.15.db
apps\api\.mypy_cache\3.11\cache.2.db
apps\api\.mypy_cache\3.11\cache.3.db
apps\api\.mypy_cache\3.11\cache.4.db
apps\api\.mypy_cache\3.11\cache.5.db
apps\api\.mypy_cache\3.11\cache.6.db
apps\api\.mypy_cache\3.11\cache.7.db
apps\api\.mypy_cache\3.11\cache.8.db
apps\api\.mypy_cache\3.11\cache.9.db
apps\api\.pytest_cache\v
apps\api\.pytest_cache\.gitignore
apps\api\.pytest_cache\CACHEDIR.TAG
apps\api\.pytest_cache\README.md
apps\api\.pytest_cache\v\cache
apps\api\.pytest_cache\v\cache\lastfailed
apps\api\.pytest_cache\v\cache\nodeids
apps\api\.ruff_cache\0.15.22
apps\api\.ruff_cache\.gitignore
apps\api\.ruff_cache\CACHEDIR.TAG
apps\api\.ruff_cache\0.15.22\15333289667307268101
apps\api\.ruff_cache\0.15.22\18282209793981061950
apps\api\.turbo\turbo-lint.log
apps\api\.turbo\turbo-test.log
apps\api\src\api
apps\api\src\api\core
apps\api\src\api\dependencies
apps\api\src\api\middlewares
apps\api\src\api\models
apps\api\src\api\routers
apps\api\src\api\schemas
apps\api\src\api\services
apps\api\src\api\config.py
apps\api\src\api\main.py
apps\api\src\api\__init__.py
apps\api\src\api\core\config.py
apps\api\tests\test_health.py
apps\web\.next
apps\web\.turbo
apps\web\app
apps\web\public
apps\web\.dockerignore
apps\web\.gitignore
apps\web\AGENTS.md
apps\web\CLAUDE.md
apps\web\Dockerfile
apps\web\eslint.config.mjs
apps\web\next-env.d.ts
apps\web\next.config.ts
apps\web\package.json
apps\web\pnpm-lock.yaml
apps\web\pnpm-workspace.yaml
apps\web\postcss.config.mjs
apps\web\README.md
apps\web\tsconfig.json
apps\web\.next\cache
apps\web\.next\diagnostics
apps\web\.next\server
apps\web\.next\static
apps\web\.next\types
apps\web\.next\app-path-routes-manifest.json
apps\web\.next\build-manifest.json
apps\web\.next\BUILD_ID
apps\web\.next\export-marker.json
apps\web\.next\fallback-build-manifest.json
apps\web\.next\images-manifest.json
apps\web\.next\next-minimal-server.js.nft.json
apps\web\.next\next-server.js.nft.json
apps\web\.next\package.json
apps\web\.next\prerender-manifest.json
apps\web\.next\required-server-files.js
apps\web\.next\required-server-files.json
apps\web\.next\routes-manifest.json
apps\web\.next\trace
apps\web\.next\trace-build
apps\web\.next\turbopack
apps\web\.next\cache\.previewinfo
apps\web\.next\cache\.rscinfo
apps\web\.next\cache\.tsbuildinfo
apps\web\.next\diagnostics\build-diagnostics.json
apps\web\.next\diagnostics\framework.json
apps\web\.next\diagnostics\route-bundle-stats.json
apps\web\.next\server\app
apps\web\.next\server\chunks
apps\web\.next\server\pages
apps\web\.next\server\app-paths-manifest.json
apps\web\.next\server\functions-config-manifest.json
apps\web\.next\server\interception-route-rewrite-manifest.js
apps\web\.next\server\middleware-build-manifest.js
apps\web\.next\server\middleware-manifest.json
apps\web\.next\server\next-font-manifest.js
apps\web\.next\server\next-font-manifest.json
apps\web\.next\server\pages-manifest.json
apps\web\.next\server\prefetch-hints.json
apps\web\.next\server\server-reference-manifest.js
apps\web\.next\server\server-reference-manifest.json
apps\web\.next\server\app\favicon.ico
apps\web\.next\server\app\index.segments
apps\web\.next\server\app\page
apps\web\.next\server\app\_global-error
apps\web\.next\server\app\_global-error.segments
apps\web\.next\server\app\_not-found
apps\web\.next\server\app\_not-found.segments
apps\web\.next\server\app\favicon.ico.body
apps\web\.next\server\app\favicon.ico.meta
apps\web\.next\server\app\index.html
apps\web\.next\server\app\index.meta
apps\web\.next\server\app\index.rsc
apps\web\.next\server\app\page.js
apps\web\.next\server\app\page.js.map
apps\web\.next\server\app\page.js.nft.json
apps\web\.next\server\app\page_client-reference-manifest.js
apps\web\.next\server\app\_global-error.html
apps\web\.next\server\app\_global-error.meta
apps\web\.next\server\app\_global-error.rsc
apps\web\.next\server\app\_not-found.html
apps\web\.next\server\app\_not-found.meta
apps\web\.next\server\app\_not-found.rsc
apps\web\.next\server\app\favicon.ico\route
apps\web\.next\server\app\favicon.ico\route.js
apps\web\.next\server\app\favicon.ico\route.js.map
apps\web\.next\server\app\favicon.ico\route.js.nft.json
apps\web\.next\server\app\favicon.ico\route\app-paths-manifest.json
apps\web\.next\server\app\favicon.ico\route\build-manifest.json
apps\web\.next\server\app\index.segments\_full.segment.rsc
apps\web\.next\server\app\index.segments\_head.segment.rsc
apps\web\.next\server\app\index.segments\_index.segment.rsc
apps\web\.next\server\app\index.segments\_tree.segment.rsc
apps\web\.next\server\app\index.segments\__PAGE__.segment.rsc
apps\web\.next\server\app\page\app-paths-manifest.json
apps\web\.next\server\app\page\build-manifest.json
apps\web\.next\server\app\page\next-font-manifest.json
apps\web\.next\server\app\page\react-loadable-manifest.json
apps\web\.next\server\app\page\server-reference-manifest.json
apps\web\.next\server\app\_global-error\page
apps\web\.next\server\app\_global-error\page.js
apps\web\.next\server\app\_global-error\page.js.map
apps\web\.next\server\app\_global-error\page.js.nft.json
apps\web\.next\server\app\_global-error\page_client-reference-manifest.js
apps\web\.next\server\app\_global-error\page\app-paths-manifest.json
apps\web\.next\server\app\_global-error\page\build-manifest.json
apps\web\.next\server\app\_global-error\page\next-font-manifest.json
apps\web\.next\server\app\_global-error\page\react-loadable-manifest.json
apps\web\.next\server\app\_global-error\page\server-reference-manifest.json
apps\web\.next\server\app\_global-error.segments\_full.segment.rsc
apps\web\.next\server\app\_global-error.segments\_head.segment.rsc
apps\web\.next\server\app\_global-error.segments\_index.segment.rsc
apps\web\.next\server\app\_global-error.segments\_tree.segment.rsc
apps\web\.next\server\app\_global-error.segments\__PAGE__.segment.rsc
apps\web\.next\server\app\_not-found\page
apps\web\.next\server\app\_not-found\page.js
apps\web\.next\server\app\_not-found\page.js.map
apps\web\.next\server\app\_not-found\page.js.nft.json
apps\web\.next\server\app\_not-found\page_client-reference-manifest.js
apps\web\.next\server\app\_not-found\page\app-paths-manifest.json
apps\web\.next\server\app\_not-found\page\build-manifest.json
apps\web\.next\server\app\_not-found\page\next-font-manifest.json
apps\web\.next\server\app\_not-found\page\react-loadable-manifest.json
apps\web\.next\server\app\_not-found\page\server-reference-manifest.json
apps\web\.next\server\app\_not-found.segments\_not-found
apps\web\.next\server\app\_not-found.segments\_full.segment.rsc
apps\web\.next\server\app\_not-found.segments\_head.segment.rsc
apps\web\.next\server\app\_not-found.segments\_index.segment.rsc
apps\web\.next\server\app\_not-found.segments\_not-found.segment.rsc
apps\web\.next\server\app\_not-found.segments\_tree.segment.rsc
apps\web\.next\server\app\_not-found.segments\_not-found\__PAGE__.segment.rsc
apps\web\.next\server\chunks\ssr
apps\web\.next\server\chunks\apps_web__next-internal_server_app_favicon_ico_route_actions_0u51f7q.js
apps\web\.next\server\chunks\apps_web__next-internal_server_app_favicon_ico_route_actions_0u51f7q.js.map
apps\web\.next\server\chunks\[externals]_next_dist_0iuj5m_._.js
apps\web\.next\server\chunks\[externals]_next_dist_0iuj5m_._.js.map
apps\web\.next\server\chunks\[root-of-the-server]__0_kzvqo._.js
apps\web\.next\server\chunks\[root-of-the-server]__0_kzvqo._.js.map
apps\web\.next\server\chunks\[turbopack]_runtime.js
apps\web\.next\server\chunks\[turbopack]_runtime.js.map
apps\web\.next\server\chunks\ssr\0vvp_@swc_helpers_cjs__interop_require_default_cjs_0l5yet_._.js
apps\web\.next\server\chunks\ssr\0vvp_@swc_helpers_cjs__interop_require_default_cjs_0l5yet_._.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_0a8tx4q._.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_0a8tx4q._.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_0yf71j9._.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_0yf71j9._.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_forbidden_1ggo7-6.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_forbidden_1ggo7-6.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_global-error_00sump4.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_global-error_00sump4.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_unauthorized_0pk5k4a.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_client_components_builtin_unauthorized_0pk5k4a.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0n_nx_e.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0n_nx_e.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0q-yo5m.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0q-yo5m.js.map
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0u7v3fl.js
apps\web\.next\server\chunks\ssr\1e9k_next_dist_esm_build_templates_app-page_0u7v3fl.js.map
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app_page_actions_1agtzgh.js
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app_page_actions_1agtzgh.js.map
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app__global-error_page_actions_1vxuwj7.js
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app__global-error_page_actions_1vxuwj7.js.map
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app__not-found_page_actions_0iqyci7.js
apps\web\.next\server\chunks\ssr\apps_web__next-internal_server_app__not-found_page_actions_0iqyci7.js.map
apps\web\.next\server\chunks\ssr\node_modules__pnpm_01nw_00._.js
apps\web\.next\server\chunks\ssr\node_modules__pnpm_01nw_00._.js.map
apps\web\.next\server\chunks\ssr\node_modules__pnpm_0juuhxd._.js
apps\web\.next\server\chunks\ssr\node_modules__pnpm_0juuhxd._.js.map
apps\web\.next\server\chunks\ssr\node_modules__pnpm_0v35rfe._.js
apps\web\.next\server\chunks\ssr\node_modules__pnpm_0v35rfe._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0-y56ms._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0-y56ms._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__03x2jhj._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__03x2jhj._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__06o13be._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__06o13be._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0947r3l._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0947r3l._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0gvqzic._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0gvqzic._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0ip0ay8._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0ip0ay8._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0u38kbp._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__0u38kbp._.js.map
apps\web\.next\server\chunks\ssr\[root-of-the-server]__1elao27._.js
apps\web\.next\server\chunks\ssr\[root-of-the-server]__1elao27._.js.map
apps\web\.next\server\chunks\ssr\[turbopack]_runtime.js
apps\web\.next\server\chunks\ssr\[turbopack]_runtime.js.map
apps\web\.next\server\pages\404.html
apps\web\.next\server\pages\500.html
apps\web\.next\static\4Il72vyhzHHscf4MZPhdf
apps\web\.next\static\chunks
apps\web\.next\static\media
apps\web\.next\static\4Il72vyhzHHscf4MZPhdf\_buildManifest.js
apps\web\.next\static\4Il72vyhzHHscf4MZPhdf\_clientMiddlewareManifest.js
apps\web\.next\static\4Il72vyhzHHscf4MZPhdf\_ssgManifest.js
apps\web\.next\static\chunks\0cz1d0mv5g_q7.js
apps\web\.next\static\chunks\0pjcgjp85jq-c.js
apps\web\.next\static\chunks\0t1g-jyjnu-c0.js
apps\web\.next\static\chunks\10sonbf0yo0pp.js
apps\web\.next\static\chunks\1pphn9jd6_uxx.js
apps\web\.next\static\chunks\3hm4udpnd6vck.js
apps\web\.next\static\chunks\3w03_klv_6vcn.css
apps\web\.next\static\chunks\41prdxmdars1m.js
apps\web\.next\static\chunks\turbopack-3s27kwb82qvnw.js
apps\web\.next\static\media\4fa387ec64143e14-s.2tuy5pz7dlieh.woff2
apps\web\.next\static\media\53b9e256198e5412-s.390ncx5urfkfu.woff2
apps\web\.next\static\media\5ce348bf30bf5439-s.31988l_ccedte.woff2
apps\web\.next\static\media\6306c77e7c8268e4-s.2dbetqa9o8jxf.woff2
apps\web\.next\static\media\7178b3e590c64307-s.21jp631_3pja2.woff2
apps\web\.next\static\media\797e433ab948586e-s.p.0r6juujl39pe6.woff2
apps\web\.next\static\media\7d817b4c03b0c5f1-s.1uyisp29ctx0d.woff2
apps\web\.next\static\media\8a480f0b521d4e75-s.1qq4vpdcun5oj.woff2
apps\web\.next\static\media\bbc41e54d2fcbd21-s.1rgnod-3esatf.woff2
apps\web\.next\static\media\caa3a2e1cccd8315-s.p.0wgildi0cnwt9.woff2
apps\web\.next\static\media\favicon.2vob68tjqpejf.ico
apps\web\.next\static\media\fef07dbb0973bf53-s.3p2_lha1f2xer.woff2
apps\web\.next\types\cache-life.d.ts
apps\web\.next\types\routes.d.ts
apps\web\.next\types\validator.ts
apps\web\.turbo\turbo-build.log
apps\web\.turbo\turbo-lint.log
apps\web\app\favicon.ico
apps\web\app\globals.css
apps\web\app\layout.tsx
apps\web\app\page.tsx
apps\web\public\file.svg
apps\web\public\globe.svg
apps\web\public\next.svg
apps\web\public\vercel.svg
apps\web\public\window.svg
apps\worker\.mypy_cache
apps\worker\.pytest_cache
apps\worker\.ruff_cache
apps\worker\.turbo
apps\worker\src
apps\worker\tests
apps\worker\.dockerignore
apps\worker\.python-version
apps\worker\Dockerfile
apps\worker\mypy.ini
apps\worker\package.json
apps\worker\pyproject.toml
apps\worker\README.md
apps\worker\ruff.toml
apps\worker\uv.lock
apps\worker\.mypy_cache\3.11
apps\worker\.mypy_cache\.gitignore
apps\worker\.mypy_cache\CACHEDIR.TAG
apps\worker\.mypy_cache\3.11\cache.0.db
apps\worker\.mypy_cache\3.11\cache.1.db
apps\worker\.mypy_cache\3.11\cache.10.db
apps\worker\.mypy_cache\3.11\cache.11.db
apps\worker\.mypy_cache\3.11\cache.12.db
apps\worker\.mypy_cache\3.11\cache.13.db
apps\worker\.mypy_cache\3.11\cache.14.db
apps\worker\.mypy_cache\3.11\cache.15.db
apps\worker\.mypy_cache\3.11\cache.2.db
apps\worker\.mypy_cache\3.11\cache.3.db
apps\worker\.mypy_cache\3.11\cache.4.db
apps\worker\.mypy_cache\3.11\cache.5.db
apps\worker\.mypy_cache\3.11\cache.6.db
apps\worker\.mypy_cache\3.11\cache.7.db
apps\worker\.mypy_cache\3.11\cache.8.db
apps\worker\.mypy_cache\3.11\cache.9.db
apps\worker\.pytest_cache\v
apps\worker\.pytest_cache\.gitignore
apps\worker\.pytest_cache\CACHEDIR.TAG
apps\worker\.pytest_cache\README.md
apps\worker\.pytest_cache\v\cache
apps\worker\.pytest_cache\v\cache\lastfailed
apps\worker\.pytest_cache\v\cache\nodeids
apps\worker\.ruff_cache\0.15.22
apps\worker\.ruff_cache\.gitignore
apps\worker\.ruff_cache\CACHEDIR.TAG
apps\worker\.ruff_cache\0.15.22\1205400479180200510
apps\worker\.ruff_cache\0.15.22\7376564740154586940
apps\worker\.turbo\turbo-lint.log
apps\worker\.turbo\turbo-test.log
apps\worker\src\worker
apps\worker\src\worker\core
apps\worker\src\worker\jobs
apps\worker\src\worker\tasks
apps\worker\src\worker\main.py
apps\worker\src\worker\__init__.py
apps\worker\src\worker\core\config.py
apps\worker\tests\test_main.py
docs\decisions
docs\diagrams
docs\api-design.md
docs\architecture.md
docs\data-model.md
docs\deployment.md
docs\development.md
docs\diagrams.md
docs\README.md
docs\request-flow.md
docs\roadmap.md
docs\system-overview.md
docs\diagrams\auth-flow.mmd
docs\diagrams\deployment.mmd
docs\diagrams\er-diagram.mmd
docs\diagrams\query-flow.mmd
docs\diagrams\system.mmd
docs\diagrams\upload-flow.mmd
infrastructure\docker
infrastructure\scripts
infrastructure\terraform
infrastructure\docker\compose
infrastructure\docker\keycloak
infrastructure\docker\minio
infrastructure\docker\postgres
infrastructure\docker\qdrant
infrastructure\docker\redis
infrastructure\docker\compose\.env
infrastructure\docker\compose\.env.example
infrastructure\docker\compose\docker-compose.override.yml
infrastructure\docker\compose\docker-compose.yml
packages\auth
packages\clients
packages\config
packages\logger
packages\types
```
