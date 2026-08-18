---
tags: [statistics, gate-da, hypothesis-testing, null-hypothesis, alternative-hypothesis, revision]
---

# 44 Null and Alternative Hypothesis

> [!note] Null hypothesis is the default assumption. Alternative hypothesis is what we want to find evidence for.

---

## Overview

Every hypothesis test involves two competing hypotheses: the null hypothesis ($H_0$) representing the status quo or no effect, and the alternative hypothesis ($H_1$) representing the research claim we want to support.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Null Hypothesis ($H_0$)** | Statement of no effect, no difference, equality |
| **Alternative Hypothesis ($H_1$ or $H_a$)** | Statement of effect, difference, what we want to prove |
| **Simple Hypothesis** | Specifies exact value of parameter |
| **Composite Hypothesis** | Specifies range of values |

---

## Formulae

### Standard Forms

**Two-tailed (Non-directional):**
$$H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0$$

**Right-tailed (Upper-tailed):**
$$H_0: \theta \leq \theta_0 \quad \text{vs} \quad H_1: \theta > \theta_0$$

**Left-tailed (Lower-tailed):**
$$H_0: \theta \geq \theta_0 \quad \text{vs} \quad H_1: \theta < \theta_0$$

### Common Scenarios

| Scenario | $H_0$ | $H_1$ |
|----------|-------|-------|
| Mean test | $\mu = \mu_0$ | $\mu \neq \mu_0$ |
| Proportion test | $p = p_0$ | $p \neq p_0$ |
| Variance test | $\sigma^2 = \sigma_0^2$ | $\sigma^2 \neq \sigma_0^2$ |
| Two means | $\mu_1 = \mu_2$ | $\mu_1 \neq \mu_2$ |
| Correlation | $\rho = 0$ | $\rho \neq 0$ |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $H_0$ | Null hypothesis |
| $H_1$ | Alternative hypothesis |
| $\theta$ | Parameter of interest |
| $\theta_0$ | Hypothesized value |

---

## Important Properties

### Null Hypothesis Always Contains Equality
- $H_0$ always has $=$, $\leq$, or $\geq$
- $H_1$ has $\neq$, $>$, or $<$

### Asymmetry
- We **never** "accept" $H_0$; we "fail to reject" it
- $H_0$ is the default; burden of proof is on $H_1$

### Choosing Direction
- Use two-tailed unless there's strong prior reason for direction
- Direction should be decided BEFORE seeing data

---

## GATE Tricks

> [!tip>
> **$H_0$ always has $=$, $\leq$, or $\geq$**
> **$H_1$ has $\neq$, $>$, or $<$**
> **Two-tailed**: $\neq$ (most common unless specified)
> **One-tailed**: $>$ or $<$ (when direction is specified)
> **Burden of proof**: On $H_1$ (we try to reject $H_0$)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| $H_0$ | $H_1$ | Status quo vs research claim |
| One-tailed | Two-tailed | Directional vs non-directional |
| $\theta = \theta_0$ | $\theta \neq \theta_0$ | Point null vs two-sided alternative |

---

## Common Mistakes

> [!warning>
> **Putting inequality in $H_0$**: $H_0$ must contain equality!
> **Choosing direction after seeing data**: Must decide before!
> **Saying "Accept $H_0$"**: Never! We "fail to reject"!
> **Switching $H_0$ and $H_1$**: $H_0$ is status quo!

---

## Memory Tricks

> [!tip>
> **$H_0$** = **H**ypothesis **0** = **H**old status quo
> **$H_1$** = **H**ypothesis **1** = **H**eavy evidence needed
> **Null** = **N**ull = **N**othing happening
> **Alternative** = **A**lternative = **A**ction needed

---

## Previous GATE Patterns

- **Formulate hypotheses**: From problem statement
- **Identify test type**: One-tailed vs two-tailed
- **Formulate for**: Means, proportions, variances, correlation

---

## Revision Summary

```
NULL & ALTERNATIVE HYPOTHESIS
├── H₀: status quo (always has =, ≤, or ≥)
├── H₁: research claim (has ≠, >, or <)
├── Two-tailed: H₀: θ = θ₀ vs H₁: θ ≠ θ₀
├── Right-tailed: H₀: θ ≤ θ₀ vs H₁: θ > θ₀
├── Left-tailed: H₀: θ ≥ θ₀ vs H₁: θ < θ₀
├── Never "accept H₀", only "fail to reject"
├── Direction chosen BEFORE seeing data
└── Burden of proof on H₁
```

---

## Related Notes

- [[43 Hypothesis Testing]]
- [[45 Type I and Type II Errors]]
- [[46 p Value and Significance Level]]
- [[48 z Test]]
- [[49 t Test]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #null-hypothesis #alternative-hypothesis #revision