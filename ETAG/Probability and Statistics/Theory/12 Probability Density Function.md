---
tags: [probability, gate-da, pdf, revision]
---

# 12 Probability Density Function (PDF)

> [!note] PDF gives the probability density of a continuous random variable. Probability is obtained by integrating over intervals.

---

## Overview

The Probability Density Function (PDF) describes a continuous random variable. The probability of the variable falling in an interval is the area under the PDF curve over that interval.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **PDF** | $f_X(x) \geq 0$, $\int_{-\infty}^{\infty} f_X(x) dx = 1$ |
| **Support** | $\{x: f_X(x) > 0\}$ |
| **Mode** | $x$ maximizing $f_X(x)$ |

---

## Formulae

### PDF Properties
$$f_X(x) \geq 0 \quad \forall x$$
$$\int_{-\infty}^{\infty} f_X(x) dx = 1$$

### Probability over Interval
$$P(a \leq X \leq b) = \int_a^b f_X(x) dx$$
$$P(X = x) = 0 \quad \forall x$$

### Expectation
$$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$$
$$E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$$
$$E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) dx$$

### Variance
$$Var(X) = E[X^2] - (E[X])^2$$

### CDF from PDF
$$F_X(x) = \int_{-\infty}^x f_X(t) dt$$
$$f_X(x) = \frac{d}{dx} F_X(x) \quad \text{(where differentiable)}$$

### Transformation $Y = g(X)$ (Monotonic)
$$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$$

### Linear Transformation $Y = aX + b$
$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $f_X(x)$ | PDF of $X$ |
| $F_X(x)$ | CDF of $X$ |
| $x$ | Real value |
| $a, b$ | Constants |

---

## Important Properties

### Uniqueness
PDF uniquely determines the distribution (up to sets of measure zero).

### Normalization
If $f_X(x) = c \cdot g(x)$, find $c$ by: $c = \frac{1}{\int g(x) dx}$

### Joint PDF (Multiple RVs)
$$f_{X,Y}(x,y) \geq 0, \quad \int \int f_{X,Y}(x,y) dx dy = 1$$

### Marginal PDF
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$$

### Conditional PDF
$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}, \quad f_Y(y) > 0$$

---

## Mathematical Intuition

**PDF = Density**: Think of a wire with varying linear density $f(x)$. Total mass = 1. Probability in $[x, x+dx]$ ≈ $f(x)dx$.

**Area = Probability**: The integral computes the area under the curve. Total area = 1.

**$f(x)$ can be > 1**: It's a density, not a probability!

---

## Algorithms / Problem-Solving

### Working with PDF
```
1. Identify support (where f(x) > 0)
2. If unknown constant c: ∫ f(x) dx = 1 → solve for c
3. E[X] = ∫ x f(x) dx
4. E[X²] = ∫ x² f(x) dx
5. Var = E[X²] - (E[X])²
6. CDF: F(x) = ∫_{-∞}^x f(t) dt
7. P(a ≤ X ≤ b) = ∫_a^b f(x) dx
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Function | Discrete | Continuous |
|----------|----------|------------|
| **PMF** | $P(X=x)$ | N/A |
| **PDF** | N/A | $f(x)$ (density) |
| **CDF** | Step function | Smooth |
| **P(X=x)** | > 0 | 0 |

---

## GATE Tricks

> [!tip]
> **$P(X=x) = 0$ always for continuous!** Don't compute it.

> [!tip]
> **PDF value $f(x)$ can be > 1**: It's density, not probability!

> [!tip>
> **Find constant $c$**: If $f(x) = c \cdot g(x)$, use $\int f = 1$ to find $c$.

> [!tip>
> **CDF derivative**: $f(x) = F'(x)$ where differentiable.

> [!tip>
> **$f(x) \propto g(x)$**: Normalize by finding area under $g(x)$.

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $f(x)$ | $P(X=x)$ | Density vs probability (0 for continuous!) |
| $f(x)$ | $F(x)$ | Derivative vs integral |
| PDF | PMF | Density vs mass |

---

## Common Mistakes

> [!warning>
> **Treating $f(x)$ as probability**: $f(x)$ is density, can exceed 1!

> [!warning>
> **$P(X=x) = 0$**: Don't try to compute it!

> [!warning>
> **Forgetting absolute value in transformation**: $|d/dy g^{-1}(y)|$!

> [!warning>
> **Wrong integration limits**: Use support of $X$!

---

## Memory Tricks

> [!tip>
> **PDF** = **P**robability **D**ensity **F**unction
> **Density** = mass per unit length (can exceed 1)
> **Continuous** = **Con**tinuous = integrate!

---

## Previous GATE Patterns

- **Find normalizing constant**: $f(x) = c \cdot g(x)$, find $c$
- **Compute expectation/variance**: Integrate $x f(x)$ and $x^2 f(x)$
- **CDF calculation**: $F(x) = \int_{-\infty}^x f(t) dt$
- **Transformation**: PDF of $Y = aX + b$ or $Y = X^2$

---

## Revision Summary

```
PROBABILITY DENSITY FUNCTION (PDF)
├── f(x) ≥ 0, ∫ f(x) dx = 1
├── P(a ≤ X ≤ b) = ∫_a^b f(x) dx
├── P(X=x) = 0 for any single x
├── E[X] = ∫ x f(x) dx
├── E[X²] = ∫ x² f(x) dx
├── Var(X) = E[X²] - μ²
├── CDF: F(x) = ∫_{-∞}^x f(t) dt
├── Transformation: f_Y(y) = f_X(g⁻¹(y)) |d/dy g⁻¹(y)|
└── Key: f(x) is density, not probability! Integrate to get probability.
```

---

## Related Notes

- [[10 Continuous Random Variables]]
- [[11 Probability Mass Function]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]
- [[22 Transformations of Random Variables]]

---

#probability #gate-da #pdf #revision