---
tags: [probability, gate-da, sample-space, events, revision]
---

# 02 Sample Space and Events

> [!note] Sample space = all possible outcomes. Events = subsets of sample space.

---

## Overview

The sample space $\Omega$ is the set of all possible outcomes of a random experiment. Events are subsets of $\Omega$ to which probabilities are assigned. Understanding the structure of sample spaces and event operations is crucial for solving probability problems.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Sample Space ($\Omega$)** | Set of all possible outcomes |
| **Outcome ($\omega$)** | Single element of $\Omega$ |
| **Event ($A$)** | Subset of $\Omega$ |
| **Elementary Event** | Single outcome $\{\omega\}$ |
| **Compound Event** | Event with multiple outcomes |
| **Certain Event** | $\Omega$ itself, $P=1$ |
| **Impossible Event** | $\emptyset$, $P=0$ |

---

## Formulae

### Set Operations on Events
| Operation | Notation | Meaning |
|-----------|----------|---------|
| Union | $A \cup B$ | $A$ or $B$ (or both) |
| Intersection | $A \cap B$ | $A$ and $B$ |
| Complement | $A^c$ or $\bar{A}$ | Not $A$ |
| Difference | $A \setminus B$ | $A$ but not $B$ |
| Symmetric Difference | $A \triangle B$ | $A$ or $B$ but not both |

### De Morgan's Laws
$$(A \cup B)^c = A^c \cap B^c$$
$$(A \cap B)^c = A^c \cup B^c$$

### Distributive Laws
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$

### Probability of Events
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(B \cap C) - P(C \cap A) + P(A \cap B \cap C)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\Omega$ | Sample space |
| $\omega$ | Single outcome |
| $A, B, C$ | Events (subsets of $\Omega$) |
| $A^c$ | Complement of $A$ |
| $\emptyset$ | Empty set (impossible event) |
| $|A|$ | Number of outcomes in event $A$ |

---

## Important Properties

### Mutually Exclusive (Disjoint) Events
$$A \cap B = \emptyset \implies P(A \cap B) = 0$$
$$P(A \cup B) = P(A) + P(B)$$

### Exhaustive Events
A collection $A_1, A_2, ..., A_n$ is exhaustive if:
$$A_1 \cup A_2 \cup ... \cup A_n = \Omega$$
$$\sum_{i=1}^n P(A_i) = 1 \quad \text{(if mutually exclusive)}$$

### Partition of Sample Space
Events $B_1, ..., B_n$ form a partition if:
- Mutually exclusive: $B_i \cap B_j = \emptyset$ for $i \neq j$
- Exhaustive: $\bigcup_{i=1}^n B_i = \Omega$
- All $P(B_i) > 0$

---

## Mathematical Intuition

**Venn Diagrams**: Visual representation of set operations. Overlap = intersection, union = everything in either circle.

**Sample Space Examples**:
- Coin toss: $\Omega = \{H, T\}$
- Die roll: $\Omega = \{1, 2, 3, 4, 5, 6\}$
- Two dice: $\Omega = \{(i,j): i,j \in \{1,...,6\}\}$ (36 outcomes)
- Continuous: $\Omega = [0, \infty)$ for time measurements

---

## Algorithms / Problem-Solving

### Sample Space Construction
```
1. Identify the random experiment
2. List ALL possible outcomes
3. Choose representation (list, tree, grid)
4. Verify completeness (no missing outcomes)
5. Check if outcomes equally likely
```

### Event Operations
```
Given events A and B:
- A ∪ B: Elements in A OR B
- A ∩ B: Elements in BOTH A and B
- Aᶜ: Elements NOT in A
- A \ B: Elements in A but NOT in B
```

---

## Complexity
Not applicable for basic set theory concepts.

---

## Comparison Tables

### Finite vs Infinite Sample Spaces

| Type | Example | Counting |
|------|---------|----------|
| Finite | Coin toss, dice | Count outcomes |
| Countably Infinite | Number of tosses until head | Summation |
| Uncountable | Time, length, weight | Integration |

### Event Relationships

| Relationship | Condition | Probability |
|--------------|-----------|-------------|
| Mutually Exclusive | $A \cap B = \emptyset$ | $P(A \cup B) = P(A) + P(B)$ |
| Independent | $P(A \cap B) = P(A)P(B)$ | See Independence |
| Subset | $A \subseteq B$ | $P(A) \leq P(B)$ |
| Complement | $B = A^c$ | $P(A) + P(B) = 1$ |

---

## GATE Tricks

> [!tip]
> **Sample space choice matters**: For two dice, use 36 ordered pairs $(i,j)$, not 21 unordered!

> [!tip]
> **Tree diagrams**: Great for sequential experiments (e.g., draw cards without replacement)

> [!tip]
> **Partition for Total Probability**: Identify partition $B_1, ..., B_n$ for complex events

> [!tip]
> **De Morgan's Laws**: $(A \cup B)^c = A^c \cap B^c$ - useful for complements of unions

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Outcome | Event | Outcome = single $\omega$; Event = set of outcomes |
| Mutually Exclusive | Independent | Disjoint vs. no influence |
| Exhaustive | Partition | Exhaustive = covers $\Omega$; Partition = exhaustive + disjoint |
| $A \setminus B$ | $B \setminus A$ | $A$ but not $B$ vs $B$ but not $A$ |

---

## Common Mistakes

> [!warning]
> **Using unordered pairs for dice**: Two dice have 36 equally likely outcomes $(1,1), (1,2), ..., (6,6)$, NOT 21!

> [!warning]
> **Forgetting empty set**: $\emptyset$ is always an event with $P(\emptyset)=0$

> [!warning]
> **Confusing union and intersection**: "Or" = union, "And" = intersection

---

## Memory Tricks

> [!tip]
> **De Morgan**: "Break the bar, flip the operation" - $\overline{A \cup B} = \bar{A} \cap \bar{B}$

> [!tip]
> **Partition**: Exhaustive + Disjoint = Partition

> [!tip]
> **Union formula**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ - don't double count overlap!

---

## Previous GATE Patterns

- **Sample space construction**: List outcomes for given experiment
- **Set operations**: Given $P(A), P(B), P(A \cap B)$, find $P(A \cup B)$ or $P(A^c)$
- **De Morgan's**: Apply to find probability of complements
- **Exhaustive/Mutually exclusive**: Identify if events form a partition

---

## Revision Summary

```
SAMPLE SPACE & EVENTS
├── Ω = all possible outcomes
├── Event = subset of Ω
├── Operations: ∪, ∩, ⁻ᶜ, \
├── De Morgan: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
├── Mutually exclusive: A ∩ B = ∅
├── Exhaustive: A₁ ∪ ... ∪ Aₙ = Ω
├── Partition: mutually exclusive + exhaustive
├── P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
└── Key: Choose sample space correctly (ordered for dice!)
```

---

## Related Notes

- [[01 Probability]]
- [[03 Counting Principles]]
- [[04 Permutations and Combinations]]
- [[05 Conditional Probability]]
- [[07 Independence]]

---

#probability #gate-da #sample-space #events #revision