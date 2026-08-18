---
tags: [probability, gate-da, markov-inequality, revision]
---

# 62 Markov Inequality

> [!note] Markov's inequality provides an upper bound on the probability that a non-negative random variable exceeds a given value.

---

## Overview

Markov's inequality is one of the simplest and most fundamental probability inequalities. It provides an upper bound on the probability that a non-negative random variable exceeds a given threshold, using only its expected value.

---

## Formulae

### Markov's Inequality
For a non-negative random variable $X \geq 0$ and any $a > 0$:
$$P(X \geq a) \leq \frac{E[X]}{a}$$

### Alternative Form
For $a = k \cdot E[X]$ where $k > 1$:
$$P(X \geq k \cdot E[X]) \leq \frac{1}{k}$$

### Proof Sketch
$$E[X] = \int_0^\infty x f(x) dx \geq \int_a^\infty x f(x) dx \geq a \int_a^\infty f(x) dx = a \cdot P(X \geq a)$$
Therefore: $P(X \geq a) \leq E[X]/a$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $X$ | Non-negative random variable ($X \geq 0$) |
| $a$ | Threshold value ($a > 0$) |
| $E[X]$ | Expected value of $X$ |

---

## Important Properties

### Requirements
- $X$ must be **non-negative** ($X \geq 0$)
- $E[X]$ must be **finite**
- $a > 0$

### Tightness
- Bound can be tight for some distributions (e.g., two-point distribution)
- Often loose for specific distributions

### Generalization
For any increasing function $\phi(x) \geq 0$:
$$P(X \geq a) = P(\phi(X) \geq \phi(a)) \leq \frac{E[\phi(X)]}{\phi(a)}$$
Choosing $\phi(x) = x^k$ gives moments-based bounds.

---

## GATE Tricks

> [!tip>
> **Markov**: $P(X \geq a) \leq E[X]/a$
> **Requires**: $X \geq 0$ and $E[X]$ known
> **One-sided**: Only bounds upper tail
> **Simple but often loose**

---

## Common Mistakes

> [!warning>
> **Applying to negative RVs**: Markov requires $X \geq 0$!
> **Using for $P(X \leq a)$**: Markov only bounds upper tail!
> **Assuming tight bound**: Often very conservative!

---

## Memory Tricks

> [!tip>
> **Markov** = **Mar**kov = **Mar**ginal bound = simple
> **$E[X]/a$** = mean divided by threshold
> **Non-negative only!**

---

## Previous GATE Patterns

- **Direct application**: Given $E[X]$, find upper bound for $P(X \geq a)$
- **Parameter estimation**: Given $P(X \geq a) \leq p$, find $E[X]$
- **Comparison**: Compare with Chebyshev bound

---

## Revision Summary

```
MARKOV INEQUALITY
├── P(X ≥ a) ≤ E[X]/a
├── Requires: X ≥ 0, a > 0
├── One-sided upper bound
├── Simple but often loose
├── Generalized: P(X ≥ a) ≤ E[φ(X)]/φ(a) for increasing φ
└── Key: Needs X ≥ 0 and finite E[X]!
```

---

## Related Notes

- [[61 Probability Inequalities]]
- [[63 Chebyshev Inequality]]
- [[34 Law of Large Numbers]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #markov-inequality #revision