---
tags: [probability, gate-da, counting, revision]
---

# 03 Counting Principles

> [!note] Counting techniques to determine number of outcomes without listing them all.

---

## Overview

Counting principles provide systematic ways to calculate the number of possible outcomes in complex scenarios. Essential for computing probabilities when outcomes are equally likely.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Fundamental Counting Principle** | Multiply choices at each step |
| **Factorial** | $n! = n \times (n-1) \times ... \times 1$ |
| **Permutations** | Arrangements where ORDER matters |
| **Combinations** | Selections where ORDER doesn't matter |
| **With/Without Replacement** | Affects available choices |

---

## Formulae

### Fundamental Counting Principle
If there are $n_1$ ways to do step 1, $n_2$ ways to do step 2, ..., $n_k$ ways to do step $k$:
$$\text{Total ways} = n_1 \times n_2 \times ... \times n_k$$

### Factorial
$$n! = n \times (n-1) \times ... \times 2 \times 1$$
$$0! = 1$$

### Factorial Approximation (Stirling's Formula)
$$n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Total number of items |
| $r$ | Number of items selected |
| $n!$ | n factorial |
| $k$ | Number of steps/choices |

---

## Important Properties

### Multiplication Rule
Sequential independent choices multiply.

### Addition Rule
Mutually exclusive choices add.

### Complementary Counting
$$\text{Wanted count} = \text{Total} - \text{Unwanted}$$

---

## Mathematical Intuition

**Fundamental Principle**: For each choice at step 1, you have all choices at step 2. Creates a Cartesian product of choice sets.

**Factorial**: Number of ways to arrange $n$ distinct objects in a line.

---

## Algorithms / Problem-Solving

### Counting Strategy
```
1. Identify if order matters (permutation) or not (combination)
2. Identify if with or without replacement
4. Apply appropriate formula
5. Check for restrictions (adjacent, together, etc.)
6. Use complementary counting if direct is hard
```

---

## Complexity
Not applicable for counting formulas.

---

## Comparison Tables

### When to Use What

| Scenario | Formula | Key Phrase |
|----------|---------|------------|
| Arrange $r$ of $n$ distinct | $^nP_r = \frac{n!}{(n-r)!}$ | "Order matters" |
| Arrange all $n$ distinct | $n!$ | "Arrange all" |
| Choose $r$ of $n$ distinct | $^nC_r = \frac{n!}{r!(n-r)!}$ | "Choose/select" |
| With repetition, order matters | $n^r$ | "With replacement" |
| With repetition, order doesn't matter | $\binom{n+r-1}{r}$ | "Multiset/identical objects" |

---

## GATE Tricks

> [!tip]
> **Multiplication for sequence**: Step 1 × Step 2 × ...

> [!tip]
> **Complementary counting**: "At least one" = Total - None

> [!tip]
> **Gap method**: Arrange unrestricted items first, then place restricted in gaps

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Permutation | Combination | Order matters vs doesn't matter |
| With replacement | Without replacement | Choices reset vs decrease |
| $n^r$ | $^nP_r$ | Repetition allowed vs not |

---

## Common Mistakes

> [!warning]
> **Using permutations when combinations needed**: "Select committee" = combination, "Assign roles" = permutation

> [!warning]
> **Forgetting $0! = 1$**: Critical for edge cases

> [!warning]
> **Order confusion**: "Password" = permutation (order matters), "Pizza toppings" = combination

---

## Memory Tricks

> [!tip]
> **Permutation** = **Perm**ute = change order = Order Matters
> **Combination** = **Com**bine = mix together = Order Doesn't Matter

---

## Previous GATE Patterns

- **Simple multiplication**: Number of ways to form passwords, codes
- **Permutations**: Arrangements with restrictions
- **Combinations**: Committee selection, team formation
- **Complementary**: At least one defective, at least one match

---

## Revision Summary

```
COUNTING PRINCIPLES
├── Fundamental: n₁ × n₂ × ... × nₖ
├── Factorial: n! = n×(n-1)×...×1, 0! = 1
├── Permutation (order): ⁿPᵣ = n!/(n-r)!
├── Combination (no order): ⁿCᵣ = n!/(r!(n-r)!)
├── With replacement: nʳ
├── Stars & Bars: (n+r-1 choose r)
├── Complementary: Total - Unwanted
└── Key: Order matters?
```

---

## Related Notes

- [[02 Sample Space and Events]]
- [[04 Permutations and Combinations]]
- [[01 Probability]]

---

#probability #gate-da #counting #revision