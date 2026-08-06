---
tags: [machine-learning, gate-da, unsupervised-learning, revision]
---

# 17 Unsupervised Learning

> [!note] Learning patterns from **unlabeled data** — no target variable $y$

---

## Overview

Unsupervised learning discovers hidden structure in data without labels. Main tasks: clustering (grouping), dimensionality reduction (compression), density estimation, and anomaly detection.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **No Labels** | Only features $X$, no targets $y$ |
| **Clustering** | Group similar points together |
| **Dimensionality Reduction** | Reduce features while preserving information |
| **Density Estimation** | Learn $P(X)$ |
| **Anomaly Detection** | Find unusual points |
| **Representation Learning** | Learn useful features automatically |

---

## Formulae

### General Objective
Find structure in $X = \{x_1, ..., x_n\}$ where $x_i \in \mathbb{R}^p$

### Clustering Objective (K-Means)
$$
\min_{C_1,...,C_K} \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2
$$

### PCA Objective
$$
\max_{W: W^T W = I} \text{Tr}(W^T X^T X W) \quad \text{s.t. } W \in \mathbb{R}^{p \times k}
$$

### Autoencoder Objective
$$
\min_{\theta, \phi} \sum_{i=1}^n ||x_i - g_\phi(f_\theta(x_i))||^2
$$
where $f_\theta$ = encoder, $g_\phi$ = decoder

### Gaussian Mixture Model (EM)
$$
P(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x | \mu_k, \Sigma_k)
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $X$ | Data matrix ($n \times p$) |
| $n$ | Number of samples |
| $p$ | Number of features |
| $K$ | Number of clusters / components |
| $C_k$ | Cluster $k$ |
| $\mu_k$ | Centroid / mean of cluster $k$ |

---

## Important Properties

### No Ground Truth
- Cannot compute "accuracy" directly
- Evaluation via internal metrics (silhouette, inertia) or external (if labels available later)
- Often used for exploration / preprocessing

### Curse of Dimensionality
- Distance metrics become meaningless in high dimensions
- Density estimation requires exponential samples
- Dimensionality reduction often essential first step

### Scaling Sensitivity
- Distance-based methods (K-Means, PCA) require feature scaling
- Features on different scales → dominated by large-scale features

---

## Mathematical Intuition

**Clustering**: Partition $\mathbb{R}^p$ into regions where points in same region are "similar"

**Dimensionality Reduction**: Find low-dimensional manifold/structure embedded in high-dimensional space

**Density Estimation**: Learn probability distribution that generated data

**Representation Learning**: Learn mapping $x \to z$ where $z$ captures essential factors of variation

---

## Algorithms Summary

| Task | Algorithms |
|------|------------|
| **Clustering** | K-Means, K-Medoids, Hierarchical, DBSCAN, GMM, Spectral |
| **Dimensionality Reduction** | PCA, t-SNE, UMAP, Autoencoders, LDA (supervised), ICA |
| **Density Estimation** | GMM, KDE, Normalizing Flows, VAE |
| **Anomaly Detection** | Isolation Forest, One-Class SVM, Autoencoders, GMM |

---

## Comparison Tables

### Supervised vs Unsupervised

| Aspect | Supervised | Unsupervised |
|--------|------------|--------------|
| Data | $(X, y)$ | $X$ only |
| Goal | Predict $y$ | Find structure |
| Evaluation | Accuracy, F1, MSE | Silhouette, reconstruction error |
| Labels | Required | Not used |
| Typical Use | Classification, Regression | Clustering, Dim reduction, Anomaly detection |

### Clustering vs Dimensionality Reduction

| Aspect | Clustering | Dimensionality Reduction |
|--------|------------|--------------------------|
| Output | Discrete cluster assignments | Continuous low-dim embeddings |
| Goal | Group similar points | Compress while preserving info |
| Number of outputs | $K$ clusters | $k \ll p$ dimensions |

---

## GATE Tricks

> [!tip] **Unsupervised Quick Rules**
> - **Always scale features** before clustering/PCA!
> - **No labels** = no accuracy, use silhouette/inertia
> - **K-Means** = spherical clusters, needs $K$ known
> - **Hierarchical** = no $K$ needed, gives dendrogram
> - **PCA** = linear, max variance, unsupervised
> - **t-SNE/UMAP** = visualization only (non-metric)
> - **GMM** = soft clustering (probabilities), elliptical clusters
> - **Autoencoder** = non-linear dim reduction (NN-based)

> [!warning] **GATE Traps**
> - **Using unscaled data** → features with large variance dominate
> - **Assuming clusters are spherical** → K-Means fails on elongated shapes
> - **Choosing $K$ arbitrarily** → use elbow, silhouette, gap statistic
> - **Using t-SNE for preprocessing** → t-SNE is for viz only, not features!
> - **PCA on non-centered data** → must center first!

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Clustering | Classification | Unsupervised vs Supervised |
| K-Means | K-Medoids | Centroid (mean) vs Medoid (actual point) |
| PCA | LDA | Unsupervised (variance) vs Supervised (separation) |
| Hard Clustering | Soft Clustering | Single assignment vs probabilities |
| t-SNE | PCA | Non-linear viz vs linear compression |

---

## Common Mistakes

1. **Not scaling features** before K-Means/PCA
2. **Using t-SNE embeddings as features** for downstream tasks
3. **Assuming K-Means clusters are meaningful** without validation
4. **Ignoring cluster shape assumptions** (K-Means = spherical)
5. **PCA without centering** data

---

## Memory Tricks

> [!tip] **Unsupervised** = "No supervisor (labels)"
> 
> **Clustering** = "Cluster" = group similar things
> 
> **PCA** = "Principal Components" = main directions of variance
> 
> **K-Means** = "K Means" = K cluster means (centroids)
> 
> **GMM** = "Gaussian Mixture Model" = mixture of Gaussians

---

## Previous GATE Patterns

- **Conceptual**: Identify supervised vs unsupervised problem
- **Preprocessing**: Feature scaling for unsupervised methods
- **K selection**: Elbow method, silhouette score
- **PCA vs LDA**: Unsupervised vs supervised
- **Clustering evaluation**: Internal vs external metrics

---

## Revision Summary

```
UNSUPERVISED LEARNING
├── No labels: only X, no y
├── Main tasks:
│   ├── Clustering: K-Means, Hierarchical, DBSCAN, GMM
│   ├── Dim Reduction: PCA, t-SNE, UMAP, Autoencoders
│   ├── Density Estimation: GMM, KDE
│   └── Anomaly Detection: Isolation Forest, Autoencoders
├── FEATURE SCALING MANDATORY for distance-based methods
├── Evaluation: Silhouette, Inertia, Reconstruction error
├── Curse of dimensionality: dim reduction often needed first
└── Used for: Exploration, Preprocessing, Feature learning
```

---

## Related Notes

- [[18 Clustering]]
- [[19 K Means]]
- [[20 K Medoids]]
- [[21 Hierarchical Clustering]]
- [[22 Dimensionality Reduction]]
- [[23 Principal Component Analysis]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #unsupervised-learning #revision