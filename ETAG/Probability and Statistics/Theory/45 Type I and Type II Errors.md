---
tags: [statistics, gate-da, hypothesis-testing, type-i-error, type-ii-error, revision]
---

# 45 Type I and Type II Errors

> [!note] Type I error = rejecting true null hypothesis. Type II error = failing to reject false null hypothesis.

---

## Overview

In hypothesis testing, there are two types of errors we can make. Understanding these errors and their probabilities is crucial for designing tests and interpreting results.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Type I Error** | Reject $H_0$ when $H_0$ is true |
| **Type II Error** | Fail to reject $H_0$ when $H_0$ is false |
| **Significance Level ($\alpha$)** | $P(\text{Type I Error})$ |
| **Power** | $1 - \beta = P(\text{Reject } H_0 | H_1 \text{ true})$ |

---

## Formulae

### Error Probabilities
| Decision \ Reality | $H_0$ True | $H_0$ False |
|--------------------|------------|-------------|
| **Reject $H_0$** | **Type I Error** ($\alpha$) | **Correct** (Power = $1-\beta$) |
| **Fail to Reject $H_0$** | **Correct** ($1-\alpha$) | **Type II Error** ($\beta$) |

### Probabilities
$$\alpha = P(\text{Reject } H_0 | H_0 \text{ true})$$
$$\beta = P(\text{Fail to Reject } H_0 | H_0 \text{ false})$$
$$\text{Power} = 1 - \beta = P(\text{Reject } H_0 | H_1 \text{ true})$$

### Relationship
- $\alpha$ is chosen by researcher (typically 0.05)
- $\beta$ depends on: effect size, sample size, $\alpha$, variability
- For fixed $n$, decreasing $\alpha$ increases $\beta$ (trade-off)

### Factors Affecting Power
1. **Sample size $n$**: Larger $n$ → higher power
2. **Effect size**: Larger effect → higher power
3. **Significance level $\alpha$**: Larger $\alpha$ → higher power
4. **Variability**: Less variability → higher power
5. **One-tailed vs two-tailed**: One-tailed has more power for same $\alpha$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\alpha$ | Type I error probability (significance level) |
| $\beta$ | Type II error probability |
| $1-\beta$ | Power |
| $1-\alpha$ | Confidence level |

---

## Important Properties

### Trade-offs
- $\alpha \downarrow \implies \beta \uparrow$ (for fixed $n$)
- $n \uparrow \implies \beta \downarrow$ (for fixed $\alpha$)
- Effect size $\uparrow \implies \beta \downarrow$

### Controlling Errors
- $\alpha$ is directly controlled by researcher
- $\beta$ is controlled indirectly via sample size, effect size, $\alpha$

---

## Mathematical Intuition

**Type I = False Alarm**: Fire alarm rings when there's no fire.

**Type II = Missed Detection**: Fire alarm fails to ring when there IS a fire.

**Power = Sensitivity**: Ability to detect an effect when it exists.

---

## Algorithms / Problem-Solving

### Choosing $\alpha$ and Sample Size
```
1. Decide acceptable α (usually 0.05)
2. Determine desired power (usually 0.8 or 0.9)
3. Estimate effect size from prior studies
4. Calculate required sample size
5. If n too large, may need to adjust α or power
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Type I** = **F**alse **P**ositive (reject true H₀)
> **Type II** = **F**alse **N**egative (miss false H₀)
> **α** = **P**robability of Type I
> **β** = **P**robability of Type II
> **Power** = 1 - β = 1 - Type II
> **Trade-off**: α ↓ → β ↑ (for fixed n)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $\alpha$ | $\beta$ | P(Type I) vs P(Type II) |
| Type I | Type II | Reject true vs fail to reject false |
| Power | $1-\alpha$ | Power = 1-β, Confidence = 1-α |

---

## Common Mistakes

> [!warning>
> **Confusing $\alpha$ and $\beta$**: $\alpha$ = P(Type I), $\beta$ = P(Type II)!
> **Saying "Accept H₀"**: Never accept, only fail to reject!
> **Confusing Power and Confidence**: Power = 1-β, Confidence = 1-α
> **Thinking low β is always possible**: Need large n!

---

## Memory Tricks

> [!tip>
> **Type I** = **F**alse **P**ositive = "I" (1st) = Reject true
> **Type II** = **F**alse **N**egative = "II" (2nd) = Miss false
> **α** = **A**lpha = **A**larm (false alarm)
> **β** = **B**eta = **B**lind (miss it)
> **Power** = **P**ower = **P**erformance = 1-β

---

## Previous GATE Patterns

- **Identify error type**: Given scenario, which error?
- **Relationship**: α vs β trade-off
- **Power calculation**: Given effect size, n, α, find power
- **Sample size**: Given desired power, find n

---

## Revision Summary

```
TYPE I & TYPE II ERRORS
├── Type I (α): Reject H₀ when true = False Positive
├── Type II (β): Fail to reject H₀ when false = False Negative
├── Power = 1-β = P(Reject | H₁ true)
├── α controlled directly, β controlled indirectly
├── Trade-off: α↓ → β↑ (fixed n), n↑ → β↓
├── Power ↑ with: n↑, effect↑, α↑, variability↓
└── Key: α = P(Type I), β = P(Type II), Power = 1-β
```

---

## Related Notes

- [[43 Hypothesis Testing]]
- [[44 Null and Alternative Hypothesis]]
- [[46 p Value and Significance Level]]
- [[46 p Value and Significance Level]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #type-i-error #type-ii-error #revision