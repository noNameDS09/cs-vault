---
tags: [machine-learning, gate-da, ridge-regression, regularization, revision]
---

# 05 Ridge Regression

> [!note] L2-regularized linear regression: $\min ||y - X\beta||^2 + \lambda ||\beta||^2$

---

## Overview

Ridge regression adds L2 penalty to handle multicollinearity and $p > n$ cases. Shrinks coefficients toward zero but never exactly zero.

---

## Key Concepts

| Concept                          | Description                                                               |
| -------------------------------- | ------------------------------------------------------------------------- |
| **Regularization Parameter**     | $\lambda \geq 0$ controls shrinkage                                       |
| **L2 Penalty**                   | $\lambda \sum_{j=1}^p \beta_j^2 = \lambda\beta_2^2$                       |
| **Shrinkage**                    | Coefficients pulled toward zero                                           |
| **No Sparsity**                  | Unlike Lasso, coefficients rarely become exactly zero                     |
| **Effective Degrees of Freedom** | $df(\lambda) = \text{tr}(H_\lambda) = \sum \frac{d_i^2}{d_i^2 + \lambda}$ |

---

## Formulae

### Optimization Problem
$$
\hat{\beta}_{ridge} = \arg\min_\beta \left\{ ||y - X\beta||^2_2 + \lambda ||\beta||^2_2 \right\}
$$
*Note: Intercept $\beta_0$ typically NOT penalized (center $y$ and standardize $X$)*

### Closed Form Solution
$$
\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} X^T y
$$
*Always invertible for $\lambda > 0$ even if $p > n$ or multicollinearity!*

### SVD Perspective
Let $X = U D V^T$ (SVD, $D$ = diag$(d_1, ..., d_p)$):
$$
\hat{\beta}_{ridge} = V (D^2 + \lambda I)^{-1} D U^T y
$$
$$
\hat{y} = X \hat{\beta}_{ridge} = U \text{diag}\left(\frac{d_i^2}{d_i^2 + \lambda}\right) U^T y
$$

### Shrinkage Factors
$$
\text{Component } i \text{ shrunk by } \frac{d_i^2}{d_i^2 + \lambda} \in [0, 1]
$$
- Large $d_i$ (high variance directions) → less shrinkage
- Small $d_i$ (low variance/noise directions) → more shrinkage

### Effective Degrees of Freedom
$$
df(\lambda) = \text{tr}(H_\lambda) = \sum_{i=1}^p \frac{d_i^2}{d_i^2 + \lambda}
$$
- $\lambda = 0$: $df = p$ (OLS)
- $\lambda \to \infty$: $df \to 0$ (all coefficients → 0)

### Bias-Variance Tradeoff
$$
\text{Bias}(\hat{\beta}_{ridge}) = -\lambda (X^T X + \lambda I)^{-1} \beta
$$
$$
\text{Var}(\hat{\beta}_{ridge}) = \sigma^2 (X^T X + \lambda I)^{-1} X^T X (X^T X + \lambda I)^{-1}
$$
$$
\text{MSE} = \text{Bias}^2 + \text{Variance}
$$

### Ridge vs OLS Variance
$$
\text{Var}(\hat{\beta}_{ridge}) \prec \text{Var}(\hat{\beta}_{OLS}) \quad \text{(in Loewner order)}
$$
*Ridge always has smaller variance than OLS*

### Generalized Cross Validation (GCV)
$$
GCV(\lambda) = \frac{n \cdot MSE}{(n - df(\lambda))^2} = \frac{||y - \hat{y}||^2}{(n - \text{tr}(H_\lambda))^2}
$$
*Fast LOOCV approximation for choosing $\lambda$*

### Ridge with Centered/Scaled Data
1. Center $y$: $\bar{y} = 0$
2. Standardize $X$: each column mean 0, variance 1
3. Then $\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} X^T y$ (no intercept needed)

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\lambda$ | Regularization parameter ($\geq 0$) |
| $d_i$ | Singular values of $X$ |
| $df(\lambda)$ | Effective degrees of freedom |
| $H_\lambda$ | Ridge hat matrix: $X(X^T X + \lambda I)^{-1} X^T$ |

---

## Important Properties

### When Ridge Helps
- **Multicollinearity**: $X^T X$ near-singular → Ridge stabilizes
- **$p > n$**: OLS fails (infinite solutions) → Ridge gives unique solution
- **High variance**: Ridge reduces variance at cost of small bias

### Ridge Path
As $\lambda$ increases from 0 to $\infty$:
- Coefficients shrink continuously toward 0
- $R^2$ decreases monotonically
- $df$ decreases from $p$ to 0
- Test error typically: decreases → minimum → increases

### Comparison with PCA Regression
- Ridge: shrinks all components, more for small $d_i$
- PCR: keeps top $k$ components, zeros out rest
- Ridge is continuous, PCR is discrete

---

## Mathematical Intuition

**Bayesian View**: Ridge = MAP estimate with Gaussian prior $\beta \sim N(0, \frac{1}{\lambda} I)$

**Constrained Form**: Equivalent to:
$$
\min ||y - X\beta||^2 \quad \text{s.t.} \quad ||\beta||^2 \leq t
$$
where $t \leftrightarrow \lambda$ (one-to-one mapping)

**Geometric**: OLS finds point on ellipsoid contours closest to origin; Ridge finds intersection of constraint circle with contours.

---

## Algorithms

### Choosing $\lambda$ via Cross Validation
```
1. Standardize X, center y
2. Define grid of λ values (log scale: 10⁻⁴, 10⁻³, ..., 10⁴)
3. For each λ:
   - Compute β̂_ridge = (XᵀX + λI)⁻¹Xᵀy
   - Compute CV error (K-fold or GCV)
4. Select λ with minimum CV error
5. Refit on full data with chosen λ
```

### Coordinate Descent (for large p)
```python
# Ridge has closed form but coordinate descent also works
for j in range(p):
    β_j = (X_jᵀ(y - X_{-j}β_{-j})) / (X_jᵀX_j + λ)
```

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Training (direct) | $O(p^3 + np^2)$ | $O(np)$ |
| Training (SVD) | $O(np^2)$ | $O(np)$ |
| Prediction | $O(p)$ | $O(p)$ |

---

## Comparison Tables

### Ridge vs Lasso vs OLS

| Property | OLS | Ridge | Lasso |
|----------|-----|-------|-------|
| $p > n$ | ✗ Fails | ✓ Works | ✓ Works |
| Multicollinearity | ✗ Unstable | ✓ Handles | ✓ Handles |
| Sparsity | No | No | **Yes** |
| Feature Selection | No | No | **Yes** |
| Solution | Closed | Closed | Iterative |
| Bias | None | Increases | Increases |

### Ridge vs PCR

| Aspect | Ridge | PCR |
|--------|-------|-----|
| Shrinkage | Continuous (all components) | Discrete (keep k, drop rest) |
| Tuning | $\lambda$ | $k$ (components) |
| Interpretation | All features retained | Features combined into PCs |

---

## GATE Tricks

> [!tip] **Ridge Quick Rules**
> - **Always works** when $p > n$ or multicollinearity
> - **Standardize features** before Ridge (penalty is scale-dependent!)
> - **Intercept not penalized** → center $y$ first
> - **$\lambda = 0$** = OLS; **$\lambda \to \infty$** = all $\beta = 0$
> - **GCV** = fast LOOCV approximation for choosing $\lambda$
> - **No sparsity** → if you need feature selection, use Lasso

> [!warning] **GATE Traps**
> - **Forgetting to standardize** → features with large scale get penalized more
> - **Penalizing intercept** → wrong! Always center $y$
> - **Assuming Ridge does feature selection** → it doesn't (use Lasso)
> - **$\lambda$ on linear scale** → use log scale for grid search

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Ridge (L2) | Lasso (L1) | L2: shrink, no sparsity | L1: sparse |
| Ridge | PCR | Ridge: continuous shrinkage | PCR: discrete components |
| $\lambda$ | $t$ (constraint) | Dual parameters, 1-to-1 mapping |

---

## Common Mistakes

1. **Not standardizing $X$** → penalty unfair to large-scale features
2. **Penalizing intercept** → biases predictions
3. **Using Ridge for feature selection** → coefficients never exactly zero
4. **Linear $\lambda$ grid** → use log scale (e.g., $10^{-4}$ to $10^4$)
5. **Choosing $\lambda$ on test set** → data leakage! Use CV

---

## Memory Tricks

> [!tip] **Ridge** = "Ridge" = L2 = squared = $\lambda \sum \beta^2$
> 
> **Ridge never zeros** = "Ridge holds on to everything"
> 
> **Standardize first** = "Level the playing field before penalty"

---

## Previous GATE Patterns

- **Numerical**: Compute $\hat{\beta}_{ridge}$ given $X, y, \lambda$
- **SVD connection**: Show shrinkage factors $d_i^2/(d_i^2 + \lambda)$
- **Bias-Variance**: Ridge reduces variance, adds bias
- **$p > n$ case**: Ridge works, OLS fails
- **GCV formula**: $\frac{||y-\hat{y}||^2}{(n - df)^2}$

---

## Revision Summary

```
RIDGE REGRESSION
├── Objective: min ||y - Xβ||² + λ||β||²
├── Solution: β̂ = (XᵀX + λI)⁻¹Xᵀy (always invertible if λ>0)
├── Standardize X, center y (intercept not penalized)
├── Shrinks coefficients: β̂_ridge = V diag(dᵢ²/(dᵢ²+λ)) D⁻¹ Uᵀ y
├── λ=0 → OLS, λ→∞ → all β=0
├── df(λ) = Σ dᵢ²/(dᵢ²+λ) (effective degrees of freedom)
├── GCV for λ selection: ||y-ŷ||²/(n-df)²
├── Handles multicollinearity & p > n
├── NO sparsity (use Lasso for feature selection)
└── Bayesian view: MAP with N(0, 1/λ) prior
```

---

## Related Notes

- [[04 Multiple Linear Regression]]
- [[06 Logistic Regression]] (can also be regularized)
- [[12 Bias Variance Tradeoff]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #ridge-regression #regularization #revision