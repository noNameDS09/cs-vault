---
tags: [machine-learning, gate-da, feedforward, neural-networks, revision]
---

# 16 Feed Forward Neural Network

> [!note] Neural network with no cycles — information flows only forward from input to output

---

## Overview

Feedforward Neural Networks (FFNN) are the foundational neural network architecture where connections don't form cycles. MLP is a type of FFNN. This note covers the general architecture, computation graph, and training principles applicable to all feedforward networks.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Acyclic Graph** | No loops — information flows one direction |
| **Layers** | Sequential transformations $x \to h_1 \to h_2 \to ... \to \hat{y}$ |
| **Computation Graph** | DAG of operations for automatic differentiation |
| **Forward Pass** | Evaluate network from input to output |
| **Backward Pass** | Compute gradients via reverse-mode autodiff |
| **Depth** | Number of hidden layers |

---

## Formulae

### General Feedforward Computation
For a network with $L$ layers (including output):
$$
a^{[0]} = x
$$
For $l = 1$ to $L$:
$$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
$$
$$
a^{[l]} = \phi^{[l]}(z^{[l]})
$$
Output: $\hat{y} = a^{[L]}$

### Loss Function
$$
J(\theta) = \frac{1}{n}\sum_{i=1}^n \mathcal{L}(y^{(i)}, \hat{y}^{(i)}) + \Omega(\theta)
$$
where $\Omega$ = regularization (L2, dropout, etc.)

### Backpropagation (Reverse-Mode AD)

**Chain Rule**: For scalar loss $J$:
$$
\frac{\partial J}{\partial z^{[l]}} = \frac{\partial J}{\partial a^{[l]}} \odot \phi'^{[l]}(z^{[l]})
$$
$$
\frac{\partial J}{\partial W^{[l]}} = \left(\frac{\partial J}{\partial z^{[l]}}\right) (a^{[l-1]})^T
$$
$$
\frac{\partial J}{\partial b^{[l]}} = \frac{\partial J}{\partial z^{[l]}}
$$
$$
\frac{\partial J}{\partial a^{[l-1]}} = (W^{[l]})^T \frac{\partial J}{\partial z^{[l]}}
$$

### Notation: Error Signal
$$
\delta^{[l]} \equiv \frac{\partial J}{\partial z^{[l]}} \quad \text{(same shape as } z^{[l]}\text{)}
$$

Then:
$$
\delta^{[L]} = \nabla_{a^{[L]}} \mathcal{L} \odot \phi'^{[L]}(z^{[L]})
$$
$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot \phi'^{[l]}(z^{[l]}) \quad \text{for } l = L-1, ..., 1
$$

### Gradient Descent Update
$$
W^{[l]} \leftarrow W^{[l]} - \eta \frac{\partial J}{\partial W^{[l]}}
$$
$$
b^{[l]} \leftarrow b^{[l]} - \eta \frac{\partial J}{\partial b^{[l]}}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $L$ | Total number of layers (1 = input, L = output) |
| $W^{[l]}$ | Weight matrix for layer $l$ |
| $b^{[l]}$ | Bias vector for layer $l$ |
| $z^{[l]}$ | Pre-activation (linear output) |
| $a^{[l]}$ | Post-activation |
| $\phi^{[l]}$ | Activation function for layer $l$ |
| $\delta^{[l]}$ | Error signal (gradient wrt $z^{[l]}$) |
| $\eta$ | Learning rate |

---

## Important Properties

### No Cycles = No Recurrence
- State at layer $l$ depends only on layer $l-1$
- Unlike RNNs: no memory of past inputs
- Fixed computation graph for given input size

### Universal Approximation
- FFNN with ≥1 hidden layer + non-linear activation = universal approximator
- Depth allows exponential efficiency for compositional functions

### Modularity
- Any differentiable operation can be a "layer"
- Conv, Pool, Attention, Residual blocks all fit FFNN framework
- Modern DL = sophisticated FFNNs with specialized layers

---

## Mathematical Intuition

**Function Composition**: FFNN computes $f = f_L \circ f_{L-1} \circ ... \circ f_1$ where $f_l(z) = \phi(Wz + b)$

**Manifold Learning**: Each layer transforms data manifold. Early layers: local features. Late layers: semantic concepts.

**Linear Regions**: Piecewise linear activations (ReLU) partition input space into convex polytopes. Network is linear within each region.

**Information Bottleneck**: Hidden layers compress input while preserving task-relevant information.

---

## Algorithms

### Forward Pass (Vectorized)
```python
def forward(X, params):
    a = X
    cache = []
    for l in range(1, L+1):
        z = W[l] @ a + b[l]
        a = activation[l](z)
        cache.append((a, z))  # store for backward
    return a, cache
```

### Backward Pass
```python
def backward(y_true, y_pred, cache, params):
    # Output layer
    delta = grad_loss(y_true, y_pred) * activation_prime[L](cache[L-1][1])
    
    grads = {}
    for l in range(L, 0, -1):
        a_prev = cache[l-2][0] if l > 1 else X
        grads['W'][l] = delta @ a_prev.T / n
        grads['b'][l] = delta.mean(axis=1, keepdims=True)
        if l > 1:
            delta = params['W'][l].T @ delta * activation_prime[l-1](cache[l-2][1])
    return grads
```

### Mini-batch SGD
```python
for epoch in range(epochs):
    for X_batch, y_batch in dataloader:
        y_pred, cache = forward(X_batch, params)
        grads = backward(y_batch, y_pred, cache, params)
        for l in range(1, L+1):
            params['W'][l] -= lr * (grads['W'][l] + weight_decay * params['W'][l])
            params['b'][l] -= lr * grads['b'][l]
```

---

## Complexity

| Operation | Time | Memory |
|-----------|------|--------|
| Forward | $O(\sum d_l d_{l-1})$ | $O(\sum d_l)$ (activations) |
| Backward | $O(\sum d_l d_{l-1})$ | $O(\sum d_l)$ |
| Parameters | $\sum d_l(d_{l-1}+1)$ | — |

*With batch size $B$: multiply by $B$ for activation memory*

---

## Comparison Tables

### FFNN Variants

| Architecture | Key Feature | Use Case |
|--------------|-------------|----------|
| **MLP** | Dense layers | Tabular data |
| **CNN** | Weight sharing (convolution) | Images, grids |
| **ResNet** | Skip connections | Very deep networks |
| **Transformer** | Self-attention | Sequences, NLP |
| **Autoencoder** | Bottleneck layer | Compression, pretraining |

### FFNN vs Recurrent (RNN)

| Aspect | FFNN | RNN |
|--------|------|-----|
| Memory | No (stateless) | Yes (hidden state) |
| Input Size | Fixed | Variable (sequence) |
| Cycles | No | Yes (recurrent) |
| Parallelization | Full (across batch) | Limited (sequential) |
| Backprop | Standard | BPTT (unrolled) |

---

## GATE Tricks

> [!tip] **FFNN Quick Rules**
> - **FFNN = Acyclic** = no loops, no memory
> - **MLP ⊂ FFNN** = MLP is dense FFNN
> - **CNN, ResNet, Transformer** = specialized FFNNs
> - **Forward pass** = evaluate function
> - **Backward pass** = reverse-mode autodiff (chain rule)
> - **Computational graph** = DAG of operations
> - **Depth** = number of hidden layers

> [!warning] **GATE Traps**
> - **FFNN ≠ RNN** — FFNN has no cycles, no state
> - **Fixed input size** — can't handle variable-length sequences natively
> - **No weight sharing** in standard MLP (unlike CNN)
> - **Vanishing gradients** in deep FFNN → use skip connections, good init
> - **Autoencoder** is FFNN with bottleneck (unsupervised)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| FFNN | RNN | Acyclic vs cyclic |
| MLP | FFNN | MLP is fully connected FFNN |
| FFNN | CNN | Dense vs convolutional (weight sharing) |
| Feedforward | Backprop | Forward = compute; Backward = gradients |
| Depth | Width | Layers vs neurons per layer |

---

## Common Mistakes

1. **Confusing FFNN with RNN** — FFNN has no memory/recurrence
2. **Thinking CNN is not FFNN** — CNN is feedforward (just with conv layers)
3. **Assuming FFNN handles sequences** — needs fixed input, use RNN/Transformer
4. **Ignoring computational graph** — essential for autodiff frameworks
5. **Not storing activations** — needed for backward pass!

---

## Memory Tricks

> [!tip] **Feedforward** = "Feed forward" = data flows one way
> 
> **FFNN** = **F**eed **F**orward **N**eural **N**etwork
> 
> **No cycles** = **N**o **C**ycles = **N**o **R**ecurrence
> 
> **MLP** = **M**ost **L**ayered **P**erceptron (dense FFNN)

---

## Previous GATE Patterns

- **Conceptual**: Distinguish FFNN from RNN/CNN
- **Architecture**: Identify if given network is feedforward
- **Computation**: Forward/backward pass equations
- **Universal Approximation**: Conditions for FFNN
- **Autoencoder**: FFNN with bottleneck for dimensionality reduction

---

## Revision Summary

```
FEEDFORWARD NEURAL NETWORK (FFNN)
├── Acyclic: no loops, no memory, fixed input size
├── Computation: a⁰=x, zˡ=Wˡaˡ⁻¹+bˡ, aˡ=φ(zˡ), ŷ=aᴸ
├── MLP: fully connected FFNN (dense layers)
├── CNN, ResNet, Transformer = specialized FFNNs
├── Backprop: reverse-mode autodiff on computation graph
│   δᴸ = ∇ₐL ⊙ φ'(zᴸ)
│   δˡ = (Wˡ⁺¹)ᵀδˡ⁺¹ ⊙ φ'(zˡ)
│   ∂J/∂Wˡ = δˡ(aˡ⁻¹)ᵀ
├── Universal approximator: 1 hidden layer + non-linearity
├── Fixed input size (unlike RNN)
├── No weight sharing (unlike CNN)
└── Autoencoder = FFNN with bottleneck (unsupervised)
```

---

## Related Notes

- [[14 Neural Networks]] (General concepts)
- [[15 Multi Layer Perceptron]] (Dense FFNN)
- [[17 Unsupervised Learning]] (Autoencoders)
- [[Formula Sheet]]

---

#machine-learning #gate-da #feedforward #neural-networks #revision