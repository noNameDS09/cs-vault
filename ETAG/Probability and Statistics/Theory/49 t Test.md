---
tags: [statistics, gate-da, t-test, hypothesis-testing, revision]
---

# 49 t Test

> [!note] t-test uses t-distribution. Used when population standard deviation is unknown and sample size is small.

---

## Overview

The t-test is a hypothesis test that uses the t-distribution. It's the appropriate test when the population standard deviation is unknown and must be estimated from the sample.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **t-test** | Test using t-distribution |
| **Degrees of Freedom** | $n-1$ for one-sample, $n_1+n_2-2$ for pooled two-sample |
| **Test Statistic** | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ |

---

## Formulae

### One-Sample t-Test
$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \sim t_{n-1}$$

### Two-Sample t-Test (Equal Variances, Pooled)
$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t_{n_1+n_2-2}$$
where $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$

### Two-Sample t-Test (Unequal Variances, Welch)
$$t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t_{\nu}$$
where $\nu \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1-1} + \frac{(s_2^2/n_2)^2}{n_2-1}}$

### Paired t-Test
For paired differences $d_i = x_{1i} - x_{2i}$:
$$t = \frac{\bar{d} - \mu_{d0}}{s_d/\sqrt{n}} \sim t_{n-1}$$
where $\bar{d}$ = mean of differences, $s_d$ = SD of differences

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $t$ | Test statistic |
| $t_{\alpha, df}$ | Upper $\alpha$ quantile of $t_{df}$ |
| $s$ | Sample standard deviation |
| $s_p$ | Pooled standard deviation |
| $df$ | Degrees of freedom |

---

## Important Properties

### When to Use t-Test
1. Population normal, $\sigma$ unknown
2. $n < 30$ (small sample)
3. Paired data

### t vs z
- t-distribution has heavier tails than normal
- As $df \to \infty$, $t \to N(0,1)$
- For $df \geq 30$, t ≈ z

### Paired vs Independent
- Paired: same subjects measured twice (more powerful)
- Independent: different subjects in each group

---

## GATE Tricks

> [!tip>
> **t-test**: $\sigma$ unknown, small n ($n < 30$)
> **Test stat**: $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
> **df** = $n-1$ (one-sample), $n_1+n_2-2$ (pooled)
> **Paired**: Use differences $d_i = x_{1i} - x_{2i}$
> **Welch**: Unequal variances, different df formula

---

## Common Mistakes

> [!warning>
> **Using z instead of t** when $\sigma$ unknown and n small!
> **Using pooled t when variances unequal**: Use Welch!
> **Forgetting paired design**: Paired data needs paired t-test!
> **df formula**: $n-1$ for one-sample, $n_1+n_2-2$ for pooled

---

## Memory Tricks

> [!tip>
> **t** = **T** = **T**iny sample (small n)
> **t** = **T** = Student's **T** distribution
> **df** = **D**egrees of **F**reedom
> **Paired** = **P**aired = **P**owerful

---

## Previous GATE Patterns

- **One-sample t**: $\sigma$ unknown, small n
- **Two-sample**: Pooled vs Welch
- **Paired t**: Before/after, matched pairs
- **Decision**: t vs critical value

---

## Revision Summary

```
T-TEST
├── One-sample: t = (x̄ - μ₀) / (s/√n) ~ t_{n-1}
├── Two-sample (pooled): t = (x̄₁-x̄₂) / (s_p√(1/n₁+1/n₂)) ~ t_{n₁+n₂-2}
├── Two-sample (Welch): t = (x̄₁-x̄₂) / √(s₁²/n₁ + s₂²/n₂) ~ t_ν
├── Paired: t = (d̄ - μ_d) / (s_d/√n) ~ t_{n-1}
├── σ unknown, small n (< 30)
├── df = n-1 or n₁+n₂-2 or Welch formula
├── Paired = more powerful for matched data
└── Key: t for unknown σ, small n; z for known σ or large n!
```

---

## Related Notes

- [[48 z Test]]
- [[47 Confidence Intervals]]
- [[38 Sampling Distribution]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #t-test #hypothesis-testing #revision