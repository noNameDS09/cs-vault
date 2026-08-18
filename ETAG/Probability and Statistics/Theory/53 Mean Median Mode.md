---
tags: [statistics, gate-da, mean-median-mode, descriptive-statistics, revision]
---

# 53 Mean Median Mode

> [!note] Three measures of central tendency: mean (average), median (middle), mode (most frequent).

---

## Overview

Mean, median, and mode are the three main measures of central tendency. They describe the "center" of a dataset in different ways.

---

## Formulae

### Mean (Arithmetic Average)
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$

**Properties:**
- Affected by all values
- Sensitive to outliers
- $\sum (x_i - \bar{x}) = 0$

### Median
- Odd $n$: Middle value when ordered
- Even $n$: Average of two middle values

**Properties:**
- Robust to outliers
- 50th percentile ($Q_2$)
- Minimizes $\sum |x_i - m|$

### Mode
- Most frequently occurring value
- Can have multiple modes (bimodal, multimodal)
- Can be used for categorical data

### Relationship in Skewed Distributions
- Symmetric: Mean = Median = Mode
- Right-skewed: Mean > Median > Mode
- Left-skewed: Mean < Median < Mode

**Empirical Relationship (Moderately Skewed):**
$$\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\bar{x}$ | Mean |
| $M$ | Median |
| $Mo$ | Mode |
| $n$ | Number of observations |

---

## GATE Tricks

> [!tip>
> **Mean** = average (affected by outliers)
> **Median** = middle value (robust)
> **Mode** = most frequent (for categorical too)
> **Skewed right**: Mean > Median > Mode
> **Skewed left**: Mean < Median < Mode
> **Empirical**: Mode ≈ 3×Median - 2×Mean

---

## Common Mistakes

> [!warning>
> **Using mean for skewed data**: Median is better!
> **Forgetting to sort data** for median!
> **Mode can be multiple**: Don't assume unique!

---

## Memory Tricks

> [!tip>
> **Mean** = **M**ean = **M**iddle = average
> **Median** = **Med**ian = **Med**dle = middle
> **Mode** = **Mo**st frequent
> **Skewed right**: tail to right → mean pulled right

---

## Previous GATE Patterns

- **Compute mean/median/mode**: Given dataset
- **Skewness identification**: Mean vs median vs mode
- **Empirical relationship**: Given two, find third

---

## Revision Summary

```
MEAN, MEDIAN, MODE
├── Mean: Σx/n (affected by outliers)
├── Median: middle value (robust)
├── Mode: most frequent
├── Symmetric: Mean = Median = Mode
├── Right-skewed: Mean > Median > Mode
├── Left-skewed: Mean < Median < Mode
├── Empirical: Mode ≈ 3×Median - 2×Mean
└── Use median for skewed data!
```

---

## Related Notes

- [[52 Descriptive Statistics]]
- [[54 Quartiles and Percentiles]]
- [[55 Range Variance Standard Deviation]]
- [[56 Skewness and Kurtosis]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #mean-median-mode #descriptive-statistics #revision