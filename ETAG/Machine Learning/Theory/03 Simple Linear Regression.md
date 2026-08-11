---
tags: [machine-learning, gate-da, simple-linear-regression, revision]
---
	
# 03 Simple Linear Regression

> [!note] Regression with **one predictor**: $y = \beta_0 + \beta_1 x + \epsilon$

---

## Overview

Models linear relationship between single feature $x$ and target $y$. Foundation for all linear models.

---

## Key Concepts

| Concept                         | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| **Slope ($\beta_1$)**           | Change in $y$ per unit change in $x$            |
| **Intercept ($\beta_0$)**       | Expected $y$ when $x=0$                         |
| **Residual**                    | $e_i = y_i - \hat{y}_i$                         |
| **Fitted Value**                | $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ |
| **Total/Explained/Residual SS** | $SS_{tot} = SS_{reg} + SS_{res}$                |

---

## Formulae

### Model
$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i, \quad \epsilon_i \overset{iid}{\sim} \mathcal{N}(0, \sigma^2)
$$

### Least Squares Estimators
$$
\hat{\beta}_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}} = r \frac{s_y}{s_x}
$$
$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

### Alternative Forms
$$
\hat{\beta}_1 = \frac{\sum x_i y_i - n\bar{x}\bar{y}}{\sum x_i^2 - n\bar{x}^2}
$$
$$
\hat{\beta}_1 = \frac{Cov(x,y)}{Var(x)}
$$

### Fitted Values & Residuals
$$
\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
$$
$$
e_i = y_i - \hat{y}_i
$$
$$
\sum e_i = 0, \quad \sum x_i e_i = 0 \quad \text{(orthogonality conditions)}
$$

### Sum of Squares
$$
SS_{tot} = \sum (y_i - \bar{y})^2
$$
$$
SS_{reg} = \sum (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1^2 \sum (x_i - \bar{x})^2
$$
$$
SS_{res} = \sum (y_i - \hat{y}_i)^2 = \sum e_i^2
$$
$$
SS_{tot} = SS_{reg} + SS_{res}
$$

### $R^2$ and Correlation
$$
R^2 = \frac{SS_{reg}}{SS_{tot}} = 1 - \frac{SS_{res}}{SS_{tot}} = r^2
$$
$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

### Error Variance Estimate
$$
\hat{\sigma}^2 = MSE = \frac{SS_{res}}{n-2}
$$
$$
SE(\hat{\beta}_1) = \sqrt{\frac{\hat{\sigma}^2}{\sum (x_i - \bar{x})^2}}
$$
$$
SE(\hat{\beta}_0) = \sqrt{\hat{\sigma}^2 \left(\frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}\right)}
$$

### Confidence Intervals
$$
\hat{\beta}_1 \pm t_{n-2, \alpha/2} \cdot SE(\hat{\beta}_1)
$$
$$
\hat{\beta}_0 \pm t_{n-2, \alpha/2} \cdot SE(\hat{\beta}_0)
$$

### Prediction Interval (New $x_0$)
$$
\hat{y}_0 \pm t_{n-2, \alpha/2} \cdot \sqrt{\hat{\sigma}^2 \left(1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\sum (x_i - \bar{x})^2}\right)}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of observations |
| $x_i, y_i$ | Observed data pairs |
| $\bar{x}, \bar{y}$ | Sample means |
| $\beta_0, \beta_1$ | True parameters |
| $\hat{\beta}_0, \hat{\beta}_1$ | OLS estimates |
| $S_{xx}$ | $\sum (x_i - \bar{x})^2$ |
| $S_{xy}$ | $\sum (x_i - \bar{x})(y_i - \bar{y})$ |
| $r$ | Pearson correlation |
| $\sigma^2$ | Error variance |
| $t_{n-2, \alpha/2}$ | t-distribution critical value |

---

## Important Properties

### OLS Properties (Gauss-Markov)
1. **Unbiased**: $E[\hat{\beta}_0] = \beta_0$, $E[\hat{\beta}_1] = \beta_1$
2. **Minimum Variance** among linear unbiased estimators
3. **Normality**: If $\epsilon_i \sim N(0,\sigma^2)$, then $\hat{\beta} \sim N(\beta, \sigma^2(X^T X)^{-1})$

### Key Identities
- $\sum e_i = 0$ (residuals sum to zero)
- $\sum \hat{y}_i = \sum y_i$ (fitted values preserve mean)
- $\sum x_i e_i = 0$ (residuals uncorrelated with $x$)
- Regression line passes through $(\bar{x}, \bar{y})$

---

## Mathematical Intuition

**Geometric View**: Minimize vertical distances (residuals) from points to line.

**Correlation Connection**: $\hat{\beta}_1 = r \frac{s_y}{s_x}$
- Slope = correlation × (spread of y / spread of x)
- If $r=0$, slope = 0 (horizontal line at $\bar{y}$)

**Projection**: $\hat{y}$ is projection of $y$ onto span$\{1, x\}$

---

## Algorithms

### Direct Calculation (O(n))
```
1. Compute x̄, ȳ
2. Compute S_xx = Σ(x_i - x̄)², S_xy = Σ(x_i - x̄)(y_i - ȳ)
3. β̂₁ = S_xy / S_xx
4. β̂₀ = ȳ - β̂₁ x̄
5. Compute R² = (S_xy)² / (S_xx × S_yy)
```

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Training | $O(n)$ | $O(1)$ |
| Prediction | $O(1)$ | $O(1)$ |

---

## Comparison Tables

### Simple vs Multiple Regression

| Aspect | Simple | Multiple |
|--------|--------|----------|
| Predictors | 1 | $p \geq 1$ |
| Formula | $\hat{\beta}_1 = S_{xy}/S_{xx}$ | $\hat{\beta} = (X^T X)^{-1}X^T y$ |
| $R^2$ | $= r^2$ | $\neq$ squared correlation |
| Visualization | 2D line | Hyperplane |

### CI vs PI

| Interval                | Width    | For          |
| ----------------------- | -------- | ------------ |
| Confidence (mean)       | Narrower | $E[Yx_0]$    |
| Prediction (individual) | Wider    | $Y_{new}x_0$ |

---

## GATE Tricks

> [!tip] **Simple Linear Regression Shortcuts**
> - **Slope sign = correlation sign**: $r > 0 \Rightarrow \hat{\beta}_1 > 0$
> - **$R^2 = r^2$**: In simple regression only!
> - **Line always passes through $(\bar{x}, \bar{y})$**
> - **Residuals sum to 0**: $\sum e_i = 0$
> - **Prediction interval wider than CI** by factor $\sqrt{1 + \frac{1}{n} + \dots}$

> [!warning] **GATE Traps**
> - Don't confuse $R^2$ (simple) with Multiple $R^2$
> - Extrapolation beyond $x$ range = unreliable
> - Correlation ≠ Causation
> - High $R^2$ ≠ good model (check residuals!)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Confidence Interval | Prediction Interval | CI for mean response, PI for new observation |
| $R^2$ | $r$ | $R^2 = r^2$ (simple only) |
| $\hat{\beta}_1$ | $r$ | $\hat{\beta}_1 = r \cdot s_y/s_x$ |

---

## Common Mistakes

1. **Using $R^2$ alone** → always check residual plots
2. **Ignoring outliers** → single point can flip slope
3. **Assuming linearity** → plot data first!
4. **Extrapolating** → predictions outside $x$ range unreliable
5. **Confusing correlation with slope** → different units!

---

## Memory Tricks

> [!tip] **Slope Formula**: "Cov over Var" = $\frac{Cov(x,y)}{Var(x)}$
> 
> **R² = r²** (ONLY in simple regression!)
> 
> **Line passes through (x̄, ȳ)** = "average point on line"

---

## Previous GATE Patterns

- **Numerical**: Given $\sum x, \sum y, \sum xy, \sum x^2, \sum y^2, n$ → compute $\hat{\beta}_0, \hat{\beta}_1, R^2$
- **Residual calculation**: $e_i = y_i - \hat{y}_i$
- **Prediction**: Given $x_0$, compute $\hat{y}_0$ and PI
- **Interpretation**: Meaning of slope/intercept in context
- **Assumption check**: Residual plots (heteroscedasticity, non-linearity)

---

## Revision Summary

```
SIMPLE LINEAR REGRESSION
├── Model: y = β₀ + β₁x + ε
├── β̂₁ = S_xy/S_xx = Cov(x,y)/Var(x) = r·s_y/s_x
├── β̂₀ = ȳ - β̂₁x̄
├── Line passes through (x̄, ȳ)
├── R² = r² = SS_reg/SS_tot
├── Residuals: Σe_i = 0, Σx_i e_i = 0
├── σ̂² = SS_res/(n-2)
├── CI for β₁: β̂₁ ± t·SE(β̂₁)
├── PI wider than CI (has +1 inside sqrt)
└── Check: linearity, homoscedasticity, normality, independence
```

---

## Related Notes

- [[02 Regression]]
- [[04 Multiple Linear Regression]]
- [[05 Ridge Regression]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #simple-linear-regression #revision