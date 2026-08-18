---
tags: [probability, gate-da, clt, central-limit-theorem, revision]
---

# 33 Central Limit Theorem (CLT)

> [!note] Sample mean of i.i.d. random variables approaches normal distribution regardless of population distribution.

---

## Overview

The Central Limit Theorem (CLT) is one of the most important theorems in probability and statistics. It explains why the normal distribution appears so frequently in nature and statistics.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **CLT** | $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$ |
| **Sample Mean** | $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ |
| **Standard Error** | $\frac{\sigma}{\sqrt{n}}$ |
| **Convergence in Distribution** | CDF converges to standard normal CDF |

---

## Formulae

### CLT Statement
If $X_1, X_2, ...$ are i.i.d. with $E[X_i] = \mu$, $Var(X_i) = \sigma^2 < \infty$:
$$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$$

Equivalently:
$$\bar{X}_n \xrightarrow{d} N\left(\mu, \frac{\sigma^2}{n}\right)$$

### Standard Error
$$SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$$

### Finite Population Correction (Sampling without replacement)
$$SE(\bar{X}) = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N-n}{N-1}}$$

### Continuity Correction (Discrete populations)
$$P(\bar{X} \leq k) \approx \Phi\left(\frac{k + 0.5 - \mu}{\sigma/\sqrt{n}}\right)$$

### Lyapunov CLT (General)
If $X_i$ independent, $E[X_i] = \mu_i$, $Var(X_i) = \sigma_i^2$, and Lyapunov condition holds:
$$\frac{\sum_{i=1}^n (X_i - \mu_i)}{\sqrt{\sum \sigma_i^2}} \xrightarrow{d} N(0,1)$$

### Lindeberg-Feller CLT
More general condition allowing different distributions.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\bar{X}_n$ | Sample mean |
| $\mu$ | Population mean |
| $\sigma$ | Population standard deviation |
| $n$ | Sample size |
| $SE$ | Standard error = $\sigma/\sqrt{n}$ |

---

## Important Properties

### Requirements
1. **Independence**: $X_i$ independent
2. **Identical distribution**: i.i.d. (classical CLT) or independent with conditions
3. **Finite variance**: $\sigma^2 < \infty$

### Rate of Convergence
- Faster for symmetric distributions
- Slower for skewed distributions
- Berry-Esseen bound: $|F_n(z) - \Phi(z)| \leq \frac{C \rho}{\sigma^3\sqrt{n}}$ where $\rho = E[|X-\mu|^3]$

### Sample Size Guidelines
- $n \geq 30$: Often sufficient (rule of thumb)
- Symmetric population: $n \geq 15$ may suffice
- Highly skewed: $n \geq 50$ or more

### Standard Error vs Standard Deviation
- **SD** ($\sigma$): Population variability
- **SE** ($\sigma/\sqrt{n}$): Variability of sample mean

---

## Mathematical Intuition

**Averaging Smooths Out**: Summing many independent variables averages out irregularities, leaving only the smooth bell curve.

**Scaling**: Division by $\sqrt{n}$ gives the right scaling for convergence.

**Universality**: The limit is ALWAYS normal, regardless of original distribution (with finite variance).

---

## Algorithms / Problem-Solving

### Using CLT
```
1. Check: i.i.d., finite variance, n large enough
2. Compute μ = E[X], σ = SD(X)
3. Standardize: Z = (X̄ - μ) / (σ/√n)
4. Use standard normal: Φ(z)
5. For discrete: apply continuity correction
```

### Sample Size Determination
```
For margin of error E with confidence 1-α:
n = (z_{α/2} * σ / E)²
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **CLT**: Sample mean ≈ Normal regardless of population!
> **Standard Error** = σ/√n (NOT σ/n!)
> **n ≥ 30** usually sufficient
> **Z = (X̄ - μ) / (σ/√n)**
> **Continuity correction** for discrete
> **Sum of i.i.d.**: CLT applies to sum too (just multiply by n)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Standard Deviation | Standard Error | σ vs σ/√n |
| Population | Sampling Distribution | Original vs distribution of mean |
| CLT | LLN | Distribution vs convergence of mean |
| Continuous | Discrete population | Continuity correction needed |

---

## Common Mistakes

> [!warning>
> **Using σ instead of σ/√n** for standard error!
> **Using σ/n**: Wrong scaling!
> **n too small**: CLT is asymptotic!
> **Forgetting continuity correction** for discrete populations
> **Applying CLT to small n without checking distribution**

---

## Memory Tricks

> [!tip>
> **CLT** = **C**entral **L**imit **T**heorem = **C**onverge to normal
> **SE = σ/√n** = "Standard Error shrinks with √n"
> **Z = (X̄ - μ) / SE** = standardize sample mean

---

## Previous GATE Patterns

- **Standardize sample mean**: Z = (X̄ - μ)/(σ/√n)
- **Find P(X̄ > c)**: Standardize, use Φ
- **Find n**: Given margin of error, confidence level
- **Sum of i.i.d.**: Apply CLT to sum
- **Discrete population**: Apply continuity correction

---

## Revision Summary

```
CENTRAL LIMIT THEOREM (CLT)
├── X̄_n ≈ N(μ, σ²/n) for large n
├── Z = (X̄ - μ) / (σ/√n) ~ N(0,1)
├── Standard Error = σ/√n (NOT σ/n!)
├── n ≥ 30 rule of thumb
├── Continuity correction for discrete
├── Applies to SUM too: ΣX_i ≈ N(nμ, nσ²)
├── Berry-Esseen: bound on error
└── Key: Standardize with SE = σ/√n!
```

---

## Related Notes

- [[31 Normal Distribution]]
- [[32 Standard Normal Distribution]]
- [[34 Law of Large Numbers]]
- [[36 Population and Sample]]
- [[38 Sampling Distribution]]
- [[47 Confidence Intervals]]
- [[48 z Test]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #clt #central-limit-theorem #revision