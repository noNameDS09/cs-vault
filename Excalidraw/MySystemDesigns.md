---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# DDD vs Modular Monolith

The easiest way to remember it is:

> **DDD is about *how you model the business*.**
> **Modular Monolith is about *how you organize and deploy the application*.**

| Domain-Driven Design (DDD)                                                                    | Modular Monolith                            |
| --------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Design methodology**                                                                        | **Software architecture**                   |
| Focuses on modeling the business domain                                                       | Focuses on structuring the application      |
| Answers: *"How should I represent business concepts?"*                                        | Answers: *"How should I organize my code?"* |
| Introduces Entities, Value Objects, Aggregates, Repositories, Domain Events, Bounded Contexts | Introduces modules with clear boundaries    |
| Can be used with monoliths or microservices                                                   | Can use DDD or not                          |
| Goal: Reduce business complexity                                                              | Goal: Reduce architectural complexity       |
| Not tied to deployment                                                                        | Single deployment unit                      |

### Think of building a shopping mall

**DDD** decides:

* What is a Customer?
* What is an Order?
* What business rules apply?
* How do payments work?

**Modular Monolith** decides:

* Put Orders in one module.
* Payments in another module.
* Inventory in another module.
* Deploy everything as **one application**.

### Together

```
Application (Modular Monolith)
│
├── User Module
│     └── DDD Model
│
├── Order Module
│     ├── Order (Entity)
│     ├── Money (Value Object)
│     ├── OrderRepository
│     └── OrderPlaced Event
│
├── Payment Module
│     └── DDD Model
│
└── Inventory Module
      └── DDD Model
```

Notice that **each module can have its own DDD model**.

### Can you have one without the other?

✅ **DDD without a Modular Monolith**

* DDD + Microservices
* DDD + Traditional Monolith

✅ **Modular Monolith without DDD**

* Modules organized by technical layers (e.g., `UserModule`, `OrderModule`) but with simple CRUD logic and no rich domain model.

### Interview takeaway

> **DDD models the business. Modular Monolith organizes the codebase. They solve different problems and are often used together.**


# Code Block

The easiest way to remember it is:

> **DDD is about *how you model the business*.**
> **Modular Monolith is about *how you organize and deploy the application*.**

| Domain-Driven Design (DDD)                                                                    | Modular Monolith                            |
| --------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Design methodology**                                                                        | **Software architecture**                   |
| Focuses on modeling the business domain                                                       | Focuses on structuring the application      |
| Answers: *"How should I represent business concepts?"*                                        | Answers: *"How should I organize my code?"* |
| Introduces Entities, Value Objects, Aggregates, Repositories, Domain Events, Bounded Contexts | Introduces modules with clear boundaries    |
| Can be used with monoliths or microservices                                                   | Can use DDD or not                          |
| Goal: Reduce business complexity                                                              | Goal: Reduce architectural complexity       |
| Not tied to deployment                                                                        | Single deployment unit                      |

### Think of building a shopping mall

**DDD** decides:

* What is a Customer?
* What is an Order?
* What business rules apply?
* How do payments work?

**Modular Monolith** decides:

* Put Orders in one module.
* Payments in another module.
* Inventory in another module.
* Deploy everything as **one application**.

### Together

```
Application (Modular Monolith)
│
├── User Module
│     └── DDD Model
│
├── Order Module
│     ├── Order (Entity)
│     ├── Money (Value Object)
│     ├── OrderRepository
│     └── OrderPlaced Event
│
├── Payment Module
│     └── DDD Model
│
└── Inventory Module
      └── DDD Model
```

Notice that **each module can have its own DDD model**.

### Can you have one without the other?

✅ **DDD without a Modular Monolith**

* DDD + Microservices
* DDD + Traditional Monolith

✅ **Modular Monolith without DDD**

* Modules organized by technical layers (e.g., `UserModule`, `OrderModule`) but with simple CRUD logic and no rich domain model.

### Interview takeaway

> **DDD models the business. Modular Monolith organizes the codebase. They solve different problems and are often used together.**


# Code Block 1

The easiest way to remember it is:

> **DDD is about *how you model the business*.**
> **Modular Monolith is about *how you organize and deploy the application*.**

| Domain-Driven Design (DDD)                                                                    | Modular Monolith                            |
| --------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Design methodology**                                                                        | **Software architecture**                   |
| Focuses on modeling the business domain                                                       | Focuses on structuring the application      |
| Answers: *"How should I represent business concepts?"*                                        | Answers: *"How should I organize my code?"* |
| Introduces Entities, Value Objects, Aggregates, Repositories, Domain Events, Bounded Contexts | Introduces modules with clear boundaries    |
| Can be used with monoliths or microservices                                                   | Can use DDD or not                          |
| Goal: Reduce business complexity                                                              | Goal: Reduce architectural complexity       |
| Not tied to deployment                                                                        | Single deployment unit                      |

### Think of building a shopping mall

**DDD** decides:

* What is a Customer?
* What is an Order?
* What business rules apply?
* How do payments work?

**Modular Monolith** decides:

* Put Orders in one module.
* Payments in another module.
* Inventory in another module.
* Deploy everything as **one application**.

### Together

```
Application (Modular Monolith)
│
├── User Module
│     └── DDD Model
│
├── Order Module
│     ├── Order (Entity)
│     ├── Money (Value Object)
│     ├── OrderRepository
│     └── OrderPlaced Event
│
├── Payment Module
│     └── DDD Model
│
└── Inventory Module
      └── DDD Model
```

Notice that **each module can have its own DDD model**.

### Can you have one without the other?

✅ **DDD without a Modular Monolith**

* DDD + Microservices
* DDD + Traditional Monolith

✅ **Modular Monolith without DDD**

* Modules organized by technical layers (e.g., `UserModule`, `OrderModule`) but with simple CRUD logic and no rich domain model.

### Interview takeaway

> **DDD models the business. Modular Monolith organizes the codebase. They solve different problems and are often used together.**

# Excalidraw Data

## Text Elements
RAG System Architecture — Grounded Retrieval + Generation ^8EjmaysK

User / Application
Input: query, intent, context need ^NfuNXcHF

Knowledge Sources
Docs, PDFs, policies, DBs, wikis, web content ^9qt6z4M6

Ingestion Pipeline
Collect → parse → clean → chunk → embed → index
Chunking options: fixed, semantic, recursive, parent-child ^QYkI051B

Search & Index Stores
Vector DB, metadata DB, object storage
Sparse retrieval, dense retrieval, hybrid retrieval ^q42pJDJY

Retrieval + Reranking
BM25 / keyword, embeddings / semantic, hybrid
Rerank with cross-encoder or bi-encoder ^21W54fI6

Prompt Assembly + Generation
Compose query + retrieved context + instructions
LLM provider generates grounded answer ^b6CqrEnl

Evaluation + Operations
Offline / online evaluation, faithfulness, relevance, latency, cost
Observability, tracing, authorization, freshness, model routing, scaling ^8wVWRnGR

query + intent ^zwGseedP

ingest / parse / clean ^uIIt6dda

chunk + embed ^MQ34MgBG

retrieve candidates ^bOhMHL2t

context + answer ^wou9CHot

feedback + metrics ^BSguvrZH

Decision logic
Sparse / dense / hybrid?
Simple / complex routing? ^KWYKROlf

routing choice ^mTHrtMVY

RAG System Architecture — Production-Grade Pipeline ^jfNTYfde

Grounded generation with external evidence — retrieval → ranking → prompt assembly → LLM response ^eLqzg7aJ

─── DATA LAYER ─────────────────────────────────────────────────────────────────────────────────── ^wXEehLGx

👤 USER / APPLICATION ^CAqcPcm9

Sends natural language query
with intent and context need.

• Query rewriting / expansion
• Multi-query generation
• HyDE (hypothetical doc embedding)
• Conversation history (if multi-turn) ^T7qN8U8i

📚 KNOWLEDGE SOURCES ^adkWPngg

External corpus — the system's memory.

• Internal documents, PDFs, policies
• Technical specs, product manuals
• Databases, structured tables
• Wikis, web content, support tickets

⚠ Quality of source = quality of system ^yTcaFH6v

⚙️ INGESTION PIPELINE ^z0nni1zZ

Collect → Parse → Clean → Chunk → Embed → Index

Chunking strategies (choose based on document type):
  • Fixed-size — simple, predictable, may split ideas
  • Semantic — groups by meaning, preserves concepts
  • Recursive — respects doc structure (headings, paragraphs)
  • Parent-child — coarse + fine-grained retrieval
  • Sliding window with overlap — reduces boundary losses ^kHO0uwQZ

raw documents ^QZ0lTl2M

─── RETRIEVAL + GENERATION LAYER ───────────────────────────────────────────────────────────────── ^ZyUCYwrM

🗄️ SEARCH & INDEX STORES ^aMjnKeRL

Storage layer for embeddings + metadata.

Vector DB — stores embeddings
  ANN indexes: HNSW, IVF, PQ, DiskANN
Metadata DB — stores chunk metadata
Object Storage — stores raw documents

Similarity: cosine, dot product, euclidean

⚠ Most consequential infra decision —
  migration after millions of chunks is painful ^M11YfPj5

🔍 RETRIEVAL + RERANKING ^q9oVDBuh

Two-stage: broad retrieval → precise reranking.

First stage — retrieve candidates:
  • Sparse (BM25 / keyword)
  • Dense (embedding similarity)
  • Hybrid (both combined) ← best default
  • Metadata filtering

Second stage — rerank top-K:
  • Cross-encoder (most accurate, slowest)
  • Bi-encoder (fast, pre-computable)
  • Late interaction / ColBERT (middle ground) ^Fv94IT5E

🤖 PROMPT ASSEMBLY + GENERATION ^QeFUIHLD

Compose final prompt and generate grounded answer.

Prompt = [system instructions] + [retrieved context]
       + [conversation history] + [user query]

Token budgeting — each component consumes context window.

⚠ "Lost in the middle" effect (Liu et al., 2023):
  Models attend to beginning and end, ignore middle.
  → Place most relevant evidence first.

• Model routing: simple queries → small model (cheaper)
                 complex queries → large model (better) ^1OYF80Gi

chunks + embeddings + metadata ^IP5JbT2R

candidate passages ^e7kGmb5j

ranked context ^s04lyK5F

─── EVALUATION + OPERATIONS LAYER ──────────────────────────────────────────────────────────────── ^3aZyPcTU

📊 EVALUATION + QUALITY ASSURANCE ^taW66CZr

Measure retrieval AND generation as integrated system.

Offline evaluation — curated test sets before deployment
Online evaluation — real user interactions in production

RAGAS Framework metrics:
  • Faithfulness — answer supported by context?
  • Answer Relevancy — does it address the question?
  • Context Precision — retrieved passages relevant?
  • Context Recall — all needed info retrieved?

Also: Precision, Recall, Hit Rate, MRR, NDCG ^ZzOAF7i5

🛡️ PRODUCTION OPERATIONS ^3WqTCMqS

Latency — p99 < 2s, retrieval < 300ms
Cost — model routing (cheap ↔ powerful)
Data freshness — updates < 5min, deletes < 60s
Throughput — burst capacity for spike events

Observability — what was retrieved and why
Tracing — distributed across pipeline
Security — auth, authz, data residency
Compliance — GDPR, SOC2, data processing

⚠ System that handles average load but
  collapses under spikes = worst UX at worst time ^VGlf8TQg

🚫 HALLUCINATION DEFENSE ^31G4Ui06

RAG doesn't make a system perfect,
but makes it controllable & auditable. ^jC8Fklcf

feedback + quality metrics ^ieO8ZcUy

🧰 EXAMPLE PRODUCTION STACK ^kfzWGHFq

Orchestration: LlamaIndex / Haystack / LangChain   │   Embeddings: BGE-large / OpenAI / Cohere   │   Vector DB: Weaviate / Pinecone / Qdrant / Milvus
Reranker: BGE-reranker / Cohere Rerank   │   LLM: Claude / GPT-4o / Llama 3   │   Observability: Datadog / W&B   │   Serving: vLLM / Triton   │   Queue: SQS / Pub/Sub ^mzBYN5kj

💡 WHY RAG EXISTS — CORE INSIGHT ^mdscLgqT

LLMs have knowledge staleness (training cutoff), can hallucinate, lack private/domain data, and cannot be retrained for every new fact. Fine-tuning changes behavior, not knowledge.
RAG shifts intelligence from static model parameters → dynamic access to external evidence. It is not a search engine on a chatbot. It is an information architecture + engineering discipline. ^wXO3PEGB

Make by @avadhoot ^4oBjFOTS

query + intent ^aLJe1wXl

Domain-Driven Design (DDD) — Business-First Software Modeling ^IwVpyEPn

Core Ideas ^O3HNNZb2

• Focus on the business, not the database ^fNZ2Hm1p

• Use ubiquitous language ^SeWfqIgz

• Put rules inside domain objects ^XtiBaov3

• Split into bounded contexts ^Gh4JOPCo

Key Building Blocks ^p6zgavUw

Entity: has unique identity ^FRHMchhC

Value Object: no identity ^AbkF3sSn

Aggregate: treat a cluster as one ^iwscLzOS

Repository: load/save domain objects ^UTRxxzHw

Domain Service: logic not in one entity ^iP00OSyk

Domain Event: something important happened ^CkRm1RY6

Example (Behavior inside domain) ^EGMNUvDz

Before (service):
orderService.cancelOrder(orderId) ^nZMABUnH

DDD (domain):
order.cancel() ^DsOOmEIb

When to use / avoid DDD ^IZGIjJHL

✅ Use for complex domains:
Banking, healthcare, ERP,
e-commerce, logistics ^H2oeRl0q

❌ Avoid for simple CRUD:
Prototypes, portfolios,
minimal business logic ^Tac8gkp1

One-line takeaway:
DDD models software around business concepts instead of database tables or technical layers. ^RK5AYU8j

Modular Monolith (Single App with Module Boundaries) ^WZB8ZcTN

Definition
A Modular Monolith is
a single deployable
application organized
into independent modules
with clear boundaries. ^Vp3wyKD3

Think of it as:

One deployable application
        │
  ├─ User Module
  ├─ Order Module
  ├─ Payment Module
  └─ Inventory Module

Modules communicate via boundaries
(in-process, not direct internals). ^tLYd1jgY

Why use it?

✅ Easier to develop & deploy
✅ Better organization than monolith
✅ Faster communication
   (function calls, no network)
✅ Easier to split later
   if distributed services are needed ^g8vVjYJJ

Modular Monolith vs Microservices

• One application vs multiple apps
• One deployment vs multiple deployments
• In-process calls vs network/API calls
• Simpler ops vs more operational complexity
• Easier debugging vs harder distributed debugging ^xWF96cWZ

When to use it

• Most startups and small-to-medium systems
• Large apps needing clean boundaries but
  not yet needing distributed services
• Teams that want to avoid microservice ops overhead ^iMW7AZoM

One-line takeaway: A Modular Monolith is a well-structured monolith with strong module boundaries. ^eDBqD64E

Enterprise RAG ^u5y8VkTE

Phase 1 (Development) ^VpMRnLWu

↓ ^eD7ZxYWe

Modular Monolith ^10iGX1zj

↓ ^vprFtLM2

DDD ^KQbzc9LJ

↓ ^osoVfy70

Clean Architecture ^xZ0aNhS2

↓ ^jrsGV0Pm

Production Ready ^EFBuwRY2

↓ ^mRx0LAX7

Phase 2 (System Design) ^7PXYHm0D

↓ ^g4L4lvha

Microservices Migration ^XjOhfQsz

↓ ^Y7yqZY85

Service Communication ^X6MSn5r6

↓ ^geodsOuN

Event-Driven Architecture ^vtHa3LyP

↓ ^BinKcTLv

Scalability ^hno4tXhJ

Reason: ^qFoZYaSZ

Learn DDD and Clean Architecture without distributed systems complexity. ^m3qK7prr

Build a working application. ^Phsq5IEa

Then refactor selected modules into microservices. This demonstrates architectural evolution, which interviewers value more than starting with microservices. ^vah8J02p

## Element Links
d5sKSpBs: [[Excalidraw/MySystemDesigns.md#Code Block 1]]

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebR4AVm0AZho6IIR9BA4oZm4AbXAwUDBSiBJuCABZAAYAfQAJGD8AERhSKskAMwBVBIQATQBGGAAOZTTSyFhESsDsKI5lYMmy

zG5nZIA2LaHtABZthNGthIB2UaGtviLIGA2hgE4a7TOhi7Ot5IT9x6uz/hlCgkdTcIbJHg1QGQSQIQjKaTcR7JKG3CDMKCkNgAawQAGE2Pg2KRKgBiZJnfZDBJDVaQTS4bDY5RYoQcYgEokkiSY6zMOC4QI5OkQLqEfD4ADKsBWEkkjI0gRFGKxuIA6iDJNwblMIKyERxwnk0ENoRA2ALsGp7iaaqjdWEEMQwd93naPmbGCx2Fw0FtRp6mKxOAA5

ThiMHXRI1P5vM2EZgtDJQJ3cLoEMJmzTCdkAUWCWRyxtQ+QAumahHBiLgU86TRd9jweENqTUEjUdWUiBxsdwOEIJWaiUzU2h0/hM2jCOysJVcAAVHjKzE4hDSmCy9CCDwi6zLcSoe1lFnCOAASWIxcKU0gAEUAPL3gAaCW2PAAMjUYAAxfRqgZGHAQz6AAahMtzlmiXTkFkF59gO+Bmqy7KGswxb9oOaLysw85YFA77Tr2Y4ZggRQAL6AiUZQVBI

oy5gAVvouAwMwADSIozAe0B4SK6xoJsWw1HsCTXCcyRiX8Zo2qgzhXKMryHPsow8N8jzKTwAZosCxCgmgFx7I8PCUs8KmHGcCRmrC8KImg3xmiqq6csSZItkMylnCKDJMiebIcoSzk8uQHD8oK2RQCKYoSuum5SAqIhIPZK7qpqYJIcIBpGqlaIWoy1pgna9kIKOqDUo8jw0mcyTlYG3qcGCnw1cGHBhhwEYmk8vziZSnaQAmSbBLWaYkVmObEPm

mRhVekG6pW1aDfWoyNo8+wxkZTZDoR8GYbqw64nWqDjpOuoppg4USAASgAggA4qgkosSm+ioJdoiSGoCALPFqCACgEqDXchxBOqg50IJihAIPQBCoAA1H92RMDWPoRZwUCSoQRgHhpZpdCj364Po4rSVsZonVAl1EMovroMEXThTVUDmAQ5PwlT0AWp5oRBNOB5HpA3YIA0cIImdJXxBZ2WkPC04ELhp2VFdt33RimTPa972fYEP1/QDQMg2DENQ

7D13w+QDN1fGM58egC77MuqprjKXHbhUZp7puvMQD556XgUtx3o+L5vp+P5/gBQGgeBUzTWU0H4wgcFoBhiFogDqHoQhZp6DkuDc6QCeoEnrtCFAbAg6wGPcJiQgIEhlCyyLEAK3dD0qy92BvSmGsIFr/2jbroOSwb+Aw3Dhqm0jlmhPXBE9kNE6kaUFFFFRvX7RAYxFWwLT0BwMBbMQAAKXRdNdIF1EV9Dvhx8BcfMiz7rxGzbMkeyjOVZUJEZN

TbACaLSbJNR9jaGuGpHgfw2y/B4F8M02ldKoAhB7KywttSQkSvbJy3J0CkkSF8BAmgObeQBhgskxAhjpgQAkCK4opSO0qPKdu8U7arg1DpLUaAep6nSpINOWVdQ5StLAfKHtHT7WpJcd4b9qpoi9E1bUOxGo+ham1EqglTinGeL/XUfVkzFUOjXNE2ZfLjULLkX2N4V7UTXkMOAbAuhPiEPRIw9EACOlYaikFGD0AY50ajYAAFJ0jKJxOcpAsRUD

9kvcxftV6VCEM4jgkg1R4n0Lme8eIuj0X2JSfQAAtM4rEuhamhEEm+ISwkQAiRBCsVYazFQkY2ZsrZ2wcO7ERAuGc0S7V0cNKcls5zzlGEw3E0UnaEhdmiN2PMzRewvFeP2UgBhdH2IU98owBhbGcfgd8fjLpDDxAMecRgqDFIgA+Z8r5rjB1/P+QCwEwIVKjtjGC8d9qFxTqNHhicOm6mwtPTaxF57kUolONeIYuhCBDE+bADRvzX1mDyHiZorY

CSEtoN+CQP5fx/lJDYZxHjALAcpcBPxDLQK0ildhyRkjaDKkMLJWwskrWeIAyyQsbKoEMtocExxvjJEbJIzRZQHK4mIRIUkrl3IEOZEQ/ymCICklIeQyh2NqEjLoXFJUaDmEUpKmlPw3DMomjNPwvKtphFFVEfsVRb9GyCsgDIpGtl9j7AUaGcMB5nVCSeGVD22iBrdPniNIxBZJoFGjpAWatTRENjAUytayQNqzy+dtLsbARz7T0STHiEgehhFI

KgBQz04A+EZmbDgAAdDgZ4OBwGLmgVxTAYDUFQNOFMORqCVqzqTAuFrkY5DRhXdhQCRLlREjGOlVVYzY1xvjQm3BiZolJszSmlQaZ02kUwBm7hl2sxLnADmYR+bcA9vzQW1kRZ7ESMayW/gZbZvQLmpgBai0lrwGWyt1ba1QHrdXUgTaW05DCs2rteEe2pgtoDK2EAFx4iGQ7DcoydyuyWO7aZrJvZzJvAspZKy1kbK2TsvZByjmBNOQHC5H4vzX

LDncyOpRw2imefnN5upU6GvaSmyAXac5j2Y98souBi6l3COjA8maU513vRAR9+bC2XWLUQN9PoP01rragBtf7m2tqA6gEDp0wPOknjhPCM82l6KBcvEFlQ4D0WxEMFoVRkiaGSGwZQt5lDMGcJoKoT4CkBJJqUiQd9JmP34i/LYZwuWjDOGAmkK1Vo4v4mcSLZUlLlTtDUf01wYE6tMsAhl1IqQ/EpHi1l57Ix7CpVcNsalwRvw4cK/EsqyRnGwM

kXA4GDGMmlaNUVWDj4fTKlQqKtC5QaoSmiRrLC4EcP1AatCvCygmsEWawqdT9gJE22AjRrqqYvw4Q6t1rVMY1FGO2IYYDqTxkTDojNPTdSGLzCGosZipgWJiRIOJCSkkpLSRkxluT8mFMCdMQL1tQlsHCTeSJb3onlDXiBUweIEhtBaBwEGkppCkGcD0R4yh6C3hB9AMH0GIdQ6mGRKpaJI3zRKjGxp7ZmmJraSx1N6a55HWon0iQC5rpwbVRIZ2

hmJkoamWiGZPs0DXl1CBSU74Wj7GcEYHokocn7GUIJSQZw1RwHvMwA+pGzmB0uVR0OtyI4PPo08uOfHOOcN8p8jjycflTxM/8g6JELOlBXvDyojxnFQC2EYfYVQthwq4qTULMkX4bai+ZFE/pRincOIlmSGL8vvHOOVSqVqaQ5dYWCNSaLfhCWOMtTLL8yvIJNFVGljYthlWWpIjFLrJtJSa1yFyLZJVZm6z5dkfX5UDewENlVI2EPqoYZqtv9tp

tsN1e8/VjvTTZUtKakqBVJu9pNIkcS23xa6kO1TDbB+yhH6UQecqVIfUomu/1UGAbOf0lGsY0NUuGM07qTG8vhkYut52u7qznzGmntBzvosdFJqxBwJDsEMQMoAgJWpKMIKIOEJWi0GmswM2gfC0N+JgZWjYopuDJgagC0AAELEHAjYgJgdocAUB4K6YoxhR9qoyiYoIpDPCjAvy0qcHIin6QA4w5B4wEz4BExZqnQ7qroIC0wihehbpMwUy7rsy

96HrczHqJoCxsoXpizXpSwcB3pywSBQEwFOjwF3TIFiDMBoEYFYE4HEEEHmBEHNpkEUGEBUEUH0EgbCgQazg87zjsRarDKjZbhjLC66ghZoAewS6YYy5y4K5K4q5q4a41Ba46564G4nJG4UZXJm7hz3JU66ixywSvL8aQBsYLbJrO5lDca5y26VGQCCYlxlysEApP56iSYGHoBGEUCwGmFIEiAWFWHYDEHYG4HNr2FWjhBOHkHNqUHUGoB0GaAMG

AZeFYSu6nSmZgFe7FBWYSDKDOANDOKaAUDnQ5JVD4CYCYDviXTeA9AcCYC3jKqLok7Bai5R7OBGTiTaCvgkp8rmRlTyJ/y4ryRvDfyfwqQ7B4p57koF62TvDAKvhJ7mRuTthvALo/KaFgix4YrggaTOoYrKRZIBEd4BRYI1Y7CPBSr95+Sd5ioICPAfRSHDY0IT5jZT4TYOjt5z7ah6oZTlEL58Jr4rYb7mpf5nCALIiV4bq1R7ZGS7YX5giEqfA

iRQlaI3b+p3aBoGIv7PamJS5+zva+4SCI70DI6o7o5rhY44544E5E7BI85k6W6Lz5FlCf7RqLRNgtiM4djM5bR1EQBdIamtHTiQb9L3j85BHoghG7ivERFoanizKvZlD0QHwgRnDYjJB1BPj0T0nXQwBVBimXQJBCB1DrAnIDC3hMSaD6BHLED0C5jYCXSXQcADDOD7D0BdANCG7kZBym43K5F0ZgAMaFEvK+l6ooTsZAGxTGbrHu7maLzApaJry

3gDDYhnhthDCkHh6VCR5IobBGRwmVQ0gxh4lKR8HrwbC7DAKGQrQnCjBnYN6LT54zaVRfFikeluQXY4n/5lBILspDCnY0qUiXB8rvDJYth2rojt6D7ird5GSUkyo0lYJ0kMldBMkC7oD0KKjslCqck6or6sZcLL7GqCnST/kin7Qvw1AxaZYYq7bcBVQQXn7uqF4t6ba+pqkP6BngFlCPZjQ6lTTVJzRf7uk/5rTfl8yAElH+kgGP7cXTBSbVrwE

Yg+ioAHyECID8yVqcjBALCoCABJhKgAKCwN3AZdgMENYPpbphoD2JWgZZkJoEDAZcGVgFpdZVQUsKgBaGWvIAdIQJgE6M2mEExDkOYDQfMCIKwIwGMaFDkM4O3OKKETHCjAOgeHCYcBimKXSv6IcFVNOoIbOiIfOmIWTAoZIdIfTIzPgBITyEoV1ioYaGoZ0tzGetXqLFehLLofoQ3IpeEGWqpepVzIaFpYSDpVAJZUZWEJZWZSEBwFNW5ZZfZY5

QBpBq5WyO5coJ5XAN5WOH5QFagEFdYFus2uFd6FFYZTFVAHFW9PgIlb1NztbPOJKOGSycEUhiLg/LGeLuhgmXqVhsmamemZmdmQgLmfmTUIWcWaWfMuWZWdWRQLWfWY2c2a2e2Z2Rkd2SbiHH2bRo6UOUxsUXbmUenHbtUbxgTX6Q0cJuXGJvdmUOQBQPXJUD1cpZwP1RpdzMNRKB9GNQZRNSZbpuZbNaZfNXZfoA5cQJZc5ZgKtT2NOBtV5T6D5

WKP5cQIFZkIdaFagCdZFTXOdUKJdfFTdSKL8m7kmh7oCvOZZouZUKMHQaQJoLmCGMoE+EYPoPgHiPOMkLeEMH4ZKDUFuUFtzSFruWFrsMOptlSOJFanaCJKns2PJO8A3j8FVtHY8GiUCDqiiK/EZJtstFklVG/FXuypCJem5BSGAgysiFAkSdBcQNgFAlAvBb1s1mKmVHSV0EuGPsyTFJhYwkSVyewjyfNsWPhUtiRUImtqIh2GlmogmlKbIn6IS

fPYosxbaGpGpBFrlVOBxbTuJg9tqRNC9r9bDjeB9ugOdGqKQaMHiLgO+LmCDO+N+JKNdPRKMPRPOAMPeLCsUqDvCuDuUhEsUgaTROgNYrYvYo4i4m4h4l4j4v4raSToKAA9Ds6RGjUrTvUu+V6S0pJXbgGWAd4VBguCBM9TFELtGR9YeHGZWD9SWPMvOGwAgD0H4l0MwGqDAJsHiD0FsJfBCDwBQPQF2ecj2VjTRhbqg4xjbuTWOcQI7pOSbTOWb

XOWADDj7iAxAM4o2HAH4i0H4gMAHegDuWiMit8G/AcN/OBU2K+I8HHbXuCNRdSNSCiJcE+fPokPJCJKZC/IeV8KcEXRenyvEGpBtnSiZN8M6jXS3VghKnBb3oQs3YhfKm3Y8B3WhRGb3dPhybPnhUPURavrlEKWRZPdwOZJ8DwFktFnRXpFvYfkGCvcdgqVcFklAstHfrdgQ1qcGofbqSWB/ug8JUtHGjFmea0qOZ0jJVxcVZUJKCEK9KgAAGSoD

VqQZ3QlyBCWEcAgTc3EgkGkHNpZBRBzS4C7M0F2D0Tc37VrPRAIEcCSh81a0DzgyQyISoCAzBQ3OBD6zPPNqSAwCaCSwS2fODzPPMEpXah7BKTJZglR0UgRZ5VQBCFzp+jFXVXUxSHrq1OkByFVWlU1X7rKGDVi4AGGgtV/naEdW3r4CM0SAzOCjtwLNLOWyrPEioGbPbP5pkH7Ogy4BHMnOeWaDnO6UYjEjXOIH3NAtPMEDNpvOTUStDw/N/MAs

PNfMEAihS39I5KkOIbjJhExlUNfXxmS50NYYMNMMsNsMcPJBcM8Pvh8MCNCPG6UaiPm55GPJQT41jMEUO4TlSWk1MC1FFyNEiaDrm2tH03UvoC0tzOLPLNYDMvrOVpbMLA7OcuoAHM8s1jHOptnMXPCvkDwFiuCiyuPPyuvPZDFsqsvO/P/MkDKvAuqtGZ/JKOe6W3e47HoBGCkHJCkFnj3g5JlSQrKA1DOIzOSj0BVBsAeQBZ/16hB2vEh3R6Z4

0p3mmSxrlNnnSRp3LtQJvBkXilkq6iwLz5UrUqQhCTRZ3nLSfBL3onlbsJNhcpUobZnaGTBNz1ZOORRPyohDHC+JN2+TQUhDEDAdTtQSqrpPjZwYD28C5Psaj2QDLakWb4Ojb4qJ/BUh4pxjL11RoBjpymr0co3n14p7b3367203P5dMmLRFtun2GmgNCBbA9DXHJAHy4DOLYj6CjDEC3hnjJDECSjfgtAIMztIOQ6OkqNANw7qNhB13OCXS5iYB

wA5J+L0AUAJDu2aC4QtDnQidcRifk6tsn1YbqMX1X03130P1P0v1v0f1f16dlLieVJuszT9NukNKeltjelNVm2Tn4MtFyXlD3XQbzi3WQX2zoWRlvW6uUORHfVGvS4/m5J4iaCkH0AHzzg5LSiX1CB4jviPBGAcB87o3COY3UYusDl41SOet00fI+t24KP4SzktuSdW2WKVDNhqg/BdBnhh7TsR6IrGNPx0ryQembZPCZXrSAk74vCfnnAojbCXB

3nvsZ0wm8CLTAKFYUgrQogiQQW/kBN7B0rje53HCVRSIfsipfswVuSxNdbxMAfXdAcgdpMvWxRslQc5OL68kj3EUFNIfkVggYrlRQIRZnlH4lPiT4cNMmjRZUo2qtOkftMBdBpPbdMCXU5uf1QiVDPV3jPs4o+LpSZ6z1vDywwgxBTrWVqkFVCJDPq4gwAUDEiq2oCLXAdy0bOFoHUhXYAKs1vECVoU/WDYjzFqCSC6ZYhoSuCtRsCAz5rEiVqaC

EDS96By+gvNG8AvBqQQgEnlRUra8cICEIsFWiFE/iG4tovlVSnYuotsz4t1WEuNXEsaF3ttVnnEidVUvE8lvPMjxC+y1LDU+08JD08ICM/M/Nps+OBLDMDPrc9HWoDVsAuC8Iw9ii/qAS9sBS/ZCq9Po7NK8q+y9MBqvBcLhFIz6riRfkPIaxfUMYaJkwjJepfpeZfZekG5f5eFfFfzKZEiPlf9m43W5FE1elF1d8mTl+t5zSMTJCZNEht7103tE

Nwk+Stk/Ayp9U8cA090+FoM9M+kAs9R8c9x/q0898/J/mmU/p/i/YCS+eY59F/y/5oF8P9q+Num1mYUf+m4P4BbFqNrxnAKAVQV8Fw2UAtAhA9AbAAMEui3h9gHAb4O+HnAGNZ2CwYOkN34hfwkgeKW1DSApB3l4O55WHtSkZTdRymQFCLBwiPb0U7QXKebpNxMibZ/GYIJPNoGPINIqKlIJxpE0SakgagXQT4FsGwr0g+8CFEkvKlwAJBiAowY+

K9x7qQd+6uWWDnyQIGIcJ6W+L/NrwYoHsz8dTHDqgARLQ9lEhWGMD/EYFI91SHTfelRzfzGtjO1tCQEMEY7MdNgbHDjlxx458cBOQnBzvaWQYU4pOdHdRk+BDCnFmA94ATlUGcTEAEgbASUHiD46YAEgFAVID/WJyicHSznK3JjyErucsGXnHBr5ykr+dQ2gXdVr4XwBatKg1fd6qhgNY0MEu8yfAFsCfCSAAI5gPtj0GwBDB2y2Ie8AMHfBCA8g

JXR1tkWxriMXOMcD1hURkZyMpKjXDYgFz/7tsIAmgLYHiGcSkBcwHACof123KDddQyKKBJwQODvANESkKkIXWm6a8DIyWZsFSnPYqQzyVA9hOnm2BUVqQDKN4CqR/IYka8kWZLHim+CCQoWd5bgWIJu4957uPWR7ok15DBQjKTBLupFwyZCDwu2qNbgQLmx5MBS/3NQShzqR0oWwVIKiuD10FUxlShg1KmVCMgN4LgHCP1JxUsE8UD61HMNIJSjT

Y9Bmq0GLOnQkqFC8GEzJkfJQ6IQAD4WIfQFtWehoR7KIhGGJWmNhjxEYnAYahKKz7dwNMMAEeHK0YAC8ZegGfTLDGnAqghACwRWpWnfDvgqghlLEGYDl6oB4CiolMBsypJAw+QdtdXiGzcgpAxSVUQkYcAiycFNIBRGdMIVN4QFzeLMMqhix0FYtKqtvPdAekd6fVnepLLQu1T4Q3ppYXvEUWKIMCSjLo0osWrKKNgmwlRFaDgASFVGTUNRWon3k

DD0xjVDRwUKuKaM4AbMLRVouADaJIBPoHRCMJ0faJ1gS03RxfQhv0nt6Xd4MZDKMjX1qG6goiDff0s0NaGWBsAHQroT0L6EDChhPfDGk637440JGw5ANovnHLj9fWKMHjP62n5hFZ+wbGmpqVYxL9KguYiUWNQLFBVNAxY0eP2OUwVi8xao9TL+k1GwxtR9YxggaIAzGjWxwUc0ZaOtFsBbRvY0sQOJdHDjgo7o9/oo0/4W1WutHdrhIE0D3hxgU

AHoF0BDD0RNA7ZEMKQS2C4QtgVQcwMgJeIPwF2mwSBK8DpTx5QmMYGxlcJpAeNAEtw8SFRX9CuMSmgkJgewmQ44V0E13HKqMDwD/sB8T3ekmIFQpIiIOH3BQWt1myEU4Of3ARAD2Kaw8VIHYXYNoPtRkj6KKkSkflGRK/AvhbTCwYTysFo9WRx9fCfYK3BOhsA8nRTsp1U7qdNO2nXTqkLtL/0nOKDCYWgxyGci8hTOHziziKGCjXJXOEMr4WjEC

B28VfGcTUKJbHh4uNHSAGqGxDQEOAQweiH4gPg1AOApAeiDkmICkEEAuYHJGyAdZZFeyYjV1lkIKJTCncMw+rn6XmHNdcJqjZYbbRAhqhzoRXMKU8RnZGMDhT8K1HEDeBZJXwPEsqKnh+CCSskMWESZ8CDGrc4EypeIO8CtTKRdgbwUEVhF+GoAIsXxMEXKghF3cHsIghJuCOQrqTZBXEFEZ9wxFKDfu+TIyXiKFSocLs+5biaSOlI2SDsZI+Uuw

nQ7uk6UzkxkWlMo7uSbBZYdkRg2/y48IKozaYfj1ALozuIIo3MM8yEBliR494RAOPDbGVp7wx8fmM+k4Asyh4VMstM2nTBi9wU+ANOMdQyCQxjszafALUlaj/o9AGIRmfYCYCQwleRAWAM2l5BWglgzaBopIA95GAyx3M9ZsPX2ZF9h4rIBmGrP2ruA5aHo1KkdP4IhikW90lFhb39LosZCm6OMY7ITEEsj0yYrsM1TumXp3emYvQtmIbgUyCAnM

lSrDFpm/iGZHAJmV0BZmFo2Z3MVnpTJ1ke5eZA4AWQ82CDCyxAos8WdgEllZ8oAMsvNPLPFDWhlZ5AVWcoHVnFxNZksbWVzIOh6ys5+gQ2VrWEAmza5ZsggBbLHG+Eoak43KdFwEx6s4uhrYqRAFKnlTKp1U2qfVManNTWp7U4YZ1OdYD8jx/UyckTRH4QBJ+J428UG2pqVxSA1cWuAzSkyhzfA1MyOXTLLEbM45CczytsOTkcy05PM9QHzKzmBA

c51gPOagDFltpC5wGYuaXLlm4AFZlc1ACrLlp1z1AWsj+a3KNAGzAYRsruXAt7ndgJgWEprs2zGkLkCJ6AL7IkmSSpJ0kmSbJHkgKTl9joiDB0mxPuFJB0UmKH0RCW2nxAk8doP4NcFUgfxxJNeVaadjFJCQUQOddMT8Nd5xAlIp2TLEZDTqZZ/yjwCChiEFBkwycsIHlpUHKmojsgxAF6GEk0VrwDOIoGxK2mKmJdSgvMKxX7HDRgBLFYAHEq8G

EV2hwQHYcyBIqmDvEDgSeJPNcDxSqIlFZwWxRI0azQUcEyQPBP9JmyAzFsCHceqtnUH7RIQZAikGdyqbwILgdkvSDHREhcTUZ5HR8cyOsFH1emOMgZglO87EtkpAogniUIHnWwegP0qoXlOHkRlqhMXOcTxXekwixBcIkKPrRFALjPJpRZwC0DqCSA/EpBYgN+DYANAqg2IHgOdC7ZQAjAZ4K+GvL745FDxMUyRsPyJleszxxNP0qoqxakFgyFst

ABYgwA6l8468UYJvG3i7x94R8E+GfAvgbL5k7cwGJUGJBK8sp/BXaofDYCtoG+jin+i8HbBCQQl/gtEHovOXshLlqAa5RkBMR3KbMdmBzE5hcxuYPMXmHzH5lIzfKuIfytQKRmVpOgD4IK4UCMrADWK6VXxVxTCqM58xQgUASsQTBkCUrqVIseRmsTwU4TWi7cxgIxOBXmKNQ6gV/DSpKFLDvJEAI5NdBETpF5pA3OWIwrEVfFFoaSqiu6D4m6h/

45TFIA3ipAXZzImWCxk8J1R3li84kOHpdlLy8ipAfsyLGeTCXXdtujjZSdST6VBQBliIsDuPjkHaSK+yUAGd92HpxLzQCS4UiZJKhw9rgQkUrNhypjlMCBTFGHhyguCLQNsfKApbJVR58V0ebI7IRyIWhcjf8spJKXvOKEL9hRDcGsU2LbRZTRQyVDXijKgi2zCqyLM3iVUjESA10Ls2Mdundm1U3p9VAqXyJd6tV/ZOhSlhGw0bASR42mFYlolL

49BBkRJEeTqzHm186h9fEZXqDGUTKplMyuZQsqWUrK1lnyrDL3zK7bLxhvUyYdVwOW1dvW54kmpeJqI3iBMd4k+WgCriBdw2UmBtQBibXG1+VCwmVUZ3/6VBjSppGAGjgxyWlcc+OQnLsN8Hic2JYCKBF8RUh0oYwZ2PlNsDjoHBmwzqK4IJHRS8KBFcagyNFk+HthkQVqZRVJNQDyQ2wGVf8p/A7CLRTsiUNRQYshxGLtFnAXReyEE0UBhNGG45

GiDMWlLLFDi+lTUFsXFIHFH5ZdtezNVMbaRP9ZwOxtzogluNuJU7MysHJPSWsbWDrGFymyKDw12IseriMSX4jREFIU7HeUuB6qYxC9VAHiWyUlQG6OwRyZ5t6g7181nTTGfJr6ZxSy1lSgoTUr9I1qv+ZQxpd3wKLgc3uHS2SZX3aWtKd1XS4QQ9xUmwjfVCIldYVMnmLjnE50ZQLgDOC3hSA+gR4HUH0DOB8AkgHgILGUX0Bewmyu9WMJ6lmb3W

z6gaaeNkZDT+NZyi5UsG4Aorbla8DFfZkczOZXM7mTzN5l8xdB/MXyovr8vtpkqTkFKsVdKsU00pG8Z287WVGtlWLGV0Km8KWFuAw5IA8KqbRMCuXzJUVYUO5XsQOJHETiZxC4lcRuJ3EHiRKnbRIFJUArRQQKqlaCtpVKabtQwUzY9v9JsqOVagWsDDulV8rpyAqoURAGFUIBRVmO3IBKskBSqRYyjcaXKqEBngzwgeYDrgGQGLS1ge5OHsAk+B

cbnU0WXPKnmcCCQaUmWa/BdmRCUgfgNGhlGinh7DMeUbkRHre1aqfxHpIa4ks9I9U0gvVg+fpaVubWRRu6v0+Qcrug6Yj9JygwyeviKZJLC88WXxStyskwzbIN0zFk1ARn+aqK5TQSJljzWTNwthajyWUpLW4yce3IytdUurWpT6lPayoHLV6oFp8CRbbuAoE7SC1LZmJeFoiy7X2ye1tvAdRVWHV9rDGo67peOqd4+ySWfs8lhmM97zro9GIZ9P

c0LTTVrAJfDKY0rDKbqcto8+ouPLr60NLFGjarbVvq2NbmtrW9rZ1rODdaOpWy/rZVyH4jkX1o/N9ccszifqyae8ymnPwfFhtnxEgGvWNULT16BaM1cDTjsg2U7CFZ9aoLeD5RVBlApBVLSUgWn7CWdYWGkJVkTqLQ1pb8a2YQJKivCKQyWCEJ8ObDBaIAzwjlFsCvJ4pBdy0fDdllumu84SrqqCu6s4Hq64m0IorT6r5Da7mlrJLCtEvnzG6l8B

k4GebpkkCBUOXwU7MtEkjJruAVqcSgwHhkEcyNNIbbJSC9147eK5O4qcAysQ2I7EDiJxK4jgDuJPE3iXxFtro4RTScfgp0rstdLxTRKMWAmT/yHDh7a1ZMhuAwjT6ww2eKek0EwaN7p6wxQSPCNnudm575C+eu3omK9n6sUx5ezxeaEDldVKguhkXvobFqdZV1Le6DD0BIbt6MtuWrvbuvnFFTFxVwOZSGDtADBmA+AZcgMGuh+JJAIYSQFUFvBC

Ap9fW7qbPqG37KRthysbe+r9IHzv19RX9RrwA0Xz51nhkeAYdwVn6WuVOohRADAZCHIGoh8Q7AykPICTFjCrJAZHfgg82FAJfVY029GJqaDG2KihSBo2jdk6uwEbuas/hnkDuSIF4H4ouBEak6xGtvAJo0VAcRNDVM0Hook1SbIpMm3UHJp6YKbokSmlTX7AcWLH/RRIvxW2E8WlBngaKTLDsf9F68tgpmhjG6p4F10AthB7knZtIM4iQZTmsGcV

HMjuQudtu5g/btQAehk1LukSECOBEQUGRhS1ojwf4rFrXO0WunO6QZz5CfSC+6SnUq0PJaAjYXXXVuus05SO926sI/lpWE9KsDcqLXRdSGWRGD10RhoLEZqDxHEjAwZI6kfSOZHsjvW/cfeoG1VdCjO8sfsWGuURSeAD2ibVAARXR9XtyK97XNsqAbwEAW8HeHvEPjHxT458CGNet1DErdt/y8ldDp5VgqXgvwNOtFihUZZXFdqUoHsHcVrRVDoZ

j4kjrOPsgDTSK2bd0zuW20mADtJ2i7Tdoe0vaPtViH7VB0/Lwde2yHYduJ2emDg/xLLItGpHPANsgZsAM4BeAdhasnBdsF8BOCOMfgkZzpKjoMCcqMdHp2kyNPwWtEgg2YOgt7qdOITCdJAYnWwzF7k68dh2mZsoD92TlTlUAM8MwDuYfQrAFQ2k3orXMbmrQqrCorKraNmdr6t9e+ggEfrP1X679T+t/RVWOdrjL+6PAnleBGQzshwDen8dTwvx

5IWWfDcBQrVMHwDF2IBOdwTX/k3j8B+XX+X/KvAf4K0DDuJB+DIHDjhi44xIB0UihzjRxrRdJtMU8qLFDxiFU8ZvAOLrgRq2rDHXjptgrtdK0i1MHItxBtgVFz425Fou6aWwLwSqBFkQvvBkLG2Bi6UDU2GrwLJdQBNsCuA9RSgskOCzxcpCAJ+LH5hIMCfM20kJBSebAJCcHrQnTdZBwphQfRDgzkQVdGLE8AyUtm/N7wJsJVCOAECCTYWtyb7q

xlRbS1FJjzk0iqWl74tGh+k0lrXU7CA1eulpZ3rRGBEQjoV8Io4e6WFbvV/JkrYKZ70NCsMkgbEGMokHnRWsrUnoNdCYj6ANcjwA+II0VOjC8jg/Ao/PqKOvqjle8lczGem1vasMH2nIAmbtrJnnartd2p7W9q+1/aJyZ03mddMHb3TsO2wVMGDNPAL2zKRsOcEUgQqSz6WMRUBV4JfB2zuoZ7YioavGmmrppiQJ227a9t+2jwQdsO1HbjtJ2OZk

lfmbdMq0iztK2s6wPYvvCK1Ii+lPNe9MkplI57W7r8DWtdhOz+gbs9ytGvY6m2gqwLkOchzFQajaIAnUTsIuk7ZzpM+cwgEXM2DlzUQLFnucQAHntzVVp7eyGxubnDzTuY85fqIkZGGg74HgM2tkPM7IAJjFEC8DSWeM0lITJg9JGjApBXNjSN4MtFfA0aWw+KfAY2ZF3rHnVSuycdBTV20gMDVJTXQlcGWaS3uf0nSXAmIM/dI1qg+E5QeKi7cK

BZ2NNdZNw4XY/NMWRILwWeBcHSZxJote/nKW5CVDIe7y2Hr8tFK61cwOsbpmsCOAhKO44Mf2jbXGHO1ZhutZYat6YsbeI6icUXqTHRXJ1qYsEBXqWxuHg5ntr5t3DwCIq/bzenwo0ubWNZWTFDbk8MrGswg0rLQDK1lZyQ5W8rBVoqzkaVMz7yrfU4beqaX17zyj6+qoyGxhtPjL5IosCd7ezu1J/bP5CDaNLCBk36O7RpwSx1cGcduOvHfjoJ2E

7oarjbxDSNsFeB3lAEDKISf6A3bagqKdecvN/DTo/A3Igtw1WVAAMXYdgd5cyKxu+BfE3IV0vbpVA516mLjGF9AFhajP6LcLxihhbJsIsN9FNJFu7apuiQUXfgieHE3ynSp49T6ymqB88ZgfSKfT95J9kg95GlAX7Ak9+xFk/u7AhL9i6JKBdO133Qej9vgvg6SCEPM8xD2Fojru2hKUDPAvgQINRE2bdJsSo1PpeMmW7cO15P4NDO81cWf96aow

b8CtTEPLJ5QULaOeKURa7jrlwPR5ewY0n8bdJkmRHr8N53oMQRoK0XeCPTjIr3eqEfLa/YCmlbe63vfMlwDNaegfhEMEYCGAcc8QyQe8MoE0CFc1QpACkickwCXRzoPAXMF0BqA+O8QOSBAPsCECsRMAnQEMP7kbulWKuLdp9Wqakq7zaTdVl7TNpNPxm14+1ntn2wHZPgh2I7NcOddA5YYBr6ACHTdeBvHaKHj1rhXzdDMx1xK12j678C+sflde

f1gm01IKeNX1ru19AIAOAFWsegYAiAVAJgFwCEBSA/q2DsafXXhrt13s2XZrN1nvU6KQkccAxSPD5rJ7T8nhoEHr1DgwzlHRiDR1cqjtvKuYRPYHMQ38Aw56G2fMC5w3JzCNmczqTnNAqFzS5qSiuaJu4295u59czja3O+lp76jJnkIEeB4gGgbAWmyTnpsQBDhnBIBLsDSXmQaQXwUA5zYfZeo34iinbs6lRMgWYwXKc9rVglIYooeCB6dS6rUt

YIZbGumx4rf9VpbA1+u4NZOKN38P+SDmuEzGuEf3TXwVKJyfQb0guHpHB4MUkg+27W39HKj5y5FodvKH8Z2jvzpoa/6R4JADYkeCOJJDwswWRhtPSbyKpZ7HZOe63m7NsMeyHeDhk9L7MQPJ2EOqduoxBMbGoBzXudohiBAf3ZSIuHJsLlFYnn1Cp5Tj/QC49YhuOPH2ILxz478ccAAnQT+ZCE7CcROonygGJ3E4SdJO0jqTkq11Iydby27OTjU5

3dX3Xju7x86o989qNSZTXsMIN00cnsLw8J2xOVbJz8kKclOKnNThpxS6hT+jIDpaWFhJHmNaLpwC4chZ/OJAuUVwYXQ3gW7AWrVSQI4L+wuxtgGU5wVjW5Eiy2qGURwwA1VAayY31F6FvC3/dE3YXxNQDx8wRfMXgPiLDxshw4r027vTg+7yECJCrM/1T3KQO8he/9BXvDIql5XdBQUlKS1bbjUVyoOjUW7nNkYQ4AGauzyu2N7ap3fUyMGbugDN

l9V1odtt+7sZAeipVScSmh7aTiW920F38O4AQIxj/l8FcFyhGwrU47VlG8sdvTYrCtnA4lfsfJXdQuYECLeHnC5gzw1xeiF0BySM8eAzZZgCIHOgWvdxpXJu2VerfZPCadbvJ7e/qtGm4zaKkp12zKdHWTr1TsdhOzqdjnczGzoa/MkLM7OTteJKlGonchEu9p81iOjsCI3WWlIEIZILc42uGnCnO14p5UCIkkSyJFEqieRNon0TGJWltZ059cMu

esMbn0aydvEj+hMsuwNSBikEiMoznt5Ir5NdK9thglbD2FTtABtA2nne8/s+DbNC/Onn05yVYC8WHQblhpBSUMoAgGkAckaNB8wijVXoDF238I1Z/GUXnAdgR71PEylfIvsqUl7zbDS7wpejlFb9+RRXV9Mnv2XcH1A0VlltWPRB8VkT3Y44/IiDdwrr7l601sCPYT5BwHtJJwQrRGkGSrz1ZZ26XSrUZHr/hR5cs6uYtTttQ/yIS2GumPxr9AF0

AtReQvDabR5kMUMMlRg7+VUMXa/DG9qV0/aqw067z0E+C9Md4QcXu9kJ3nDAcqvVJkR9OhkfI8A5pLHR8NKjHgVtpRFc5PQYBP5W2N4uMk/SfZP8nxT8p9U/qfNPN6vcek83m7LjxFR+3DVdpNd3aTG++8afPPkSYB7DcBn8QCZ+wwWf5gMezCFefg2EXa8PELeDOBnhRgOSZgEMHfAhhMAdQbEGqAOK3hsAaoHgMVYm/oAWJKwLDYnmAQomSvFT

Dm9wEZxcprp46b4pOho1QJEEfswy6CfBHXk7QqI5H9Y54HHwR8I+PAxhQe9ZbQ1MS3S0DLe8GWPvPmiEEpFUSMVjbGJx1Uq6RDC7loyx4H0x9B/yb9S0nNeMENCHhDJQkQ6IbEPiHJBEhyQnwRvcyGDayTblzBrR68t8ifLxMxy+lMMe4A1QlQrjxY/CP8/91Zd6APsHnD+gzwq5MaNgBAjYh6yNQBoEnjxCQ7b1Onqt/L+3m1uO7fZs35sX69yr

WI/4ViOdD3g+ABpJ++2hpvYP2IfiF5h+DYNtKru7wOxZiOvKFtLQk6ttFgpA+JJniAIK7D/obGfoMIgcO4IjEwOeBWpgZxW25Ly5lagKgK6T4BBkh6RqWIjCbiu73rGr4kFZkmoEeegg1BYmrBuhx2ghwD/oOWyjhjJauajuD7uWsaMHo/6hMjo6MerRPD4QASYFaBNQgCq5jmAhbMZTPoMrAnqJ8irCQAAA/IgSEAEosEDPoegMYFxsxsnLR6BG

PlcA2uOPt2p4+4ds2qyEzrqT52GnsqoRU+3/GXpeuLhh7xzqUmIoEJgKlESCqA2AOoGTUhaFoHPoSfPoGGB5gaYF5iwQJgCdyxcFYHBuc4GqDsexfrx4hWPPtG5JWU8lADH+p/uf71kV/jf53+NQA/5pOlbnL6Pq/BG/4GeH/jo6q+Ojur5/qMCq27a+86kEHKBoQWoG3Mh+tEGFosQcQAGBtzEYE+A2gWYHTBKQZYFLA1gd25vOFvpUD9+VQGEI

RCUQjEJxCCQkkIpCoAQMbTe7xFtjAIECJwRee83KibSQLFl8QN4TTDX4mQNGlgLNMPBGdiXA1+Bwi4B/mviiCQUCFzoaQXwJCTf2r7phZPuADj/YPuchphqgOH7iMoQO37mg5kW0SM4AvBMWG8HHAhIoZCgeYCGcH/BSkICEUg5ULB5S213On41APDrhR8OZflrZoeKfuDI/E1wGDwZKGkKAbN+ekNFgXA38FRQd+RJiyJg+1HrkKL+cWq7Z6ODJ

qXxPgBflFw8+hdpG7F2E6jyZCePLjd58u+/g47S+2nrL47KDQXsqVW7dsr7bWdCn/Q6mDXjhRqKJnlF4TOMXhIDTOIAnM7gCkAtAKwC8AgkCICl1i6b7arniNatOKDq/bfwuwGdz/knBGIigerAuc7HOm7gRp1eUcLqZwq0ZmM6GhZQM1armlvtb62+9vo77O+rvu77OInvt76++9Tus5ZenoTl7ehIsCdrnYF2FSibYb8OJBUoumnWZAm9Xiyp3

O7Kl2bo6LTs84NcX/qTKQ2I5t/59uMGhID6A84A0BYsVQCBD6M69mAFB+gCCcIgIK0CCRAGK3s2CPWy0M2Cb05wJwYoB8+NaqfCzwIg4qQykC4ysuf5Cd6khPAly5y2V3uQEqhlAVDrUB+Bn3SG6T3q+oveYrvEqOakrhh6w8HYJJbsBXmo6glQOHhwHNQBHBRrLQyFlfbmCaMhq7CBvBqSYukWPBD648Ugeoar+QgWAFBYGCh5TtwIKhGCWuQdn

YF2yjqkugOuRPpHauBihOT48mlPvHbeBU6mSx+BvrlJgLBG1HhHmAqIoya4AU4crqmO+UiXqQApdn3pP+WoQ+qz+WTnqHv+BoRPwNuU/E25U0Lblr79286mxFWU+EaiJteA4a0aX6pAHUC/gQwJKBJC0vDE4UAcSIjg8AMAMqpGht8HOysSxwUSHUon5KdhdQ5UECGp4JkM4p0o5wngJNmgttRQnuv7By7yoQwAgBgITmNy45+0grgBdA6XiY5yh

dAbZCiuHsNrbfhCJvtAEkNqJtj1+6JkGFWWgkJthv6TBoIHcG/Id35RIgQkuSSAd5FUAUAZlJgBbA+ADki/gfiPiCsQt4GqBt6cOLIYmKM/uo4VKj9nWEgRLtgx6w+QZKXyasZjnx7yhgkZ7DCmh/hwBnA+ACGBngfiNiAwAygMwxDAaoN763gCANILOIsKHp5SRzQQaFamYOGF6mhpvqfo9uqwRIAKeIYB/RdAPytOFYuJjPHjmMiDqcDggG2Fj

BXChkEIreRWqhcB+RO4SUxlQNKBFjfRP8Ke7i2rvCtDBRvAl0DWWjOteEfS13vCKied3glEvhYas94RqXgalHoe6UflDGQyijGAZKxwGbbukIFMVFKOpUSUqiBgobq7B6oBtIEGubtnIHE8N0M3DKwT0G3Adw3NF9C/QuYsQAmiZaM4D/QPLN3BqU7NKcYdqgdiGwQgxERnqkRFhuRER2MYlHYuuhehT5x2Hrj4HTq3rq4Z0+Iok3BKwj0KrDxUn

cFADCxqlFiBixMEpLHkAgMGzSO87PrgCoxfETjGdKCocJHzIi0ctGrR60ZtF+I20btH7RXQIdGZOjQTW6nRJRsvpogbQZOQdBSkYBo7659DzEWxrcGrA2xdsaLHixPoM7HSxbsUejLB5vj/5tGl5s4hGAygGcC4A0ho/qqqzau9Gvgn0c6jQxv0T/qbsYpF5Fc6ZkGdie6YMXpDp48ilkiXae9o7qSKrVKginePAp8JKQ+CGjG9KGMX6r3hLJj7E

5BIrjSGExdIVX7/kDFFSB3ClMVI4sGGapNbNgnxmKS8hgXF35Mxc/ho4SBFamzHoRO0GNGBc8gb3C+QQMH2L0ys1MCAZ8eEEwBByKcj2LHYWsNqJQwBlJTxy041OKKSioQJ+KyiBlB2IPM/IG2KoiRvFa4qIKsaHbaGTgYOraxbga65jq+seoSJ2JoMbH+BWYvOpfxM4BLS/x1MgAni8QCaQAgJEMGAliAECT7xQJWtMLywJvNPAljUiCTKKaiKC

fBLrMNiO8wZBPOEvHex3Pvx57+QkfNF96gcStFrRG0VtE7RPAHtEHRR0a/5xxfpLk6tBckYfI/qzbr3bdBKkVJh0JgMAwkoSKlMwms8p0MAlQwHCW8xcJv0JAnDw0CfwkeUgiXmLCJhYl+JiJqAKgmSJGCSfpg22kRfoz2FAE+C5gCAJIDvg10EPJNxewlN4zu0eB9FUuueD9Gfw3cfZKAx/cb5FDxh7Fap0u1YfRqMGWqjgF+yyBnJI8Cy0LgBO

YG6pd7oxt4ZjG3eMcOlrmOMoVSHq2yUWbqV+satcDMus1kbbomVMdwHnxzYOiGQgLLqqRkca/vBEkm9tszEoRrMfq4pSnMR/FSYgAACkhySQSXQ84JdBhJl0AMD30qAIck3JtyXcn3JDyY8lPJzyS8mvJ9yTYGG8Idrj7mGEYm4GOulEST7UR9hp4H0Rp6DT6zqNCQclHJLQCclnJVxJcnnQ1yW8nIpKKailopDyTInWwcUVz59JiiSXYqJAcUtH

qJIcVokRxeiTHG6hZiYvoyRF4tnBfqCkZvqa+6cTr6VANyccmnJ5yQilIp6KTym8pfKTclRJH/DEltcl+i0C3ghAJdB1AjwNiDNCAsJdCM8AeDACy4+wDRGyGAfqiKtxxAt/AdxuAl3Gp4kFsUk+RIMWUnHSx7AjGnhIsIn6IxESlErLxfJiQgOUMUZgm9J00YlEwcO8fRFEx9IXUgFRcikooZKAEXbrO64EWZBZYXwHTHLJmEXfF8GvfpUA9AQw

MwCSAEymcDnQmgH4j6ApBAkBGAeMKQQWAoblP7QhhnCowSMShjFqDRwYSMyvxbOGKH+WLHmyYRuCiTNFeB/sVhgwAZ4M4CSA+wLmAIaowC0D3ghAHUB+IyQM4D0AdQBwCXQ95lhhqJwcZolhx2ibolRx+iTqEK+e8sYnnRf9JdEthWkX16DhywniCXQziNgAHw2AI1pM6z+gzZPwtlu3F5JfKAUn6ptXn3FGpg8Y6rgGeGikCQgyWOZIwxU8TCB3

SLhqn7PSoUStAxRkUdgZdJqoVQGcer1P0nZMeMW+EExnqXvGxqClv8GMaFlh7DshbGopZJ475jfEFqCEeskPxFSk7Yvx0Pr5Y1pcPlJiAAvBuAAJjuoAKuFclyYB8AfDvgZ4PunzgvbCGAY+s8QHbG89gZnqOBGsc4GuygKduS6xtEWQk+cjEWmK0+AQSKK0Z9GZKCMZz0MxmsZ7GZxmYp0GJSENpuKU2n0RLafqrtpnad2ktAvaf2mDpw6aOnjp

k6bqDTpGiaHHhxOiZHHRxx0VSlK+CcfW50pa+mr492B4H3aL8LKRIAKZDGYilMZLGWxknJGmeXHCpXkjPbzgZwM4ghgniKMCEAZ6ZknPmmwFem5JncXelXCSimBZCQJScakvpuWLXgealUKDyCQHwl8F+yD7A0mfsl4SBSbYoGavG4GytrplupGtghkpRSGVK7sW5Gp8DIg6GX5oMUMYH8TsUkaQzGqOGPERmO2QzLfhVqo0bslTMNLHoqx8ehLb

HkAw8GLJLAVMqYQailaE4nLqwieyBLE3aIaBOg2gJWiVogAEQEqAFkaNoDzBQCSw3cs+hYAAoMFB/id2VUADgDMM4A1ijCe+gcAd2U0AtAuYKgAAAFL8w2I6gKDCVUrzGmis8PhuzxLAAAJS3ZqAASAcAMiNTJvQebJqIQ5hAF0Bpsv2crybZHAKjk2BWPnxkkRDsrYb/JWsVRFiZNEQyB0RBsdJlJ2zEabENwMzOyDrZNYCIBQwO2cN7XMQEo2i

HZYvKBphQgbqdmmuF2cQBXZ5YndkPZf6E9kvZsCYWjvZfIF9moAP2fgB/ZAOQ4nKiwOagCg54OVDnwA6LrCDYsCOdgBI54tIabo5JuVjk45fVHjlrMBOUTkk5+uWTkiAFOZpkgZU0XkF4pfsQSmtpRmV2k9pfaQOlDpI6WOkTppGHZkkpc6WSmLpFKSum0mxibJFeZjbj5kWJfmVYkBZ86rzmXgBcALlbZgCnuB7Z6osBIS5GfMdky5EtHLkWoiu

Rjkq5mooEDPZagBrnOJH2U1AY5euQbmLqgOTrlm5kOdDlW5cOe4C259uU6CO5GOS7lBguOQmAe5kOV7n6ApOc4Dk5lOdFk7pOkTPYVi10EsAUAygDADXQ0QhwBNarEKjaVSHDMxJ2Rgfg5HhR16Tll/RExraCNgj6cDHPpNGiJKsaVqXPHgirWO1i+GMVqQGAcgMCkzOpj4dBn1p6IqX74xjuD1lfhxMbrbRoHpLnjHuuHtBaARR2Moh/4ZeASF4

ZPugRll2/BnGkJpSaVripp6aZmnZpuALmlGA+aeFL0K8hn25eSbRreDVRowLVH1RjUc1H6ArUXiDtRnUQWm9R0UjqGlp4geWkvwlaWRkYReOtxE4K8iR1kCRzaWHm6gowKQQ1AzAPGlwArEPoBbA2IEIBVApxPsD4AAwGqBuYieUSkzpDmfOnOZS6RJGxx+nkYmGeiYb/QHgm6ewVTk0SXvmxJ6jDyxu+B8EsDKFNkRkktxT8GtAlmQxhcFMasdH

lkPpmVEVk/5w8bwDp4CakiaHu+9o6rfB/6QQHPSCQJoDNgqwi1mdJa8TroupwedpYfh9uO+HIFErqgVGW62FRQaIxDhko4FQaYR6X4oTHShmSxBU5akFVHrNksxv+Atn0eMge/ErZ6AFRmAAWzuoASbveBqgd9C0DXQ4OZKD3gPQOdB4guYE9SERIbDxlJU2PrTn2u9ORRGM5omXizApDVF4FgpvgbJmQp8mfMWLFyxbmCrF6xZsXbFuxQHm0KOQ

fxG+xs0QZllAWhToV6FBhUYUmFZhRYVWFaGoSlBx9maSlOZ5Ka5mK+WebSlRA9KXnmKRlicpFF51Gc8UhgSxSsVrFd0J8U7FexasQ3RKwZXGX6MAPOB4A34A0A8MaWZEVhY0RbI7XS+vLemOqSHMtBf5A8aDHlJukucCMq/wItAQkadKAbfB+GojFPs1II8SCe4BcqHgZ68VUU7+MGfAVEGQyYI6gyaBQwbKKkEaeQdFcMtKTYmlwBFiiKEacjxw

RKwmVH3xSEeSaYMKhuMUjRkxctmR6EgIpwpgbCVDB6ApALWix8v0LDn7ULcPoAAA5LHxZA7cn+it5JudWjelICcQBpoQgNRw2EoxIZRjIExBsx3ZuEO3AcA8OfyAfQdhA7HixabNYBUyE4BjmV2UQKzmTElzGfJdwEtDWXBA2ZagAagbhDMQeEjBO2j7UlYDYhYsMCuYC4guQNdkcAgAAVk92RWXWgnlMTmCA/RN3AAAvEBJ9ysADOUhlfMVTm4J

3yWHZCZhCUzlXFHgTcWgpnrkbFc5cmSHIuJPpcPB+lAZVrDBlzAKGURlqPtGUwAsZXdnxlricPBJl2ACmWTQaZXYSZlRBBjm5l3CAWU42xZbLyllwVBWWtl1ZZAqcwxBNBKbZQMM2Wssd2e2VzECxGdk6YansWjEgY1FujDlGzJWgTlWRiuWaitiPtTmEi5cuWKyFFbOWhlAeallB56pSHmAlGhcCXaFuhdYjglxhaYVVA5hZYXWFJyEnmzpjmQu

kuZBia4WDSpRivo558kViWMp/6oXmlEGcRABeln5QwT+lgwneWwg65Y9BPlUZcSCvlo5e+WAYV5bbm/lRYP+VjEgFWhWoAIFfmXT5hZUMRjEJZbpTQVGYFWWZstZYhUtiyFU2WQKLZRjkYV7hIsSeEUAIFR9l+FYOUjgI5eWKkVU5auWUVc5SgSoAS5a4jkVa5Q+Ublu+VBq7pcqvOAgQAjMoDzKGnveAcAT4EzKEAPAGqDOAHQLCXhFgdKgLzsx

wfIpapX0bqm5Z7+Rvif5yRU+mClpqfOhJ4/+ZJKAFz0mSQN4ZRWKiKoHWAqU9JMBdKFwFJfsh4epDRcwF9Zoun8CAhkyd5qPkMyUYL7YWAf+SOqJUTbZ2lMaZVGVAXBTVF1R5xPwUtRbUR1FdRMhqwVRSV0f24mca8LazoE94CBDOIAwKxCaAZBE4h6aQwBjCYAUvlhg9RGQhIXOFEAFIWYMMhcNHL+ooSsnMeG/vRDb+sBXpkxuB/n3o5IaoEMC

SAEWD0AsZCQPQCSgjwPfrJAPQGeCYAzgCb6QAolfYWp5klculNBbhS0HrpXhbGEu4VJRXEFVbRkYC1S+ZeDWTRoAW9F7kgBi/ldVb+WUBIcIpf1Xf5g1ZACvpGkDSgfpz7HA4mCdSVIr1ZV3Jw4VM5wNNWGMFAZUWLVmWuG6al9ASbrFg61SMl9ZG2GpBch4IBZaommGW6AbYVWcpADFmrkMX9Rc2dyIulqNUtkUZXMSKKAAmWSAA8H9LMIYGsWS

gHGfeAhgqlGeAHwuYKxkhguYNxkewJhra4OBPyfj6swDOXbpEJQKYeUKhdxaeUPFQcvOox1cdQnVJ1KdQfBp1GdWeBZ1AeT1oqFrqWoX6ZHFZACE1xNaTXk1lNdTXXQtNfTWM1NhfCXJ54lY4Xp5nNTJWJxuoMnFSUqcTiXMpddbHXt1jdZxmp16dZnXZ1eVefoipM9tiANA94DUBCAFALeAS1TVYYznp2LtLUvk2WXLWFJa9AVlAxApSalq1mdG

Yz687YEngiQORSe7mpF4eCJylzWXalkBgUHeEW1UGUtU1FXWUgXDJQjj+HwIAPlVke1DfpwR+aa0Oaq4ZMEYSa3xF1YhGxS8/njLB1BsSv5vx7pXj6VA2lBcwGUbHBoEGUeIILSWUeICLSoAuYMjmWUsbNLTliXDWtSwJKoLUiqA4QJDl4RgErWUS0rNN+VWVBFTfCo5yAJWioAqAHdnfgQKozWiYWsKwDmBblU6DmAqFfszMQ+1CWhjUPYqEBqN

GjXdCn8W6FrBewsfJoCaiWQNYCYKXYuEByykjVnBiAW1BszqNd2SDA/lp1N3BeJ4QDja5AM+UhVfQUOUBwc80VPmzkAcAJIDMATuYE2qUF1FdQJUWsHoDx6I8GKCGgzgCyBXigLDwn4ANjXdmSgHgLAnAg7IJDjX8nlF6BiycANwmOxkjbxSCgmokSDSiJvi2qKxqVNTmmG25fgm7l1hjiw6xLOZzDuu5CeCkUsjxQ3CMNulMw35NbDRw1sN3Dbw

3i0/DZbCjlwjQHwbUYjSmASNsfBDnSNk1LI0vyllSYgwKyjao2zUtjVo0q0OjRjB6NUwcECGNjgKgJfiutExCai/IIrItogMNY0PNVTfY3mAjjehjONrjTNQeN6zN42x8vjQgD+NlTevwhNOtNwkuVUTd+X1l4sbE1GKCTXrTRAyTak3pNtjSw1hQ2TTdS5NbAPk2wwhTQgDFN5ANzBlNlbKi3VNJALU3BkDTU4njmpAC01tNJoh02jQXTSoG9NA

eZz5/Fm8Vyah5FWgeqD1JNWcBk174BTVU1NNXTUM1TNRAAs1iJRJVOFqpidFc1NKR+ryVbmevUF5uJapWBZ6AEs080mTaw2Y56zZjmbNfDQZQCNezW5SiNvIMc1EEUjZrIyNnMHI2zUCjTc2cQKjai1PNToC81hN+1O8260njV80mNZZf80WNQLSEABNtjTMzBUDjb9BONqAC42o+7jabKeNZcj43uoKLaC1otEVIQCMAmLZE2x8OLTE2awcTTyy

EtRlMS24AKTWk2otFLbFSG0EtL9B5NGgfS3cwTLaU11sq/Oy01NHlHU1JlFAI018tAreE3tNzjSK2q5PTWEB9N26flX756jPGmJpyaTQUZpWaTml5pYbmkL6c07hll8oJ9q/X5J8tXcBgg1lm+aUgA1T/VgGeFHxoWps0SuaQhivjhb3uwDuUhmgtxkRYoOkDjFLkOp9HlGIhMYbsoAZZIDalyJj3tSGIF7GA7VoNJMbZDA8RXs2AshvwH5pncHu

siACB9MedWMxM2Q6UUN7pMjVyFNDdWno1Ysvc7thjzndY6O3EfoBShVtTx7/FeWgqFZ+N4bA0qlzakCWQAuEJZHJAVQFUBqgdQNdDsMdQB1F4gfiKxB1ACRtPXEpYlQ4XIlUlYa1L1tVsZ4JhZnp9prwYqRKlSpMqU+BypCqbADKp5PpAANOxYQWZlhYKvBzXaUKqw5wdLYRF6xmRTuZ7aKeIEfnKAJ+WfkX5V+Tfn0Qd+Rl5XW2XmlrbOeXl+6+

h7nbc7btWhp15TmiNr147tARcYrbICAEMDxJkrZ4URFbxDe2QGLTIcDgULFm2D6pXEqwK+MxwMtyGQuamkXKQJZhcBAhexhdhwx06mV0G1Kuoh04mtqe0krx5RW1nxRjaZ1nalFfph16luHIfYaQGkOI5ARkFlZYQgyJNRSnVZHTaXRpZDQjXIR4gc6XUNaNZhHyBIGsdk2BqJnnX8Zasb8nF15xaXX7lZPtcWV1J5UxE117hhIBndyxM2rcRXAC

xU41s4rK0C+B6uJ0wAkndJ2yd8nYp3KdqnYV3M1thQiUp5SJWnkolq6e4XZ5GJd5ntBvmUyltuIol91gax9S0bZd11dwW8F91U1GPVwhc9VTuwHW1UaIstfe3v1wETFgvtKRarUftGIl+0wWIsPgFoWQmr/aTkAHQL1QhRwTcZgO8IQl03gqDpB1qa3PdL0khOQdBTAFVmjUV6SJBnyQYdupc0X7QRWOKXPAbIQ37pUVlplh/AYjnLrUQW3eR6kN

hGVR2PxtHdsm1K4dYFxMdbYYDYdhLXrSbcRbAFx3cesoRN291HsAJ0dJQnRUVCmcrQtEI9s9Vp0o9OnW5lolduPk6bWpnr53Gd/nYF3Bd5+QkCX5dQNfnKAt+c4Duhg1iWGxdnYS53+eTKs2E+F3nVtZGdLVmvBFVJVWVWkAFVVVVigtVfVWZGRfc54l9PSXF0+h0vRX23annT4UpdX/Gl3/OPXt0wxZn1Zfq31NQFSz4APAFUAslm9geGM9t6Q+

2/6RIv8KFZb7SVlrcPxm8DiQyimKQoklwDVmIGvXYjEq9oBSQHZ+YGWH3tZPdSh2DJa1ag3a9IiIXi0opqixrYFGGWfHKIkIBfYqQAgn7WrJdtmQWxpEgDdU8Fd1Q1GU9ghU9WiFLBekJsFlOIob7dTpfNlHdYdejXyB9NNc2ho+xalSXdXyQXU7lZxZrEPdlxU90V1s0VXVvdEKbXWsRlAEQMvYHsTRH+9qhQCXqFEfaolR9mnWzX6tc+vH3o96

JVeIKV2Pfnm49PQawPztIbcQOUlfhVl2n16jEp49A+yM9kr9r0Y/WapG/Xql5ZEILv1f1pSQf1wIAIgcBKkYyYFGIxzSa0mm10AObW+9oVrw5v9aHZr0f9Otjr2R+doHMkyulMYb2mlBHD6ZlQh0pt2TZ5HdNm7diNZQ1jFBAuzE7JzvdMUQAbKedC5g84OdBngknpdDvgI8GsVZ1V0E3WcpVyfyllDvKR8lblFA6M1UDwmUOo2GxCeJm1lMzVJk

UJbvMwMfd6AGkMZDWQzkN5DRsI7T30kWcnUlDiKeUPjDqKQHnOI2NYg2A97FfwNwlGnazXI97NfDUZ5Ojgn1lGpiYr7mtsg9Ykii3Q5kPZDIELkP5Dgw0UN718KaUMTDNwy8mCp2EjP1DhjToQDfg+wBQD6A9cc4gNSXQNAKkAOhbeDMAjwHfXpJzVffCP5WSZlltxd7Zv3M94IBRbK139eYPz48WM/Yp+BRSQj10TIY4OkgDPjwBhRLgxqUrVUJ

h4P21Xg2lGzdmPjsBNgDKLsAdFTBp7Wf6PFpcATZ1pdb0UdDfOQUSAP1WwB/VANUDUg19EGDUQ1UNffWFpEnI9qz9bRvsCaAt4JKAHwygKxDJAkoLbRdArEN+DJA34AfADAYCDoPdRb1UWkYDkhVgMxoDvYtlulyQ70gseIozx3StvPkolzRCw1hhCAtBUMBiy+gN+A+I9EDUDvg50KxDXQl0C3WNVtmYIPLDerQvWGJeneM4gj8CHzXj2AtY8PL

CuAFUD0QHANfnnQjpkV2TerJdklUoBg91UK1LoMlj8lZgwn4XAb5jqr7Y3XcXR9d0FLSiaAQwMh1gFD/a1lYxC1Qg3cdbg1qXv9Opd4Nf9uHDMYVZS3XoKdFaJsGkZqH6SiBV0iyZb2RD23Tb3+6IxZsnxDjvTD50NhdZUBUZgACO7sdUpmhOqLgyzt1YOU+B3Q84PeDpDFJbxnYJhxTbLHFqsXTl/J93WiZl1zOc90MDr3TJkdDadkFnbjd0LmB

7jDQAeMhgR4yeNnj3xR7F9N3Ay/18d8w8D2H+zoxmmuj+MB6M1AXoz6N+jAY2eBBjZQDq1I9YY6j2Z54gya2Y9uedIPYlFrZvXUZP47uPbFAEzGxATuYMeOJ1oExeNxjKgyfWxZ6jFUAtgiyAfD0Q81ZmMP16WRelhYWWdqk3phgz1V+ixY8Vmlj+KFajjZG3hYwuG0pZyg1j7qk1n8TioUqXFacDQSPLVCANvEkjs0V6lV+xzitLGQFlk36ADB4

Kog7Afg/SJW9IPvOPDFdvcRnzZCQ1WnAEa4x7Y0sVzKYRiyMAE+g4w+aEfwx8zPtyxHMsZUmxrMuzHo1rMkjaFMeYNjZdAhgKdVLThAaAGKaSgaoM2hngIEN+BYEt4E4QJg2IClMhglaFUARTmbLFO/QebD43zU6bEcwyygrGNTSgIrKYS1T8U7HyEDig0WCjlaMMISCg1oGgBSy3MNKzouCEo7GRVrPCaIeAM1KOUTlE7LXpZwYQA2ghUUMNOCx

wZbEoEqU30DY0EwJTX1QxR3pWmzUIitGuWeGsfAmDnUm0wOCblCsTTl3jpxQ+PUDT4493uBbriCns5bQzOrzNLAyKJtT+bN3ABTQUzsyJTsfIb5VTUQFFPssNU5cwsssfODPJTqU8tRYAGU6bkhg2U7lP5ThU8VPMApU6lMVTUM1mykEcUwjNWUa1Kj6HMmbM1MXMgM6LmdT5Mz1PJl1HP1NGB4oENOwAI01nxjTCOWNRdikFQsCR8s01Y3liJFb

rnFySxKtPVw608PCbT5ANtPBBrNHtMPNB03/GButME+jCERAG2IXTblFdOx8AoLdOFdGNUQwF27JgH28DfdY6MzQLo26PITqE76P+jgY+p12FurfPX4TGw4RNbDprTsM49ylZa1tE1rRAD0z/k8xCgzIU8jmGmEM1TMZs0M6OXRTKbKTOMz6zLPko5SUw81lTqM/5Q+UWUzlNLMOM6pRFTJBCVNlTRM9TNRAcM3VOItDU8TO0zulKHMxt1c3wkKD

LM5NBszg0y9kwA3M6wCGg40/zPuV00wgAizwLWLPjlEs8tMYJa0wzAbTHAFtOAwO08rP7T8IOrPHTWs2dO6zlFZdMtohszxh8y9w7jr+Fag2vDVRjwC0BwAWwGeCseeIIy3/kt4PlNqgjtKqnPED+RqlRFL9WJOv5sI2+DSTqRUKVwInqKiP4BjSZ9IaWf7NA3QUA2MByaTG8ZbNbxtmkZO7xKBd6nJK9Gk+wN4xpX5rRY3KBpDbhSyayNOT7IyM

qcj6ANKOyj8o4qPKjFAKqPqjmo9qOPAuo69VoD71SyqSjl+kMDZDzqDVpCAweLeCM8ZwDABqgfiJKAdA2KdDX6j4oyWnGjNHXDwVpK4+Rno13EQqbd11RXMN8DsE33owCdgFsCDpmgDgBvw94JXYwAeINgBcNaSdhMhj7s9p0c1EY6NqO4PNfRSxj10WxPE9x85UDOIjwGwAgQZBEIC/FAkzOFP5UI5/Nv1+qQAa/zHPa+mfA9LjqodOF/VWOWpa

k00ktJR8Y4O2OEGQ+HtjfvQMldjiC4hnILVfshbNgiQJVCYLB1V4XMaadFkgsjLknONELC465NB1y42aMcxFo/Q1BZgALC7wMD0PHDpw+TxDDIYKxA71OdVUMCZhdQQnjN8Yk0PTNX07M33Fn4/OpUZnS+kNHDfQ37z9Lgy/HUB5BYVK1wLMrTBP418yFourCui/ouPAhi8xAmLZi67OI9c9dYtrDi9XYvjaScdsMMpGvgHMUT8mUsvdLqy30tXQ

Ay0MtE9BCm4sSA34PQDLQZ4POAJAR9ZLV6DURUEudVTPfqlUgn9ez3vt4BkzbxA6VH8DOMzLk/bft7CP+SylGk6kvODz/aou4x7g/BkoNPY+SM+DOSgUkbeQ41TAjjntf+ShMNlqR2zjbI9EO295DY/HOlHk/IW0NrS+uMSA84EzyM1UQPARoA/zLS2stpPHAmbmxbDAlLAsZVo0sAY1KoodTE7RDCZ2PtiQCj29zRk13M+TRDnb8IfLvxh8+/MQ

Bktd2UmDvMkOYlOxtnc9aC2rpuboES0EOdmAZ8ZgUryGgNq6gCAACYT5tMeoDDpgv2ai2VTFc8cyRQ3pXLT9TH0JwAS0WqzG2BAV/HujOArEEau2NeIHfyF8dohDntyteoyAhNtSIFREgdBBiBur5yvmtPoEOemAYghjXFR5ixcEFUIAbq++C1IUudXJ9UhaJyCkE99POCQ5BMMBwmBVJDvkPT2Cfh5HFj03glkRtQ3uW0DH06QktDThnMt/TnQx

ADirbAJKvXMMq1iA8sOq77yCJSq93BprficoBqrhABquXMDM0et6rI9k6LZrVTfcxmrwfKHzh8B/G6v2rk1BDlOr+jRzNdzbq00D88kOd6s38BgH6tOgqOUGshrtemGuCY+uZGvEzvlPrlMA8a+WIzMWcMmtSrqaxvwwKFoJmvPrmOXmuv8da0WvCJ2AKWspg5a1DZVrqLTWtkb+aPWtsqTa7MGtrPzR2tdr2mD2sqUfa4SADr50EOuFrJAMQBjr

AMBOsGORDE+bW14VjwPQT6iwctYYRyzot+Iei9gAGLRi5cuSA5i/D0z1QgysMiDFVmIMtBGPZINmt/s10GBzQGiKLbru69Kv5tB6/Kur8iq0oFnrG/HLRXrN6ymvcJGdsPa+2hq+y2vr5qx+vWr36+Wzdwf61HOiN7M2LJAbqLSBtKsXq1bkMEYtCy0wbwaw5TwbUhIhslylbVGtxzMa+KBxrgfJhuJrp2T5vhN6a4RtZrqLbmtZ89/DLwFrFG4G

5UbguTRv7UFa71TVryvExuQ5Da9NOeNzaxKIcbwQFxspg3a4yC9rmOQJuDrw66Jvibo0JJusTQqUfMcTJ8w0BwA+gO+BbA74HiCEAWwDkgJAfiD0AdgAwGQQ1AnHdOHqpm9jknBLiK0YPwje/SrVorOqPvZALiMVw47AmfryYwNWCFRtdAmgMjF6TavVN1MBjteg0qQ2Gu7q7VQESyvWTmJEcISlVpTUvcrIgZdVfVlQBwu5gXC4Ji8L/C4IvCLo

i2IWw1H1SQsYA1+n8MgQ+wDxH4ARgH4hPg162kYcA9EPeD3AqA5e3oDUi46Umjsi7IXyLChaTLcR5izaO7Ldo/ik2zawPQCXQ22/ZiYAQwN+Dt1cILly3gwAVACShIlZYu4THs3H2ol7hQ4u2QTi74Wrbqg+tvXVCAN+B01VNmvYwrQk0/UYCokwiswjoS0WMIjJY2kXl0+WILo5qXXf/mJLhAdSAUI2boqXNjo3a2OQZvHbJsGTr4Yvr1FZI00V

9j1fs4zooOUd5rw7wQ+fFPANFECEo7sEWjsB1YgdgPB1gq/R1eTIqz5PoAgAHwbgAGi7qlIAFVAGXM9CSgSmVUCkE74AMBnDhQ8MNcZJA8fYjLN3UXVRii6w0Pl1n00eXfTczZXrnllQDXt1794A3tDrl0M3u5gre+3ud7Qw03UB57OyousVuNYUGLimANLuy7LQPLuK7IYMrtW+auxruLDbs9rt3LBrSZvGtPs8RNSDKcZZv+ZVrfOqz7B8PXuN

7S+y3tt7HewMNd7m+4CtT2NJTPZDAfQt+BJ410MxW272Y+8SO7OqQ9uSTyK+Euvba3CtBJAjeIJDGDI3BEz4rvAEZCS2SvepNFYmk8H0jdofWN3YxYu52O21GvaSM0rCe+DKHuCCPWalLoES7ofpJwIt3Nd+C6juELPK/Ut8rbk8XsC7wq/gNSYlYjYiTUhTVDACzb4o3n2iKEt3BoSMucwB20sZa+KSiS5fkA5VlsUaL+VitKWAjw+QGBJN5/rq

WA2N6jXYeww+QFnCu5KlO7nGVZhw4eDCT6BqI2H5Ygwy4gs1JoBCAcBHDkeUv0CED0sswaJo5AUs7+WIt/rqLz1NFALGUTl5aBADvgks9OAwKelSOtibCBBACs8w+GNQQ5BEEICs8wifgDaAzaCkrJA4bQ80TsaCrHw1gbaE2VsAIa/4D5lHlD7as87IFpiUwLLKdOjrCAIrnqNzDWLJcJLW7/IGw0R+4k583cGKAarb5RLNoKqQd3JoA+jdMFi5

g8LHwGUzAExASgabB3JnNminTJktdh2cfnHdh7MHJBmx760GUcW6YTEqw8F6ugw3pcts3jLBJ6JDN+daMuUDL03UPPjB5WPsvdhsUwMbrX4za0AS8h1mIISyh10eA56h0OKaH2h6OW6HY1PoeGHKsMYcNl3lO4clglh9hWnQPhxcfmHTh0vlu5K+W4fmHnh/mjeHo5X4fZA+bUEfwEr2WEcKgqW1InS5K07EcEnY1LO2Q4yR6gCpH6R7XqZHwZTk

fBAqRwUeI+ulMUeEApR6DCBuFR1Ud/htR+o31HQQI0dcqp2SXBtH04B0cbUXR3oq9H0BJrDinQxzY2jHjIN3ATHQsodSgJHiXMfXrGIIsfqn6CmkFLAax3G03HkjTsd7Hw8I8d+tIQCce2HxJ8SdXHcbBpi3HleaQAPHhxw5RcqpAG8emzc4EYAzD3HQUFieU8ofsy774HLsK7Su3KeX7tMNftTpWu7cux9Ni9JWPLslc8u+zry50Ef7Qc/OqyHg

EgofDwShwgmnZ8J4OJ9w6ElodMAOh0InpVJYBidPQWJ4XFtiuJxYd1iVh/qJQARJxccOHpJywDL5+OVOfUnmxzAA+HlaPScBHTJyEcbUrJxEcAShoNEdcnWQHEdznCR3O0CnQpxkezUYpwtt5HUpxcyyn8p+UeVHmvCpCqnSxxqeBuWpy0e6nHAPqcqHRpy2h9Hpp0+fDHllAfBjH1p5LOTHwsmNQzH4CfMfOnplb+dunqx86sbHkZz6f7Ufpwcf

LHRx0GdMApx6GcXH4ZykF4X2x9GexnxF/GevHB880ZArZu1yPJAv1f9WA1wNaQSg1lwMKO09MIRCPyKck9yHiIK0Hgf6pX8ApBC2yeI2DbA27mtzB+n5KcAgkZAj+lOqrvGdiQxHYOcDMuYdOZYHGWLH+1QuL7oB1vuIHRL1l2CISg4/uKIWA0K9SIYxb2X9KlSBnSR4UqQ7skIKMB2Xp9HzrWqKl+cD/k6l3RZuXRS11CnAXlyZpOXwliiHKXG4

UFfT0Waj/TaXCisUv6XWIYr1R70FJNXB78C6h1Ur6HfHsoLLoOCBwju+B0VcB3B+BEEutlmLpEN6NTt28re3TzsyLlUHIvNLSQ4x1NeHvWx2TkjJpoB2gIO/92zDgfRAvKlT/ZmeLi9AJoA5I9AM4C5g2IMwCjeVQOsr0QkoEIADAkgE+Dvgf3Tfs3LMfasMP7eu6ZtguBncn2WhSYZM5brxVfQClVVQOVWVV1VR30NV3fY53NOnvbs4PWdoCuzb

YwA76Z2gfjA8Zoon6X8ShefDBtLhe8YRddRjT2tdcgqrw+8OfD3w78P/DgI8CNlADnU05bOZfXDr5YzGsQ5/GJzlkoohdZiaEj9yOmP1MefYV86BzKNmjblRdguv5WwtumaFYsYKjWYOXN4GFdVh9Gp/AUC0VzFdJh7IBzf+XCdAldqXFTHRZgAPNx5eRXAtz5en092nDUgmt7hC5wuvYYTYwuxNnjbsTs/TPZp1x21pxLKq/YwpNMIN1Ds7GhWR

BSkUshawI8ayio0jJ4lqhiJF4IXtdLRYH6d/Anu1/eNVkguVySu6TZK7vuTd3Y9N2f9qHEUvx0g8UEN7V2DRntGCp7m/BcW4A7aV1LLk2IeNLHxCXvHdeOvIHbz3hg7nH8kM9GsXd/e/eN3dr0y4FLrJCbHarrpehzmUJZ5Qs0eG+sw0bRbYUyXeFbmmYNcXeOKVBN7Lim+qGH4s1/NeLXy16cRrXG11tc7Xe16Wf6boYzruVnundWfL1VRC8uKV

by1ZsfLOhm3eF3c+cXexzRzMxe3REB+owIAaZLlaaACQFjW6Ddu4zZZI8FtWHMoLZhH5GGrPWtBZ4jSH8AnANGlEtVh4IE11QeIPM/ZxA/u89LgmWI+Nc6TwncNcUrOS4VeeDLByVcErbK6djzc+HafEJ3VIhuHuav9w1dRpzk4HWjF2d5IcMdJ3e276rQlHHpoQ1zH01YJbamQO3jc6+rELrEy9Havjtxe+Oc573eCf7yVD12sCgtD0pQ93HYGm

fceGZxEaS7kAEYBGAkoDwCf0PALkipcpAE+D6AMYKQBNA10CxMWLC91YsVn9y7YvFGswkRPmbfszIOkyNmzoYCPE20I/MAdDyffUlQtZfpkLcowqNKjKo2qMajWozqOCXMm/bsvmj99CO/R1wUDwXY8FqYPGpLt3AhiSRB3z3GXoITo7C9kmr/Zijll3CHWXUvVMAy9DQVB03gsT7ZdV9qtyAsQPmI43Rup6vXHvIPVfpSZzcqe0BFc6ZtmkoIWE

QwQud+RD4Xu877V/zudXTvd1fMd7vax07O/V8FyDXBwXQfybUe5Hvi7/Hb9vCesD/vsHqsj/I+KPyj6QSqP6j48CaPZ+To96bSw/o9HXogyddP7ephaGw3NytaHPDiNx8PscKNy9Bo3QI29fY3Xof33lhFDkP0ed9GEbs19KfdF5+dcoG/Dnzl89fO3zNQPfPfgj8yGB2d+OkWHPPpYa8+emHz8l09hpu/rcycgCCISsQCQDZn+LUtRgLKQBkEV4

FJB4aapIrvcT9fnBEWFnuKXJ0pAbYkKJBHRzJf/Tz02SpB9ldPcYC2Iv39gnWbVB343ZM88ehk4g/MH4d72PgyfB64pYFoEcfb1PeBalSZY7kMYPVLee8Ifo7MQ9IvlqHxCKF4DFD4PbC8ToJ2j+uZdw9PDN1Q/Ot/Hw+xM2NDUzWzmzL1dfMusDPYOBJznoj7bAjX6Z3z7KJ0jyHN1AuYPMoiAxAPODXQrECOxHIu8HACXQvbNcvR9wg+GNVnxj

08sr1G96RNKVNpVY9zA+r7OdYuVN+AfOPkB5wvq4eO/sB8LFAAItCLIi1UBcvF7RZdtV7kHmO2SeWewYRPqK9E/z4BT9PHso8T3e4i9/7WZc9vNb+L0ZP9xuB2wduT+RZ0WOT4OTsOJT2SA/smlqDth34OzN10rcauEzMjZ2CyHVdZS5saW2l8andNXohy1fUd/KHzso13gaXu6O/T273NefV1JQDXbYHA/935K1bNB9czxNe0HaoeJ5lAkoL6/+

vB/EG8hvkoGG/wAkby9XBjej3fsGPx12j2nXifedeRe5z8mF3Kp80C9XzIEDfMAI4L5C/QvWN5s4vPuN7s6udDKkl1V9yOj8+XXcN5c9SAm29tu7b+24dvHbp2wo8XbV29tqZecL6X2fXNl9L0I6yL/GNrbaL2vDtYSnsenzgTSnfeIHzT/W+wjDeIakvbSIyUx4okMRCQyKF0nissvJoOA9kg9g5oBtJIezy9ODfLxM8D3grzHt1F3WcVdV+AYT

X6WWuHrRTbv0ksQ7yTjYPu8dPGyQd3zZ2r+aPSHBw0cl9DzHMUORy6dRcPJ1koKMPcptw5F+3JlQya/fHA++MvE+I+y+P0DXDyCcfjYJ/Opsp/n93s0ywX93thfVw2MNRfxX4cmiPfXDvsA9Y11NcHqOE+WeHPxm8c8eZKvsm9v7Fj9vd49DcFl8nD74AF971QXxvucZBXxcnXDJX1F+OPgtbu1rwdELgAJpDQIrh9CDOwo8NA2nDkisQ/j2qmvz

JXXdtO7EkwWP1gJB27syTaRQmr/5I1X7dioCHl7H6fIfUhQUhZwDILB3lX6/2rVuS1r1ivdSBSBl0YiLDt6ClTA58lQhkHMbRYFvSFpcrqr0MU9+V1RIAIAlOzUDU7tO/TuM7pAMzus72+0wuc7LC8WmYDrVye/dPZ74kN9PmEfe/EBouwK+SPn71PIIAfiMQBZ1i5s4DYgR8LgC1muYH4h0lWyEIJ7Pt+3V9GbrdvG/VWTXx4XVvhu1dHG7DwwJ

9PD0AJv47AMTtaN02sKyJO5jwT/mOPt9YH1XPbiI7/l/Ay7DRTIkPwFB7xL2oFp9ioFICiAtJgdws/8vJnwwevewr8ZO9Z6DZKUb0S0BZZYPY44dWqXDKHygOTYP+0/p3xD0uNavZD2Xs+fDcFRmAAUzs8N3X718jDsMLeDMcrGR/RN7koFsUpTOxcMuxf13RXdD77D5M2cPx5Wl88PDr/JkR/2X4F/3Z8fxCsd7/+yn8hgaf+z6DXenzstk/nrw

6MaL72tT+0/LWgz/pgzP6z/zg7P9G8GbeE7rswfJz7Wcv7Fm21+Nn6b0Fkl/Ufzl+x/Ff4n/V/fy3X/KDJu3rcS/OSEYD3gE6WcCEAmk3L/33l6Yr/3bzu3lnJY+KId9/zQ1bZAUWu3JfbUisMf/mEr535y7Er0D4/0fvEe7aPW/tRQwFIPUV60rRPZmQSBCy6F36EdBlCchC9iufP36dPIPRjFLz4tLEP6VASqahAL6DeJZ6BATVQ6OiFSihAKX

KHTIGCjnWMpPyN+SpyPqiDtdrYoVGPRhAKJoOUYKbdwQGA+ANgAwAExCMyV+SGgFORhyamThNKGAbnHjZTbc6aZHAWZTTP8SC8G6BL7VADfgZ5D78EXhG+IYjEbPGAZyfmRGgLWDmuXsp4VLFhAwAtoNiCYIZNJsj9nfNAgwP+QSyLWBJlSRpqAQNzAcdZix8YMoNoFmgcAPQE5reI5iiJVa7Te9YS0Ox50PbORTHKABOAu7JY5btDBNAgDDwX6A

hAgzBAwTaatHSw4TBStDkwQQBoAVwGLzDgDNoYIGDgU3KWA86BlrXXLnQc6DNoICYBde6a8ZU14/HGoYWvHP7WvPP4T7ddZT7Fu4SANAFqeTWCYAlKYtAHAHRyWaj4A7TCEA5NahlEgHMyMgHcAigG6YKgFNlGgGgwZxpSEfo5MAokCsAsKDsA9mTkA9wGBAPgF5oSbYwSK6azUEQETnMeYKwSQHSAuOCyAqmas+eQARtHOBfyTOSqAsIEYSJ9C4

Vfsq1gfNqaiXQGotAwF20dfgmAwuRmAxhhXTYRLWA1QF2A6uAOA/wEzbK85JApWazUcJoZ2TwGIJbwGIXQ6hAgwIGgYNIGhAxU7DweXKRAuebRAmc6xA8dITgNgCJA+YBgg1IEfQEIHNoBoCZA7IEPXPIGoAAoHnte955XKZ62jcn5evNv5NWDv65gOn7d/Jn41AFn5s/d8Ac/bVplnQ648/SSKP7AX5mbTEopvLe7T/NSoNAjAHlNLAGtAkfKs0

ToGAYboH6VTIB9A+OQDAm+RDA6jbUA2vS0AiYEMAstjMA2YE5AeYHag8OTKzB5grAp9ACA9YEAYSabbA0cq7AsL77ArICHA+QEnAytpKA84EqAtCBqA64H5oW4H4VbQGPA/1xAgl4FPoYwFTHD4G/QcwHfAqwFkAP4F6VewFloeEEuAgkHKBCEHAsIGBeApSg+ApC4Zgq85IgtQH7HNEES0KIEeA7EHxAvEH2xNwGcAIkHuAF5hkgsahZAjraUg/

IEtAQoFgHXtyTfSoAypZgDNgVXaYAAYCEAZIDKAd8BQAYgCv0bNL7AOaSijG7aMKNsAdVFA7n/SSaqGDA4KfNAAyKU77ALBrJp+cpgZ+bEaI+LoDJAbAAk/WBYCvP/6VPCz7VPWNQdQUlCEiDooADbB5PtVNQFJPBYzjNp58hOAHufJGqnvOjq53IXajPcGjiPXfwS7FkG6gBICsQHJAvDA+BwAUYB+IBIBQAHJBOOEMCpcM8DXQRICD/Re737I5

6j/AX4G7GMYi/HN59gknoSAZIBqgZxDzgPECRCHR5C/QSaSfb+Crg8SbK/bfrdQLcEJ+LdhkUQbKAIQ7zqfDt4JLG/qNmPgTm/Sa7GfZ975XSlax7O8FAA1g51IYDwsQqV64FZlYmlN35eFROjhRJfyKOH36/gkQ4Z3I978rTz5B/S966vUP6AAQ73Y6j/tDFpoNihveA8vk3UGIQw8DirnVyBqUDzXpXd/ju9Na7nrF67tT4agSnZuchuMrIXPs

WgHZC96g5CBvqF9RHpuR3XhI8W/qJ0IADBC4IZqNEIchDUIehDMIdhD+Jpz8DrrG9PZvqExQRIMJQa18yJnsM8SvJlQoTZDwoR7RIoY5DBvuN8ExnKpQ3MAFRgPOB3MKbcHIixDpPvqlL/lxCPduE8/iMcBEgE8ANpMpM/0q/9wGqroP/sN17UjQdw9hktpnn/9kGkVd7wVK4Dwg2Y8OtgV1Id0V50AmpFrMq9iGvhk1koe9YhggDA/r09VxuXss

IugBO1sApNRL9A4AGVBUAAAAeXgDEETAHvQpmz6ADZgEgWvS/QAM5qREi6dtVACAAFMIMynbQ+ZE7k4Ki3JwgMPQtYJ/hY+O9CEgATAUgWWx/UMjD7pDoUdzpIA5sF+gtYIEcb1ngASKAdAdmPyBXCN3BdVn1NyxPeBZZKQBy5HRUtYJJoawPMR8AficujpJoYADudq5LAl4wSvlJYIEd7gYyA7+IZQBqJpRbmB9ARANOUwgfXJ4FJIAjANKxqpu

sxOEtzD/xMYEnAJ4k/oC0Af9s2gNiniA+AK8xqpgLMLCL3NlAAtNeYpbF1AKzD5QOyAWyoG4vQKLkiQIeshYTY09ABKBO2pu1UAN/FgwXABKYbHwlyvvxa9D0BjxqzCg4QRUjApglW1J8dy7s9MvIZa9Jlja9JMmut7Xhl8pMPdCc+I9DDKC9D3oTwBPofKDvoXaBfocNQAYURcggCsdYEiDDWmhDCbEFDCBwDDDqptBB4YWnBEYf0wsYajDpwNK

wdEFjDBIBsx5wHjCuEATDfoETDlpp21/uGTDfYZTCU5O3NaYfTDGYTLD5iPKBeTuzCZziocuYTzDcoKEdXmALDCAELDXRLfwGtmLC5YjcwsNtLDVyrLD1APLDFYUbDK5irCPEmrDZDkQB/5DG1roDrCqQfrDDYbywTYUaAMNuLNs4k9BrYWNRbYbkdGjo7D/JnKtGTnlt1Gu7CWml7CfYeY1/YcOdw4fRlQ4bydiQLXoGYFkBRHrBh4oRBCgekpt

oIbBD4IelCUIWhC6gBhCe2DlDcIQc9hQS4UV7gm8azkm86zpvcGzipUmzunCC5FnDnoY8A3oR9DBZJWxeET9C/oZLNAYR3JgYe3AgzuDDIYUwBoYWgRG4cgoAwb9AkYbwiO4ejC0FA/ge4TjCOAP3D8YcXBCYRFQxqCTDx4cFMEEbiBp4TTDwFAzDIFBXJz4YvCw4SvDIQWvDfmBvCa5GYCd4XvDhxAfCAwX7Dj4YgQpYV3M1AXLDA3PXJr4byw7

4ZnCVRCWhn4T3A34XrC0kJ/DjYViBTYb/Dx5v/CsjjbCfbPbDcAGAjgZhAjXYQ80YEZ7DJGvAiKYbiAA4fMR0EWNQQ4f+cKkTetMEZpEUXpv9lhDABsQLI8QwF8NUmv5QwECBAYAE+BvwMoBiAF8N78i1V7IsJdOoL1CL/gd91fu7t/5sewzvhp91uPuDDauCIHKFWEq3lQd5of1hEfPsAEAOV9JISHd4HsSNbfkgtGiig8VEERwP0rK8qYOxYRs

lVBPGLACDIf79pCoBDTIbIFShKBCbdk+8DkS+9Fnof4oAADU/ENdAzgI4AlRl0BLREEB7wPOAugB2lbqHlCY3oZs43vQj+fvYt5kBFJvCpTdGka4s2LugAX4NdB9gD0BCAJlguoWMiP5jt92IaRROIdf8IlrlgTgAcBFwnygxIBpBfdkQd8ijO9W6MjEVIPSCtJqHsFod0kf/vQdslowcqnvJCzkXCMR0KZBY7st19qtVdz4t8BKQGIoRxmdValo

8j4AZq8Ksq8ipih6UZioABqvdNyuQx6+8QhDAOXzBy34EdoSmXT+xQLi+Wf0J8VdxEySX0BOK6xmWrQ0n2QUOn2QWV1RDQH1Rmg3bqxqNzApqMxm0Kyk2sXm5B4EPyCiUP7q0AABRQKJBRkoDBRlU3wAkKOhRkgFhRAoIg+3P0RRooJMez+zMe9ZzTiHXw3GHqK9RhqN9R/qPNRvYLui6AHogeIFGA34GxA+AGwAIAVFGeLxkgqSgmRG4KU+VKMw

OM2G3sSxjFIi7kO8etVaodkDf+8qEgalBzfeMDwkhbY2WhgqJt+skOpWIqP3iB7jEcRpVw8bkHpGCOz0gTwAro9V0EOKr19+KqP/BcQ0uhExWQB5kPlgPMQTBHADDKY1CYgZiOOYo50MoMiO5oNBCFhZZTKRLaEMRKMCxAHsJ+aDLEEwjgFQq2gCKBM6xKB8XzGaiXyteo+0dR4+zteoJ1qB/02X4l6K+B16NvRuAHvR6oKegdMmlOkVUV4eiLvR

FgK/ROQB/RYsj/RizAAxagDbWwGPr+NQBxepPxM+TINb+BCKCQUaOBR44NjR4KITRUKJhR1CMg+9X15+SKOpSxUNMepULXq7+zYRM/0zit0CvRN6PfR3cAfRoZSfRpABwxr6Pwx6GMIxZ2RIxba3/RQR0oxPzWox6/zF+qLwl+MP2SAVOxp2AwDp2DOyZ2IYBZ2bOz8em9gxQLwAro1wA7i8aH1SEAU7R24LY0bcUhA/oCbAXnBiwyAQWRbcX9MY

WIywDbw5I/PRSeD7iF6fbxixQHSEuZQFA6n7hHehT1l6WT1KAKWHzoKIAkuHUENsvlxvAf7npcuC3Kgb8EroZglPo2WNssgCEUUTeBpAhWK8U2l2CuwPzLwFWLocMtxD8MYFOwAYnjwHYE+ezhTyeTWN8xCrwCxKJG2wP9DxcTKB6xHwFfA/WMaxMlkI08QFGxQHjd0wWJvAoWPCxYWJUgWVx488Hnh4iHkOROlle+ln1jUnt0Bu+kADShlkwyJd

H4CeAlaeQhwPRar2au50Nx+Q0SAhOrzx0rvQecPZhBsd71Ah57SvBVvwtmMUGrAiaTv6Mz1miGyL+2hnwt+UjyghZQCugT4E0A74H2A1UXoAMABDAnmEWUkoAGAZ4FIIcABLO4H32efGNoRlKUa+WaNOehnVT69fToQNHx22e2wO2R2xO2Z2xY+Tzzw+8LwI+J2kSAp5E9Q/NnrwOJlDCHYChuozhhugvyQ+U31zAM32YAc32cAC3yfAS3xW+a33

ZxMXT76XOOBu3pkDEYpDToyWGvwHWO+uZGkW6a0iNxiimjCXz1IhmKOpuHzihs+0EbO9N0o8kPxM491Gks2UjUUHN3pUYAGqx9wjyx9WIGxg2JGcot2axPGkhI5WN+AlWKqxdeBqxPuNPIfuOVuZO2k491FZuruPZutKhrMQeNKxbWLDxHWM9xkeO9xdWJjx0SDsUAeNTxxWJaxIeMqWo6B/onWP3sHBF6xc2ObAheMAYjuKDRO4NSEK5kDxSQDL

xZWIrx4eO5uXWNrxs2LEUseNSEeig7xp7BWxgWImx0SGrx02JOAg+PmxStz6iepnVuJNi0M0Ln3MGt2MxywnBgxEhyQ2AB6AaP2jGASwhGL8FP+ZKK36pFChi3ohOA6iEo0IDzSKhWHiA3jGZGtFmZcg6L/Ivt2mhZIEu+4kO/+S0N/+s6P/+dtTt++SwfBhLmoohkCZW86CuRLujcUz6X6KBDymyz2LOhGryfiJ6NdKZ6Lzu9PiR83WBHgmVSZh

XoONelqMz+ccOz+kGMThVQLgx6XwQxm6z18Bvloq05UIJNGPG8XyKe+Cm2tmCOMgASOJRxaONGAGOKxx9Px4AuOPxxhON4x6aMKh0kWEx2aNExduF2G7y3zREgDoJuBNhg+BMYJaPi3aluNze/YIkAOSH0A9EDqAl4FKmWwCy2b0EeAv0NYggQFY+i4M2+jCm2+a4N2+Kv014iui8xgtne2RBwPciMVCi4UUbG3Lxu+Q+DIQCQC6AXKKBxUkKj20

HFvBC6KXeEd2KgF/XMk/FhfBZtkW8wDWgie6OOhJBVOhhkNexGkBeRV0IUWRP1AhZ4FDRbFSHuX70gA9EEIAVQAvqqY1wAnBCSSAwEeAT4HoApBCfAQRL8WcKKH+S90MefPyExKKPEWG6SN2ZEIrREAGxAXQCMAaoGugMKGmGEny2+Z+PsJ5KOPsEuhcJaRSgQ1KBB4el39AqkDSU/+SWR/XTFQfAhRiv+MWhIRO+R0kIQe86LWhi6IfB6kGRId5

CgJfoF2hcr3qgVFEHiFGgeRyBMyJqBOdKSAK6u56IkAle0AAD7s8NJ8CXQBvZ30MKERQkYaJ1S6DCFGwKOqK7onFQTJsPcgkcPFL75/Ru7tDNOEiiAElAkkEksZcHI1QiEkp1KEkwkmjGNxBkFi7RjFJQ8omVEiqqsQGomRKVoQNEpoktEx4BtE1NEk48Qkj/AiawfaQlY9MqGpvaUHBzbEkMTXElgkgkl1QyEmnJEkmGYw+Zb4uVTVkUggDAEMA

JAbEC33BA4zE1iFfzOOirQAaGzI/KDtgTVQRYM3qGQZ/5EHYdFf4i76EuKaqf/FsZ8o//ECo2DIyQ8z6REz8KnI/eKzGZLDMjSVHDjB4lgRTPZ3CbFbtgN4kF7I9EXQ2ywao7ya3QiAD3gV6C9UP+JoAd8BujXAACNZ9ANAZiCqKJkDPoTtZLALho8YOw6AAIFI7Dls0D7jHw0APfpcwK1pBQKYRC0FHJx0meBn0ASBYQJrB1GoWT1GonMOWKQQ0

AGqAQgGYAu1oWg1KIaAs4NoFbwJ4BojoWhGJPgB6AIMIU+JTwmAGWS1ivVUN+E+h+Nk2Tu4P7wReC2S7Dh2I0AOw0AMdoFroBlxWyK0dC0ImT8YMcxkgAWS7DnTCy5NYi6KmgA4KkmUNqIWg1QPMxSZpuT1GjMwGYXLQ0AJfB4JIWh5wC9lWaO+TJysPMEAGgBJQLKNn0AfAtAAoANrj4T+mh8dBmrHDESeUDkSbn9USdUDU4TQS+HjGSJEUc0fQ

AmSkySmTC0GmSHoLgSTyXuBcyZkdgKcWT05j5RyyZWSYztoFayZG8GyWwBVyZeS2ybDMyCF2SeyVYAJtv2TuYEOTn0COSgoPvpdcuKApyRsx1yXOTUAAxTz1k69ZMDNsOKeuTOKWElLRDuSxZEEd9yYeT9gMeSwkkmT4EGpTryRAooFFzMSCJmxHyc+gXyW+TUAK2S7Gl+SPTqgBfyVaJ/yYBSHmnZS7Dg9lq4OBTIKf2SYKXBTRHv4QKvqNcfkd

V9D/NSSqiXSTaiYyTGic0TWiWIShQRmiKcYm917swjJQawjrNmpVcKbCB8KZwBCKWeTiKabl0yVEBMyRRScyfKBqKZ5T1GrRTo5vOSKyfcdmKYgA6yWxSOKcBT2ybsxeKdkj+KdoEByeVthyaOTxKROSpKTOT9XqQB6qYuTZyUpTGyUwA1yfhtgKduTHWnuTn0AeT5wEeSsyYZSLycBSTKVYizKd3MLKYcxXMNZTXyWpTPyWYAnKS5Tn0ABS1AEB

TqqSBSfKXdA/KapQAqVoAmoeL9lhOsFckPoBJQMQAqgHAA6gGqBz9m1gW+tdA6MRt8RkeCNr2nYS2IRfiUEENDpkUd89SSaA3CQsiE9uiM9iSxYZvtiMEAHwIeAIj5H3qcSjkecTAAVET3vhlEADLuwrkfOhXwRpD6oK+AoEC2BFUY5MnsSGTFxs8i8fh9jvPvkT/DINcMxvRjQiZDiSiVPIWifrhPMHb4jkGqAM0tgAQwIA56IBrhEqQVCuSV7N

uaqiiLogMTNCeRDgVugB9AJeBsAO+BlADRDiUVDTZiTDTmek2BRLAjSb/r/VdJOVAFILMYNibisDftJJPtn8QzsIcS7SccS2CWESzPgACRXqTTgAahwzsMVhIWFTT7iWbZb7B7pd0d+DHsfpD3iU8ii9mMVUTAT9roSgCgsoABCnbbKDQA72TcAYmZ4ETqYX1+geIFAmcdUlAWEOW+sJOQpYywgxAKXtRdAyBOb4wL+Td14eCywzp7vmzpPMVzp+

dK1gRdPSGJdLLpqzktGhjkGujCyb+DGPDR3rxFpB8DFp2/woAktNzSMtJegctL2RxOK5+SVIkJ8cUpx4/xzRLCLzRcg3kyrdKzpwMA7pT4Dzpj1G7pxdPbqpdImJA9P5qLi1Yugn0qA8SXvArHFzA10Dih6pNsJJtK1JVwisY3Fktp1KIxEt3BpQhIkWg5wCUmTtPgQRv3f+FB3dp6S09poVMJpc6OdJFxP9pCkNEQpUGAGpTC4OqkNgJ5wDvI9K

HfaSqPz2GRPjpx6PDJuRMF2NpXkCHYlj48oFraZUmMIwR1vWwQBbhEOV5A04FgSP5RLgx8FRywGAso8oAlAJomlgHWzGOIvC7ENbVqQCgCTKTEEyORzHVksuWsA0BDGoDlDrY47RMRuq1VyhoHna6YAWA2gCkBo7VtiIF3bge4A6aSSW6pxIGbQSjNQADDO6IJhHNO6OB5iiaSJyUTW0wEoHhAsxxbkBgFvWDjQDO7bQOYQYEsoxABgAehAJgduR

LWfwNaOrCXYSSEmOwejLp0O8wLgE0wfRszHpY2QH8A3cGVBVlBrA3qziZljUaOs1CiBDWmpkdLEFiXcAaMSwG5g6Gw8ojgGYAVoBLQhoAMxl4yIiGfwRJVdKRJNdKgxyX3rpqX3RJv02wp86hoZifGyR3cBsZPRG7gqihYZqgLYZzLSMZQmB4ZfDNmoAjN8AqsmyBojOtEEjJTAUjIMAeZLkZKhyzsVjJUZQLDUZYMy9Amoi0ZHuF0Z+jKKahjM4

ZtsILBDlDoZ7AFIAljImmozLsZiuSbgTjNpgGwJTAbjIdEXCWggXjNUUPjI7kfjIfwLAECZwTNnQYTKo2ETOcSCZTcSMTLEAuTISZVjOSZJTO6O6TKuaxzGMZUAByZSzDyZMuQAwwUyYgR01ziQsU1g+hgqZF2Ulg1TITAdTP5gjTOZuwaJ72IVI9e9oyShk9OnpEtKlpC9Pqk8tM12aaLXpStKKhm9KYRE/3Me5UPkJe9IbggzLoZIzOgItjKYZ

EzPhgAYOmZPGE4ZczK6AvDOHsQzMEZKzJEZuBPEZkME2Z0jJ2ZmbHkZTeUUZE00OZA8GOZIU1OZPaG0ZU2z0ZWjWuZbIFuZJjImBjzIsZiTLGobzOCOHzMcZb0G+ZUuT+ZHjMBZT0GBZELV8ZgoDjg3pVouQTJCZELXCZAYJ1OUTMRZnCSGOBLNRZSTP2oKTJYS1LIyZHQKyZeLPRcKLOumFlEKZpLLwB5LLKZVLPSZVTI2oNTIZZ3MCZZziw3+W

KIfpEgD0ppBHog34EhRDEKP+iB3NplWE6gtqkZQ8xh/p/AROEEl0T8QFBZQD+KeABwGcYXBHHQASilKfsk/xZByaSNOwcGNpLD2HtLVKXtNM+cGWJpftNdJG1Uh2F7isYlwmleaAF9q/3w/Sb9j7R3vx/BJDT/BbNITpHxCTpmqLaW6ACqA6mIeBqAAAAAtkieWP60ddNHDSBpXTfjqzAb0IiAKgdBi67k6iU4fBjXUXUCAOUByC2mBzIYMQBIOa

I8wPuSTm/hyyI0bV9hWcvdM0alSuMC18xMVP8JMTKDsOZqJcORBy2AOi43qTaVk6UMT5wCGB9AD/szgFUAdtqMBroPQBVis4AjUfoBkgEm5hkWCM35vxAcSC6oDSpONbLOhwVvCfZVECMYTyMyikaSVA7bv6EfTOJBE6CONvguZAgEHPi3IozSTgC58R0eSA0DH3cmxgZ8cRikwYovBT4GarYjse6lclqh5QCVK5deOcAjwhkpT3FZZksF8AecSH

VdIe+yToZAMPiTj9LsPuRvohGSbofe9rIqPSBaZSSI0VEJjiFABroF0Bc1vRBSCDwA8QOdBagAMAgdpoNkqYRCxWStsjMU0i5VGeAKACBA4ADABcwCEUjacJMZIG4oXgNcBQLJ6gNwlOyeqnyhIDCDxgwo2ACQjyEWur8AV2QF4jvGaSoGSFFYKCT9ocfM8p0fyig1LQEPOatC9LJcSpXN5d0HhxoaaUBFksFZYRuIZzzpMGSSGaqi0CeQzT0T8S

sCSKJ0CDIyXAC0BJYIwBZqEmBWAJTBIci0BvuTBtfoO3xe5kaBnAOqta9EgRaYBQBQoJhd+5JOsNeFv14SU9MUKfHCkOV0yYMcCdemVQkWIvdztmdOAxlC9yGTu9yWYF9yfuVrB/udzApeMDzWprYgoAODzNYK6coefsMG4A9yeMDjya2njyRMJ9yIct9yWgL9y5KYMJSeZ5hyeWYQweRDzaedNoaMVhN+aScTB7hwTmMZABMuedBsublz6pAVyi

uSVyyubBh16Ua0pCb2C5KhKzc0RvUhiQSi4AL6NEkj0BSCF0BthHUB5wBwxiAHUBNAFIIZOWgIIRsLpIVOcIJSNVhZXCt5Jucoo78WnQPyLX4aNI2Ak/FIp5kTuzwREh1sRvr4QgPjTHvu9x1uc98iacgytuagzRUUopeFDnhAuVZM3wSaBsVr7ynMedzouaQyRKKaorgN8JQ6lzTFCqBCFwalzJeYLTpecPcygHLyFeXlzlecVyJTGryKudySx/

rfTO2ffSJfs/SxTCEJiim1yAnrJAoEAw5XeVVg8Dv1y9vj5pKQIBQfebsAPgvg8dObbTz7Dwon/jNyFkayiDwYBkFubAzVSotV3OfHykGb7TaQj5z0Gs/BM8CGE10a789oTuCngPcJTGPnzKPIXy1UfWEKGVIdfiRCdNYBeB02hajQMVajSCTajvITXcplra9nUYFCfXMFCJAASAf+cC0+mpJiIALALu4L/zQgKI8GIZBM0uePTOCRoxiAFlycuc

3zCua3zSub0B1eSKzJCVVyO2TVyv+KvVZCeJjq4EMTyJDkgOtPoBrEMPzkUPfZx+eWZJ+SxCbbpH46UPPyaDL7yPgqAZ0VqihfRA2AJSvr9tiZ4S9+QezeUXAzj2bHznwsfygCUwcz+W6TY1N5dSoC5Fb+XoIUiTgzWDLcIxsgYLQfpFz0iQXzLuc6Uk6Z5MzIXdyG4Jo1kyrHxWaMGVAjgDy0IC8yCKnpUjmLWUK6S0z4eW0zUKR0yKCRhSqCYX

9MSQ4KpAU4Krmq4LeeVnIrGcGUfBZzARQIgLHBT+VnBQ+c9Km4K+eZ4KsjowCfKskKaMTfTq+Sez0ud69G+QQKleUQLVeaQKO+crSu+dVzZSVoZaBRTR6BZrTsUSHMDJlHEzwMoBUztMS2JJwKviBPzwsLwLtpM6hBBZIhF+aExBbJygngOujfTEpBjwjIKbOUQF9+fA17vEK5EGWoL3wt5zNBVK4uoJfZxjKpDmBHg1wsOCBtgA9j90bHTWaQ0s

SHtdyMCbdzSZPIE7so+hvYUrxXEDdSdKsLlq8n4LiCa0y4OWQTghSiTumWiSfpujzoBegAXhZNQtAIQAPhSXAvhVXlrmCkK1KlCLu4DCK4RcIBY+N8KkRTRjxPmyyEoaRzyhXgL5eZUL8udUK2+bUKNeZGMdHGRCdedvSMqWnEhiU+AGYKQRcAIhJxnkfjm0aPzTgEMLuBSMKPefxI5+d7yhBVMKCOssSKQPlg8BA2BThInhlhRaTomHIK5oTDi0

lgfyEGkfythZtzy/Mnz94t8A1oFS8DufoK9BX6TDqgDFeFFbZECVEM46VYL5sjYKhVuQ97BZUA7stBSxqGfJ7YUaIexAjlHufywWpvQ9oOZGBYOWUDEeWhTKgaEKIBVhSMOYhjHRc9SXRQOALAZ9lXYmazMjjmwFgAgKURdGKtaLGKNgQ4BGAVjzZqMmLTEDRjsgsRyx6YSKcBRULFeWSKVeRSLyuVSLV7q14NaXSKZCa0L6OQwKz7mvBroJ2k/E

A5CCQOwKHgGPzeReOz3edPzHCWV4Jhf8Q/eaILcsC2BNVIZzIrpwQFknKLQ+bvzbuItyJ0V/8jiUoL1Rd7Sz2YnytRZeyIdlh0N8HFhaHEaKThf983wARoECakTGrm58v2WQz3+TdzCfg6KJAC+tAWq2hWjrxRnXqTBfRQM1/Rf4KWHrd1ARRcVa6cusUObBiwxehyoBW6jIRXdBU2u+L82r2ceTqmLg5q+LLAfBLPxVm88IH0173lv5cEWGjSxT

LzcBfgKKxS3yahTWLyBRvTqOaL8mhTQLaOXQKWxe0Lu2egBsABBTWIP9VHMFtRVlOKBsQCGBvwPgBroGwApiaAElwccEvrAOK3eVPy+BTuCveZ8ARRX7zl+bf8MTAaTqRDSAfgBUxTnO4SG8Gihn2XwxYKD/oEOmKhb+mFwluU9xICtHzLfjQEVBVsKIiYwF9xcu9E9vxYeUJ8IDRVTATwjKiiPOfZMCkdCbxZ+zbhRD5i+QlyP+faKQITzSagET

jixVgKCJfXzZecSKm+VUKqxSQLyJZRyUqYwjGhSxctCRRD0ABfNa4tkiegOt9MXPL8ZIJCRxJTwKBRT1VGUGOLhBSNxvMRIh4SAaU7QFVA5FBAzt+csjlxZCJrvtQdeXnDjp0VpI4+RqKUPKdi+styFp6JRRAuUaKXdJRR12AFyLRcqirRaGS3+baKL3m8iUhtflNRO3wEqLAlSCLtAfxYhS+9v+KRmp5CgJTQMQJb5CJMv5CGImCLm7pGLDCGHw

eeRtKPKFtKQCMhL51KtK7pTdRNpdtLRHrxFWCQgypeXjVopURKSRSRLyRYlKyBclLKuVRLaRVvSmxYGwpWdvchiR6N5lO3BJADgiP6ccFipTtJBxZJLtpAILhRZMKJxYLY0AuNxuBZFciNO/jLUjsToKKsL5BV1KVufaS1uVZLtxU6TT+UgyTJiwE3dJ+Zpkvey41IR1MqKYJOVuYLBihdz5pVdyHxQ8KnxU8Kr5CFRzKdhBvYfmUG0Gm1pZYfj3

jlOs4Se5DwMe0zgJZ0yHUWBLUeZdLm6VLKGYDLL8AR6yFZWAkjZcrL2EeTIlZWgBZZabLq4IrKLZaI8MbhLzShdgLCJeWLCBQlL2+bWKGEWvcqBTRKmPC0LYZQKTvnEMTLoJoBsQOqN1zHPdORYVLnABjLhhUOKpJfoJxhXjLxxSIL/IpFhPzCcA39GZIb2EJC9pfKL5uSuK1hVKEtxaezmZcATWZfb9DxfxYOwKIoBDscLYeFZYv4OZJuoM/yBQ

neKwyWLKy+ZgTJZSKIQIGHJu4HTCWponBWjubK8oL3tkaQGLDpcAKE4cCKUeQ3S0eVdLN1kPLfACPKBWNzRx5Y7Kp5TKzYNMPLUAKPLt5Ykzd5YIgaMVd8Shb9La+f9LSiYDK4pZWLiBT7KKJZrzKBdRL0pYFxg5TPwGJUMTCABQBame+Ad/kOyCpcf8ksLbTMZRJLRhYKKgEOnKqpWKKdOeCQn8WpB3hKyEmpYuL2XjwJqZUqLluX/i3OUX4mZW

cTdxRoKr2XXLnUMANlFBujcouNLwIp/AuNPxC32THSP2Yeju5QtLEuanT0AJdBlACyBUbLUhlKiEBhEgLRBhCdN8AeCFoeZ6I1Zcw8Dpaw8ghVrKQhSCLMKZBKTYtBKIAJwruFTVoUwHwrWYTizfAMrB80CIr5YvTzKgKorAgOoqwKV0F+FYG5BFborA3BkKuIqBD4KZgKa+WUKyxbFLSRaRLqxWDKuiYJj3Mm/KoZeKz6RfySpQWHK2xXGlMhhc

QjAA0B8pU/pQFTJB/RCVjlFCf0cENygVvLbST2JBEFku11W3nIhIsI/ZzIOGlrBhNCpFJTLruFgqOpZsjYcXTK8FZsKCFUKiEMrsKSFRSM8SAe4IPNgyuio8Ts+X4MwSCTdrxYQ9fJZnc7hb3Lz3sBCqGd7w5DjdS/0GgBnYcQAFAPY9a2omK8xVvKUxb8KABSQSEeUdK3pqAKk4edLGBtQSIxZusQYGMqPcpMq5VjMrhmZ6K8yfmLnpaMqeZkcq

VAjyxTlXMrcxd6LuaNhLQIVW9HFW7KopXfLPZfFKn5ZSKX5dSLQbD3zWiF/Kj5HDKANL/KapFE57oF3Um0fHK4lcFcElfVg8lOaSZ+WsZubFVBDgBkrc5aWNIDDsZ7gnOzmpcUrMFYqKylcqLSVhZKnwpkx+pR6l6lQeKKRm5BMoucLKFWntfSS7pfgIzSE8AwqrhUwq5pSwrRZYtLhlVoZ5AozzMjmdTOIscqwgn6zHQaJpujk7Lp5Tgl9pWa9p

FUGKgRehT5FWEKm6UX8GeU8rxVWIBJVRC0rGUmLOAWFA95YYqJAKKrZqHqqzFQME7ckaq8xSaqlZaI99JtM9nFR7LXFcDLvZf8rwZZ3yteTKSP5Y2K+SXRzwVcEq83uow8QNiBzoKwLzoOshexfxAEVfWZ2rpAT8XEfZcOJtgMVekrv4Jkrf8hKLLnO2BFhUyjClTPFiVQHtS5TTKKlbgrNxfgrK5YQqWZbUU2ZVK5uoJ4w/FK0rRxnfy41NyJsF

t5Lelcwq/JR59g6oKrPsQPKdVV6KKZGFA1jgYBQYG9APKFMF8Knad5QMWh4YMyY/RTPKlVR5CVVesrq7idKwBcnCG7vrLtVZUBLVTw1Xud+gqKgcxp1RtRZ1Vix51Z21mqRDjEBUeqx1TkAJ1eerYElerFgEAjb1UurRHtplstBST3ZQDKflY/KyJZ4roPr6rfFQ2LoZUGr6JSGrWxWGq14BkhsQMpw/YaxBIVh0AkwECjdkFfRtlv4sRJU7ywEC

7y+RcnLU8KZzKpaKLJxUpcgySyjwuQZKkKJy8TwYj5oFuXLq1TeCBpetD0Gn0UcSHKiWVct1M+bTTs+XFgFvMg5o6TyqouS/yrBQFLS+UMqh1TaV73o2ir5eyzIIe6riJV7K/lUlKvFVRzUpQHKP5UMTX6VUAQwD0BROX0K0ZfhqeRRArSpcOLf9P1DYFeRrcVSkAJEGRRjnGLZ/8mA9ZBWWrsFe+8NxYfyWNYATNRcQr6VSu9rLHkqSsKeKW5U+

yuNCAZ77J3LtXCLLrBWwqv+epVMAPjANjmaszGWYAdmO6KExbmKkzi5CrZLPKN1fPKkeTrK/Iahy91S6ioJZhzEtclqTAqlqfWfmhMtTmLHuUmdEBYpxqtZFtmpHVqoJB6L5lUmd73mEUFNQSKlNYBqPVapqQNXULRWZDLINf4qYZd/LYNYxKJfhwBTiJdBSCLcQWCXHKYldyKuBVjKoFT1UPNGRqCZcsSNau/BARN1ivrKiZvghKK5uS9JVxUqF

J0ZWrvNdUqa1bUr7NHZLoiaIhfFA0hAxGNK/NKGkzhNyq0iULLLBbFr5skwZk6XkTnxegBmpMaCIcmXJOIrUdmeEwBrVboBn4QmiD+EwAIcgjqp+DlqV1X/p8tYBLCtcGLkOSVrwJWhzdlRVrrpZDrJgc21YdWIB4dWjrSAEjqs7GIBUdXLwMdfTqLwM1q1KlDr+jjDq5ZHDr7mpjrGdSjqYyazrMdRzrRHn4tXZdfK3VcNqVNb8qxtb7LkUZNr+

PjaVQVeYk5tUMTb/J6jbwFUAYAHUBLoGYSNQLCBUkG1pamQ5i2JOTESpfyLLNdJBcXPtrM5Q/jrxppdWqF28TLmCEDFcLdAHOZd8LOk9GbrFc0sY5cMsdB1rxjYoinnYMjwRSEF3l5zBpRxrJEB1Bulc3LFVe5KqRFlRICQpKzBYwqxNV3K+1U6VJNTncZNeKFQpfAd9kSeyPldLqW/iZK7tYtCkoUBr3FaDLxtRQLldXfTWiEn0EPkk9obm3qk4

EMSWgGEJ7wCkgzwPBTh2W8ROCIRrttWVKZ+XtqbNQdqdOWRQBdCXhzbGogi1eyhLtW5r2pQ5y/CSqL1hb1LGZU9qT+dXL61bXKKRhHRteD6hvtf99PSN9EudJcKAdf7VhZfyrnSqDrbBctKtUQoFvuZDketQLr6dcjrjsPgAIctjrfxZp88dYPsCdWqqQxRqqIJWTqlFZVrOee/rstZ/q5eN/rmdX/rkRcHMYDRDkP9ZWhMdYgaggMgaaMWqSfpY

pr8EbLqgZaNqPFQ3rKJVpr35T25A1SRNAlZlT5tcsImgEelSAO+AQIChNzoFsB9cI1JiJNiAB1lErbIhDS5OTJAPdFbriNVcJSNVPqHdTpy5sf/kaNejTSSPwJvttiMAdkDt7OatzBXH1KalcdjjkQfrz+XXKmsqcAPghny8GgRpZdKlhotfaV+lf5L4uVJqwdZQzC9UPSagLCqBtXgj9lsQaH5XXrn5T6r6hX6ru+dQLe+csIzwDkhroGeAqpFT

Y41WnhzIKIbsZeIalPpIbphcsSAKFcAXaoJAN6DrwXNWy89sSUrSVevrOpRWqvNWqKfNY6Ta1fvq6VfZLUOCb8RuB+Yz9cnqXQPTT/MdOsM9aJqLBeJrgdcHVH9XaLg/glq1QLCAHzq0dPDs+hskSCoJaJzybAj/o4eQBLgDZbwQBduqtlaVqAoeGLydZusejQycdTgMbC0EMba2KMaFCegAVjX0bvYZEEHYcMaSCN9zRHibMy9YQa3Dd8qRtfLq

yDYrqeiU3rgVZ/K6Jc2KNdSEqJAA0AeAIwxzoPgBh2BEbUQlEbzNdbqU5R8F7dQkaZ9RDFVJTtI+0RAh9uHdIRIMbFaNSXK19b4S8jZvrmNY9qVoWxrtuRxrfGJSBeLL6SzxbUbs+V79IENfEZpcQygdffqQdfFqIdRABAAKDk9GXkOOzCou5yqNE9zVZFBzR+YIQH1ykgDwAgQGbQ99APgNBEZaZgSyAKBFFkqgWUobPjEVqVDPIExqkV+OumNC

8vVVS8p6Z+6oiFlQEZNrwpMRrJvmV3oM5N61G5NBAHUA/Jt1oQppFNw23FNACgGC0pquVIom1NzJvzQeptzFBpovWxpt5NZpsFN50GFNlaFFNXZiYANpqlNW6FeVoUqsJLhvwlQ2uuNcuuA1dxoBVdYs/8KuuaFLxpDlQSrg12hPQA84EZA4wCQ1ahsYhx+Iyyel2iNO2on1EMXiN8CsUl66JBux+vCwhKtY0CJpaluxIVF7mrJVOCoKNGws0Nu+

u2FdSpj1h4uOAgSijANRsMF58VwEe3D4OFhso6Vhv7VYxQ6NS0r/Zoq3QAgABlyZ6D0AY40mI9Y4mBIrk9AFoD3NXMQlwTiAAVLFg4wHWZ4EDgBowowJQwbIUtw21U2BeU3qy61HKmorV10tU2gi8rVQGinUQAZc2XQVc21sdc1enLc07mytB7m9Fw3wQ81QAY83sAU83nmvY6MndwVYi1QJVvRAVfmn80S0P80JBAC27mrED7m0C22VI81jILPg

0EaC2XmuIWqAm800Y2OURSpxUAa6M0kG24316+40+Kx43+GkFUpm2bWhy9M2ZSiAD7APxAcGs8FLRbADTKPxAgQTADfgKoCPAWa4gQDkW4amwnHBZ3nFm8fWOEtlYwK2SX4yy4BZKnfBO66UqZYI1SPCN3Q0gAGKgGJE22c87wMa4+APfSlWF+TE2AEmyVJ817Vk0yMAiQN+BKkHjV6CKTWsrCDyoKic3qvWLnbVVEi2Gp/Xzmu6ihSn3p4S4ol1

8mi0eGkGVeGjTUpS/2VUGpx4ZmxuBYvC5LrqfA3raxA6DCoE1iGySbn2ME3qWnzG9dW4ncKApX1mktVtS16S5G8pXommPkVyrE20q3s0Mqz7WSWKjXcy0wVtq9pW9VI4Bz4gWWZ6lo3Z6qc3fs9PlBSro10miqqMtFmRRAXECUAZiD3NGA2PHWPiCAIXmawQUCjQWC188pYh+NFxnNiIDhrlJIWTUVCrOC/NCdwUCrT5EGYsAdtkIUq8ZuQyRXKq

pU1OyW1H1DbWXPm3WXLyjU39MqTBjW1rTJySa0hAcHndzNAhv6+a1UVJa3yYgGBrWluFItfxpQSFMCHrSip7W7uAHWzyhHWj6AnWoXLhzc60oG+dSfWia3qY6a3/WjgBzWw2QLWynnU80G2rWq82qAyG1bW5WCw24nLw2mBRtrQ60wKFG1OVNG2BTDG00YrgYg4ksVRmqeS16qK3eqmK0Qyyg1+KtKm68nen68943oAFLIwADSDvgPOBZASWl1oy

0SaAHoD3gbED8Gz2yCGqPDeRVgTOfYlz8WIHw/0osbe827ishaXQ1ShBCsaJbGuKLhSMoZUhXaq8IeanPzOcwHYYmzs2sa+q3sauuXhpALHVGtdGLs4k0coKsK+MYTVNGm/UQDVo336xOjrkQdXl8kKWOGoSUEGwbVEGu+VPgZrRgoNUDfgdhoh4ECBCABoD4AIYCXQBoAa4YTgMWzYbloqW3TyHJBX0PfE8ciI0fpdgin4syRGkhV5x0AQXjcKG

IiKYH7vAP+4AUHATsGTrqX9IdFXa0pWVW8lVGfHqUq2Io021PfXqCmuV6GhlUgxarDqQDPl8a9tVnsMdE9W5o2A6qO056+8WzmoVVGuKTD1HAcCCgCWbQERWTi8CHJowUXAvoRpqn2kwKkENdpEEf/W7S9hDjG+81ACx82E65HkvW9U1vm6hIfmx+3n2idiX2yXI32uWgmBeTCtNJxKP27uDP23yBDTcICc64OYgO/NBgOsZAZ8SB132mB0P2yCp

P2l+0oO0R7WjC40p2q43C0jO1dALO052icL52wu3F20u3kG1+VMWwOUsW9Kl0GxkVV25IBngSQBFFM4DLXE9K0tKoCsQPbbfgdZ74AKvnSW7W0LsDqB623iwG2nPA8leihwWU/qgIa9iXYZ4KaWv9Jc3LI08CcPnlqhVCOpcyUl65QXUqrQ2ecnQ1lGt7VW6UlA68de2cBGAngRZECm9PwbX6nyW9qga3f4GO24CWk0J2qDCDXCCbc2yKW82xcTp

2/QCZ27O34AXO30Oou0l2rYBl2+M1+y+sVJmrtkS/RrnJACgAwAViAtAKS35m5tFNgIBB72fE0SCwbk/mF+xqO9yAXuOgwIK8J6xFdaQgUTDgnuVFUYK0tUom7lEGfaq0WWsx2/qokZz2nYUNWld7fEcCg1hANLek40WYwA3ojcck09KpAk3Crx09yw+0F64+33cqQgcMoHJnJdB0X2rB3i8BMCVoB9FQOxgHItGYFtrfZ0KYUtAqUYkA1afMoYw

XUTwS5yjNUt5i3ogh2ssJxKN6Z/hEO5gAXW3LVEmlZX/CwMWbqu1FPW0CXE6vWWAOjHkM8tZ35lDZ1LHM+0YOzgA7Oneb7O2Np326YEsA0516Ec51KYVmhXO9xq3OytD3OmcCPO6XLfKTMV15G/jmUD51IOrY4XWh9VQu7vLG5TZ0EO0B0Iuq+1IuvQgou/cAmgk50/NM52voamS4um50GvDo46nB516KEl0vOjZhvOyl0IS6l1EEC633vc2Y6ZH

m2p2yh0RO6h1ROmJ0F2uJ1MO8u3ezbXlQa2g3Bq9i0MGuVSH7GoBqgS4BE5KSwdYOeYcAb8CjhGToO81qpZJUjXFOq1ClOo20Dc1R2X/Kp1LQAgTgGAMR3BULmYhNaRp0P3bZy4l4n9N/RVXJcUWaEArGStcXPSJ0Dt0aAqFGqy3FGhPl1q6x32W3DjH9W1TvtCHjtQFy0TO7gC5yv4gJ68O0eOvlX72ovmyS3x3DWuwX+O4NHKLZO2uGoWlhOqh

00O6J10O7V2MOhJ3MOwFUvOVJ0BGuVT4QAYCkIOWnfS9K1R4azXW6TPBaqAWxXCYwavAKAFsrRjQLcX/KTctLBJ4PlB/AMujlMf/KP3Ue05G1E1VWilWmO2q2+a7E3aih8G/RUCh0iFkLSo4c1GCE5zoPC4VeWl7GfE+bKc0/uUjK2zbTqkXiUVSwGhAe5rsAo52mg7TG3qxTBliEM5nHfMk2NQAA4pPskmTU+h4HUh6UPSLq0PS86MPZk0zQWNR

0PQ81AACikKHurQJ6uMqsLolO5YngdcR0BsHrLfQ3cF7JsrvZAyDo2YhORcA38I8F0qscAd8G7WQcjSa3zpx1bVoVNt1qmN91pmNwLtOlzQ3mNF0vBdEIq3WgHrXKIHu9B4Hu5d6Lr/R0HoudxuVDOCHoeayHtQ98LrFiVHvUa+nqw9hntjFuHrY4+Hso9NzHUaJHsZY5HtVyhHoqmkrtS2G+VZtE2yY9nTS2OlaHY93gCSRKCm4916wuYPG349q

OVpdalX7hhECU9QSTA9sck4BaLpgAUHqxdsHo8p5x109JnpQ9MmBs9uHrM9OXr09KHqs9NzUI9dntI92OTCgFHuc9HABo9bnvo9Xay89nzt892PM49xBCsZPHpC95lTC9CrtAhOGql1lxo7dB6nCdkTtodedr7d8TsSd3hom1Itqm1YtoCVxrq3utXKlG9EEqkBXHTIziAicQgH7+B2xDAbHiqAvXvBpsnJ1tfJXddijrKd/EhYElTppE/rvF02j

qkUG2E+2pXmtJztvBEs1QoQ7tp31ntuj13tsatQHkhY5ou5lR3P+++JqUUUlk/dKBJ8tPjrdqjbuf1LePQAg138eZDvbd4VrVdw3p7do3oYd43sHdCZppFGtKGJygD4JIEHogAwD8QZJPydhUsKd8jpKdsYDO9PVQKigFDxQfrs0dHu1m8a0gRIs1njogkN/SiBhD5rTvKtN2u0m64qPZD2o9t17q9tOJr7NXGmctYzrwaEl1klU3FmdlovmdRkP

EOYxV/djwv/dDcB6NmogGNagGxBjJqlxrACfQOp0BgjACJArTUWYiXsrQjJuakCZyRt1zvRg1Mmths1Hbk4DvUAVvqkBbKifQYprq9QOTsO9azZAMEm9sEoFa9rR0NAVPOJA2ICdy+vtCA4MCOtrRwBalgKAUTAFsOXuRqZYMA8R+bK/JFhEDcmsArBYxqANCX1ANROrOlMnp2V4QvetIoi19Bxu7guvtHK0fsN9cfrLYpvotADLEt9HAGt9Lxzz

4MZzxdjvtthBx1d9kgHd9eMGsV3vo89f4j994KFagfVGbBIfp7Q4ftIAkfvd9Bvtj9BG3MagLST9pABT9dNvcRxcCIBfOuz9EPLz9OxunkvzGr9n6L19PDRj9RvtaOJvqCALfot9xzpYB7vpt9J00FdDvr6oTvv79OzqH9nvudNXZh994/vUa/vqn9KlBn9LzLn9sgKj9l/ob9q/oT9Y1A39W/u3hKoF3hu/uTW+/skah/otQEOPveIu0R9kZtVd

nbvVd3bq1dGPt1dSTqV103pHd7DvFtDIslt8GsqARgDxAB8DxAzgAAprEHoAWwCjVfKEwAfiCztIYDZFzrtGRz5mzUlPo9d1Pq9daKou9vrqu9TPukNaAWRIEIGUUkiCOER7qu1c73AWz3uekUC2iE73vMdXZpste4qjUi9pXeNWMO8Djqpg2IXPFVwCI0qnIpN4Pzv1tbv9d9bqh9j4pTp3NMcNlsrwDYVtvlKPo1dI3tid/bom9QtvA1rDp01V

dswAWdrToXvhdlQ+oXY3OlEDp3okDI4rbA9PvUd1ToDdOqED56ARYscPEninPud1f5BFKJ7pbN49rbNQvvTdIvszd/Tp7N33pXeSOzlRRwraVVMEDS7VtLdtoAI1Cr2nGVbp7VNboWdb/LV9Eso19qAOZd8LoH9zlNj4aXkl46AeIqJuTGtgbhS9fVHoAkZVJyGx1vVrZTmDiXpuaSwe9yDMA2OmwZnhZlX89aaEptIQNj42wbD9sgIUAGEyD9lZ

RNyA02mC8vDkA4wYOOmsAtA7QN9KSQSwA1oAxyy/qfQgMECOXCtgS2wflA9OqQD6ftQDZbABD/gH61KsrbUn9put66rutJdQ2VsxsoJEBvL9eyr4eWzswdbLu2DkwbVEWftZYGOTmDmnuxds1G2DG+R9yqweLQ6wYS9j/us9FIZWDJgX2DNMMODLXpuDZwfWyoMEuD1wZn9GOXuDwQEeDnIZeDGTPvkZaA+D5gUwA3wZNyvwfzQ/wb8A0IeeDIIb

tEafsFhEIflDgIdF5+8vqBIwe2duIYmD5gCmDhIZmDd2RJDCwZUojIapDJgTWDxIbpDpoK2DywatDEHpmBrMzjKHHoC9AYJn9zwYuDEfquDLdQ5D/IbjaQoeeD0ZVFD7wevKnwalDsAB+DV/rlDeCAVDQIdoZgoBVDO/vuBGoehDoj2M1bbvwDFDsIDqPpIDOroHderp5JBrum10GteNJrqGJDQB/Kt4DYAOSDxA34EugowHYDLtCnpz9oSA50H2

9L8xkd03jkdJ3s9dyjofZykukDGjuxW19lzGilm1xMimA8BAmlKveL0d4Ih/xhjpxpF93Mtl7pntfTssd57P815RuKgwAxPYQdJclSICcdsyRC5c+KZpekN5VSvqyJsYAKiLgfFlbgYr5PNP/IRRL324VL70Q3r8DaPoCDmPuLDDQu01p93oDu+mk6ZwEugOSDYAI9Nxe5PpIO99jP6PoknQBcscJVnOAQ5ZkuwhhsWgP+nAMnqFI0Cl3OwevG05

hcprwxQfadlesF9iguF9H3tF9X3vF9DKqzw65B5xgXIpi4Wso0oXPcdPQevD37uDqAwcfDw6sqAextX9Ovry2A+UlmK5krA+TOTWfpy3yO6yyAjgBTKmGNbKnayYp8waeD8uU4ZHDW89vrXyR6jSsZgUzGoqkbpZyAYz9NOvsquEHxgtgKXhbMOiOOp02NEtFCZRobMAXCQtAzgq9AwmgVVwnq/taypANsisXl/9tfNkAvfNyxt6NAkcmoagAwuS

001Wt7jEjKh12OIQKkjzgBkjcpyjZoZQUjVZPkxNIYMwakZmozHurAWx0gRNjR0jCp30jzbNTDe/uNDwFRCAv0PSRy8KsjrRxsjp0y8R6Ac2ozkaYArke1DuxqCjaxpCjQkZNy4UdvWWLCijXRxijEoDijCUbkjo5xSjSkbWDGUdwi6kc+deUYeaBUb0jFqFgSqoZQD9wOMjrZVMjlUcARlkYIqtUZQt9UfsjnESajTTRajxxnr+LYFfDai2R9eY

a/DBYcCDWPuSdiZub1zxo4d83voNePoVwqMHSGr9G/ACAB3+l0HvAKZW/AWwAJtggchp7XL7D+toHD96UhAqQcZ9Y4cd1L8D1tJkAf55qmM5d0iBuxcuMtnqkMdZlrMtugd6d0ewKu24YXtewo4133iJuU0MT1G73P1HcQqYb9jB9MXOPel2GcDcdr/dDhoCdF2CujVX3hxhEs/DxAd7dpAaLD5AYeNlAZejQxIQAZBGcQLQAZQgaJndC7Ap9/Yf

EDg4Y3wFTpHD6Qe28h/VXCi/MbMzqBNJGlzyKxEYqtZ7ont3UvUNlkr0DdVuojt7r6yhIlPcHcWl9/33RQl9g/ddgZZpDgb6Dosu4j4Ot4jEgGxt31txtf1rQATLqM9LLrGDlbPmIQQHwAkq2xO8UFsjrLslyTiQcgHlFJdJgQ0j4QEE9ABs14Bfurp3kdVNvkYUVkBqAdm6wDjnAJ+teNpDjlHvDjiLsjjdBGGjTbSBgLvsRdycZXAqcZed2UdY

9EXuDmZcYRtQcZmtz0GrjowdrjjRyjjDcf8q8ca/9bLtbjWIHbjRnu7gGca+dPd3BAPMbCpfMYBlAsc1dQscLDQQbA1Phog1VAdejNAc4ddAcSt0QjYgdzHIIyAij4ba03s2lwGc7pB6xhkFhGjKteAsBg0gFjAKilAje2teBPYwigPcdYXJlCpCiWgYgbwF9itQ4JvYJZVv9uYWLLlNVo3DxMadJXgZSFpRsGdFdv2Fj9iPDtoGVi5+uJlNDggo

r2L3dG3nKYqJiIZX/GEiDGAPehkOkCEAHyA+QEU45sk8AFAAUAuuv/h+PMpgXzp1ppIAJArsUelmZKGApYFLAIoBh9IoMV8otoEA7gAPAlii652eGjon9lC8akuKQMidmswIhN+jwmdQEjHSFJcH0AcFQo++OkPgWIDkAFHwjQYQGvJnLWsASYHDW+uWLAtanHtgHKgA7cBvo2OTQF6MjsTNYHbgSNna+cOFIjWgbXDWGGhxtMi/CY1To42YHp19

iY8TmXQ/2zInp1kCz8T+9Hp1gSYlc9KgfC2QDjgIEGCCPzSFE5DxBgrbSWA6pyZSTeKdGpifsA5iYJtOW1+yNiYo4psfCTKMusAkMEqT7tmqT7ibJ0kSZUqpsdiT8mvHtiSfXwwSfiTcvBqTniaiTtpRiT13AJjJyFCTcvG6TQpGsUKSZCZCAHSTrAEyTribMhOScNM+SfeWRuwGudKEtwiVtwAFhJ04QhPvA+wHogDQDOAmAHiEUABaAUAEwA50

DSt/izLixwUbA4TwKStqEQcnBFVjo/L5KCCCJEAZkX5NGiD5CujUQ9t0BuB8VUljqkYxRltCiUKZ+2t2s+kakkZIMfI7GgBP0lwTpr52bsGdFCYIhXvVGe1IBQTKtL6JmMCN2DkpXYMYEXcgXOpjTQdwZQWJPYUdO6Dczs9jyvqDqHYESA3xMGDWhhSxkvQD12TwWxdKh/oypEgM/pl2AoJA+Eu2Nb1SKjixouM71Z12ixlxglTbup0cBBA2iegi

0MgxKrtjXIeuHAHfAaoFbdCsfRltCpSAe9kxVoikaNv+gTlWxm9QDUo+A7KwT84IEAoSgcvi+sfl9hEfSK10egTYqGhToUWxp8Kc6T9MuBxVQbY0oVrxTAztqDmKYa+e8i2Ty9LFjcVpABIXjWMJbsN+JhsYMVjDatZCY9jVJscDsaAi1JHFcDvsaGDEgAPg2EG7gQwC+5uqzN9JiFQd86gLTnMBKgJaeb9W2zCgb9qutucc1lx0sk94mTV1Sxr4

eVacmoxaY55paYtA5ad3AbQs1VGJL8NbDtNdVcRaAZwByQo4O7J/xs4EkBnj1VFBPwDbp6qmwGYUFqazV2C0gQgtgBT1Y1dTnhLy6R6a9TKFAJpFjpRTyroFp6KZDTKiT3jIz2fDJP3QTHGp5E7BkJQ+HX+8ElmToXMpE1EdrTunjsZTurizT7MfV9wqqkwgAGTCTG3gZ//nvHMDEPm8T0qmsA1lho1124EuN8PCDOpm+g0jpvplpSwCOJW/8iEA

a6BPgcGp3Jsn0ba4yDUoGvxLePJRlY3nTmpn1BbpsN1jQ1wlHcSawzWbDRYOP3YHplYVHpz1PLh71Nnprs0Xpv9UCva9M0RpjG96O9P/Y58ON/KNO1WVDivsYZhnc3DyKuTdF04V8BkKhpBMx1/mZpz4zZph8O5p0DMiibEOJx0EDH+4zMD+6DMIU2DPf2+DNPmkF37yVi0V+huDmZnZ1DphiVYZ42KqpoCPoAegBdib8D4QWnjzpqkCLpq9jLpw

qL3hxwmBMJ6z/EIpaDxTCOftTjO8xuN3upnjMwpgX3Ju/jOIprJb+poTNybEz6iZ22PrxhLiSZu3BbJrlFPpw8WnAGrDKQFq2J6w910xvFATjWrN0pxX0Mpm8PEiT+B6ZvuUgZlZ0NwdDNtRiAD9ZppmuQ5tMyK1tNyKpDOv7KSioZ+dRDZ9XUmujzPKTXH1V29qJ+OEfDbIILOBMFvCbuBfXe3K4RaS6LNp0WLOANAPlmc71ABhY2ofCRLNrx5L

PRMVLMnp76RZZ1wbIpwNM3uuy20rUNMCYtzJbJy6B4p/8N1Bz+7ncULUup88X8Q44BJBiLm9W3e39WgDMoRIDN+OvNPoAbY0DZ5HPDZk7CjZ1VX5xxDOzembVOZw9WnGjDO700nUYhgCMJWzi1Z8LxZdAGABikILNXALlChZ0XTjcUJ4f5KLDcKI7MXYOLO7p67NQJw9PQph7MIp7p1IpnLOvZsX2FZin67ddYb3poekbkP7O+Gvs168DCNfgpoP

agEt3sq/rH9miHOpp64VtZ793w56H2BWqMlzZz/ZQZhVVO6kT2IhsT3IhrdVtpmiIdpgKNoZtzNzaxbPrGZbPeZ7Fw5IGoC4AdIzyPedNQqdggeu+biA/N+66c/FCHZ7rmLdeXrW09Wz+gVgQM+7VJSCw2N/pM8gQp+Q0hRe7N8Z09NPZwkaIJ3cIi5m2PvZpoqfZ0RPhpnFOoyp6M6OEAHvwf4BYJkHNB2/ARvCd3RaZ60V65nNP2G3rMMNDhoC

xdWDIVSDMiidhpZRrvN5xPQM/O52lrqjWVjZlEM25kUB25mbMyHTvN1snvOE5jerO5yu1u5+iAsAU+A1AA+DhmqCNkZ4LP05qpaM51dMz886Ss53iTh5znMP4vdPCQpLO8+lyDp5zQOzvTLOC57LOz2gNP4i0KwFZgvOGWIvN0I77M4pz5EUB6NMMhW1Bv2NSDvp8/WZRBdNsR+lPppr2OwGXTPAZtlPt5iQBG5q2V9ZyzPm58fOY58bM+RmjlvR

lDMQuyoBoFuQleJ4nNaq/1W4Zzi1+o9vjHEbUZBZ5RQ0oQblkKxaBRan+l0uMPPHZyPOc9dWzp4DzQfmHiw68U2wso5PMt/SFMP51s2qSTPMv557PC5j/M8+L/NGB8mPi55q6S5qTPS5+WOyZvJyR3QMTHkdPbeaFTNZ8unD+mMIa57X9NUJ7TMIFzrNIFniOI50USDzFSirJy2WICguKB+pwuYFjyOBCnAuT5ibM458sMHq/NMOF1mjuFpfPkTF

fOUFsnNa0/HTnQTADejS6BPgEn6xB9GX75pdNH5iLO/6cphAITgsc5k7NX57nN/S3nPHpjPOPZmQvZ56Di5Z3IJop1BM3p/gYlZv0hbJujEVZikYGcuBwUp1oMq54LlNIEvD/a6t0cRny0dZkhMI5wzMYF4/1oFkfM5xsfNwZq3NAu3wv4F4+PTZoguoFx3MLZ9EMUFsdNhBt3NnAA+BPgAYANAdR6AF3fOIHePBZFmkbwBUyCPsnqryKM/MxZnI

sZB3SQ4aISAUKyFi5Y2UUiFrjPYxj1NpZnlFIUZ/OmOoXNv5iovTPRQsNqorOTm8nEl558PntJouBa5dOwGdcIshJlawEl9hxZmZ0/p3os65/ost5/TNt5yjI5iQtO8ASHJpI9hP+5Y/3dp7uA8AQkuKY4kuNpmHnXW2daKmy3OPja3OzFhzMEFv0iz5vEvVpiks32qkts8kktsWtM0u9bh5rFnDORFjoXKAfYCo4ycnygWnMhZw/Mrp9Is3BAQX

ZFxbp3F9WzX5hNO35hcOAZCQulBqQslFv4uv5zcOAl20bAlw/XiZ4rNYp9jo4ptbVaFivNsHKxgna8wMdF8/WpqeHgtq92Pa5uAuw5jz5Yl7rPIF3EsjFgbNjFnHVm5zwsAiryO4FguNzFub2EF+T0kF4dOrF0dOilib6cWrMj3gboAAjLMO6piEYeKU9g0jVor+Y7gs3BSbkqlw2w2p6lDlZL4Bl0R2n5Fm+WFF3jOP52ki/Fqe3Xgl7PyFsLhm

l4wO/58EvYp58OFEod2J9Ng74aBPAQ5ot215l90HgYBr9msOhN54HV+l6TXx2uwv4hjaMSUw6YTwAbMrl6YNrlv+IeFhEPYFwF2PWlksz5xYsAcw0MEhhyOSNRiTrl82AClzDNJl7DOk51MtRFgYACLZxA5IAYBu0/oXJFunOpFhUvM5+BAbcMstSa2lx1llPNsou7N854osC5w0uyFgEt55qx0Yp29NWlqXNcx0n3QlxPYBiTrMpKCAtB2+4Tlm

cUpzl6k0Lluw2f8uk1oFxAUhl7ONhl/ctTFpkszFvAusl+Ytxl5RUJl9zMPlzzOu5xK1PgBiSSgDgAJAUgCRp0jNHFiqCrulaR8MMBMpy6/DXF9nOqlm1PCQBii0GDn3NS0Qv2jcQtQVpss/F6QuwVsotWqBCukx3Q3KF5kH41OosXR4Knl55czgycIaNSkH7tFl4THcjaTVYJ1MtZ2aV9FlmNWFwYv65yMnyBa1UzbOj1j+28vmqyNiNRjlQABw

KszrJtOTFmzPTFo8uMVk8vye3yuhVgKsUW6DCJl8gvJlp8vNQtozwEWXhhCCFCylg/NikNIsAVjbBZFrhQ3FuSt5Ft4tal9StFFzSvfsFssWxmvl//E0ti7LstGVi0tgltQulZnFN80jCuocTy44ZJuXK5odBWWSpYl8sRREVjNMeVrrOLljmMoF9AAUVtSpUV9+0TFv4UBCiMs/2ov1/2mMu45zEOzZ5YuCl8IvrFqgtRF+gBQANMnJAd8BWRX3

OfEWRzLGCEBxYDhDSQNLAyVi/MgV0rLh0R24dBxqUYx/WrvF27Np5jSuSFngRfSGCutlv1PwVjstBpmoNiZnsvdV+os4pyCOMWyg0OShbxt+V4nKZxEsEcL37vGQhnM0r0t72+AsDF2aukV4KV2Fp9WXUZ7ks82aiD5ilmoiFrUnq5nmvcq2KlMxfOymouV/OjasAuyMs+FuKuOZ/atXyJmvU1lmt01ruCHV+8vpVx8vxW58sdChFSsQbADzgd8B

dh6JVHFlIsM5/8uwBMqts596tqlogwal+ys1V1PPioXUvtJ/Uvg1pqul69svZhzsvVFuGvIVsNN9l6XOssiytguVDgmqJxhFeXCuTlzEh4CITUwF1rPel9rMkVgK3eVk3PBlvcv0l0T2F+rHPF++KusViWtE5srX+RrzOJW7hBsAfYDq7SZRBZ9PBKOsZJt+Epb8SdPDAVvWtIgalB4oNSBJ4WrCeeWcNJ5gGt35lLPA1vUug1xqu+pgWktV/StE

KsmMNKzqsS5h5aw+lYRQHWXNvy4lODjMCjA5wwv8a4CKTjbbgXhwWW36oOu65xAtDFhashzdwC3ks1WVQnnLr1vamR16zOeRraux1natMV2Mvsl08tr1ggAb18+V3lpOsLGxRWp1zi1CABIBjAK/wyeILO0ox4uFl7xjMvGfmbAZEDsEDnOP2WvzOVngtuMCXSFecEjmlOs1EHK1CvASQXHOD4DFLeuval+/NN1s2st17SsQ19uvW1iM221+e2GV

nuvw1/uvMswiRDAFLl2lyysffRNQ1eZ0vYJk3rAiIOmVuyHM72hetE1n0vYDIkSvsAzOr1rYTelcRmTUBWC95kOTmVfhtrkm6AY+FaDs6WT4bE8KI7sEZYQUOeWH1qMvY53av+FzU2elERuSwARviN0IsVQu+taEM97iJuasIQIYmHROsMDAXACq4edMbEzhT+KNaTtXAgREwUss9Y7+AnAbarCF6Q05K0rxzC6Btb85zE/wcRDchD4B/fG7MN1y

Ct1VkGtwpzBuW16+Ud16GtvZpQuENh2tfZxXxbJ8Xn9VmIk1hdxThc8csl0Mau72J4BMhKavE13X62BLys3Q+QI5JwQAcAZABCN+WDptfKmwkqLDrhAtUeuvbPrVyY0x15Rtx1gWudp+dRVNxpu6N6VlS1ziuHxoYmSc5xCsQM4BdiWX4gKo4s2NwEJGQexuGckjUdgL4iyuarOgWSwPSGpSBXkPJSfAUpgX9bYlP4gMRcWFEDBNiCjgVnfmoNiJ

vN1qJsGlrBvNVnBuUWk9ntVpJu1FlCvqFrmNSOlGvAF9bCYhFpg6Q3JvtNn2uafZbhfAVzTFN9ht4yUpuOqMmsjWv2N3Q2Zhvct/VdHfvMWUMWvIVa/hdyMENqh9aPJR9k7JBa0DdxgZnItk42tAtFvz562L017Ft6I1aNGRgltUXYltNN2XSjcldhtNph5R1i3NdNvmvRlk+t7VvpvpwslswGylsD5hfNfQZhI4t+lsQh8aOEtr4OwAC62kFxs5

l+kUuZV96lyqAtPMAZxAJAbIaXyw4tvEQ6SrE4aWAGEAzM9HkRcoMZJgMjKiiKBPyzeQB5/4SqDeRJd1+Nk5v6QA+LPEzEyhNlBuN125voN+5sW1tutPNuQs21mGsvaxJsBaohtGPEhtw+wyLD1qiUOS+SZVhcpiEmylA/fNoOY+PbhAPHovsRjEvuVi4Sd2leuBlyoDrS6lrHMWQGwJUkNliEltSYEtvDiWpHrUZSMwestBZx1au/lm1DlMdlvU

GTlv71rwuHlgE7PW1RvIZs+vye2tuWK8tudHc0OcARVtpV5OuLGmWtZVy/SQwaqJ+IDsDPzVWsGthZt8HMCj50NyUz8/E0h+SusXsbxvi6Ny5chdRAQJmbGsaSRv50Txh+Y6kClMJgxXN1qU3NxsuRNjLPRNwNtW14Nu4N0Nu2S8NvLvSNvdE5M6kN4oUUNt2t1IEXSmc/3nKZ67GqZ0JgX2ZUjb28wu3i6av5tolyFtiOoNwfuEMnQIA6MmKaHo

bmhNx1z3wSuyMXlziJfOhyp45Mtgu+o5oYB8VtbZP02rm3wDNySTTmAXZ3mVMwAIAO2hnBw+Whh9JGzUFcxctDPikdjaPVtgD04dnLbJsYMEZABYBEd+eM/M1o4id6YN6MqL0NtTIBtib1p0d6lsawRFmEgNIKNgxeFsd7tacd7jvOU3jv9HT/2CdmdqS5JTvGhltuqy5ptstgkhdtjHN9tnyHtp3pv25+dTYd2ai4dqbbkwmTv3AtONxinU62dy

8sUd1TvUdjTumwLTts1wXLDwCGB6dljtvQelg8bEzsBMymTwXTWCWd29xCd8Xhhd8jvTttr5aGFVsZV+dvqttoxdAGng6J2v4mzGGp09XMvANTiQUCSpYVXK4T75i9zbcFiFpYfK3WqALGPV1BWYquE1SKAQUdt1Pm8aKpaqV7ky1V19t3N99sPNmJv/FzcM3uS9NVF/Bs5uj7PJN4vNO1rmN4i8vPEQ8m4+FRPYpKQB7ORDJQ86f75VZ4pbyKKF

uEJkvClQNq3wtpt02lDlOZPLlOh6oPVFY1rohclax8HW9I9ORxTUgM4KIkCUg4II4Q8pvTSjcBZIspilxDdn+hkaTFZek7KhCSNsCip+D7ipqSjkfIzwypwXqY9+LGXGNJ5wqa3H9hZGzAuVGyguOD5qKFfF42CVPU9lJ0Sxqu1qeKoCV2Za6/Z78sQjNS1xAOrBWMRqUzWDyL/1n4B/GKGI7AVyBbuusz6QJfU35r1szdr4uOcsGs+p+BlLdnPM

J85BMJNkEsqFw94I1i6NFi35tyZ9bBmqJEgdFahXjjQB4cEEGLquRs4HvSch3diUgAGH2M4lzDuVAQAAwpPylAAAikdTYkALvb5S7vdNzdJZ7bm1dszv9uK1/LbUbeOc97bvcTry+Y4riQCGJZMGwAziDYA9EFwAMQbmbw+uXTC1keLVZl8UsMY8YsvuF77fgfxG3Arrx/R+iJVuqr0veNrnxf5zCvaUFSvfCJndbebEba27f+dSbOKdwl2Psobo

iA3CyKxYhTsaDt97b3dD/LPISqMt7842t7GryITsrnyDT3ZETFewgA9lKLJp2RkwsfAuO+ZI976AAX7NVKX7eaBX76Xr3rgAoPrgfe2rwffjrlWs37PDW37ATNX7kfbCL0fZUsK2aaJdWgaAIECErSRY57B8ROElZnXInUBTlJ1WpQgva7tS3hbACfk/yxLkJc5TDCYhBy35U3YVCMver7Amc+9P7bV75pcA73iq2T4Ut172hbqQf4WW4xgw6K4z

qRLOdC4I20IV9ZBdYb6NikoNvZPYULAw7eyRFEhZN4apoKKgEQEugxADRhfofrJdlPX78/Z4axgRYBzA6uDbA+nAHA5bJ+/dWVvbd5rzJf5rbJYCLG/d4HTA/CAgg/YH1wa4HQzbIH+jZ4eCMq2AB8CX2aoDYApPrf7GWU57j7HUg1jDBz96SLwAA4ObQA9LrTqHF7cSzArYhcr7ptY6dfhNJA8vYQH1lob7dtbFzxlYkznzZ6rz4endYHaHLPqV

xcul3u92BXMDE0q66ykHj8M0tH7dS3H7OP0n7dvdoHKQxI9TyUAANKQvJQAAYpNwPMh48kch88l8h773XO5IOGK3y3T+x+bChw8lih08lShzfWo+yM2ls2M2q7bhAa7L2w8QCLtDB+1yE5ZXWUgByrRIJWYXDKRRzhUMKhewIIC+zPrXNeX2ec9xm0G64O8je4PW64r2jS8r3tDS83r5Y32AO833ey9aXnwy7KMmxlFKzC47IsYnrGg60H2VVzo3

gEyiLe2wire5QOJ++OyADHC3Q6xU2pMGv3j/V8OOa6PmOmwyWeW1IOqh552OSw3Afh2CqViy0OXc20O3c/sBoSaQQLsLeBxeb0OR+RXXhjFSM98I1nU1cBEY81YP8+8AOH8Vf8lK6aToB8g24B9BWa+5bV1h/X34m6Lnv8z4G+61G2grdLm9W5gP7S8VA3IoVkcVVEP8oqShhFOtiXK4kORDskPj3qkOQuekOX9YAAe0m4H0o7KHUVcP7MVf7b9m

eqHm61lHTQ9v7UI9XziVqUyUcVguOSBkzwleH1cIzRQl7GW4ipFhGCyQmHgA5F7tg/gQdLizwVWamsaCrmHBRYWHvraWH5SpWHH7bWHcFeW73g/W7SFY+bjtYOH0ufgpxw/4F8qMXc8dzT20Q4I4eSsYMZlnuHgc0eHduCoHU/beHnRue7wxcqAvDaYAojeeg9ZK6IYzNUoQChJZ3A9zH/pS0b3cFYpRY7sZJY5rAZY7lH/w+jrece6bx9ZVHfDw

rH+Y5rHirOLHsFwbHxIB3zqVfYrmo4iLstaYlEAA5AQASa5wEHnTAw8H7ww/MHeWSPCVo+sHNo+vsmRqNjZI+cHiw58TT+e9HtfepHCCyQHdI//b2vVQH/+efDiFv1dfWTzogvcRj3MsuHntQZQN5EAQiEeYbtOCFHyBJFHGjjFHsbv9LthezHEgHBHW9cqAIE9hDI2flHEg6UbvLZUbIfaHbsg/n7N/b0bsnpTrXFbTL4NXmTkoE0AA5ZM1Rg+c

Y9tx4sVWR+Aow+AT//bz7Uw4JHOnO+iaKCaYzo9JHRtYgrQNfdHe4+bLB46pHvo42HW4b693Hh2H5472HWvcHpXMbwb/2cT2QVxrxNTouHsY8z2JeF+iP9cFHDw7H7Tw5SHLw/FH5TfYVEAC972Q+eSgAB5SZ5L1Dh5I+9gbNaTooe6T/SfPJIydo5zmswZg/vQTo/tH1k/sgj8+smTuodmT7SdPJSyfzZo6t39rUecWoALdgjbBPgc9ooj5FDAU

Dxi+84LN4Rrd6STAid4jyie2j/bBUObPD6W8aEqV7cdMTk2u7jpN37jhbuft2JteD2kf55s8feDC8et958MM1m8foNQLTLcJlAdFaSfKIOVHRYY8ikJrbpfj0go/jgZh/jjMdzmsOsiiSUcUXdRr9Tii5DT0M4jT4k5qjoKsQAMafjTgafTT845zTs44TTiKu0l8ocwToEdwTjsfzqBaeLT2ae7T4afIT4Zuzt++voTqIuo40ghQooQB96/41xDj

xhdQESRnYT+yhLQ4Crj/Ee2jpt4929sC/VyXualivsZTqvsUjzwf+plbvCZ/LM+D+ke/IwyGCTgev1jH1Phj6SW+ifcJ1Tn7WEoaMBUgJMdXh06EdT9zhdTiUf/siACrSsyi0tDclXkj2FMQM461k86BdyJ9B2HRiRVoe8DnHKlQYgbhUQUvqtqVAmfOw4mfqNIAKGUq8nNUyme7+/NA0z6cC9sBmfFyZme3gPmnjFmitctg8sVD2KvAjmQfqNzo

hh8QmfoY847czs8nkzvmdUzwWdqnYWf0zs46MzqADizvmlKtthGld6WsP1qItQAe8BQAD4aXJrlEhTjYAEvZixANi4SQEgCv2MXPuTDmwcB8/nRZ4KSwZURfVpTxifXNn1uzdv1vzdgNs+j3Sskxnief5sGfFTzbtBjlJsQl6XMwhtked9kpgx0dixYxqSety2YznN3BoJDxSdJD5Seij1Sf/j4xsBlx3sSACHK/8pWUwbc47FHS0RNzs44tzqoB

tzv31aNFspdzyHIFbI5gVpqTD1zp52urC44dzvueQ5DsSTziHI9zlB3NzgeeZsGkuQT5sfct1sewTnpuKzsPvoAEeemq2AAzz6efjzw+fNzuedpNBefEzJM5mzwOYWz0ZsM9t3OFyJUk9Ab8D/MOcfWqBceoKvnt5ZSOgvT+KcbjkOe/TsOfhNiOcejmHFej3Kcxz/SY0jkNvID7ssCT4hvMjrmOS6uGc+abbDrhcbmPj+qdymo8gsWdIsj90ufC

j8ue/jyufdTo+1Ft4CfcD8CeXWladQTgPuKj9zu25pyfyeyhdXzoUuN0srtWzjoVFFdfPzge4jmVnMsZZNEenaDEfuQSAlIrXZtxT32eEjt+NgAzfnOplwxPtps3MT4BesTrSvgLw8ecTqBcnjoqfq9vweWl4MeoV2LxDAYvVAFvXsZRYAanYUChIzp9mKBx4RSavBfJjpSepj54e29tSet5siuItqacyjsQf/OxRv2TtseOTreeC1vqcHT9QeoT

udscLiceQwHoBwAGVIMMa6eiKAXTbVW+zeRaKcn5kLw/zyRfUT6lDFeJjSnYBZIERrn0zxGAc/tHccsT7KdsTtRccT2OcIFLReIVmosaLUytCTwxckZ5BcN4FiEaINNv7Q1bpImb3H2WVqf4L78eELzqfEL3GcLm05CDU7geiUw6jeL7mu+LuhebK6fOML5RVTL+8IsL46splhdsz2SQB/ASQAzpzAC4TuFUbavxTZLgjUAiD10XFk/MCSDJfrjh

/FfAVgT4kMBC7sXgK5FOuuhz59vhz2XtuDjwdZ5yBfHjrYfcdPiclTuBdMj4Dsxt5w0hDk5SB0uPzMpu4n3STBeF4cUgcCKidol23EDL9qdDL7GcjL9ScJaiHIdUuCq1lIeciiXFfcUgoVhAZefo5mhc81taeVDjadLLyrXErqTsHU+CpkrkJfKt4UvsLk6cdCgYDDzS4gh4bMv6ttiQM++SDvzilyfzySZbea5fTDys2zDhicAL95dALz5fLD75

elF35dxz1XunjnRe911QvwL0FeD1k2bILjnOuaJlCwrp8eqZ0BlLNq6TozrPWlKLGeciHGfYruk2ULxAWULqWd+92ye0L+ivyz2leBLwVv0D1lfmz9leWzzlcTjnTiYAZYDirA0dOzsBVa/UsxHhA7zYjsRDez60dSrqPNEGIkcyL/INbjt5eKLzKdlL2FNRzykeZLDRd/L+OcKFxOear0qdpzrmNDj5BejZC0omr+FeOfBEgfpK1d9Wm1cYru1d

Yrtxfk1oCfoAJafG54JdNjrmudN9efrTzefMV4dvKK/tfDjp3M+TscebL0ziSANJCl0/iXxLk+xC2OEZHuZxgeYlSCSr5Fepr3wZhhVLBaaApX/z+YcfFlwcqLhqvsTotfVLl761LgysbdwvPAroDtbJlKsGr++yQRc+xWL/vtv2BvCUaPpezjNqeYzjtdlqe1fdrhFt2FkGA1M7gfQbhMAzLkdctpjeftjulcfmuDd9NNZdzrk6tilicfYgZTqa

PdI4p99dtsSZkZORbrGM4B6c26hy1Jrtccpr0Bsq5uICPFqFhfTs9euji9dZT/Nc5T6OfqLu9cq91FOvN8tcoDl9doDnFMhWjvvgd/aB/EFYy7tkatwrk3o0iWlACjj8e03DGeQDW1dgbrtfYl9xd2FiHI30CREMsGZhoQFSiVTF8qErhuC6bhUDdwRZiGb5QImb4yrkr6ydWZ91dUrvxfIbgJcTrxCcWb/TfWbn+Gs0Ozd/oS+cztjQeqt8rs7t

cADTQaDDFoaUC1IS0LQAWEBYIiQA5R5w0MAcGAUAVkWcbsVD4xvxP7yEQD60OnSZAaUB/T3Us5b0JCfaR6Dpb9LNcb+TUlbvLePQHue3rxKg1bsrcFb7JarSyoCjR8M1NblqyPQQrergIeWSwK+vSQVkuqKMrRdb1cw9b/jcIMsbf5b/QD8z4NNVEXLfNb/QBTJzDrTbureeFtbeZAWZTUVo8CbbkcIFaw+t7b6LcJPb3VVWPbdbCL3X9vH3VFAP

bcSaK3kzsAGCrAPbfughACUzzcCs4dEAHwiUCShB9mnCYvA7sXWrbVQECfbkjH6MJLCBMevALeURQ+ob8jyqNjmcdKMYMAYeXHoTWqmMLYh7b/mcGhdzJPblkAkASKuFSPHcpgfdC4cYHe4736lF8LYRtrZRxzREgB9YH3DP2o2hBYXxy4ACHJzJKo6923gAc7yFRJnEGDDeOLZzAZnes72/C8AYXf9FQ8BfESnLo7kJr60Xre4gWmTeUGri6hEG

AzgWlm/PYW5U7lCdmUdSgoTuZMoTruQOGRs5MQBf1MAfgMJb0JdG73ECbCPQg/NVFccWm7eXKviudtdU6U7m3dMiaDCmiRgAMMQkCXXfM0EdmCTT5oRUGAe7cHgeatMeSNkzMUahARErtsqS6Ae7hABe7mnsmNoziTjhMBtrBEGnQSqb9gN3d+rQ0yuAxHxCgZRAYAa3ewEJ7cJgEzwu7kveHTxRyiqW4yO74tBy0Cvcqb4HfZgTAAR77mg+gdZP

MS1fQPISJApJzUyU4MiBAAA=
```
%%