---
tags: [statistics, gate-da, mle, estimation, revision]
---

# 41 Maximum Likelihood Estimation (MLE)

> [!note] MLE finds parameter values that maximize the likelihood of observing the given data.

---

## Overview

Maximum Likelihood Estimation (MLE) is the most widely used method for parameter estimation. It finds the parameter values that make the observed data most probable.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Likelihood** | $L(\theta) = P(\text{data} | \theta)$ viewed as function of $\theta$ |
| **Log-Likelihood** | $\ell(\theta) = \log L(\theta)$ |
| **MLE** | $\hat{\theta}_{MLE} = \arg\max_\theta L(\theta)$ |
| **Score Function** | $U(\theta) = \frac{\partial}{\partial \theta} \ell(\theta)$ |

---

## Formulae

### Likelihood Function
For i.i.d. sample $x_1, ..., x_n$:
$$L(\theta) = \prod_{i=1}^n f(x_i; \theta)$$

### Log-Likelihood
$$\ell(\theta) = \sum_{i=1}^n \log f(x_i; \theta)$$

### MLE Procedure
1. Write likelihood $L(\theta)$
2. Take log: $\ell(\theta)$
3. Differentiate: $\frac{d\ell}{d\theta} = 0$
4. Solve for $\hat{\theta}$
5. Check second derivative $< 0$ (maximum) or check boundaries

### Fisher Information
$$I(\theta) = E\left[\left(\frac{\partial}{\partial \theta} \log f(X; \theta)\right)^2\right] = -E\left[\frac{\partial^2}{\partial \theta^2} \log f(X; \theta)\right]$$

### Asymptotic Distribution
$$\sqrt{n}(\hat{\theta}_{MLE} - \theta) \xrightarrow{d} N\left(0, \frac{1}{I(\theta)}\right)$$
i.e., $\hat{\theta}_{MLE} \approx N\left(\theta, \frac{1}{n I(\theta)}\right)$ for large $n$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $L(\theta)$ | Likelihood function |
| $\ell(\theta)$ | Log-likelihood |
| $\hat{\theta}_{MLE}$ | Maximum likelihood estimator |
| $I(\theta)$ | Fisher information |

---

## Important Properties

### Invariance Property
If $\hat{\theta}$ is MLE for $\theta$, then $g(\hat{\theta})$ is MLE for $g(\theta)$.

### Asymptotic Properties (under regularity conditions)
1. **Consistency**: $\hat{\theta}_{MLE} \xrightarrow{P} \theta$
2. **Asymptotic Normality**: $\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} N(0, I(\theta)^{-1})$
3. **Asymptotic Efficiency**: Achieves Cramér-Rao lower bound

---

## Mathematical Intuition

**Likelihood = Probability of Data Given Parameters**: Turn the probability function around - fix data, vary parameters.

**Log-Likelihood**: Products become sums, easier to differentiate. Same maximum!

**Score Equation**: $\frac{d\ell}{d\theta} = 0$ finds where likelihood is maximized.

---

## Algorithms / Problem-Solving

### MLE Steps
```
1. Write likelihood L(θ) = ∏ f(x_i; θ)
2. Take log: ℓ(θ) = Σ log f(x_i; θ)
3. Differentiate: dℓ/dθ = 0
4. Solve for θ̂
5. Check second derivative < 0
6. Check boundaries if needed
```

### Common MLEs (Memorize!)

| Distribution | Parameter | MLE |
|--------------|-----------|-----|
| Bernoulli($p$) | $p$ | $\hat{p} = \bar{x}$ |
| Binomial($n,p$) | $p$ | $\hat{p} = \bar{x}/n$ |
| Poisson($\lambda$) | $\lambda$ | $\hat{\lambda} = \bar{x}$ |
| Normal($\mu, \sigma^2$) | $\mu$ | $\hat{\mu} = \bar{x}$ |
| Normal($\mu, \sigma^2$) | $\sigma^2$ | $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$ |
| Exponential($\lambda$) | $\lambda$ | $\hat{\lambda} = 1/\bar{x}$ |
| Uniform($0, \theta$) | $\theta$ | $\hat{\theta} = \max(x_i)$ |

---

## GATE Tricks

> [!tip>
> **MLE Steps**: Likelihood → Log → Differentiate → Solve → Check
> **Common MLEs MEMORIZE**: Bernoulli/Poisson/Normal/Exp/Uniform
> **Normal $\sigma^2$**: MLE uses $1/n$ NOT $1/(n-1)$!
> **Uniform $\theta$**: MLE = max($x_i$), NOT sample mean!
> **Exponential**: $\hat{\lambda} = 1/\bar{x}$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Likelihood | Probability | $P(data|\theta)$ vs $P(data)$ |
| Log-likelihood | Likelihood | Log makes product → sum |
| MLE | MOM | Max likelihood vs match moments |
| MLE variance | Unbiased variance | $1/n$ vs $1/(n-1)$ for normal |

---

## Common Mistakes

> [!warning>
> **Forgetting to check boundaries**: Uniform MLE is at boundary!
> **Normal MLE for $\sigma^2$**: Uses $1/n$, NOT $1/(n-1)$!
> **Forgetting second derivative check**: Could be minimum!
> **Not checking regularity conditions**: MLE may not be asymptotically normal!

---

## Memory Tricks

> [!tip>
> **MLE** = **M**aximum **L**ikelihood **E**stimation
> **Likelihood** = **L**ikelihood of data given $\theta$
> **Log** turns product into sum
> **Invariance**: $g(\hat{\theta})$ is MLE for $g(\theta)$

---

## Previous GATE Patterns

- **Derive MLE**: Given PDF, derive MLE
- **Compare MLE vs MOM**: Compute both
- **Normal MLE**: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$
- **Exponential MLE**: $\hat{\lambda} = 1/\bar{x}$
- **Uniform MLE**: $\hat{\theta} = \max(x_i)$

---

## Revision Summary

```
MAXIMUM LIKELIHOOD ESTIMATION (MLE)
├── L(θ) = ∏ f(x_i; θ), ℓ(θ) = Σ log f(x_i; θ)
├── Steps: Likelihood → Log → d/dθ = 0 → Solve → Check
├── Invariance: g(θ̂) is MLE for g(θ)
├── Asymptotic: √n(θ̂-θ) → N(0, I(θ)⁻¹)
├── Common MLEs:
│   ├── Bernoulli/Poisson: θ̂ = x̄
│   ├── Normal μ: x̄
│   ├── Normal σ²: (1/n)Σ(x-x̄)²
│   ├── Exponential λ: 1/x̄
│   └── Uniform θ: max(x_i)
├── Key: Log turns product into sum!
└── Check boundaries!
```

---

## Related Notes

- [[39 Point Estimation]]
- [[42 Method of Moments]]
- [[40 Interval Estimation]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #mle #estimation #revision