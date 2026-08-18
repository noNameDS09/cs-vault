---
tags: [probability, gate-da, independence-rv, revision]
---

# 21 Independence of Random Variables

> [!note] Random variables are independent if their joint distribution factors into the product of marginals.

---

## Overview

Independence of random variables means that knowing the value of one provides no information about the other. It's the multivariate extension of event independence.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Independent RVs** | $f_{X,Y}(x,y) = f_X(x) f_Y(y)$ for all $x,y$ |
| **Mutual Independence** | All combinations factor |
| **Pairwise Independence** | Every pair independent |

---

## Formulae

### Definition
$$X \perp Y \iff f_{X,Y}(x,y) = f_X(x) f_Y(y) \quad \forall x,y$$

### Discrete
$$P(X=x, Y=y) = P(X=x) P(Y=y) \quad \forall x,y$$

### Continuous
$$f_{X,Y}(x,y) = f_X(x) f_Y(y) \quad \forall x,y$$

### Implications of Independence
1. $E[g(X)h(Y)] = E[g(X)]E[h(Y)]$
2. $E[XY] = E[X]E[Y]$
3. $Cov(X,Y) = 0$
3. $Var(X+Y) = Var(X) + Var(Y)$
4. $M_{X+Y}(t) = M_X(t) M_Y(t)$
5. $f_{Y|X}(y|x) = f_Y(y)$

### Mutual Independence
$X_1, ..., X_n$ mutually independent iff for any subset:
$$f_{X_{i_1}, ..., X_{i_k}}(x_1, ..., x_k) = \prod_{j=1}^k f_{X_{i_j}}(x_j)$$

### Pairwise vs Mutual
- Pairwise: every pair independent
- Mutual: all combinations factor
- **Mutual ⇒ Pairwise, but Pairwise ⇏ Mutual**

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $X \perp Y$ | X and Y are independent |
| $f_X(x)$ | Marginal PDF/PMF |
| $f_{X,Y}(x,y)$ | Joint PDF/PMF |

---

## Important Properties

### Equivalent Conditions for Independence
All equivalent:
1. $f_{X,Y}(x,y) = f_X(x) f_Y(y)$
2. $F_{X,Y}(x,y) = F_X(x) F_Y(y)$
3. $f_{Y|X}(y|x) = f_Y(y)$
4. $E[g(X)h(Y)] = E[g(X)]E[h(Y)]$ for all bounded $g,h$
5. $M_{X+Y}(t) = M_X(t) M_Y(t)$

### Functions of Independent RVs
If $X \perp Y$, then $g(X) \perp h(Y)$ for any measurable $g, h$.

---

## Mathematical Intuition

**Independence = No Information Flow**: The conditional distribution equals the marginal. Knowing $X$ tells you nothing about $Y$.

**Product of Marginals**: The joint "rectangle" is perfectly aligned with axes - no tilt, no dependence.

---

## Algorithms / Problem-Solving

### Checking Independence
```
1. Find joint f(x,y)
2. Find marginals f_X(x), f_Y(y)
3. Check if f(x,y) = f_X(x) f_Y(y) for all x,y
4. OR check if F(x,y) = F_X(x) F_Y(y)
5. OR check if support is Cartesian product and density factors
```

### Using Independence
```
If independent:
- E[XY] = E[X]E[Y]
- Var(X+Y) = Var(X) + Var(Y)
- MGF: M_{X+Y}(t) = M_X(t) M_Y(t)
- f_{Y|X}(y|x) = f_Y(y)
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Independence Type | Definition |
|-------------------|------------|
| Pairwise | $X_i \perp X_j$ for all pairs |
| Mutual | All combinations factor |
| Conditional | $X \perp Y | Z$ |

| Level | Implies |
|-------|---------|
| Mutual | Pairwise |
| Pairwise | NOT Mutual (in general) |

---

## GATE Tricks

> [!tip>
> **Check support first**: If support is NOT rectangular (Cartesian product), CANNOT be independent!
> **Independence ⇒ E[XY] = E[X]E[Y], Var(X+Y) = Var(X)+Var(Y)**
> **MGF of sum = product**: $M_{X+Y}(t) = M_X(t)M_Y(t)$
> **Functions of independent are independent**: $g(X) \perp h(Y)$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Pairwise | Mutual | Every pair vs all combinations |
| Independent | Uncorrelated | Independent ⇒ ρ=0, but ρ=0 ⇏ Independent |
| Events | RVs | Events: P(A∩B)=P(A)P(B); RVs: f(x,y)=f_X f_Y |

---

## Common Mistakes

> [!warning>
> **Assuming pairwise ⇒ mutual**: Classic counterexample exists!
> **Assuming uncorrelated ⇒ independent**: False in general (true for bivariate normal)
> **Not checking support**: Non-rectangular support = NOT independent!

---

## Memory Tricks

> [!tip>
> **Independent** = **In** + **Dependent** = NOT dependent
> **Support check**: Rectangular support needed for independence
> **Independence = Product**: f(x,y) = f_X(x) * f_Y(y)

---

## Previous GATE Patterns

- **Check independence**: Given joint, verify if factors
- **Support check**: Identify non-rectangular support
- **Use independence**: Simplify E[XY], Var(X+Y)
- **Pairwise vs mutual**: Construct/identify counterexample
- **MGF product**: Sum of independent via MGF

---

## Revision Summary

```
INDEPENDENCE OF RANDOM VARIABLES
├── f_{X,Y}(x,y) = f_X(x) f_Y(y) for all x,y
├── Equivalent: F(x,y) = F_X(x)F_Y(y), f(y|x) = f_Y(y)
├── Independent ⇒ E[XY]=E[X]E[Y], Cov=0, Var(X+Y)=Var(X)+Var(Y)
├── M_{X+Y}(t) = M_X(t)M_Y(t)
├── Functions of independent are independent
├── Support must be Cartesian product (rectangular)
├── Mutual ⇒ Pairwise, NOT vice versa
└── Key: Independence = no information flow = factorization
```

---

## Related Notes

- [[07 Independence]]
- [[17 Covariance and Correlation]]
- [[18 Joint Probability Distributions]]
- [[19 Marginal Distributions]]
- [[20 Conditional Distributions]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #independence-rv #revision