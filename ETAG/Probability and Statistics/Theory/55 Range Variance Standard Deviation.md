---
tags: [statistics, gate-da, range-variance-sd, descriptive-statistics, revision]
---

# 55 Range Variance Standard Deviation

> [!note] Range, variance, and standard deviation are measures of dispersion (spread) in data.

---

## Overview

Measures of dispersion quantify how spread out the data is. They complement measures of central tendency by describing the variability.

---

## Formulae

### Range
$$R = \max(x) - \min(x) = x_{(n)} - x_{(1)}$$

### Variance
**Population:**
$$\sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2$$

**Sample (Bessel's Correction):**
$$s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$$

**Computational Formula:**
$$s^2 = \frac{1}{n-1}\left(\sum x_i^2 - n\bar{x}^2\right) = \frac{1}{n-1}\left(\sum x_i^2 - \frac{(\sum x_i)^2}{n}\right)$$

### Standard Deviation
$$\sigma = \sqrt{\sigma^2}, \quad s = \sqrt{s^2}$$

### Properties of Variance
- $Var(aX + b) = a^2 Var(X)$
- $Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)$
- If independent: $Var(X+Y) = Var(X) + Var(Y)$

### Coefficient of Variation
$$CV = \frac{s}{\bar{x}} \times 100\%$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $R$ | Range |
| $\sigma^2$ | Population variance |
| $s^2$ | Sample variance |
| $\sigma$ | Population SD |
| $s$ | Sample SD |
| $CV$ | Coefficient of variation |

---

## GATE Tricks

> [!tip>
> **Range** = max - min (simplest, sensitive to outliers)
> **Variance** = $s^2 = \frac{1}{n-1}\sum(x-\bar{x})^2$ (divide by n-1!)
> **SD** = $\sqrt{variance}$ (same units as data)
> **CV** = $s/\bar{x}$ (unit-free, compare variability across scales)

---

## Common Mistakes

> [!warning>
> **Using $n$ instead of $n-1$** for sample variance!
> **Range ignores all middle values**: Only uses min and max!
> **SD has same units as data**, variance has squared units!

---

## Memory Tricks

> [!tip>
> **Range** = max - min
> **Variance** = average squared deviation
> **SD** = **S**tandard **D**eviation = square root of variance
> **Bessel** = $n-1$ correction for sample

---

## Previous GATE Patterns

- **Compute variance/SD**: Given dataset
- **Identify formula**: Population vs sample
- **CV calculation**: Compare variability across datasets

---

## Revision Summary

```
RANGE, VARIANCE, STANDARD DEVIATION
├── Range = max - min
├── Population variance = Σ(x-μ)²/N
├── Sample variance = Σ(x-x̄)²/(n-1) (Bessel's correction)
├── SD = √variance
├── Range: sensitive to outliers
├── SD: same units as data
├── CV = s/x̄ (relative variability)
└── Key: Use n-1 for sample!
```

---

## Related Notes

- [[52 Descriptive Statistics]]
- [[53 Mean Median Mode]]
- [[54 Quartiles and Percentiles]]
- [[56 Skewness and Kurtosis]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #range-variance-sd #descriptive-statistics #revision