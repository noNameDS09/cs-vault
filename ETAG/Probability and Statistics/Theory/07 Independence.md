---
tags: [probability, gate-da, independence, revision]
---

# 07 Independence

> [!note] Independence means occurrence of one event doesn't affect probability of another.

---

## Overview

Independence is a fundamental concept where the occurrence of one event provides no information about another. It simplifies probability calculations significantly.

---

## Key Concepts

| Concept                      | Definition                            |
| ---------------------------- | ------------------------------------- |
| **Independent Events**       | $P(A \cap B) = P(A)P(B)$              |
| **Conditional Independence** | $P(AB) = P(A)$ (if $P(B)>0$)          |
| **Pairwise Independence**    | Every pair is independent             |
| **Mutual Independence**      | All combinations satisfy independence |
| **Independent RVs**          | Joint = product of marginals          |

---

## Formulae

### Events
**Definition**: $A \perp B \iff P(A \cap B) = P(A)P(B)$

**Equivalent Conditions** (if $P(B) > 0$):
- $P(A|B) = P(A)$
- $P(B|A) = P(B)$
- $P(A^c|B) = P(A^c)$

**Multiple Events**: $A_1, ..., A_n$ mutually independent iff for every subset:
$$P\left(\bigcap_{i \in I} A_i\right) = \prod_{i \in I} P(A_i)$$

### Random Variables
**Discrete**: $P(X=x, Y=y) = P(X=x)P(Y=y)$ for all $x,y$
**Continuous**: $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for all $x,y$

**Expectation of Product**: If $X \perp Y$, then $E[XY] = E[X]E[Y]$

**Variance of Sum**: If $X \perp Y$, $Var(X+Y) = Var(X) + Var(Y)$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $A \perp B$ | A and B are independent |
| $P(A \cap B)$ | Joint probability |
| $f_{X,Y}$ | Joint PDF/PMF |
| $f_X, f_Y$ | Marginal PDF/PMF |

---

## Important Properties

### Hierarchy of Independence
1. **Mutual Independence** ⇒ **Pairwise Independence** ⇒ **Uncorrelated**
2. Reverse implications are FALSE in general!

### Pairwise vs Mutual Independence
- **Pairwise**: $P(A_i \cap A_j) = P(A_i)P(A_j)$ for all pairs
- **Mutual**: All combinations including triple intersections

**Classic Counterexample**: Three events pairwise independent but not mutually independent.

### Independent vs Mutually Exclusive
- **Independent**: $P(A \cap B) = P(A)P(B)$ - can occur together
- **Mutually Exclusive**: $P(A \cap B) = 0$ - cannot occur together
- **Non-trivial events cannot be both!**

---

## Mathematical Intuition

**Independence = No Information Flow**: Knowing B occurred doesn't change probability of A.

**Geometric View**: In probability space, independent events have intersection area = product of areas.

---

## Algorithms / Problem-Solving

### Checking Independence
```
For events:
1. Compute P(A), P(B), P(A ∩ B)
2. Check if P(A ∩ B) = P(A)P(B)

For RVs:
1. Find joint distribution f(x,y)
2. Find marginals f_X(x), f_Y(y)
3. Check if f(x,y) = f_X(x)f_Y(y) for all x,y
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Relationship | Formula | Can Both Occur? |
|--------------|---------|-----------------|
| Independent | $P(A \cap B) = P(A)P(B)$ | Yes |
| Mutually Exclusive | $P(A \cap B) = 0$ | No |
| Dependent | $P(A \cap B) \neq P(A)P(B)$ | Yes |

| Independence Level | Implies |
|-------------------|---------|
| Mutual | Pairwise |
| Pairwise | NOT Mutual |
| Independence | Uncorrelated (zero covariance) |
| Uncorrelated | NOT Independence |

---

## GATE Tricks

> [!tip]
> **If $P(A) = 0$ or $1$, A is independent of ANY event!**

> [!tip]
> **$P(A \cap B) = P(A)P(B)$ is the definition - use it to check**

> [!tip]
> **Independent RVs**: $E[XY] = E[X]E[Y]$, $Cov(X,Y) = 0$

> [!tip]
> **Independent ⇒ Uncorrelated, but Uncorrelated ⇏ Independent!**

> [!tip]
> **Mutually exclusive with non-zero prob = DEPENDENT** (knowing one occurred means other cannot)

---

## Frequently Confused Concepts

| Concept A            | Concept B                | Difference                           |
| -------------------- | ------------------------ | ------------------------------------ |
| Independent          | Mutually Exclusive       | Can both occur vs Cannot both occur  |
| Pairwise Independent | Mutually Independent     | Pairs vs all combinations            |
| Uncorrelated         | Independent              | Zero covariance vs full independence |
| $P(AB) = P(A)$       | $P(A \cap B) = P(A)P(B)$ | Equivalent definitions               |


---

## Common Mistakes

> [!warning]
> **Assuming pairwise ⇒ mutual**: Counterexample exists!

> [!warning]
> **Confusing independent with mutually exclusive**: $A \cap B = \emptyset$ means dependent (unless trivial)!

> [!warning]
> **Assuming zero covariance = independent**: Only true for jointly normal!

> [!warning]
> **Using $P(A|B) = P(A)$ without checking $P(B) > 0$**

---

## Memory Tricks

> [!tip]
> **Independent** = "In" + "Dependent" = NOT dependent on each other
> **Mutually Exclusive** = "Mutually" + "Exclusive" = Exclude each other

> [!tip]
> **Venn Diagram**: Independent = area(A ∩ B) = area(A) × area(B) (scaled)

---

## Previous GATE Patterns

- **Check independence**: Given joint and marginal, verify
- **Find P(A ∩ B)**: Given independence, multiply
- **Pairwise vs mutual**: Construct/identify counterexample
- **Independent RVs**: Use $E[XY] = E[X]E[Y]$, $Var(X+Y) = Var(X)+Var(Y)$
- **Independent + Normal = Bivariate Normal**

---

## Revision Summary

```
INDEPENDENCE
├── Events: P(A ∩ B) = P(A)P(B) ⇔ P(A|B) = P(A)
├── RVs: f(x,y) = f_X(x)f_Y(y)
├── E[XY] = E[X]E[Y] if independent
├── Cov(X,Y) = 0 if independent
├── Var(X+Y) = Var(X) + Var(Y) if independent
├── Mutual ⇒ Pairwise, NOT vice versa
├── Independent ≠ Mutually Exclusive (unless trivial)
├── Uncorrelated ⇏ Independent (except bivariate normal)
└── Key: Independence = no information flow
```

---

## Related Notes

- [[05 Conditional Probability]]
- [[06 Bayes Theorem]]
- [[17 Covariance and Correlation]]
- [[21 Independence of Random Variables]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #independence #revision