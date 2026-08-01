# Enterprise RAG - Detailed Codebase Analysis

  

> **Purpose**: Comprehensive file-by-file analysis for interview preparation and onboarding.

> **Project**: Enterprise Retrieval-Augmented Generation Platform

> **Stack**: FastAPI, Qdrant, PostgreSQL, Redis, Ollama, LangChain, uv

  

---

  

## Table of Contents

  

1. [Project Structure Overview](#project-structure-overview)

2. [Root Configuration Files](#root-configuration-files)

3. [Infrastructure & Deployment](#infrastructure--deployment)

4. [API Application (`apps/api/`)](#api-application-appsapi)

   - [Core Configuration & Dependencies](#core-configuration--dependencies)

   - [AI Module (Embeddings, Reranker, Vector Store)](#ai-module-embeddings-reranker-vector-store)

   - [Database Layer](#database-layer)

   - [Document Processing Pipeline](#document-processing-pipeline)

   - [LLM Provider Abstraction](#llm-provider-abstraction)

   - [Prompt Engineering System](#prompt-engineering-system)

   - [Retrieval Pipeline](#retrieval-pipeline)

   - [Generation Pipeline](#generation-pipeline)

   - [API Endpoints](#api-endpoints)

5. [Frontend (`apps/web/`)](#frontend-appsweb)

6. [Internal Packages (`packages/`)](#internal-packages-packages)

7. [Key Architecture Patterns](#key-architecture-patterns)

8. [Interview Talking Points](#interview-talking-points)

  

---

  

## Project Structure Overview

  

```

enterprise-rag/

├── apps/

│   ├── api/                 # FastAPI backend (FULLY IMPLEMENTED)

│   └── web/                 # Next.js frontend (EMPTY PLACEHOLDER)

├── packages/                # Monorepo internal packages (MOSTLY EMPTY)

│   ├── ai/                  # Minimal exports only

│   ├── agents/              # Empty

│   ├── chunking/            # Empty

│   ├── common/              # Empty

│   ├── core/                # Empty

│   ├── embeddings/          # Empty

│   ├── evaluation/          # Empty

│   ├── ingestion/           # Empty

│   ├── rag/                 # Empty

│   └── retrieval/           # Empty

├── infrastructure/          # Docker, Nginx, Qdrant configs

├── docs/                    # Documentation (this file)

├── docker-compose.yml       # Multi-service orchestration

├── Taskfile.yml             # Task runner (just/Taskfile)

├── pyproject.toml           # Root workspace config

├── uv.lock                  # Locked dependencies

├── .env.example             # Environment template

├── .pre-commit-config.yaml  # Ruff hooks

├── mypy.ini                 # Type checking config

├── ruff.toml                # Linting config

└── README.md                # Project overview

```

  

---

  

## Root Configuration Files

  

### `pyproject.toml` (Root)

**Purpose**: Workspace configuration for `uv` monorepo.

```toml

[tool.uv.workspace]

members = ["apps/api", "packages/*"]

```

- Defines workspace members: API app + all packages

- Shared dev dependency: `ruff`

  

### `Taskfile.yml`

**Purpose**: Cross-platform task runner (replaces Make/just).

```yaml

tasks:

  dev:        # uv run uvicorn app.main:app --reload (in apps/api)

  lint:       # uv run ruff check .

  format:     # uv run ruff format .

  typecheck:  # uv run mypy .

  test:       # uv run pytest (in apps/api)

  compose-up: # docker compose up -d

  compose-down:

  compose-logs:

  check:      # lint + typecheck + test

```

**Interview Note**: Shows modern Python tooling preference (uv, Ruff, Taskfile over poetry/pip/make).

  

### `docker-compose.yml`

**Purpose**: Local development infrastructure.

```yaml

services:

  qdrant:

    image: qdrant/qdrant:latest

    ports: ["6333:6333", "6334:6334"]

    volumes: ["./infrastructure/qdrant:/qdrant/storage"]

```

**⚠️ Issue**: References `./apps/api/.env` but compose file is in root. Path resolution may fail.

  

### `.env.example`

**Purpose**: Environment variable template (safe to commit).

Key configs:

- **Ollama**: `OLLAMA_HOST=https://ollama.com`, `OLLAMA_MODEL=gpt-oss:120b`

- **Qdrant**: `QDRANT_URL=http://localhost:6333`, `QDRANT_COLLECTION=documents`

- **PostgreSQL**: `DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag`

- **Redis**: `REDIS_URL=redis://localhost:6379`

- **Chunking**: `chunk_size=1000`, `chunk_overlap=200`

- **Retrieval**: `retrieval_top_k=20`, `retrieval_score_threshold=0.55`

- **Reranking**: `rerank_top_k=5`

  

### `uv.lock`

**Purpose**: Reproducible dependency resolution (248KB). Committed for CI/CD consistency.

  

### `.pre-commit-config.yaml`

```yaml

repos:

  - repo: https://github.com/astral-sh/ruff-pre-commit

    hooks: [ruff-check, ruff-format]

```

Fast linting/formatting on commit.

  

---

  

## Infrastructure & Deployment

  

### `infrastructure/`

```

infrastructure/

├── docker/          # Dockerfile configs per service

├── nginx/           # Reverse proxy config (SSL, rate limiting)

├── qdrant/          # Qdrant collection config, aliases, persistence

└── scripts/         # Deployment/backup scripts

```

**Note**: Qdrant data persists in `./infrastructure/qdrant/` (mounted in compose).

  

---

  

## API Application (`apps/api/`)

  

### Structure

```

apps/api/

├── .env / .env.example

├── pyproject.toml        # App-specific dependencies

├── Taskfile.yml          # (if exists)

├── app/

│   ├── __init__.py

│   ├── main.py           # FastAPI app factory

│   ├── core/             # Config, DI, logging

│   ├── api/v1/           # REST endpoints

│   ├── ai/               # Embeddings, reranker, vectorstore

│   ├── db/               # Database clients (Qdrant, Postgres)

│   ├── documents/        # Document pipeline (load, split, index, store)

│   ├── generation/       # RAG pipeline (retrieve → prompt → generate → postprocess)

│   ├── llm/              # LLM abstraction + Ollama provider

│   ├── prompts/          # Prompt building, formatting, templates

│   ├── retrieval/        # Vector search + reranking service

│   ├── repositories/     # SQLAlchemy repositories

│   ├── schemas/          # Pydantic API models

│   └── services/         # Business logic (empty __init__.py only)

├── tests/                # Test suite (empty?)

└── uploads/              # Runtime file storage

```

  

---

  

### Core Configuration & Dependencies

  

#### `app/main.py` - FastAPI App Factory

```python

app = FastAPI(title="Enterprise RAG", version="0.1.0")

app.include_router(health_router)

app.include_router(document_router)

app.include_router(search_router)

app.include_router(chat_router)

```

- Minimal app creation

- Registers 4 routers: health, documents, search, chat

- No middleware, CORS, exception handlers yet

  

#### `app/core/config.py` - Pydantic Settings

```python

class Settings(BaseSettings):

    # Ollama

    ollama_api_key: str

    ollama_host: str

    ollama_model: str

  

    # Qdrant

    qdrant_url: str

    qdrant_collection: str

  

    # Chunking

    chunk_size: int = 1000

    chunk_overlap: int = 200

  

    # Retrieval

    retrieval_top_k: int = 20

    retrieval_score_threshold: float = 0.55

  

    # Reranking

    rerank_top_k: int = 5

  

    # Uploads

    upload_directory: str = "uploads"

    max_upload_size_mb: int = 20

  

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

  

@lru_cache

def get_settings() -> Settings:

    return Settings()

```

- Single source of truth for all configuration

- `@lru_cache` ensures singleton pattern

- `extra="ignore"` allows extra env vars without error

  

#### `app/core/dependencies.py` - Dependency Injection Container

```python

@lru_cache

def get_prompt_builder() -> PromptBuilder: ...

  

@lru_cache

def get_llm_provider() -> OllamaCloudProvider: ...

  

@lru_cache

def get_llm_service() -> LLMService:

    return LLMService(provider=get_llm_provider())

  

@lru_cache

def get_retrieval_service() -> RetrievalService:

    return RetrievalService(

        vector_store=get_vector_store(),

        reranker=get_reranker(),

    )

  

# Pipeline stages (singletons)

@lru_cache

def get_retrieve_stage() -> RetrieveStage: ...

@lru_cache

def get_prompt_stage() -> PromptStage: ...

@lru_cache

def get_generate_stage() -> GenerateStage: ...

@lru_cache

def get_postprocess_stage() -> PostProcessStage: ...

  

@lru_cache

def get_generation_service() -> GenerationService:

    return GenerationService(

        retrieve_stage=get_retrieve_stage(),

        prompt_stage=get_prompt_stage(),

        generate_stage=get_generate_stage(),

        postprocess_stage=get_postprocess_stage(),

    )

  

# Request-scoped (not cached)

def get_document_service(...) -> DocumentService: ...

```

**Pattern**: `@lru_cache` singletons for stateless services, request-scoped for DB sessions.

**Interview Point**: Demonstrates FastAPI DI + manual singleton management.

  

#### `app/core/logging.py`

```python

def setup_logging() -> None:

    logging.basicConfig(

        level=logging.INFO,

        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",

    )

```

Basic structlog-ready config. Structlog imported in services but not configured here yet.

  

---

  

### AI Module (Embeddings, Reranker, Vector Store)

  

#### `app/ai/embeddings.py` - Local Embedding Service

```python

MODEL_NAME = "BAAI/bge-base-en-v1.5"

EMBEDDING_DIMENSION = 768

  

@lru_cache(maxsize=1)

def get_model() -> SentenceTransformer:

    device = "cuda" if torch.cuda.is_available() else "cpu"

    return SentenceTransformer(MODEL_NAME, device=device)

  

class LocalEmbeddingService(Embeddings):

    def __init__(self): self.model = get_model()

    def embed_documents(self, texts): ...

    def embed_query(self, text): ...

```

**Key Features**:

- GPU auto-detection (`cuda`/`cpu`)

- Normalized embeddings (`normalize_embeddings=True`)

- Batch processing (`batch_size=64`)

- Implements LangChain `Embeddings` interface for QdrantVectorStore

- Singleton model loading via `@lru_cache`

  

#### `app/ai/reranker.py` - Cross-Encoder Reranker

```python

class CrossEncoderReranker:

    def __init__(self):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model_name = "BAAI/bge-reranker-base"

        self.model = CrossEncoder(self.model_name, device=self.device)

        self._warmup()  # Pre-load CUDA kernels

  

    def rerank(self, query: str, chunks: list[RetrievedChunk], top_k: int):

        sentence_pairs = [(query, chunk.text) for chunk in chunks]

        scores = self.model.predict(sentence_pairs, batch_size=16)

        # Attach reranker_score, sort by final_score, return top_k

  

@lru_cache

def get_reranker() -> CrossEncoderReranker: ...

```

**Key Features**:

- Cross-encoder (not bi-encoder) for higher accuracy

- GPU warmup avoids cold-start latency

- Batch inference for throughput

- Returns `RetrievedChunk` with `reranker_score` + `final_score` property

- **Interview Point**: Two-stage retrieval (vector → rerank) is production best practice

  

#### `app/ai/vectorstore.py` - Qdrant Wrapper

```python

def get_qdrant_client() -> QdrantClient:

    return QdrantClient(url=settings.qdrant_url)

  

def ensure_collection(client):  # Creates if not exists

    client.create_collection(

        collection_name=settings.qdrant_collection,

        vectors_config=VectorParams(size=768, distance=Distance.COSINE),

    )

  

def get_vector_store() -> QdrantVectorStore:

    client = get_qdrant_client()

    ensure_collection(client)

    return QdrantVectorStore(

        client=client,

        collection_name=settings.qdrant_collection,

        embedding=LocalEmbeddingService(),

    )

```

- Auto-creates collection with correct vector dimensions (768)

- Uses cosine distance (standard for normalized embeddings)

- Returns LangChain-compatible `QdrantVectorStore`

  

#### `app/ai/client.py` - Ollama Client Singleton

```python

from ollama import Client

from app.core.config import get_settings

  

settings = get_settings()

client = Client(

    host=settings.ollama_host,

    headers={"Authorization": f"Bearer {settings.ollama_api_key}"},

)

```

Module-level singleton. Used by `OllamaCloudProvider`.

  

---

  

### Database Layer

  

#### `app/db/qdrant.py` - Qdrant Client (Module Singleton)

```python

from qdrant_client import QdrantClient

from app.core.config import get_settings

  

settings = get_settings()

client = QdrantClient(url=settings.qdrant_url)

```

**Note**: Duplicate of `ai/vectorstore.py:get_qdrant_client()`. Should be consolidated.

  

#### `app/db/base.py` - SQLAlchemy DeclarativeBase

```python

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

```

  

#### `app/db/models/document.py` - Document ORM Model

```python

class DocumentStatus(StrEnum):

    PENDING = "PENDING"

    PROCESSING = "PROCESSING"

    READY = "READY"

    FAILED = "FAILED"

  

class Document(Base):

    __tablename__ = "documents"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)

    filename: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    original_filename: Mapped[str] = mapped_column(String(255))

    mime_type: Mapped[str] = mapped_column(String(100), default="application/pdf")

    size: Mapped[int] = mapped_column(Integer, default=0)

    checksum: Mapped[str | None] = mapped_column(String(64), nullable=True, unique=True)  # SHA256

    status: Mapped[str] = mapped_column(String(50), default=DocumentStatus.PENDING.value, index=True)

    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    chunk_count: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

```

**Design**: Full audit trail (checksum dedup, status tracking, timestamps).

  

---

  

### Document Processing Pipeline

  

#### `app/documents/loader.py` - PDF Loader

```python

def load_pdf(file_path: Path) -> list[Document]:

    loader = PyPDFLoader(str(file_path))

    documents = loader.load()

    # Detailed debug logging per page

    return documents

```

- Uses LangChain `PyPDFLoader`

- One `Document` per PDF page

- Rich debug output (page count, metadata, preview)

  

#### `app/documents/splitter.py` - Recursive Text Splitter

```python

_splitter = RecursiveCharacterTextSplitter(

    chunk_size=settings.chunk_size,      # 1000

    chunk_overlap=settings.chunk_overlap, # 200

    separators=["\n\n", "\n", ". ", " ", ""],

)

  

def split_documents(documents: list[Document]) -> list[Document]:

    return _splitter.split_documents(documents)

```

- Module-level singleton splitter (config from settings)

- Hierarchical separators preserve semantic boundaries

- Overlap prevents context loss at chunk boundaries

  

#### `app/documents/indexer.py` - Indexing Orchestrator

```python

def index_pdf(file_path: Path, vector_store: QdrantVectorStore, document_id: UUID, original_filename: str) -> int:

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    # Debug logging per chunk

    for i, chunk in enumerate(chunks):

        chunk.metadata["document_id"] = str(document_id)

        chunk.metadata["filename"] = original_filename

        chunk.metadata["chunk_index"] = i

        chunk.metadata["source"] = original_filename  # Legacy

        chunk.metadata["document_name"] = original_filename  # Legacy

    vector_store.add_documents(chunks)

    return len(chunks)

```

- Load → Split → Enrich metadata → Index

- Metadata includes: `document_id`, `filename`, `chunk_index`, `source`, `document_name`

- Returns chunk count for Document model

  

#### `app/documents/storage.py` - File Storage

```python

def save_upload(file: UploadFile) -> Path:

    upload_dir = Path(settings.upload_directory)

    upload_dir.mkdir(parents=True, exist_ok=True)

    destination = upload_dir / f"{uuid4()}{extension}"

    with destination.open("wb") as buffer:

        buffer.write(file.file.read())

    return destination

  

def delete_upload(filename: str) -> None:

    (Path(settings.upload_directory) / filename).unlink(missing_ok=True)

```

- UUID filenames prevent collisions

- Creates upload directory on demand

- Simple local filesystem storage (replaceable with S3)

  

#### `app/documents/service.py` - Document Business Logic

```python

class DocumentService:

    def __init__(self, vector_store: QdrantVectorStore, repository: DocumentRepository):

        self.vector_store = vector_store

        self.repository = repository

  

    async def list_documents(self) -> list[Document]:

        return await self.repository.list_documents()

  

    async def upload(self, file: UploadFile) -> Document:

        # 1. Validate PDF

        # 2. Compute SHA256 checksum

        # 3. Check duplicate via checksum

        # 4. Save to disk

        # 5. Create Document record (status=PROCESSING)

        # 6. Index PDF → Qdrant (updates chunk_count, status=READY)

        # 7. On failure: status=FAILED, error_message

        return document

  

    async def delete(self, document_id: UUID) -> None:

        # 1. Delete from Qdrant (filter by metadata.document_id)

        # 2. Delete from disk

        # 3. Delete from PostgreSQL

```

**Key Features**:

- Checksum-based deduplication (SHA256)

- Atomic status transitions: PENDING → PROCESSING → READY/FAILED

- Cascade delete: Qdrant + Disk + Postgres

- HTTPException for API errors (400, 404, 409)

  

#### `app/schemas/document.py` - API Response Model

```python

class DocumentResponse(BaseModel):

    id: UUID

    filename: str

    original_filename: str

    mime_type: str

    size: int

    status: str

    chunk_count: int

    created_at: datetime

    updated_at: datetime

    error_message: str | None = None

    checksum: str | None = None

    model_config = ConfigDict(from_attributes=True)  # ORM → Pydantic

```

  

#### `app/api/v1/documents.py` - REST Endpoints

```python

router = APIRouter(prefix="/documents", tags=["Documents"])

  

@router.get("")                          # List all

@router.post("/upload", status_code=202) # Upload PDF (async processing)

@router.delete("/{document_id}", status_code=204) # Delete

```

- `202 Accepted` for upload (processing is async-ish)

- `DocumentResponse` serialization via `model_validate`

  

---

  

### LLM Provider Abstraction

  

#### `app/llm/models.py` - Provider-Agnostic Models

```python

class FinishReason(StrEnum):

    STOP, LENGTH, CONTENT_FILTER, TOOL_CALLS, ERROR

  

class Usage(BaseModel):

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0

  

class GenerationOptions(BaseModel):

    model: str

    temperature: float = Field(default=0.0, ge=0.0, le=2.0)

    max_tokens: int | None = Field(default=None, gt=0)

    top_p: float | None = Field(default=None, gt=0.0, le=1.0)

    stream: bool = False

    metadata: dict[str, Any] = {}

  

class LLMRequest(BaseModel):

    prompt: Prompt      # From prompts.models

    options: GenerationOptions

  

class LLMResponse(BaseModel):

    text: str

    model: str

    finish_reason: FinishReason

    usage: Usage

    created_at: datetime

    metadata: dict[str, Any] = {}

```

**Design**: Normalized interface independent of provider SDK.

  

#### `app/llm/providers/base.py` - Abstract Base Class

```python

class BaseLLMProvider(ABC):

    @property @abstractmethod def name(self) -> str: ...

    @abstractmethod async def generate(self, request: LLMRequest) -> LLMResponse: ...

    @abstractmethod async def generate_stream(self, request: LLMRequest) -> AsyncGenerator[str, None]: ...

    async def health_check(self) -> bool: return True

```

**Pattern**: Strategy pattern for LLM providers. Easy to add OpenAI, Anthropic, Gemini.

  

#### `app/llm/providers/ollama.py` - Ollama Cloud Implementation

```python

class OllamaCloudProvider(BaseLLMProvider):

    def __init__(self, client: Client | None = None):

        self._client = client or Client(host=settings.ollama_host, headers={...})

  

    @property def name(self): return "ollama"

  

    async def generate(self, request: LLMRequest) -> LLMResponse:

        # Validate no streaming (sync only)

        # Build options dict (temperature, top_p, num_predict)

        # Convert messages to Ollama format

        # Call self._client.chat(stream=False)

        # Translate exceptions → domain exceptions

        # Build LLMResponse with usage, finish_reason

  

    async def generate_stream(self, request): ...  # stream=True, yield tokens

  

    async def health_check(self): return self._client.ps()

  

    def _build_response(self, response: ChatResponse) -> LLMResponse: ...

    def _finish_reason(self, reason) -> FinishReason: ...  # stop/length/error

    def _translate_exception(self, exc) -> Exception: ...  # Maps to domain exceptions

```

**Features**:

- Sync + streaming support

- Comprehensive exception mapping (Auth, RateLimit, Timeout, Connection, Request)

- Usage tracking (prompt_eval_count, eval_count)

- Health check via `ps()` (list running models)

  

#### `app/llm/exceptions.py` - Domain Exceptions

```python

class ProviderError(Exception): ...

class AuthenticationError(ProviderError): ...

class RateLimitError(ProviderError): ...

class TimeoutError(ProviderError): ...

class ConnectionError(ProviderError): ...

class InvalidRequestError(ProviderError): ...

class ResponseParsingError(ProviderError): ...

```

Hierarchy enables catch-all `except ProviderError`.

  

#### `app/llm/service.py` - LLM Service Facade

```python

class LLMService:

    def __init__(self, provider: BaseLLMProvider):

        self._provider = provider

  

    async def generate(self, request: LLMRequest) -> LLMResponse:

        logger.info("llm.generate.start", provider=..., model=...)

        response = await self._provider.generate(request)

        logger.info("llm.generate.success", tokens=..., finish_reason=...)

        return response

  

    async def generate_stream(...): ...

    async def health_check(self): ...

```

- Thin wrapper adding structured logging (structlog)

- Single entry point for generation

  

---

  

### Prompt Engineering System

  

#### `app/prompts/models.py` - Prompt Domain Models

```python

class MessageRole(StrEnum): SYSTEM, USER, ASSISTANT

  

class ChatMessage(BaseModel):

    role: MessageRole

    content: str

  

class PromptSource(BaseModel):  # Structured source metadata

    source_number: int

    document_name: str

    page: int | None

    vector_score: float

    reranker_score: float | None

    final_score: float

    metadata: dict[str, Any]

  

class PromptContext(BaseModel):

    text: str                    # Formatted context for LLM

    sources: list[PromptSource]  # Structured for citations/UI

  

class PromptMetadata(BaseModel):

    template: str

    retrieval_count: int

    estimated_tokens: int = 0

    created_at: datetime

  

class Prompt(BaseModel):

    query: str

    messages: list[ChatMessage]

    context: PromptContext

    metadata: PromptMetadata

```

**Design**: Separation of formatted text (`PromptContext.text`) from structured metadata (`PromptContext.sources`) enables citations without parsing.

  

#### `app/prompts/formatter.py` - Context Formatter

```python

class ContextFormatterConfig(BaseModel):

    include_document_name: bool = True

    include_page_number: bool = True

    include_scores: bool = False

    separator: str = "=" * 80

  

class ContextFormatter:

    def format(self, chunks: list[RetrievedChunk]) -> PromptContext:

        # For each chunk: create PromptSource + formatted section

        # Section: [separator, "Source [N]", Document, Page, Scores, Content]

        # Returns PromptContext(text=joined_sections, sources=structured_list)

```

- Configurable output (scores, page numbers, document names)

- Deterministic formatting for reproducibility

- Handles empty chunks gracefully

  

#### `app/prompts/templates.py` - Prompt Templates

```python

DEFAULT_INSTRUCTIONS = """Answer the user's question using ONLY the supplied context.

If the answer cannot be determined from the context, state that explicitly.

When appropriate, cite supporting sources using Source [1], Source [2], etc."""

  

class PromptTemplate:

    def render(self, context: PromptContext, query: str) -> str:

        return f"""CONTEXT

--------

{context.text}

  

QUESTION

--------

{query}

  

INSTRUCTIONS

------------

{DEFAULT_INSTRUCTIONS}"""

```

- Extensible template system

- Clear section delimiters for LLM parsing

  

#### `app/prompts/system.py` - System Prompt Registry

```python

ENTERPRISE_QA = """You are an enterprise RAG assistant.

- Treat context as source of truth

- Do not fabricate facts

- If unavailable, state explicitly

- Cite sources as Source [1], Source [2]"""

  

SUMMARY = """Generate concise summary using only supplied context."""

EXTRACTION = """Extract only requested information from context."""

QUERY_REWRITE = """Rewrite user query to be self-contained given history.

DO NOT answer. ONLY output rewritten query."""

  

SYSTEM_PROMPTS = {

    "enterprise_qa": ENTERPRISE_QA,

    "summary": SUMMARY,

    "extraction": EXTRACTION,

    "query_rewrite": QUERY_REWRITE,

}

  

def get_system_prompt(name: str = "enterprise_qa") -> str: ...

```

- Centralized prompt management

- Versionable, testable, swappable

- `query_rewrite` enables conversational RAG (future)

  

#### `app/prompts/builder.py` - Prompt Builder

```python

class PromptBuilder:

    def __init__(self, formatter=None, template=None, system_prompt_name="enterprise_qa"):

        self._formatter = formatter or ContextFormatter()

        self._template = template or PromptTemplate()

        self._system_prompt_name = system_prompt_name

  

    def build(self, query: str, chunks: list[RetrievedChunk], history=None) -> Prompt:

        context = self._formatter.format(chunks=chunks)

        system_prompt = get_system_prompt(self._system_prompt_name)

        user_prompt = self._template.render(context=context, query=query)

  

        messages = [

            ChatMessage(role=SYSTEM, content=system_prompt),

            *(history or []),

            ChatMessage(role=USER, content=user_prompt),

        ]

  

        return Prompt(

            query=query,

            messages=messages,

            context=context,

            metadata=PromptMetadata(template=type(self._template).__name__, retrieval_count=len(chunks))

        )

```

- Orchestrates formatter + template + system prompt

- Supports conversation history

- Returns full `Prompt` domain model

  

---

  

### Retrieval Pipeline

  

#### `app/retrieval/models.py` - RetrievedChunk Domain Model

```python

@dataclass(slots=True)

class RetrievedChunk:

    text: str

    vector_score: float

    reranker_score: float | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

  

    @property

    def final_score(self) -> float:

        return self.reranker_score if self.reranker_score is not None else self.vector_score

  

    @property

    def source(self) -> str: return str(self.metadata.get("source", "Unknown"))

    @property

    def document_name(self) -> str: return str(self.metadata.get("document_name", self.source))

    @property

    def page(self) -> int | None: ...

  

    def to_dict(self): ...

    def __repr__(self): ...

```

**Design**: `slots=True` for memory efficiency. `final_score` property enables seamless pre/post-rerank sorting.

  

#### `app/retrieval/utils.py` - Retrieval Utilities

```python

@dataclass

class RetrievalStats:

    retrieved: int = 0

    duplicates_removed: int = 0

    filtered_by_score: int = 0

    filtered_by_metadata: int = 0

    returned: int = 0

  

def documents_to_chunks(raw_results) -> list[RetrievedChunk]:

    return [RetrievedChunk(text=doc.page_content, vector_score=score, metadata=doc.metadata) for doc, score in raw_results]

  

def remove_duplicates(chunks): ...        # By text hash

def filter_by_score(chunks, threshold): ...  # vector_score >= threshold

def filter_by_metadata(chunks, filters): ... # Exact match on metadata keys

def sort_by_score(chunks): ...              # Descending final_score

def limit_results(chunks, top_k): ...       # Slice

def print_retrieval_stats(stats): ...       # Debug logging

def print_chunks(chunks): ...               # Debug logging

```

**Pipeline Helpers**: Pure functions, testable, composable.

  

#### `app/retrieval/filters.py` - Filter Functions (re-exports from utils)

```python

from .utils import filter_by_metadata, filter_by_score, limit_results, remove_duplicates, sort_by_score

```

  

#### `app/retrieval/service.py` - RetrievalService (Core Pipeline)

```python

class RetrievalService:

    """Enterprise Retrieval Pipeline:

    Query → Dense Retrieval (Qdrant) → Remove Duplicates → Score Filter

    → Metadata Filter → Sort by Vector Score → Cross-Encoder Rerank → Return Top K

    """

  

    def __init__(self, vector_store, reranker: CrossEncoderReranker):

        self.vector_store = vector_store

        self.reranker = reranker

        self.settings = get_settings()

  

    def search(self, query: str, top_k=None, metadata_filters=None) -> list[RetrievedChunk]:

        retrieval_k = self.settings.retrieval_top_k           # 20

        rerank_top_k = top_k or self.settings.rerank_top_k    # 5

  

        stats = RetrievalStats()

  

        # 1. Vector Search (Qdrant)

        raw_results = self.vector_store.similarity_search_with_score(query, k=retrieval_k)

        stats.retrieved = len(raw_results)

        chunks = documents_to_chunks(raw_results)

  

        # 2. Remove Duplicates

        before = len(chunks)

        chunks = remove_duplicates(chunks)

        stats.duplicates_removed = before - len(chunks)

  

        # 3. Score Threshold

        before = len(chunks)

        chunks = filter_by_score(chunks, self.settings.retrieval_score_threshold)  # 0.55

        stats.filtered_by_score = before - len(chunks)

  

        # 4. Metadata Filtering

        before = len(chunks)

        chunks = filter_by_metadata(chunks, metadata_filters)

        stats.filtered_by_metadata = before - len(chunks)

  

        # 5. Sort by Vector Score

        chunks = sort_by_score(chunks)

  

        # 6. Cross-Encoder Rerank

        chunks = self.reranker.rerank(query, chunks, top_k=rerank_top_k)

  

        # 7. Safety Limit

        chunks = limit_results(chunks, rerank_top_k)

  

        stats.returned = len(chunks)

        print_retrieval_stats(stats)  # Debug

        print_chunks(chunks)          # Debug

  

        return chunks

  

    def similarity_search(self, query, top_k=None): return self.search(query, top_k)

```

**Interview Gold**: Complete production retrieval pipeline with:

- Two-stage retrieval (vector + cross-encoder)

- Configurable thresholds at each stage

- Comprehensive stats for observability

- Metadata filtering support

- Duplicate removal (critical for PDFs with repeated headers/footers)

  

#### `app/api/v1/search.py` - Search Endpoint

```python

@router.post("/documents/search", response_model=SearchResponse)

def semantic_search(request: SearchRequest, service: RetrievalService = Depends(get_retrieval_service)):

    results = service.search(query=request.query, top_k=request.top_k)

    return SearchResponse(query=request.query, total_results=len(results), results=[...])

```

  

---

  

### Generation Pipeline

  

#### `app/generation/models.py` - Request/Response Models

```python

class RetrievalConfig(BaseModel):

    top_k: int = Field(default=5, ge=1, le=50)

    metadata_filters: dict[str, object] | None = None

  

class GenerationRequest(BaseModel):

    query: str

    retrieval: RetrievalConfig = Field(default_factory=RetrievalConfig)

    generation: GenerationOptions = Field(default_factory=lambda: GenerationOptions(model="gpt-oss:120b"))

    system_prompt: str = "enterprise_qa"

  

class GenerationResponse(BaseModel):

    query: str

    answer: str

    model: str

    finish_reason: FinishReason

    usage: Usage

    sources: list[PromptSource]  # For citations

    created_at: datetime

```

  

#### `app/generation/pipeline/base.py` - Pipeline Stage Base

```python

class PipelineStage(Generic[InputT, OutputT], ABC):

    @abstractmethod

    async def run(self, input: InputT) -> OutputT: ...

```

Generic async pipeline stage interface.

  

#### `app/generation/pipeline/retrieve.py` - RetrieveStage

```python

class RetrieveStage(PipelineStage[GenerationRequest, list[RetrievedChunk]]):

    def __init__(self, retrieval_service: RetrievalService):

        self._retrieval_service = retrieval_service

  

    async def run(self, request: GenerationRequest) -> list[RetrievedChunk]:

        return self._retrieval_service.search(

            query=request.query,

            top_k=request.retrieval.top_k,

        )

```

Thin wrapper - all logic in `RetrievalService`.

  

#### `app/generation/pipeline/prompt.py` - PromptStage

```python

class PromptStage(PipelineStage[tuple[GenerationRequest, list[RetrievedChunk]], Prompt]):

    def __init__(self, prompt_builder: PromptBuilder):

        self._prompt_builder = prompt_builder

  

    async def run(self, input: tuple[GenerationRequest, list[RetrievedChunk]]) -> Prompt:

        request, chunks = input

        return self._prompt_builder.build(

            query=request.query,

            chunks=chunks,

        )

```

Receives `(request, chunks)` tuple from previous stage.

  

#### `app/generation/pipeline/generate.py` - GenerateStage

```python

class GenerateStage(PipelineStage[tuple[GenerationRequest, Prompt], LLMResponse]):

    def __init__(self, llm_service: LLMService):

        self._llm_service = llm_service

  

    async def run(self, input: tuple[GenerationRequest, Prompt]) -> LLMResponse:

        request, prompt = input

        llm_request = LLMRequest(

            prompt=prompt,

            options=request.generation,

        )

        return await self._llm_service.generate(llm_request)

```

Converts internal `Prompt` → provider `LLMRequest`.

  

#### `app/generation/pipeline/postprocess.py` - PostProcessStage

```python

class PostProcessStage(PipelineStage[tuple[Prompt, list[RetrievedChunk], LLMResponse], GenerationResponse]):

    async def run(self, input: tuple[Prompt, list[RetrievedChunk], LLMResponse]) -> GenerationResponse:

        prompt, chunks, llm_response = input

        return GenerationResponse(

            query=prompt.query,

            answer=llm_response.text,

            model=llm_response.model,

            finish_reason=llm_response.finish_reason,

            usage=llm_response.usage,

            sources=prompt.context.sources,  # Citations!

            created_at=llm_response.created_at,

        )

```

**Critical**: Extracts `sources` from `PromptContext` for frontend citations.

  

#### `app/generation/service.py` - GenerationService (Orchestrator)

```python

class GenerationService:

    """RAG Pipeline:

    GenerationRequest → RetrieveStage → PromptStage → GenerateStage → PostProcessStage → GenerationResponse

    """

  

    def __init__(self, retrieve_stage, prompt_stage, generate_stage, postprocess_stage):

        self._retrieve_stage = retrieve_stage

        self._prompt_stage = prompt_stage

        self._generate_stage = generate_stage

        self._postprocess_stage = postprocess_stage

  

    async def generate(self, request: GenerationRequest) -> GenerationResponse:

        logger.info("generation.start", query=request.query)

  

        chunks = await self._retrieve_stage.run(request)

        logger.info("generation.retrieval.complete", chunks=len(chunks))

  

        prompt = await self._prompt_stage.run((request, chunks))

        logger.info("generation.prompt.complete", messages=len(prompt.messages))

  

        llm_response = await self._generate_stage.run((request, prompt))

        logger.info("generation.llm.complete", finish_reason=..., total_tokens=...)

  

        response = await self._postprocess_stage.run((prompt, chunks, llm_response))

        logger.info("generation.success")

        return response

```

**Pattern**: Explicit pipeline orchestration with structured logging at each stage.

**Observability**: Logs chunk count, message count, tokens, finish reason.

  

#### `app/api/v1/chat.py` - Chat Endpoint

```python

@router.post("", response_model=GenerationResponse)

async def chat(request: GenerationRequest, generation_service: GenerationService = Depends(get_generation_service)):

    return await generation_service.generate(request)

```

Single endpoint for full RAG query.

  

---

  

### API Endpoints Summary

  

| Endpoint | Method | Path | Purpose |

|----------|--------|------|---------|

| Health | GET | `/health` | Liveness/readiness |

| Documents | GET | `/documents` | List all documents |

| Documents | POST | `/documents/upload` | Upload PDF (202) |

| Documents | DELETE | `/documents/{id}` | Delete document (204) |

| Search | POST | `/documents/search` | Semantic search only |

| Chat | POST | `/chat` | Full RAG (retrieve + generate) |

  

---

  

### Database Repository

  

#### `app/repositories/document.py` - DocumentRepository

```python

class DocumentRepository:

    def __init__(self, session: AsyncSession): self.session = session

  

    async def get_by_id(self, doc_id: UUID) -> Document | None: ...

    async def get_by_filename(self, filename: str) -> Document | None: ...

    async def get_by_checksum(self, checksum: str) -> Document | None: ...

    async def create(self, document: Document) -> Document: ...

    async def update(self, document: Document) -> Document: ...

    async def delete(self, document: Document) -> None: ...

    async def list_documents(self) -> list[Document]: ...

```

Standard async SQLAlchemy repository pattern.

  

---

  

## Frontend (`apps/web/`)

  

**Status**: Empty directory. Placeholder for Next.js application.

  

---

  

## Internal Packages (`packages/`)

  

| Package | Status | Purpose (Intended) |

|---------|--------|-------------------|

| `ai/` | Minimal (`__init__.py`, `py.typed`) | Shared AI utilities |

| `agents/` | Empty | Agent orchestration |

| `chunking/` | Empty | Advanced chunking strategies |

| `common/` | Empty | Shared utilities, constants |

| `core/` | Empty | Core domain models |

| `embeddings/` | Empty | Embedding providers |

| `evaluation/` | Empty | RAG evaluation metrics |

| `ingestion/` | Empty | Document ingestion pipelines |

| `rag/` | Empty | RAG orchestration |

| `retrieval/` | Empty | Retrieval strategies |

  

**Note**: Monorepo structure exists but packages are not yet utilized. Code lives in `apps/api/app/`.

  

---

  

## Key Architecture Patterns

  

### 1. **Pipeline Architecture**

```

Request → Stage1 → Stage2 → Stage3 → Stage4 → Response

```

Each stage: `async run(input) -> output`, single responsibility, testable in isolation.

  

### 2. **Dependency Injection via `@lru_cache` Singletons**

```python

@lru_cache

def get_service() -> Service: return Service(dependencies...)

```

- FastAPI DI for request-scoped (DB sessions)

- Module-level singletons for stateless services

- No external DI container needed

  

### 3. **Provider Abstraction (Strategy Pattern)**

```python

BaseLLMProvider (ABC)

    └── OllamaCloudProvider

    └── (Future) OpenAIProvider, AnthropicProvider

```

Swap providers without changing pipeline code.

  

### 4. **Domain Models vs Infrastructure Models**

- `RetrievedChunk` (domain) ≠ LangChain `Document`

- `Prompt` (domain) ≠ Provider message format

- `LLMRequest/Response` (domain) ≠ Ollama `ChatResponse`

- **Adapters** at boundaries (vectorstore, LLM provider)

  

### 5. **Two-Stage Retrieval**

```

Vector Search (ANN, fast, recall) → Cross-Encoder Rerank (precise, slow, precision)

```

Industry best practice for production RAG.

  

### 6. **Structured Logging with structlog**

```python

logger.info("generation.retrieval.complete", chunks=len(chunks))

```

Key-value logs for observability platforms (Datadog, Loki, etc.).

  

### 7. **Pydantic Settings + Validation**

- Type-safe config with defaults

- Environment-specific `.env` files

- Field validation (ge, le, gt)

  

---

  

## Interview Talking Points

  

### Technical Depth Questions

  

**Q: Walk me through the RAG pipeline from query to answer.**

> A: Request hits `/chat` → `GenerationService.generate()` orchestrates 4 stages:

> 1. **RetrieveStage** → `RetrievalService.search()`: Qdrant vector search (top-20) → dedup → score filter (0.55) → metadata filter → sort → CrossEncoder rerank (top-5)

> 2. **PromptStage** → `PromptBuilder.build()`: Format chunks → system prompt + template → `Prompt` domain model

> 3. **GenerateStage** → `LLMService.generate()` → `OllamaCloudProvider.generate()`: Normalized request → Ollama API → normalized response

> 4. **PostProcessStage**: Extract answer + citations from `PromptContext.sources` → `GenerationResponse`

  

**Q: Why two-stage retrieval?**

> A: Vector search (HNSW) optimizes for **recall** - fast ANN over millions of vectors. Cross-encoder optimizes for **precision** - full attention over query+doc pairs but O(n²). Combining gives best of both: broad recall then precise rerank. Typical 20→5 reduction.

  

**Q: How do you handle duplicate chunks from PDFs?**

> A: `remove_duplicates()` in retrieval pipeline uses text hashing. Also `DocumentService.upload()` computes SHA256 checksum for whole-document deduplication before processing.

  

**Q: How is configuration managed?**

> A: Pydantic `BaseSettings` with `.env` files. `@lru_cache` on `get_settings()` ensures singleton. All config centralized in `core/config.py` with validation (e.g., `temperature: ge=0, le=2`).

  

**Q: How would you add a new LLM provider (e.g., OpenAI)?**

> A: 1) Create `OpenAIProvider` implementing `BaseLLMProvider` 2) Implement `generate()`, `generate_stream()`, `health_check()` 3) Map OpenAI exceptions to domain exceptions 4) Update `dependencies.py` to inject new provider 5) No pipeline changes needed.

  

**Q: How do you ensure observability?**

> A: Structured logging at each pipeline stage with key metrics (chunk count, tokens, latency). `RetrievalStats` tracks funnel: retrieved → deduped → score filtered → metadata filtered → reranked → returned. Ready for OpenTelemetry integration.

  

**Q: What's the document processing flow?**

> A: Upload → SHA256 checksum → duplicate check → save to disk → `Document` record (PROCESSING) → `index_pdf()`: PyPDFLoader (1 doc/page) → RecursiveCharacterTextSplitter (1000/200) → enrich metadata (doc_id, chunk_index) → QdrantVectorStore.add_documents() → update `Document` (READY, chunk_count).

  

### Architecture & Design Questions

  

**Q: Why separate `packages/` if they're empty?**

> A: Monorepo preparation. When we extract shared code (schemas, config, utilities), they'll move to packages with independent versioning. Currently all in `apps/api/app/` for velocity.

  

**Q: How do you handle schema evolution?**

> A: Pydantic models with `ConfigDict(from_attributes=True)` for ORM→API. Alembic for DB migrations (configured in pyproject.toml). Versioned API via `/v1/` prefix.

  

**Q: What's the scaling strategy for Qdrant?**

> A: Current: single-node Docker. Production: Qdrant Cluster (sharding, replication). Collection config in `infrastructure/qdrant/`. Can scale horizontally with consistent hashing.

  

**Q: How do you handle streaming responses?**

> A: `OllamaCloudProvider.generate_stream()` yields tokens via `AsyncGenerator`. `LLMService.generate_stream()` passes through. Frontend would consume via SSE/WebSocket (not yet implemented).

  

**Q: What are the current limitations?**

> A:

> - No PostgreSQL migrations applied (models exist but no Alembic)

> - Empty frontend, empty packages

> - Docker Compose env path issue

> - No authentication/authorization

> - No rate limiting

> - No evaluation pipeline

> - Sync `DocumentService.upload()` blocks on indexing (should be background job)

  

### Code Quality Questions

  

**Q: How do you ensure code quality?**

> A: Pre-commit hooks (Ruff check/format), MyPy strict mode, pytest. `Taskfile.yml` commands: `lint`, `typecheck`, `test`, `check` (all). UV for fast, reproducible installs.

  

**Q: Why Ruff over Black/Flake8/Isort?**

> A: Single tool, 10-100x faster (Rust), unified config, built-in caching. `ruff.toml` configures: target py312, line-length 88, select E/F/I/UP/B, known-first-party=["app"].

  

---

  

## File Inventory (Quick Reference)

  

### Root

| File | Purpose |

|------|---------|

| `pyproject.toml` | uv workspace config |

| `Taskfile.yml` | Task runner |

| `docker-compose.yml` | Local infra (Qdrant) |

| `.env.example` | Env template |

| `uv.lock` | Locked deps |

| `.pre-commit-config.yaml` | Ruff hooks |

| `mypy.ini` | Type check config |

| `ruff.toml` | Lint config |

| `README.md` | Overview |

  

### API App (`apps/api/app/`)

| File | Lines | Purpose |

|------|-------|---------|

| `main.py` | 16 | FastAPI factory |

| `core/config.py` | 39 | Pydantic Settings |

| `core/dependencies.py` | 93 | DI container |

| `core/logging.py` | 8 | Basic logging |

| `ai/embeddings.py` | 43 | BGE embeddings (GPU) |

| `ai/reranker.py` | 159 | CrossEncoder reranker |

| `ai/vectorstore.py` | 43 | Qdrant wrapper |

| `ai/client.py` | 10 | Ollama client |

| `db/qdrant.py` | 9 | Qdrant client (dup) |

| `db/base.py` | 5 | SQLAlchemy Base |

| `db/models/document.py` | 44 | Document ORM |

| `documents/loader.py` | 35 | PyPDFLoader |

| `documents/splitter.py` | 24 | RecursiveTextSplitter |

| `documents/indexer.py` | 44 | Load→Split→Index |

| `documents/storage.py` | 34 | File save/delete |

| `documents/service.py` | 94 | Business logic |

| `documents/__init__.py` | 1 | Package |

| `repositories/document.py` | 48 | SQLAlchemy repo |

| `schemas/document.py` | 20 | API response |

| `schemas/search.py` | - | Search models |

| `schemas/__init__.py` | 1 | Package |

| `llm/models.py` | 90 | Provider-agnostic models |

| `llm/providers/base.py` | 58 | ABC for providers |

| `llm/providers/ollama.py` | 245 | Ollama Cloud impl |

| `llm/exceptions.py` | - | Domain exceptions |

| `llm/service.py` | 92 | LLM facade + logging |

| `llm/__init__.py` | 1 | Package |

| `prompts/models.py` | 121 | Prompt domain models |

| `prompts/formatter.py` | 125 | Context formatting |

| `prompts/templates.py` | 53 | Prompt templates |

| `prompts/system.py` | 85 | System prompt registry |

| `prompts/builder.py` | 100 | Prompt orchestration |

| `prompts/__init__.py` | 1 | Package |

| `retrieval/models.py` | 98 | RetrievedChunk |

| `retrieval/utils.py` | - | Pipeline helpers |

| `retrieval/filters.py` | - | Filter re-exports |

| `retrieval/service.py` | 205 | Core retrieval pipeline |

| `retrieval/__init__.py` | 1 | Package |

| `generation/models.py` | - | Request/Response |

| `generation/pipeline/base.py` | - | Stage ABC |

| `generation/pipeline/retrieve.py` | 40 | RetrieveStage |

| `generation/pipeline/prompt.py` | - | PromptStage |

| `generation/pipeline/generate.py` | - | GenerateStage |

| `generation/pipeline/postprocess.py` | - | PostProcessStage |

| `generation/pipeline/__init__.py` | 1 | Package |

| `generation/service.py` | 138 | Pipeline orchestrator |

| `generation/__init__.py` | 1 | Package |

| `api/v1/health.py` | - | Health check |

| `api/v1/documents.py` | 57 | Document CRUD |

| `api/v1/search.py` | 52 | Semantic search |

| `api/v1/chat.py` | 35 | RAG chat |

| `api/v1/__init__.py` | 1 | Package |

| `api/__init__.py` | 1 | Package |

  

---

  

## Summary

  

This is a **well-architected, production-oriented RAG codebase** demonstrating:

- ✅ Clean architecture with clear layer separation

- ✅ Modern Python tooling (uv, Ruff, Taskfile, Pydantic v2)

- ✅ Industry best practices (two-stage retrieval, provider abstraction, pipeline pattern)

- ✅ Observability-ready (structlog, stats tracking)

- ✅ Type safety throughout (Pydantic, SQLAlchemy 2.0, MyPy)

  

**Main gaps for production**: Auth, rate limiting, background job queue, evaluation pipeline, frontend, populated internal packages, PostgreSQL migrations applied.

  

---

  

*Generated for interview preparation. Last updated: 2025-07-27*