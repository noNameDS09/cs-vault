# 47 FastAPI Basics

tags:
#fastapi
#python
#api
#ai-engineering
#placements
#interview

---

## Why this topic matters
Once you've trained an ML model or built an AI agent, you need to **serve it** so other applications can use it. **FastAPI** is the most popular Python framework for building high-performance APIs quickly. It's essential for deploying ML models as REST endpoints and integrating AI services into production systems.

## Learning Objectives
- Understand what FastAPI is and why it's popular.
- Learn how to create basic endpoints.
- Understand request/response models.
- Know how to deploy and test FastAPI applications.

## Prerequisites
- [[04 Python for ML]]
- [[55 AI System Design Basics]]

---

## Intuition
Imagine you've built an amazing **AI model** that can classify images.

**Problem**: How does a mobile app, website, or another service use your model?

**Solution**: Wrap your model in an **API**.

```
Mobile App → API (FastAPI) → Your AI Model → Prediction → API → Mobile App
```

**FastAPI** is like a **waiter** at a restaurant:
- Takes orders (requests) from customers (apps).
- Brings them to the kitchen (your model).
- Serves the food (responses) back to customers.

---

## Detailed Explanation

### What is FastAPI?

**FastAPI** is a modern, fast Python web framework for building APIs.

**Key Features**:
- **Fast**: High performance (comparable to Node.js and Go).
- **Easy**: Simple syntax, minimal boilerplate.
- **Automatic Docs**: Generates interactive API documentation (Swagger UI).
- **Type Hints**: Uses Python type annotations for validation.
- **Async Support**: Handles concurrent requests efficiently.

### Basic FastAPI Structure

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Create app
app = FastAPI()

# Define a request model
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Define an endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Define an endpoint with parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define a POST endpoint with request body
@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "total": item.price * 1.1}
```

### Running the Application

```bash
# Install: pip install fastapi uvicorn

# Run: uvicorn main:app --reload
# --reload: Auto-reload on code changes (development)
```

**Access**:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc

### Request and Response Models

#### Path Parameters

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):  # user_id is automatically validated as int
    return {"user_id": user_id}
```

#### Query Parameters

```python
@app.get("/search")
def search(q: str, limit: int = 10):  # q is required, limit defaults to 10
    return {"query": q, "limit": limit}
```

#### Request Body (POST/PUT)

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users/")
def create_user(user: UserCreate):
    # user is automatically parsed and validated
    return {"message": f"User {user.username} created"}
```

#### Response Model

```python
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    ...
```

### Integrating ML Models

```python
from fastapi import FastAPI
import joblib

app = FastAPI()

# Load model at startup
model = joblib.load("model.pkl")

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: int
    probability: float

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    # Make prediction
    pred = model.predict([request.features])[0]
    prob = model.predict_proba([request.features])[0][1]
    
    return PredictionResponse(prediction=pred, probability=prob)
```

### Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

### Middleware and Dependencies

#### Middleware (for logging, CORS, etc.)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### Dependencies (for auth, validation)

```python
from fastapi import Depends

def verify_token(token: str):
    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/protected")
def protected(token: str = Depends(verify_token)):
    return {"message": "Access granted"}
```

---

## Real-world Example

**ML Model Serving for Fraud Detection**

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("fraud_model.pkl")

class Transaction(BaseModel):
    amount: float
    merchant: str
    location: str
    user_id: int

class FraudResponse(BaseModel):
    is_fraud: bool
    risk_score: float
    reason: str

@app.post("/check-fraud", response_model=FraudResponse)
def check_fraud(transaction: Transaction):
    features = preprocess(transaction)
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1]
    
    return FraudResponse(
        is_fraud=prediction == 1,
        risk_score=probability,
        reason="High risk transaction pattern" if probability > 0.8 else "Normal"
    )
```

**Usage**:
```bash
curl -X POST "http://localhost:8000/check-fraud" \
  -H "Content-Type: application/json" \
  -d '{"amount": 5000, "merchant": "Unknown", "location": "Foreign", "user_id": 123}'
```

---

## Advantages
- **Fast Development**: Minimal boilerplate, automatic validation.
- **Performance**: Async support, high throughput.
- **Documentation**: Auto-generated interactive docs.
- **Type Safety**: Python type hints catch errors early.
- **Ecosystem**: Integrates with ML libraries, databases, auth.

## Limitations
- **Learning Curve**: Requires understanding of async, type hints.
- **Overhead**: For simple scripts, might be overkill.
- **Production Deployment**: Requires additional setup (Gunicorn, Docker, etc.).

---

## Common Interview Questions
- **What is FastAPI and why use it?**
- **How do you create a POST endpoint in FastAPI?**
- **What is the difference between path and query parameters?**
- **How do you validate request data?**
- **How do you serve an ML model with FastAPI?**
- **What is Swagger UI and how do you access it?**
- **How do you handle errors in FastAPI?**

### Interview Answer Tips
- Emphasize **automatic validation** and **documentation** as key benefits.
- Mention that FastAPI uses **Pydantic** for data validation.
- Note that it's **async-ready** for high-performance applications.

---

## Common Mistakes
- Not using Pydantic models for validation.
- Blocking async event loop with synchronous code (e.g., heavy ML inference).
- Not handling errors properly (always return proper HTTP status codes).
- Forgetting middleware (CORS, logging, auth).

---

## Summary
FastAPI is a modern Python framework for building high-performance APIs with automatic documentation and validation. Use it to serve ML models, create REST endpoints, and integrate AI services. Key features include type hints for validation, async support, and auto-generated Swagger docs. It's the go-to choice for deploying Python ML/AI applications.

---

## Practice Questions
1. What is the main advantage of FastAPI over Flask?
2. How do you define a request body in FastAPI?
3. What is Swagger UI and how do you access it?
4. How do you handle errors in FastAPI?
5. What is Pydantic and how is it used?
6. How do you add authentication to a FastAPI endpoint?
7. What does `--reload` do when running uvicorn?
8. How would you serve a scikit-learn model with FastAPI?

---

## Mini Project Ideas
1. **Model API**: Wrap a trained sklearn model in a FastAPI endpoint.
2. **Todo API**: Build a CRUD API for a todo list.
3. **ML Pipeline**: Create a multi-endpoint API (predict, retrain, get stats).

---

## Further Reading
- [[04 Python for ML]]
- [[55 AI System Design Basics]]
- [[58 MLOps]]