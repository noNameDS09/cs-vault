---
tags: [probability, gate-da, lln, law-of-large-numbers, revision]
---

# 34 Law of Large Numbers (LLN)

> [!note] Sample mean converges to population mean as sample size increases.

---

## Overview

The Law of Large Numbers (LLN) states that as the sample size grows, the sample mean converges to the expected value. It provides the theoretical foundation for using sample averages to estimate population parameters.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **LLN** | Sample mean converges to population mean |
| **Weak LLN** | Convergence in probability |
| **Strong LLN** | Almost sure convergence |
| **Sample Mean** | $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ |

---

## Formulae

### Weak Law of Large Numbers (WLLN)
If $X_1, X_2, ...$ are i.i.d. with $E[X_i] = \mu$, $Var(X_i) = \sigma^2 < \infty$:
$$\bar{X}_n \xrightarrow{P} \mu$$

Equivalently: $\forall \epsilon > 0, \lim_{n \to \infty} P(|\bar{X}_n - \mu| > \epsilon) = 0$

### Chebyshev Proof of WLLN
$$P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{Var(\bar{X}_n)}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2} \to 0$$

### Strong Law of Large Numbers (SLLN)
If $X_1, X_2, ...$ are i.i.d. with $E[|X_i|] < \infty$:
$$\bar{X}_n \xrightarrow{a.s.} \mu$$

i.e., $P(\lim_{n \to \infty} \bar{X}_n = \mu) = 1$

### Generalizations
- **Ergodic Theorem**: For stationary processes
- **Kolmogorov's SLLN**: For independent (not necessarily identical) with $\sum \frac{Var(X_k)}{k^2} < \infty$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $\bar{X}_n$ | Sample mean of $n$ observations |
| $\mu$ | Population mean |
| $\xrightarrow{P}$ | Convergence in probability |
| $\xrightarrow{a.s.}$ | Almost sure convergence |

---

## Important Properties

### Weak vs Strong
- **WLLN**: $P(|\bar{X}_n - \mu| > \epsilon) \to 0$ (probability of large deviation vanishes)
- **SLLN**: $\bar{X}_n \to \mu$ almost surely (eventually stays close forever)
- **SLLN ⇒ WLLN** (almost sure ⇒ in probability)

### Requirements
- **WLLN**: i.i.d., finite variance
- **SLLN**: i.i.d., finite mean ($E[|X|] < \infty$)

### Sample Variance Consistency
$$S^2 \xrightarrow{P} \sigma^2$$

---

## Mathematical Intuition

**Averaging Cancels Noise**: Random fluctuations cancel out when averaged over many trials.

**LLN vs CLT**:
- **LLN**: Where the mean converges TO (the point $\mu$)
- **CLT**: The SHAPE of the distribution around $\mu$ (normal)

**Insurance/Casino Logic**: Many independent bets → average outcome → expected value.

---

## Algorithms / Problem-Solving

### Applying LLN
```
1. Check: i.i.d. observations
2. Check: finite mean (and variance for WLLN)
3. Conclude: sample mean → population mean
4. Use for: estimating μ from sample, justifying Monte Carlo
```

---

## Complexity
Not applicable.

---

## GATE Tricks

> [!tip>
> **LLN**: Sample mean → population mean
> **WLLN**: Convergence in probability
> **SLLN**: Almost sure convergence (stronger)
> **Requires**: i.i.d., finite mean
> **CLT vs LLN**: LLN = where it converges, CLT = shape around limit

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| LLN | CLT | Convergence of mean vs distribution shape |
| WLLN | SLLN | In probability vs almost sure |
| LLN | Monte Carlo | Theory vs application |

---

## Common Mistakes

> [!warning>
> **Assuming LLN holds without i.i.d. assumption**
> **Using LLN for small samples**: LLN is asymptotic!
> **Confusing WLLN and SLLN**: SLLN is stronger
> **Applying LLN to dependent data without conditions**

---

## Memory Tricks

> [!tip>
> **LLN** = **L**aw of **L**arge **N**umbers = **L**arge **N** → mean converges
> **W**eak = **W**eaker (in probability)
> **S**trong = **S**tronger (almost sure)

---

## Previous GATE Patterns

- **Conceptual**: Difference between LLN and CLT
- **Conditions**: When LLN applies (i.i.d., finite mean)
- **WLLN vs SLLN**: Probability vs almost sure convergence
- **Application**: Justifying sample mean as estimator

---

## Revision Summary

```
LAW OF LARGE NUMBERS (LLN)
├── WLLN: X̄_n → μ in probability (requires finite variance)
├── SLLN: X̄_n → μ almost surely (requires finite mean)
├── SLLN ⇒ WLLN (stronger)
├── Requires: i.i.d. observations
├── X̄_n → μ as n → ∞
├── CLT vs LLN: LLN = point convergence, CLT = distributional shape
└── Key: Sample mean consistently estimates population mean!
```

---

## Related Notes

- [[33 Central Limit Theorem]]
- [[36 Population and Sample]]
- [[38 Sampling Distribution]]
- [[39 Point Estimation]]
- [[GATE Numerical Tricks]]

---

#probability #gate-da #lln #law-of-large-numbers #revision