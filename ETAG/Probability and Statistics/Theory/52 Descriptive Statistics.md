---
tags: [statistics, gate-da, descriptive-statistics, revision]
---

# 52 Descriptive Statistics

> [!note] Descriptive statistics summarize and describe the main features of a dataset.

---

## Overview

Descriptive statistics provide simple summaries about the sample and the measures. They form the basis for virtually every quantitative analysis of data.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Central Tendency** | Typical/central value (mean, median, mode) |
| **Dispersion/Variability** | Spread of data (range, variance, SD, IQR) |
| **Shape** | Distribution shape (skewness, kurtosis) |
| **Outliers** | Extreme values that differ significantly |

---

## Formulae

### Central Tendency

**Mean (Arithmetic):**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$

**Weighted Mean:**
$$\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$$

**Median:**
- Odd $n$: Middle value
- Even $n$: Average of two middle values

**Mode:** Most frequent value

**Geometric Mean:**
$$\text{GM} = \left(\prod_{i=1}^n x_i\right)^{1/n} = e^{\frac{1}{n}\sum \ln x_i}$$

**Harmonic Mean:**
$$\text{HM} = \frac{n}{\sum_{i=1}^n \frac{1}{x_i}}$$

**Relationship:** HM ≤ GM ≤ AM (for positive numbers)

### Dispersion

**Range:**
$$R = x_{(n)} - x_{(1)}$$

**Variance (Sample):**
$$s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$$

**Standard Deviation:**
$$s = \sqrt{s^2}$$

**Interquartile Range (IQR):**
$$IQR = Q_3 - Q_1$$

**Mean Absolute Deviation (MAD):**
$$\text{MAD} = \frac{1}{n}\sum |x_i - \bar{x}|$$

**Coefficient of Variation:**
$$CV = \frac{s}{\bar{x}} \times 100\%$$

### Shape

**Skewness:**
$$\gamma_1 = \frac{n}{(n-1)(n-2)} \sum \left(\frac{x_i - \bar{x}}{s}\right)^3$$

**Kurtosis (Excess):**
$$\gamma_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum \left(\frac{x_i - \bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Sample size |
| $\bar{x}$ | Sample mean |
| $s$ | Sample standard deviation |
| $s^2$ | Sample variance |
| $Q_1, Q_2, Q_3$ | Quartiles |

---

## GATE Tricks

> [!tip>
> **Mean** = average, **Median** = middle, **Mode** = most frequent
> **Variance** = $s^2$ (divide by $n-1$ for sample)
> **SD** = $\sqrt{variance}$
> **IQR** = $Q_3 - Q_1$ (robust to outliers)
> **CV** = $s/\bar{x}$ (unit-free variability measure)

---

## Common Mistakes

> [!warning>
> **Using $n$ instead of $n-1$** for sample variance!
> **Confusing population and sample formulas**
> **Mean ≠ Median in skewed distributions**
> **Outliers affect mean/SD, not median/IQR**

---

## Memory Tricks

> [!tip>
> **Mean** = **M**ean = **M**iddle = average
> **Median** = **Med**ian = **Med**dle = middle
> **Mode** = **Mo**st frequent
> **IQR** = **I**nter**q**uartile **R**ange = $Q_3-Q_1$

---

## Revision Summary

```
DESCRIPTIVE STATISTICS
├── Central Tendency: Mean, Median, Mode
├── Mean = Σx/n, Median = middle, Mode = most frequent
├── Dispersion: Range, IQR, Variance, SD
├── Variance: s² = Σ(x-x̄)²/(n-1)
├── SD = √variance
├── IQR = Q₃ - Q₁ (robust)
├── Skewness: asymmetry
├── Kurtosis: tail heaviness
└── CV = s/x̄ (relative variability)
```

---

## Related Notes

- [[53 Mean Median Mode]]
- [[54 Quartiles and Percentiles]]
- [[55 Range Variance Standard Deviation]]
- [[56 Skewness and Kurtosis]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #descriptive-statistics #revision