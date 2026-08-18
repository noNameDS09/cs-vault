---
tags: [probability, gate-da, permutations, combinations, revision]
---

# 04 Permutations and Combinations

> [!note] Permutations = ordered arrangements. Combinations = unordered selections.

---

## Overview

Permutations and combinations are the two fundamental ways to count selections from a set. The key difference: **Does order matter?**

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Permutation** | Arrangement of objects where ORDER matters |
| **Combination** | Selection of objects where ORDER doesn't matter |
| **Without Replacement** | Object cannot be chosen again |
| **With Replacement** | Object can be chosen multiple times |
| **Multiset** | Selection with repetition allowed (order doesn't matter) |

---

## Formulae

### Permutations (Without Replacement)
$$^nP_r = \frac{n!}{(n-r)!} = n(n-1)...(n-r+1)$$
- Arrange $r$ objects from $n$ distinct objects
- $^nP_n = n!$ (arrange all)

### Combinations (Without Replacement)
$$^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$
- Choose $r$ objects from $n$ distinct objects
- Properties:
  - $^nC_r = ^nC_{n-r}$
  - $\sum_{r=0}^n \binom{n}{r} = 2^n$
  - Pascal's Identity: $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$

### With Replacement
| Type | Formula |
|------|---------|
| Permutations with replacement | $n^r$ |
| Combinations with replacement (Multiset) | $\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$ |

### Arrangements with Repeated Objects
If $n$ objects with $n_1$ identical of type 1, $n_2$ of type 2, ..., $n_k$ of type k:
$$\frac{n!}{n_1! n_2! ... n_k!}$$

### Circular Permutations
- Distinct objects around a circle (clockwise ≠ anticlockwise): $(n-1)!$
- Necklace/Bracelet (reflections same): $\frac{(n-1)!}{2}$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Total distinct objects |
| $r$ | Number selected/arranged |
| $n_i$ | Number of identical objects of type $i$ |

---

## Important Properties

### Combinatorial Identities
- $\binom{n}{0} = \binom{n}{n} = 1$
- $\binom{n}{1} = \binom{n}{n-1} = n$
- $\binom{n}{r} = \binom{n}{n-r}$
- **Vandermonde's Identity**: $\binom{m+n}{r} = \sum_{k=0}^r \binom{m}{k}\binom{n}{r-k}$
- **Hockey Stick**: $\sum_{i=r}^n \binom{i}{r} = \binom{n+1}{r+1}$

---

## Mathematical Intuition

**Permutations**: Each position has one fewer choice. $n$ choices for first, $(n-1)$ for second, etc.

**Combinations**: Each unordered selection corresponds to $r!$ permutations. So divide by $r!$.

**Stars and Bars** (Multiset): $n$ types, $r$ selections. Represent as $r$ stars and $n-1$ bars separating types.

---

## Algorithms / Problem-Solving

### Decision Tree
```
1. Does ORDER matter?
   YES → Permutation
   NO → Combination

2. With REPLACEMENT?
   YES → n^r (perm) or C(n+r-1, r) (comb)
   NO → n!/(n-r)! (perm) or C(n, r) (comb)

3. Any REPEATED/IDENTICAL objects?
   YES → Divide by factorials of identical counts

4. CIRCULAR arrangement?
   YES → (n-1)! or (n-1)!/2
```

---

## Complexity
Not applicable for combinatorial formulas.

---

## Comparison Tables

### Quick Reference

| Scenario | Formula | Example |
|----------|---------|---------|
| Arrange $r$ of $n$ distinct | $^nP_r$ | Passwords, rankings |
| Choose $r$ of $n$ distinct | $^nC_r$ | Committees, teams |
| With replacement, order | $n^r$ | Dice rolls, codes |
| With replacement, no order | $\binom{n+r-1}{r}$ | Ice cream scoops |
| Repeated objects | $\frac{n!}{n_1!...n_k!}$ | MISSISSIPPI |
| Circular (distinct) | $(n-1)!$ | Seating at round table |
| Necklace | $(n-1)!/2$ | Bracelet arrangements |

---

## GATE Tricks

> [!tip]
> **Permutation** = **Perm**ute = **Order Matters**
> **Combination** = **Com**bine = **Order Doesn't Matter**

> [!tip]
> **$^nC_r = ^nC_{n-r}$**: Choosing $r$ to include = choosing $n-r$ to exclude

> [!tip]
> **Sum of combinations**: $\sum_{r=0}^n \binom{n}{r} = 2^n$ (all subsets)

> [!tip]
> **Gap Method**: No two adjacent = arrange others first, choose gaps

> [!tip]
> **Complementary Counting**: At least one = Total - None

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Permutation | Combination | Order matters vs. doesn't |
| With replacement | Without replacement | $n^r$ vs $^nP_r$ |
| Circular | Linear | $(n-1)!$ vs $n!$ |
| Multiset | Combination | Repetition allowed vs not |

---

## Common Mistakes

> [!warning]
> **Using $n^r$ for without-replacement**: $n^r$ assumes replacement!

> [!warning]
> **Forgetting identical objects**: MISSISSIPPI = $\frac{11!}{4!4!2!}$ not $11!$

> [!warning]
> **Circular vs Linear**: Round table uses $(n-1)!$, not $n!$

> [!warning]
> **Necklace**: If flipping doesn't create new, divide by 2!

---

## Memory Tricks

> [!tip]
> **P**ermutation = **P**osition matters = Ordered
> **C**ombination = **C**hoose = Unordered

> [!tip]
> **Stars & Bars**: $\binom{n+r-1}{r}$ = $r$ stars + $n-1$ bars

> [!tip]
> **Vandermonde**: $\binom{m+n}{r} = \sum \binom{m}{k}\binom{n}{r-k}$

---

## Previous GATE Patterns

- **Password/Code formation**: Permutations with/without replacement
- **Committee selection**: Combinations
- **Arrangements with restrictions**: Vowels together, no two adjacent
- **Repeated letters**: MISSISSIPPI, BANANA type problems
- **Circular seating**: Round table arrangements
- **Stars and bars**: Distribution of identical objects

---

## Revision Summary

```
PERMUTATIONS & COMBINATIONS
├── Permutation (order): ⁿPᵣ = n!/(n-r)!
├── Combination (no order): ⁿCᵣ = n!/(r!(n-r)!)
├── With replacement: nʳ or C(n+r-1, r)
├── Identical objects: n!/(n₁!n₂!...nₖ!)
├── Circular: (n-1)! or (n-1)!/2
├── Key identities: ⁿCᵣ = ⁿCₙ₋ᵣ, ΣⁿCᵣ = 2ⁿ
├── Gap method: No adjacent = choose gaps
└── Complementary: At least one = Total - None
```

---

## Related Notes

- [[03 Counting Principles]]
- [[01 Probability]]
- [[02 Sample Space and Events]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #permutations #combinations #revision