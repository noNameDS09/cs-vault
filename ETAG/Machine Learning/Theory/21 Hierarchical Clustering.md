---
tags: [machine-learning, gate-da, hierarchical-clustering, unsupervised-learning, revision]
---

# 21 Hierarchical Clustering

> [!note] Builds a tree of clusters (dendrogram) — no need to specify K in advance

---

## Overview

Hierarchical clustering creates a nested sequence of partitions, represented as a dendrogram. Two main approaches: Agglomerative (bottom-up) and Divisive (top-down). Linkage criteria determine inter-cluster distances.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Agglomerative** | Bottom-up: start with n clusters, merge iteratively |
| **Divisive** | Top-down: start with 1 cluster, split recursively |
| **Dendrogram** | Tree diagram showing merge/split hierarchy |
| **Linkage** | Criterion for distance between clusters |
| **Cut** | Horizontal line on dendrogram to get K clusters |

---

## Formulae

### Linkage Criteria

**Single Linkage** (Minimum):
$$
d(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x, y)
$$
*Chaining effect — can create elongated clusters*

**Complete Linkage** (Maximum):
$$
d(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x, y)
$$
*Compact clusters — sensitive to outliers*

**Average Linkage** (UPGMA):
$$
d(C_i, C_j) = \frac{1}{|C_i||C_j|} \sum_{x \in C_i} \sum_{y \in C_j} d(x, y)
$$
*Balanced — often works well*

**Centroid Linkage** (UPGMC):
$$
d(C_i, C_j) = ||\mu_i - \mu_j||^2
$$
*Uses cluster centroids*

**Ward's Linkage** (Minimum Variance):
$$
d(C_i, C_j) = \frac{|C_i||C_j|}{|C_i| + |C_j|} ||\mu_i - \mu_j||^2
$$
*Minimizes increase in WCSS — tends to create equal-sized clusters*

### Agglomerative Algorithm
```
1. Start with each point as cluster: C = {{x₁}, {x₂}, ..., {xₙ}}
2. Compute proximity matrix P[i,j] = d(Cᵢ, Cⱼ)
3. While |C| > 1:
   a. Find closest pair (i*, j*) = argmin P[i,j]
   b. Merge Cᵢ* and Cⱼ* → new cluster C_new
   c. Update proximity matrix:
      For each other cluster C_k:
        P[k, new] = linkage(C_k, C_new)
   d. Remove i*, j* from C, add C_new
4. Return dendrogram
```

### Lance-Williams Formula (Efficient Update)
For many linkages, new distance can be computed without recomputing all pairwise distances:
$$
d(C_k, C_i \cup C_j) = \alpha_i d(C_k, C_i) + \alpha_j d(C_k, C_j) + \beta d(C_i, C_j) + \gamma |d(C_k, C_i) - d(C_k, C_j)|
$$

| Linkage | $\alpha_i$ | $\alpha_j$ | $\beta$ | $\gamma$ |
|---------|------------|------------|---------|----------|
| Single | 0.5 | 0.5 | 0 | -0.5 |
| Complete | 0.5 | 0.5 | 0 | 0.5 |
| Average | $\frac{|C_i|}{|C_i|+|C_j|}$ | $\frac{|C_j|}{|C_i|+|C_j|}$ | 0 | 0 |
| Ward | $\frac{|C_k|+|C_i|}{|C_k|+|C_i|+|C_j|}$ | $\frac{|C_k|+|C_j|}{|C_k|+|C_i|+|C_j|}$ | $-\frac{|C_k|}{|C_k|+|C_i|+|C_j|}$ | 0 |

### Divisive Algorithm
```
1. Start with all points in one cluster
2. While clusters can be split:
   a. Choose cluster to split (e.g., largest diameter)
   b. Split using 2-means or farthest point heuristic
3. Return dendrogram
```
*Computationally harder — rarely used in practice*

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $C_i, C_j$ | Clusters |
| $d(C_i, C_j)$ | Inter-cluster distance (linkage) |
| $\mu_i$ | Centroid of cluster $i$ |
| $|C_i|$ | Size of cluster $i$ |
| Dendrogram | Tree showing merge history |

---

## Important Properties

### Linkage Comparison

| Linkage | Cluster Shape | Outlier Sensitivity | Chaining | Typical Use |
|---------|---------------|---------------------|----------|-------------|
| Single | Elongated, irregular | High | **Yes** | Rare |
| Complete | Compact, spherical | High | No | Good default |
| Average | Moderate | Medium | Mild | Good default |
| Ward | Spherical, equal size | Medium | No | **Best for spherical** |

### Dendrogram Interpretation
- **Height of merge** = distance between merged clusters
- **Long vertical lines** = well-separated clusters
- **Cut at height h** → clusters with merge distance ≤ h
- **Number of clusters** = number of vertical lines crossed

### Complexity
| Approach | Time | Space |
|----------|------|-------|
| Agglomerative (naive) | $O(n^3)$ | $O(n^2)$ |
| Agglomerative (priority queue) | $O(n^2 \log n)$ | $O(n^2)$ |
| Divisive | $O(n^2 \log n)$ to $O(n^3)$ | $O(n^2)$ |

*Much slower than K-Means — impractical for large n (>10K)*

---

## Mathematical Intuition

**Agglomerative = Greedy Merging**: At each step, merge the two "most similar" clusters. Greedy — not globally optimal.

**Single Linkage = Minimum Spanning Tree**: The dendrogram from single linkage corresponds to MST of the proximity graph.

**Ward = Variance Minimization**: Equivalent to K-Means objective but hierarchical. Minimizes $\Delta WCSS$ at each merge.

**Ultrametric**: Dendrogram defines ultrametric distance: $d(x,y) \leq \max(d(x,z), d(z,y))$

---

## Algorithms

### Agglomerative Clustering (Scikit-learn style)
```python
from sklearn.cluster import AgglomerativeClustering

# No need to specify n_clusters if using distance_threshold
model = AgglomerativeClustering(
    n_clusters=None,
    distance_threshold=0,
    linkage='ward',  # or 'complete', 'average', 'single'
    metric='euclidean'  # or 'precomputed' for distance matrix
)
labels = model.fit_predict(X)
```

### Extracting K Clusters from Dendrogram
```python
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# linkage matrix
Z = linkage(X, method='ward')

# Plot dendrogram
dendrogram(Z)

# Get clusters by cutting at K
labels = fcluster(Z, K, criterion='maxclust')

# Or cut by distance threshold
labels = fcluster(Z, t=threshold, criterion='distance')
```

---

## Comparison Tables

### Hierarchical vs K-Means

| Aspect | Hierarchical | K-Means |
|--------|--------------|---------|
| **K required** | No (dendrogram) | Yes |
| **Scalability** | Poor (O(n²)) | Good (O(n)) |
| **Deterministic** | Yes (mostly) | No (random init) |
| **Cluster Shape** | Any (with right linkage) | Spherical |
| **Outliers** | Sensitive (complete/ward) | Sensitive |
| **Interpretability** | High (dendrogram) | Low |

### Linkage Selection Guide

| Data Characteristics | Recommended Linkage |
|---------------------|---------------------|
| Spherical, equal size | Ward |
| Compact, unknown size | Complete / Average |
| Elongated / irregular | Single (but beware chaining) |
| With outliers | Average / Ward (not Complete) |

---

## GATE Tricks

> [!tip] **Hierarchical Quick Rules**
> - **No K needed** — dendrogram shows all levels
> - **Agglomerative** = bottom-up (standard), **Divisive** = top-down (rare)
> - **Linkage** = how to measure cluster distance
> - **Ward** = minimizes variance increase (like K-Means)
> - **Single** = chaining effect (long clusters)
> - **Complete** = compact clusters
> - **Average** = balanced
> - **Cut dendrogram** at height to get K clusters
> - **O(n²) memory** — impractical for large n

> [!warning] **GATE Traps**
> - **Single linkage chaining** — merges closest pair regardless of cluster shape
> - **Complete linkage sensitive to outliers** — one outlier increases all distances
> - **Ward requires Euclidean** — uses centroid distances
> - **Distance matrix O(n²)** — can't scale to large datasets
> - **Deterministic but not optimal** — greedy merges
> - **Standardize features first!**

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Agglomerative | Divisive | Bottom-up vs Top-down |
| Single | Complete | Min vs Max distance |
| Ward | K-Means | Hierarchical vs Flat; both minimize variance |
| Dendrogram height | Distance | Height = merge distance |
| Linkage | Distance metric | Linkage = inter-cluster; metric = inter-point |

---

## Common Mistakes

1. **Using on large datasets** → O(n²) memory/time
2. **Not scaling features** → distances dominated by large-scale features
3. **Using single linkage** → chaining creates poor clusters
4. **Using Ward with non-Euclidean** → Ward needs centroid distances
5. **Not visualizing dendrogram** → always check before cutting

---

## Memory Tricks

> [!tip] **Agglomerative** = **Agg**lomerate = gather together (bottom-up)
> 
> **Divisive** = **Div**ide = split apart (top-down)
> 
> **Single** = **S**ingle closest pair = min
> 
> **Complete** = **C**omplete farthest pair = max
> 
> **Ward** = **W**ard off variance = minimize WCSS increase
> 
> **Dendrogram** = **Den**dro = tree (Greek)

---

## Previous GATE Patterns

- **Linkage comparison**: Given cluster shapes, choose linkage
- **Lance-Williams**: Compute updated distance after merge
- **Dendrogram reading**: Determine K from dendrogram cut
- **Complexity**: O(n²) or O(n³) — why not for large n
- **Ward vs K-Means**: Both minimize variance
- **Single linkage = MST**: Connection to graph theory

---

## Revision Summary

```
HIERARCHICAL CLUSTERING
├── Agglomerative (bottom-up): start n clusters, merge closest
├── Divisive (top-down): start 1 cluster, split recursively
├── Linkage criteria:
│   ├── Single: min distance (chaining)
│   ├── Complete: max distance (compact)
│   ├── Average: mean distance (balanced)
│   └── Ward: min variance increase (spherical, equal)
├── Dendrogram: tree of merges, height = distance
├── Cut dendrogram → K clusters
├── Lance-Williams: O(1) distance updates
├── Complexity: O(n²) to O(n³) — small n only
├── Deterministic (mostly), no K needed upfront
└── FEATURE SCALING MANDATORY
```

---

## Related Notes

- [[18 Clustering]]
- [[19 K Means]]
- [[20 K Medoids]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #hierarchical-clustering #unsupervised-learning #revision