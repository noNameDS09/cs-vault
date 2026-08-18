---
tags: [statistics, gate-da, sampling-distribution, revision]
---

# 38 Sampling Distribution

> [!note] The probability distribution of a statistic computed from a random sample.

---

## Overview

A sampling distribution is the probability distribution of a statistic (like sample mean or sample proportion) over all possible samples of a given size from a population. It's the bridge between sample statistics and population parameters.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Sampling Distribution** | Distribution of a statistic over all possible samples |
| **Standard Error** | Standard deviation of the sampling distribution |
| **Unbiased Estimator** | $E[\hat{\theta}] = \theta$ |

---

## Formulae

### Sampling Distribution of Sample Mean
If $X_1, ..., X_n$ i.i.d. with mean $\mu$, variance $\sigma^2$:
- $E[\bar{X}] = \mu$
- $Var(\bar{X}) = \frac{\sigma^2}{n}$
- $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$

### Central Limit Theorem (Approximation)
$$\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right) \text{ for large } n$$

### Exact Distribution (Normal Population)
If $X_i \sim N(\mu, \sigma^2)$ i.i.d.:
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{exact for any } n$$

### Sampling Distribution of Sample Variance (Normal Population)
$$\frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$$

### Sampling Distribution of Sample Proportion
$$\hat{p} = \frac{X}{n} \quad \text{where } X \sim Bin(n, p)$$
$$E[\hat{p}] = p, \quad Var(\hat{p}) = \frac{p(1-p)}{n}$$
$$\hat{p} \approx N\left(p, \frac{p(1-p)}{n}\right) \text{ for large } n$$

### t-Distribution (Unknown Variance)
$$\frac{\bar{X} - \mu}{s/\sqrt{n}} \sim t_{n-1} \quad \text{if } X_i \sim N(\mu, \sigma^2)$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\bar{X}$ | Sample mean |
| $s^2$ | Sample variance |
| $SE$ | Standard error |
| $\chi^2_{n-1}$ | Chi-square with $n-1$ df |
| $t_{n-1}$ | t-distribution with $n-1$ df |

---

## Important Properties

### Standard Error vs Standard Deviation
| | Population | Sample | Sampling Dist |
|---|---|---|---|
| **Mean** | $\mu$ | $\bar{x}$ | $\mu$ |
| **SD** | $\sigma$ | $s$ | $\sigma/\sqrt{n}$ |

### Unbiasedness
- $E[\bar{X}] = \mu$
- $E[s^2] = \sigma^2$
- $E[\hat{p}] = p$

### Consistency
As $n \to \infty$: $\bar{X} \xrightarrow{P} \mu$, $s^2 \xrightarrow{P} \sigma^2$, $\hat{p} \xrightarrow{P} p$

---

## GATE Tricks

> [!tip>
> **SE = σ/√n** (not σ/n!)
> **Normal population → exact normal** for sample mean
> **CLT → approximate normal** for any population (n large)
> **s² → χ²**: (n-1)s²/σ² ~ χ²_{n-1}
> **t = (x̄-μ)/(s/√n)** when σ unknown

---

## Common Mistakes

> [!warning>
> **σ/n instead of σ/√n** for standard error!
> **Confusing σ and s**: σ known → z, σ unknown → t
> **Forgetting CLT requires n large**: Not always exact!

---

## Memory Tricks

> [!tip>
> **SE** = **S**tandard **E**rror = σ/√n
> **Sampling distribution** = distribution of statistic over samples
> **Unbiased** = E[statistic] = parameter

---

## Previous GATE Patterns

- **SE calculation**: σ/√n
- **Distribution of sample mean**: Normal/t/CLT
- **Chi-square for variance**: (n-1)s²/σ²
- **Distribution of sample proportion**: Binomial/Normal approx

---

## Revision Summary

```
SAMPLING DISTRIBUTION
├── X̄: E=μ, Var=σ²/n, SE=σ/√n
├── Normal pop → exact N(μ, σ²/n)
├── CLT → approx N(μ, σ²/n) for any pop (n large)
├── s²: (n-1)s²/σ² ~ χ²_{n-1} (normal pop)
├── p̂: E=p, Var=p(1-p)/n
├── σ known → z, σ unknown → t
└── Key: SE = σ/√n, CLT for large n!
```

---

## Related Notes

- [[33 Central Limit Theorem]]
- [[36 Population and Sample]]
- [[37 Sampling Techniques]]
- [[39 Point Estimation]]
- [[47 Confidence Intervals]]
- [[48 z Test]]
- [[49 t Test]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #sampling-distribution #revision