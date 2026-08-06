---
tags: [machine-learning, gate-da, svm, classification, revision]
---

# 10 Support Vector Machine (SVM)

> [!note] Max-margin classifier finding optimal separating hyperplane with maximal geometric margin

---

## Overview

SVM finds the hyperplane that maximizes the margin (distance to nearest data points). Uses kernel trick for non-linear boundaries. Only support vectors (boundary points) determine the solution.

---

## Key Concepts

| Concept             | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Hyperplane**      | $w^T x + b = 0$ (decision boundary)                          |
| **Margin**          | Distance from hyperplane to nearest points: $\frac{2}{w}$    |
| **Support Vectors** | Points with $\alpha_i > 0$ (define the boundary)             |
| **Hard Margin**     | Linearly separable data, no misclassification allowed        |
| **Soft Margin**     | Allows slack variables $\xi_i$ for non-separable data        |
| **Kernel Trick**    | Implicit mapping to high-dimensional space via $K(x_i, x_j)$ |
| **C Parameter**     | Regularization: trade-off margin vs misclassification        |

---

## Formulae

### Hard Margin SVM (Linearly Separable)

**Primal**:
$$
\min_{w,b} \frac{1}{2} ||w||^2 \quad \text{s.t.} \quad y_i(w^T x_i + b) \geq 1 \quad \forall i
$$

**Lagrangian**:
$$
L(w,b,\alpha) = \frac{1}{2}||w||^2 - \sum_{i=1}^n \alpha_i [y_i(w^T x_i + b) - 1]
$$

**Dual** (after KKT conditions):
$$
\max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j y_i y_j x_i^T x_j
$$
$$
\text{s.t.} \quad \alpha_i \geq 0, \quad \sum_{i=1}^n \alpha_i y_i = 0
$$

**Solution**:
$$
w = \sum_{i=1}^n \alpha_i y_i x_i
$$
$$
b = y_k - w^T x_k \quad \text{for any } \alpha_k > 0
$$

**Decision Function**:
$$
f(x) = \text{sign}\left( \sum_{i=1}^n \alpha_i y_i x_i^T x + b \right)
$$

---

### Soft Margin SVM (Non-Separable)

**Primal**:
$$
\min_{w,b,\xi} \frac{1}{2} ||w||^2 + C \sum_{i=1}^n \xi_i
$$
$$
\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0
$$

**Dual**:
$$
\max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j y_i y_j x_i^T x_j
$$
$$
\text{s.t.} \quad 0 \leq \alpha_i \leq C, \quad \sum_{i=1}^n \alpha_i y_i = 0
$$

**Key Difference**: $\alpha_i$ now upper-bounded by $C$

**KKT Conditions**:
- $\alpha_i = 0$ → correctly classified, outside margin ($y_i(w^T x_i + b) > 1$)
- $0 < \alpha_i < C$ → on margin ($y_i(w^T x_i + b) = 1$)
- $\alpha_i = C$ → inside margin or misclassified ($y_i(w^T x_i + b) < 1$)

---

### Kernel Trick

Replace $x_i^T x_j$ with kernel $K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$

**Common Kernels**:

| Kernel | Formula | Parameters |
|--------|---------|------------|
| Linear | $x_i^T x_j$ | None |
| Polynomial | $(\gamma x_i^T x_j + r)^d$ | $\gamma, r, d$ |
| RBF / Gaussian | $\exp(-\gamma ||x_i - x_j||^2)$ | $\gamma > 0$ |
| Sigmoid | $\tanh(\gamma x_i^T x_j + r)$ | $\gamma, r$ |

**Decision with Kernel**:
$$
f(x) = \text{sign}\left( \sum_{i=1}^n \alpha_i y_i K(x_i, x) + b \right)
$$

---

### Multi-Class SVM

- **One-vs-One**: $\frac{K(K-1)}{2}$ binary classifiers, majority vote
- **One-vs-Rest**: $K$ binary classifiers, choose max score
- **Crammer-Singer**: Single optimization (native multi-class)

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $w$ | Weight vector (normal to hyperplane) |
| $b$ | Bias term |
| $\alpha_i$ | Lagrange multipliers (dual variables) |
| $\xi_i$ | Slack variables (soft margin) |
| $C$ | Regularization parameter |
| $\gamma$ | RBF kernel parameter |
| Support Vectors | Points with $\alpha_i > 0$ |

---

## Important Properties

### Sparsity
- Only **support vectors** ($\alpha_i > 0$) matter for prediction
- Typically small fraction of training data
- Model size independent of $n$, depends on #SV

### Margin Maximization = Regularization
- Maximizing margin $\Leftrightarrow$ minimizing $||w||^2$
- Equivalent to structural risk minimization

### Convex Optimization
- Dual is convex QP → global optimum guaranteed
- KKT conditions necessary and sufficient

### Kernel Requirements
- Mercer's condition: $K$ must be positive semi-definite
- Gram matrix $K_{ij} = K(x_i, x_j)$ must be PSD

---

## Mathematical Intuition

**Geometric Margin**: Distance from $x$ to hyperplane = $\frac{|w^T x + b|}{||w||}$

**Functional Margin**: $y(w^T x + b)$ (scaled by $||w||$)

**Canonical Hyperplane**: Scale $w,b$ so min functional margin = 1
- Then geometric margin = $\frac{1}{||w||}$
- Maximizing margin $\Leftrightarrow$ minimizing $||w||^2$

**Support Vectors**: "Support" the margin boundaries — only these points define the solution.

**Kernel**: Computes inner product in feature space without explicitly mapping $\phi(x)$.

---

## Algorithms

### SMO (Sequential Minimal Optimization) — Standard SVM Solver
```
1. Initialize α = 0, b = 0
2. Repeat until convergence:
   a. Select two α_i, α_j to optimize (heuristics)
   b. Optimize analytically (2-variable QP)
   c. Update threshold b
3. Return α, b
```

### Primal Coordinate Descent (for Linear SVM)
```
1. Initialize w = 0
2. For each coordinate j:
   - Update w_j by minimizing objective
3. Efficient for large-scale linear SVM (Liblinear)
```

### Choosing C and Kernel Parameters
```
Grid Search with Cross-Validation:
C ∈ {0.01, 0.1, 1, 10, 100}
γ ∈ {0.01, 0.1, 1, 10, 100}  (for RBF)
```

---

## Complexity

| Aspect | Complexity |
|--------|------------|
| Training (General) | $O(n^2)$ to $O(n^3)$ |
| Training (Linear, Primal) | $O(np)$ |
| Prediction | $O(n_{SV} \cdot p)$ |
| Space | $O(n_{SV} \cdot p)$ |

*$n_{SV}$ = number of support vectors (typically << n)*

---

## Comparison Tables

### SVM vs Logistic Regression

| Aspect | SVM | Logistic Regression |
|--------|-----|---------------------|
| Loss | Hinge | Cross-entropy |
| Output | Decision value (or calibrated) | Probability |
| Sparsity | Yes (support vectors) | No |
| Outliers | Robust (hinge loss) | Sensitive (log loss) |
| Kernel | Native | Not native |
| Multi-class | OvO / OvR | Native (softmax) |

### Hard vs Soft Margin

| Aspect | Hard Margin | Soft Margin |
|--------|-------------|-------------|
| Data | Linearly separable | Any |
| Slack $\xi_i$ | Not allowed | Allowed |
| $\alpha_i$ bounds | $\alpha_i \geq 0$ | $0 \leq \alpha_i \leq C$ |
| $C$ parameter | $\infty$ | Finite |

### Kernel Comparison

| Kernel | Best For | Parameters |
|--------|----------|------------|
| Linear | Large $p$, text, linearly separable | None |
| RBF | General non-linear, default choice | $\gamma$ |
| Polynomial | Image, specific structures | $d, \gamma, r$ |

---

## GATE Tricks

> [!tip] **SVM Quick Rules**
> - **C large** = less regularization = harder margin = more overfitting
> - **C small** = more regularization = wider margin = more bias
> - **RBF $\gamma$ large** = tight fit = complex boundary = overfitting
> - **RBF $\gamma$ small** = smoother boundary = underfitting
> - **Only support vectors matter** for prediction
> - **Linear kernel** = fastest, use when $p$ large or $n$ large
> - **Feature scaling critical** for RBF kernel!

> [!warning] **GATE Traps**
> - **Hard margin only works if perfectly separable** (rare in practice)
> - **SVM doesn't output probabilities** natively (need Platt scaling)
> - **Kernel matrix must be PSD** (Mercer's condition)
> - **Unscaled features** → RBF kernel fails (distance dominated by large-scale features)
> - **Multi-class**: OvO trains $K(K-1)/2$ models, OvR trains $K$ models

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Hard Margin | Soft Margin | Separable vs non-separable |
| $C$ | $\gamma$ (RBF) | C = regularization, $\gamma$ = kernel width |
| Support Vectors | All training points | Only $\alpha_i > 0$ points matter |
| Primal | Dual | Primal: $w,b$; Dual: $\alpha$ |
| Linear SVM | Logistic Regression | Hinge vs Cross-entropy loss |

---

## Common Mistakes

1. **No feature scaling** → RBF kernel dominated by large-scale features
2. **Default C=1, γ=1** → always tune via CV!
3. **Using RBF for text/linear problems** → linear kernel faster & often better
4. **Expecting probabilities** → need Platt scaling (extra CV)
5. **Not handling class imbalance** → use class_weight='balanced'

---

## Memory Tricks

> [!tip] **Support Vectors** = "Support" the margin boundaries
> 
> **C** = "**C**ost of misclassification" = inverse regularization
> 
> **γ (gamma)** = "**G**aussian width" = inverse radius of influence
> 
> **Margin** = $2/||w||$ = "2 over norm of w"
> 
> **Kernel** = "Implicit feature mapping"

---

## Previous GATE Patterns

- **Numerical**: Identify support vectors, compute $w,b$ from given $\alpha$
- **KKT conditions**: Classify points by $\alpha_i$ value
- **Kernel computation**: Compute $K(x_i, x_j)$ for given kernel
- **C and $\gamma$ effects**: Overfitting/underfitting analysis
- **Comparison**: SVM vs Logistic Regression vs Decision Trees
- **Primal vs Dual**: When to use which
- **Multi-class strategies**: OvO vs OvR

---

## Revision Summary

```
SUPPORT VECTOR MACHINE (SVM)
├── Hard Margin: min ½||w||² s.t. yᵢ(wᵀxᵢ+b) ≥ 1
├── Soft Margin: min ½||w||² + CΣξᵢ s.t. yᵢ(wᵀxᵢ+b) ≥ 1-ξᵢ, ξᵢ≥0
├── Dual: max Σαᵢ - ½ΣΣαᵢαⱼyᵢyⱼK(xᵢ,xⱼ) s.t. 0≤αᵢ≤C, Σαᵢyᵢ=0
├── Decision: f(x) = sign(ΣαᵢyᵢK(xᵢ,x) + b)
├── Only support vectors (αᵢ>0) matter
├── Kernels: Linear, Poly, RBF=exp(-γ||xᵢ-xⱼ||²), Sigmoid
├── C ↑ = less regularization, harder margin
├── γ ↑ = tighter RBF, more complex boundary
├── Feature scaling MANDATORY for RBF
├── No native probabilities (Platt scaling for calibration)
└── Multi-class: OvO (K(K-1)/2) or OvR (K)
```

---

## Related Notes

- [[06 Logistic Regression]] (Comparison)
- [[09 Linear Discriminant Analysis]] (Linear classifier comparison)
- [[11 Decision Trees]] (Non-linear comparison)
- [[Formula Sheet]]

---

#machine-learning #gate-da #svm #classification #revision