---
tags: [probability, gate-da, chebyshev-inequality, revision]
---

# 63 Chebyshev Inequality

> [!note] Chebyshev's inequality provides a two-sided bound on the probability that a random variable deviates from its mean.

---

## Overview

Chebyshev's inequality gives an upper bound on the probability that a random variable deviates from its mean by more than a certain number of standard deviations. It works for any distribution with finite mean and variance.

---

## Formulae

### Chebyshev's Inequality
For any random variable $X$ with finite mean $\mu$ and finite variance $\sigma^2$:
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad k > 0$$

### Equivalent Forms
$$P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}$$

$$P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2} \quad \text{(where } a > 0\text{)}$$

### Proof Sketch
$$P(|X - \mu| \geq k\sigma) = P((X - \mu)^2 \geq k^2\sigma^2) \leq \frac{E[(X - \mu)^2]}{k^2\sigma^2} = \frac{\sigma^2}{k^2\sigma^2} = \frac{1}{k^2}$$
(using Markov's inequality on $(X - \mu)^2$)

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\mu$ | Population mean |
| $\sigma^2$ | Population variance |
| $k$ | Number of standard deviations ($k > 0$) |
| $a$ | Deviation threshold ($a > 0$) |

---

## Important Properties

### Requirements
- Finite mean $\mu$
- Finite variance $\sigma^2$
- $k > 0$ (or $a > 0$)

### Two-Sided Bound
- Bounds **both tails** simultaneously
- $P(|X - \mu| \geq k\sigma)$ includes both tails

### Tightness
- Can be tight for some distributions (e.g., two-point distribution at $\mu \pm \sigma$)
- Often loose for specific distributions (e.g., normal gives much tighter bounds)

### Relation to Markov
Chebyshev is derived from Markov applied to $(X - \mu)^2$:
$$P(|X - \mu| \geq k\sigma) = P((X - \mu)^2 \geq k^2\sigma^2) \leq \frac{E[(X - \mu)^2]}{k^2\sigma^2} = \frac{1}{k^2}$$

---

## GATE Tricks

> [!tip>
> **Chebyshev**: $P(|X-\mu| \geq k\sigma) \leq 1/k^2$
> **Alternative**: $P(|X-\mu| < k\sigma) \geq 1 - 1/k^2$
> **Two-sided**: Bounds BOTH tails
> **Needs**: $\mu, \sigma^2$ finite
> **For $k=2$**: At least 75% within $2\sigma$
> **For $k=3$**: At least 88.9% within $3\sigma$

---

## Common Mistakes

> [!warning>
> **Using $k \leq 1$**: Bound is trivial ($\geq 1$)!
> **Confusing one-sided vs two-sided**: Chebyshev is two-sided!
> **Using for one tail**: $P(X-\mu \geq k\sigma) \leq 1/(2k^2)$ only if symmetric!
> **Applying to Cauchy**: Variance doesn't exist!

---

## Memory Tricks

> [!tip>
> **Chebyshev** = **Cheb** = **Cheb** both sides = two-sided
> **$1/k^2$** = "one over k squared"
> **$k=2$**: 75% within $2\sigma$
> **$k=3$**: 88.9% within $3\sigma$

---

## Previous GATE Patterns

- **Direct application**: Given $\mu, \sigma$, bound $P(|X-\mu| \geq k\sigma)$
- **Sample size**: Find $n$ such that sample mean is within $\epsilon$ with probability $1-\alpha$
- **Comparison**: Chebyshev vs Markov vs exact distribution

---

## Revision Summary

```
CHEBYSHEV INEQUALITY
├── P(|X - μ| ≥ kσ) ≤ 1/k²
├── P(|X - μ| < kσ) ≥ 1 - 1/k²
├── Two-sided bound (both tails)
├── Needs: finite μ, σ²
├── Derived from Markov on (X-μ)²
├── k=2: ≥ 75% within 2σ
├── k=3: ≥ 88.9% within 3σ
└── Key: Two-sided, needs μ and σ²!
```

---

## Related Notes

- [[61 Probability Inequalities]]
- [[62 Markov Inequality]]
- [[34 Law of Large Numbers]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #chebyshev-inequality #revision