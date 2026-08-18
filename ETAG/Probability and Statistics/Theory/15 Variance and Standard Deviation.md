---
tags: [probability, gate-da, variance, standard-deviation, revision]
---

# 15 Variance and Standard Deviation

> [!note] Variance measures spread around the mean. Standard deviation is the square root, in same units as the data.

---

## Overview

Variance quantifies how much a random variable deviates from its mean. It's the second central moment and fundamental for understanding variability.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Variance** | $Var(X) = E[(X - \mu)^2]$ |
| **Standard Deviation** | $\sigma = \sqrt{Var(X)}$ |
| **Second Central Moment** | $\mu_2 = Var(X)$ |

---

## Formulae

### Definition
$$Var(X) = E[(X - \mu)^2] \quad \text{where } \mu = E[X]$$

### Computational Formula
$$Var(X) = E[X^2] - (E[X])^2$$

### Discrete
$$Var(X) = \sum_i (x_i - \mu)^2 p_i$$

### Continuous
$$Var(X) = \int (x - \mu)^2 f(x) dx$$

### Standard Deviation
$$\sigma_X = \sqrt{Var(X)}$$

### Linear Transformation
$$Var(aX + b) = a^2 Var(X)$$
$$\sigma_{aX+b} = |a| \sigma_X$$

### Sum of Independent Variables
$$Var(X + Y) = Var(X) + Var(Y) \quad \text{if independent}$$

### Sum of Variables (General)
$$Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)$$
$$Var\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n Var(X_i) + 2\sum_{i<j} Cov(X_i, X_j)$$

### For i.i.d. Variables
$$Var(\bar{X}) = \frac{\sigma^2}{n}$$
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $Var(X)$ | Variance of $X$ |
| $\sigma^2$ | Population variance |
| $\sigma$ | Population standard deviation |
| $\sigma_X$ | Standard deviation of $X$ |
| $Cov(X,Y)$ | Covariance of $X$ and $Y$ |

---

## Important Properties

### Non-negativity
$$Var(X) \geq 0$$
$$Var(X) = 0 \iff X \text{ is constant (with probability 1)}$$

### Scale Invariance of Correlation
Correlation is scale-invariant, but variance is not.

### Sample Variance (Bessel's Correction)
$$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$$
$n-1$ makes it unbiased for $\sigma^2$.

### Variance of Linear Combinations
$$Var\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 Var(X_i) + 2\sum_{i<j} a_i a_j Cov(X_i, X_j)$$

---

## Mathematical Intuition

**Average Squared Distance**: Variance = average squared distance from mean. Squaring gives more weight to larger deviations.

**Units**: Variance in squared units of $X$. Standard deviation restores original units.

**Bessel's Correction**: Dividing by $n-1$ (not $n$) corrects the bias from using sample mean $\bar{x}$ instead of true $\mu$.

---

## Algorithms / Problem-Solving

### Computing Variance
```
1. Find E[X] = μ
2. Find E[X²] (LOTUS directly!)
3. Var(X) = E[X²] - μ²
4. σ = √Var(X)
```

### Linear Combinations
```
For Var(aX + bY):
1. Find Var(X), Var(Y), Cov(X,Y)
2. Var = a²Var(X) + b²Var(Y) + 2ab Cov(X,Y)
```

### Sample Variance
```
s² = 1/(n-1) Σ(x_i - x̄)²
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Measure | Formula | Units |
|---------|---------|-------|
| Variance | $E[(X-μ)²]$ | Units² |
| Standard Deviation | $\sqrt{Var(X)}$ | Units of X |
| Covariance | $E[(X-μ_X)(Y-μ_Y)]$ | Units X × Units Y |
| Correlation | $Cov/(σ_X σ_Y)$ | Unitless |

---

## GATE Tricks

> [!tip>
> **Computational formula**: $Var(X) = E[X^2] - (E[X])^2$ - often easier than $E[(X-μ)²]$

> [!tip>
> **$Var(aX+b) = a^2 Var(X)$**: Adding constant doesn't change variance!

> [!tip>
> **Independent ⇒ $Var(X+Y) = Var(X) + Var(Y)$**

> [!tip>
> **Sample variance uses $n-1$**: Unbiased estimator of $\sigma^2$

> [!tip>
> **Variance of sum = sum of variances ONLY if independent!**

> [!tip>
> **$Var(\bar{X}) = \sigma^2/n$**: Standard error = $\sigma/\sqrt{n}$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Variance | Standard Deviation | Squared units vs original units |
| Population Var | Sample Var | $1/n$ vs $1/(n-1)$ |
| $Var(X+Y)$ | $Var(X)+Var(Y)$ | Equal only if independent! |
| Variance | Covariance | $Cov(X,X) = Var(X)$ |

---

## Common Mistakes

> [!warning>
> **Assuming $Var(X+Y) = Var(X) + Var(Y)$ without independence**: Need covariance term!

> [!warning>
> **Using $n$ instead of $n-1$ for sample variance**: Biased!

> [!warning>
> **$Var(aX) = a Var(X)$**: Wrong! It's $a^2 Var(X)$!

> [!warning>
> **$Var(X) = E[X^2] - E[X]^2$**: Order matters! $E[X^2]$ first.

---

## Memory Tricks

> [!tip>
> **Computational**: $Var = E[X^2] - (E[X])^2$ - "Mean of squares minus square of mean"
> **Scaling**: $Var(aX) = a^2 Var(X)$ - "Variance scales with square of constant"
> **Bessel**: "n-1 for sample" - sample uses one degree of freedom for mean

---

## Previous GATE Patterns

- **Compute variance**: Given PMF/PDF, find $E[X^2]$ and $E[X]$
- **Linear transformation**: $Var(aX+b)$
- **Sum of independent**: $Var(\sum X_i) = \sum Var(X_i)$
- **Sample variance**: Identify correct formula ($n$ vs $n-1$)
- **Standard error**: $\sigma/\sqrt{n}$ for sample mean

---

## Revision Summary

```
VARIANCE & STANDARD DEVIATION
├── Var(X) = E[(X-μ)²] = E[X²] - μ²
├── σ = √Var(X)
├── Var(aX+b) = a² Var(X)
├── Independent: Var(X+Y) = Var(X) + Var(Y)
├── General: Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)
├── Sample: s² = 1/(n-1) Σ(xᵢ - x̄)² (Bessel's correction)
├── Var(X̄) = σ²/n, SE = σ/√n
├── Cov(X,X) = Var(X)
└── Key: Computational formula is your friend!
```

---

## Related Notes

- [[14 Expectation]]
- [[16 Moments]]
- [[17 Covariance and Correlation]]
- [[36 Population and Sample]]
- [[38 Sampling Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #variance #standard-deviation #revision