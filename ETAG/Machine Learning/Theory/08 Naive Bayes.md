---
tags: [machine-learning, gate-da, naive-bayes, classification, revision]
---

# 08 Naive Bayes

> [!note] Probabilistic classifier using Bayes' theorem with **conditional independence** assumption

---

## Overview

Naive Bayes applies Bayes' theorem with the "naive" assumption that features are conditionally independent given the class. Despite this strong assumption, it works well in practice, especially for text classification.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Bayes' Theorem** | $P(C|X) = \frac{P(X|C)P(C)}{P(X)}$ |
| **Conditional Independence** | $P(X|C) = \prod_{j=1}^p P(x_j|C)$ |
| **Prior** | $P(C)$ - class probability before seeing features |
| **Likelihood** | $P(X|C)$ - probability of features given class |
| **Posterior** | $P(C|X)$ - class probability after seeing features |
| **Evidence** | $P(X)$ - normalizing constant |

---

## Formulae

### Bayes' Theorem (Classification)
$$
P(C_k|x) = \frac{P(x|C_k) P(C_k)}{P(x)} \propto P(C_k) \prod_{j=1}^p P(x_j|C_k)
$$

### Prediction Rule
$$
\hat{y} = \arg\max_{C_k} P(C_k) \prod_{j=1}^p P(x_j|C_k)
$$

### Log-Posterior (Numerically Stable)
$$
\log P(C_k|x) = \log P(C_k) + \sum_{j=1}^p \log P(x_j|C_k) + \text{const}
$$

---

### Gaussian Naive Bayes (Continuous Features)
$$
P(x_j|C_k) = \frac{1}{\sqrt{2\pi \sigma_{jk}^2}} \exp\left(-\frac{(x_j - \mu_{jk})^2}{2\sigma_{jk}^2}\right)
$$
$$
\mu_{jk} = \frac{1}{n_k} \sum_{i:y_i=C_k} x_{ij}, \quad \sigma_{jk}^2 = \frac{1}{n_k} \sum_{i:y_i=C_k} (x_{ij} - \mu_{jk})^2
$$

### Multinomial Naive Bayes (Discrete Counts / Text)
$$
P(x_j|C_k) = \frac{n_{jk} + \alpha}{n_k + \alpha V}
$$
- $n_{jk}$ = count of feature $j$ in class $k$
- $n_k = \sum_j n_{jk}$ = total feature count in class $k$
- $V$ = vocabulary size (number of features)
- $\alpha$ = Laplace smoothing parameter ($\alpha=1$ = add-one smoothing)

### Bernoulli Naive Bayes (Binary Features)
$$
P(x_j|C_k) = \begin{cases} 
\theta_{jk} & \text{if } x_j = 1 \\
1 - \theta_{jk} & \text{if } x_j = 0
\end{cases}
$$
$$
\theta_{jk} = \frac{n_{jk} + \alpha}{n_k + 2\alpha}
$$
where $n_{jk}$ = number of documents in class $k$ with feature $j$ present

### Categorical Naive Bayes
$$
P(x_j = v|C_k) = \frac{n_{jkv} + \alpha}{n_k + \alpha V_j}
$$
- $V_j$ = number of possible values for feature $j$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $C_k$ | Class $k$ ($k = 1, ..., K$) |
| $x_j$ | Feature $j$ ($j = 1, ..., p$) |
| $P(C_k)$ | Prior probability of class $k$ |
| $P(x_j|C_k)$ | Likelihood of feature $j$ given class $k$ |
| $\mu_{jk}, \sigma_{jk}^2$ | Mean/variance of feature $j$ in class $k$ (Gaussian) |
| $\alpha$ | Smoothing parameter |
| $n_k$ | Number of samples in class $k$ |

---

## Important Properties

### Conditional Independence Assumption
$$
P(x_1, ..., x_p | C) = \prod_{j=1}^p P(x_j | C)
$$
- **Naive** because rarely true in practice
- But often works well because:
  1. Only need correct **ranking** of posteriors, not exact probabilities
  2. Errors in likelihood estimates may cancel out
  3. Works especially well when dependencies are similar across classes

### Decision Boundary
- Gaussian NB with shared variances → **Linear** (same as LDA)
- Gaussian NB with class-specific variances → **Quadratic** (same as QDA)
- Multinomial/Bernoulli → **Linear** in log-space

### Calibration
- Naive Bayes tends to produce **overconfident** probabilities
- Posteriors pushed toward 0 or 1
- Use Platt scaling or isotonic regression for calibration

### Zero Frequency Problem
- If $P(x_j|C_k) = 0$ for some feature → entire posterior = 0
- **Solution**: Laplace/Additive smoothing ($\alpha > 0$)

---

## Mathematical Intuition

**Generative Model**: Naive Bayes models $P(X, C) = P(C) \prod P(x_j|C)$ — learns how data is generated for each class.

**Discriminative vs Generative**:
- Logistic Regression: Directly models $P(C|X)$ (discriminative)
- Naive Bayes: Models $P(X|C)$ and $P(C)$ (generative)

**Asymptotic Comparison**:
- Generative (NB) converges faster (lower variance) but has bias (independence assumption)
- Discriminative (LR) has lower asymptotic error but needs more data

---

## Algorithms

### Training (All Variants)
```
For each class k:
    P(C_k) = n_k / n
    For each feature j:
        Estimate P(x_j|C_k) from data (with smoothing)
```

### Prediction
```
For each class k:
    log_posterior[k] = log(P(C_k))
    For each feature j:
        log_posterior[k] += log(P(x_j|C_k))
Return class with max log_posterior
```

### Laplace Smoothing
```
# Add α to all counts
P(x_j = v | C_k) = (count(v, k) + α) / (count(k) + α * num_values)
```

---

## Complexity

| Variant | Training | Prediction | Space |
|---------|----------|------------|-------|
| Gaussian | $O(np)$ | $O(Kp)$ | $O(Kp)$ |
| Multinomial | $O(np)$ | $O(Kp)$ | $O(Kp)$ |
| Bernoulli | $O(np)$ | $O(Kp)$ | $O(Kp)$ |

*Very fast! Linear in data size.*

---

## Comparison Tables

### NB Variants

| Variant | Feature Type | Use Case |
|---------|-------------|----------|
| Gaussian | Continuous | General continuous data |
| Multinomial | Counts (TF) | Text classification (bag-of-words) |
| Bernoulli | Binary (presence/absence) | Text (binary features), categorical |
| Categorical | Categorical | Discrete features with few values |

### Naive Bayes vs Logistic Regression

| Aspect | Naive Bayes | Logistic Regression |
|--------|-------------|---------------------|
| Type | Generative | Discriminative |
| Assumption | Conditional independence | None (linear log-odds) |
| Training | Closed-form (counting) | Iterative optimization |
| Data Efficiency | High (less data needed) | Lower |
| Asymptotic Error | Higher (bias) | Lower |
| Feature Dependencies | Ignored | Can capture (with interactions) |

---

## GATE Tricks

> [!tip] **Naive Bayes Quick Rules**
> - **Log-space computation**: Always use log probabilities to avoid underflow
> - **Smoothing is essential**: Without it, unseen feature = zero probability
> - **Gaussian NB + shared variance = LDA** (linear boundary)
> - **Gaussian NB + class-specific variance = QDA** (quadratic boundary)
> - **Multinomial NB** for word counts, **Bernoulli NB** for binary presence
> - **Fast training & prediction** → good for baseline / large datasets

> [!warning] **GATE Traps**
> - **Zero probability problem** → always use Laplace smoothing
> - **Independence assumption violated** → but still often works!
> - **Overconfident probabilities** → don't trust raw posteriors
> - **Feature scaling NOT needed** for NB (probabilistic, not distance-based)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Multinomial NB | Bernoulli NB | Counts vs Binary presence |
| Gaussian NB | LDA | LDA assumes shared covariance |
| Generative | Discriminative | Models $P(X,C)$ vs $P(C|X)$ directly |
| Laplace smoothing | Lidstone smoothing | $\alpha=1$ vs general $\alpha$ |

---

## Common Mistakes

1. **No smoothing** → zero probabilities kill predictions
2. **Using probabilities directly** → underflow (use logs!)
3. **Assuming calibrated probabilities** → NB is overconfident
4. **Wrong variant for data type** → Multinomial for counts, Bernoulli for binary
5. **Ignoring class priors** → important for imbalanced data

---

## Memory Tricks

> [!tip] **Naive** = "Naive assumption of independence"
> 
> **Bayes** = $P(C|X) \propto P(X|C)P(C)$
> 
> **Multinomial** = "Multiple counts" (word frequencies)
> 
> **Bernoulli** = "Binary" (present/absent)
> 
> **Log posteriors** = "Logs prevent underflow"

---

## Previous GATE Patterns

- **Numerical**: Compute posterior given priors and likelihoods
- **Smoothing**: Calculate smoothed probabilities
- **Variant selection**: Choose correct NB type for data
- **Comparison**: NB vs Logistic Regression (generative vs discriminative)
- **Decision boundary**: Gaussian NB → linear/quadratic
- **Log computation**: Why log-space is needed

---

## Revision Summary

```
NAIVE BAYES
├── Bayes: P(C|X) ∝ P(C) ∏ P(xⱼ|C)  (conditional independence)
├── Log posterior: log P(C) + Σ log P(xⱼ|C)  (use logs!)
├── Variants:
│   ├── Gaussian: continuous, P(xⱼ|C) ~ N(μ,σ²)
│   ├── Multinomial: counts (text), P(xⱼ|C) = (nⱼₖ+α)/(nₖ+αV)
│   ├── Bernoulli: binary, P(xⱼ|C) = θⱼₖ or 1-θⱼₖ
│   └── Categorical: discrete categories
├── Smoothing (Laplace): α=1 prevents zero probabilities
├── Fast: O(np) training, O(Kp) prediction
├── Generative (models P(X,C)) vs Logistic discriminative (models P(C|X))
├── Gaussian + shared variance = LDA (linear boundary)
├── Gaussian + class-specific variance = QDA (quadratic)
└── Overconfident posteriors → calibrate if needed
```

---

## Related Notes

- [[09 Linear Discriminant Analysis]] (Gaussian NB with shared cov = LDA)
- [[06 Logistic Regression]] (discriminative counterpart)
- [[10 Support Vector Machine]] (another classifier)
- [[Formula Sheet]]

---

#machine-learning #gate-da #naive-bayes #classification #revision