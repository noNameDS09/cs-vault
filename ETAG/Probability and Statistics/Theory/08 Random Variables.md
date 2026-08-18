---
tags: [probability, gate-da, random-variables, revision]
---

# 08 Random Variables

> [!note] A random variable is a function mapping outcomes to real numbers.

---

## Overview

A random variable (RV) assigns a numerical value to each outcome of a random experiment. It's the bridge between abstract probability spaces and numerical analysis.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Random Variable (RV)** | Function $X: \Omega \to \mathbb{R}$ |
| **Discrete RV** | Takes countable values $\{x_1, x_2, ...\}$ |
| **Continuous RV** | Takes uncountable values (intervals) |
| **Support** | Set of values with non-zero probability |
| **Distribution** | Complete description of probabilities |

---

## Formulae

### Types of RVs
**Discrete**: $X$ takes values in countable set
- PMF: $P(X = x_i) = p_i$
- $\sum_i p_i = 1$

**Continuous**: $X$ takes values in $\mathbb{R}$ or interval
- PDF: $f(x) \geq 0$, $\int_{-\infty}^{\infty} f(x) dx = 1$
- $P(X = x) = 0$ for any single $x$

### Distribution Function (CDF)
$$F_X(x) = P(X \leq x)$$
- Discrete: $F(x) = \sum_{x_i \leq x} p_i$
- Continuous: $F(x) = \int_{-\infty}^x f(t) dt$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $X, Y, Z$ | Random variables (uppercase) |
| $x, y, z$ | Realized values (lowercase) |
| $X(\omega)$ | Value of $X$ at outcome $\omega$ |
| $\mathcal{X}$ | Support of $X$ |

---

## Important Properties

### Function of a Random Variable
If $Y = g(X)$:
- Discrete: $P(Y = y) = \sum_{x: g(x)=y} P(X=x)$
- Continuous: $f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$ (monotonic)

### Indicator Random Variable
$$I_A(\omega) = \begin{cases} 1 & \omega \in A \\ 0 & \omega \notin A \end{cases}$$
- $E[I_A] = P(A)$
- $Var(I_A) = P(A)(1-P(A))$

---

## Mathematical Intuition

**RV as Measurement**: Random experiment → outcome → measure something about it → numerical value.

**Why Random Variables?** They allow us to use calculus, algebra, and numerical methods on probabilistic phenomena.

---

## Algorithms / Problem-Solving

### Identifying RV Type
```
1. List possible values of X
2. If countable (finite or countably infinite) → Discrete
3. If interval/uncountable → Continuous
4. Check if P(X=x) > 0 for some x → Discrete
   If P(X=x) = 0 for all x → Continuous
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Property | Discrete RV | Continuous RV |
|----------|-------------|---------------|
| Values | Countable | Uncountable |
| PMF/PDF | $P(X=x_i)$ | $f(x)$ |
| $P(X=x)$ | Can be > 0 | Always 0 |
| CDF | Step function | Continuous |
| Probability | Sum PMF | Integrate PDF |

---

## GATE Tricks

> [!tip]
> **Discrete**: Can list values. **Continuous**: Intervals.

> [!tip]
> **$P(X=x) = 0$ for continuous RVs**: Only probabilities over intervals matter!

> [!tip]
> **Indicator RVs**: Convert events to numbers. $E[I_A] = P(A)$.

> [!tip]
> **Mixed RVs**: Some discrete, some continuous (e.g., insurance claims with probability of zero claim)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Discrete RV | Continuous RV | Countable vs uncountable values |
| PMF | PDF | $P(X=x)$ vs density $f(x)$ |
| $P(X=x)$ | $f(x)$ | Probability vs density value |
| RV | Distribution | RV is function; distribution is probabilities |

---

## Common Mistakes

> [!warning]
> **Treating PDF value as probability**: $f(x)$ can be > 1! Only area = probability.

> [!warning]
> **$P(X=x)$ for continuous**: Always 0! Use $P(a < X < b)$.

> [!warning]
> **Confusing RV with its value**: $X$ is the function, $x$ is a number.

---

## Memory Tricks

> [!tip]
> **Discrete** = **Dis**crete = distinct separate values
> **Continuous** = **Con**tinuous = unbroken interval

> [!tip]
> **PMF**: **P**robability **M**ass **F**unction - mass at points
> **PDF**: **P**robability **D**ensity **F**unction - density over intervals

---

## Previous GATE Patterns

- **Identify type**: Given description, classify as discrete/continuous
- **Support**: Find range of possible values
- **Indicator variables**: Use for expectation of counts
- **Transformation**: Find distribution of $Y = g(X)$

---

## Revision Summary

```
RANDOM VARIABLES
├── X: Ω → ℝ (function)
├── Discrete: countable values, PMF, P(X=x) > 0
├── Continuous: uncountable, PDF, P(X=x) = 0
├── CDF: F(x) = P(X ≤ x)
├── Indicator: I_A, E[I_A] = P(A)
└── Key: Discrete = sum, Continuous = integrate
```

---

## Related Notes

- [[09 Discrete Random Variables]]
- [[10 Continuous Random Variables]]
- [[11 Probability Mass Function]]
- [[12 Probability Density Function]]
- [[13 Cumulative Distribution Function]]
- [[14 Expectation]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #random-variables #revision