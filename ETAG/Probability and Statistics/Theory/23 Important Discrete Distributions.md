---
tags: [probability, gate-da, discrete-distributions, revision]
---

# 23 Important Discrete Distributions

> [!note] Overview of key discrete distributions: Bernoulli, Binomial, Geometric, Poisson. Each has dedicated notes.

---

## Overview

Discrete distributions model countable outcomes. Each has specific assumptions, PMF, mean, variance, and applications. Understanding when to use which is crucial for GATE.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **PMF** | $P(X=x)$ for each possible value |
| **Support** | Set of possible values |
| **Parameters** | Numbers defining the distribution |

---

## Formulae Summary

### Bernoulli($p$)
- **Support**: $\{0, 1\}$
- **PMF**: $P(X=x) = p^x (1-p)^{1-x}$
- **Mean**: $p$
- **Variance**: $p(1-p) = pq$

### Binomial($n, p$)
- **Support**: $\{0, 1, ..., n\}$
- **PMF**: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
- **Mean**: $np$
- **Variance**: $np(1-p) = npq$

### Geometric($p$) - Trials until first success
- **Support**: $\{1, 2, 3, ...\}$
- **PMF**: $P(X=k) = (1-p)^{k-1} p$
- **Mean**: $\frac{1}{p}$
- **Variance**: $\frac{1-p}{p^2} = \frac{q}{p^2}$

### Poisson($\lambda$)
- **Support**: $\{0, 1, 2, ...\}$
- **PMF**: $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$
- **Mean**: $\lambda$
- **Variance**: $\lambda$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | Probability of success |
| $q$ | $1-p$ (probability of failure) |
| $n$ | Number of trials |
| $\lambda$ | Rate parameter (mean) |
| $k$ | Number of successes |

---

## Important Properties

### Relationships
- Binomial = sum of $n$ i.i.d. Bernoulli($p$)
- Poisson limit of Binomial: $n \to \infty, p \to 0, np = \lambda$
- Geometric = waiting time for first success in Bernoulli trials
- Poisson process: inter-arrival times $\sim$ Exponential

### Memoryless Property
- Geometric (discrete) and Exponential (continuous) are the ONLY memoryless distributions
- $P(X > m+n | X > m) = P(X > n)$

### Sums of Independent
- Binomial + Binomial (same $p$) = Binomial($n_1+n_2, p$)
- Poisson + Poisson = Poisson($\lambda_1 + \lambda_2$)
- NOT for Geometric!

---

## Comparison Tables

| Distribution | Support | Mean | Variance | When to Use |
|--------------|---------|------|----------|-------------|
| Bernoulli | $\{0,1\}$ | $p$ | $pq$ | Single trial |
| Binomial | $\{0,...,n\}$ | $np$ | $npq$ | $n$ fixed trials |
| Geometric | $\{1,2,...\}$ | $1/p$ | $q/p^2$ | Trials until 1st success |
| Poisson | $\{0,1,2,...\}$ | $\lambda$ | $\lambda$ | Events in fixed interval |

---

## GATE Tricks

> [!tip>
> **Bernoulli**: Single trial, success/failure
> **Binomial**: $n$ trials, count successes
> **Geometric**: How many trials until first success?
> **Poisson**: Count events in fixed time/space

> [!tip>
> **Memoryless**: Only Geometric (discrete) and Exponential (continuous)!
> **Poisson**: Mean = Variance = $\lambda$ ⭐
> **Binomial**: Mean = $np$, Var = $npq$
> **Geometric**: Mean = $1/p$, Var = $q/p^2$

> [!tip>
> **Binomial → Poisson**: $n$ large, $p$ small, $np = \lambda$
> **Poisson + Poisson = Poisson**: Sum of independent Poissons

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Binomial | Poisson | Fixed $n$ vs rate $\lambda$ |
| Geometric | Binomial | Wait for 1st success vs count successes in $n$ |
| Geometric | Negative Binomial | 1st success vs $r$-th success |
| Poisson | Exponential | Discrete count vs continuous time |

---

## Common Mistakes

> [!warning>
> **Geometric support**: $\{1,2,3,...\}$ not $\{0,1,2,...\}$!
> **Poisson mean = variance**: Both = $\lambda$
> **Binomial**: Need fixed $n$, independent trials, constant $p$
> **Geometric**: $P(X=k) = q^{k-1}p$, NOT $q^k p$

---

## Memory Tricks

> [!tip>
> **Poisson**: Mean = Variance = $\lambda$ (Lam-b-da)
> **Binomial**: Mean = $np$, Var = $npq$ (p-q-r-s-t)
> **Geometric**: $1/p$ for mean, $q/p^2$ for var

---

## Previous GATE Patterns

- **Identify distribution**: From problem description
- **Compute probability**: Given parameters, find $P(X=k)$
- **Find parameters**: Given mean/variance, find $n,p$ or $\lambda$
- **Sum of Poissons**: $\lambda_1 + \lambda_2$
- **Binomial → Poisson**: Approximation when $n$ large, $p$ small

---

## Revision Summary

```
IMPORTANT DISCRETE DISTRIBUTIONS
├── Bernoulli(p): 0/1, mean=p, var=pq
├── Binomial(n,p): 0..n, mean=np, var=npq
├── Geometric(p): 1,2,..., mean=1/p, var=q/p²
├── Poisson(λ): 0,1,2,..., mean=λ, var=λ
├── Relationships:
│   ├── Binomial = sum of Bernoullis
│   ├── Poisson = limit of Binomial
│   ├── Geometric = waiting for 1st success
│   └── Poisson process ↔ Exponential
├── Memoryless: Geometric only (discrete)
└── Key: Poisson mean=var, Binomial np/npq, Geom 1/p, q/p²
```

---

## Related Notes

- [[24 Bernoulli Distribution]]
- [[25 Binomial Distribution]]
- [[26 Geometric Distribution]]
- [[27 Poisson Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #discrete-distributions #revision