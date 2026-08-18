---
tags: [probability, gate-da, joint-distribution, revision]
---

# 18 Joint Probability Distributions

> [!note] Joint distribution describes the probability of two or more random variables simultaneously.

---

## Overview

Joint distributions capture the relationship between multiple random variables. They are essential for understanding dependence, computing conditional probabilities, and multivariate analysis.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Joint PMF** | $p_{X,Y}(x,y) = P(X=x, Y=y)$ (discrete) |
| **Joint PDF** | $f_{X,Y}(x,y)$ (continuous) |
| **Support** | $\{(x,y): f_{X,Y}(x,y) > 0\}$ |

---

## Formulae

### Discrete Joint PMF
$$p_{X,Y}(x,y) = P(X=x, Y=y)$$
$$p_{X,Y}(x,y) \geq 0$$
$$\sum_x \sum_y p_{X,Y}(x,y) = 1$$

### Continuous Joint PDF
$$f_{X,Y}(x,y) \geq 0$$
$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y) dx dy = 1$$

### Joint CDF
$$F_{X,Y}(x,y) = P(X \leq x, Y \leq y)$$
- Discrete: $F(x,y) = \sum_{u \leq x} \sum_{v \leq y} p(u,v)$
- Continuous: $F(x,y) = \int_{-\infty}^x \int_{-\infty}^y f(u,v) du dv$

### Probabilities from Joint Distribution
$$P((X,Y) \in A) = \begin{cases}
\sum_{(x,y) \in A} p(x,y) & \text{discrete} \\
\int \int_A f(x,y) dx dy & \text{continuous}
\end{cases}$$

### Expectation of Function
$$E[g(X,Y)] = \begin{cases}
\sum_x \sum_y g(x,y) p(x,y) & \text{discrete} \\
\int \int g(x,y) f(x,y) dx dy & \text{continuous}
\end{cases}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p_{X,Y}(x,y)$ | Joint PMF |
| $f_{X,Y}(x,y)$ | Joint PDF |
| $F_{X,Y}(x,y)$ | Joint CDF |

---

## Important Properties

### Independence
$X \perp Y \iff f_{X,Y}(x,y) = f_X(x) f_Y(y)$ for all $x,y$

### Marginal Distributions
- Discrete: $p_X(x) = \sum_y p_{X,Y}(x,y)$
- Continuous: $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$

### Conditional Distributions
$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}, \quad f_X(x) > 0$$

### Expectation of Sum
$$E[X + Y] = E[X] + E[Y]$$
(Always holds, no independence needed!)

### Covariance
$$Cov(X,Y) = E[XY] - E[X]E[Y]$$
$$E[XY] = \sum \sum xy p(x,y) \quad \text{or} \quad \int \int xy f(x,y) dx dy$$

---

## Mathematical Intuition

**Joint = 2D Distribution**: Probability mass/density spread over a 2D plane.

**Marginal = Projection**: Project 2D onto axes by summing/integrating out the other variable.

**Conditional = Slice**: Fix one variable, renormalize the slice.

---

## Algorithms / Problem-Solving

### Joint Distribution Analysis
```
1. Identify if discrete or continuous
2. Find support (where f/p > 0)
3. Verify normalization (sum/integral = 1)
4. Compute marginals by summing/integrating
5. Check independence: f(x,y) = f_X(x)f_Y(y)?
6. Compute E[XY] for covariance
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Operation | Discrete | Continuous |
|-----------|----------|------------|
| Normalization | $\sum \sum p = 1$ | $\int \int f = 1$ |
| Marginal | $\sum_y p(x,y)$ | $\int f(x,y) dy$ |
| Conditional | $p(y|x) = p(x,y)/p_X(x)$ | $f(y|x) = f(x,y)/f_X(x)$ |
| E[XY] | $\sum \sum xy p(x,y)$ | $\int \int xy f(x,y) dx dy$ |

---

## GATE Tricks

> [!tip>
> **E[X+Y] = E[X] + E[Y]** ALWAYS, even if dependent!
> **Independence**: Check if $f(x,y) = f_X(x)f_Y(y)$
> **$E[XY] = E[X]E[Y]$** only if independent!
> **$E[g(X)h(Y)] = E[g(X)]E[h(Y)]$** if independent
> **$E[X+Y] = E[X] + E[Y]$** always!

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Joint | Marginal | 2D vs 1D |
| Joint | Conditional | Unconditional vs given X=x |
| Marginal | Conditional | Unconditional vs given |

---

## Common Mistakes

> [!warning>
> **Forgetting to check support**: $f(x,y)$ might be 0 in some regions!
> **Assuming independence**: Always verify $f(x,y) = f_X(x)f_Y(y)$
> **Using wrong limits**: Integration limits depend on support!
> **E[XY] = E[X]E[Y] without independence**: Only true if independent!

---

## Memory Tricks

> [!tip>
> **Joint** = **Jo**int = **Jo**ined together = 2D
> **Marginal** = **Mar**ginal = **Mar**gin = edge = projected to axes
> **Conditional** = **Con**ditional = given condition

---

## Previous GATE Patterns

- **Find constant**: Normalize joint PDF/PMF
- **Find marginals**: Integrate/sum out other variable
- **Check independence**: Factor joint into marginals
- **Compute E[XY]**: For covariance
- **Find probability**: $P(X < Y)$, $P(X+Y < c)$ etc.

---

## Revision Summary

```
JOINT PROBABILITY DISTRIBUTIONS
├── Discrete: p(x,y) = P(X=x,Y=y), ΣΣ p = 1
├── Continuous: f(x,y) ≥ 0, ∫∫ f = 1
├── Marginals: p_X(x) = Σ_y p(x,y) or ∫ f(x,y) dy
├── Conditionals: f(y|x) = f(x,y)/f_X(x)
├── Independence: f(x,y) = f_X(x)f_Y(y)
├── E[X+Y] = E[X] + E[Y] (ALWAYS!)
├── E[XY] = E[X]E[Y] (iff independent)
├── Cov(X,Y) = E[XY] - E[X]E[Y]
└── Key: Marginals = integrate out other variable!
```

---

## Related Notes

- [[17 Covariance and Correlation]]
- [[19 Marginal Distributions]]
- [[20 Conditional Distributions]]
- [[21 Independence of Random Variables]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #joint-distribution #revision