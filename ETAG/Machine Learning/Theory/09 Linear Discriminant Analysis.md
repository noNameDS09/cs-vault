---
tags: [machine-learning, gate-da, lda, classification, dimensionality-reduction, revision]
---

# 09 Linear Discriminant Analysis (LDA)

> [!note] Linear classifier maximizing **between-class variance / within-class variance** ratio

---

## Overview

LDA is a generative classifier that assumes Gaussian class-conditionals with **shared covariance matrix**. It finds linear discriminants (projections) that best separate classes. Also used for dimensionality reduction.

---

## Key Concepts

| Concept                      | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| **Discriminant Function**    | $\delta_k(x) = \log P(C_kx)$ (score for class $k$)         |
| **Linear Decision Boundary** | $\delta_k(x) = \delta_l(x)$ → linear in $x$                |
| **Shared Covariance**        | $\Sigma_k = \Sigma$ for all classes                        |
| **Between-Class Scatter**    | $S_B = \sum n_k (\mu_k - \mu)(\mu_k - \mu)^T$              |
| **Within-Class Scatter**     | $S_W = \sum \sum_{i \in C_k} (x_i - \mu_k)(x_i - \mu_k)^T$ |
| **Fisher's Criterion**       | Maximize $\frac{w^T S_B w}{w^T S_W w}$                     |

---

## Formulae

### Generative Model (Gaussian with Shared Covariance)
$$
x | y=k \sim \mathcal{N}(\mu_k, \Sigma)
$$
$$
P(y=k) = \pi_k
$$

### Discriminant Function
$$
\delta_k(x) = x^T \Sigma^{-1} \mu_k - \frac{1}{2} \mu_k^T \Sigma^{-1} \mu_k + \log \pi_k
$$
*Linear in $x$! (No quadratic term because $\Sigma$ shared)*

### Decision Boundary (Class $k$ vs $l$)
$$
\delta_k(x) = \delta_l(x) \Rightarrow x^T \Sigma^{-1} (\mu_k - \mu_l) = \frac{1}{2} (\mu_k^T \Sigma^{-1} \mu_k - \mu_l^T \Sigma^{-1} \mu_l) - \log \frac{\pi_k}{\pi_l}
$$

### Parameter Estimation
$$
\hat{\pi}_k = \frac{n_k}{n}
$$
$$
\hat{\mu}_k = \frac{1}{n_k} \sum_{i:y_i=k} x_i
$$
$$
\hat{\Sigma} = \frac{1}{n-K} \sum_{k=1}^K \sum_{i:y_i=k} (x_i - \hat{\mu}_k)(x_i - \hat{\mu}_k)^T
$$
*Pooled covariance (weighted average of class covariances)*

### Fisher's Linear Discriminant (Dimensionality Reduction)
Maximize:
$$
J(w) = \frac{w^T S_B w}{w^T S_W w}
$$

**Solution**: Generalized eigenvalue problem
$$
S_B w = \lambda S_W w
$$

- Eigenvectors $w_1, ..., w_{K-1}$ = discriminant directions
- At most $K-1$ non-zero eigenvalues (rank of $S_B \leq K-1$)

### Scatter Matrices
$$
S_B = \sum_{k=1}^K n_k (\mu_k - \mu)(\mu_k - \mu)^T, \quad \mu = \frac{1}{n}\sum n_k \mu_k
$$
$$
S_W = \sum_{k=1}^K \sum_{i:y_i=k} (x_i - \mu_k)(x_i - \mu_k)^T = \sum_{k=1}^K (n_k - 1) \Sigma_k
$$
$$
S_T = S_B + S_W = \sum_{i=1}^n (x_i - \mu)(x_i - \mu)^T \quad \text{(Total scatter)}
$$

### Projection
$$
Z = X W \quad \text{where } W = [w_1, ..., w_{K-1}]
$$
*Projects $p$-dim data to $(K-1)$-dim space*

### Classification in Projected Space
Use LDA classifier on $Z$ or nearest centroid in projected space.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $K$ | Number of classes |
| $p$ | Number of features |
| $n_k$ | Samples in class $k$ |
| $\mu_k$ | Mean of class $k$ |
| $\Sigma$ | Shared covariance matrix |
| $S_B$ | Between-class scatter |
| $S_W$ | Within-class scatter |
| $w$ | Discriminant direction (eigenvector) |
| $\lambda$ | Eigenvalue (separation measure) |

---

## Important Properties

### Assumptions
1. **Gaussian class-conditionals**: $x|y=k \sim N(\mu_k, \Sigma)$
2. **Shared covariance**: $\Sigma_k = \Sigma$ for all $k$
3. **Classes separable** (not perfectly overlapping)

### When Assumptions Hold
- LDA is **Bayes optimal** (minimum error rate)
- Equivalent to Gaussian Naive Bayes with shared covariance

### Dimensionality Reduction
- Max $K-1$ discriminant components
- $S_B$ has rank $\leq K-1$ (sum of $K$ rank-1 matrices with constraint)
- Unlike PCA: **supervised** (uses labels)

### Regularized LDA
For $p > n$ or singular $S_W$:
$$
S_W(\gamma) = (1-\gamma) S_W + \gamma I
$$
- $\gamma = 0$: Standard LDA
- $\gamma = 1$: Naive Bayes (diagonal covariance)
- Shrinkage LDA: $\gamma$ chosen via CV

---

## Mathematical Intuition

**Geometry**: LDA finds directions where:
- Class means are far apart (large $w^T S_B w$)
- Within-class spread is small (small $w^T S_W w$)

**Connection to Regression**: For $K=2$, LDA direction $\propto \Sigma^{-1}(\mu_1 - \mu_2)$. This is proportional to coefficients from linear regression of $y$ on $X$!

**Fisher's View**: Project data to maximize ratio of between-class to within-class variance.

---

## Algorithms

### LDA Classification
```
1. Compute class priors π_k = n_k / n
2. Compute class means μ_k
3. Compute pooled covariance Σ = 1/(n-K) Σ_k Σ_{i∈C_k} (x_i - μ_k)(x_i - μ_k)ᵀ
4. For new x: compute δ_k(x) for all k, predict argmax
```

### LDA Dimensionality Reduction (Fisher)
```
1. Compute S_B and S_W
2. Solve S_B w = λ S_W w for eigenvectors
3. Take top K-1 eigenvectors as W
4. Project: Z = X W
```

### Regularized LDA (for p > n)
```
1. Compute S_W
2. S_W_reg = (1-γ) S_W + γ I
3. Solve S_B w = λ S_W_reg w
4. Choose γ via cross-validation
```

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Training | $O(Kp^2 + np^2)$ | $O(p^2)$ |
| Classification | $O(Kp)$ | $O(p)$ |
| Dimensionality Reduction | $O(p^3)$ (eigendecomp) | $O(p^2)$ |

---

## Comparison Tables

### LDA vs QDA vs Logistic Regression

| Property | LDA | QDA | Logistic Regression |
|----------|-----|-----|---------------------|
| Covariance | Shared | Class-specific | N/A (discriminative) |
| Decision Boundary | Linear | Quadratic | Linear |
| Parameters | $Kp + p(p+1)/2$ | $Kp + Kp(p+1)/2$ | $Kp$ |
| $p > n$ | Fails (needs reg) | Fails | Works with reg |
| Optimal if | Gaussian + shared $\Sigma$ | Gaussian + diff $\Sigma$ | Linear log-odds true |

### LDA vs PCA

| Aspect | LDA | PCA |
|--------|-----|-----|
| Supervision | **Supervised** (uses labels) | Unsupervised |
| Objective | Max class separation | Max variance |
| Max Components | $K-1$ | $p$ |
| Covariance | $S_W^{-1} S_B$ | $S_T$ |

### LDA vs Naive Bayes

| Aspect | LDA | Gaussian NB |
|--------|-----|-------------|
| Covariance | Full $\Sigma$ | Diagonal $\Sigma$ |
| Decision Boundary | Linear | Linear (if shared variance) |
| Parameters | $O(p^2)$ | $O(p)$ |

---

## GATE Tricks

> [!tip] **LDA Quick Rules**
> - **Shared covariance** = linear boundary; **different covariances** = QDA (quadratic)
> - **Max $K-1$ discriminant components** (not $p$ like PCA)
> - **$S_B w = \lambda S_W w$** = generalized eigenvalue problem
> - **LDA = Gaussian NB with shared full covariance**
> - **For $p > n$**: Use regularized/shrinkage LDA
> - **Two classes**: LDA direction $\propto \Sigma^{-1}(\mu_1 - \mu_2)$

> [!warning] **GATE Traps**
> - **LDA ≠ PCA**: LDA supervised, PCA unsupervised
> - **Max components = $K-1$**, not $\min(n,p)$
> - **Assumes Gaussian + shared $\Sigma$** → if violated, QDA or LR better
> - **Singular $S_W$** when $p > n$ → must regularize

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| LDA (classification) | LDA (dim reduction) | Same math, different use |
| LDA | QDA | Shared vs class-specific covariance |
| LDA | PCA | Supervised vs Unsupervised |
| LDA | Logistic Regression | Generative vs Discriminative |
| LDA | Gaussian NB | Full vs Diagonal covariance |

---

## Common Mistakes

1. **Using LDA for dimensionality reduction without labels** → that's PCA!
2. **Forgetting $K-1$ limit** on discriminant components
3. **Not regularizing when $p \geq n$** → singular covariance
4. **Assuming LDA always beats QDA** → QDA better if covariances truly differ
5. **Confusing with Latent Dirichlet Allocation** (topic modeling) — same acronym!

---

## Memory Tricks

> [!tip] **LDA** = **L**inear **D**iscriminant **A**nalysis = **Linear** boundaries
> 
> **QDA** = **Q**uadratic **D**iscriminant **A**nalysis = **Quadratic** boundaries
> 
> **Fisher** = "Between/Within" ratio
> 
> **K-1 components** = "One less than classes"
> 
> **LDA vs PCA**: "**L**abels for **L**DA, **P**CA has **P**robably no labels"

---

## Previous GATE Patterns

- **Numerical**: Compute discriminant function $\delta_k(x)$, find decision boundary
- **Scatter matrices**: Compute $S_B$, $S_W$ from given data
- **Generalized eigenvalue**: $S_B w = \lambda S_W w$
- **Comparison**: LDA vs QDA vs PCA vs Logistic Regression
- **Regularized LDA**: Shrinkage parameter $\gamma$
- **Two-class case**: LDA direction $\propto \Sigma^{-1}(\mu_1 - \mu_2)$

---

## Revision Summary

```
LINEAR DISCRIMINANT ANALYSIS (LDA)
├── Generative: x|y=k ~ N(μ_k, Σ) with SHARED Σ
├── Discriminant: δ_k(x) = xᵀΣ⁻¹μ_k - ½μ_kᵀΣ⁻¹μ_k + log π_k
├── Decision boundary: LINEAR (δ_k = δ_l)
├── Estimation: π_k = n_k/n, μ_k = mean, Σ = pooled covariance
├── Fisher's LDA (dim reduction): max wᵀS_B w / wᵀS_W w
├── Generalized eigen: S_B w = λ S_W w
├── Max K-1 discriminant components
├── S_B = Σ n_k(μ_k-μ)(μ_k-μ)ᵀ, S_W = Σ Σ_{i∈C_k}(x_i-μ_k)(x_i-μ_k)ᵀ
├── Optimal if Gaussian + shared Σ true
├── p > n → Regularized LDA: S_W(γ) = (1-γ)S_W + γI
└── LDA vs PCA: Supervised vs Unsupervised
```

---

## Related Notes

- [[08 Naive Bayes]] (Gaussian NB with shared Σ = LDA)
- [[23 Principal Component Analysis]] (PCA comparison)
- [[06 Logistic Regression]] (Discriminative counterpart)
- [[10 Support Vector Machine]] (Another linear classifier)
- [[Formula Sheet]]

---

#machine-learning #gate-da #lda #classification #dimensionality-reduction #revision