

A **Modular Monolith** is a **single application (monolith)** that is **organized into independent modules** with clear boundaries.

Think of it as:

```
One deployable application
        │
 ├── User Module
 ├── Order Module
 ├── Payment Module
 └── Inventory Module
```

Each module:

- Owns its business logic.
    
- Exposes only a public interface.
    
- Doesn't directly access another module's internals.
    
- Can often have its own database schema or package.
    

### Why use it?

- ✅ Easier to develop and deploy than microservices.
    
- ✅ Better organization than a traditional monolith.
    
- ✅ Faster communication (function calls instead of network calls).
    
- ✅ Easier to split into microservices later if needed.
    

### Modular Monolith vs Microservices

|Modular Monolith|Microservices|
|---|---|
|One application|Multiple applications|
|One deployment|Multiple deployments|
|In-process communication|Network/API communication|
|Simpler operations|More operational complexity|
|Easier debugging|Harder due to distributed systems|

### When to use it

- Most startups and small-to-medium systems.
    
- Large applications that need clean architecture but don't yet need distributed services.
    
- Teams that want to avoid the operational overhead of microservices.
    

**One-line takeaway:**

> **A Modular Monolith is a well-structured monolith with strong module boundaries, giving many of the design benefits of microservices without the deployment and operational complexity.**


## Excalidraw Diagram : [[Excalidraw/MySystemDesigns.md#^8iy28LrImeWmklLMbUOkw|Modular Monolith]]
