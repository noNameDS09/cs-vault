---
tags: [statistics, gate-da, population-sample, revision]
---

# 36 Population and Sample

> [!note] Population = complete set of interest. Sample = subset selected for study.

---

## Overview

Understanding the distinction between population and sample is fundamental to statistics. All inferential statistics is about using sample information to make conclusions about the population.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Population** | Complete set of all items/individuals of interest |
| **Sample** | Subset of population selected for observation |
| **Census** | Study of entire population |
| **Sampling Frame** | List from which sample is drawn |

---

## Formulae

### Population Parameters
- **Mean**: $\mu = \frac{1}{N}\sum_{i=1}^N x_i$
- **Variance**: $\sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2$
- **Standard Deviation**: $\sigma = \sqrt{\sigma^2}$
- **Proportion**: $p = \frac{\text{# with characteristic}}{N}$

### Sample Statistics
- **Mean**: $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$
- **Variance**: $s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$
- **Standard Deviation**: $s = \sqrt{s^2}$
- **Proportion**: $\hat{p} = \frac{\text{# with characteristic}}{n}$

### Bessel's Correction
$$s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$$
Uses $n-1$ (degrees of freedom) instead of $n$ to make $s^2$ unbiased for $\sigma^2$.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $N$ | Population size |
| $n$ | Sample size |
| $\mu, \sigma^2$ | Population parameters |
| $\bar{x}, s^2$ | Sample statistics |
| $p, \hat{p}$ | Population/sample proportion |

---

## Important Properties

### Representativeness
A sample must be **representative** of the population for valid inference.

### Sampling Error
Difference between sample statistic and population parameter due to random sampling.

### Non-sampling Error
Errors not related to sampling (measurement error, non-response, etc.)

---

## Mathematical Intuition

**Population = Truth, Sample = Window**: We look through the window (sample) to infer the truth (population).

**Parameter = Fixed, Statistic = Random**: $\mu$ is fixed but unknown; $\bar{x}$ varies from sample to sample.

---

## Algorithms / Problem-Solving

### Population vs Sample
```
1. Identify population of interest
2. Identify sample drawn
3. Distinguish parameters (Greek) vs statistics (Latin)
4. Use sample to estimate parameters
5. Quantify uncertainty (standard error, CI)
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Parameter** = **P**opulation = **P**ermanent = Greek ($\mu, \sigma, p$)
> **Statistic** = **S**ample = **S**ummary = Latin ($\bar{x}, s, \hat{p}$)
> **Population variance** = divide by $N$
> **Sample variance** = divide by $n-1$ (Bessel's correction)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Population | Sample | All vs subset |
| Parameter | Statistic | Population vs sample characteristic |
| Census | Survey | All vs subset |
| $\sigma^2$ | $s^2$ | $1/N$ vs $1/(n-1)$ |

---

## Common Mistakes

> [!warning>
> **Using $N$ instead of $N-1$ for sample variance**: Biased!
> **Confusing parameter and statistic**: $\mu$ vs $\bar{x}$
> **Assuming sample = population**: Sample is only an estimate!

---

## Memory Tricks

> [!tip>
> **Parameter** = **P**opulation = **P** = Greek ($\mu, \sigma$)
> **Statistic** = **S**ample = **S** = Latin ($\bar{x}, s$)
> **Bessel** = **B**ias correction = $n-1$

---

## Previous GATE Patterns

- **Parameter vs Statistic**: Identify which is which
- **Variance formula**: $N$ vs $n-1$
- **Symbol identification**: Greek vs Latin letters

---

## Revision Summary

```
POPULATION & SAMPLE
├── Population: All items of interest (size N)
├── Sample: Subset studied (size n)
├── Parameter: Population characteristic (μ, σ, p) - Greek
├── Statistic: Sample characteristic (x̄, s, p̂) - Latin
├── Population variance: σ² = Σ(x-μ)²/N
├── Sample variance: s² = Σ(x-x̄)²/(n-1) (Bessel's correction)
└── Key: Sample estimates population!
```

---

## Related Notes

- [[35 Statistics]]
- [[37 Sampling Techniques]]
- [[38 Sampling Distribution]]
- [[39 Point Estimation]]
- [[55 Range Variance Standard Deviation]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #population-sample #revision