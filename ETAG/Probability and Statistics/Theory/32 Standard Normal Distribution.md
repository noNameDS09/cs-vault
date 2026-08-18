---
tags: [probability, gate-da, standard-normal, revision]
---

# 32 Standard Normal Distribution

> [!note] Normal distribution with mean 0 and variance 1. The reference distribution for all normal probabilities.

---

## Overview

The Standard Normal distribution $Z \sim N(0,1)$ is the normalized version of any normal distribution. All normal probabilities are computed by standardizing to $Z$.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Standard Normal** | $Z \sim N(0,1)$ |
| **Standardization** | $Z = \frac{X-\mu}{\sigma}$ |
| **CDF** | $\Phi(z) = P(Z \leq z)$ |

---

## Formulae

### PDF
$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$$

### CDF
$$\Phi(z) = P(Z \leq z) = \int_{-\infty}^z \phi(t) dt$$

### Symmetry
$$\Phi(-z) = 1 - \Phi(z)$$
$$\phi(-z) = \phi(z)$$

### Tail Probabilities
$$P(Z > z) = 1 - \Phi(z)$$
$$P(|Z| > z) = 2(1 - \Phi(z))$$
$$P(|Z| < z) = 2\Phi(z) - 1$$

### Key Percentiles (Memorize!)
| $\alpha$ | $z_\alpha$ (one-tail) | $z_{\alpha/2}$ (two-tail) |
|----------|----------------------|---------------------------|
| 0.10 | 1.282 | 1.645 |
| 0.05 | 1.645 | 1.96 |
| 0.025 | 1.96 | 2.241 |
| 0.01 | 2.326 | 2.576 |
| 0.005 | 2.576 | 2.807 |

### MGF
$$M(t) = e^{t^2/2}$$

### Moments
- $E[Z] = 0$
- $Var(Z) = 1$
- $E[Z^2] = 1$
- $E[Z^3] = 0$
- $E[Z^4] = 3$
- Skewness = 0, Kurtosis = 3 (excess = 0)

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $Z$ | Standard normal variable |
| $\phi(z)$ | Standard normal PDF |
| $\Phi(z)$ | Standard normal CDF |
| $z_\alpha$ | Upper $\alpha$ quantile |

---

## Important Properties

### Symmetry Properties
- $\Phi(0) = 0.5$
- $\Phi(-z) = 1 - \Phi(z)$
- $P(Z > z) = P(Z < -z)$

### Standardization
If $X \sim N(\mu, \sigma^2)$, then $Z = \frac{X-\mu}{\sigma} \sim N(0,1)$

### Tail Bounds (Mills' Ratio)
For $z > 0$:
$$\frac{1}{z} - \frac{1}{z^3} < \frac{1-\Phi(z)}{\phi(z)} < \frac{1}{z}$$

---

## Mathematical Intuition

**Reference Distribution**: All normal distributions transform to $Z \sim N(0,1)$ via $Z = \frac{X-\mu}{\sigma}$.

**Tables/Software**: Standard normal tables/software give $\Phi(z)$. All normal probabilities reduce to this.

**Symmetry**: The bell curve is perfectly symmetric about 0.

---

## Algorithms / Problem-Solving

### Computing Normal Probabilities
```
1. Standardize: Z = (X - μ)/σ
2. Look up Φ(z) or use software
3. Apply symmetry if needed: Φ(-z) = 1 - Φ(z)
4. For intervals: P(a < X < b) = Φ((b-μ)/σ) - Φ((a-μ)/σ)
```

### Finding Percentiles
```
Given p, find z such that Φ(z) = p
Use inverse CDF (quantile function)
Common: z_0.025 = 1.96, z_0.05 = 1.645
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Φ(0) = 0.5**
> **Φ(-z) = 1 - Φ(z)**
> **P(|Z| < z) = 2Φ(z) - 1**
> **Key percentiles**: 1.645, 1.96, 2.326, 2.576
> **P(Z > z) = 1 - Φ(z)**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $\phi(z)$ | $\Phi(z)$ | PDF vs CDF |
| $z_\alpha$ | $z_{\alpha/2}$ | One-tail vs two-tail |
| $P(Z < z)$ | $P(Z > z)$ | $\Phi(z)$ vs $1-\Phi(z)$ |

---

## Common Mistakes

> [!warning>
> **Using $z_\alpha$ instead of $z_{\alpha/2}$ for two-tailed tests**
> **Forgetting symmetry**: $\Phi(-z) = 1 - \Phi(z)$
> **Confusing PDF and CDF**: $\phi$ vs $\Phi$

---

## Memory Tricks

> [!tip>
> **Φ** = **P**hi = **P**robability = CDF
> **ϕ** = **p**hi = **p**df = PDF
> **1.96** = 95% two-tail
> **2.576** = 99% two-tail

---

## Previous GATE Patterns

- **Standardize**: Convert X to Z
- **Find probability**: $\Phi(z)$
- **Find percentile**: Given p, find z
- **Two-tailed**: Use $z_{\alpha/2}$
- **Confidence intervals**: Use $z_{\alpha/2}$

---

## Revision Summary

```
STANDARD NORMAL DISTRIBUTION
├── Z ~ N(0,1)
├── φ(z) = 1/√(2π) e^(-z²/2) (PDF)
├── Φ(z) = P(Z ≤ z) (CDF)
├── Φ(-z) = 1 - Φ(z) (symmetry)
├── P(Z > z) = 1 - Φ(z)
├── P(|Z| < z) = 2Φ(z) - 1
├── Key percentiles: 1.645 (90%), 1.96 (95%), 2.576 (99.5%)
├── Standardize: Z = (X-μ)/σ
└── Key: All normal → standard normal!
```

---

## Related Notes

- [[31 Normal Distribution]]
- [[33 Central Limit Theorem]]
- [[47 Confidence Intervals]]
- [[48 z Test]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #standard-normal #revision