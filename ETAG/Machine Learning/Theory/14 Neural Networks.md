---
tags: [machine-learning, gate-da, neural-networks, deep-learning, revision]
---

# 14 Neural Networks

> [!note] Composable differentiable functions with learnable parameters — universal function approximators

---

## Overview

Neural networks are parametric models composed of layers of neurons. Each neuron computes a weighted sum of inputs followed by a non-linear activation. Deep networks (many layers) can approximate any continuous function.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Neuron/Unit** | Computes $a = g(w^T x + b)$ |
| **Layer** | Collection of neurons operating in parallel |
| **Input Layer** | Receives features (no computation) |
| **Hidden Layers** | Intermediate transformations |
| **Output Layer** | Final predictions |
| **Weights** | Learnable parameters $W$ |
| **Biases** | Learnable offsets $b$ |
| **Activation** | Non-linear function $g$ |
| **Forward Pass** | Compute output from input |
| **Backpropagation** | Compute gradients via chain rule |

---

## Formulae

### Single Neuron
$$
z = w^T x + b = \sum_{j=1}^p w_j x_j + b
$$
$$
a = g(z)
$$

### Layer Forward Pass (Vectorized)
$$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
$$
$$
a^{[l]} = g^{[l]}(z^{[l]})
$$

### Common Activation Functions

| Name | Formula | Derivative | Range |
|------|---------|------------|-------|
| **Sigmoid** | $\sigma(z) = \frac{1}{1+e^{-z}}$ | $\sigma(z)(1-\sigma(z))$ | $(0,1)$ |
| **Tanh** | $\tanh(z) = \frac{e^z-e^{-z}}{e^z+e^{-z}}$ | $1-\tanh^2(z)$ | $(-1,1)$ |
| **ReLU** | $\max(0,z)$ | $\begin{cases}1 & z>0\\0 & z\leq0\end{cases}$ | $[0,\infty)$ |
| **Leaky ReLU** | $\max(\alpha z, z)$ | $\begin{cases}1 & z>0\\\alpha & z\leq0\end{cases}$ | $\mathbb{R}$ |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | $\text{diag}(s) - ss^T$ | $(0,1), \sum=1$ |

### Loss Functions

**Regression (MSE)**:
$$
J = \frac{1}{2n}\sum_{i=1}^n ||y^{(i)} - \hat{y}^{(i)}||^2_2
$$

**Binary Classification (Binary Cross-Entropy)**:
$$
J = -\frac{1}{n}\sum_{i=1}^n [y^{(i)} \log \hat{y}^{(i)} + (1-y^{(i)})\log(1-\hat{y}^{(i)})]
$$

**Multi-class Classification (Categorical Cross-Entropy)**:
$$
J = -\frac{1}{n}\sum_{i=1}^n \sum_{k=1}^K y_k^{(i)} \log \hat{y}_k^{(i)}
$$

**Regularized Loss**:
$$
J_{reg} = J + \frac{\lambda}{2} \sum_l ||W^{[l]}||^2_F
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $L$ | Number of layers |
| $n^{[l]}$ | Number of units in layer $l$ |
| $W^{[l]}$ | Weight matrix $(n^{[l]} \times n^{[l-1]})$ |
| $b^{[l]}$ | Bias vector $(n^{[l]} \times 1)$ |
| $z^{[l]}$ | Linear output (pre-activation) |
| $a^{[l]}$ | Activation (post-activation) |
| $g^{[l]}$ | Activation function for layer $l$ |
| $J$ | Cost/loss function |

---

## Important Properties

### Universal Approximation Theorem
A feedforward network with **one hidden layer** and **finite neurons** can approximate any continuous function on compact domain (given enough neurons).

### Depth vs Width
- **Deep (many layers)**: Hierarchical feature learning, fewer parameters for same expressivity
- **Wide (many neurons per layer)**: Can approximate any function with 1 hidden layer

### Non-Convex Optimization
- Loss surface has many local minima, saddle points
- Gradient descent finds good solutions in practice
- Proper initialization critical (Xavier, He)

### Overparameterization
- Modern networks often have more parameters than samples
- Yet generalize well (double descent phenomenon)
- Implicit regularization from SGD

---

## Mathematical Intuition

**Composition of Functions**: Network = $f(x) = f_L \circ f_{L-1} \circ ... \circ f_1(x)$ where $f_l(z) = g(Wz + b)$

**Gradient Flow**: Chain rule propagates gradients backward:
$$
\frac{\partial J}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T
$$
where $\delta^{[l]}$ = error signal at layer $l$

**ReLU Networks = Piecewise Linear**: Each neuron is linear in regions, creating piecewise linear decision boundaries.

**Skip Connections (ResNet)**: $a^{[l]} = g(z^{[l]} + a^{[l-1]})$ — solves vanishing gradient in very deep nets.

---

## Algorithms

### Forward Propagation
```python
a = X
for l in range(1, L+1):
    z = W[l] @ a + b[l]
    a = activation[l](z)
return a
```

### Backpropagation
```python
# Output layer
delta = grad_loss(y, a[L]) * activation_prime[L](z[L])

# Hidden layers (backward)
for l in range(L, 0, -1):
    dW[l] = delta @ a[l-1].T / n
    db[l] = delta.mean(axis=1, keepdims=True)
    delta = (W[l].T @ delta) * activation_prime[l](z[l])

# Update
for l in range(1, L+1):
    W[l] -= lr * dW[l]
    b[l] -= lr * db[l]
```

### Weight Initialization

| Method | Formula | Best For |
|--------|---------|----------|
| **Xavier/Glorot** | $W \sim U[-\frac{\sqrt{6}}{\sqrt{n_{in}+n_{out}}}, \frac{\sqrt{6}}{\sqrt{n_{in}+n_{out}}}]$ | Tanh, Sigmoid |
| **He** | $W \sim N(0, \frac{2}{n_{in}})$ | ReLU, Leaky ReLU |

### Optimizers

| Optimizer | Update Rule |
|-----------|-------------|
| **SGD** | $W \leftarrow W - \alpha \nabla J$ |
| **Momentum** | $v \leftarrow \beta v + (1-\beta)\nabla J$, $W \leftarrow W - \alpha v$ |
| **Adam** | Adaptive LR per parameter (momentum + RMSprop) |

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Forward Pass | $O(\sum n^{[l]} n^{[l-1]})$ | $O(\sum n^{[l]})$ |
| Backward Pass | $O(\sum n^{[l]} n^{[l-1]})$ | $O(\sum n^{[l]})$ |
| Parameters | $\sum n^{[l]} n^{[l-1]} + n^{[l]}$ | — |

---

## Comparison Tables

### Activation Functions

| Property | Sigmoid | Tanh | ReLU | Leaky ReLU |
|----------|---------|------|------|------------|
| Zero-centered | No | **Yes** | No | No |
| Saturates | Both sides | Both sides | One side | No |
| Derivative | Max 0.25 | Max 1 | 0 or 1 | $\alpha$ or 1 |
| Dead Neurons | No | No | Yes | **Fixed** |

### Output Layer by Task

| Task | Activation | Loss |
|------|------------|------|
| Regression | Linear (none) | MSE |
| Binary Classification | Sigmoid | Binary CE |
| Multi-class Classification | Softmax | Categorical CE |
| Multi-label Classification | Sigmoid (per class) | Binary CE |

---

## GATE Tricks

> [!tip] **Neural Networks Quick Rules**
> - **ReLU default** for hidden layers (fast, no vanishing gradient for $z>0$)
> - **He init** for ReLU, **Xavier** for Tanh/Sigmoid
> - **Softmax + Cross-Entropy** for multi-class (gradient simplifies nicely)
> - **Sigmoid + BCE** for binary/multi-label
> - **Batch Norm** after linear, before activation (stabilizes training)
> - **Dropout** at training only (scales by $1/(1-p)$ at test)
> - **Adam** = good default optimizer

> [!warning] **GATE Traps**
> - **Vanishing gradients** with Sigmoid/Tanh in deep nets
> - **Dead ReLUs** (always output 0) → use Leaky ReLU
> - **Softmax gradient** = $\hat{y} - y$ (same as logistic regression!)
> - **Initialization matters** — all zeros = symmetry breaking failure
> - **Feature scaling critical** for NN (gradients explode/vanish)
> - **No free lunch** — shallow networks can't learn complex patterns efficiently

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Epoch | Iteration | Epoch = full pass; Iteration = one batch |
| Batch Size | Mini-batch | Same thing |
| Backprop | Chain Rule | Backprop = algorithm using chain rule |
| Parameters | Hyperparameters | Learned vs set before training |
| Overfitting | Underfitting | Train error low vs high |

---

## Common Mistakes

1. **No feature scaling** → slow/no convergence
2. **All-zero initialization** → symmetry, no learning
3. **Sigmoid in deep hidden layers** → vanishing gradients
4. **No regularization** → severe overfitting
5. **Dropout at test time** → wrong predictions (must scale or disable)
6. **Softmax for multi-label** → use sigmoid per class instead

---

## Memory Tricks

> [!tip] **ReLU** = "Rectified Linear Unit" = max(0,z)
> 
> **He init** = "He" for **Re**LU (2/fan_in)
> 
> **Xavier** = "Glorot" for tanh/sigmoid
> 
> **Softmax** = "Soft maximum" = smooth argmax
> 
> **Adam** = **Ad**aptive **M**oment estimation

---

## Previous GATE Patterns

- **Numerical**: One step of forward/backward pass for small network
- **Activation derivatives**: Compute $\sigma'(z)$, ReLU', etc.
- **Initialization**: Xavier vs He formulas
- **Loss gradients**: Cross-entropy + Softmax = $\hat{y} - y$
- **Architecture**: Parameter count calculation
- **Vanishing gradient**: Why ReLU helps

---

## Revision Summary

```
NEURAL NETWORKS
├── Neuron: a = g(wᵀx + b)
├── Layer: z = Wa + b, a = g(z)
├── Activations: ReLU (default), Tanh, Sigmoid, Softmax
├── Loss: MSE (reg), BCE (binary), CCE (multi-class)
├── Init: He (ReLU), Xavier (Tanh/Sigmoid)
├── Backprop: Chain rule backward
│   ├── δᴸ = ∇ₐJ ⊙ g'(zᴸ)
│   ├── δˡ = (Wˡ⁺¹)ᵀδˡ⁺¹ ⊙ g'(zˡ)
│   ├── ∂J/∂Wˡ = δˡ(aˡ⁻¹)ᵀ
├── Optimizers: SGD, Momentum, Adam
├── Regularization: L2, Dropout, BatchNorm, Early Stopping
├── Universal Approximation: 1 hidden layer sufficient (wide)
└── Deep = hierarchical features, fewer params
```

---

## Related Notes

- [[15 Multi Layer Perceptron]] (Specific architecture)
- [[16 Feed Forward Neural Network]] (General class)
- [[06 Logistic Regression]] (Single neuron with sigmoid)
- [[Formula Sheet]]

---

#machine-learning #gate-da #neural-networks #deep-learning #revision