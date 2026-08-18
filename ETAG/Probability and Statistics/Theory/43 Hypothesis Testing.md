---
tags: [statistics, gate-da, hypothesis-testing, revision]
---

# 43 Hypothesis Testing

> [!note] Hypothesis testing is a formal procedure for making decisions about population parameters based on sample data.

---

## Overview

Hypothesis testing is a formal statistical procedure to evaluate claims about population parameters using sample data. It involves comparing a null hypothesis against an alternative hypothesis using sample evidence.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Null Hypothesis ($H_0$)** | Default assumption (no effect/difference) |
| **Alternative Hypothesis ($H_1$ or $H_a$)** | What we want to find evidence for |
| **Test Statistic** | Standardized value computed from sample |
| **Critical Region** | Values of test statistic leading to rejection |
| **Significance Level ($\alpha$)** | $P(\text{Reject } H_0 | H_0 \text{ true})$ |
| **p-value** | $P(\text{data as extreme as observed} | H_0 \text{ true})$ |

---

## Formulae

### General Test Statistic
$$\text{Test Statistic} = \frac{\text{Estimate} - \text{Hypothesized Value}}{\text{Standard Error}}$$

### Decision Rule
- **Reject $H_0$** if $|\text{Test Statistic}| > \text{Critical Value}$ OR $p\text{-value} < \alpha$
- **Fail to Reject $H_0$** otherwise

### Types of Tests
| Alternative | Test Type | Rejection Region |
|-------------|-----------|------------------|
| $\theta \neq \theta_0$ | Two-tailed | Both tails |
| $\theta > \theta_0$ | Right-tailed | Upper tail |
| $\theta < \theta_0$ | Left-tailed | Lower tail |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $H_0$ | Null hypothesis |
| $H_1$ | Alternative hypothesis |
| $\alpha$ | Significance level |
| $p$ | p-value |
| $TS$ | Test statistic |
| $CV$ | Critical value |

---

## Important Properties

### Steps of Hypothesis Testing
```
1. State H₀ and H₁
2. Choose significance level α
3. Identify test statistic and its distribution under H₀
4. Determine critical value(s) or compute p-value
5. Calculate test statistic from sample
6. Make decision: Reject or Fail to Reject H₀
7. Interpret in context
```

### Power of Test
$$\text{Power} = 1 - \beta = P(\text{Reject } H_0 | H_1 \text{ true})$$
- Increases with: larger $n$, larger effect size, larger $\alpha$

---

## Mathematical Intuition

**Hypothesis Testing = Proof by Contradiction**: Assume $H_0$ true, see if data contradicts it. If contradiction is strong enough (p < α), reject $H_0$.

**Burden of Proof**: On the alternative hypothesis. We don't "accept" $H_0$, we "fail to reject" it.

---

## Algorithms / Problem-Solving

### Hypothesis Testing Procedure
```
1. State H₀ and H₁ clearly
2. Choose α (typically 0.05)
3. Identify appropriate test (z, t, χ², F, etc.)
4. Find critical value(s) or compute p-value
5. Compute test statistic from data
6. Compare: TS vs CV or p-value vs α
7. Decide and conclude
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **p-value < α → Reject H₀**
> **p-value ≥ α → Fail to Reject H₀**
> **Two-tailed**: α/2 in each tail
> **One-tailed**: α in one tail
> **Test Stat = (Estimate - Hypothesized) / SE**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| p-value | α | Data-dependent vs pre-specified |
| Fail to Reject | Accept H₀ | Never "accept" H₀! |
| Type I | Type II | Reject true H₀ vs Fail to reject false H₀ |
| One-tailed | Two-tailed | Directional vs non-directional |

---

## Common Mistakes

> [!warning>
> **Saying "Accept H₀"**: We NEVER accept H₀, only fail to reject!
> **Confusing p-value with α**: p-value is data-dependent!
> **One-tailed vs two-tailed**: Wrong tails = wrong conclusion!
> **Confusing Type I and Type II**: α = P(Type I), β = P(Type II)

---

## Memory Tricks

> [!tip>
> **H₀** = **H**ypothesis **0** = status quo
> **H₁** = **H**ypothesis **1** = alternative
> **p < α** = **R**eject (p is small → strong evidence)
> **Type I** = **F**alse **P**ositive (reject true H₀)
> **Type II** = **F**alse **N**egative (miss false H₀)

---

## Previous GATE Patterns

- **State hypotheses**: From problem description
- **Choose test**: z, t, χ², F
- **Compute test statistic**: Formula application
- **Decision**: p-value vs α or TS vs CV
- **Type I/II error**: Definitions and relationships

---

## Revision Summary

```
HYPOTHESIS TESTING
├── H₀: null (status quo), H₁: alternative
├── TS = (Estimate - Hypothesized) / SE
├── Decision: p-value < α → Reject H₀
├── Two-tailed: H₁: θ ≠ θ₀, reject if |TS| > CV
├── One-tailed: H₁: θ > θ₀ or θ < θ₀
├── α = P(Type I) = P(Reject H₀ | H₀ true)
├── β = P(Type II) = P(Fail to Reject | H₁ true)
├── Power = 1 - β
└── Never "accept H₀", only "fail to reject"!
```

---

## Related Notes

- [[44 Null and Alternative Hypothesis]]
- [[45 Type I and Type II Errors]]
- [[46 p Value and Significance Level]]
- [[47 Confidence Intervals]]
- [[48 z Test]]
- [[49 t Test]]
- [[50 Chi Square Test]]
- [[51 ANOVA]]
- [[GATE Numerical Tricks]]

---

#statistics #gate-da #hypothesis-testing #revision