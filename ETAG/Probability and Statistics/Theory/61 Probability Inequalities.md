---
tags: [probability, gate-da, probability-inequalities, revision]
---

# 61 Probability Inequalities

> [!note] Probability inequalities provide bounds on probabilities without requiring exact distributions.

---

## Overview

Probability inequalities give upper or lower bounds on probabilities of events, often with minimal assumptions. They are powerful tools for proving convergence, establishing bounds, and solving GATE numerical problems when exact distributions are unknown.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Inequality** | Mathematical statement providing bounds |
| **Bound** | Upper or lower limit on probability |
| **Tail Bound** | Bound on probability of extreme values |

---

## Formulae

### Markov's Inequality
For $X \geq 0$ and $a > 0$:
$$P(X \geq a) \leq \frac{E[X]}{a}$$

### Chebyshev's Inequality
For any $X$ with finite mean $\mu$ and variance $\sigma^2$:
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad k > 0$$

Equivalently:
$$P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}$$

### Chernoff Bound (General)
$$P(X \geq a) \leq \frac{E[e^{tX}]}{e^{ta}} \quad \text{for } t > 0$$

### Hoeffding's Inequality
For independent $X_i \in [a_i, b_i]$, $S_n = \sum X_i$:
$$P(|S_n - E[S_n]| \geq t) \leq 2 \exp\left(-\frac{2t^2}{\sum (b_i - a_i)^2}\right)$$

### Jensen's Inequality
For convex function $\phi$:
$$\phi(E[X]) \leq E[\phi(X)]$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $E[X]$ | Expected value |
| $\sigma^2$ | Variance |
| $k$ | Number of standard deviations |
| $t$ | Parameter in Chernoff bound |

---

## GATE Tricks

> [!tip>
> **Markov**: $P(X \geq a) \leq E[X]/a$ (only needs $X \geq 0$ and $E[X]$)
> **Chebyshev**: $P(|X-\mu| \geq k\sigma) \leq 1/k^2$ (needs $\mu, \sigma^2$)
> **Chebyshev**: $P(|X-\mu| < k\sigma) \geq 1 - 1/k^2$
> **Key difference**: Markov = one-sided, Chebyshev = two-sided

---

## Common Mistakes

> [!warning>
> **Markov requires $X \geq 0$**: Can't apply to negative RVs!
> **Chebyshev needs finite variance**: Won't work for Cauchy!
> **Confusing one-sided vs two-sided**: Markov = one tail, Chebyshev = two tails
> **$k$ must be $> 1$ for meaningful Chebyshev bound**

---

## Memory Tricks

> [!tip>
> **Markov** = **Mar**kov = **Mar**ginal bound = simple bound
> **Chebyshev** = **Cheb**yshev = **Cheb** = bound on both sides
> **Markov**: One-sided, needs $X \geq 0$
> **Chebyshev**: Two-sided, needs $\mu, \sigma^2$

---

## Previous GATE Patterns

- **Markov application**: Given $E[X]$, find upper bound for $P(X \geq a)$
- **Chebyshev application**: Given $\mu, \sigma$, find bound for $P(|X-\mu| \geq k\sigma)$
- **Comparison**: Which gives tighter bound?
- **Numerical**: Compute bound for given values

---

## Revision Summary

```
PROBABILITY INEQUALITIES
├── Markov: $P(X \geq a) \leq E[X]/a$ (for $X \geq 0$)
├── Chebyshev: $P(|X-\mu| \geq k\sigma) \leq 1/k^2$
├── Chebyshev alt: $P(|X-\mu| < k\sigma) \geq 1 - 1/k^2$
├── Markov: one-sided, needs $X \geq 0$ only
├── Chebyshev: two-sided, needs $\mu, \sigma^2$
├── Chernoff: Uses MGF, tighter for large deviations
├── Hoeffding: For bounded independent sums
└── Key: Markov = simple, Chebyshev = tighter for two-sided
```

---

## Related Notes

- [[62 Markov Inequality]]
- [[63 Chebyshev Inequality]]
- [[33 Central Limit Theorem]]
- [[34 Law of Large Numbers]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #probability-inequalities #markov #chebyshev #revision