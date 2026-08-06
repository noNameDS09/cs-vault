---
tags: [machine-learning, gate-da, dimensionality-reduction, unsupervised-learning, revision]
---

# 22 Dimensionality Reduction

> [!note] Reducing number of features while preserving essential information

---

## Overview

Dimensionality reduction transforms high-dimensional data into lower dimensions. Used for visualization, noise reduction, computational efficiency, and avoiding curse of dimensionality.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Feature Selection** | Choose subset of original features |
| **Feature Extraction** | Create new features from original (e.g., PCA) |
| **Linear vs Non-linear** | PCA (linear) vs t-SNE/UMAP/Autoencoders (non-linear) |
| **Supervised vs Unsupervised** | LDA (supervised) vs PCA (unsupervised) |
| **Intrinsic Dimension** | True dimensionality of data manifold |

---

## Formulae

### General Objective
Find mapping $f: \mathbb{R}^p \to \mathbb{R}^k$ ($k \ll p$) preserving "important" structure.

### Linear Methods
$$
z = W^T x \quad \text{where } W \in \mathbb{R}^{p \times k}, W^T W = I
$$

### PCA Objective
$$
\max_{W: W^T W = I} \text{Tr}(W^T X^T X W) = \max \sum_{i=1}^k w_i^T \Sigma w_i
$$
where $\Sigma = \frac{1}{n} X^T X$ (covariance, assuming centered X)

### LDA Objective (Supervised)
$$
\max_W \frac{\text{Tr}(W^T S_B W)}{\text{Tr}(W^T S_W W)}
$$

### Reconstruction Error (Autoencoder)
$$
\min_{\theta, \phi} \sum_{i=1}^n ||x_i - g_\phi(f_\theta(x_i))||^2
$$

### t-SNE Objective (Simplified)
Minimize KL divergence between pairwise similarities in high-D and low-D:
$$
\min \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}
$$
where $p_{ij}$ = Gaussian similarity in high-D, $q_{ij}$ = Student-t in low-D

### UMAP Objective
Similar to t-SNE but uses fuzzy topological representation and cross-entropy.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p$ | Original dimension |
| $k$ | Reduced dimension ($k \ll p$) |
| $W$ | Projection matrix ($p \times k$) |
| $z$ | Low-dimensional representation |
| $\Sigma$ | Covariance matrix |

---

## Important Properties

### Linear Dimensionality Reduction
| Method | Supervision | Objective | Output |
|--------|-------------|-----------|--------|
| **PCA** | Unsupervised | Max variance | Orthogonal components |
| **LDA** | Supervised | Max class separation | Discriminant directions |
| **ICA** | Unsupervised | Independent components | Non-Gaussian sources |
| **Factor Analysis** | Unsupervised | Latent factors | Probabilistic |

### Non-Linear Dimensionality Reduction
| Method | Purpose | Preserves | Scalability |
|--------|---------|-----------|-------------|
| **t-SNE** | Visualization | Local structure | Poor (O(n²)) |
| **UMAP** | Visualization + Features | Local + Global | Better |
| **Autoencoder** | Feature learning | Task-dependent | Good (GPU) |
| **Isomap** | Manifold learning | Geodesic distances | Poor |
| **LLE** | Manifold learning | Local linear structure | Poor |

---

## Mathematical Intuition

**PCA**: Finds orthogonal directions of maximum variance. Equivalent to SVD of centered data matrix.

**LDA**: Finds directions maximizing between-class / within-class variance ratio. Supervised.

**t-SNE/UMAP**: Preserve local neighborhood structure. Good for visualization, not for feature extraction (no inverse transform).

**Autoencoder**: Neural network with bottleneck. Learns non-linear compression. Can be deep.

---

## Algorithms

### Choosing Dimension k

**PCA**: Scree plot (eigenvalues), cumulative variance explained (>95%), elbow

**Autoencoder**: Validation reconstruction error

**t-SNE/UMAP**: Usually 2 or 3 for visualization

### Preprocessing
**ESSENTIAL**: Center data (subtract mean) before PCA/LDA
**RECOMMENDED**: Scale features (unit variance) if features have different units

### Pipeline
```
1. Preprocess: Center + Scale
2. Choose method (PCA/LDA/t-SNE/UMAP/Autoencoder)
3. Select k (variance explained, elbow, task performance)
4. Transform data
5. (Optional) Use for downstream task
```

---

## Complexity

| Method | Training | Transform | Space |
|--------|----------|-----------|-------|
| PCA (SVD) | $O(\min(np^2, n^2p))$ | $O(npk)$ | $O(p^2)$ or $O(np)$ |
| LDA | $O(np^2 + p^3)$ | $O(npk)$ | $O(p^2)$ |
| t-SNE | $O(n^2)$ | N/A (no transform) | $O(n^2)$ |
| UMAP | $O(n \log n)$ | $O(npk)$ | $O(n)$ |
| Autoencoder | $O(n \cdot \text{params} \cdot \text{epochs})$ | $O(npk)$ | $O(\text{params})$ |

---

## Comparison Tables

### Linear Methods Comparison

| Aspect | PCA | LDA | ICA | Factor Analysis |
|--------|-----|-----|-----|-----------------|
| Supervision | No | Yes | No | No |
| Objective | Max variance | Max separation | Independence | Latent factors |
| Components | Orthogonal | Not necessarily | Independent | Correlated |
| Output | Uncorrelated | Correlated | Independent | - |

### When to Use Which

| Scenario | Method |
|----------|--------|
| Unsupervised, linear, max variance | PCA |
| Supervised, classification, linear | LDA |
| Blind source separation | ICA |
| Visualization (2D/3D) | t-SNE / UMAP |
| Non-linear feature learning | Autoencoder |
| Large dataset, need transform | PCA / UMAP / Autoencoder |
| Very large n, visualization | UMAP (faster than t-SNE) |

---

## GATE Tricks

> [!tip] **Dimensionality Reduction Quick Rules**
> - **PCA** = Unsupervised, max variance, linear
> - **LDA** = Supervised, max separation, linear
> - **t-SNE/UMAP** = Visualization only (usually 2D/3D)
> - **Autoencoder** = Non-linear, neural network
> - **Always center data** before PCA/LDA
> - **Scale features** if different units
> - **PCA components are orthogonal** (uncorrelated)
> - **LDA max components = K-1** (K classes)

> [!warning] **GATE Traps**
> - **PCA on non-centered data** → wrong components!
> - **Using t-SNE for features** → no inverse transform, stochastic
> - **LDA needs labels** → can't use unsupervised
> - **LDA max K-1 components** → not p like PCA
> - **PCA vs LDA**: PCA = variance, LDA = separation
> - **Explained variance ratio** = λᵢ / Σλⱼ

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| PCA | LDA | Unsupervised vs Supervised |
| Feature Selection | Feature Extraction | Subset vs New features |
| Linear | Non-linear | PCA vs t-SNE/UMAP/AE |
| t-SNE | UMAP | Both viz; UMAP faster, preserves global |
| PCA | ICA | Variance vs Independence |

---

## Common Mistakes

1. **Not centering data** before PCA
2. **Using t-SNE embeddings as features** for ML
3. **Applying LDA without labels**
4. **Choosing k arbitrarily** → use variance explained
5. **Not scaling features** when units differ

---

## Memory Tricks

> [!tip] **PCA** = **P**rincipal **C**omponent **A**nalysis = main variance directions
> 
> **LDA** = **L**inear **D**iscriminant **A**nalysis = discrimination (supervised)
> 
> **t-SNE** = **t**-distributed **S**tochastic **N**eighbor **E**mbedding
> 
> **UMAP** = **U**niform **M**anifold **A**pproximation and **P**rojection
> 
> **Autoencoder** = **Auto** encode = self-reconstruction

---

## Previous GATE Patterns

- **PCA vs LDA**: Unsupervised vs Supervised distinction
- **Explained variance**: Cumulative sum of eigenvalues
- **Component selection**: Scree plot, Kaiser rule (λ>1)
- **Preprocessing**: Centering and scaling
- **t-SNE purpose**: Visualization, not feature extraction

---

## Revision Summary

```
DIMENSIONALITY REDUCTION
├── Linear:
│   ├── PCA: Unsupervised, max variance, orthogonal components
│   ├── LDA: Supervised, max separation, max K-1 components
│   ├── ICA: Independent components (source separation)
│   └── Factor Analysis: Latent variables
├── Non-linear:
│   ├── t-SNE: Visualization, local structure, O(n²)
│   ├── UMAP: Visualization + features, faster, global+local
│   └── Autoencoder: NN bottleneck, non-linear compression
├── PREPROCESSING: Center (mandatory), Scale (recommended)
├── PCA: Eigenvectors of Σ = XᵀX/n (centered)
├── Explained variance: λᵢ/Σλ
├── LDA: Max Tr(WᵀS_B W)/Tr(WᵀS_W W), max K-1 components
└── Use case determines method
```

---

## Related Notes

- [[23 Principal Component Analysis]]
- [[09 Linear Discriminant Analysis]]
- [[17 Unsupervised Learning]]
- [[18 Clustering]] (PCA for visualization)
- [[Formula Sheet]]

---

#machine-learning #gate-da #dimensionality-reduction #pca #revision