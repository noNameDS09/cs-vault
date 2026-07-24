# Step 2 — Backend Foundation: Configuration, ORM, Migrations, Response Layer

**Status**: ✅ Completed  
**Date**: 2026-07-21  

---

## Objective

Convert the empty [apps/api](file:///d:/Programming/enterprise-rag/apps/api) scaffold into a fully wired FastAPI application with typed configuration, SQLAlchemy 2.0 ORM models matching [data-model.md](file:///d:/Programming/enterprise-rag/docs/data-model.md), Alembic migrations, and a standard API response framework matching [api-design.md](file:///d:/Programming/enterprise-rag/docs/api-design.md).

---

## Tasks Completed

- [x] **1. Add Production Dependencies** — [pyproject.toml](file:///d:/Programming/enterprise-rag/apps/api/pyproject.toml)
  - Added `sqlalchemy[asyncio]`, `asyncpg`, `alembic`, `pydantic-settings`, `redis`, `python-multipart`, `httpx`.
  - Separated dev dependencies (`mypy`, `pytest`, `ruff`) into `[project.optional-dependencies]`.
  - Ran `uv sync --all-extras` successfully.

- [x] **2. Pydantic Settings Configuration** — [core/config.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/config.py)
  - `Settings(BaseSettings)` with typed fields for PostgreSQL, Redis, Qdrant, MinIO, Keycloak, Ollama, and OpenRouter.
  - `@computed_field database_url` → async PostgreSQL connection string (`postgresql+asyncpg://...`).
  - `@computed_field database_url_sync` → sync string for Alembic (`postgresql://...`).
  - `@lru_cache get_settings()` singleton factory.

- [x] **3. Async Database Engine & Session** — [core/database.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/database.py)
  - `create_async_engine` with connection pooling (`pool_size=10`, `max_overflow=20`, `pool_pre_ping=True`).
  - `async_sessionmaker` factory.
  - `get_db_session()` async generator with automatic commit/rollback for FastAPI DI.

- [x] **4. SQLAlchemy 2.0 ORM Models** (14 classes across 5 files)
  - [x] [models/base.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/base.py) — `Base`, `TimestampMixin`, `SoftDeleteMixin`, `TenantMixin`, `generate_uuid()`.
  - [x] [models/tenant.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/tenant.py) — `Tenant` (name, slug, JSONB settings, soft delete).
  - [x] [models/user.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/user.py) — `User`, `Role`, `Permission`, `UserRole`, `RolePermission` (RBAC many-to-many).
  - [x] [models/document.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/document.py) — `Collection`, `Document` (with SHA-256 hash, status tracking), `DocumentChunk` (parent-child hierarchy, `vector_id`).
  - [x] [models/conversation.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/conversation.py) — `Conversation`, `Message` (role, token count, feedback), `Citation` (similarity score, snippet).
  - [x] [models/job.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/job.py) — `Job` (task tracking with JSONB result/error).
  - [x] [models/__init__.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/__init__.py) — Central re-export of all 14 model classes.

- [x] **5. Alembic Migration System**
  - [x] [alembic.ini](file:///d:/Programming/enterprise-rag/apps/api/alembic.ini) — Points to `src/api/migrations`.
  - [x] [migrations/env.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/migrations/env.py) — Wired to `Base.metadata` and `Settings.database_url_sync`.
  - [x] [migrations/script.py.mako](file:///d:/Programming/enterprise-rag/apps/api/src/api/migrations/script.py.mako) — Standard revision template.
  - [x] `migrations/versions/` — Created (empty, awaiting first `alembic revision --autogenerate`).

- [x] **6. API Response Framework & Exception Handling**
  - [x] [schemas/response.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/schemas/response.py) — `ApiResponse[T]` (generic success envelope), `ApiErrorResponse`, `ErrorDetail`, `PaginationMeta`, `ResponseMetadata`.
  - [x] [core/exceptions.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/exceptions.py) — `AppException` base + `NotFoundException`, `ForbiddenException`, `UnauthorizedException`, `ValidationException`, `ConflictException`, `ServiceUnavailableException`.
  - [x] [middlewares/exception_handlers.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/middlewares/exception_handlers.py) — Handlers for `AppException`, `RequestValidationError`, and catch-all `Exception`.

- [x] **7. Enhanced Application Entry Point** — [main.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/main.py)
  - `lifespan` async context manager with startup/shutdown logging.
  - Exception handlers registered via `register_exception_handlers(app)`.
  - `/health`, `/ready`, `/live` K8s probe endpoints.
  - API metadata (`title`, `version`, `description`) from `Settings`.

- [x] **8. Verification**
  - [x] `uv run pytest -q` — **3 passed** (health, readiness, liveness).
  - [x] `uv run ruff check .` — **All checks passed** (after auto-fix).
  - [x] `python -c "from api.models import *"` — **All 14 models imported successfully**.

---

## Files Created / Modified

| Action | File |
| :--- | :--- |
| MODIFIED | [pyproject.toml](file:///d:/Programming/enterprise-rag/apps/api/pyproject.toml) |
| CREATED | [core/__init__.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/__init__.py) |
| CREATED | [core/config.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/config.py) |
| CREATED | [core/database.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/database.py) |
| CREATED | [core/exceptions.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/core/exceptions.py) |
| CREATED | [models/base.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/base.py) |
| CREATED | [models/tenant.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/tenant.py) |
| CREATED | [models/user.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/user.py) |
| CREATED | [models/document.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/document.py) |
| CREATED | [models/conversation.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/conversation.py) |
| CREATED | [models/job.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/job.py) |
| CREATED | [models/__init__.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/models/__init__.py) |
| CREATED | [schemas/__init__.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/schemas/__init__.py) |
| CREATED | [schemas/response.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/schemas/response.py) |
| CREATED | [middlewares/__init__.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/middlewares/__init__.py) |
| CREATED | [middlewares/exception_handlers.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/middlewares/exception_handlers.py) |
| CREATED | [alembic.ini](file:///d:/Programming/enterprise-rag/apps/api/alembic.ini) |
| CREATED | [migrations/env.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/migrations/env.py) |
| CREATED | [migrations/script.py.mako](file:///d:/Programming/enterprise-rag/apps/api/src/api/migrations/script.py.mako) |
| CREATED | [migrations/versions/.gitkeep](file:///d:/Programming/enterprise-rag/apps/api/src/api/migrations/versions/.gitkeep) |
| MODIFIED | [main.py](file:///d:/Programming/enterprise-rag/apps/api/src/api/main.py) |
| MODIFIED | [tests/test_health.py](file:///d:/Programming/enterprise-rag/apps/api/tests/test_health.py) |
