---
tags: [statistics, gate-da, confidence-intervals, revision]
---

# 47 Confidence Intervals

> [!note] Confidence interval provides a range of plausible values for a parameter with a specified confidence level.

---

## Overview

A confidence interval (CI) gives a range of plausible values for a population parameter, along with a confidence level indicating the reliability of the estimation method.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Confidence Interval** | Range of plausible values for parameter |
| **Confidence Level** | $1-\alpha$ = long-run proportion of CIs containing true parameter |
| **Margin of Error** | Half-width of CI |
| **Significance Level** | $\alpha$ = probability CI misses parameter |

---

## Formulae

### Confidence Interval for Mean

**$\sigma$ known (z-interval):**
$$\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**$\sigma$ unknown, normal population (t-interval):**
$$\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$

**$\sigma$ unknown, large sample (z-interval):**
$$\bar{x} \pm z_{\alpha/2} \frac{s}{\sqrt{n}}$$

### Confidence Interval for Proportion
$$\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### Confidence Interval for Difference of Means

**Known variances:**
$$(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

**Unknown, equal variances (pooled):**
$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, n_1+n_2-2} s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$
where $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$

**Unknown, unequal variances (Welch):**
$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, \nu} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$

### Confidence Interval for Variance (Normal Population)
$$\left(\frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}}\right)$$

### Confidence Interval for Ratio of Variances (Normal)
$$\left(\frac{s_1^2}{s_2^2} \cdot \frac{1}{F_{\alpha/2, n_1-1, n_2-1}}, \frac{s_1^2}{s_2^2} \cdot F_{\alpha/2, n_2-1, n_1-1}\right)$$

### Sample Size for Given Margin of Error
**Mean:** $n = \left(\frac{z_{\alpha/2} \sigma}{E}\right)^2$
**Proportion:** $n = \frac{z_{\alpha/2}^2 p(1-p)}{E^2}$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\alpha$ | Significance level |
| $1-\alpha$ | Confidence level |
| $z_{\alpha/2}$ | Upper $\alpha/2$ quantile of $N(0,1)$ |
| $t_{\alpha/2, df}$ | Upper $\alpha/2$ quantile of $t_{df}$ |
| $\chi^2_{\alpha, df}$ | Upper $\alpha$ quantile of $\chi^2_{df}$ |
| $F_{\alpha, df_1, df_2}$ | Upper $\alpha$ quantile of $F_{df_1, df_2}$ |

---

## GATE Tricks

> [!tip>
> **$\sigma$ known → z, $\sigma$ unknown → t**
> **Large sample (n ≥ 30)** → z even if $\sigma$ unknown
> **$\sigma$ known CI**: $\bar{x} \pm z_{\alpha/2} \sigma/\sqrt{n}$
> **$\sigma$ unknown CI**: $\bar{x} \pm t_{\alpha/2} s/\sqrt{n}$
> **Paired data**: Use differences, then one-sample CI
> **Paired vs independent**: Paired = dependent = more powerful

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Confidence Level | Significance Level | $1-\alpha$ vs $\alpha$ |
| z-interval | t-interval | $\sigma$ known vs unknown |
| CI for mean | CI for proportion | $\mu$ vs $p$ |
| One-sided | Two-sided | One tail vs two tails |

---

## Common Mistakes

> [!warning>
> **Interpreting CI as probability**: Parameter is fixed, CI is random!
> **Using z when $\sigma$ unknown and n small**: Must use t!
> **Confusing $z_{\alpha/2}$ and $z_{\alpha}$**: Two-tailed uses $\alpha/2$
> **Not checking normality for t-interval**: n < 30 needs normality!

---

## Memory Tricks

> [!tip>
> **CI** = **C**onfidence **I**nterval = range of plausible values
> **Margin of Error** = half-width
> **$\sigma$ known → z**, $\sigma$ unknown → t
> **Paired data** = differences = more powerful

---

## Previous GATE Patterns

- **CI for mean**: $\sigma$ known/unknown, n large/small
- **CI for proportion**: $\hat{p} \pm z \sqrt{\hat{p}(1-\hat{p})/n}$
- **Paired vs independent**: Paired = more powerful
- **Sample size for given margin of error**: $n = (z \sigma / E)^2$

---

## Revision Summary

```
CONFIDENCE INTERVALS
├── CI = Estimate ± Margin of Error
├── Mean ($\sigma$ known): x̄ ± z σ/√n
├── Mean ($\sigma$ unknown): x̄ ± t s/√n
├── Proportion: p̂ ± z √(p̂(1-p̂)/n)
├── Difference of means: (x̄₁-x̄₂) ± margin
├── Variance: ((n-1)s²/χ²_α/₂, (n-1)s²/χ²_{1-α/₂})
├── $\sigma$ known → z, unknown → t
├── Paired data: use differences
├── Interpretation: $100(1-\alpha)\%$ confident, NOT probability!
└── Key: z for known $\sigma$ or large n, t for unknown $\sigma$ small n
```

---

## Related Notes

- [[39 Point Estimation]]
- [[40 Interval Estimation]]
- [[48 z Test]]
- [[49 t Test]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #confidence-intervals #revision