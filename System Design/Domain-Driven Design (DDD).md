
**Domain-Driven Design (DDD)** is a way to design software where the **business domain** (how the business works) determines the structure of the code.

### Core ideas

- **Focus on the business**, not the database.
    
- **Use the same language** as business experts (Ubiquitous Language).
    
- **Put business rules inside domain objects**, not scattered across services.
    
- **Split large systems into Bounded Contexts**, where each part has its own model and responsibilities.
    

### Key building blocks

- **Entity**: Has a unique identity (e.g., `Customer`, `Order`).
    
- **Value Object**: Defined by its values, no identity (e.g., `Address`, `Money`).
    
- **Aggregate**: A group of related objects treated as one unit (e.g., `Order` + `OrderItems`).
    
- **Repository**: Loads and saves domain objects.
    
- **Domain Service**: Business logic that doesn't naturally belong to a single entity.
    
- **Domain Event**: Something important that happened (e.g., `OrderPlaced`).
    

### Example

Instead of:

```java
orderService.cancelOrder(orderId);
```

DDD encourages:

```java
order.cancel();
```

The `Order` object enforces its own business rules.

### When to use DDD

✅ Banking, healthcare, ERP, e-commerce, logistics, and other complex business systems.

### When not to use DDD

❌ Simple CRUD apps, prototypes, portfolios, or projects with minimal business logic.

**One-line takeaway:**

> **DDD models software around business concepts instead of database tables or technical layers.**



## Excalidraw for DDD: [[Excalidraw/MySystemDesigns.md#^TNmPR7ML68GvDG-NAm3KN|DDD]]

