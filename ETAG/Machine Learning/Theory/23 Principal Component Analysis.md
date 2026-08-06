---
tags: [machine-learning, gate-da, pca, dimensionality-reduction, unsupervised-learning, revision]
---

# 23 Principal Component Analysis (PCA)

> [!note] Linear dimensionality reduction via **eigendecomposition of covariance matrix** — finds directions of maximum variance

---

## Overview

PCA finds orthogonal directions (principal components) that capture maximum variance in the data. It's the most widely used linear dimensionality reduction technique.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Principal Components** | Eigenvectors of covariance matrix (directions of max variance) |
| **Explained Variance** | Eigenvalue = variance captured by that component |
| **Projection** | $Z = X V_k$ where $V_k$ = top $k$ eigenvectors |
| **Reconstruction** | $\hat{X} = Z V_k^T$ (approximation) |
| **Scree Plot** | Eigenvalues in descending order — choose k at elbow |

---

## Formulae

### Data Centering (Mandatory!)
$$
\tilde{X} = X - \mathbf{1}\mu^T, \quad \mu = \frac{1}{n}\sum_{i=1}^n x_i
$$

### Covariance Matrix
$$
\Sigma = \frac{1}{n-1} \tilde{X}^T \tilde{X} \quad \text{(or } \frac{1}{n} \text{ for MLE)}
$$

### Eigendecomposition
$$
\Sigma v = \lambda v
$$
- Eigenvalues: $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_p \geq 0$
- Eigenvectors: $v_1, v_2, ..., v_p$ (orthonormal: $v_i^T v_j = \delta_{ij}$)

### Principal Components (Scores)
$$
Z = \tilde{X} V_k \quad \text{where } V_k = [v_1, ..., v_k] \in \mathbb{R}^{p \times k}
$$
$Z \in \mathbb{R}^{n \times k}$ — each row is a sample in PC space

### Explained Variance
$$
\text{Variance explained by PC}_i = \lambda_i
$$
$$
\text{Total variance} = \sum_{i=1}^p \lambda_i = \text{Tr}(\Sigma)
$$
$$
\text{Proportion explained by PC}_i = \frac{\lambda_i}{\sum_{j=1}^p \lambda_j}
$$
$$
\text{Cumulative variance} = \frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^p \lambda_j}
$$

### Reconstruction (Approximation)
$$
\hat{X} = Z V_k^T + \mathbf{1}\mu^T
$$
$$
\text{Reconstruction error} = \frac{1}{n} ||\tilde{X} - \hat{X}||_F^2 = \sum_{i=k+1}^p \lambda_i
$$

### SVD Perspective (Numerically Stable)
$$
\tilde{X} = U D V^T
$$
- $U \in \mathbb{R}^{n \times p}$: left singular vectors
- $D \in \mathbb{R}^{p \times p}$: diagonal singular values
- $V \in \mathbb{R}^{p \times p}$: right singular vectors = eigenvectors of $\Sigma$
- $\lambda_i = \frac{d_i^2}{n-1}$

### Whitening (PCA + Scaling)
$$
Z_{white} = \tilde{X} V D^{-1/2}
$$
- Components have unit variance
- Covariance = Identity

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | Original dimension |
| $k$ | Number of components ($k \leq p$) |
| $\tilde{X}$ | Centered data matrix ($n \times p$) |
| $\Sigma$ | Covariance matrix ($p \times p$) |
| $\lambda_i$ | Eigenvalue (variance of PC$_i$) |
| $v_i$ | Eigenvector (direction of PC$_i$) |
| $V_k$ | Matrix of top $k$ eigenvectors |
| $Z$ | Principal component scores ($n \times k$) |

---

## Important Properties

### Orthogonality
- Principal components are **orthogonal**: $v_i^T v_j = 0$ for $i \neq j$
- Uncorrelated: $\text{Cov}(Z_i, Z_j) = 0$ for $i \neq j$

### Variance Maximization
- PC1 = direction of maximum variance
- PC2 = direction of maximum variance orthogonal to PC1
- etc.

### Optimal Reconstruction
- For any $k$, PCA gives best rank-$k$ approximation in Frobenius norm
- Minimizes reconstruction error among all linear projections

### Rotation Invariance
- PCA is rotation-invariant: rotating data rotates components accordingly
- But not translation-invariant (must center!)

---

## Mathematical Intuition

**Geometric**: PCA fits a $k$-dimensional affine subspace minimizing orthogonal distances to data points.

**Probabilistic**: PCA = Gaussian latent variable model with isotropic noise:
$$
x = W z + \mu + \epsilon, \quad z \sim \mathcal{N}(0,I), \epsilon \sim \mathcal{N}(0, \sigma^2 I)
$$

**Information Theory**: Maximizes mutual information $I(X; Z)$ under Gaussian assumption.

**Rayleigh Quotient**: PC$_1$ maximizes $\frac{v^T \Sigma v}{v^T v}$

---

## Algorithms

### PCA via Eigendecomposition
```python
def pca_eigen(X, k):
    # Center
    mu = X.mean(axis=0)
    X_centered = X - mu
    
    # Covariance
    Sigma = X_centered.T @ X_centered / (n - 1)
    
    # Eigendecomposition
    eigvals, eigvecs = np.linalg.eigh(Sigma)
    
    # Sort descending
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    
    # Top k
    V_k = eigvecs[:, :k]
    
    # Project
    Z = X_centered @ V_k
    
    return Z, V_k, eigvals, mu
```

### PCA via SVD (Preferred for Numerical Stability)
```python
def pca_svd(X, k):
    mu = X.mean(axis=0)
    X_centered = X - mu
    
    # SVD
    U, D, Vt = np.linalg.svd(X_centered, full_matrices=False)
    
    # Top k
    V_k = Vt[:k].T
    Z = U[:, :k] * D[:k]  # or X_centered @ V_k
    
    eigvals = D**2 / (n - 1)
    
    return Z, V_k, eigvals, mu
```

### Incremental PCA (Large Datasets)
```python
from sklearn.decomposition import IncrementalPCA
ipca = IncrementalPCA(n_components=k, batch_size=100)
for batch in data_loader:
    ipca.partial_fit(batch)
Z = ipca.transform(X)
```

### Choosing k
```python
# Cumulative variance
cumsum = np.cumsum(eigvals) / np.sum(eigvals)
k = np.argmax(cumsum >= 0.95) + 1  # 95% variance

# Or scree plot elbow
# Or Kaiser rule: keep eigenvalues > 1 (if standardized)
```

---

## Complexity

| Method | Time | Space |
|--------|------|-------|
| Eigendecomposition | $O(p^3 + np^2)$ | $O(p^2)$ |
| SVD | $O(\min(np^2, n^2p))$ | $O(\min(n,p)^2)$ |
| Randomized SVD | $O(npk)$ | $O(pk)$ |
| Incremental PCA | $O(npk)$ per batch | $O(pk)$ |

---

## Comparison Tables

### PCA vs Other Methods

| Aspect | PCA | LDA | t-SNE | Autoencoder |
|--------|-----|-----|-------|-------------|
| **Supervision** | No | Yes | No | No/Yes |
| **Linearity** | Linear | Linear | Non-linear | Non-linear |
| **Max Components** | $p$ | $K-1$ | Usually 2-3 | Flexible |
| **Inverse Transform** | Yes | Yes | **No** | Yes (decoder) |
| **Feature Selection** | No (combinations) | No | No | Learned |
| **Interpretability** | High (loadings) | Medium | Low | Low |

### PCA vs Factor Analysis

| Aspect | PCA | Factor Analysis |
|--------|-----|-----------------|
| **Model** | Variance decomposition | Latent variables |
| **Error** | None (exact decomposition) | Unique variance per variable |
| **Rotation** | Fixed (orthogonal) | Rotated for interpretability |

---

## GATE Tricks

> [!tip] **PCA Quick Rules**
> - **CENTER DATA FIRST** — subtract mean from each feature!
> - **Scale if different units** — standardize to unit variance
> - **Eigenvalues = variance** of each PC
> - **Sum of eigenvalues = total variance** = trace of covariance
> - **Components are orthogonal** (uncorrelated)
> - **PC1 = max variance direction**
> - **Cumulative variance** for choosing k (95% rule)
> - **SVD more stable** than eigendecomposition

> [!warning] **GATE Traps**
> - **Forgetting to center** → first PC points to mean, not max variance!
> - **PCA on unscaled data** → large-variance features dominate
> - **Using PCA for classification** → unsupervised, may lose discriminative info (use LDA)
> - **PCA components not necessarily interpretable** — linear combinations
> - **No inverse for t-SNE** — PCA has inverse (reconstruction)
> - **Eigenvalues can be zero** — rank deficient data

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| PCA | LDA | Unsupervised (variance) vs Supervised (separation) |
| PCA | SVD | PCA = SVD on centered data |
| Eigenvalues | Singular Values | $\lambda = d^2/(n-1)$ |
| Loadings | Scores | Loadings = $V$ (features); Scores = $Z$ (samples) |
| Explained Variance | Explained Variance Ratio | $\lambda_i$ vs $\lambda_i/\sum\lambda$ |

---

## Common Mistakes

1. **Not centering data** — most common error!
2. **Not scaling** when features have different units
3. **Using PCA for classification** without checking if discriminative info preserved
4. **Choosing k arbitrarily** — use scree plot / cumulative variance
5. **Interpreting PCs as original features** — they're linear combinations

---

## Memory Tricks

> [!tip] **PCA** = **P**rincipal **C**omponent **A**nalysis = main variance directions
> 
> **Center first** = "Center of mass at origin"
> 
> **Eigenvalue** = "Own value" = variance of that component
> 
> **SVD** = **S**ingular **V**alue **D**ecomposition = numerically stable PCA
> 
> **Orthogonal** = uncorrelated = independent (for Gaussian)

---

## Previous GATE Patterns

- **Numerical**: Compute covariance, eigenvalues, explained variance
- **Projection**: Given $X$ and $V_k$, compute $Z$
- **Reconstruction**: Given $Z$ and $V_k$, compute $\hat{X}$
- **Centering**: Effect of not centering
- **Scree plot**: Identify elbow
- **PCA vs LDA**: Unsupervised vs Supervised
- **SVD connection**: $X = UDV^T$, $V$ = eigenvectors

---

## Revision Summary

```
PRINCIPAL COMPONENT ANALYSIS (PCA)
├── CENTER DATA FIRST! X̃ = X - μ
├── Covariance: Σ = X̃ᵀX̃/(n-1)
├── Eigendecomposition: Σv = λv
├── Eigenvalues λ₁ ≥ λ₂ ≥ ... ≥ λₚ = variances
├── Eigenvectors = Principal Components (orthogonal)
├── Scores: Z = X̃Vₖ (n × k)
├── Explained variance: λᵢ / Σλ
├── Cumulative variance for choosing k
├── Reconstruction: X̂ = ZVₖᵀ + μ
├── Reconstruction error = Σ_{i=k+1}ᵖ λᵢ
├── SVD: X̃ = UDVᵀ, V = eigenvectors, λ = d²/(n-1)
├── Unsupervised, linear, max variance
├── Optimal rank-k approximation (Frobenius norm)
└── SCALE features if different units
```

---

## Related Notes

- [[22 Dimensionality Reduction]]
- [[09 Linear Discriminant Analysis]] (Supervised alternative)
- [[17 Unsupervised Learning]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #pca #dimensionality-reduction #revision