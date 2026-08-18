---
tags: [probability, gate-da, conditional-distribution, revision]
---

# 20 Conditional Distributions

> [!note] Conditional distribution describes the distribution of one variable given a specific value of another.

---

## Overview

Conditional distributions describe how one variable behaves when another is known. They are essential for Bayesian inference, regression, and understanding dependence.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Conditional PMF** | $p_{Y|X}(y|x) = \frac{p_{X,Y}(x,y)}{p_X(x)}$ |
| **Conditional PDF** | $f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$ |
| **Conditional Expectation** | $E[Y|X=x]$ |
| **Conditional Variance** | $Var(Y|X=x)$ |

---

## Formulae

### Discrete Conditional PMF
$$p_{Y|X}(y|x) = \frac{p_{X,Y}(x,y)}{p_X(x)}, \quad p_X(x) > 0$$

### Continuous Conditional PDF
$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}, \quad f_X(x) > 0$$

### Conditional Expectation
$$E[Y|X=x] = \begin{cases}
\sum_y y \, p_{Y|X}(y|x) & \text{discrete} \\
\int y \, f_{Y|X}(y|x) dy & \text{continuous}
\end{cases}$$

### Conditional Variance
$$Var(Y|X=x) = E[Y^2|X=x] - (E[Y|X=x])^2$$

### Law of Total Expectation
$$E[Y] = E[E[Y|X]] = \sum_x E[Y|X=x] p_X(x) = \int E[Y|X=x] f_X(x) dx$$

### Law of Total Variance
$$Var(Y) = E[Var(Y|X)] + Var(E[Y|X])$$

### Conditional Independence
$Y \perp Z | X \iff f_{Y,Z|X}(y,z|x) = f_{Y|X}(y|x) f_{Z|X}(z|x)$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p_{Y|X}(y|x)$ | Conditional PMF of Y given X=x |
| $f_{Y|X}(y|x)$ | Conditional PDF of Y given X=x |
| $E[Y|X=x]$ | Conditional expectation |
| $E[Y|X]$ | Random variable (function of X) |

---

## Important Properties

### Conditional Expectation as Random Variable
$E[Y|X]$ is a function of $X$, hence a random variable.
- $E[E[Y|X]] = E[Y]$
- $Cov(X, E[Y|X]) = Cov(X, Y)$
- $E[Y|X] = E[Y]$ if $X \perp Y$

### Conditional Variance Decomposition
$$Var(Y) = E[Var(Y|X)] + Var(E[Y|X])$$
- $E[Var(Y|X)]$ = average within-group variance
- $Var(E[Y|X])$ = between-group variance

### Regression Function
$m(x) = E[Y|X=x]$ is the regression function.

---

## Mathematical Intuition

**Conditioning = Slice and Renormalize**: Take a slice of the joint distribution at $X=x$, then renormalize so it integrates/sums to 1.

**Conditional Expectation = Best Predictor**: $E[Y|X]$ minimizes $E[(Y - g(X))^2]$ over all functions $g$.

**Law of Total Variance**: Total variability = average within-group + between-group.

---

## Algorithms / Problem-Solving

### Finding Conditional Distribution
```
1. Find joint f(x,y) and marginal f_X(x)
2. Divide: f_{Y|X}(y|x) = f(x,y) / f_X(x)
3. Determine support of y given x
4. Compute conditional expectation/variance
```

### Law of Total Expectation/Variance
```
For E[Y]:
1. Find E[Y|X=x] as function of x
2. Average over distribution of X: E[E[Y|X]]

For Var(Y):
1. Find Var(Y|X=x) and E[Y|X=x]
2. Apply: E[Var(Y|X)] + Var(E[Y|X])
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| | Discrete | Continuous |
|---|----------|------------|
| Conditional PMF/PDF | $p(y|x) = p(x,y)/p_X(x)$ | $f(y|x) = f(x,y)/f_X(x)$ |
| Conditional E[Y|X] | $\sum y p(y|x)$ | $\int y f(y|x) dy$ |

---

## GATE Tricks

> [!tip>
> **Conditional = Joint / Marginal**
> **E[Y] = E[E[Y|X]]** (Law of Total Expectation)
> **Var(Y) = E[Var(Y|X)] + Var(E[Y|X])** (Law of Total Variance)
> **E[Y|X] = E[Y] if independent**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $E[Y|X=x]$ | $E[Y|X]$ | Number vs random variable |
| Conditional | Marginal | Given X=x vs unconditional |
| $E[Y|X]$ | $E[Y]$ | Function of X vs constant |

---

## Common Mistakes

> [!warning>
> **Forgetting to divide by marginal**: $f(y|x) = f(x,y)/f_X(x)$, not just $f(x,y)$!
> **Using wrong support**: Support of $Y|X=x$ may differ from support of $Y$!
> **Confusing $E[Y|X=x]$ with $E[Y|X]$**: One is number, one is RV!

---

## Memory Tricks

> [!tip>
> **Conditional** = **Con**ditional = given **Con**dition
> **Slice and renormalize**: $f(y|x) = f(x,y)/f_X(x)$
> **Total Expectation**: $E[Y] = E[E[Y|X]]$

---

## Previous GATE Patterns

- **Find conditional distribution**: Given joint, find $f(y|x)$
- **Law of Total Expectation**: Compute $E[Y]$ via $E[E[Y|X]]$
- **Law of Total Variance**: Decompose variance
- **Conditional expectation**: $E[Y|X=x]$ from conditional distribution

---

## Revision Summary

```
CONDITIONAL DISTRIBUTIONS
├── f_{Y|X}(y|x) = f_{X,Y}(x,y) / f_X(x)
├── E[Y|X=x] = Σ/∫ y f(y|x) dy
├── Law of Total Expectation: E[Y] = E[E[Y|X]]
├── Law of Total Variance: Var(Y) = E[Var(Y|X)] + Var(E[Y|X])
├── E[Y|X] = best predictor (minimizes MSE)
├── Conditional independence: f(y,z|x) = f(y|x)f(z|x)
└── Key: Slice joint at X=x, renormalize!
```

---

## Related Notes

- [[18 Joint Probability Distributions]]
- [[19 Marginal Distributions]]
- [[21 Independence of Random Variables]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #conditional-distribution #revision