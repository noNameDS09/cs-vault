---
tags: [probability, gate-da, geometric, discrete-distribution, revision]
---

# 26 Geometric Distribution

> [!note] Number of trials until the first success in independent Bernoulli trials.

---

## Overview

The Geometric distribution models the number of trials needed to get the first success in a sequence of independent Bernoulli trials. It's the only discrete distribution with the memoryless property.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Trial** | Independent Bernoulli trial with success prob p |
| **X** | Number of trials until first success |
| **Support** | {1, 2, 3, ...} |

---

## Formulae

### PMF
$$P(X = k) = (1-p)^{k-1} p = q^{k-1} p, \quad k = 1, 2, 3, ...$$

### Mean
$$E[X] = \frac{1}{p}$$

### Variance
$$Var(X) = \frac{1-p}{p^2} = \frac{q}{p^2}$$

### CDF
$$F(k) = P(X \leq k) = 1 - q^k$$

### Survival Function
$$P(X > k) = q^k$$

### MGF
$$M(t) = \frac{pe^t}{1 - qe^t}, \quad t < -\ln q$$

### Memoryless Property
$$P(X > m+n | X > m) = P(X > n) = q^n$$
**Only discrete distribution with this property!**

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | Probability of success per trial |
| $q = 1-p$ | Probability of failure |
| $k$ | Trial number of first success |

---

## Important Properties

### Memoryless Property
$$P(X > m+n | X > m) = P(X > n)$$
**The ONLY discrete memoryless distribution!**

### Relation to Bernoulli
$X = \min\{k: X_k = 1\}$ where $X_i \sim Bernoulli(p)$ i.i.d.

### Sum of Independent Geometrics
Sum of $r$ i.i.d. Geometric($p$) = Negative Binomial($r, p$)

### Hazard Rate (Constant)
$$h(k) = P(X=k | X \geq k) = p$$

---

## Mathematical Intuition

**Waiting for First Success**: Keep flipping a biased coin until heads appears. X = number of flips.

**Memoryless**: "The coin has no memory" - past failures don't change future success probability.

**Constant Hazard**: At each trial, probability of success is p, regardless of history.

---

## Algorithms / Problem-Solving

### Geometric Problems
```
1. Identify: "until first success" or "number of trials until"
2. Identify p (success prob per trial)
3. X = trial number of first success (1, 2, 3, ...)
4. PMF: P(X=k) = q^(k-1) * p
5. P(X > k) = q^k
5. E[X] = 1/p, Var = q/p^2
5. Use memoryless property when applicable
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Geometric**: Trials UNTIL first success
> **Support**: {1, 2, 3, ...} (NOT 0,1,2...!)
> **Mean = 1/p**, **Var = q/p^2**
> **Memoryless**: P(X > m+n | X > m) = P(X > n)
> **P(X > k) = q^k**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Geometric | Binomial | Wait for 1st success vs count in n |
| Geometric | Negative Binomial | 1st success vs r-th success |
| Support {1,2,...} | Support {0,1,...} | Some texts use {0,1,...} for failures |

---

## Common Mistakes

> [!warning>
> **Support is {1,2,3,...} NOT {0,1,2,...}!** (unless counting failures)
> **PMF**: q^(k-1)p, NOT q^k p
> **Mean = 1/p**, NOT p or 1/q
> **Memoryless only for Geometric/Exponential**

---

## Memory Tricks

> [!tip>
> **Geometric** = **Geo**metric = **Geo** = earth/ground = waiting for first success
> **1/p** = mean (1 over p)
> **q/p^2** = variance
> **Memoryless**: "No memory of past failures"

---

## Previous GATE Patterns

- **Identify distribution**: "Number of trials until first success"
- **P(X > k)**: Use q^k directly
- **Memoryless**: Use P(X > m+n | X > m) = P(X > n)
- **Find p**: Given mean = 1/p, find p
- **Sum of geometrics**: Negative Binomial

---

## Revision Summary

```
GEOMETRIC DISTRIBUTION
├── X = trials until first success
├── Support: {1, 2, 3, ...}
├── PMF: P(X=k) = q^(k-1) p
├── Mean = 1/p
├── Variance = q/p^2
├── P(X > k) = q^k
├── Memoryless: P(X>m+n|X>m) = P(X>n) ⭐ ONLY discrete!
├── Hazard rate: p (constant)
└── Key: 1/p for mean, q/p^2 for var, memoryless!
```

---

## Related Notes

- [[24 Bernoulli Distribution]]
- [[25 Binomial Distribution]]
- [[27 Poisson Distribution]]
- [[30 Exponential Distribution]] (continuous analog)
- [[GATE Numerical Tricks]]

---

#probability #gate-da #geometric #discrete-distribution #revision