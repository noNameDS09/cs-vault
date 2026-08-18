---
tags: [probability, gate-da, continuous-rv, revision]
---

# 10 Continuous Random Variables

> [!note] Continuous RVs take uncountable values. Described by Probability Density Function (PDF).

---

## Overview

A continuous random variable takes values in an uncountable set (typically intervals of real numbers). The probability of taking any specific value is zero. Probabilities are computed by integrating the PDF over intervals.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Continuous RV** | Takes uncountable values (intervals) |
| **PDF** | $f(x) \geq 0$, probability density |
| **Support** | $\{x: f(x) > 0\}$ |
| **Mode** | $x$ maximizing $f(x)$ |

---

## Formulae

### PDF Properties
$$f(x) \geq 0$$
$$\int_{-\infty}^{\infty} f(x) dx = 1$$

### Probability over Interval
$$P(a \leq X \leq b) = \int_a^b f(x) dx$$
$$P(X = x) = 0 \quad \text{for any single } x$$

### Expectation
$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
$$E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x) dx$$

### Variance
$$Var(X) = E[X^2] - (E[X])^2$$
$$E[X^2] = \int_{-\infty}^{\infty} x^2 f(x) dx$$

### CDF
$$F(x) = P(X \leq x) = \int_{-\infty}^x f(t) dt$$
$$f(x) = \frac{d}{dx} F(x) \quad \text{(where differentiable)}$$

### Quantiles
$p$-th quantile $q_p$: $F(q_p) = p$
Median = $q_{0.5}$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $f(x)$ | Probability density function |
| $F(x)$ | Cumulative distribution function |
| $x$ | Real value |
| $\mu$ | $E[X]$ |

---

## Important Properties

### Linearity of Expectation (Always!)
$$E[aX + bY + c] = aE[X] + bE[Y] + c$$

### Sum of Independent Continuous RVs
If $X \perp Y$:
- $f_{X+Y}(z) = \int f_X(x) f_Y(z-x) dx$ (Convolution)
- $E[X+Y] = E[X] + E[Y]$
- $Var(X+Y) = Var(X) + Var(Y)$

### Transformation $Y = g(X)$ (Monotonic)
$$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$$

### Uniform Distribution (Reference)
$$X \sim Uniform(a,b): \quad f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$
$$E[X] = \frac{a+b}{2}, \quad Var(X) = \frac{(b-a)^2}{12}$$

---

## Mathematical Intuition

**PDF = Density**: $f(x)dx$ ≈ probability in tiny interval $[x, x+dx]$. Area under curve = probability.

**CDF = Accumulated Area**: $F(x)$ = area under PDF from $-\infty$ to $x$. Smooth, non-decreasing.

**$P(X=x)=0$**: Because area of a point is zero. Only intervals have non-zero probability!

---

## Algorithms / Problem-Solving

### Continuous RV Analysis
```
1. Identify support (where f(x) > 0)
2. Verify ∫ f(x) dx = 1 (find constant if needed)
4. Compute E[X] = ∫ x f(x) dx
5. Compute E[X²] = ∫ x² f(x) dx
6. Var(X) = E[X²] - (E[X])²
7. CDF: F(x) = ∫_{-∞}^x f(t) dt
8. Probabilities: P(a ≤ X ≤ b) = ∫_a^b f(x) dx
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Property | Continuous | Discrete |
|----------|------------|----------|
| $P(X=x)$ | 0 | Can be > 0 |
| Probability | Integrate PDF | Sum PMF |
| CDF | Continuous, smooth | Step function |
| Mode | Max of $f(x)$ | Max of $p_i$ |

---

## GATE Tricks

> [!tip]
> **$P(X=x) = 0$ always for continuous!** Only $P(a \leq X \leq b)$ matters.

> [!tip]
> **PDF value $f(x)$ can be > 1**: It's density, not probability!

> [!tip]
> **Find constant $c$**: If $f(x) = c \cdot g(x)$, use $\int f = 1$ to find $c$.

> [!tip]
> **CDF derivative**: $f(x) = F'(x)$ where differentiable.

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $f(x)$ | $P(X=x)$ | Density vs probability (0 for continuous!) |
| $f(x)$ | $F(x)$ | Derivative vs integral |
| $E[X]$ | $E[X^2]$ | Mean vs mean of squares |

---

## Common Mistakes

> [!warning]
> **Treating $f(x)$ as probability**: $f(x)$ is density, can exceed 1!

> [!warning]
> **$P(X=x) = 0$**: Don't try to compute it!

> [!warning]
> **Forgetting absolute value in transformation**: $|d/dy g^{-1}(y)|$!

> [!warning>
> **Wrong limits**: Use support of $X$, not $[-\infty, \infty]$ if not needed.

---

## Memory Tricks

> [!tip]
> **PDF** = **P**robability **D**ensity **F**unction - density, not mass
> **Continuous** = **Con**tinuous = unbroken, integrate!
> **$P(X=x)=0$**: Point has no area!

---

## Previous GATE Patterns

- **Find normalizing constant**: Given $f(x) = c \cdot g(x)$, find $c$
- **Compute expectation/variance**: Integrate $x f(x)$ and $x^2 f(x)$
- **CDF calculation**: $F(x) = \int_{-\infty}^x f(t) dt$
- **Transformation**: Find PDF of $Y = aX + b$ or $Y = X^2$

---

## Revision Summary

```
CONTINUOUS RANDOM VARIABLES
├── PDF: f(x) ≥ 0, ∫ f(x) dx = 1
├── P(a ≤ X ≤ b) = ∫_a^b f(x) dx
├── P(X=x) = 0 for any single x
├── E[X] = ∫ x f(x) dx
├── E[X²] = ∫ x² f(x) dx
├── Var(X) = E[X²] - μ²
├── CDF: F(x) = ∫_{-∞}^x f(t) dt
├── Transformation: f_Y(y) = f_X(g⁻¹(y)) |d/dy g⁻¹(y)|
└── Key: Integrate! f(x) is density, not probability.
```

---

## Related Notes

- [[08 Random Variables]]
- [[12 Probability Density Function]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]
- [[29 Uniform Distribution]]
- [[30 Exponential Distribution]]
- [[31 Normal Distribution]]

---

#probability #gate-da #continuous-rv #revision