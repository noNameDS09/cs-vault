---
tags: [machine-learning, gate-da, regression, revision]
---

# 02 Regression

> [!note] Predicting continuous target variable $y \in \mathbb{R}$

---

## Overview

Regression models the relationship between features $X$ and continuous target $y$. Goal: learn $f: \mathbb{R}^p \to \mathbb{R}$ minimizing prediction error.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Simple Linear Regression** | One feature: $y = \beta_0 + \beta_1 x + \epsilon$ |
| **Multiple Linear Regression** | Multiple features: $y = \beta_0 + \sum_{j=1}^p \beta_j x_j + \epsilon$ |
| **Polynomial Regression** | Non-linear via basis expansion: $y = \beta_0 + \beta_1 x + \beta_2 x^2 + ...$ |
| **Regularized Regression** | Ridge (L2), Lasso (L1), Elastic Net |
| **Residual** | $e_i = y_i - \hat{y}_i$ |
| **Homoscedasticity** | Constant variance of errors: $Var(\epsilon_i) = \sigma^2$ |
| **Heteroscedasticity** | Non-constant error variance |

---

## Formulae

### Linear Model
$$
y = X\beta + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2 I)
$$

### Least Squares Objective
$$
\min_\beta ||y - X\beta||^2_2 = \min_\beta \sum_{i=1}^n (y_i - x_i^T \beta)^2
$$

### Normal Equation (Closed Form)
$$
\hat{\beta} = (X^T X)^{-1} X^T y
$$
*Requires $X^T X$ invertible (full column rank, $n \geq p$)*

### Gradient Descent Update
$$
\beta := \beta - \alpha X^T (X\beta - y)
$$

### Prediction
$$
\hat{y} = X\hat{\beta} = H y, \quad H = X(X^T X)^{-1} X^T \text{ (Hat Matrix)}
$$

### Residuals
$$
e = y - \hat{y} = (I - H)y
$$

### $R^2$ (Coefficient of Determination)
$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

### Adjusted $R^2$
$$
R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}
$$
*Penalizes adding useless predictors*

### Mean Squared Error (MSE)
$$
MSE = \frac{1}{n}\sum (y_i - \hat{y}_i)^2 = \frac{SS_{res}}{n}
$$

### Root Mean Squared Error (RMSE)
$$
RMSE = \sqrt{MSE}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of observations |
| $p$ | Number of predictors (features) |
| $X$ | Design matrix $(n \times (p+1))$ with intercept column |
| $y$ | Response vector $(n \times 1)$ |
| $\beta$ | Coefficient vector $((p+1) \times 1)$ |
| $\hat{\beta}$ | Estimated coefficients |
| $\epsilon$ | Error term |
| $\sigma^2$ | Error variance |
| $H$ | Hat matrix (projection onto column space of X) |
| $h_{ii}$ | Leverage of observation $i$ |

---

## Important Properties

### Gauss-Markov Theorem (BLUE)
Under assumptions:
1. Linearity: $y = X\beta + \epsilon$
2. Exogeneity: $E[\epsilon|X] = 0$
3. Homoscedasticity: $Var(\epsilon|X) = \sigma^2 I$
4. No autocorrelation: $Cov(\epsilon_i, \epsilon_j|X) = 0$
5. Full rank: $rank(X) = p+1$

**OLS is Best Linear Unbiased Estimator (BLUE)**

### OLS Assumptions Checklist
- [ ] Linear in parameters
- [ ] Random sampling
- [ ] No perfect multicollinearity
- [ ] Zero conditional mean $E[\epsilon|X]=0$
- [ ] Homoscedasticity
- [ ] No autocorrelation
- [ ] Normality (for inference only)

### Multicollinearity
- High correlation among predictors
- Inflates variance of $\hat{\beta}$: $Var(\hat{\beta}_j) = \frac{\sigma^2}{(1-R_j^2)\sum(x_{ij}-\bar{x}_j)^2}$
- **VIF** (Variance Inflation Factor): $VIF_j = \frac{1}{1-R_j^2} > 10$ indicates problem

### Leverage & Influence
- **Leverage**: $h_{ii} = x_i^T (X^T X)^{-1} x_i$ (diagonal of hat matrix)
- High leverage: $h_{ii} > 2(p+1)/n$
- **Cook's Distance**: $D_i = \frac{e_i^2}{p \cdot MSE} \cdot \frac{h_{ii}}{(1-h_{ii})^2}$ (influence measure)

---

## Mathematical Intuition

**Projection View**: OLS projects $y$ onto column space of $X$.
- $\hat{y} = Hy$ is orthogonal projection
- Residuals $e = (I-H)y$ orthogonal to $\hat{y}$
- $H$ is idempotent ($H^2=H$) and symmetric

**Geometric**: Minimize distance from $y$ to subspace spanned by columns of $X$.

---

## Algorithms

### Normal Equation (Direct)
```
1. Compute X^T X
2. Compute X^T y
3. Solve (X^T X)β = X^T y for β
4. Complexity: O(p^3 + np^2)
```

### Gradient Descent (Iterative)
```
1. Initialize β
2. Repeat until convergence:
   β := β - α X^T (Xβ - y)
3. Complexity per iteration: O(np)
```

### QR Decomposition (Numerically Stable)
```
1. X = QR (Q orthogonal, R upper triangular)
2. Solve Rβ = Q^T y
```

---

## Complexity

| Method | Training | Prediction | Space |
|--------|----------|------------|-------|
| Normal Equation | $O(p^3 + np^2)$ | $O(p)$ | $O(np)$ |
| Gradient Descent | $O(np \cdot \text{iter})$ | $O(p)$ | $O(np)$ |
| QR Decomposition | $O(np^2)$ | $O(p)$ | $O(np)$ |

---

## Comparison Tables

### OLS vs Regularized

| Aspect | OLS | Ridge | Lasso |
|--------|-----|-------|-------|
| Solution | $(X^T X)^{-1}X^T y$ | $(X^T X + \lambda I)^{-1}X^T y$ | No closed form |
| Multicollinearity | Fails | Handles well | Handles well |
| Feature Selection | No | No (shrinkage) | Yes (sparsity) |
| Bias | 0 | Increases with $\lambda$ | Increases with $\lambda$ |

### Evaluation Metrics

| Metric    | Formula                          | Range          | Interpretation                   |
| --------- | -------------------------------- | -------------- | -------------------------------- |
| $R^2$     | $1 - SS_{res}/SS_{tot}$          | $(-\infty, 1]$ | Proportion of variance explained |
| Adj $R^2$ | $1 - \frac{(1-R^2)(n-1)}{n-p-1}$ | $(-\infty, 1]$ | Penalizes extra predictors       |
| MSE       | $\frac{1}{n}\sum(y-\hat{y})^2$   | $[0, \infty)$  | Average squared error            |
| RMSE      | $\sqrt{MSE}$                     | $[0, \infty)$  | Error in target units            |
| MAE       | $\frac{1}{n}\sum y-\hat{y}$      | $[0, \infty)$  | Average absolute error           |

---

## GATE Tricks

> [!tip] **Regression Quick Rules**
> - **$R^2$ always increases** with more predictors (use Adj $R^2$)
> - **$R^2_{adj}$ decreases** if new predictor doesn't improve fit enough
> - **Multicollinearity**: VIF > 10 = problem; Ridge/Lasso fix it
> - **Heteroscedasticity**: Use robust standard errors (White's)
> - **Outliers**: Check leverage ($h_{ii}$) and Cook's distance
> - **Normality**: Only needed for hypothesis tests, not prediction

> [!warning] **GATE Traps**
> - $R^2$ can be negative if fit worse than horizontal line (no intercept model)
> - OLS fails when $p > n$ or multicollinearity (use Ridge)
> - Correlation ≠ Causation (confounding variables)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $R^2$ | Adjusted $R^2$ | Adj penalizes useless predictors |
| Confidence Interval | Prediction Interval | CI for mean $E[y|x]$, PI for individual $y$ |
| Leverage | Influence | Leverage = potential, Influence = actual effect |
| Multicollinearity | Correlation | Multicollinearity = multiple predictors correlated |

---

## Common Mistakes

1. **Adding intercept manually** when X already has one → perfect multicollinearity
2. **Interpreting $R^2$ as accuracy** (it's variance explained)
3. **Ignoring assumptions** → invalid p-values, confidence intervals
4. **Extrapolation** → predictions outside training range unreliable
5. **Using $R^2$ for model comparison** across different $y$ scales

---

## Memory Tricks

> [!tip] **BLUE** = Best Linear Unbiased Estimator
> 
> **VIF** = Variance Inflation Factor > 10 = bad
> 
> **R²** = "R-square" = variance explained
> 
> **Adj R²** = "Adjusted" = penalizes extra variables

---

## Previous GATE Patterns

- **Numerical**: Compute $\hat{\beta}$, $R^2$, leverage, Cook's distance
- **MCQ**: Identify violated assumption from residual plot
- **Theory**: Gauss-Markov conditions, BLUE property
- **Comparison**: Ridge vs Lasso vs Elastic Net

---

## Revision Summary

```
REGRESSION ESSENTIALS
├── Model: y = Xβ + ε, ε ~ N(0, σ²I)
├── OLS: β̂ = (XᵀX)⁻¹Xᵀy (minimizes ||y - Xβ||²)
├── Assumptions: Linearity, Exogeneity, Homoscedasticity, No Autocorr, Full Rank
├── Gauss-Markov: OLS is BLUE under assumptions
├── Diagnostics: R², Adj R², Residual plots, VIF, Leverage, Cook's D
├── Problems: Multicollinearity → Ridge/Lasso, Heteroscedasticity → Robust SE
├── Regularization: Ridge (L2), Lasso (L1), Elastic Net (L1+L2)
└── p > n or multicollinearity → must use regularization
```

---

## Related Notes

- [[03 Simple Linear Regression]]
- [[04 Multiple Linear Regression]]
- [[05 Ridge Regression]]
- [[12 Bias Variance Tradeoff]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #regression #revision