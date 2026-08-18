---
tags: [probability, gate-da, conditional-probability, revision]
---

# 05 Conditional Probability

> [!note] Probability of event A given that event B has occurred.

---

## Overview

Conditional probability updates our assessment of likelihood when we gain new information. It's the foundation for Bayes' theorem and statistical inference.

---

## Key Concepts

| Concept                     | Definition                                  |
| --------------------------- | ------------------------------------------- |
| **Conditional Probability** | $P(AB)$ = probability of A given B occurred |
| **Conditioning Event**      | B (must have $P(B) > 0$)                    |
| **Multiplication Rule**     | $P(A \cap B) = P(AB)P(B)$                   |
| **Total Probability**       | Law of total probability over a partition   |

---

## Formulae

### Definition
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

### Multiplication Rule
$$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$

### Chain Rule (Multiple Events)
$$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1 \cap A_2) ... P(A_n|A_1 \cap ... \cap A_{n-1})$$

### Total Probability Theorem
If $B_1, ..., B_n$ partition $\Omega$ (mutually exclusive, exhaustive):
$$P(A) = \sum_{i=1}^n P(A|B_i)P(B_i)$$

### Bayes Theorem
$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^n P(A|B_j)P(B_j)}$$

---

## Meaning of Variables

| Symbol        | Meaning                      |
| ------------- | ---------------------------- |
| $P(AB)$       | Probability of A given B     |
| $P(A \cap B)$ | Joint probability of A and B |
| $P(B)$        | Marginal probability of B    |
| $B_i$         | Partition events             |

---

## Important Properties

### Basic Properties of Conditional Probability
For fixed $B$ with $P(B) > 0$:
1. $0 \leq P(A|B) \leq 1$
2. $P(\Omega|B) = 1$
3. If $A_1, A_2, ...$ are disjoint: $P(\bigcup A_i | B) = \sum P(A_i|B)$

### Independence and Conditional Probability
If $A \perp B$: $P(A|B) = P(A)$ and $P(B|A) = P(B)$

---

## Mathematical Intuition

**Conditioning = Restricting Sample Space**: Given $B$ occurred, we restrict attention to outcomes in $B$. New probabilities proportional to original probabilities within $B$.

**Multiplication Rule**: Probability of both A and B = probability of B × probability of A within B.

---

## Algorithms / Problem-Solving

### Conditional Probability Calculation
```
1. Identify events A (what we want) and B (given)
2. Find P(A ∩ B) - joint probability
3. Find P(B) - probability of given event
4. Compute P(A|B) = P(A ∩ B) / P(B)
```

### Using Total Probability
```
1. Identify partition B₁, ..., Bₙ (exhaustive, mutually exclusive)
2. Find P(Bᵢ) for each partition element
3. Find P(A|Bᵢ) for each
4. Sum: P(A) = Σ P(A|Bᵢ)P(Bᵢ)
```

### Tree Diagrams
```
Root → B₁ (P(B₁)) → A (P(A|B₁))
    → B₂ (P(B₂)) → A (P(A|B₂))
    ...
Path probability = product along branches
Total P(A) = sum of path probabilities to A
```

---

## Complexity
Not applicable for basic conditional probability.

---

## Comparison Tables

| Concept           | Formula                            | Use When                        |
| ----------------- | ---------------------------------- | ------------------------------- |
| Conditional Prob  | $P(AB) = \frac{P(A \cap B)}{P(B)}$ | Given B, find P(A)              |
| Multiplication    | $P(A \cap B) = P(AB)P(B)$          | Find joint from conditional     |
| Total Probability | $P(A) = \sum P(AB_i)P(B_i)$        | Find marginal from conditionals |
| Bayes             | $P(BA) = \frac{P(AB)P(B)}{P(A)}$   | Reverse conditional             |

---

## GATE Tricks

> [!tip]
> **Always check $P(B) > 0$**: Conditional probability undefined if $P(B) = 0$

> [!tip]
> **Tree diagrams**: Draw for multi-stage problems - multiply along branches, add at root

> [!tip]
> **Total Probability**: If you need $P(A)$ and have $P(A|B_i)$ for partition $B_i$, use total probability

> [!tip]
> **Bayes reverses**: $P(\text{cause}|\text{effect})$ from $P(\text{effect}|\text{cause})$

> [!tip]
> **Medical testing pattern**: Disease = cause, Test = effect. $P(\text{Disease}|\text{Positive})$ is what we want!

---

## Frequently Confused Concepts

|Concept A|Concept B|Difference|Key Point|
|---|---|---|---|
|$P(A\mid B)$|$P(B\mid A)$|Different! Reverse conditionals|The condition is reversed.|
|$P(A\cap B)$|$P(A\mid B)$|Joint vs. conditional|$P(A\cap B)$ is the probability of both; $P(A\mid B)$ is the probability of $A$ given $B$.|
|Independent|Conditional|$P(A\mid B)=P(A)$ if independent|Independence means knowing $B$ does not change the probability of $A$.|
|$P(A\mid B)+P(A^c\mid B)$|$1$|Always sums to 1|Given $B$, either $A$ or its complement $A^c$ occurs.|

---

## Common Mistakes

> [!warning]
> **$P(A|B) \neq P(B|A)$**: The most common confusion! Use Bayes to convert.

> [!warning]
> **Using $P(A)$ instead of $P(B)$ in denominator**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

> [!warning]
> **Forgetting to normalize**: In Bayes, denominator is sum over ALL hypotheses

> [!warning]
> **Assuming $P(A|B) + P(A|B^c) = 1$**: False! It's $P(A|B) + P(A^c|B) = 1$

---

## Memory Tricks

> [!tip]
> **Vertical bar = "Given"**: $P(A|B)$ = "A given B"
> **Numerator**: What we want AND what we know ($A \cap B$)
> **Denominator**: What we know ($B$)

> [!tip]
> **Tree**: Multiply down, add across

---

## Previous GATE Patterns

- **Direct calculation**: Given $P(A \cap B)$ and $P(B)$, find $P(A|B)$
- **Total probability**: Given $P(A|B_i)$ and $P(B_i)$, find $P(A)$
- **Bayes**: Medical testing, spam filtering, quality control
- **Chain rule**: Sequential draws without replacement

---

## Revision Summary

```
CONDITIONAL PROBABILITY
├── P(A|B) = P(A ∩ B) / P(B), P(B) > 0
├── Multiplication: P(A ∩ B) = P(A|B)P(B)
├── Chain rule: P(A₁∩...∩Aₙ) = P(A₁)P(A₂|A₁)...
├── Total Probability: P(A) = Σ P(A|Bᵢ)P(Bᵢ) for partition Bᵢ
├── Bayes: P(B|A) = P(A|B)P(B) / P(A)
├── Tree diagrams: multiply down, add across
├── Key: P(A|B) ≠ P(B|A)!
└── Independent ⇒ P(A|B) = P(A)
```

---

## Related Notes

- [[06 Bayes Theorem]]
- [[07 Independence]]
- [[01 Probability]]
- [[02 Sample Space and Events]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #conditional-probability #bayes #revision