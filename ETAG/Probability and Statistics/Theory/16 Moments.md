---
tags: [probability, gate-da, moments, revision]
---

# 16 Moments

> [!note] Moments are expected values of powers of a random variable. They characterize the shape of a distribution.

---

## Overview

Moments provide a systematic way to describe the shape of a distribution. The first moment is the mean, the second central moment is the variance, and higher moments describe skewness and kurtosis.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Raw Moment** | $\mu_k' = E[X^k]$ |
| **Central Moment** | $\mu_k = E[(X - \mu)^k]$ |
| **Moment Generating Function** | $M_X(t) = E[e^{tX}]$ |

---

## Formulae

### Raw Moments
$$\mu_k' = E[X^k] = \begin{cases}
\sum x^k p(x) & \text{discrete} \\
\int x^k f(x) dx & \text{continuous}
\end{cases}$$

### Central Moments
$$\mu_k = E[(X - \mu)^k]$$

Key central moments:
- $\mu_1 = 0$ (by definition)
- $\mu_2 = Var(X) = \sigma^2$
- $\mu_3$ = Skewness (unnormalized)
- $\mu_4$ = Kurtosis-related

### Normalized Moments
**Skewness**:
$$\gamma_1 = \frac{\mu_3}{\sigma^3} = \frac{E[(X-\mu)^3]}{\sigma^3}$$

**Kurtosis (Excess)**:
$$\gamma_2 = \frac{\mu_4}{\sigma^4} - 3 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$$

### Relationships
$$\mu_2 = \mu_2' - (\mu_1')^2$$
$$\mu_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3$$
$$\mu_4 = \mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4$$

### Moment Generating Function (MGF)
$$M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} \frac{t^k}{k!} E[X^k] = \sum_{k=0}^{\infty} \frac{t^k}{k!} \mu_k'$$

### MGF Properties
1. $M_X(0) = 1$
2. $\frac{d^k}{dt^k} M_X(t) \big|_{t=0} = \mu_k'$
3. $M_{aX+b}(t) = e^{bt} M_X(at)$
4. If $X \perp Y$: $M_{X+Y}(t) = M_X(t) M_Y(t)$
5. MGF uniquely determines distribution (if it exists)

### Characteristic Function
$$\phi_X(t) = E[e^{itX}] \quad \text{(always exists)}$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\mu_k'$ | $k$-th raw moment |
| $\mu_k$ | $k$-th central moment |
| $\mu$ | $\mu_1' = E[X]$ |
| $\sigma^2$ | $\mu_2$ = variance |
| $\gamma_1$ | Skewness |
| $\gamma_2$ | Excess kurtosis |
| $M_X(t)$ | Moment generating function |

---

## Important Properties

### Skewness
- $\gamma_1 > 0$: Right-skewed (long right tail)
- $\gamma_1 < 0$: Left-skewed (long left tail)
- $\gamma_1 = 0$: Symmetric

### Kurtosis
- $\gamma_2 > 0$: Heavy tails (leptokurtic)
- $\gamma_2 < 0$: Light tails (platykurtic)
- $\gamma_2 = 0$: Normal-like tails (mesokurtic)

### MGF of Common Distributions
- Bernoulli($p$): $M(t) = 1-p + pe^t$
- Binomial($n,p$): $M(t) = (1-p+pe^t)^n$
- Poisson($\lambda$): $M(t) = e^{\lambda(e^t-1)}$
- Normal($\mu,\sigma^2$): $M(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$
- Exponential($\lambda$): $M(t) = \frac{\lambda}{\lambda-t}$ for $t < \lambda$

---

## Mathematical Intuition

**MGF = Laplace Transform**: $M_X(t)$ is the Laplace transform of the PDF/PMF. The derivatives at 0 give moments.

**Uniqueness**: MGF (if it exists in a neighborhood of 0) completely determines the distribution.

**Sum of Independent**: MGF of sum = product of MGFs. Very powerful for sums!

---

## Algorithms / Problem-Solving

### Finding Moments from MGF
```
1. Identify MGF M(t)
2. Compute derivatives: M'(t), M''(t), M'''(t), M''''(t)
3. Evaluate at t=0: μ₁' = M'(0), μ₂' = M''(0), etc.
4. Convert to central moments if needed
```

### Using MGF for Sums
```
1. Find MGFs of independent variables
2. Multiply MGFs
3. Recognize resulting MGF as known distribution
```

---

## Complexity
Not applicable.

---

## Comparison Tables

| Moment | Name | Central/Raw | Normalized |
|--------|------|-------------|------------|
| 1st | Mean | Central = 0 | - |
| 2nd | Variance | $\sigma^2$ | - |
| 3rd | Skewness | $\mu_3$ | $\gamma_1 = \mu_3/\sigma^3$ |
| 4th | Kurtosis | $\mu_4$ | $\gamma_2 = \mu_4/\sigma^4 - 3$ |

### Skewness Interpretation

| $\gamma_1$ | Shape |
|------------|-------|
| $> 0$ | Right tail longer |
| $= 0$ | Symmetric |
| $< 0$ | Left tail longer |

### Kurtosis Interpretation

| $\gamma_2$ | Shape |
|------------|-------|
| $> 0$ | Heavy tails (outliers likely) |
| $= 0$ | Normal-like |
| $< 0$ | Light tails |

---

## GATE Tricks

> [!tip>
> **MGF of sum = product**: $M_{X+Y}(t) = M_X(t)M_Y(t)$ for independent

> [!tip>
> **Normal MGF**: $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ - recognize this pattern!

> [!tip>
> **Poisson MGF**: $e^{\lambda(e^t-1)}$ - sum of Poissons is Poisson!

> [!tip>
> **Skewness**: $\gamma_1 = E[(X-\mu)^3]/\sigma^3$
> **Kurtosis**: $\gamma_2 = E[(X-\mu)^4]/\sigma^4 - 3$

> [!tip>
> **Normal distribution**: $\gamma_1 = 0$, $\gamma_2 = 0$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Raw moment | Central moment | About 0 vs about mean |
| Skewness | Kurtosis | Asymmetry vs tail heaviness |
| MGF | Characteristic function | $e^{tX}$ vs $e^{itX}$ (CF always exists) |

---

## Common Mistakes

> [!warning>
> **Confusing raw and central moments**: $\mu_1' = \mu$, but $\mu_1 = 0$!

> [!warning>
> **Forgetting -3 in kurtosis**: Excess kurtosis = $\mu_4/\sigma^4 - 3$

> [!warning>
> **MGF doesn't always exist**: Some distributions (like lognormal) have no MGF

> [!warning>
> **Using MGF outside radius of convergence**

---

## Memory Tricks

> [!tip>
> **MGF**: "Moment Generating Function" - derivatives at 0 give moments
> **Skewness** = "Skew" = asymmetry
> **Kurtosis** = "Cur" = curvature/tailedness

---

## Previous GATE Patterns

- **MGF identification**: Given MGF, find distribution or moments
- **Sum of independent**: Use MGF product property
- **Skewness/kurtosis**: Compute from given moments
- **Normal distribution**: MGF = $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$

---

## Revision Summary

```
MOMENTS
├── Raw: μₖ' = E[Xᵏ]
├── Central: μₖ = E[(X-μ)ᵏ]
├── μ₁' = μ, μ₁ = 0
├── μ₂ = σ² (variance)
├── Skewness: γ₁ = μ₃/σ³
├── Kurtosis: γ₂ = μ₄/σ⁴ - 3
├── MGF: M(t) = E[e^{tX}]
├── M'(0) = μ, M''(0) = μ₂', etc.
├── M_{X+Y}(t) = M_X(t)M_Y(t) (independent)
├── Normal: M(t) = e^{μt + ½σ²t²}
├── Poisson: M(t) = e^{λ(e^t-1)}
└── Key: MGF of sum = product!
```

---

## Related Notes

- [[14 Expectation]]
- [[15 Variance and Standard Deviation]]
- [[17 Covariance and Correlation]]
- [[31 Normal Distribution]]
- [[27 Poisson Distribution]]

---

#probability #gate-da #moments #revision