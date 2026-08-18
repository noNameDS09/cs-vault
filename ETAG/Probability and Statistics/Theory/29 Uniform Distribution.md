---
tags: [probability, gate-da, uniform, continuous-distribution, revision]
---

# 29 Uniform Distribution

> [!note] All outcomes in an interval are equally likely.

---

## Overview

The Uniform distribution assigns equal probability density to all points in an interval [a, b]. It's the simplest continuous distribution.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Bounds** | $a$ (minimum), $b$ (maximum) |
| **Equal Likelihood** | All values in [a, b] equally likely |
| **Parameters** | $a$ (lower), $b$ (upper) |

---

## Formulae

### PDF
$$f(x) = \frac{1}{b-a}, \quad a \leq x \leq b$$

### CDF
$$F(x) = \begin{cases}
0 & x < a \\
\frac{x-a}{b-a} & a \leq x \leq b \\
1 & x > b
\end{cases}$$

### Mean
$$E[X] = \frac{a+b}{2} \quad \text{(midpoint)}$$

### Variance
$$Var(X) = \frac{(b-a)^2}{12}$$

### MGF
$$M(t) = \frac{e^{tb} - e^{ta}}{t(b-a)}, \quad t \neq 0$$

### Standard Uniform
$$X \sim Uniform(0,1): \quad f(x) = 1, \quad 0 \leq x \leq 1$$
$$E[X] = \frac{1}{2}, \quad Var(X) = \frac{1}{12}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $a$ | Lower bound (minimum) |
| $b$ | Upper bound (maximum) |
| $b-a$ | Range |

---

## Important Properties

### Symmetry
- Symmetric about midpoint $\frac{a+b}{2}$
- Skewness = 0

### Linear Transformation
If $X \sim Uniform(a,b)$, then $Y = cX + d \sim Uniform(ca+d, cb+d)$

### Standard Uniform as Building Block
If $U \sim Uniform(0,1)$, then $X = a + (b-a)U \sim Uniform(a,b)$

### Sum of Independent Uniforms
Sum of $n$ i.i.d. $Uniform(0,1)$ = Irwin-Hall distribution

---

## Mathematical Intuition

**Equal Likelihood**: A "fair" continuous distribution. Every point in [a,b] is equally likely.

**Area = Probability**: Rectangle with width $(b-a)$ and height $1/(b-a)$. Total area = 1.

---

## Algorithms / Problem-Solving

### Uniform Problems
```
1. Identify a and b from problem
2. PDF = 1/(b-a) on [a,b]
3. P(X ≤ x) = (x-a)/(b-a) for a ≤ x ≤ b
4. Mean = (a+b)/2, Var = (b-a)²/12
5. Standardize: U = (X-a)/(b-a) ~ Uniform(0,1)
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Uniform**: All outcomes equally likely in [a,b]
> **Mean = (a+b)/2** (midpoint)
> **Variance = (b-a)²/12**
> **P(X ≤ x) = (x-a)/(b-a)**
> **Standard U(0,1)**: mean=1/2, var=1/12

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Uniform | Normal | Flat vs bell-shaped |
| Continuous | Discrete Uniform | Interval vs finite set |
| PDF | CDF | 1/(b-a) vs (x-a)/(b-a) |

---

## Common Mistakes

> [!warning>
> **PDF outside [a,b]**: f(x) = 0 for x < a or x > b!
> **PDF height**: 1/(b-a), not 1!
> **P(X=x)**: Always 0 for continuous!

---

## Memory Tricks

> [!tip>
> **Uniform** = "Uniform" = all equal
> **Mean** = midpoint = (a+b)/2
> **Variance** = (b-a)²/12

---

## Previous GATE Patterns

- **P(a < X < b)**: Simple ratio of lengths
- **Mean/Variance**: Given a, b
- **Standard Uniform**: U(0,1) properties
- **Transformation**: a + (b-a)U

---

## Revision Summary

```
UNIFORM DISTRIBUTION
├── f(x) = 1/(b-a) for a ≤ x ≤ b
├── F(x) = (x-a)/(b-a) for a ≤ x ≤ b
├── Mean = (a+b)/2 (midpoint)
├── Variance = (b-a)²/12
├── P(X ≤ x) = (x-a)/(b-a)
├── U(0,1): mean=1/2, var=1/12
├── X = a + (b-a)U transforms U(0,1) to U(a,b)
└── Key: Flat PDF, linear CDF, simple formulas!
```

---

## Related Notes

- [[28 Important Continuous Distributions]]
- [[30 Exponential Distribution]]
- [[31 Normal Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #uniform #continuous-distribution #revision