# 49 GPU vs CPU Inference

tags:
#gpu
#cpu
#inference
#hardware
#placements
#interview

---

## Why this topic matters
Running ML models efficiently requires choosing the right hardware. **CPUs** and **GPUs** have different strengths: CPUs are versatile but slower for parallel tasks; GPUs are specialized for matrix operations but more expensive. Understanding when to use each is critical for optimizing cost, latency, and throughput in production AI systems.

## Learning Objectives
- Understand the differences between CPU and GPU.
- Learn when to use CPU vs. GPU for inference.
- Understand quantization and optimization techniques.
- Know cost-performance trade-offs.

## Prerequisites
- [[21 Neural Networks Basics]]
- [[48 Model Serving]]
- [[55 AI System Design Basics]]

---

## Intuition
Imagine you're organizing a **pizza party** for 100 people.

**CPU (General-Purpose Chef)**:
- One chef who can do everything: chop, cook, bake, deliver.
- Great at multitasking, but slow for large batches.
- **Best for**: Complex, sequential tasks (one pizza at a time).

**GPU (Assembly Line)**:
- 1000 workers, each doing one simple task (add sauce, add cheese, bake).
- Amazing at parallel work, but inflexible.
- **Best for**: Simple, repetitive tasks (100 pizzas at once).

**ML Inference**:
- **CPU**: Good for small models, low traffic, complex preprocessing.
- **GPU**: Best for large models (LLMs), high traffic, batch predictions.

---

## Detailed Explanation

### CPU vs. GPU Architecture

| Feature | CPU | GPU |
| :--- | :--- | :--- |
| **Cores** | Few (4-64), powerful | Thousands (1000s-10000s), simple |
| **Purpose** | General-purpose, versatile | Specialized for parallel compute |
| **Latency** | Low for single tasks | Higher for single tasks |
| **Throughput** | Lower for parallel tasks | Very high for parallel tasks |
| **Memory** | Large RAM (16-512 GB) | VRAM (8-80 GB, expensive) |
| **Cost** | Cheap ($100-$1000) | Expensive ($500-$15000+) |
| **Power** | Low (65-250W) | High (200-700W) |

### When to Use CPU

**Best For**:
- **Small models**: Traditional ML (Random Forest, XGBoost, small neural nets).
- **Low traffic**: <10 requests per second.
- **Latency-sensitive**: Single predictions need to be fast.
- **Complex preprocessing**: CPU handles logic better than GPU.
- **Cost-sensitive**: CPU instances are cheaper.

**Example Use Cases**:
- Fraud detection for a small fintech startup.
- Sentiment analysis on customer reviews (batch, once/day).
- Traditional ML models in production (sklearn, XGBoost).

**Popular CPU Options**:
- **AWS**: m5, c5 instances.
- **GCP**: N2, C2 instances.
- **Azure**: D-series, F-series.

### When to Use GPU

**Best For**:
- **Large models**: Deep learning (CNNs, Transformers, LLMs).
- **High traffic**: 100+ requests per second.
- **Batch inference**: Process thousands of samples at once.
- **Matrix operations**: Neural network forward passes.

**Example Use Cases**:
- Running a 7B parameter LLM for a chatbot.
- Image classification for a photo app (millions of images).
- Real-time object detection for autonomous vehicles.

**Popular GPU Options**:
- **NVIDIA T4**: Budget inference ($0.35/hr on AWS).
- **NVIDIA A10**: Mid-range, good for LLMs.
- **NVIDIA A100**: High-end, large LLMs, training.
- **NVIDIA H100**: Cutting-edge, massive models.

### Inference Optimization Techniques

#### 1. Quantization

**Idea**: Reduce precision from 32-bit floats to 8-bit integers.

```
FP32 (32-bit): 0.123456789 → High precision, large memory
INT8 (8-bit): 0.12 → Lower precision, 4x smaller, faster
```

**Impact**:
- **Model Size**: 4x smaller (16 GB → 4 GB).
- **Speed**: 2-3x faster inference.
- **Accuracy**: Minimal loss (1-2% drop).

**Tools**: ONNX Runtime, TensorRT, OpenVINO, bitsandbytes.

#### 2. Model Pruning

**Idea**: Remove unnecessary weights/neurons.

**Impact**: Smaller model, faster inference, minimal accuracy loss.

#### 3. Batch Inference

**Idea**: Process multiple requests together on GPU.

```
Single Request: 50ms latency
Batch of 32: 80ms total (2.5ms per request!)
```

**Trade-off**: Higher throughput, but higher latency per request.

#### 4. Model Distillation

**Idea**: Train a small "student" model to mimic a large "teacher" model.

```
Teacher: GPT-4 (1.7T params) → Student: TinyLlama (1.1B params)
```

**Impact**: 100x smaller, 10x faster, 90% of accuracy.

### Cost Comparison

**Scenario**: Serve an LLM for a chatbot.

| Setup | Monthly Cost | Latency | Throughput |
| :--- | :--- | :--- | :--- |
| **CPU (c5.4xlarge)** | $250 | 500ms | 10 req/s |
| **GPU (T4)** | $750 | 100ms | 100 req/s |
| **GPU (A10)** | $1500 | 50ms | 500 req/s |

**Decision**:
- Low traffic, budget-conscious → CPU.
- High traffic, low latency → GPU.

---

## Real-world Example

**Startup AI Chatbot**

**Phase 1 (Startup, 100 users/day)**:
- **Hardware**: CPU (AWS c5.large, $60/month).
- **Model**: Distilled LLM (TinyLlama, 1B params).
- **Latency**: 800ms (acceptable for MVP).
- **Cost**: Minimal.

**Phase 2 (Growth, 10,000 users/day)**:
- **Hardware**: GPU (AWS g4dn.xlarge, T4, $450/month).
- **Model**: Medium LLM (Mistral 7B, quantized).
- **Latency**: 150ms.
- **Throughput**: Handles peak traffic.

**Phase 3 (Scale, 1M users/day)**:
- **Hardware**: Multiple GPUs (A100 cluster, $5000/month).
- **Model**: Large LLM (Llama 2 70B).
- **Latency**: 50ms.
- **Throughput**: 1000s of requests per second.

---

## Advantages
- **CPU**: Cheap, versatile, good for low traffic.
- **GPU**: Fast for large models, high throughput.
- **Optimization**: Quantization and distillation reduce costs.

## Limitations
- **CPU**: Too slow for large models.
- **GPU**: Expensive, overkill for small models.
- **Optimization**: Quantization can reduce accuracy.

---

## Common Interview Questions
- **When would you use CPU vs. GPU for inference?**
- **What is quantization and why use it?**
- **How do you reduce inference costs?**
- **What is model distillation?**
- **Explain the difference between latency and throughput.**
- **How would you serve an LLM cost-effectively?**
- **What are the trade-offs of batch inference?**

### Interview Answer Tips
- Use the **pizza chef analogy** for CPU vs. GPU.
- Emphasize that **quantization** is the #1 optimization for LLMs.
- Mention that **batch inference** improves throughput but increases latency.

---

## Common Mistakes
- Using GPU for small models (waste of money).
- Using CPU for large LLMs (too slow).
- Not considering quantization (paying for unnecessary precision).
- Ignoring batch inference for high-throughput scenarios.

---

## Summary
CPUs are versatile and cheap, best for small models and low traffic. GPUs are specialized for parallel compute, essential for large models and high throughput. Optimization techniques like quantization (FP32→INT8), pruning, and distillation reduce costs and improve speed. Choose CPU for cost-sensitive, low-traffic scenarios; choose GPU for large models and high traffic. Balance latency, throughput, and cost based on your use case.

---

## Practice Questions
1. Why are GPUs faster than CPUs for deep learning?
2. What is quantization and what are its benefits?
3. When would you choose CPU over GPU for inference?
4. How does batch inference improve throughput?
5. What is model distillation?
6. What's the cost difference between T4 and A100 GPUs?
7. How do you decide between latency and throughput optimization?
8. What optimization would you use for a 70B parameter LLM?

---

## Mini Project Ideas
1. **CPU vs. GPU Benchmark**: Run the same model on CPU and GPU. Compare latency and throughput.
2. **Quantization Experiment**: Quantize a model to INT8. Measure speedup and accuracy loss.
3. **Batch Inference Test**: Test single-request vs. batch inference on a GPU.

---

## Further Reading
- [[21 Neural Networks Basics]]
- [[48 Model Serving]]
- [[55 AI System Design Basics]]
- [[47 FastAPI Basics]]