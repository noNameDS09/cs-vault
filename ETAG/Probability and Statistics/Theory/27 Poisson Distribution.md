---
tags: [probability, gate-da, poisson, discrete-distribution, revision]
---

# 27 Poisson Distribution

> [!note] Count of events occurring in a fixed interval of time/space, with constant average rate λ.

---

## Overview

The Poisson distribution models the number of events occurring in a fixed interval of time or space, given a constant average rate. It's the limit of Binomial(n,p) as n→∞, p→0, np=λ.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Rate λ** | Average number of events per interval |
| **X** | Number of events in the interval |
| **Support** | {0, 1, 2, ...} |

---

## Formulae

### PMF
$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, ...$$

### Mean
$$E[X] = \lambda$$

### Variance
$$Var(X) = \lambda$$

### **Key**: Mean = Variance = λ

### MGF
$$M(t) = e^{\lambda(e^t - 1)}$$

### Sum of Independent Poissons
If $X \sim Pois(\lambda_1)$, $Y \sim Pois(\lambda_2)$ independent:
$$X + Y \sim Pois(\lambda_1 + \lambda_2)$$

### Poisson Process
Inter-arrival times $\sim$ Exponential($\lambda$)

### Binomial Approximation
Binomial($n, p$) $\approx$ Poisson($\lambda$) when $n$ large, $p$ small, $np = \lambda$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\lambda$ | Rate (mean events per interval) |
| $k$ | Number of events |
| $t$ | Time/space interval |

---

## Important Properties

### Mean = Variance = $\lambda$ ⭐
**Most distinctive feature!**

### Additivity
Sum of independent Poissons = Poisson with summed rates.

### Poisson Process
- Events occur continuously at rate $\lambda$
- Inter-arrival times $\sim$ Exponential($\lambda$)
- Number in interval $t$ $\sim$ Poisson($\lambda t$)

### Binomial Limit
$n \to \infty, p \to 0, np = \lambda \implies Bin(n,p) \to Pois(\lambda)$

### Normal Approximation
For large $\lambda$ (say $\lambda \geq 10$): $Pois(\lambda) \approx N(\lambda, \lambda)$

### Mode
$\lfloor \lambda \rfloor$ (if $\lambda$ not integer) or $\lambda$ and $\lambda-1$ (if integer)

---

## Mathematical Intuition

**Rare Events**: Many trials, each with tiny success probability, but expected total is $\lambda$.

**Random Arrival**: Events arrive randomly at constant average rate $\lambda$.

**Mean = Variance**: Unique among common distributions (exponential also has this property).

---

## Algorithms / Problem-Solving

### Poisson Problems
```
1. Identify: counting events in fixed interval
2. Identify λ (average rate)
3. Check: events independent, constant rate
4. PMF: P(X=k) = e^(-λ) λ^k / k!
5. Mean = Var = λ
5. Sum of Poissons: add λ's
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Poisson**: Events in fixed interval
> **Mean = Variance = λ** ⭐ KEY!
> **Sum of Poissons**: Add λ's
> **Poisson process**: Inter-arrival ~ Exponential(λ)
> **Binomial → Poisson**: n large, p small, np=λ

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Poisson | Binomial | Rate λ vs fixed n |
| Poisson | Geometric | Count in interval vs wait for 1st |
| Poisson | Exponential | Discrete count vs continuous time |

---

## Common Mistakes

> [!warning>
> **Mean = Variance = λ**: Both equal!
> **Confusing λ with n**: Poisson has rate, Binomial has n
> **Using Poisson when events not independent**: Must be independent!
> **Rate changes in interval**: Not Poisson then!

---

## Memory Tricks

> [!tip>
> **Poisson** = **Poi**sson = **Poi**nt process
> **λ** = **Lambda** = rate
> **Mean = Var = λ**: "Lambda equals both!"
> **Poisson + Poisson = Poisson**: Add the lambdas

---

## Previous GATE Patterns

- **Identify**: "Events per hour/minute/page"
- **Given mean, find variance**: Both = λ!
- **Sum of Poissons**: Add λ's
- **P(X=k)**: Compute PMF
- **λt for time t**: If rate λ per unit time, interval t gives λt
- **Poisson process**: Inter-arrival ~ Exponential

---

## Revision Summary

```
POISSON DISTRIBUTION
├── X = events in fixed interval
├── Support: {0, 1, 2, ...}
├── PMF: e^(-λ) λ^k / k!
├── Mean = λ
├── Variance = λ ⭐ MEAN = VARIANCE!
├── MGF: e^{λ(e^t - 1)}
├── Sum of independent: add λ's
├── Poisson process: inter-arrival ~ Exponential(λ)
├── Binomial approx: n large, p small, np=λ
└── Key: Mean = Variance = λ!
```

---

## Related Notes

- [[23 Important Discrete Distributions]]
- [[24 Bernoulli Distribution]]
- [[25 Binomial Distribution]]
- [[26 Geometric Distribution]]
- [[30 Exponential Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #poisson #discrete-distribution #revision