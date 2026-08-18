---
tags: [probability, gate-da, pmf, revision]
---

# 11 Probability Mass Function (PMF)

> [!note] PMF gives the probability that a discrete random variable takes a specific value.

---

## Overview

The Probability Mass Function (PMF) completely describes a discrete random variable by assigning a probability to each possible value. It's the fundamental tool for working with discrete distributions.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **PMF** | $p_X(x) = P(X = x)$ for all $x$ |
| **Support** | $\{x: p_X(x) > 0\}$ |
| **Normalization** | $\sum_x p_X(x) = 1$ |
| **Non-negativity** | $p_X(x) \geq 0$ |

---

## Formulae

### PMF Definition
$$p_X(x) = P(X = x)$$

### Properties
1. $p_X(x) \geq 0$ for all $x$
2. $\sum_{x \in \mathcal{X}} p_X(x) = 1$
3. $P(X \in A) = \sum_{x \in A} p_X(x)$

### Expectation via PMF
$$E[g(X)] = \sum_x g(x) p_X(x)$$

### Variance via PMF
$$E[X] = \sum_x x p_X(x)$$
$$E[X^2] = \sum_x x^2 p_X(x)$$
$$Var(X) = E[X^2] - (E[X])^2$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p_X(x)$ | PMF of $X$ |
| $\mathcal{X}$ | Support of $X$ |
| $x$ | Possible value of $X$ |

---

## Important Properties

### Uniqueness
PMF uniquely determines the distribution of a discrete RV.

### Transformation
If $Y = g(X)$:
$$p_Y(y) = \sum_{x: g(x)=y} p_X(x)$$

### Joint PMF (Multiple RVs)
$$p_{X,Y}(x,y) = P(X=x, Y=y)$$

### Conditional PMF
$$p_{X|Y}(x|y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}, \quad p_Y(y) > 0$$

---

## Mathematical Intuition

**PMF = Mass Points**: Imagine physical masses $p_i$ placed at locations $x_i$. The PMF tells you exactly how much "probability mass" is at each point.

**Sum = 1**: Total probability mass is 1 (conservation of probability).

---

## Algorithms / Problem-Solving

### Working with PMF
```
1. List all values in support
2. Assign probabilities p_i
3. Check Σ p_i = 1
4. Compute E[X] = Σ x_i p_i
5. Compute E[X²] = Σ x_i² p_i
6. Var = E[X²] - (E[X])²
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Function | Discrete | Continuous |
|----------|----------|------------|
| **PMF** | $p(x) = P(X=x)$ | N/A |
| **PDF** | N/A | $f(x)$ (density) |
| **CDF** | $F(x) = \sum_{x_i \leq x} p_i$ | $F(x) = \int_{-\infty}^x f(t) dt$ |

---

## GATE Tricks

> [!tip]
> **PMF table often has missing value**: Use $\sum p_i = 1$ to find it!

> [!tip]
> **E[X] from PMF**: Just weighted average $\sum x_i p_i$

> [!tip]
> **Common GATE**: PMF defined piecewise, find constant $c$ using $\sum p_i = 1$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| PMF | CDF | Point prob vs cumulative |
| PMF | PDF | Mass vs density |
| $p_X(x)$ | $p_Y(y)$ | Different variables |

---

## Common Mistakes

> [!warning]
> **Forgetting normalization**: $\sum p_i = 1$ must hold!

> [!warning]
> **Negative probabilities**: PMF cannot be negative!

> [!warning>
> **Using PMF for continuous RV**: Continuous RVs don't have PMF!

---

## Memory Tricks

> [!tip]
> **PMF** = **P**robability **M**ass **F**unction
> **Mass** = concentrated at points (like atoms)
> **Discrete** = **Dis**crete = separate masses

---

## Previous GATE Patterns

- **Find missing probability**: $\sum p_i = 1$
- **Compute mean/variance**: From PMF table
- **Find constant**: $p(x) = c \cdot f(x)$, solve for $c$
- **Transformation**: PMF of $Y = g(X)$

---

## Revision Summary

```
PROBABILITY MASS FUNCTION (PMF)
├── p_X(x) = P(X = x)
├── p_X(x) ≥ 0
├── Σ p_X(x) = 1
├── E[g(X)] = Σ g(x) p_X(x)
├── E[X] = Σ x p_X(x)
├── Var(X) = E[X²] - (E[X])²
└── Key: Discrete only! Sum, don't integrate.
```

---

## Related Notes

- [[09 Discrete Random Variables]]
- [[12 Probability Density Function]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]

---

#probability #gate-da #pmf #revision