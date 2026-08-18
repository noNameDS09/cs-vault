---
tags: [probability, gate-da, exponential, continuous-distribution, revision]
---

# 30 Exponential Distribution

> [!note] Models time between events in a Poisson process. The only continuous memoryless distribution.

---

## Overview

The Exponential distribution models the time between events in a Poisson process. It's the only continuous distribution with the memoryless property.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Rate $\lambda$** | Average events per unit time |
| **X** | Time until next event |
| **Support** | $[0, \infty)$ |

---

## Formulae

### PDF
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

### CDF
$$F(x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

### Survival Function
$$P(X > x) = e^{-\lambda x}$$

### Mean
$$E[X] = \frac{1}{\lambda}$$

### Variance
$$Var(X) = \frac{1}{\lambda^2}$$

### MGF
$$M(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda$$

### Memoryless Property
$$P(X > s + t | X > s) = P(X > t) = e^{-\lambda t}$$
**Only continuous memoryless distribution!**

### Hazard Rate
$$h(x) = \lambda \quad \text{(constant)}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\lambda$ | Rate parameter (events per unit time) |
| $x$ | Time |
| $1/\lambda$ | Mean time between events |

---

## Important Properties

### Memoryless Property ⭐
$$P(X > s + t | X > s) = P(X > t)$$
**Only continuous distribution with this property!**

### Poisson Process Connection
- Events occur at rate $\lambda$
- Inter-arrival times $\sim$ Exponential($\lambda$)
- Number of events in time $t \sim$ Poisson($\lambda t$)

### Sum of Independent Exponentials
Sum of $n$ i.i.d. Exponential($\lambda$) = Gamma($n, \lambda$)
- Erlang distribution if $n$ is integer

### Minimum of Independent Exponentials
If $X_i \sim \text{Exp}(\lambda_i)$ independent:
$$\min(X_1, ..., X_n) \sim \text{Exp}(\lambda_1 + ... + \lambda_n)$$

### Scaling
If $X \sim \text{Exp}(\lambda)$, then $cX \sim \text{Exp}(\lambda/c)$

---

## Mathematical Intuition

**Time Between Events**: In a Poisson process with rate $\lambda$, the time until the next event is Exponential($\lambda$).

**Memoryless**: "The process has no memory" - time already waited doesn't affect future waiting time.

**Constant Hazard**: Instantaneous failure rate is constant $\lambda$.

---

## Algorithms / Problem-Solving

### Exponential Problems
```
1. Identify: "time until event", "waiting time", "lifetime"
2. Identify λ (rate)
3. Mean = 1/λ, Var = 1/λ²
4. P(X > x) = e^(-λx)
5. Use memoryless property when given conditional
6. Poisson connection: arrivals ~ Poisson, gaps ~ Exponential
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Exponential**: Time between events in Poisson process
> **Mean = 1/λ**, **Var = 1/λ²**
> **P(X > x) = e^(-λx)**
> **Memoryless**: P(X > s+t | X > s) = P(X > t)
> **Poisson process**: arrivals ~ Poisson(λt), gaps ~ Exp(λ)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Exponential | Poisson | Continuous time vs discrete count |
| Exponential | Geometric | Continuous vs discrete memoryless |
| Rate λ | Mean 1/λ | Rate vs mean time |

---

## Common Mistakes

> [!warning>
> **Mean = 1/λ, NOT λ!**
> **Var = 1/λ², NOT λ!**
> **P(X > x) = e^(-λx), NOT e^(-x/λ)!**
> **Only continuous memoryless distribution**

---

## Memory Tricks

> [!tip>
> **Exponential** = **Exp**onential = **Exp**onent = e^(-λx)
> **Mean = 1/λ**: "1 over lambda"
> **Memoryless**: "No memory of past waiting"
> **Poisson arrivals → Exponential gaps**

---

## Previous GATE Patterns

- **P(X > x)**: Use e^(-λx) directly
- **Memoryless**: P(X > s+t | X > s) = P(X > t)
- **Given mean, find λ**: λ = 1/mean
- **Poisson process**: Inter-arrival ~ Exp(λ)
- **Minimum of exponentials**: Sum of rates

---

## Revision Summary

```
EXPONENTIAL DISTRIBUTION
├── f(x) = λ e^(-λx), x ≥ 0
├── F(x) = 1 - e^(-λx)
├── P(X > x) = e^(-λx)
├── Mean = 1/λ
├── Variance = 1/λ²
├── Memoryless: P(X>s+t|X>s) = P(X>t) ⭐ ONLY continuous!
├── Poisson process: gaps ~ Exp(λ), arrivals ~ Poisson(λt)
├── Min of exponentials: sum of rates
└── Key: Mean = 1/λ, Var = 1/λ², Memoryless!
```

---

## Related Notes

- [[28 Important Continuous Distributions]]
- [[27 Poisson Distribution]]
- [[26 Geometric Distribution]] (discrete analog)
- [[33 Central Limit Theorem]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #exponential #continuous-distribution #revision