# 48 Model Serving

tags:
#mlops
#model-serving
#deployment
#ai-engineering
#placements
#interview

---

## Why this topic matters
Training a model is only half the battle. To deliver value, the model must be **served** (deployed) so applications can use it for predictions. **Model Serving** involves packaging, deploying, scaling, and monitoring ML models in production. This is a critical skill for ML Engineers and is frequently asked in interviews.

## Learning Objectives
- Understand what model serving is and why it's needed.
- Learn different serving patterns (real-time vs. batch).
- Understand model packaging and versioning.
- Know popular model serving tools and frameworks.

## Prerequisites
- [[03 AI Development Lifecycle]]
- [[47 FastAPI Basics]]
- [[55 AI System Design Basics]]

---

## Intuition
Imagine you've trained a brilliant **chess grandmaster** (your ML model).

**Problem**: The grandmaster is locked in a room. No one can play chess with them!

**Solution**: Build a **chess table** where people can sit, make moves, and get the grandmaster's responses.

**Model Serving** is building that "chess table" for your ML model:
- **API Endpoint**: Where users send data.
- **Prediction**: Model processes data and returns results.
- **Scaling**: Multiple grandmasters for many players.
- **Monitoring**: Ensuring the grandmaster isn't getting tired or making mistakes.

---

## Detailed Explanation

### What is Model Serving?

**Model Serving** is the process of deploying a trained ML model to make it accessible for **inference** (predictions) in production.

**Key Components**:
1. **Model Packaging**: Saving the model in a portable format.
2. **Deployment**: Running the model on servers/cloud.
3. **API Layer**: Exposing endpoints for predictions.
4. **Scaling**: Handling multiple requests concurrently.
5. **Monitoring**: Tracking performance, latency, errors.

### Serving Patterns

#### 1. Real-Time (Online) Serving

**Description**: Model responds to requests immediately (<100ms latency).

**Use Cases**:
- Fraud detection (approve/reject transactions).
- Recommendation systems (what to show next).
- Chatbots and AI assistants.
- Real-time predictions (stock prices, weather).

**Architecture**:
```
User Request → Load Balancer → Model Server 1 → Prediction
                              → Model Server 2 → Prediction
                              → Model Server 3 → Prediction
```

**Tools**: FastAPI, Flask, TensorFlow Serving, TorchServe, KServe, Seldon Core.

**Pros**: Low latency, immediate feedback.
**Cons**: Expensive (servers running 24/7), complex scaling.

#### 2. Batch Serving

**Description**: Process large batches of data periodically (hourly, daily).

**Use Cases**:
- Daily recommendation updates.
- Nightly fraud analysis.
- Weekly sales forecasts.
- Monthly churn predictions.

**Architecture**:
```
Scheduled Job → Load Data → Model → Store Predictions → Users Access Later
```

**Tools**: Apache Spark, Airflow, AWS Batch, Google Dataflow.

**Pros**: Cost-effective (run only when needed), simpler.
**Cons**: High latency (predictions not immediate).

#### 3. Edge Serving

**Description**: Run model directly on user's device (phone, IoT).

**Use Cases**:
- Mobile apps (on-device speech recognition).
- IoT devices (smart home sensors).
- Autonomous vehicles (real-time object detection).

**Tools**: TensorFlow Lite, ONNX Runtime, Core ML (Apple), ML Kit (Google).

**Pros**: No network latency, works offline, privacy (data stays on device).
**Cons**: Limited compute power, model size constraints.

### Model Packaging

#### Pickle (Python-specific)

```python
import joblib

# Save
joblib.dump(model, 'model.pkl')

# Load
model = joblib.load('model.pkl')
```

**Pros**: Simple, works with any Python object.
**Cons**: Python-only, security risks (don't load untrusted pickles).

#### ONNX (Open Neural Network Exchange)

```python
import onnx

# Export from PyTorch
torch.onnx.export(model, dummy_input, "model.onnx")

# Load and run in any ONNX-compatible runtime
```

**Pros**: Cross-framework, optimized runtimes, language-agnostic.
**Cons**: Not all models/layers supported, conversion can be tricky.

#### PMML / PFA (Traditional ML)

**Use Case**: Traditional ML models (trees, linear models) for enterprise systems.

### Model Versioning

**Problem**: Models get updated. How do you manage versions?

**Solutions**:
1. **File Naming**: `model_v1.pkl`, `model_v2.pkl`
2. **Model Registry**: MLflow, DVC, Weights & Biases
3. **Container Tags**: `myapp:model-1.0`, `myapp:model-2.0`

**Best Practice**: Use a **Model Registry** to track versions, metadata, and lineage.

### Popular Model Serving Tools

| Tool | Best For | Key Features |
| :--- | :--- | :--- |
| **FastAPI / Flask** | Custom APIs, simple deployments | Easy, flexible, Python-based |
| **TensorFlow Serving** | TensorFlow models | Optimized, production-ready |
| **TorchServe** | PyTorch models | Native PyTorch support |
| **KServe** | Kubernetes-native serving | Auto-scaling, canary deployments |
| **Seldon Core** | Enterprise ML deployments | Advanced monitoring, A/B testing |
| **BentoML** | Multi-framework serving | Unified API, model management |
| **AWS SageMaker** | Cloud-native serving | Managed service, auto-scaling |

---

## Real-world Example

**E-commerce Recommendation System**

**Scenario**: Amazon needs to recommend products to millions of users in real-time.

**Serving Architecture**:
1. **Model Training**: Nightly batch job trains new recommendation model.
2. **Model Registry**: New model version uploaded to MLflow.
3. **Deployment**: Model deployed to KServe on Kubernetes cluster.
4. **API Endpoint**: `POST /recommendations` accepts user_id, returns product list.
5. **Scaling**: Auto-scales from 10 to 100 replicas during Black Friday.
6. **Monitoring**: Tracks latency (target <50ms), error rate (<0.1%), model drift.
7. **A/B Testing**: 10% of users get new model; compare conversion rates.

---

## Advantages
- **Accessibility**: Models can be used by any application via API.
- **Scalability**: Serve millions of predictions per day.
- **Monitoring**: Track model health and performance.
- **Versioning**: Roll back to previous versions if needed.

## Limitations
- **Cost**: Running servers 24/7 is expensive.
- **Complexity**: Production serving is much harder than training.
- **Latency**: Network and inference time add up.
- **Maintenance**: Models need updates, monitoring, and debugging.

---

## Common Interview Questions
- **What is model serving?**
- **Difference between real-time and batch serving?**
- **How do you package a model for deployment?**
- **What is ONNX and why use it?**
- **How do you handle model versioning?**
- **What tools have you used for model serving?**
- **How do you scale a model to handle 10,000 requests per second?**

### Interview Answer Tips
- Emphasize that **serving is different from training** (different requirements).
- Mention that **real-time serving needs low latency**, **batch serving is cost-effective**.
- Note that **model versioning** is critical for production.

---

## Common Mistakes
- Not versioning models (can't roll back).
- Ignoring monitoring (model drift goes unnoticed).
- Deploying without load testing (crashes under traffic).
- Using pickle for cross-language deployments.

---

## Summary
Model serving deploys trained models for production inference. Patterns include real-time (low latency), batch (cost-effective), and edge (on-device). Models can be packaged as pickle, ONNX, or in framework-specific formats. Versioning via model registries is essential. Popular tools include FastAPI, TensorFlow Serving, KServe, and cloud services. Serving requires scaling, monitoring, and maintenance.

---

## Practice Questions
1. When would you use batch serving over real-time serving?
2. What is ONNX and what are its benefits?
3. How do you version models in production?
4. What is the difference between TensorFlow Serving and FastAPI for serving?
5. How would you handle 100x traffic spike for your model?
6. Why is monitoring important in model serving?
7. What is edge serving and when is it useful?
8. Name three model serving tools and their use cases.

---

## Mini Project Ideas
1. **Simple API**: Serve a sklearn model with FastAPI.
2. **Batch Processing**: Create a daily batch job that runs predictions on new data.
3. **Model Versioning**: Set up MLflow to track and serve different model versions.

---

## Further Reading
- [[03 AI Development Lifecycle]]
- [[47 FastAPI Basics]]
- [[55 AI System Design Basics]]
- [[58 MLOps]]