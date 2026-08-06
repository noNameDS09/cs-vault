---
tags: [machine-learning, gate-da, clustering, unsupervised-learning, revision]
---

# 18 Clustering

> [!note] Grouping similar data points into clusters — **unsupervised** partitioning of data

---

## Overview

Clustering partitions data into groups (clusters) such that points in the same cluster are more similar to each other than to points in other clusters. No labels available — purely based on feature similarity.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Cluster** | Group of similar data points |
| **Centroid** | Mean of points in cluster (K-Means) |
| **Medoid** | Actual data point minimizing distances (K-Medoids) |
| **Distance Metric** | Euclidean, Manhattan, Cosine, etc. |
| **Hard Clustering** | Each point belongs to exactly one cluster |
| **Soft Clustering** | Probabilistic assignment (GMM) |
| **Number of Clusters (K)** | Often unknown, must be estimated |

---

## Formulae

### General Clustering Objective
Partition $X = \{x_1, ..., x_n\}$ into $K$ clusters $C_1, ..., C_K$ minimizing:
$$
\sum_{k=1}^K \sum_{x \in C_k} d(x, \text{rep}_k)
$$
where $\text{rep}_k$ = cluster representative (centroid/medoid)

### K-Means Objective (WCSS - Within-Cluster Sum of Squares)
$$
\min_{C_1,...,C_K} \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2
$$
where $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$

### K-Medoids Objective
$$
\min_{C_1,...,C_K} \sum_{k=1}^K \sum_{x \in C_k} d(x, m_k)
$$
where $m_k \in C_k$ (medoid is actual data point)

### Silhouette Coefficient (Evaluation)
For point $i$:
$$
a(i) = \text{avg distance to points in same cluster}
$$
$$
b(i) = \min_{k \neq C(i)} \text{avg distance to points in cluster } k
$$
$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} \in [-1, 1]
$$
Average over all points = overall silhouette score.

### Davies-Bouldin Index
$$
DB = \frac{1}{K}\sum_{i=1}^K \max_{j \neq i} \frac{s_i + s_j}{d(\mu_i, \mu_j)}
$$
where $s_i$ = avg distance within cluster $i$. Lower = better.

### Calinski-Harabasz Index
$$
CH = \frac{\text{Tr}(S_B) / (K-1)}{\text{Tr}(S_W) / (n-K)}
$$
where $S_B$ = between-cluster scatter, $S_W$ = within-cluster scatter. Higher = better.

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $K$ | Number of clusters |
| $C_k$ | Set of points in cluster $k$ |
| $\mu_k$ | Centroid of cluster $k$ |
| $m_k$ | Medoid of cluster $k$ |
| $d(x, y)$ | Distance between points |
| $n$ | Number of data points |

---

## Important Properties

### Distance Metrics & When to Use
| Metric | Formula | Best For |
|--------|---------|----------|
| Euclidean | $\sqrt{\sum (x_i-y_i)^2}$ | Continuous, isotropic clusters |
| Manhattan | $\sum |x_i-y_i|$ | Grid-like, high-dim sparse |
| Cosine | $1 - \frac{x^T y}{||x||||y||}$ | Text, normalized vectors |
| Mahalanobis | $\sqrt{(x-y)^T\Sigma^{-1}(x-y)}$ | Correlated features |

### Cluster Shapes Different Algorithms Handle
| Algorithm | Cluster Shape | Scalability |
|-----------|---------------|-------------|
| K-Means | Spherical (convex) | Good (with k-means++) |
| K-Medoids | Any (with appropriate metric) | Medium |
| Hierarchical | Any | Poor (O(n²) or O(n³)) |
| DBSCAN | Arbitrary density-based | Good with indexing |
| GMM | Elliptical | Medium |

---

## Mathematical Intuition

**K-Means = Voronoi Partitioning**: Space divided by perpendicular bisectors between centroids.

**Optimization Perspective**: K-Means alternates between:
1. **Assignment step**: Minimize wrt cluster assignments (E-step)
2. **Update step**: Minimize wrt centroids (M-step)
This is coordinate descent on WCSS — guaranteed to converge to local minimum.

**Soft vs Hard**: 
- Hard: $z_{ik} \in \{0,1\}$ (K-Means, K-Medoids)
- Soft: $z_{ik} \in [0,1]$, $\sum_k z_{ik}=1$ (GMM)

---

## Algorithms

### Choosing K (Number of Clusters)

**Elbow Method**: Plot WCSS vs K, look for "elbow" (diminishing returns)

**Silhouette Analysis**: Compute avg silhouette for each K, pick max

**Gap Statistic**: Compare WCSS to null reference distribution

**Cross-Validation**: Stability of clusters across subsamples

### General Clustering Pipeline
```
1. Preprocess: Scale features!
2. Choose distance metric
3. Choose algorithm (K-Means, Hierarchical, DBSCAN, GMM)
4. Select K (elbow, silhouette, gap stat, domain knowledge)
5. Run clustering (multiple random starts for K-Means)
6. Evaluate: internal (silhouette, DB, CH) + external (if labels)
7. Visualize: PCA/t-SNE projection colored by cluster
```

---

## Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| K-Means | $O(n \cdot K \cdot p \cdot \text{iter})$ | $O(n \cdot p + K \cdot p)$ |
| K-Medoids (PAM) | $O(K(n-K)^2 \cdot \text{iter})$ | $O(n \cdot p)$ |
| Hierarchical (Agglomerative) | $O(n^2)$ to $O(n^3)$ | $O(n^2)$ |
| DBSCAN | $O(n \log n)$ with indexing | $O(n \cdot p)$ |
| GMM (EM) | $O(n \cdot K \cdot p^2 \cdot \text{iter})$ | $O(K \cdot p^2)$ |

---

## Comparison Tables

### Clustering Algorithm Comparison

| Aspect | K-Means | K-Medoids | Hierarchical | DBSCAN | GMM |
|--------|---------|-----------|--------------|--------|-----|
| **Cluster Shape** | Spherical | Any (metric) | Any | Arbitrary | Elliptical |
| **Scalability** | Good | Medium | Poor | Good | Medium |
| **Outliers** | Sensitive | Robust | Sensitive | **Handles** | Sensitive |
| **K Required** | Yes | Yes | No (dendrogram) | No (eps, minPts) | Yes |
| **Soft/Hard** | Hard | Hard | Hard | Hard | **Soft** |
| **Deterministic** | No (random init) | No | Yes | Yes | No (random init) |

### When to Use Which

| Scenario | Recommended |
|----------|-------------|
| Large n, spherical clusters, K known | K-Means |
| Outliers present, any metric | K-Medoids |
| Small n, need hierarchy, unknown K | Hierarchical |
| Arbitrary shapes, noise/outliers | DBSCAN |
| Probabilistic assignment, elliptical | GMM |

---

## GATE Tricks

> [!tip] **Clustering Quick Rules**
> - **SCALE FEATURES FIRST** — essential for all distance-based clustering!
> - **K-Means** = spherical clusters, centroid = mean
> - **K-Medoids** = robust to outliers, medoid = actual point
> - **Hierarchical** = dendrogram, no K needed initially
> - **DBSCAN** = density-based, finds arbitrary shapes, handles noise
> - **GMM** = soft clustering, elliptical clusters
> - **Elbow/Silhouette** for choosing K
> - **Multiple runs** for K-Means (different inits)

> [!warning] **GATE Traps**
> - **Unscaled features** → large-scale features dominate distance
> - **K-Means on non-spherical clusters** → fails (use GMM/DBSCAN)
> - **Single K-Means run** → local optimum (use k-means++ init, multiple runs)
> - **t-SNE for clustering** → t-SNE is for visualization only!
> - **Hierarchical on large n** → O(n²) memory/time impractical

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| K-Means | K-Medoids | Mean vs actual point as center |
| Hard Clustering | Soft Clustering | Single assignment vs probabilities |
| Hierarchical (Agglomerative) | Divisive | Bottom-up vs Top-down |
| DBSCAN | K-Means | Density-based vs centroid-based |
| Silhouette | Elbow | Cohesion/separation vs WCSS drop |

---

## Common Mistakes

1. **Forgetting to scale features** → wrong clusters
2. **Assuming K-Means works for all shapes** → only spherical
3. **Using elbow method blindly** → elbow often ambiguous
4. **Not running multiple initializations** for K-Means
5. **Using clustering results as features without validation**

---

## Memory Tricks

> [!tip] **K-Means** = **K** **Means** = K cluster means (centroids)
> 
> **K-Medoids** = **Medoid** = **Med**ian-like (actual point)
> 
> **DBSCAN** = **D**ensity-**B**ased **S**patial **C**lustering **A**pplications with **N**oise
> 
> **Hierarchical** = builds **Hierarchy** (tree) of clusters
> 
> **GMM** = **G**aussian **M**ixture **M**odel = probabilistic

---

## Previous GATE Patterns

- **Algorithm selection**: Given scenario, choose right clustering method
- **K selection**: Elbow method, silhouette interpretation
- **Distance metrics**: When to use Euclidean vs Cosine vs Mahalanobis
- **Complexity**: Time/space for different algorithms
- **Evaluation**: Internal metrics (silhouette, DB, CH)

---

## Revision Summary

```
CLUSTERING
├── Unsupervised: group similar points
├── Distance-based: SCALE FEATURES FIRST!
├── Algorithms:
│   ├── K-Means: spherical, centroid=mean, fast, sensitive to outliers
│   ├── K-Medoids: any metric, medoid=actual point, robust
│   ├── Hierarchical: dendrogram, O(n²), no K needed
│   ├── DBSCAN: density-based, arbitrary shapes, handles noise
│   └── GMM: soft, elliptical, probabilistic
├── Choose K: Elbow (WCSS), Silhouette, Gap Statistic
├── Evaluate: Silhouette (internal), ARI/NMI (external if labels)
├── K-Means = coordinate descent on WCSS (local optima)
└── Always run K-Means multiple times (k-means++ init)
```

---

## Related Notes

- [[19 K Means]]
- [[20 K Medoids]]
- [[21 Hierarchical Clustering]]
- [[22 Dimensionality Reduction]]
- [[23 Principal Component Analysis]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #clustering #unsupervised-learning #revision