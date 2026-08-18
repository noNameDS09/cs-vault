---
tags: [probability, gate-da, normal, continuous-distribution, revision]
---

# 31 Normal Distribution

> [!note] The most important continuous distribution - bell-shaped, symmetric, central to CLT and statistical inference.

---

## Overview

The Normal (Gaussian) distribution is the most important continuous distribution in statistics. It appears naturally due to the Central Limit Theorem and forms the basis for most parametric statistical inference.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Parameters** | $\mu$ (mean), $\sigma^2$ (variance) |
| **Support** | $(-\infty, \infty)$ |
| **Shape** | Bell-shaped, symmetric about $\mu$ |
| **Standard Normal** | $Z \sim N(0,1)$ |

---

## Formulae

### PDF
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$

### CDF
$$F(x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$$
where $\Phi$ is the standard normal CDF.

### Mean
$$E[X] = \mu$$

### Variance
$$Var(X) = \sigma^2$$

### MGF
$$M(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$

### Standardization
$$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$
$$X = \mu + \sigma Z$$

### Probabilities
$$P(X \leq x) = \Phi\left(\frac{x-\mu}{\sigma}\right)$$
$$P(a < X < b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right)$$

### Symmetry
$$\Phi(-z) = 1 - \Phi(z)$$

### 68-95-99.7 Rule (Empirical Rule)
- $P(\mu - \sigma < X < \mu + \sigma) \approx 0.68$
- $P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.95$
- $P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.997$

### Key Quantiles
| Probability | $z$-value |
|-------------|-----------|
| 0.90 | 1.282 |
| 0.95 | 1.645 |
| 0.975 | 1.96 |
| 0.99 | 2.326 |
| 0.995 | 2.576 |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\mu$ | Mean (location) |
| $\sigma$ | Standard deviation (scale) |
| $\sigma^2$ | Variance |
| $Z$ | Standard normal variable |

---

## Important Properties

### Linear Transformation
If $X \sim N(\mu, \sigma^2)$, then $aX + b \sim N(a\mu + b, a^2\sigma^2)$

### Sum of Independent Normals
If $X_i \sim N(\mu_i, \sigma_i^2)$ independent:
$$\sum X_i \sim N\left(\sum \mu_i, \sum \sigma_i^2\right)$$

### Sample Mean
If $X_1, ..., X_n$ i.i.d. $\sim N(\mu, \sigma^2)$:
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### Sample Variance
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$
And $\bar{X} \perp S^2$

### MGF of Normal
$$M(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$
Recognize this pattern for sums!

### Multivariate Normal
Joint PDF for $\mathbf{X} = (X_1, ..., X_p)^T$:
$$f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}} e^{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T \Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu})}$$

---

## Mathematical Intuition

**Bell Curve**: Symmetric, unimodal, maximum at $\mu$. Inflection points at $\mu \pm \sigma$.

**CLT**: Sum of many independent variables → approximately normal, regardless of original distributions.

**MGF Pattern**: $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ - recognize this for sums!

---

## Algorithms / Problem-Solving

### Normal Problems
```
1. Identify μ and σ
2. Standardize: Z = (X - μ)/σ
3. Use standard normal table/values: Φ(z)
4. Use symmetry: Φ(-z) = 1 - Φ(z)
5. For sample mean: use σ/√n
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Standardize**: Z = (X - μ)/σ
> **Use Φ table**: P(X ≤ x) = Φ((x-μ)/σ)
> **Symmetry**: Φ(-z) = 1 - Φ(z)
> **Empirical rule**: 68-95-99.7 within 1,2,3 σ
> **Key percentiles**: 1.645 (95%), 1.96 (97.5%), 2.576 (99.5%)
> **Sum of normals**: Sum means, sum variances
> **Sample mean**: N(μ, σ²/n)
> **MGF**: e^(μt + ½σ²t²) - recognize for sums!

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| X | Z | Original vs standardized |
| σ | σ² | SD vs variance |
| P(X < x) | P(X > x) | Φ(z) vs 1-Φ(z) |
| Population | Sample mean | σ vs σ/√n |

---

## Common Mistakes

> [!warning>
> **Using σ instead of σ/√n for sample mean**
> **Forgetting symmetry**: Φ(-z) = 1 - Φ(z)
> **Using wrong tail**: P(X > x) = 1 - Φ(z)
> **Not standardizing**: Always use Z = (X-μ)/σ

---

## Memory Tricks

> [!tip>
> **Normal** = **Nor**mal = **Nor**m = standard
> **68-95-99.7**: Empirical rule for 1,2,3 σ
> **Standardize**: "Z = (X - μ)/σ"
> **MGF**: e^(μt + ½σ²t²) - sum of normals = normal

---

## Previous GATE Patterns

- **Standardization**: Compute P(a < X < b) given μ, σ
- **Sample mean**: P(\bar{X} > c) using σ/√n
- **Sum of normals**: Recognize MGF pattern
- **Percentiles**: Find x such that P(X ≤ x) = p
- **Confidence intervals**: z-based for normal

---

## Revision Summary

```
NORMAL DISTRIBUTION
├── f(x) = 1/(σ√2π) e^(-(x-μ)²/(2σ²))
├── Support: (-∞, ∞)
├── Mean = μ, Variance = σ²
├── Standardize: Z = (X-μ)/σ ~ N(0,1)
├── P(X ≤ x) = Φ((x-μ)/σ)
├── Symmetry: Φ(-z) = 1-Φ(z)
├── 68-95-99.7 rule (1,2,3 σ)
├── Key percentiles: 1.645, 1.96, 2.576
├── Linear transform: aX+b ~ N(aμ+b, a²σ²)
├── Sum: ΣXᵢ ~ N(Σμᵢ, Σσᵢ²)
├── Sample mean: X̄ ~ N(μ, σ²/n)
├── MGF: e^(μt + ½σ²t²)
└── Key: Standardize to Z, use Φ table!
```

---

## Related Notes

- [[30 Exponential Distribution]]
- [[32 Standard Normal Distribution]]
- [[33 Central Limit Theorem]]
- [[36 Population and Sample]]
- [[38 Sampling Distribution]]
- [[47 Confidence Intervals]]
- [[48 z Test]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #normal #continuous-distribution #revision