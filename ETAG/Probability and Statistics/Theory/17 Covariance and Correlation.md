---
tags: [probability, gate-da, covariance, correlation, revision]
---

# 17 Covariance and Correlation

> [!note] Covariance measures joint variability direction. Correlation standardizes it to [-1, 1].

---

## Overview

Covariance and correlation quantify the linear relationship between two random variables. Covariance has units and is hard to interpret; correlation is unit-free and ranges from -1 to 1.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Covariance** | $Cov(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$ |
| **Correlation** | $\rho_{XY} = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$ |
| **Linear Relationship** | Correlation measures strength of linear association |

---

## Formulae

### Covariance
$$Cov(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X \mu_Y$$

### Properties of Covariance
1. $Cov(X, X) = Var(X)$
2. $Cov(X, Y) = Cov(Y, X)$
3. $Cov(aX + b, cY + d) = ac \cdot Cov(X, Y)$
4. $Cov(X+Y, Z) = Cov(X, Z) + Cov(Y, Z)$
5. If $X \perp Y$: $Cov(X, Y) = 0$

### Correlation
$$\rho_{XY} = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}, \quad -1 \leq \rho \leq 1$$

### Properties of Correlation
1. $\rho_{XY} = \rho_{YX}$
2. $\rho_{aX+b, cY+d} = \text{sign}(ac) \cdot \rho_{XY}$
3. $|\rho| \leq 1$
4. $|\rho| = 1 \iff Y = aX + b$ (perfect linear relationship)
5. $\rho = 0 \not\Rightarrow$ independence (except for bivariate normal)

### Variance of Sum
$$Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)$$

### Variance of Linear Combination
$$Var\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 Var(X_i) + 2\sum_{i<j} a_i a_j Cov(X_i, X_j)$$

### Sample Covariance & Correlation
$$s_{XY} = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})$$
$$r = \frac{s_{XY}}{s_X s_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $Cov(X,Y)$ | Covariance of $X$ and $Y$ |
| $\rho_{XY}$ | Population correlation |
| $r$ | Sample correlation |
| $s_{XY}$ | Sample covariance |
| $s_X, s_Y$ | Sample standard deviations |

---

## Important Properties

### Cauchy-Schwarz Inequality
$$|Cov(X,Y)| \leq \sigma_X \sigma_Y \implies |\rho| \leq 1$$

### Correlation = 0 $\not\Rightarrow$ Independence
- Uncorrelated ($\rho=0$) does NOT imply independent
- Independent $\Rightarrow$ $\rho=0$
- Exception: Bivariate normal $\Rightarrow$ $\rho=0 \iff$ independent

### Coefficient of Determination
$$R^2 = \rho^2$$
Proportion of variance explained by linear relationship.

---

## Mathematical Intuition

**Covariance**: Average of $(X-\mu_X)(Y-\mu_Y)$. Positive when both deviate in same direction, negative when opposite.

**Correlation**: Standardized covariance. Divides by product of standard deviations to get unit-free measure.

**$\rho = \pm 1$**: Perfect linear relationship ($Y = aX + b$)

**$\rho = 0$**: No linear relationship (but could be nonlinear!)

---

## Algorithms / Problem-Solving

### Computing Covariance
```
1. Find E[X], E[Y], E[XY] (use LOTUS: E[XY] = ΣΣ xy p(x,y) or ∫∫ xy f(x,y) dx dy)
2. Cov = E[XY] - E[X]E[Y]
3. Find Var(X), Var(Y)
4. ρ = Cov / (σ_X σ_Y)
```

### Using Correlation
```
For Var(aX + bY):
1. Var = a²Var(X) + b²Var(Y) + 2ab ρ σ_X σ_Y
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Measure | Range | Units | Interpretation |
|---------|-------|-------|----------------|
| Covariance | $(-\infty, \infty)$ | X × Y | Direction only |
| Correlation | $[-1, 1]$ | None | Strength & direction |

| $\rho$ Value | Interpretation |
|--------------|----------------|
| $\approx 1$ | Strong positive linear |
| $\approx 0.5$ | Moderate positive |
| $\approx 0$ | No linear |
| $\approx -0.5$ | Moderate negative |
| $\approx -1$ | Strong negative |

---

## GATE Tricks

> [!tip>
> **Cov(X,X) = Var(X)**: Quick check!
> **Cov(aX+b, cY+d) = ac Cov(X,Y)**: Scale by ac, constants b,d drop out!
> **Independent ⇒ ρ = 0**, but ρ = 0 ⇏ Independent!
> **Perfect correlation**: ρ = 1 means Y = aX + b with a > 0; ρ = -1 means a < 0
> **Variance of sum**: Always use Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Covariance | Correlation | Units vs unit-free |
| ρ = 0 | Independent | Zero linear vs no relationship at all |
| Cov(X,Y) | Cov(X,X) | Joint vs variance |
| Sample r | Population ρ | Estimator vs parameter |

---

## Common Mistakes

> [!warning>
> **Assuming ρ = 0 means independent**: FALSE! Only means no linear relationship.
> **Assuming Cov(X,Y) = 0 means independent**: Same trap!
> **Using ρ formula with wrong variances**: Must use population σ, not sample s
> **Forgetting 2Cov in Var(X+Y)**: Critical for dependent variables!

---

## Memory Tricks

> [!tip>
> **Covariance** = **Co** + **Variance** = joint variation
> **Correlation** = **Cor**rectly scaled covariance
> **ρ = Cov/(σ_X σ_Y)** = "Covariance divided by product of sigmas"
> **ρ = 1**: "Perfect positive" = line going up

---

## Previous GATE Patterns

- **Compute Cov(X,Y)**: Given joint distribution, find E[XY] - μ_X μ_Y
- **Find ρ**: Compute Cov, σ_X, σ_Y
- **Var of sum**: Use covariance formula
- **Linear transformation**: Cov(aX+b, cY+d) = ac Cov(X,Y)
- **Correlation from regression**: ρ = sign(β) * sqrt(R²)

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
- [[18 Joint Probability Distributions]]
- [[19 Marginal Distributions]]
- [[21 Independence of Random Variables]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #covariance #correlation #revision