---
tags: [probability, gate-da, cdf, revision]
---

# 13 Cumulative Distribution Function (CDF)

> [!note] CDF gives the probability that a random variable is less than or equal to a given value.

---

## Overview

The Cumulative Distribution Function (CDF) completely describes a random variable's distribution, whether discrete or continuous. It's the universal function for computing probabilities of intervals.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **CDF** | $F_X(x) = P(X \leq x)$ |
| **Support** | Domain where $F$ is strictly increasing |
| **Quantiles** | $q_p = F^{-1}(p)$ |

---

## Formulae

### Definition
$$F_X(x) = P(X \leq x)$$

### Properties (Universal)
1. **Non-decreasing**: $x_1 < x_2 \implies F(x_1) \leq F(x_2)$
2. **Limits**: $F(-\infty) = 0$, $F(\infty) = 1$
3. **Right-continuous**: $\lim_{h \downarrow 0} F(x+h) = F(x)$

### Discrete RV
$$F_X(x) = \sum_{x_i \leq x} p_X(x_i)$$
- Step function with jumps of size $p_i$ at $x_i$

### Continuous RV
$$F_X(x) = \int_{-\infty}^x f_X(t) dt$$
$$f_X(x) = \frac{d}{dx} F_X(x) \quad \text{(where differentiable)}$$

### Probabilities from CDF
$$P(a < X \leq b) = F(b) - F(a)$$
$$P(a \leq X \leq b) = F(b) - F(a) + P(X=a)$$
$$P(X > a) = 1 - F(a)$$
$$P(X \geq a) = 1 - F(a) + P(X=a)$$

### Quantiles
$p$-th quantile: $q_p = \inf\{x: F(x) \geq p\}$
- Median: $q_{0.5}$
- Quartiles: $q_{0.25}, q_{0.75}$

### Survival Function
$$S(x) = P(X > x) = 1 - F(x)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $F_X(x)$ | CDF of $X$ |
| $x$ | Real value |
| $p$ | Probability level (0 to 1) |
| $q_p$ | $p$-th quantile |

---

## Important Properties

### Universal Properties (Both Discrete & Continuous)
- $0 \leq F(x) \leq 1$
- $F$ is non-decreasing
- Right-continuous
- $F(-\infty) = 0$, $F(\infty) = 1$

### Discrete: Step function
- Jumps at points in support
- Jump size = $p_X(x_i)$

### Continuous: Smooth
- $F$ is continuous and differentiable where $f(x) > 0$
- $f(x) = F'(x)$

### Inverse CDF (Quantile Function)
$$F^{-1}(p) = \inf\{x: F(x) \geq p\}$$
- For continuous strictly increasing: $F^{-1}(p)$ is the unique $x$ with $F(x)=p$

---

## Mathematical Intuition

**CDF = Accumulated Probability**: $F(x)$ = how much probability mass is to the left of $x$.

**Universal**: Works for ANY random variable - discrete, continuous, or mixed!

**Complement**: $P(X > x) = 1 - F(x)$ (survival function).

---

## Algorithms / Problem-Solving

### Computing Probabilities
```
Given CDF F(x):
- P(X ≤ x) = F(x)
- P(X > x) = 1 - F(x)
- P(a < X ≤ b) = F(b) - F(a)
- P(X = x) = F(x) - F(x⁻) [jump at x]
```

### Finding Quantiles
```
Given CDF F(x) and probability p:
1. If continuous and strictly increasing: solve F(x) = p
2. If discrete: find smallest x with F(x) ≥ p
3. If mixed: use infimum definition
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Property | Discrete | Continuous |
|----------|----------|------------|
| **Shape** | Step function | Smooth curve |
| **Derivative** | Not defined at jumps | $f(x) = F'(x)$ |
| **Inverse** | Generalized inverse | Regular inverse |
| **Jumps** | At support points | None |

---

## GATE Tricks

> [!tip]
> **CDF works for BOTH discrete and continuous!** Universal tool.

> [!tip>
> **$P(a < X ≤ b) = F(b) - F(a)$** works universally!

> [!tip>
> **$P(X > x) = 1 - F(x)$** (survival function)

> [!tip>
> **$P(X = x) = F(x) - F(x⁻)$** = jump size at $x$ (0 for continuous)

> [!tip>
> **Quantile**: For continuous, solve $F(x) = p$. For discrete, smallest $x$ with $F(x) \geq p$.

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $F(x)$ | $f(x)$ | Cumulative vs density |
| $P(X < x)$ | $P(X \leq x)$ | $F(x) - P(X=x)$ vs $F(x)$ |
| $P(X > x)$ | $1 - F(x)$ | $P(X > x) = 1 - F(x)$ for continuous, $= 1 - F(x)$ for discrete? No: $P(X > x) = 1 - P(X \leq x) = 1 - F(x)$ always! |

---

## Common Mistakes

> [!warning]
> **$P(X < x) \neq F(x)$ for discrete**: $P(X < x) = F(x) - P(X=x)$

> [!warning>
> **For continuous**: $P(X < x) = P(X \leq x) = F(x)$

> [!warning>
> **$P(X \geq a) = 1 - F(a) + P(X=a)$**: careful with discrete!

> [!warning>
> **Quantile for discrete**: Use infimum, not simple equation solving.

---

## Memory Tricks

> [!tip]
> **CDF** = **C**umulative **D**istribution **F**unction = accumulated probability
> **F(x)** = **F**or all values **x** or less
> **Survival** = **S** = 1 - F = what **S**urvives past x

---

## Previous GATE Patterns

- **Given CDF, find probabilities**: $P(a < X \leq b) = F(b) - F(a)$
- **Find CDF from PDF/PMF**: Integrate or sum
- **Find median/quantiles**: Solve $F(x) = 0.5$ or find smallest $x$ with $F(x) \geq 0.5$
- **Jump size**: $P(X=x) = F(x) - F(x⁻)$

---

## Revision Summary

```
CUMULATIVE DISTRIBUTION FUNCTION (CDF)
├── F(x) = P(X ≤ x)
├── Universal: works for ALL random variables
├── Properties: 0 ≤ F ≤ 1, non-decreasing, right-continuous
├── Limits: F(-∞)=0, F(∞)=1
├── Discrete: Step function, jumps = p_i
├── Continuous: Smooth, f(x) = F'(x)
├── Probabilities: P(a < X ≤ b) = F(b) - F(a)
├── Survival: P(X > x) = 1 - F(x)
├── Quantiles: q_p = inf{x: F(x) ≥ p}
└── Key: Universal, works for everything!
```

---

## Related Notes

- [[11 Probability Mass Function]]
- [[12 Probability Density Function]]
- [[09 Discrete Random Variables]]
- [[10 Continuous Random Variables]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #cdf #revision