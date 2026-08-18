---
tags: [probability, gate-da, continuous-distributions, revision]
---

# 28 Important Continuous Distributions

> [!note] Overview of key continuous distributions: Uniform, Exponential, Normal. Each has dedicated notes.

---

## Overview

Continuous distributions model measurements on a continuous scale. Each has specific PDF, support, parameters, and applications.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **PDF** | $f(x) \geq 0$, $\int f(x) dx = 1$ |
| **Support** | $\{x: f(x) > 0\}$ |
| **Parameters** | Location, scale, shape |

---

## Formulae Summary

### Uniform($a, b$)
- **Support**: $[a, b]$
- **PDF**: $f(x) = \frac{1}{b-a}$
- **Mean**: $\frac{a+b}{2}$
- **Variance**: $\frac{(b-a)^2}{12}$

### Exponential($\lambda$)
- **Support**: $[0, \infty)$
- **PDF**: $f(x) = \lambda e^{-\lambda x}$
- **Mean**: $\frac{1}{\lambda}$
- **Variance**: $\frac{1}{\lambda^2}$
- **Memoryless**: Only continuous memoryless distribution

### Normal($\mu, \sigma^2$)
- **Support**: $(-\infty, \infty)$
- **PDF**: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
- **Mean**: $\mu$
- **Variance**: $\sigma^2$
- **Standard Normal**: $Z \sim N(0,1)$, $Z = \frac{X-\mu}{\sigma}$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $a, b$ | Uniform bounds |
| $\lambda$ | Exponential rate |
| $\mu$ | Normal mean |
| $\sigma^2$ | Normal variance |
| $\sigma$ | Standard deviation |

---

## Important Properties

### Relationships
- Uniform: all outcomes equally likely
- Exponential: memoryless, inter-arrival in Poisson process
- Normal: CLT, sum of independent normals is normal
- Standardization: $Z = \frac{X-\mu}{\sigma} \sim N(0,1)$

### Sum of Independent
- Normal + Normal = Normal (sum means, sum variances)
- Exponential sum = Gamma
- Uniform sum = Irwin-Hall

---

## Comparison Tables

| Distribution | Support | Mean | Variance | Memoryless |
|--------------|---------|------|----------|------------|
| Uniform | $[a,b]$ | $(a+b)/2$ | $(b-a)^2/12$ | No |
| Exponential | $[0,\infty)$ | $1/\lambda$ | $1/\lambda^2$ | **Yes** |
| Normal | $(-\infty,\infty)$ | $\mu$ | $\sigma^2$ | No |

---

## GATE Tricks

> [!tip>
> **Uniform**: All outcomes equally likely, mean = midpoint
> **Exponential**: Memoryless, mean = 1/λ, var = 1/λ²
> **Normal**: Symmetric, bell-shaped, CLT
> **Standardization**: Z = (X-μ)/σ

---

## Memory Tricks

> [!tip>
> **Uniform**: "Uniform" = all equal
> **Exponential**: Mean = 1/λ, Var = 1/λ²
> **Normal**: μ = mean, σ² = variance

---

## Related Notes

- [[29 Uniform Distribution]]
- [[30 Exponential Distribution]]
- [[31 Normal Distribution]]
- [[32 Standard Normal Distribution]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #continuous-distributions #revision