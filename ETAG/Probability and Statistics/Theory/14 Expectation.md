---
tags: [probability, gate-da, expectation, revision]
---

# 14 Expectation

> [!note] Expectation is the long-run average value of a random variable. The most fundamental summary statistic.

---

## Overview

Expectation (expected value) represents the center of a distribution. It's the weighted average of all possible values, weighted by their probabilities. Linearity of expectation is one of the most powerful tools in probability.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Expectation** | $E[X]$ = long-run average of $X$ |
| **Linearity** | $E[aX + bY] = aE[X] + bE[Y]$ (always!) |
| **Law of Unconscious Statistician** | $E[g(X)]$ computed from distribution of $X$ |

---

## Formulae

### Discrete
$$E[X] = \sum_i x_i P(X = x_i) = \sum_i x_i p_i$$

### Continuous
$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$

### Function of RV (LOTUS)
$$E[g(X)] = \begin{cases}
\sum_x g(x) p(x) & \text{discrete} \\
\int g(x) f(x) dx & \text{continuous}
\end{cases}$$

### Linearity (ALWAYS HOLDS!)
$$E[aX + bY + c] = aE[X] + bE[Y] + c$$
$$E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]$$

### Conditional Expectation
$$E[X|Y=y] = \sum_x x P(X=x|Y=y) \quad \text{or} \quad \int x f_{X|Y}(x|y) dx$$

### Law of Total Expectation
$$E[X] = E[E[X|Y]]$$
$$E[X] = \sum_y E[X|Y=y] P(Y=y) \quad \text{or} \quad \int E[X|Y=y] f_Y(y) dy$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $E[X]$ | Expected value of $X$ |
| $\mu$ | $E[X]$ (population mean) |
| $g(X)$ | Function of $X$ |
| $E[X|Y]$ | Conditional expectation (function of $Y$) |

---

## Important Properties

### Linearity (No Independence Needed!)
$$E[X+Y] = E[X] + E[Y]$$
$$E[aX] = aE[X]$$
$$E[c] = c$$

### Non-negative RV
If $X \geq 0$, then $E[X] \geq 0$

### Jensen's Inequality
For convex $g$: $E[g(X)] \geq g(E[X])$
For concave $g$: $E[g(X)] \leq g(E[X])$

### Indicator Variables
$$I_A = \begin{cases} 1 & A \text{ occurs} \\ 0 & \text{otherwise} \end{cases}$$
$$E[I_A] = P(A)$$
**Powerful trick**: Counting events = sum of indicators

---

## Mathematical Intuition

**Center of Mass**: Distribution as mass on a line. Expectation = balance point.

**Long-run Average**: Repeat experiment many times, average the outcomes.

**Linearity = Superposition**: Expectation of sum = sum of expectations, ALWAYS.

---

## Algorithms / Problem-Solving

### Computing Expectation
```
1. Identify distribution (discrete/continuous)
2. For E[X]: use ∫ x f(x) dx or Σ x p(x)
3. For E[g(X)]: use LOTUS (don't find distribution of g(X)!)
4. Use linearity: E[aX+bY+c] = aE[X]+bE[Y]+c
5. For counts: write as sum of indicators
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Property | Discrete | Continuous |
|----------|----------|------------|
| $E[X]$ | $\sum x p(x)$ | $\int x f(x) dx$ |
| $E[g(X)]$ | $\sum g(x) p(x)$ | $\int g(x) f(x) dx$ |
| Linearity | Same | Same |

---

## GATE Tricks

> [!tip>
> **Linearity ALWAYS works**: $E[X+Y] = E[X] + E[Y]$ even if dependent!

> [!tip>
> **LOTUS**: $E[g(X)]$ from $X$'s distribution directly - don't find $g(X)$'s distribution!

> [!tip>
> **Indicator trick**: Number of events = sum of indicators. E[count] = Σ P(event)

> [!tip>
> **$E[X^2] \neq (E[X])^2$**: Variance is the difference!

> [!tip>
> **Conditional expectation**: $E[X] = E[E[X|Y]]$ - useful for hierarchical models

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $E[X+Y]$ | $E[X]+E[Y]$ | Always equal (linearity) |
| $E[XY]$ | $E[X]E[Y]$ | Equal ONLY if independent |
| $E[X^2]$ | $(E[X])^2$ | Different! Difference = variance |

---

## Common Mistakes

> [!warning>
> **Assuming $E[XY] = E[X]E[Y]$ without independence**: Only true if independent!

> [!warning>
> **Finding distribution of $g(X)$ first**: Use LOTUS directly!

> [!warning>
> **$E[X^2] = (E[X])^2$**: False! That would make variance zero.

---

## Memory Tricks

> [!tip>
> **LOTUS** = **L**aw **o**f **T**he **U**nconscious **S**tatistician
> **Linearity**: Expectation is **linear** - respects addition and scaling
> **Indicator**: "I" for event = 1 if happens, 0 if not. E[I] = P(event)

---

## Previous GATE Patterns

- **Linearity**: $E[aX+bY+c]$ from given $E[X], E[Y]$
- **LOTUS**: $E[X^2], E[1/X], E[e^X]$ from distribution
- **Indicator variables**: Expected number of fixed points, matches, etc.
- **Total expectation**: $E[X] = E[E[X|Y]]$

---

## Revision Summary

```
EXPECTATION
├── Discrete: E[X] = Σ x p(x)
├── Continuous: E[X] = ∫ x f(x) dx
├── LOTUS: E[g(X)] = Σ/∫ g(x) p(x) dx (don't find g(X) distribution!)
├── Linearity: E[aX+bY+c] = aE[X]+bE[Y]+c (ALWAYS!)
├── E[X+Y] = E[X] + E[Y] (always!)
├── E[XY] = E[X]E[Y] (iff independent)
├── E[X²] ≠ (E[X])²
├── Indicators: E[I_A] = P(A)
├── Total Expectation: E[X] = E[E[X|Y]]
└── Key: Linearity is your superpower!
```

---

## Related Notes

- [[15 Variance and Standard Deviation]]
- [[16 Moments]]
- [[17 Covariance and Correlation]]
- [[19 Marginal Distributions]]
- [[20 Conditional Distributions]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #expectation #revision