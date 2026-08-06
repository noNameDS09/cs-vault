---
tags: [machine-learning, gate-da, multiple-linear-regression, revision]
---

# 04 Multiple Linear Regression

> [!note] Regression with **multiple predictors**: $y = \beta_0 + \sum_{j=1}^p \beta_j x_j + \epsilon$

---

## Overview

Extends simple linear regression to $p$ features. Uses matrix algebra for compact representation and computation.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Design Matrix** | $X$ is $n \times (p+1)$ with first column = 1 (intercept) |
| **Coefficient Vector** | $\beta = (\beta_0, \beta_1, ..., \beta_p)^T$ |
| **Multicollinearity** | High correlation among predictors |
| **Partial Regression Coefficient** | $\beta_j$ = effect of $x_j$ holding others constant |
| **Hat Matrix** | $H = X(X^T X)^{-1} X^T$ projects $y$ onto column space of $X$ |

---

## Formulae

### Matrix Model
$$
y = X\beta + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2 I_n)
$$
$$
X = \begin{bmatrix} 1 & x_{11} & \cdots & x_{1p} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n1} & \cdots & x_{np} \end{bmatrix}_{n \times (p+1)}
$$

### Normal Equation
$$
X^T X \hat{\beta} = X^T y
$$
$$
\hat{\beta} = (X^T X)^{-1} X^T y \quad \text{(requires } X^T X \text{ invertible)}
$$

### Fitted Values & Residuals
$$
\hat{y} = X\hat{\beta} = H y, \quad H = X(X^T X)^{-1} X^T
$$
$$
e = y - \hat{y} = (I - H)y
$$

### Properties of Hat Matrix
- $H^T = H$ (symmetric)
- $H^2 = H$ (idempotent)
- $rank(H) = p+1$
- $h_{ii} = x_i^T (X^T X)^{-1} x_i$ (leverage)

### Sum of Squares
$$
SS_{tot} = y^T (I - \frac{1}{n}J) y = \sum (y_i - \bar{y})^2
$$
$$
SS_{reg} = \hat{y}^T (I - \frac{1}{n}J) \hat{y} = \hat{\beta}^T X^T y - n\bar{y}^2
$$
$$
SS_{res} = e^T e = y^T (I - H) y
$$

### $R^2$ and Adjusted $R^2$
$$
R^2 = \frac{SS_{reg}}{SS_{tot}} = 1 - \frac{SS_{res}}{SS_{tot}}
$$
$$
R^2_{adj} = 1 - \frac{SS_{res}/(n-p-1)}{SS_{tot}/(n-1)} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}
$$

### F-Statistic (Overall Significance)
$$
F = \frac{SS_{reg}/p}{SS_{res}/(n-p-1)} = \frac{R^2/p}{(1-R^2)/(n-p-1)}
$$
Tests $H_0: \beta_1 = \beta_2 = ... = \beta_p = 0$

### Coefficient Variance
$$
Var(\hat{\beta}) = \sigma^2 (X^T X)^{-1}
$$
$$
Var(\hat{\beta}_j) = \frac{\sigma^2}{(1-R_j^2)\sum (x_{ij} - \bar{x}_j)^2}
$$
where $R_j^2$ = $R^2$ from regressing $x_j$ on other predictors

### Variance Inflation Factor (VIF)
$$
VIF_j = \frac{1}{1 - R_j^2}
$$
- $VIF > 5$: Moderate multicollinearity
- $VIF > 10$: Severe multicollinearity

### Confidence Interval for $\beta_j$
$$
\hat{\beta}_j \pm t_{n-p-1, \alpha/2} \cdot SE(\hat{\beta}_j)
$$

### Prediction Interval for New $x_0$
$$
\hat{y}_0 \pm t_{n-p-1, \alpha/2} \cdot \sqrt{\hat{\sigma}^2 (1 + x_0^T (X^T X)^{-1} x_0)}
$$

### Partial F-Test (Nested Models)
Compare full model (p predictors) vs reduced model (q predictors):
$$
F = \frac{(SS_{res,reduced} - SS_{res,full})/(p-q)}{SS_{res,full}/(n-p-1)}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of observations |
| $p$ | Number of predictors (excluding intercept) |
| $X$ | Design matrix $n \times (p+1)$ |
| $y$ | Response vector $n \times 1$ |
| $\beta$ | True coefficient vector $(p+1) \times 1$ |
| $\hat{\beta}$ | OLS estimate |
| $H$ | Hat matrix (projection) |
| $h_{ii}$ | Leverage of $i$-th observation |
| $R_j^2$ | $R^2$ from regressing $x_j$ on other $x$'s |
| $VIF_j$ | Variance Inflation Factor |

---

## Important Properties

### OLS Assumptions (Same as Simple)
1. **Linearity**: $E[y|X] = X\beta$
2. **Exogeneity**: $E[\epsilon|X] = 0$
3. **Homoscedasticity**: $Var(\epsilon|X) = \sigma^2 I$
4. **No Autocorrelation**: $Cov(\epsilon_i, \epsilon_j|X) = 0$
5. **Full Rank**: $rank(X) = p+1$ (no perfect multicollinearity)
6. **Normality**: $\epsilon \sim N(0, \sigma^2 I)$ (for inference)

### Multicollinearity Effects
- Inflates $Var(\hat{\beta}_j)$ → large standard errors
- Unstable estimates (small data changes → large coefficient changes)
- Signs may be wrong
- **Does NOT affect** prediction accuracy or $R^2$

### Model Selection Criteria
| Criterion | Formula | Preference |
|-----------|---------|------------|
| AIC | $n \log(SS_{res}/n) + 2(p+1)$ | Lower |
| BIC | $n \log(SS_{res}/n) + (p+1)\log(n)$ | Lower |
| Adj $R^2$ | $1 - \frac{(1-R^2)(n-1)}{n-p-1}$ | Higher |
| Mallows $C_p$ | $\frac{SS_{res}}{\hat{\sigma}^2_{full}} - n + 2(p+1)$ | $\approx p+1$ |

---

## Mathematical Intuition

**Geometry**: OLS finds $\hat{\beta}$ minimizing $||y - X\beta||^2$ — the projection of $y$ onto column space of $X$.

**Partial Effect**: $\beta_j$ = change in $y$ per unit $x_j$ **holding all other $x$'s constant**.

**Frisch-Waugh-Lovell Theorem**: $\hat{\beta}_j$ = coefficient from regressing $y$ on residual of $x_j$ after regressing on other $x$'s.

---

## Algorithms

### Normal Equation (Direct)
```python
# O(p³ + np²) - good for p < ~1000
β̂ = (X.T @ X)⁻¹ @ X.T @ y
```

### QR Decomposition (Stable)
```python
# X = QR, solve Rβ = Q.T y
# O(np²) - numerically stable
```

### Gradient Descent (Large p)
```python
β = 0
for epoch in range(iterations):
    β = β - α * X.T @ (X @ β - y)
```

### Coordinate Descent (Sparse/Lasso)
```python
for j in range(p):
    β_j = update_using_partial_residual(j)
```

---

## Complexity

| Method | Training | Prediction | Space |
|--------|----------|------------|-------|
| Normal Eq | $O(p^3 + np^2)$ | $O(p)$ | $O(np)$ |
| QR | $O(np^2)$ | $O(p)$ | $O(np)$ |
| Gradient Descent | $O(np \cdot \text{iter})$ | $O(p)$ | $O(np)$ |

---

## Comparison Tables

### Simple vs Multiple $R^2$

| Aspect | Simple | Multiple |
|--------|--------|----------|
| $R^2$ | $= r^2$ | $\neq$ squared correlation |
| Adding predictors | N/A | $R^2$ never decreases |
| Adj $R^2$ | N/A | Penalizes useless predictors |

### OLS vs Ridge vs Lasso

| Property | OLS | Ridge | Lasso |
|----------|-----|-------|-------|
| $p > n$ | Fails | Works | Works |
| Multicollinearity | Fails | Handles | Handles |
| Feature Selection | No | No | Yes |
| Solution | Closed form | Closed form | Iterative |

---

## GATE Tricks

> [!tip] **Multiple Regression Quick Rules**
> - **$R^2$ never decreases** when adding predictors (use Adj $R^2$)
> - **Adj $R^2$ decreases** if new predictor's t-stat < 1
> - **VIF > 10** = severe multicollinearity
> - **F-stat tests ALL slopes = 0** simultaneously
> - **Partial F-test** compares nested models
> - **$p > n$**: OLS fails → must use Ridge/Lasso/PCR

> [!warning] **GATE Traps**
> - $R^2$ vs Adj $R^2$: Adj can be negative!
> - Multicollinearity ≠ affects predictions (only interpretation)
> - Omitted variable bias: correlated omitted variable → biased estimates
> - Dummy variable trap: $k$ categories → $k-1$ dummies + intercept

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $R^2$ | Adjusted $R^2$ | Adj penalizes extra predictors |
| Multicollinearity | Correlation | Multiple variables, not just pairwise |
| Partial F-test | t-test | t-test = single coeff, F-test = group |
| CI | PI | CI for $E[y|x]$, PI for individual $y$ |

---

## Common Mistakes

1. **Including all dummy categories** → perfect multicollinearity (dummy trap)
2. **Interpreting coefficients with multicollinearity** → unreliable
3. **Using $R^2$ to compare models** with different $y$ transformations
4. **Stepwise selection** → invalid p-values, overfitting
5. **Ignoring $p > n$** → OLS matrix not invertible

---

## Memory Tricks

> [!tip] **VIF** = "Variance Inflation Factor" > 10 = bad
> 
> **Adj R² formula**: $1 - (1-R^2)\frac{n-1}{n-p-1}$
> 
> **F-stat**: $\frac{R^2/p}{(1-R^2)/(n-p-1)}$ = "explained variance per predictor / unexplained per df"

---

## Previous GATE Patterns

- **Numerical**: Compute $\hat{\beta}$, $R^2$, Adj $R^2$, VIF, F-stat from given matrices
- **Matrix algebra**: $(X^T X)^{-1} X^T y$ computation
- **Multicollinearity**: Identify from VIF / correlation matrix
- **Model selection**: AIC/BIC/Adj $R^2$ comparison
- **Dummy variables**: $k$ categories → $k-1$ dummies

---

## Revision Summary

```
MULTIPLE LINEAR REGRESSION
├── Model: y = Xβ + ε, X: n×(p+1)
├── OLS: β̂ = (XᵀX)⁻¹Xᵀy
├── Fitted: ŷ = Hy, H = X(XᵀX)⁻¹Xᵀ
├── R² = 1 - SS_res/SS_tot (never decreases)
├── Adj R² = 1 - (1-R²)(n-1)/(n-p-1) (can decrease)
├── F-stat: (R²/p) / ((1-R²)/(n-p-1)) tests all βⱼ=0
├── VIFⱼ = 1/(1-R²ⱼ) > 10 = multicollinearity
├── Assumptions: Linearity, Exogeneity, Homoscedasticity, No Autocorr, Full Rank
├── p > n → OLS fails → use Ridge/Lasso
└── Dummy trap: k categories → k-1 dummies
```

---

## Related Notes

- [[03 Simple Linear Regression]]
- [[05 Ridge Regression]]
- [[12 Bias Variance Tradeoff]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #multiple-linear-regression #revision