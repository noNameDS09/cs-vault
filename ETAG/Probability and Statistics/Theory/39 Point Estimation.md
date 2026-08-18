---
tags: [statistics, gate-da, point-estimation, revision]
---

# 39 Point Estimation

> [!note] Point estimation provides a single value (point estimate) to approximate an unknown population parameter.

---

## Overview

Point estimation uses sample data to calculate a single value (point estimate) that serves as the best guess for an unknown population parameter.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Parameter** | Unknown population characteristic ($\theta$) |
| **Estimator** | Rule/formula to compute estimate from sample ($\hat{\theta}$) |
| **Estimate** | Numerical value of estimator for a given sample |
| **Point Estimate** | Single value estimate of parameter |

---

## Formulae

### Common Point Estimators
| Parameter | Estimator | Formula |
|-----------|-----------|---------|
| Mean $\mu$ | Sample mean $\bar{X}$ | $\bar{x} = \frac{1}{n}\sum x_i$ |
| Variance $\sigma^2$ | Sample variance $S^2$ | $s^2 = \frac{1}{n-1}\sum(x_i-\bar{x})^2$ |
| Proportion $p$ | Sample proportion $\hat{p}$ | $\hat{p} = x/n$ |
| Covariance $\sigma_{XY}$ | $s_{XY}$ | $\frac{1}{n-1}\sum(x_i-\bar{x})(y_i-\bar{y})$ |

### Properties of Estimators
| Property | Definition |
|----------|------------|
| **Unbiasedness** | $E[\hat{\theta}] = \theta$ |
| **Consistency** | $\hat{\theta}_n \xrightarrow{P} \theta$ as $n \to \infty$ |
| **Efficiency** | Minimum variance among unbiased estimators |
| **Sufficiency** | $\hat{\theta}$ captures all info about $\theta$ |

### Mean Squared Error (MSE)
$$MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = Var(\hat{\theta}) + Bias(\hat{\theta})^2$$

### Bias
$$Bias(\hat{\theta}) = E[\hat{\theta}] - \theta$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\theta$ | Population parameter |
| $\hat{\theta}$ | Estimator (random variable) |
| $\hat{\theta}(x)$ | Estimate (numerical value) |
| $MSE$ | Mean squared error |

---

## Important Properties

### Unbiasedness of Common Estimators
- $\bar{X}$ is unbiased for $\mu$
- $S^2 = \frac{1}{n-1}\sum(X_i-\bar{X})^2$ is unbiased for $\sigma^2$
- $\hat{p} = X/n$ is unbiased for $p$

### Variance of Estimators
- $Var(\bar{X}) = \frac{\sigma^2}{n}$
- $Var(\hat{p}) = \frac{p(1-p)}{n}$
- $Var(S^2) = \frac{2\sigma^4}{n-1}$ (for normal population)

### Cramér-Rao Lower Bound
For unbiased estimators: $Var(\hat{\theta}) \geq \frac{1}{n I(\theta)}$
where $I(\theta) = E\left[\left(\frac{\partial}{\partial \theta}\ln f(X;\theta)\right)^2\right]$ is Fisher information.

---

## Mathematical Intuition

**Estimator = Random Variable**: Different samples give different estimates.

**Unbiasedness**: On average, hits the target. Doesn't guarantee any single estimate is close.

**MSE = Variance + Bias²**: Trade-off between precision and accuracy.

---

## Algorithms / Problem-Solving

### Evaluating an Estimator
```
1. Identify parameter θ and estimator θ̂
2. Find E[θ̂] and check if = θ (unbiased)
3. Find Var(θ̂)
4. Compute MSE = Var + Bias²
5. Compare with Cramér-Rao bound
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **Unbiased**: E[θ̂] = θ
> **Consistent**: θ̂ → θ as n → ∞
> **MSE = Var + Bias²**
> **Sample variance**: use n-1 (unbiased)
> **Cramér-Rao**: Lower bound on variance of unbiased estimators

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Unbiased | Consistent | E[θ̂]=θ vs θ̂→θ as n→∞ |
| Bias | MSE | E[θ̂]-θ vs E[(θ̂-θ)²] |
| Estimator | Estimate | Random variable vs number |

---

## Common Mistakes

> [!warning>
> **Using n instead of n-1 for sample variance**: Biased!
> **Confusing bias and MSE**: MSE includes variance too!
> **Assuming unbiased = best**: Sometimes biased has lower MSE!

---

## Memory Tricks

> [!tip>
> **Bias** = **B**ias = off-center
> **Consistent** = **Con**verges = eventually right
> **MSE** = **M**ean **S**quared **E**rror

---

## Previous GATE Patterns

- **Check unbiasedness**: E[θ̂] = θ?
- **Compute MSE**: Var + Bias²
- **Cramér-Rao bound**: Minimum variance
- **Compare estimators**: Compare MSE

---

## Revision Summary

```
POINT ESTIMATION
├── Estimator θ̂ = rule, Estimate = value
├── Unbiased: E[θ̂] = θ
├── Consistent: θ̂ → θ as n → ∞
├── MSE = Var + Bias²
├── Common: x̄ for μ, s² for σ², p̂ for p
├── s² uses n-1 (unbiased)
├── Cramér-Rao: lower bound for unbiased
└── Key: Unbiased + Low MSE = good estimator!
```

---

## Related Notes

- [[38 Sampling Distribution]]
- [[40 Interval Estimation]]
- [[41 Maximum Likelihood Estimation]]
- [[42 Method of Moments]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #point-estimation #revision