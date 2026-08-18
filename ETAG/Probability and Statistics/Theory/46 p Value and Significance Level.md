---
tags: [statistics, gate-da, p-value, significance-level, revision]
---

# 46 p Value and Significance Level

> [!note] p-value = probability of observing data as extreme as (or more extreme than) the observed data, assuming H₀ is true.

---

## Overview

The p-value is a measure of the strength of evidence against the null hypothesis. It quantifies how compatible the observed data are with the null hypothesis.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **p-value** | $P(\text{data as extreme or more} | H_0 \text{ true})$ |
| **Significance Level ($\alpha$)** | Threshold for rejecting $H_0$ |
| **Critical Value** | Test statistic value corresponding to $\alpha$ |

---

## Formulae

### p-value Calculation
| Test Type | p-value |
|-----------|---------|
| Right-tailed | $P(TS \geq ts_{obs} | H_0)$ |
| Left-tailed | $P(TS \leq ts_{obs} | H_0)$ |
| Two-tailed | $2 \times P(TS \geq |ts_{obs}| | H_0)$ |

### Decision Rule
- **Reject $H_0$** if $p\text{-value} < \alpha$
- **Fail to Reject $H_0$** if $p\text{-value} \geq \alpha$

### Relationship with Critical Value
- Reject $H_0$ if $|TS| > CV$ (two-tailed)
- Equivalent to $p < \alpha$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | p-value |
| $\alpha$ | Significance level |
| $TS$ | Test statistic |
| $CV$ | Critical value |

---

## Important Properties

### p-value Interpretation
- **Small p-value**: Strong evidence against $H_0$
- **Large p-value**: Weak evidence against $H_0$
- $p = 0.03$: If $H_0$ true, would see such extreme data only 3% of the time

### What p-value IS NOT
- **NOT** $P(H_0 \text{ true} | \text{data})$
- **NOT** probability $H_0$ is true
- **NOT** probability results are due to chance

### Significance Level $\alpha$
- Pre-determined threshold (usually 0.05, 0.01, 0.10)
- $\alpha = P(\text{Type I Error})$
- Chosen BEFORE collecting data

---

## GATE Tricks

> [!tip>
> **p-value < α → Reject H₀**
> **p-value ≥ α → Fail to Reject H₀**
> **p-value** = probability of data THIS extreme if H₀ true
> **α** = pre-chosen threshold
> **Two-tailed**: p-value = 2 × tail probability

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| p-value | α | Data-dependent vs pre-specified |
| p-value | $P(H_0 | data)$ | p-value = $P(data | H_0)$, not $P(H_0 | data)$ |
| One-tailed p | Two-tailed p | Two-tailed = 2 × one-tailed |

---

## Common Mistakes

> [!warning>
> **Interpreting p as P(H₀ true)**: WRONG! p = P(data | H₀), not P(H₀ | data)!
> **p = 0.051 vs 0.049**: Binary thinking at α=0.05 is wrong!
> **Saying "p = probability H₀ true"**: WRONG!
> **Reporting only "p < 0.05"**: Report exact p-value!

---

## Memory Tricks

> [!tip>
> **p-value** = **p**robability of data if H₀ true
> **α** = **A**lpha = **A**lready chosen threshold
> **p < α** = **R**eject (small p = strong evidence)
> **Two-tailed** = **T**wo **T**ails = multiply by 2

---

## Previous GATE Patterns

- **Compute p-value**: Given test statistic, find p
- **Decision**: p-value vs α
- **Interpretation**: What does p-value mean?
- **Two-tailed p-value**: Multiply one-tailed by 2

---

## Revision Summary

```
p-VALUE & SIGNIFICANCE LEVEL
├── p = P(data as extreme | H₀ true)
├── α = pre-chosen threshold (usually 0.05)
├── p < α → Reject H₀
├── p ≥ α → Fail to Reject H₀
├── Two-tailed p = 2 × one-tailed
├── p ≠ P(H₀ true | data)!
├── Exact p-value > binary decision
└── Key: p < α → Reject H₀
```

---

## Related Notes

- [[43 Hypothesis Testing]]
- [[44 Null and Alternative Hypothesis]]
- [[45 Type I and Type II Errors]]
- [[48 z Test]]
- [[49 t Test]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #p-value #significance-level #revision