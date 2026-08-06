---
tags: [machine-learning, gate-da, mlp, neural-networks, revision]
---

# 15 Multi Layer Perceptron (MLP)

> [!note] Fully connected feedforward neural network with one or more hidden layers

---

## Overview

MLP is the classic neural network architecture: input layer → hidden layer(s) → output layer, with all neurons fully connected between adjacent layers. It's a universal function approximator.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Fully Connected** | Every neuron connects to all neurons in adjacent layers |
| **Hidden Layers** | Layers between input and output (at least 1 for MLP) |
| **Non-Linearity** | Activation function enabling complex functions |
| **Depth** | Number of hidden layers + 1 |
| **Width** | Number of neurons per layer |
| **Backpropagation** | Training algorithm using chain rule |

---

## Formulae

### Architecture (L layers, L-1 hidden)
```
Input (d₀) → Hidden₁ (d₁) → Hidden₂ (d₂) → ... → Hidden_{L-1} (d_{L-1}) → Output (d_L)
```

### Forward Pass
For $l = 1$ to $L$:
$$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
$$
$$
a^{[l]} = g^{[l]}(z^{[l]})
$$
with $a^{[0]} = x$ (input), $\hat{y} = a^{[L]}$

### Hidden Layer Activations
- **ReLU** (default): $g(z) = \max(0, z)$
- **Tanh**: $g(z) = \tanh(z)$
- **Sigmoid**: Rarely used in hidden layers (vanishing gradient)

### Output Layer by Task

| Task | Output Activation | Loss |
|------|-------------------|------|
| Regression | Linear ($g(z)=z$) | MSE |
| Binary Classification | Sigmoid | BCE |
| Multi-class (K classes) | Softmax | CCE |

### Loss Functions

**MSE (Regression)**:
$$
J = \frac{1}{2n}\sum_{i=1}^n ||y^{(i)} - \hat{y}^{(i)}||^2
$$

**Binary Cross-Entropy**:
$$
J = -\frac{1}{n}\sum_{i=1}^n [y^{(i)} \log \hat{y}^{(i)} + (1-y^{(i)})\log(1-\hat{y}^{(i)})]
$$

**Categorical Cross-Entropy**:
$$
J = -\frac{1}{n}\sum_{i=1}^n \sum_{k=1}^K y_k^{(i)} \log \hat{y}_k^{(i)}
$$

### Backpropagation (Chain Rule)

**Output Layer Error**:
$$
\delta^{[L]} = \nabla_{a^{[L]}} J \odot g'^{[L]}(z^{[L]})
$$

**Hidden Layer Error** (for $l = L-1, ..., 1$):
$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot g'^{[l]}(z^{[l]})
$$

**Gradients**:
$$
\frac{\partial J}{\partial W^{[l]}} = \frac{1}{n} \delta^{[l]} (a^{[l-1]})^T + \lambda W^{[l]} \quad \text{(with L2 reg)}
$$
$$
\frac{\partial J}{\partial b^{[l]}} = \frac{1}{n} \sum_{i=1}^n \delta^{[l](i)}
$$

### Special Gradients (Output Layer)

**Softmax + CCE**:
$$
\delta^{[L]} = \hat{y} - y
$$

**Sigmoid + BCE**:
$$
\delta^{[L]} = \hat{y} - y
$$

**Linear + MSE**:
$$
\delta^{[L]} = (\hat{y} - y) \odot g'^{[L]}(z^{[L]}) = \hat{y} - y \quad \text{(since } g'(z)=1\text{)}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $L$ | Total layers (including output) |
| $d_l$ | Width of layer $l$ ($d_0$ = input dim, $d_L$ = output dim) |
| $W^{[l]}$ | Weights $(d_l \times d_{l-1})$ |
| $b^{[l]}$ | Biases $(d_l \times 1)$ |
| $\delta^{[l]}$ | Error signal at layer $l$ |

---

## Important Properties

### Universal Approximation
- **1 hidden layer + enough neurons** = universal approximator
- **But**: May need exponentially many neurons
- **Deep (multiple layers)** = exponentially more efficient for some functions

### Parameter Count
$$
\text{Params} = \sum_{l=1}^L (d_l \cdot d_{l-1} + d_l) = \sum_{l=1}^L d_l(d_{l-1} + 1)
$$

### Depth vs Width Tradeoff
| Aspect | Deep (many layers) | Wide (many neurons) |
|--------|-------------------|-------------------|
| Parameters | Fewer for same expressivity | More |
| Training | Harder (vanishing grad) | Easier |
| Feature Learning | Hierarchical | Shallow |
| Generalization | Often better | Can overfit |

---

## Mathematical Intuition

**Composition**: MLP computes $f(x) = f_L \circ f_{L-1} \circ ... \circ f_1(x)$ where $f_l(z) = g(Wz + b)$

**Feature Hierarchy**: Early layers learn simple features (edges, textures), later layers compose them into complex concepts.

**ReLU Networks = Piecewise Linear**: Each ReLU creates linear regions. Network partitions input space into convex polytopes.

**Residual Connections**: $a^{[l]} = g(W^{[l]}a^{[l-1]} + b^{[l]} + a^{[l-1]})$ enables very deep networks (ResNet).

---

## Algorithms

### Training Procedure
```
1. Initialize weights (He for ReLU, Xavier for Tanh)
2. For epoch in 1..max_epochs:
   For each minibatch:
     Forward pass: compute a^[l] for all layers
     Compute loss J
     Backward pass: compute δ^[l] from output to input
     Compute gradients ∂J/∂W, ∂J/∂b
     Update: W -= lr * (∂J/∂W + λW), b -= lr * ∂J/∂b
   Evaluate on validation set
   Early stopping if no improvement
```

### Hyperparameters
| Hyperparameter | Typical Range |
|----------------|---------------|
| Hidden layers | 1-5 |
| Neurons per layer | 32-1024 (often decreasing) |
| Learning rate | 1e-4 to 1e-2 |
| Batch size | 32, 64, 128, 256 |
| L2 regularization (λ) | 1e-6 to 1e-2 |
| Dropout rate | 0.1 to 0.5 |

---

## Complexity

| Aspect | Complexity |
|--------|------------|
| Forward Pass | $O(\sum d_l d_{l-1})$ |
| Backward Pass | $O(\sum d_l d_{l-1})$ |
| Parameters | $\sum d_l(d_{l-1} + 1)$ |
| Memory (activations) | $O(\sum d_l \times \text{batch})$ |

---

## Comparison Tables

### MLP vs Other Models

| Aspect | MLP | Linear/Logistic | SVM (RBF) | Decision Tree |
|--------|-----|----------------|-----------|---------------|
| Non-linearity | Yes (deep) | No | Yes (kernel) | Yes |
| Feature Learning | Yes | No | No | Implicit |
| Scalability | Good (GPU) | Excellent | Poor (large n) | Good |
| Interpretability | Low | High | Low | High |
| Feature Scaling | **Critical** | Helpful | **Critical** | Not needed |

### MLP vs CNN/RNN

| Aspect | MLP | CNN | RNN |
|--------|-----|-----|-----|
| Input Type | Tabular (fixed) | Images (grid) | Sequences |
| Weight Sharing | No | **Yes** (filters) | **Yes** (recurrent) |
| Spatial/Temporal | No | Yes (translation inv.) | Yes (order matters) |

---

## GATE Tricks

> [!tip] **MLP Quick Rules**
> - **Input dim = features**, Output dim = classes (or 1 for regression/binary)
> - **ReLU + He init** = standard hidden layer config
> - **Softmax + CCE** gradient = $\hat{y} - y$ (simple!)
> - **Sigmoid + BCE** gradient = $\hat{y} - y$ (simple!)
> - **Always scale features** (StandardScaler or MinMax)
> - **Early stopping** on validation loss = best regularization
> - **Dropout** only during training, scale at test

> [!warning] **GATE Traps**
> - **Output activation matters**: Linear for regression, Sigmoid for binary, Softmax for multi-class
> - **Loss must match output**: MSE + Linear, BCE + Sigmoid, CCE + Softmax
> - **Don't use Sigmoid/Tanh in deep hidden layers** (vanishing gradient)
> - **Parameter count** = $\sum d_l(d_{l-1}+1)$ — often asked!
> - **XOR needs hidden layer** — single perceptron can't solve

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| MLP | Perceptron | MLP has hidden layers, non-linear |
| MLP | Deep Network | MLP = any depth; "Deep" = many layers |
| Backprop | Gradient Descent | Backprop computes gradients; GD uses them |
| Epoch | Iteration | Epoch = full dataset; Iteration = one batch |

---

## Common Mistakes

1. **Sigmoid output for multi-class** → use Softmax!
2. **MSE with Softmax** → use Cross-Entropy!
3. **No hidden layer for non-linear problem** → linear separator only
4. **All same layer widths** → often better to taper (e.g., 256-128-64)
5. **No validation set** → can't early stop or tune hyperparameters

---

## Memory Tricks

> [!tip] **MLP** = **M**ulti **L**ayer **P**erceptron = Perceptrons stacked
> 
> **Softmax + CCE** = "Target minus prediction" = $\hat{y} - y$
> 
> **Sigmoid + BCE** = "Target minus prediction" = $\hat{y} - y$
> 
> **He init** = **H**e for **Re**LU
> 
> **Taper layers** = "Funnel shape" (256→128→64)

---

## Previous GATE Patterns

- **Numerical**: Parameter count for given architecture
- **Forward/Backward**: One step computation for small net
- **Activation choice**: Why ReLU over Sigmoid
- **Output layer**: Match activation to task
- **Gradient**: Softmax+CCE = $\hat{y}-y$ simplification
- **Architecture**: Minimum layers for XOR

---

## Revision Summary

```
MULTI-LAYER PERCEPTRON (MLP)
├── Architecture: Input(d₀) → Hidden₁(d₁) → ... → Hidden_{L-1} → Output(d_L)
├── Forward: zˡ = Wˡaˡ⁻¹ + bˡ, aˡ = g(zˡ)
├── Hidden: ReLU (default) + He init
├── Output: Linear+MSE (reg), Sigmoid+BCE (binary), Softmax+CCE (multi)
├── Backprop: δᴸ = ŷ-y (for Softmax/CCE or Sigmoid/BCE)
│   δˡ = (Wˡ⁺¹)ᵀδˡ⁺¹ ⊙ g'(zˡ)
│   ∂J/∂Wˡ = δˡ(aˡ⁻¹)ᵀ/n + λWˡ
├── Params: Σ dₗ(dₗ₋₁+1)
├── Universal Approximator: 1 hidden layer (wide enough)
├── Feature scaling: MANDATORY
├── Regularization: L2, Dropout, BatchNorm, Early Stopping
└── XOR problem: needs ≥1 hidden layer
```

---

## Related Notes

- [[14 Neural Networks]] (General NN concepts)
- [[16 Feed Forward Neural Network]] (Broader class)
- [[06 Logistic Regression]] (Single neuron MLP)
- [[Formula Sheet]]

---

#machine-learning #gate-da #mlp #neural-networks #revision