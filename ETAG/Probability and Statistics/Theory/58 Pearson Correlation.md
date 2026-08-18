---
tags: [statistics, gate-da, pearson-correlation, revision]
---

# 58 Pearson Correlation

> [!note] Pearson correlation measures the strength and direction of linear relationship between two variables.

---

## Overview

Pearson correlation coefficient (r) measures the strength and direction of the linear relationship between two quantitative variables. It's the most widely used correlation coefficient.

---

## Formulae

### Pearson Correlation Coefficient
$$r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}$$

**Alternative Formula:**
$$r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

### Population Pearson Correlation
$$\rho = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

### Properties
- $-1 \leq r \leq 1$
- $r = 1$: Perfect positive linear relationship
- $r = -1$: Perfect negative linear relationship
- $r = 0$: No linear relationship
- $r$ is symmetric: $r_{XY} = r_{YX}$
- Invariant to linear transformations: $r_{aX+b, cY+d} = \text{sign}(ac) \cdot r_{XY}$

### Coefficient of Determination
$$R^2 = r^2$$
Proportion of variance in Y explained by linear relationship with X.

### Hypothesis Test for $\rho = 0$
$$t = r \sqrt{\frac{n-2}{1-r^2}} \sim t_{n-2}$$

### Confidence Interval for $\rho$
Using Fisher's z-transformation:
$$z = \frac{1}{2}\ln\left(\frac{1+r}{1-r}\right)$$
$$z \approx N\left(\frac{1}{2}\ln\left(\frac{1+\rho}{1-\rho}\right), \frac{1}{n-3}\right)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $r$ | Sample Pearson correlation |
| $\rho$ | Population Pearson correlation |
| $R^2$ | Coefficient of determination |

---

## GATE Tricks

> [!tip>
> **r = Cov(X,Y) / (s_X s_Y)**
> **-1 ≤ r ≤ 1**
> **r² = proportion of variance explained**
> **Test H₀: ρ = 0**: t = r√((n-2)/(1-r²)) ~ t_{n-2}
> **Linear transform**: r(aX+b, cY+d) = sign(ac) × r(X,Y)

---

## Common Mistakes

> [!warning>
> **r = 0 ≠ No relationship**: Only no LINEAR relationship!
> **Correlation ≠ Causation**: r doesn't imply cause-effect!
> **Outliers**: Can drastically change r!
> **Non-linear**: r = 0 but perfect non-linear relationship possible

---

## Memory Tricks

> [!tip>
> **r** = **R**elationship strength
> **r = 1**: Perfect line going up
> **r = -1**: Perfect line going down
> **r = 0**: No linear pattern
> **r²**: "R squared" = proportion explained

---

## Previous GATE Patterns

- **Compute r**: Given paired data
- **Test significance**: t = r√((n-2)/(1-r²))
- **Interpret r²**: Proportion of variance explained
- **Effect of linear transformation**: sign(ac) × r

---

## Revision Summary

```
PEARSON CORRELATION
├── r = Σ(x-x̄)(y-ȳ) / √[Σ(x-x̄)² Σ(y-ȳ)²]
├── -1 ≤ r ≤ 1
├── r = 1: perfect positive linear
├── r = -1: perfect negative linear
├── r = 0: no linear relationship
├── r² = proportion of variance explained
├── Invariant to linear transforms: sign(ac) × r
├── Test ρ=0: t = r√((n-2)/(1-r²)) ~ t_{n-2}
└── Key: r measures LINEAR relationship only!
```

---

## Related Notes

- [[57 Covariance and Correlation]]
- [[59 Spearman Rank Correlation]]
- [[60 Simple Linear Regression Statistics]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #pearson-correlation #revision