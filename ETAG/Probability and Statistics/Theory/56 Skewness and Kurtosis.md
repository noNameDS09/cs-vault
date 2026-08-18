---
tags: [statistics, gate-da, skewness-kurtosis, descriptive-statistics, revision]
---

# 56 Skewness and Kurtosis

> [!note] Skewness measures asymmetry. Kurtosis measures tail heaviness.

---

## Overview

Skewness and kurtosis are measures of the shape of a distribution. Skewness indicates asymmetry, while kurtosis indicates the heaviness of tails relative to a normal distribution.

---

## Formulae

### Skewness
$$\gamma_1 = \frac{n}{(n-1)(n-2)} \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^3$$

**Population Skewness:**
$$\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}$$

**Interpretation:**
- $\gamma_1 > 0$: Right-skewed (positive skew)
- $\gamma_1 = 0$: Symmetric
- $\gamma_1 < 0$: Left-skewed (negative skew)

### Kurtosis (Excess Kurtosis)
$$\gamma_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}$$

**Population Kurtosis:**
$$\gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$$

**Interpretation:**
- $\gamma_2 > 0$: Leptokurtic (heavy tails, more outliers)
- $\gamma_2 = 0$: Mesokurtic (normal-like tails)
- $\gamma_2 < 0$: Platykurtic (light tails, fewer outliers)

### Sample Formulas (Alternative)
**Skewness:**
$$g_1 = \frac{\frac{1}{n}\sum (x_i - \bar{x})^3}{\left(\frac{1}{n}\sum (x_i - \bar{x})^2\right)^{3/2}}$$

**Kurtosis:**
$$g_2 = \frac{\frac{1}{n}\sum (x_i - \bar{x})^4}{\left(\frac{1}{n}\sum (x_i - \bar{x})^2\right)^2} - 3$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\gamma_1$ | Skewness |
| $\gamma_2$ | Excess kurtosis |
| $s$ | Sample standard deviation |

---

## GATE Tricks

> [!tip>
> **Skewness** = asymmetry (right/left tail)
> **Kurtosis** = tail heaviness (outliers)
> **Right-skewed**: tail to right, Mean > Median
> **Left-skewed**: tail to left, Mean < Median
> **Kurtosis > 0**: heavy tails, more outliers
> **Kurtosis < 0**: light tails, fewer outliers
> **Normal**: Skewness = 0, Kurtosis = 0

---

## Common Mistakes

> [!warning>
> **Confusing skewness direction**: Right-skewed = tail on RIGHT
> **Kurtosis vs Variance**: Kurtosis = tail shape, not spread!
> **Excess kurtosis**: Normal has excess kurtosis = 0 (not 3!)

---

## Memory Tricks

> [!tip>
> **Skew** = **S**kew = **S**lant = asymmetry
> **Kurtosis** = **Cur**tosis = **Cur**vature = tails
> **Right skew** = **R**ight tail = Mean > Median
> **Lepto** = **Le**avy tails
> **Platy** = **Pl**at = flat = light tails

---

## Previous GATE Patterns

- **Identify skewness**: Given mean, median, mode
- **Identify kurtosis**: Heavy/light tails
- **Compute sample skewness/kurtosis**: Given moments

---

## Revision Summary

```
SKEWNESS & KURTOSIS
├── Skewness = E[(X-μ)³]/σ³
├── γ₁ > 0: Right-skewed (Mean > Median)
├── γ₁ < 0: Left-skewed (Mean < Median)
├── γ₁ = 0: Symmetric
├── Kurtosis (excess) = E[(X-μ)⁴]/σ⁴ - 3
├── γ₂ > 0: Heavy tails (leptokurtic)
├── γ₂ < 0: Light tails (platykurtic)
├── γ₂ = 0: Normal-like (mesokurtic)
└── Normal: Skew=0, Excess Kurtosis=0
```

---

## Related Notes

- [[52 Descriptive Statistics]]
- [[53 Mean Median Mode]]
- [[55 Range Variance Standard Deviation]]
- [[31 Normal Distribution]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #skewness-kurtosis #descriptive-statistics #revision