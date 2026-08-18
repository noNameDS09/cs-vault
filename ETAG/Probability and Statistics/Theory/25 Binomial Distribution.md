---
tags: [probability, gate-da, binomial, discrete-distribution, revision]
---

# 25 Binomial Distribution

> [!note] Number of successes in n independent Bernoulli trials, each with success probability p.

---

## Overview

The Binomial distribution models the number of successes in a fixed number of independent Bernoulli trials. It's one of the most widely used discrete distributions.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **n trials** | Fixed number of independent trials |
| **Success** | Probability p (same for each trial) |
| **X** | Number of successes in n trials |
| **Parameters** | n (trials), p (success probability) |

---

## Formulae

### PMF
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, ..., n$$

### Mean
$$E[X] = np$$

### Variance
$$Var(X) = np(1-p) = npq$$

### MGF
$$M(t) = (1-p + pe^t)^n = (q + pe^t)^n$$

### Mode
$$\text{Mode} = \lfloor (n+1)p \rfloor \quad \text{(if not integer)} \quad \text{or } (n+1)p \text{ and } (n+1)p - 1 \text{ (if integer)}$$

### Sum of Independent Binomials
If $X \sim Bin(n_1, p)$ and $Y \sim Bin(n_2, p)$ independent:
$$X + Y \sim Bin(n_1 + n_2, p)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of trials |
| $p$ | Success probability per trial |
| $q = 1-p$ | Failure probability |
| $k$ | Number of successes |

---

## Important Properties

### Additivity
Sum of independent Binomials with same $p$ is Binomial with summed $n$.

### Poisson Approximation
If $n$ large, $p$ small, $np = \lambda$:
$$Bin(n, p) \approx Poisson(\lambda)$$
Good when $n \geq 20$, $p \leq 0.05$, $np \leq 5$

### Normal Approximation
If $np \geq 5$ and $nq \geq 5$:
$$Bin(n, p) \approx N(np, npq)$$
With continuity correction: $P(X=k) \approx P(k-0.5 < N < k+0.5)$

### Relationship to Bernoulli
$$X = \sum_{i=1}^n X_i \quad \text{where } X_i \sim Bernoulli(p) \text{ i.i.d.}$$

---

## Mathematical Intuition

**n Coin Flips**: Count heads in n flips of a coin with P(heads)=p.

**Combinatorial**: $\binom{n}{k}$ ways to choose which $k$ trials succeed, each with prob $p^k q^{n-k}$.

---

## Algorithms / Problem-Solving

### Binomial Problems
```
1. Identify: fixed n trials, success prob p, count successes
2. Check: independent trials, constant p
3. Compute P(X=k) using PMF
3. For "at least k": 1 - P(X ≤ k-1)
4. For large n: use normal approximation with continuity correction
5. For rare events (n large, p small): use Poisson approximation
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Binomial**: n fixed trials, count successes
> **Mean = np, Variance = npq**
> **PMF**: nCk * p^k * q^(n-k)
> **Mode**: floor((n+1)p)

> [!tip>
> **Poisson approx**: n large, p small, np = λ
> **Normal approx**: np ≥ 5 and nq ≥ 5
> **Sum of Binomials**: Same p → add n's

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Binomial | Poisson | Fixed n vs rate λ |
| Binomial | Geometric | Count successes in n vs wait for 1st success |
| Binomial | Negative Binomial | n fixed vs r fixed |

---

## Common Mistakes

> [!warning>
> **Using nCk when n is large**: Use approximation!
> **Forgetting continuity correction**: Normal approx needs ±0.5
> **Using Binomial when trials not independent**: Must be independent!
> **p changes between trials**: Not Binomial then!

---

## Memory Tricks

> [!tip>
> **Binomial** = **Bi**nomial = **Bi** = two outcomes (success/failure)
> **Mean = np**, **Var = npq** (p then q)
> **PMF**: "n choose k" times p^k times q^(n-k)

---

## Previous GATE Patterns

- **Direct PMF**: Given n, p, find P(X=k)
- **Cumulative**: P(X ≤ k) or P(X ≥ k)
- **Find parameters**: Given mean/var, find n, p
- **Approximations**: Poisson or Normal approximation
- **Sum of Binomials**: Add n's when same p

---

## Revision Summary

```
BINOMIAL DISTRIBUTION
├── n independent trials, success prob p
├── X = # successes, k = 0,1,...,n
├── PMF: P(X=k) = C(n,k) p^k q^(n-k)
├── Mean = np
├── Variance = npq
├── Mode = floor((n+1)p)
├── Approximations:
│   ├── Poisson: n large, p small, np=λ
│   └── Normal: np≥5, nq≥5 (with continuity correction)
├── Sum of independent (same p): add n's
└── Key: np for mean, npq for variance
```

---

## Related Notes

- [[24 Bernoulli Distribution]]
- [[23 Important Discrete Distributions]]
- [[27 Poisson Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #binomial #discrete-distribution #revision