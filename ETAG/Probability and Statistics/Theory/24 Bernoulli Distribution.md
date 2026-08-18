---
tags: [probability, gate-da, bernoulli, discrete-distribution, revision]
---

# 24 Bernoulli Distribution

> [!note] Single trial with two outcomes: success (1) with probability p, failure (0) with probability 1-p.

---

## Overview

The Bernoulli distribution is the simplest discrete distribution, modeling a single binary trial. It's the building block for the Binomial distribution.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Trial** | Single experiment with two outcomes |
| **Success** | Outcome coded as 1 |
| **Failure** | Outcome coded as 0 |
| **Parameter p** | Probability of success |

---

## Formulae

### PMF
$$P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$$
Alternatively: $P(X=1) = p, \quad P(X=0) = 1-p$

### CDF
$$F(x) = \begin{cases}
0 & x < 0 \\
1-p & 0 \leq x < 1 \\
1 & x \geq 1
\end{cases}$$

### Mean
$$E[X] = p$$

### Variance
$$Var(X) = p(1-p) = pq$$

### MGF
$$M(t) = 1-p + pe^t = q + pe^t$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | Probability of success |
| $q = 1-p$ | Probability of failure |
| $X$ | Indicator of success (1) or failure (0) |

---

## Important Properties

### Indicator Variable
$X = I_A$ where $A$ is the event "success occurs"
- $E[X] = P(A) = p$
- $Var(X) = P(A)(1-P(A)) = p(1-p)$

### Building Block
Sum of $n$ i.i.d. Bernoulli($p$) = Binomial($n, p$)

### MGF
$$M(t) = q + pe^t$$
- $M'(0) = p$
- $M''(0) = p$

---

## Mathematical Intuition

**Single Coin Flip**: Heads=1 (prob p), Tails=0 (prob 1-p). The simplest possible random experiment.

**Indicator**: $X = 1$ if event $A$ occurs, $0$ otherwise. $E[X] = P(A)$.

---

## Algorithms / Problem-Solving

### Bernoulli Problems
```
1. Identify if problem involves single binary trial
2. Identify p (probability of success)
3. X = 1 for success, 0 for failure
4. E[X] = p, Var(X) = p(1-p)
5. For sum of n: use Binomial(n, p)
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Bernoulli = Single trial**
> **Mean = p, Variance = p(1-p)**
> **Sum of n i.i.d. Bernoulli = Binomial(n, p)**
> **Indicator variable: E[I_A] = P(A)**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Bernoulli | Binomial | 1 trial vs n trials |
| p | q | Success prob vs failure prob |
| X=1 | X=0 | Success vs Failure |

---

## Common Mistakes

> [!warning>
> **Confusing n=1 Binomial with Bernoulli**: They're the same, but notation differs!
> **Forgetting q = 1-p**: Often used in variance formula

---

## Memory Tricks

> [!tip>
> **Bernoulli** = **Bern**oulli = **Bern** = one trial (like "one" in French?)
> **p for success, q for failure**
> **Mean = p, Var = pq**

---

## Previous GATE Patterns

- **Identify as Bernoulli**: Single trial with two outcomes
- **Mean/Variance**: Given p, compute
- **Sum of indicators**: Convert to Binomial

---

## Revision Summary

```
BERNOULLI DISTRIBUTION
├── Single trial, two outcomes
├── X = 1 (success, prob p), X = 0 (failure, prob q=1-p)
├── PMF: P(X=1)=p, P(X=0)=q
├── Mean = p
├── Variance = pq
├── MGF = q + pe^t
├── Sum of n i.i.d. = Binomial(n, p)
└── Indicator: E[I_A] = P(A)
```

---

## Related Notes

- [[25 Binomial Distribution]]
- [[23 Important Discrete Distributions]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #bernoulli #discrete-distribution #revision