---
tags: [statistics, gate-da, covariance-correlation, revision]
---

# 57 Covariance and Correlation

> [!note] Covariance measures joint variability direction. Correlation standardizes it to [-1, 1].

---

## Overview

Covariance and correlation quantify the linear relationship between two variables. Covariance indicates direction, correlation indicates both direction and strength.

---

## Formulae

### Covariance
$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X \mu_Y$$

**Sample Covariance:**
$$s_{XY} = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})$$

### Correlation (Pearson)
$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$
$$r = \frac{s_{XY}}{s_X s_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

### Properties of Covariance
1. $\text{Cov}(X, X) = \text{Var}(X)$
2. $\text{Cov}(X, Y) = \text{Cov}(Y, X)$
3. $\text{Cov}(aX + b, cY + d) = ac \cdot \text{Cov}(X, Y)$
4. $\text{Cov}(X+Y, Z) = \text{Cov}(X, Z) + \text{Cov}(Y, Z)$
5. If $X \perp Y$: $\text{Cov}(X, Y) = 0$

### Properties of Correlation
1. $-1 \leq \rho \leq 1$
2. $\rho_{aX+b, cY+d} = \text{sign}(ac) \cdot \rho_{XY}$
3. $|\rho| = 1 \iff Y = aX + b$ (perfect linear)
4. $\rho = 0 \not\Rightarrow$ independence (except bivariate normal)

### Variance of Sum
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$$

### Variance of Linear Combination
$$\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum a_i^2 \text{Var}(X_i) + 2\sum_{i<j} a_i a_j \text{Cov}(X_i, X_j)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\text{Cov}(X,Y)$ | Covariance |
| $\rho_{XY}$ | Population correlation |
| $r$ | Sample correlation |
| $s_{XY}$ | Sample covariance |

---

## GATE Tricks

> [!tip>
> **Cov(X,X) = Var(X)**
> **Cov(aX+b, cY+d) = ac Cov(X,Y)**
> **Independent ⇒ ρ = 0**, but ρ = 0 ⇏ Independent!
> **ρ = 1**: Y = aX + b (a > 0)
> **ρ = -1**: Y = aX + b (a < 0)
> **Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)**

---

## Common Mistakes

> [!warning>
> **Assuming ρ = 0 means independent**: FALSE!
> **Assuming Cov = 0 means independent**: Same trap!
> **Using ρ formula with wrong SDs**: Must use population σ
> **Forgetting 2Cov in Var(X+Y)**

---

## Memory Tricks

> [!tip>
> **Covariance** = **Co** + **Variance** = joint variation
> **Correlation** = **Cor**rectly scaled covariance
> **ρ = Cov/(σ_X σ_Y)** = "Covariance divided by product of sigmas"

---

## Previous GATE Patterns

- **Compute Cov(X,Y)**: Given joint data
- **Find ρ**: Compute Cov, σ_X, σ_Y
- **Var of sum**: Use covariance formula
- **Linear transformation**: Cov(aX+b, cY+d) = ac Cov(X,Y)

---

## Revision Summary

```
COVARIANCE & CORRELATION
├── Cov(X,Y) = E[XY] - E[X]E[Y]
├── Cov(aX+b, cY+d) = ac Cov(X,Y)
├── Cov(X,X) = Var(X)
├── ρ = Cov/(σ_X σ_Y) ∈ [-1, 1]
├── Independent ⇒ ρ=0, but ρ=0 ⇏ Independent!
├── Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)
├── Var(ΣaᵢXᵢ) = Σaᵢ²Var(Xᵢ) + 2ΣaᵢaⱼCov(Xᵢ,Xⱼ)
├── R² = ρ² = proportion of variance explained
└── Key: ρ = 0 ≠ independence (except bivariate normal)
```

---

## Related Notes

- [[15 Variance and Standard Deviation]]
- [[16 Moments]]
- [[17 Covariance and Correlation]]
- [[58 Pearson Correlation]]
- [[59 Spearman Rank Correlation]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #covariance #correlation #revision