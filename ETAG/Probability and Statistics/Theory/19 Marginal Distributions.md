---
tags: [probability, gate-da, marginal-distribution, revision]
---

# 19 Marginal Distributions

> [!note] Marginal distribution is the distribution of one variable obtained from a joint distribution by "summing/integrating out" the other variable.

---

## Overview

Given a joint distribution of (X, Y), the marginal distribution of X is the distribution of X alone, obtained by summing/integrating over all possible values of Y.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Marginal PMF** | $p_X(x) = \sum_y p_{X,Y}(x,y)$ |
| **Marginal PDF** | $f_X(x) = \int f_{X,Y}(x,y) dy$ |
| **Marginal CDF** | $F_X(x) = F_{X,Y}(x, \infty)$ |

---

## Formulae

### Discrete Marginal PMF
$$p_X(x) = \sum_y p_{X,Y}(x,y)$$
$$p_Y(y) = \sum_x p_{X,Y}(x,y)$$

### Continuous Marginal PDF
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$$
$$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dx$$

### Marginal CDF
$$F_X(x) = F_{X,Y}(x, \infty) = P(X \leq x, Y < \infty) = P(X \leq x)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p_X(x)$ | Marginal PMF of X |
| $f_X(x)$ | Marginal PDF of X |
| $F_X(x)$ | Marginal CDF of X |

---

## Important Properties

### Normalization
$$\sum_x p_X(x) = 1 \quad \text{or} \quad \int f_X(x) dx = 1$$

### From Marginals to Joint (if Independent)
If $X \perp Y$:
$$f_{X,Y}(x,y) = f_X(x) f_Y(y)$$
$$p_{X,Y}(x,y) = p_X(x) p_Y(y)$$

### Marginals Don't Determine Joint
Marginal distributions alone **do not** uniquely determine the joint distribution (unless independent).

### Law of Total Expectation
$$E[X] = \sum_y E[X|Y=y] p_Y(y) = \int E[X|Y=y] f_Y(y) dy$$

---

## Mathematical Intuition

**Marginal = Projection**: Project the 2D joint distribution onto the axes. The marginal is the "shadow" cast on each axis.

**Summing/Integrating Out**: "Averaging over" the other variable. You lose information about the relationship between variables.

---

## Algorithms / Problem-Solving

### Finding Marginals
```
1. Identify joint PMF/PDF
2. Determine limits for the other variable
3. Sum (discrete) or integrate (continuous) over the other variable
4. Verify normalization of marginal
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| | Discrete | Continuous |
|---|----------|------------|
| Marginal PMF/PDF | $p_X(x) = \sum_y p(x,y)$ | $f_X(x) = \int f(x,y) dy$ |
| Limits | Sum over all y | Integrate over support of Y |

---

## GATE Tricks

> [!tip>
> **Marginal = sum/integrate out the other variable**
> **Marginal CDF**: $F_X(x) = F_{X,Y}(x, \infty)$
> **Marginals don't determine joint**: Unless independent!
> **E[X] from marginal**: Same as from joint!

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Marginal | Conditional | Unconditional vs given X=x |
| Marginal | Joint | 1D vs 2D |
| $f_X(x)$ | $f_{X|Y}(x|y)$ | No condition vs given Y=y |

---

## Common Mistakes

> [!warning>
> **Wrong limits**: Must integrate over FULL support of other variable!
> **Assuming marginals determine joint**: False unless independent!
> **Using wrong variable**: $f_X(x) = \int f(x,y) dy$, not $dx$!

---

## Memory Tricks

> [!tip>
> **Marginal** = **Mar**ginal = **Mar**gin = edge = projected to axis
> **Sum/integrate OUT** the other variable

---

## Previous GATE Patterns

- **Find marginal PDF/PMF**: Integrate/sum joint
- **Check independence**: Factor joint
- **Find E[X] from marginal**: Use marginal directly

---

## Revision Summary

```
MARGINAL DISTRIBUTIONS
├── Discrete: p_X(x) = Σ_y p(x,y)
├── Continuous: f_X(x) = ∫ f(x,y) dy
├── Marginal CDF: F_X(x) = F_{X,Y}(x, ∞)
├── E[X] from marginal = E[X] from joint
├── Marginals ≠ Joint (unless independent)
├── If independent: f(x,y) = f_X(x)f_Y(y)
└── Key: Integrate/sum OUT the other variable!
```

---

## Related Notes

- [[18 Joint Probability Distributions]]
- [[20 Conditional Distributions]]
- [[21 Independence of Random Variables]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #marginal-distribution #revision