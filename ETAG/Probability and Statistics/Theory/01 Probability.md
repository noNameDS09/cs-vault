---
tags: [probability, gate-da, basics, revision]
---

# 01 Probability

> [!note] Probability quantifies uncertainty. Foundation for all statistical inference.

---

## Overview

Probability assigns numerical values (0 to 1) to outcomes of random experiments. Forms the mathematical basis for statistics, machine learning, and data-driven decision making.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Random Experiment** | Process with uncertain outcome (e.g., coin toss, die roll) |
| **Sample Space ($\Omega$)** | Set of all possible outcomes |
| **Event** | Subset of sample space |
| **Probability Measure** | Function $P: \mathcal{F} \to [0,1]$ satisfying axioms |
| **Probability of Event $A$** | $P(A)$ = likelihood of event $A$ occurring |

---

## Formulae

### Probability Axioms (Kolmogorov)
1. **Non-negativity**: $P(A) \geq 0$ for any event $A$
2. **Normalization**: $P(\Omega) = 1$
3. **Countable Additivity**: For disjoint events $A_1, A_2, ...$
   $$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

### Basic Properties
$$P(\emptyset) = 0$$
$$P(A^c) = 1 - P(A)$$
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
If $A \subseteq B$: $P(A) \leq P(B)$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\Omega$ | Sample space (all outcomes) |
| $A, B, C$ | Events (subsets of $\Omega$) |
| $P(A)$ | Probability of event $A$ |
| $A^c$ | Complement of $A$ |
| $A \cup B$ | Union (A or B or both) |
| $A \cap B$ | Intersection (A and B) |
| $\emptyset$ | Impossible event |

---

## Important Properties

### Equally Likely Outcomes
If $\Omega = \{\omega_1, ..., \omega_n\}$ and all outcomes equally likely:
$$P(A) = \frac{|A|}{|\Omega|}$$
where $|A|$ = number of outcomes in event $A$

### Odds
Odds in favor of $A$: $\frac{P(A)}{P(A^c)} = \frac{P(A)}{1-P(A)}$

### Probability Bounds
$$0 \leq P(A) \leq 1$$
$$P(A \cap B) \leq \min(P(A), P(B))$$
$$P(A \cup B) \geq \max(P(A), P(B))$$

---

## Mathematical Intuition

**Probability as Relative Frequency**: For repeatable experiments, $P(A) \approx \frac{\text{times A occurs}}{\text{total trials}}$ as trials $\to \infty$.

**Probability as Degree of Belief**: For non-repeatable events (Bayesian view), probability quantifies subjective certainty.

---

## Algorithms / Problem-Solving

### Basic Probability Calculation
```
1. Identify sample space Ω
2. Define event of interest A
3. Check if outcomes are equally likely
4. If yes: P(A) = |A| / |Ω|
5. If no: Use given probabilities or axioms
6. Apply addition/multiplication rules as needed
```

---

## Complexity
Not applicable for basic probability concepts.

---

## Comparison Tables

### Probability Interpretations

| Interpretation | Description | Example |
|----------------|-------------|---------|
| **Frequentist** | Long-run relative frequency | Coin toss probability = 0.5 |
| **Bayesian** | Degree of belief | Probability it will rain tomorrow |
| **Axiomatic** | Mathematical structure satisfying Kolmogorov axioms | Theoretical foundation |

### Event Types

| Type | Notation | Description |
|------|----------|-------------|
| Certain | $\Omega$ | Always occurs, $P=1$ |
| Impossible | $\emptyset$ | Never occurs, $P=0$ |
| Elementary | $\{\omega\}$ | Single outcome |
| Compound | Multiple outcomes | Any non-elementary event |

---

## GATE Tricks

> [!tip]
> **Equally likely shortcut**: If all outcomes equally likely, just count!
> $$P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$$

> [!tip]
> **Complement is often easier**: "At least one" $\to$ $1 - P(\text{none})$

> [!tip]
> **Mutually exclusive = just add**: If $A \cap B = \emptyset$, then $P(A \cup B) = P(A) + P(B)$

---

## Frequently Confused Concepts

| Concept A          | Concept B    | Difference                                |
| ------------------ | ------------ | ----------------------------------------- |
| Probability        | Odds         | Probability ∈ [0,1], Odds ∈ [0, ∞)        |
| Union              | Intersection | $A \cup B$ = A or B; $A \cap B$ = A and B |
| Mutually exclusive | Independent  | Disjoint vs. no influence                 |
| $P(AB)$            | $P(BA)$      | Different conditionals!                   |

---

## Common Mistakes

> [!warning]
> **Assuming equally likely when not true**: Don't assume outcomes equally likely without justification.

> [!warning]
> **Double counting**: For $P(A \cup B)$, always subtract $P(A \cap B)$.

> [!warning]
> **$P(A|B) \neq P(B|A)$**: Confusing conditionals is a major error!

---

## Memory Tricks

> [!tip]
> **Axioms**: Non-neg, Sum to 1, Add for disjoint
> **Union**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (VENN DIAGRAM!)
> **Complement**: $P(A^c) = 1 - P(A)$ ("the rest")

---

## Previous GATE Patterns

- **Counting-based**: Simple probability from counting favorable/total
- **Set operations**: Given $P(A), P(B), P(A \cap B)$, find $P(A \cup B)$
- **Complement**: Find probability of "at least one" event
- **Basic axioms**: Verify if given probabilities are valid

---

## Revision Summary

```
PROBABILITY BASICS
├── Axioms: P(A) ≥ 0, P(Ω) = 1, P(∪Aᵢ) = ΣP(Aᵢ) for disjoint
├── P(∅) = 0, P(Aᶜ) = 1 - P(A)
├── Union: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
├── Equally likely: P(A) = |A|/|Ω|
├── Bounds: 0 ≤ P(A) ≤ 1
└── Key: Complement, mutual exclusion, independence
```

---

## Related Notes

- [[02 Sample Space and Events]]
- [[03 Counting Principles]]
- [[04 Permutations and Combinations]]
- [[05 Conditional Probability]]
- [[07 Independence]]

---

#probability #gate-da #basics #revision