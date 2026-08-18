---
tags: [probability, gate-da, discrete-rv, revision]
---

# 09 Discrete Random Variables

> [!note] Discrete RVs take countable values. Described by Probability Mass Function (PMF).

---

## Overview

A discrete random variable takes values in a countable set (finite or countably infinite). Each possible value has a specific probability. The PMF gives the probability for each value.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Discrete RV** | Takes countable values $\{x_1, x_2, ...\}$ |
| **PMF** | $P(X = x_i) = p_i$ |
| **Support** | $\{x: P(X=x) > 0\}$ |
| **Mode** | Value with highest probability |

---

## Formulae

### PMF Properties
$$P(X = x_i) = p_i \geq 0$$
$$\sum_i p_i = 1$$

### Expectation (Discrete)
$$E[X] = \sum_i x_i p_i$$

### Variance (Discrete)
$$Var(X) = \sum_i (x_i - \mu)^2 p_i = E[X^2] - \mu^2$$
$$E[X^2] = \sum_i x_i^2 p_i$$

### CDF (Discrete)
$$F(x) = P(X \leq x) = \sum_{x_i \leq x} p_i$$

### Indicator Variables
For event $A$: $I_A = 1$ if $A$ occurs, $0$ otherwise
$$P(I_A = 1) = P(A), \quad P(I_A = 0) = 1 - P(A)$$
$$E[I_A] = P(A), \quad Var(I_A) = P(A)(1-P(A))$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $X$ | Discrete random variable |
| $x_i$ | Possible values |
| $p_i$ | $P(X = x_i)$ |
| $\mu$ | $E[X]$ |

---

## Important Properties

### Linearity of Expectation (Always Holds!)
$$E[aX + bY + c] = aE[X] + bE[Y] + c$$
**No independence needed!**

### Sum of Independent Discrete RVs
If $X, Y$ independent:
- $P(X+Y = z) = \sum_x P(X=x)P(Y=z-x)$ (Convolution)
- $E[X+Y] = E[X] + E[Y]$
- $Var(X+Y) = Var(X) + Var(Y)$

---

## Mathematical Intuition

**PMF = Mass Distribution**: Imagine unit mass distributed at points $x_i$ with weights $p_i$. Expectation = center of mass.

**CDF = Step Function**: Jumps of size $p_i$ at each $x_i$.

---

## Algorithms / Problem-Solving

### Discrete RV Analysis
```
1. Identify all possible values x_i
2. Find probabilities p_i for each
3. Verify Σ p_i = 1
4. Compute E[X] = Σ x_i p_i
5. Compute E[X²] = Σ x_i² p_i
6. Var(X) = E[X²] - (E[X])²
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Property  | Discrete      | Continuous    |
| --------- | ------------- | ------------- |
| Values    | Countable     | Uncountable   |
| $P(X=x)$  | Can be $> 0$  | Always 0      |
| $PMF/PDF$ | $p_i$         | $f(x)$        |
| $E[X]$    | $Σ x_i p_i$   | $∫ x f(x) dx$ |
| $CDF$     | Step function | Continuous    |

---

## GATE Tricks

> [!tip]
> **Indicator variables**: Convert "number of events" to sum of indicators. $E[count] = Σ P(event)$

> [!tip]
> **Linearity of E**: Works ALWAYS, even with dependence!

> [!tip]
> **$E[X²]$ shortcut**: Compute directly from distribution, then Var = $E[X²] - μ²$

> [!tip]
> **Common GATE**: Given PMF table with missing value, use $Σp_i = 1$ to find it

---

## Frequently Confused Concepts

|Concept A|Concept B|Difference|
|---|---|---|
|PMF|CDF|$P(X=x)$ vs. $P(X\le x)$|
|$E[X]$|$E[X^2]$|Mean vs. mean of squares|
|$E[XY]$|$E[X]E[Y]$|Equal only if $X$ and $Y$ are independent|

---

## Common Mistakes

> [!warning]
> **Forgetting $Σp_i = 1$**: Always verify!

> [!warning]
> **$E[X²] ≠ (E[X])²$**: Variance is the difference!

> [!warning]
> **Confusing $PMF$ with $CDF$**: $PMF$ = point probability, $CDF$ = cumulative

---

## Memory Tricks

> [!tip]
> **PMF** = **P**robability **M**ass **F**unction - mass at points
> **$E[X]$** = center of mass = $Σ (position × mass)$

---

## Previous GATE Patterns

- **PMF table completion**: Find missing probability
- **Expectation calculation**: Given PMF, find $E[X], E[X²]$
- **Variance**: Using $E[X²] - μ²$
- **Indicator variables**: Expected number of occurrences

---

## Revision Summary

```
DISCRETE RANDOM VARIABLES
├── PMF: P(X=x_i) = p_i, Σp_i = 1
├── E[X] = Σ x_i p_i
├── E[X²] = Σ x_i² p_i
├── Var(X) = E[X²] - (E[X])²
├── Linearity: E[aX+bY] = aE[X]+bE[Y] (always!)
├── Indicators: E[I_A] = P(A)
└── Key: Summation, not integration!
```

---

## Related Notes

- [[08 Random Variables]]
- [[11 Probability Mass Function]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]

---

#probability #gate-da #discrete-rv #revision