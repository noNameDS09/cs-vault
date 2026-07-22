# 23 Activation Functions

tags:
#deep-learning
#activation-functions
#neural-networks
#placements
#interview

---

## Why this topic matters
Activation functions are what make neural networks **powerful**. Without them, a neural network is just a fancy linear regression. They introduce **non-linearity**, allowing networks to learn complex patterns like images, speech, and text.

## Learning Objectives
- Understand why we need activation functions.
- Learn about Sigmoid, Tanh, ReLU, and Softmax.
- Understand the Vanishing Gradient problem.
- Know which activation to use where.

## Prerequisites
- [[21 Neural Networks Basics]]
- [[22 Backpropagation]]

---

## Intuition
Imagine a **light switch** in your brain.

- **Without activation**: The light gradually gets brighter as you turn the knob. Linear, boring.
- **With activation**: The light is either **ON** or **OFF**. Or maybe it has multiple modes: DIM, BRIGHT, BLINKING.

Activation functions decide: **"Should this neuron fire? How strongly?"**

They add the "decision-making" capability to each neuron, allowing the network to learn complex, non-linear relationships.

---

## Detailed Explanation

### Why Do We Need Activation Functions?

Without activation functions, a neural network is just:
```
Output = W3(W2(W1 × Input + b1) + b2) + b3
```
This simplifies to:
```
Output = W_combined × Input + b_combined
```
Which is just... **Linear Regression**! No matter how many layers you stack, it collapses into a single linear function.

**Activation functions add non-linearity**, allowing the network to approximate any function (Universal Approximation Theorem).

### Common Activation Functions

#### 1. Sigmoid (Logistic)

**Formula**: `σ(x) = 1 / (1 + e^(-x))`

**Range**: 0 to 1

**Use Case**: 
- Output layer for **binary classification** (probability).
- **Not recommended** for hidden layers (vanishing gradient).

```
Input → -3 → -1 → 0 → 1 → 3
Output → 0.05 → 0.27 → 0.5 → 0.73 → 0.95
```

**Pros**: Smooth gradient, interpretable (probability).
**Cons**: Vanishing gradient, not zero-centered.

#### 2. Tanh (Hyperbolic Tangent)

**Formula**: `tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))`

**Range**: -1 to 1

**Use Case**: 
- Hidden layers (better than Sigmoid).
- Zero-centered (helps with gradient flow).

**Pros**: Zero-centered, stronger gradients than Sigmoid.
**Cons**: Still suffers from vanishing gradient.

#### 3. ReLU (Rectified Linear Unit) ⭐ MOST POPULAR

**Formula**: `f(x) = max(0, x)`

**Range**: 0 to ∞

**Use Case**: 
- **Default choice** for hidden layers.
- Works well for most deep learning problems.

```
Input → -2 → -1 → 0 → 1 → 2
Output → 0 → 0 → 0 → 1 → 2
```

**Pros**: 
- Computationally efficient (just max operation).
- Solves vanishing gradient (for positive values).
- Sparse activation (some neurons are completely off).

**Cons**: 
- "Dying ReLU" problem (neurons can get stuck at 0).
- Not zero-centered.

#### 4. Leaky ReLU

**Formula**: `f(x) = x if x > 0 else 0.01x`

**Range**: -∞ to ∞ (small negative values allowed)

**Use Case**: 
- Alternative to ReLU to prevent "Dying ReLU."

**Pros**: Fixes dying ReLU problem.
**Cons**: Slightly more computation.

#### 5. Softmax

**Formula**: `σ(z)_i = e^(z_i) / Σ e^(z_j)`

**Range**: 0 to 1 (all outputs sum to 1)

**Use Case**: 
- **Output layer for multi-class classification**.
- Converts raw scores to probabilities.

```
Raw Scores → [2.0, 1.0, 0.1]
Softmax → [0.66, 0.24, 0.10]  # 66% Class 1, 24% Class 2, 10% Class 3
```

**Pros**: Great for multi-class, interpretable.
**Cons**: Only for output layer, computationally expensive.

### Comparison Table

| Activation | Range | Best For | Vanishing Gradient? |
| :--- | :--- | :--- | :--- |
| **Sigmoid** | 0 to 1 | Binary output | ❌ Yes |
| **Tanh** | -1 to 1 | Hidden layers | ❌ Yes (less than Sigmoid) |
| **ReLU** | 0 to ∞ | **Hidden layers (default)** | ✅ No (for positive) |
| **Leaky ReLU** | -∞ to ∞ | Hidden layers | ✅ No |
| **Softmax** | 0 to 1 (sum=1) | Multi-class output | N/A |

```mermaid
graph LR
    subgraph "Binary Classification"
    Sigmoid[Sigmoid Output]
    end
    
    subgraph "Multi-Class Classification"
    Softmax[Softmax Output]
    end
    
    subgraph "Hidden Layers"
    ReLU[ReLU (Recommended)]
    Tanh[Tanh (Alternative)]
    end
```

---

## Real-world Example

**Image Classification (Cat vs. Dog vs. Bird)**

- **Hidden Layers**: Use **ReLU** to learn complex features (edges, textures, shapes).
- **Output Layer**: Use **Softmax** to output probabilities:
  - Cat: 75%
  - Dog: 20%
  - Bird: 5%

---

## Advantages
- **Non-Linearity**: Enables learning complex patterns.
- **Decision Making**: Neurons can "decide" to fire or not.
- **Gradient Flow**: Proper activations enable effective backpropagation.

## Limitations
- **Choice Matters**: Wrong activation can kill training (vanishing gradient).
- **ReLU Limitations**: Can cause "dead neurons."
- **Not Universal**: Different tasks need different activations.

---

## Common Interview Questions
- **Why do we need activation functions?**
- **What is the difference between Sigmoid and ReLU?**
- **Why is ReLU the default choice for hidden layers?**
- **What is the Vanishing Gradient problem?**
- **When do you use Softmax?**
- **What is the "Dying ReLU" problem?**

### Interview Answer Tips
- Emphasize that **without activation, neural networks collapse to linear regression**.
- ReLU is default because it's **simple, fast, and solves vanishing gradient**.
- Softmax is for **multi-class**, Sigmoid is for **binary**.

---

## Common Mistakes
- Using Sigmoid in hidden layers of deep networks (vanishing gradient).
- Using Softmax for binary classification (use Sigmoid).
- Using ReLU for output regression (use linear/identity).
- Not normalizing data before using certain activations.

---

## Summary
Activation functions add non-linearity to neural networks. **ReLU** is the default for hidden layers. **Sigmoid** is for binary output. **Softmax** is for multi-class output. Choosing the right activation is critical for successful training.

---

## Practice Questions
1. What happens if you remove activation functions from a neural network?
2. Why is ReLU better than Sigmoid for hidden layers?
3. What is the output range of Tanh?
4. When would you use Leaky ReLU instead of ReLU?
5. Why can't we use Softmax for binary classification?
6. What is the Vanishing Gradient problem?
7. Why is Sigmoid not zero-centered and why does it matter?

---

## Mini Project Ideas
1. **Activation Comparison**: Train the same network with Sigmoid, Tanh, and ReLU. Compare convergence speed.
2. **Dying ReLU Demo**: Build a network and track how many neurons become "dead" (always output 0).
3. **Visualization**: Plot all activation functions and their derivatives to understand gradient flow.

---

## Further Reading
- [[21 Neural Networks Basics]]
- [[22 Backpropagation]]
- [[24 CNN Basics]]
- [[09 Bias-Variance Tradeoff]]