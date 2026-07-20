Implementation order:

1. High-Level Architecture (C4 Level 1)
2. Container Diagram (C4 Level 2)
3. Component Diagrams (C4 Level 3)
4. Database Schema
5. API Design
6. gRPC Contracts
7. Folder Structure
8. Service Implementation
9. Deployment

| Service              | Responsibility                            |
| -------------------- | ----------------------------------------- |
| API Gateway          | REST, WebSockets, authentication, routing |
| Auth Service         | Keycloak integration, RBAC/ABAC           |
| Document Service     | Upload, parsing, indexing                 |
| RAG Service          | Retrieval pipeline, prompt orchestration  |
| Search Service       | Hybrid search + reranking                 |
| Memory Service       | Conversation & semantic memory            |
| LLM Service          | Provider abstraction (Ollama/OpenRouter)  |
| Worker Service       | Celery background jobs                    |
| Notification Service | Streaming, events, notifications          |
| Monitoring Service   | Metrics, logs, traces                     |

