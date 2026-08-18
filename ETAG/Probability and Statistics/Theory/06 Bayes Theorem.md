---
tags: [probability, gate-da, bayes-theorem, revision]
---

# 06 Bayes Theorem

> [!note] Bayes theorem reverses conditional probabilities: from P(Evidence|Hypothesis) to P(Hypothesis|Evidence).

---

## Overview

Bayes theorem is the mathematical rule for updating beliefs based on evidence. It's fundamental to statistical inference, machine learning, and decision making under uncertainty.

---

## Key Concepts

|Concept|Definition|
|---|---|
|**Prior Probability**|$P(H)$ — belief before seeing evidence|
|**Likelihood**|$P(E\mid H)$ — probability of evidence given the hypothesis|
|**Posterior Probability**|$P(H\mid E)$ — updated belief after seeing evidence|
|**Evidence (Marginal Likelihood)**|$P(E)$ — total probability of the evidence|
|**Bayes Theorem**|$P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}$|

---

## Formulae

### Bayes Theorem (Two Hypotheses)
$$P(H|E) = \frac{P(E|H)P(H)}{P(E|H)P(H) + P(E|H^c)P(H^c)}$$

### Bayes Theorem (Multiple Hypotheses)
If $H_1, ..., H_n$ form a partition:
$$P(H_i|E) = \frac{P(E|H_i)P(H_i)}{\sum_{j=1}^n P(E|H_j)P(H_j)}$$

### Odds Form
$$\text{Posterior Odds} = \text{Prior Odds} \times \text{Likelihood Ratio}$$
$$\frac{P(H|E)}{P(H^c|E)} = \frac{P(H)}{P(H^c)} \times \frac{P(E|H)}{P(E|H^c)}$$

### Log-Odds Form
$$\log \frac{P(H|E)}{P(H^c|E)} = \log \frac{P(H)}{P(H^c)} + \log \frac{P(E|H)}{P(E|H^c)}$$

---

## Meaning of Variables

|Symbol|Meaning|
|---|---|
|$H, H_i$|Hypothesis (event we want to infer)|
|$E$|Evidence (observed data)|
|$P(H)$|Prior probability|
|$P(E\mid H)$|Likelihood|
|$P(H\mid E)$|Posterior probability|
|$P(E)$|Evidence (marginal likelihood)

---

## Important Properties

### Normalization
Posterior probabilities sum to 1: $\sum_i P(H_i|E) = 1$

### Updating Sequential Evidence
$$P(H|E_1, E_2) = \frac{P(E_2|H, E_1)P(H|E_1)}{P(E_2|E_1)}$$
If $E_1, E_2$ independent given $H$:
$$P(H|E_1, E_2) \propto P(E_2|H)P(E_1|H)P(H)$$

### Likelihood Ratio
$$\Lambda = \frac{P(E|H)}{P(E|H^c)}$$
- $\Lambda > 1$: Evidence supports $H$
- $\Lambda < 1$: Evidence supports $H^c$

---

## Mathematical Intuition

**Bayes = Proportionality**: $P(H|E) \propto P(E|H)P(H)$
- Prior represents initial belief
- Likelihood represents how well hypothesis explains evidence
- Posterior balances both

**Odds Form**: Updates odds multiplicatively. Each piece of evidence multiplies the odds by its likelihood ratio.

---

## Algorithms / Problem-Solving

### Bayes Theorem Steps
```
1. Identify hypotheses H₁, H₂, ... (partition)
2. Identify evidence E
3. Find priors P(Hᵢ)
4. Find likelihoods P(E|Hᵢ)
5. Compute denominator P(E) = Σ P(E|Hᵢ)P(Hᵢ)
6. Compute posteriors P(Hᵢ|E) = P(E|Hᵢ)P(Hᵢ) / P(E)
```

### Tree Diagram Method
```
Root → H₁ (prior) → E (likelihood)
    → H₂ (prior) → E (likelihood)
    ...
Path to E via Hᵢ: P(Hᵢ) × P(E|Hᵢ)
Posterior P(Hᵢ|E) = (path to Hᵢ & E) / (sum of all paths to E)
```

### 2×2 Table for Medical Testing
|          | Disease (+) | Disease (-) | Total |
| -------- | ----------- | ----------- | ----- |
| Test (+) | True Pos    | False Pos   |       |
| Test (-) | False Neg   | True Neg    |       |
| Total    | Prevalence  | 1-Prev      | 1     |

---

## Complexity
Not applicable for Bayes theorem formulas.

---

## Comparison Tables

### Prior vs Posterior

|              | Prior                | Posterior      |
| ------------ | -------------------- | -------------- |
| **Timing**   | Before evidence      | After evidence |
| **Based on** | Background knowledge | Data + Prior   |
| **Formula**  | $P(H)$               | $P(HE)$        |


### Bayes vs Frequentist

| Aspect | Bayesian | Frequentist |
|--------|----------|-------------|
| Parameter | Random variable | Fixed unknown |
| Probability | Degree of belief | Long-run frequency |
| Inference | Posterior distribution | Confidence intervals |
| Prior | Required | Not used |

---

## GATE Tricks

> [!tip]
> **Odds form is faster for binary**: Posterior Odds = Prior Odds × Likelihood Ratio

> [!tip]
> **Medical test pattern**: 
> - Disease = Hypothesis, Test = Evidence
> - Sensitivity = $P(+|D)$
> - Specificity = $P(-|D^c)$
> - Prevalence = $P(D)$

> [!tip]
> **Common GATE structure**: "A factory has machines A, B, C producing items with defect rates... item is defective, which machine made it?"

> [!tip]
> **Base rate fallacy**: Don't ignore prior! Low prevalence can make $P(D|+)$ small even with high sensitivity/specificity

---

## Frequently Confused Concepts

|Concept A|Concept B|Difference|Key Point|
|---|---|---|---|
|Sensitivity|$P(+\mid D)$|True positive rate|Probability of a positive test given disease|
|Specificity|$P(-\mid D^c)$|True negative rate|Probability of a negative test given no disease|
|PPV|$P(D\mid +)$|Positive predictive value|Probability of disease given a positive test|
|NPV|$P(D^c\mid -)$|Negative predictive value|Probability of no disease given a negative test|
|$P(H\mid E)$|$P(E\mid H)$|Posterior vs. likelihood|$P(H\mid E)$ updates belief; $P(E\mid H)$ measures how likely the evidence is given the hypothesis

---

## Common Mistakes

> [!warning]
> **Ignoring the denominator**: Must compute $P(E)$ as sum over ALL hypotheses

> [!warning]
> **Confusing sensitivity with PPV**: $P(+|D) \neq P(D|+)$!

> [!warning]
> **Not normalizing**: Posterior must sum to 1

> [!warning]
> **Using wrong prior**: Prior should reflect knowledge BEFORE seeing evidence

---

## Memory Tricks

> [!tip]
> **Bayes**: "Posterior ∝ Likelihood × Prior"
> **Formula**: $P(H|E) = \frac{P(E|H)P(H)}{P(E)}$ - "Likelihood times Prior over Evidence"

> [!tip]
> **Medical test**: 
> - Sensitivity = $P(+|D)$ (detect disease)
> - Specificity = $P(-|D^c)$ (detect healthy)
> - PPV = $P(D|+)$ (what doctor tells patient!)

---

## Previous GATE Patterns

- **Medical diagnosis**: Given sensitivity, specificity, prevalence, find $P(D|+)$
- **Machine defect**: Multiple machines with different defect rates, find source
- **Spam filtering**: Word probabilities in spam vs ham
- **Sequential updating**: Multiple independent tests

---

## Revision Summary

```
BAYES THEOREM
├── P(H|E) = P(E|H)P(H) / P(E)
├── Posterior ∝ Likelihood × Prior
├── Odds: Post Odds = Prior Odds × Likelihood Ratio
├── Multiple hypotheses: sum in denominator
├── Medical: Sensitivity = P(+|D), Specificity = P(-|Dᶜ)
├── PPV = P(D|+) = what we want!
├── Base rate matters: low prevalence → low PPV
└── Sequential: multiply likelihoods for independent evidence
```

---

## Related Notes

- [[05 Conditional Probability]]
- [[07 Independence]]
- [[GATE Numerical Tricks]]
- [[41 Maximum Likelihood Estimation]]

---

#probability #gate-da #bayes #revision