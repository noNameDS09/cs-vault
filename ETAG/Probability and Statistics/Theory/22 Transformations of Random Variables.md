---
tags: [probability, gate-da, transformations, revision]
---

# 22 Transformations of Random Variables

> [!note] Transformations find the distribution of Y = g(X) from the distribution of X.

---

## Overview

Transformations allow us to find the distribution of a function of a random variable. Methods differ for monotonic vs non-monotonic transformations and discrete vs continuous RVs.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Transformation** | $Y = g(X)$ where $X$ is a known RV |
| **Monotonic** | Strictly increasing or decreasing |
| **CDF Method** | $F_Y(y) = P(g(X) \leq y)$ |
| **PDF/PMF Method** | Direct formula for monotonic transformations |

---

## Formulae

### CDF Method (Universal)
$$F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$$
Then differentiate: $f_Y(y) = \frac{d}{dy} F_Y(y)$

### Monotonic Transformation (Continuous)
If $g$ is strictly monotonic and differentiable:
$$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$$

### Linear Transformation $Y = aX + b$
$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$$
$$E[Y] = aE[X] + b, \quad Var(Y) = a^2 Var(X)$$

### $Y = X^2$ (Non-monotonic, $X$ continuous)
$$f_Y(y) = \frac{1}{2\sqrt{y}} \left[ f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right], \quad y > 0$$

### Sum of Independent RVs
$$f_{X+Y}(z) = \int f_X(x) f_Y(z-x) dx \quad \text{(Convolution)}$$

### Discrete Transformation
$$p_Y(y) = \sum_{x: g(x)=y} p_X(x)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $g$ | Transformation function |
| $g^{-1}$ | Inverse function |
| $Y$ | Transformed variable |

---

## Important Properties

### Support Transformation
If $X$ has support $\mathcal{X}$, then $Y$ has support $g(\mathcal{X})$.

### Expectation via Transformation
$$E[g(X)] = \sum g(x) p_X(x) \quad \text{or} \quad \int g(x) f_X(x) dx$$
(Don't need to find distribution of $g(X)$!)

---

## Mathematical Intuition

**CDF Method**: $P(Y \leq y) = P(g(X) \leq y) = P(X \in g^{-1}((-\infty, y]))$. Find the set of $X$ values that map to $Y \leq y$.

**Monotonic Formula**: The density stretches/compresses by the derivative factor. $\frac{dy}{dx}$ gives the stretching.

**Convolution**: Sum of independent = integral of product = sliding one density past another.

---

## Algorithms / Problem-Solving

### CDF Method (Always Works)
```
1. Write F_Y(y) = P(g(X) ≤ y)
2. Express {g(X) ≤ y} in terms of X
3. Compute probability using X's CDF/PDF
4. Differentiate to get f_Y(y)
```

### Monotonic Transformation
```
1. Check if g is strictly monotonic
2. Find inverse x = g⁻¹(y)
3. Compute derivative dx/dy
4. Apply formula: f_Y(y) = f_X(g⁻¹(y)) |dx/dy|
```

### Non-monotonic (e.g., Y = X²)
```
1. Find all x such that g(x) = y
2. For each branch, apply monotonic formula
3. Sum contributions from all branches
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Method | When to Use |
|--------|-------------|
| CDF Method | Always works, any g |
| Monotonic Formula | g strictly monotonic, differentiable |
| Convolution | Sum of independent RVs |
| MGF | Sum of independent, known MGFs |

---

## GATE Tricks

> [!tip>
> **Expectation**: Use LOTUS! E[g(X)] = ∫ g(x) f(x) dx - DON'T find distribution!
> **Linear**: Y = aX + b → f_Y(y) = 1/|a| f_X((y-b)/a)
> **Y = X²**: f_Y(y) = 1/(2√y) [f(√y) + f(-√y)]
> **Sum of independent**: Convolution or MGF product

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| CDF Method | Monotonic Formula | Universal vs restricted |
| Transformation | Convolution | Single RV vs sum of RVs |
| PDF of Y | CDF of Y | Derivative vs integral |

---

## Common Mistakes

> [!warning>
> **Forgetting absolute value**: |d/dy g⁻¹(y)|
> **Forgetting 1/|a| in linear transformation**
> **Using monotonic formula for non-monotonic g**
> **Finding distribution when only expectation needed**: Use LOTUS!

---

## Memory Tricks

> [!tip>
> **CDF Method**: "Cumulative" = P(g(X) ≤ y) = P(X ∈ g⁻¹(...))
> **Monotonic**: f_Y(y) = f_X(g⁻¹(y)) |d/dy g⁻¹(y)|
> **Linear**: "Stretch by |a|, shift by b"

---

## Previous GATE Patterns

- **Y = aX + b**: Find PDF/CDF
- **Y = X²**: Given X's distribution, find Y's
- **Y = e^X or ln X**: Log-normal, etc.
- **Sum of independent**: Convolution or MGF
- **Expectation of function**: Use LOTUS directly

---

## Revision Summary

```
TRANSFORMATIONS
├── CDF Method: F_Y(y) = P(g(X) ≤ y) (always works)
├── Monotonic: f_Y(y) = f_X(g⁻¹(y)) |d/dy g⁻¹(y)|
├── Linear: f_Y(y) = 1/|a| f_X((y-b)/a)
├── Y = X²: f_Y(y) = 1/(2√y) [f(√y) + f(-√y)]
├── Sum of independent: Convolution
├── Expectation: Use LOTUS directly!
└── Key: LOTUS for expectation, CDF for distribution!
```

---

## Related Notes

- [[08 Random Variables]]
- [[10 Continuous Random Variables]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[33 Central Limit Theorem]]

---

#probability #gate-da #transformations #revision