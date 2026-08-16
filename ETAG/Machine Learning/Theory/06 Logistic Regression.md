---
tags: [machine-learning, gate-da, logistic-regression, classification, revision]
---

# 06 Logistic Regression

> [!note] Linear model for **binary classification** via sigmoid: $P(y=1|x) = \sigma(\beta^T x)$

---

## Overview

Logistic regression models $P(y=1|x)$ using logistic (sigmoid) function. Despite name, it's a **classification** algorithm.

---

## Key Concepts

| Concept                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Sigmoid Function**   | $\sigma(z) = \frac{1}{1+e^{-z}}$ maps $\mathbb{R} \to (0,1)$ |
| **Log-Odds (Logit)**   | $\log \frac{P(y=1x)}{P(y=0x)} = \beta^T x$                   |
| **Decision Boundary**  | $\beta^T x = 0$ (linear hyperplane)                          |
| **Maximum Likelihood** | Parameters estimated via MLE, no closed form                 |
| **Cross-Entropy Loss** | Convex loss function for training                            |

---

## Formulae

### Model
$$
P(y=1|x) = \sigma(\beta^T x) = \frac{1}{1 + e^{-\beta^T x}}
$$
$$
P(y=0|x) = 1 - P(y=1|x) = \frac{e^{-\beta^T x}}{1 + e^{-\beta^T x}}
$$

### Log-Odds (Linear in Parameters)
$$
\log \frac{P(y=1|x)}{P(y=0|x)} = \beta^T x
$$

### Likelihood
$$
L(\beta) = \prod_{i=1}^n P(y_i|x_i) = \prod_{i=1}^n [\sigma(\beta^T x_i)]^{y_i} [1-\sigma(\beta^T x_i)]^{1-y_i}
$$

### Log-Likelihood
$$
\ell(\beta) = \sum_{i=1}^n \left[ y_i \log \sigma(\beta^T x_i) + (1-y_i) \log (1-\sigma(\beta^T x_i)) \right]
$$

### Cross-Entropy Loss (Negative Log-Likelihood)
$$
J(\beta) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log \hat{y}_i + (1-y_i) \log (1-\hat{y}_i) \right]
$$
where $\hat{y}_i = \sigma(\beta^T x_i)$

### Gradient
$$
\frac{\partial J}{\partial \beta} = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i) x_i = \frac{1}{n} X^T (\hat{y} - y)
$$

### Hessian
$$
H = \frac{1}{n} X^T D X, \quad D = \text{diag}(\hat{y}_i(1-\hat{y}_i))
$$
*Positive definite → loss is convex*

### Newton-Raphson / IRLS Update
$$
\beta^{(t+1)} = \beta^{(t)} - H^{-1} \nabla J = (X^T D X)^{-1} X^T D z
$$
where $z = X\beta^{(t)} + D^{-1}(y - \hat{y})$ (working response)

### Gradient Descent Update
$$
\beta := \beta - \alpha \frac{1}{n} X^T (\hat{y} - y)
$$

### Regularized (Ridge) Logistic Regression
$$
J(\beta) = -\frac{1}{n} \sum [y_i \log \hat{y}_i + (1-y_i)\log(1-\hat{y}_i)] + \frac{\lambda}{2} ||\beta||^2
$$
$$
\nabla J = \frac{1}{n} X^T (\hat{y} - y) + \lambda \beta
$$

### Decision Rule
$$
\hat{y} = \begin{cases} 1 & \text{if } \hat{P}(y=1|x) \geq 0.5 \text{ (or threshold } \tau) \\ 0 & \text{otherwise} \end{cases}
$$
Equivalent to: $\hat{y} = 1$ if $\beta^T x \geq 0$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\beta$ | Coefficient vector $(p+1) \times 1$ |
| $\sigma(z)$ | Sigmoid function |
| $\hat{y}_i$ | Predicted probability $P(y=1|x_i)$ |
| $D$ | Diagonal matrix with $\hat{y}_i(1-\hat{y}_i)$ |
| $z$ | Working response in IRLS |

---

## Important Properties

### Convexity
- Cross-entropy loss is **convex** in $\beta$
- Global minimum guaranteed
- No local minima issues

### Probabilistic Output
- Outputs calibrated probabilities (unlike SVM)
- Useful for ranking, risk assessment

### Linear Decision Boundary
- $\beta^T x = 0$ is a hyperplane
- Cannot solve XOR or non-linearly separable problems without feature engineering

### Relationship to Linear Regression
- Linear regression on binary $y$ → predictions outside [0,1]
- Logistic regression → predictions in (0,1)
- Both have linear decision boundaries

---

## Mathematical Intuition

**Odds Ratio**: $\frac{P}{1-P} = e^{\beta^T x}$

**Interpretation of $\beta_j$**: 
- $\beta_j$ = change in log-odds per unit increase in $x_j$
- $e^{\beta_j}$ = multiplicative change in odds
- If $\beta_j > 0$: increasing $x_j$ increases probability of class 1

**Latent Variable View**: 
- $y^* = \beta^T x + \epsilon$, $\epsilon \sim \text{Logistic}(0,1)$
- $y = 1$ if $y^* > 0$, else $0$

---

## Algorithms

### Gradient Descent (Standard)
```python
β = 0
for epoch in range(iterations):
    ŷ = sigmoid(X @ β)
    β = β - α * (X.T @ (ŷ - y)) / n
```

### Newton-Raphson / IRLS (Faster Convergence)
```python
β = 0
for epoch in range(iterations):
    ŷ = sigmoid(X @ β)
    D = diag(ŷ * (1 - ŷ))
    z = X @ β + (y - ŷ) / (ŷ * (1 - ŷ))
    β = (X.T @ D @ X)⁻¹ @ X.T @ D @ z
```

### Coordinate Descent (for Regularized)
```python
# Cyclic coordinate descent on regularized loss
for j in range(p):
    # Update β_j holding others fixed
```

---

## Complexity

| Method | Training | Prediction | Space |
|--------|----------|------------|-------|
| Gradient Descent | $O(np \cdot \text{iter})$ | $O(p)$ | $O(np)$ |
| Newton-Raphson | $O(p^3 + np^2)$ per iter | $O(p)$ | $O(np)$ |
| Coordinate Descent | $O(np \cdot \text{iter})$ | $O(p)$ | $O(np)$ |

---

## Comparison Tables

### Logistic Regression vs Linear Regression

| Aspect | Logistic Regression | Linear Regression |
|--------|---------------------|-------------------|
| Target | Binary {0,1} | Continuous |
| Output | Probability ∈ (0,1) | Any real value |
| Loss | Cross-entropy | MSE |
| Decision Boundary | Linear | Linear |
| Assumptions | Fewer (no normality) | Gauss-Markov |

### Logistic Regression vs SVM

| Aspect | Logistic Regression | SVM |
|--------|---------------------|-----|
| Output | Probabilities | Hard decision (or Platt scaling) |
| Loss | Cross-entropy | Hinge loss |
| Margin | Probabilistic | Maximal geometric margin |
| Outliers | Sensitive (log loss) | Robust (hinge loss) |
| Kernel | Not native | Native (kernel trick) |

### Regularization Effects

| Regularization | Effect | Use Case |
|----------------|--------|----------|
| L2 (Ridge) | Shrinks coefficients | Multicollinearity, $p > n$ |
| L1 (Lasso) | Sparsity | Feature selection |
| Elastic Net | Both | Correlated features + selection |

---

## GATE Tricks

> [!tip] **Logistic Regression Quick Rules**
> - **Sigmoid derivative**: $\sigma'(z) = \sigma(z)(1-\sigma(z))$
> - **Gradient**: $\frac{1}{n}X^T(\hat{y} - y)$ — same form as linear regression residuals!
> - **Decision boundary**: $\beta^T x = 0$ (linear)
> - **Always regularize** in practice (especially $p \approx n$ or $p > n$)
> - **Feature scaling** helps gradient descent converge faster
> - **Probabilities calibrated** → can adjust threshold for precision/recall tradeoff

> [!warning] **GATE Traps**
> - **No closed-form solution** → must use iterative optimization
> - **Complete separation** → coefficients → ∞ (use regularization!)
> - **Linear decision boundary** → can't solve XOR without feature engineering
> - **Cross-entropy** vs **MSE**: MSE is non-convex for logistic model!

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Logistic Regression | Linear Regression | Binary vs continuous target |
| Cross-Entropy | MSE | CE convex for logistic; MSE non-convex |
| Logistic Regression | SVM | Probabilistic vs margin-based |
| Sigmoid | Softmax | Binary vs multi-class |
| Log-odds | Probability | Log-odds linear, probability sigmoid |

---

## Common Mistakes

1. **Using MSE loss** → non-convex, local minima
2. **No regularization** → overfitting, complete separation issues
3. **Ignoring feature scaling** → slow GD convergence
4. **Threshold fixed at 0.5** → adjust for class imbalance
5. **Assuming linearity in probability** → it's linear in log-odds!

---

## Memory Tricks

> [!tip] **Sigmoid derivative**: $\sigma'(z) = \sigma(z)(1-\sigma(z))$ = "sigmoid times one-minus-sigmoid"
> 
> **Gradient**: $X^T(\hat{y} - y)/n$ = "design matrix times residuals"
> 
> **Log-odds linear**: "log odds = βᵀx"
> 
> **IRLS** = Iteratively Reweighted Least Squares = "repeated weighted LS"

---

## Previous GATE Patterns

- **Numerical**: One step of gradient descent / Newton update
- **Derivation**: Gradient of cross-entropy loss
- **Properties**: Convexity, decision boundary linearity
- **Comparison**: Logistic vs SVM vs LDA
- **Regularization**: Effect of L1 vs L2

---

## Revision Summary

```
LOGISTIC REGRESSION
├── Model: P(y=1|x) = σ(βᵀx) = 1/(1+e^{-βᵀx})
├── Log-odds: log(P/(1-P)) = βᵀx (linear!)
├── Loss: Cross-entropy J = -1/n Σ[y log ŷ + (1-y)log(1-ŷ)]
├── Gradient: ∇J = 1/n Xᵀ(ŷ - y)
├── Hessian: H = 1/n XᵀDX (convex!)
├── Optimization: GD, Newton-Raphson (IRLS), Coordinate Descent
├── Decision: ŷ = 1 if βᵀx ≥ 0 (threshold adjustable)
├── Regularization: Add λ||β||²/2 (Ridge) or λ||β||₁ (Lasso)
├── No closed form → iterative
├── Probabilistic output (calibrated)
└── Linear decision boundary
```

---

## Related Notes

- [[02 Regression]]
- [[05 Ridge Regression]] (regularization applies here too)
- [[09 Linear Discriminant Analysis]] (also linear classifier)
- [[10 Support Vector Machine]] (comparison)
- [[Formula Sheet]]

---

#machine-learning #gate-da #logistic-regression #classification #revision