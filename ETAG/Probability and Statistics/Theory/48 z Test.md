---
tags: [statistics, gate-da, z-test, hypothesis-testing, revision]
---

# 48 z Test

> [!note] z-test uses standard normal distribution. Used when population standard deviation is known or sample size is large.

---

## Overview

The z-test is a hypothesis test that uses the standard normal distribution. It's appropriate when the population standard deviation is known, or when the sample size is large enough for the Central Limit Theorem to apply.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **z-test** | Test using standard normal distribution |
| **Standard Error** | $\sigma/\sqrt{n}$ (known) or $s/\sqrt{n}$ (large n) |
| **Test Statistic** | $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ |

---

## Formulae

### One-Sample z-Test (Mean)

**$\sigma$ known:**
$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)$$

**$\sigma$ unknown, large $n$ (CLT):**
$$z = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \approx N(0,1)$$

### Two-Sample z-Test (Means)

**Known variances:**
$$z = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

**Unknown, large samples:**
$$z = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

### One-Sample z-Test (Proportion)
$$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$

### Two-Sample z-Test (Proportions)
$$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$
where $\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$ (pooled proportion)

### Decision Rule
| Alternative | Reject $H_0$ if |
|-------------|-----------------|
| $H_1: \mu \neq \mu_0$ | $|z| > z_{\alpha/2}$ |
| $H_1: \mu > \mu_0$ | $z > z_{\alpha}$ |
| $H_1: \mu < \mu_0$ | $z < -z_{\alpha}$ |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $z$ | Test statistic |
| $z_{\alpha}$ | Upper $\alpha$ quantile of $N(0,1)$ |
| $\sigma$ | Population standard deviation |
| $s$ | Sample standard deviation |
| $\hat{p}$ | Sample proportion |

---

## Important Properties

### When to Use z-Test
1. Population normal, $\sigma$ known
2. Population normal, $n \geq 30$ (CLT)
3. Proportion tests with $np \geq 5, n(1-p) \geq 5$

### Relationship with CI
- Reject $H_0$ at level $\alpha$ iff $\mu_0$ not in $100(1-\alpha)\%$ CI

---

## GATE Tricks

> [!tip>
> **z-test**: $\sigma$ known OR large n ($n \geq 30$)
> **Test stat**: $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$
> **Proportion**: $z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}}$
> **Two-tailed**: compare $|z|$ with $z_{\alpha/2}$
> **One-tailed**: compare $z$ with $z_{\alpha}$

---

## Common Mistakes

> [!warning>
> **Using z when $\sigma$ unknown and n small**: Use t-test!
> **Using $z_{\alpha}$ instead of $z_{\alpha/2}$** for two-tailed
> **Confusing $\sigma$ and $s$**: Use correct one!

---

## Memory Tricks

> [!tip>
> **z** = **Z**ero-one = standard normal
> **z-test** = **Z** = standard normal test
> **z** = (estimate - hypothesized) / SE

---

## Previous GATE Patterns

- **One-sample mean**: Known/unknown $\sigma$, large/small n
- **Proportion test**: Single or two-sample
- **Decision**: Compare z with critical value or p-value

---

## Revision Summary

```
Z-TEST
├── One-sample mean: z = (x̄ - μ₀) / (σ/√n)
├── Two-sample means: z = (x̄₁ - x̄₂ - Δ) / √(σ₁²/n₁ + σ₂²/n₂)
├── Proportion: z = (p̂ - p₀) / √(p₀(1-p₀)/n)
├── Two-sample proportions: z = (p̂₁ - p̂₂) / √(p̂(1-p̂)(1/n₁ + 1/n₂))
├── σ known OR n ≥ 30
├── Two-tailed: |z| > z_{α/2}
├── One-tailed: z > z_α or z < -z_α
└── CI relationship: μ₀ in CI ↔ Fail to Reject
```

---

## Related Notes

- [[47 Confidence Intervals]]
- [[49 t Test]]
- [[33 Central Limit Theorem]]
- [[32 Standard Normal Distribution]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #z-test #hypothesis-testing #revision