---
tags: [statistics, gate-da, quartiles, percentiles, revision]
---

# 54 Quartiles and Percentiles

> [!note] Quartiles divide data into four equal parts. Percentiles divide data into 100 equal parts.

---

## Overview

Quartiles and percentiles are measures of position that describe the relative standing of values within a dataset.

---

## Formulae

### Quartiles
- **Q₁ (First Quartile)**: 25th percentile
- **Q₂ (Second Quartile)**: 50th percentile = Median
- **Q₃ (Third Quartile)**: 75th percentile

### Percentiles
$P_k$ = value below which $k\%$ of data falls

**Position Formula:**
$$\text{Position} = \frac{k}{100} \times (n + 1)$$
If not integer, interpolate between adjacent values.

### Interquartile Range (IQR)
$$IQR = Q_3 - Q_1$$

### Outlier Detection (Tukey's Fences)
- Lower fence: $Q_1 - 1.5 \times IQR$
- Upper fence: $Q_3 + 1.5 \times IQR$
- Values outside fences = outliers

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $Q_1$ | First quartile (25th percentile) |
| $Q_2$ | Second quartile = Median |
| $Q_3$ | Third quartile (75th percentile) |
| $P_k$ | $k$-th percentile |
| $IQR$ | Interquartile range |

---

## GATE Tricks

> [!tip>
> **Q₁** = 25th percentile, **Q₂** = Median, **Q₃** = 75th percentile
> **IQR** = Q₃ - Q₁
> **Outliers**: Q₁ - 1.5×IQR, Q₃ + 1.5×IQR
> **Percentile position**: k/100 × (n+1)

---

## Common Mistakes

> [!warning>
> **Not sorting data** before finding quartiles!
> **Different methods**: Some use (n+1), some use n/4, etc.
> **Q₂ ≠ Mean** unless symmetric!

---

## Memory Tricks

> [!tip>
> **Quartile** = **Quart** = quarter = 4 parts
> **Percentile** = **Per**cent = 100 parts
> **IQR** = Q₃ - Q₁ = middle 50%

---

## Previous GATE Patterns

- **Find Q₁, Q₂, Q₃**: Given dataset
- **IQR calculation**: Q₃ - Q₁
- **Outlier detection**: Tukey's fences
- **Percentile calculation**: Given k, find value

---

## Revision Summary

```
QUARTILES & PERCENTILES
├── Q₁ = 25th percentile
├── Q₂ = Median = 50th percentile
├── Q₃ = 75th percentile
├── IQR = Q₃ - Q₁
├── Position = k/100 × (n+1)
├── Outliers: Q₁ - 1.5×IQR, Q₃ + 1.5×IQR
└── Key: Q₂ = Median, IQR = middle 50%
```

---

## Related Notes

- [[53 Mean Median Mode]]
- [[55 Range Variance Standard Deviation]]
- [[56 Skewness and Kurtosis]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #quartiles #percentiles #revision