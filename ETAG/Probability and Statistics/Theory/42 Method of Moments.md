---
tags: [statistics, gate-da, method-of-moments, estimation, revision]
---

# 42 Method of Moments

> [!note] Method of moments estimates parameters by equating sample moments to population moments.

---

## Overview

The Method of Moments (MOM) is a classical estimation technique that equates sample moments (like sample mean, sample variance) to their theoretical population counterparts to solve for parameters.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Population Moments** | $\mu_k' = E[X^k]$ |
| **Sample Moments** | $m_k = \frac{1}{n}\sum_{i=1}^n X_i^k$ |
| **Method of Moments** | Equate sample moments to population moments |

---

## Formulae

### Procedure
For $k$ parameters $\theta_1, ..., \theta_k$:
1. Compute first $k$ population moments: $\mu_1', \mu_2', ..., \mu_k'$
2. Compute first $k$ sample moments: $m_1, m_2, ..., m_k$
3. Set $\mu_j' = m_j$ for $j = 1, ..., k$
4. Solve the system for $\theta_1, ..., \theta_k$

### Sample Moments
$$m_1 = \bar{x} = \frac{1}{n}\sum x_i$$
$$m_2 = \frac{1}{n}\sum x_i^2$$
$$m_k = \frac{1}{n}\sum x_i^k$$

### Population Moments (Examples)
| Distribution | $\mu_1' = E[X]$ | $\mu_2' = E[X^2]$ |
|--------------|------------------|-------------------|
| Bernoulli($p$) | $p$ | $p$ |
| Binomial($n,p$) | $np$ | $np(1-p) + n^2p^2$ |
| Poisson($\lambda$) | $\lambda$ | $\lambda + \lambda^2$ |
| Normal($\mu,\sigma^2$) | $\mu$ | $\mu^2 + \sigma^2$ |
| Exponential($\lambda$) | $1/\lambda$ | $2/\lambda^2$ |
| Uniform($a,b$) | $(a+b)/2$ | $(a^2+ab+b^2)/3$ |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\mu_k'$ | $k$-th population moment |
| $m_k$ | $k$-th sample moment |
| $\bar{x}$ | First sample moment |

---

## Important Properties

### MOM vs MLE
| Aspect | MOM | MLE |
|--------|-----|-----|
| **Simplicity** | Often simpler | Can be complex |
| **Efficiency** | Less efficient | Asymptotically efficient |
| **Existence** | Always exists (if moments exist) | May not exist |
| **Invariance** | Not invariant | Invariant |

### Properties
- MOM estimators are generally consistent
- MOM estimators are not necessarily unbiased
- MOM is not invariant to transformations

---

## Mathematical Intuition

**Moment Matching**: The shape of a distribution is characterized by its moments. By matching the "shape" of the sample to the theoretical shape, we estimate parameters.

**Sample Moments = Empirical**: Sample moments are the empirical counterparts of theoretical moments.

---

## Algorithms / Problem-Solving

### MOM Procedure
```
1. Identify number of parameters k
2. Write first k population moments in terms of parameters
3. Compute first k sample moments from data
4. Equate: population moment = sample moment
5. Solve for parameters
```

### Example: Normal($\mu, \sigma^2$)
$$\mu_1' = \mu = \bar{x} \Rightarrow \hat{\mu} = \bar{x}$$
$$\mu_2' = \mu^2 + \sigma^2 = \frac{1}{n}\sum x_i^2 \Rightarrow \hat{\sigma}^2 = \frac{1}{n}\sum x_i^2 - \bar{x}^2 = \frac{1}{n}\sum(x_i - \bar{x})^2$$

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **MOM**: Match moments! Sample moment = Population moment
> **Normal**: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x-\bar{x})^2$ (uses $1/n$!)
> **Exponential**: $\hat{\lambda} = 1/\bar{x}$
> **Uniform**: $\hat{a}+\hat{b} = 2\bar{x}$, $\hat{b}-\hat{a} = \sqrt{12 s^2}$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| MOM | MLE | Match moments vs max likelihood |
| Population moment | Sample moment | Theoretical vs empirical |
| $1/n$ | $1/(n-1)$ | MOM uses $1/n$, unbiased uses $1/(n-1)$ |

---

## Common Mistakes

> [!warning>
> **MOM variance uses $1/n$**: NOT $1/(n-1)$!
> **Number of moments = number of parameters**: Need as many equations as unknowns
> **MOM not invariant**: $g(\hat{\theta}_{MOM}) \neq$ MOM for $g(\theta)$
> **MOM can be outside parameter space**: Check validity!

---

## Memory Tricks

> [!tip>
> **MOM** = **M**ethod **o**f **M**oments = **M**atch **M**oments
> **Moment** = **Mo**ment = average of powers
> **Sample** = empirical, **Population** = theoretical

---

## Previous GATE Patterns

- **Derive MOM estimators**: For given distribution
- **Compare MOM vs MLE**: Compute both
- **Normal MOM**: $\hat{\mu}=\bar{x}$, $\hat{\sigma}^2=\frac{1}{n}\sum(x-\bar{x})^2$
- **Exponential MOM**: $\hat{\lambda}=1/\bar{x}$
- **Uniform MOM**: Solve system for $a,b$

---

## Revision Summary

```
METHOD OF MOMENTS (MOM)
├── Match sample moments to population moments
├── k parameters → need first k moments
├── $m_k = \frac{1}{n}\sum x_i^k = \mu_k'(\theta)$
├── Solve for $\theta$
├── MOM: $1/n$ (not $1/(n-1)$!)
├── Common: Normal $\hat{\mu}=\bar{x}$, $\hat{\sigma}^2=\frac{1}{n}\sum(x-\bar{x})^2$
├── Exponential: $\hat{\lambda}=1/\bar{x}$
├── Not invariant to transformations
└── Less efficient than MLE, but simpler
```

---

## Related Notes

- [[39 Point Estimation]]
- [[41 Maximum Likelihood Estimation]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #method-of-moments #estimation #revision