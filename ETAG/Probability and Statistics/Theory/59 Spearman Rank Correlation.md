---
tags: [statistics, gate-da, spearman-correlation, revision]
---

# 59 Spearman Rank Correlation

> [!note] Spearman rank correlation measures monotonic relationship using ranks instead of raw values.

---

## Overview

Spearman rank correlation (ρ_s or r_s) is a non-parametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function.

---

## Formulae

### Spearman Rank Correlation
For ranks $R_X$ and $R_Y$:
$$r_s = \frac{\sum (R_{X_i} - \bar{R}_X)(R_{Y_i} - \bar{R}_Y)}{\sqrt{\sum (R_{X_i} - \bar{R}_X)^2 \sum (R_{Y_i} - \bar{R}_Y)^2}}$$

### Simplified Formula (No Tied Ranks)
$$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$
where $d_i = R_{X_i} - R_{Y_i}$ (difference in ranks)

### With Tied Ranks
Use Pearson correlation on ranks:
$$r_s = \frac{\sum (R_{X_i} - \bar{R}_X)(R_{Y_i} - \bar{R}_Y)}{\sqrt{\sum (R_{X_i} - \bar{R}_X)^2 \sum (R_{Y_i} - \bar{R}_Y)^2}}$$

### Properties
- $-1 \leq r_s \leq 1$
- $r_s = 1$: Perfect monotonic increasing
- $r_s = -1$: Perfect monotonic decreasing
- $r_s = 0$: No monotonic relationship

### Hypothesis Test for $\rho_s = 0$
For $n \geq 10$:
$$t = r_s \sqrt{\frac{n-2}{1 - r_s^2}} \sim t_{n-2}$$

For small $n$: Use critical value tables.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $r_s$ | Sample Spearman rank correlation |
| $d_i$ | Difference in ranks |
| $R_{X_i}$ | Rank of $X_i$ |

---

## GATE Tricks

> [!tip>
> **No ties**: $r_s = 1 - \frac{6\sum d_i^2}{n(n^2-1)}$
> **With ties**: Use Pearson on ranks
> **Monotonic**: Captures non-linear but monotonic relationships
> **Test**: $t = r_s\sqrt{\frac{n-2}{1-r_s^2}}$ for $n \geq 10$

---

## Common Mistakes

> [!warning>
> **Using formula without ties when ties exist**: Use Pearson on ranks!
> **Confusing with Pearson**: Pearson = linear, Spearman = monotonic
> **Assuming normal distribution needed**: Non-parametric!

---

## Memory Tricks

> [!tip>
> **Spearman** = **Spear**man = **Spear** = rank = non-parametric
> **$\sum d^2$** = sum of squared rank differences
> **6∑d²/(n³-n)** = easy formula for no ties

---

## Previous GATE Patterns

- **Compute r_s**: Given paired data, rank and compute
- **Tied ranks**: Use Pearson on ranks
- **Significance test**: t = r_s√((n-2)/(1-r_s²))

---

## Revision Summary

```
SPEARMAN RANK CORRELATION
├── Non-parametric: uses ranks, not raw values
├── Measures MONOTONIC relationship
├── No ties: r_s = 1 - 6∑d_i²/(n(n²-1))
├── With ties: Pearson on ranks
├── Captures monotonic (not just linear)
├── Test H₀: ρ_s = 0: t = r_s√((n-2)/(1-r_s²)) ~ t_{n-2}
├── Non-parametric = no normality assumption
└── Key: Spearman = monotonic, Pearson = linear!
```

---

## Related Notes

- [[57 Covariance and Correlation]]
- [[58 Pearson Correlation]]
- [[60 Simple Linear Regression Statistics]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #spearman-correlation #revision