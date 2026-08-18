---
tags: [statistics, gate-da, simple-linear-regression, revision]
---

# 60 Simple Linear Regression Statistics

> [!note] Simple linear regression models the relationship between a dependent variable and one independent variable.

---

## Overview

Simple linear regression models the linear relationship between a dependent variable (Y) and an independent variable (X). It's the foundation for predictive modeling.

---

## Formulae

### Model
$$Y = \beta_0 + \beta_1 X + \epsilon$$
where $\epsilon \sim N(0, \sigma^2)$

### Least Squares Estimates
$$\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}} = r \frac{s_y}{s_x}$$
$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

### Fitted Values & Residuals
$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$$
$$e_i = y_i - \hat{y}_i$$

### Sum of Squares
$$SS_{Total} = \sum (y_i - \bar{y})^2 = S_{yy}$$
$$SS_{Reg} = \sum (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1^2 S_{xx}$$
$$SS_{Res} = \sum (y_i - \hat{y}_i)^2 = SS_{Total} - SS_{Reg}$$

### Coefficient of Determination
$$R^2 = \frac{SS_{Reg}}{SS_{Total}} = 1 - \frac{SS_{Res}}{SS_{Total}} = r^2$$

### Standard Error
$$s = \sqrt{\frac{SS_{Res}}{n-2}} = \sqrt{MSE}$$
$$SE(\hat{\beta}_1) = \frac{s}{\sqrt{S_{xx}}}$$
$$SE(\hat{\beta}_0) = s \sqrt{\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}}$$

### Confidence Intervals
$$\hat{\beta}_1 \pm t_{\alpha/2, n-2} \cdot SE(\hat{\beta}_1)$$

### Prediction Interval (New $x_0$)
$$\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\beta_0, \beta_1$ | True parameters |
| $\hat{\beta}_0, \hat{\beta}_1$ | Estimates |
| $S_{xy}$ | $\sum (x_i - \bar{x})(y_i - \bar{y})$ |
| $S_{xx}$ | $\sum (x_i - \bar{x})^2$ |
| $r$ | Pearson correlation |

---

## GATE Tricks

> [!tip>
> **$\hat{\beta}_1 = r \frac{s_y}{s_x}$**: Slope = correlation × ratio of SDs
> **$R^2 = r^2$**: In simple regression
> **$SS_{Reg} + SS_{Res} = SS_{Total}$**
> **$t = \hat{\beta}_1 / SE(\hat{\beta}_1)$** for testing $\beta_1 = 0$
> **PI wider than CI**: PI has $+1$ inside sqrt

---

## Common Mistakes

> [!warning>
> **Confusing CI and PI**: CI for mean, PI for individual!
> **Extrapolation**: Predictions outside x-range unreliable!
> **Assuming causation**: Regression ≠ causation!
> **R² vs r**: $R^2 = r^2$ in simple regression only!

---

## Memory Tricks

> [!tip>
> **$\hat{\beta}_1 = r \frac{s_y}{s_x}$**: "rise over run" scaled by correlation
> **$R^2 = r^2$**: In simple regression only!
> **PI > CI**: PI has "+1" inside sqrt

---

## Previous GATE Patterns

- **Compute estimates**: Given data, find $\hat{\beta}_0, \hat{\beta}_1$
- **Test significance**: $t = \hat{\beta}_1 / SE(\hat{\beta}_1)$
- **$R^2$ interpretation**: Proportion of variance explained
- **Prediction interval**: For new observation

---

## Revision Summary

```
SIMPLE LINEAR REGRESSION
├── Model: Y = β₀ + β₁X + ε
├── β̂₁ = S_{xy}/S_{xx} = r s_y/s_x
├── β̂₀ = ȳ - β̂₁ x̄
├── R² = r² = SS_Reg / SS_Total
├── s² = SS_Res/(n-2)
├── SE(β̂₁) = s/√S_{xx}
├── CI for β₁: β̂₁ ± t·SE
├── PI: ŷ₀ ± t·s√(1 + 1/n + (x₀-x̄)²/S_{xx})
└── Key: β̂₁ = r × (s_y/s_x), R² = r²
```

---

## Related Notes

- [[57 Covariance and Correlation]]
- [[58 Pearson Correlation]]
- [[59 Spearman Rank Correlation]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #simple-linear-regression #revision