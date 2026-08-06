---
tags: [machine-learning, gate-da, kmedoids, clustering, unsupervised-learning, revision]
---

# 20 K Medoids

> [!note] Medoid-based clustering — more robust to outliers than K-Means

---

## Overview

K-Medoids (Partitioning Around Medoids - PAM) is similar to K-Means but uses **actual data points** as cluster centers (medoids) instead of means. More robust to outliers and works with any distance metric.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Medoid** | Actual data point minimizing sum of distances to other points in cluster |
| **PAM** | Partitioning Around Medoids (standard algorithm) |
| **CLARA** | Clustering Large Applications (sampling for scalability) |
| **CLARANS** | Randomized search for large datasets |
| **Robustness** | Less sensitive to outliers than K-Means |

---

## Formulae

### Objective Function
$$
\min_{C_1,...,C_K} \sum_{k=1}^K \sum_{x \in C_k} d(x, m_k)
$$
where $m_k \in C_k$ is the **medoid** (actual data point)

### Medoid Definition
$$
m_k = \arg\min_{x \in C_k} \sum_{y \in C_k} d(x, y)
$$

### PAM Algorithm (Exact)
**BUILD Phase** (initialization):
1. Choose first medoid: point minimizing total distance to all others
2. Iteratively add medoid that most reduces objective

**SWAP Phase** (optimization):
For each medoid $m$ and non-medoid $x$:
- Compute cost change if swap $m \leftrightarrow x$
- If negative (improvement), perform swap
- Repeat until no improving swaps

### Cost Change for Swap
Let $m$ be current medoid, $x$ be candidate non-medoid.
For each point $y$:
- If $y$ assigned to $m$:
  - New distance = $d(y, x)$
  - Change = $d(y, x) - d(y, m)$
- If $y$ assigned to another medoid $m'$:
  - New distance = $\min(d(y, m'), d(y, x))$
  - Change = $\min(d(y, m'), d(y, x)) - d(y, m')$

Total change = sum over all points.

### CLARA (For Large Datasets)
1. Draw multiple samples of size $s$ (e.g., 40+2K)
2. Run PAM on each sample
3. Select best medoids
4. Assign all points to nearest selected medoid

### Choosing K
Same as K-Means: Elbow method, Silhouette, Gap Statistic

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $K$ | Number of clusters |
| $m_k$ | Medoid of cluster $k$ (actual data point) |
| $C_k$ | Points assigned to cluster $k$ |
| $d(x, y)$ | Distance metric (any) |
| $n$ | Number of data points |

---

## Important Properties

### Medoid vs Centroid
| Property | Centroid (K-Means) | Medoid (K-Medoids) |
|----------|-------------------|-------------------|
| **Definition** | Mean of points | Actual data point |
| **Robustness** | Sensitive to outliers | Robust to outliers |
| **Distance** | Euclidean only | Any metric |
| **Interpretability** | May not be real point | Always a real observation |
| **Computation** | Fast (mean) | Slower (search) |

### Distance Metrics
K-Medoids works with **any distance metric**:
- Euclidean, Manhattan, Cosine
- Mahalanobis
- Custom dissimilarity matrices
- Categorical data (Hamming, Jaccard)

### Complexity
| Algorithm | Time | Space |
|-----------|------|-------|
| PAM (exact) | $O(K(n-K)^2 \cdot \text{iter})$ | $O(n^2)$ for distance matrix |
| CLARA | $O(K s^2 \cdot \text{samples})$ | $O(s^2)$ |
| CLARANS | $O(K \cdot \text{maxneighbor} \cdot n)$ | $O(n)$ |

*Much slower than K-Means for large $n$*

---

## Mathematical Intuition

**Medoid = Fermat-Weber Point**: In 1D, median minimizes sum of absolute distances. In higher dimensions, medoid is discrete version.

**PAM = Local Search**: Explores neighborhood of current medoids by swapping. Guaranteed to find local optimum.

**Why Robust?**: Outlier affects mean (centroid) proportionally to its distance. Medoid only affected if outlier becomes medoid (unlikely since it increases distances to others).

---

## Algorithms

### PAM Algorithm
```python
def pam(X, K, distance_matrix=None):
    if distance_matrix is None:
        D = pairwise_distances(X)  # O(n²)
    else:
        D = distance_matrix
    
    # BUILD: Greedy initialization
    medoids = build_phase(D, K)
    
    # SWAP: Local improvement
    while True:
        best_swap = None
        best_cost = 0
        
        for m_idx in medoids:
            for x_idx in non_medoids:
                cost_change = compute_swap_cost(D, medoids, m_idx, x_idx)
                if cost_change < best_cost:
                    best_cost = cost_change
                    best_swap = (m_idx, x_idx)
        
        if best_swap is None:
            break
        
        # Perform swap
        medoids.remove(best_swap[0])
        medoids.add(best_swap[1])
    
    # Assign points to nearest medoid
    labels = assign_clusters(D, medoids)
    return labels, medoids
```

---

## Comparison Tables

### K-Medoids vs K-Means

| Aspect | K-Means | K-Medoids (PAM) |
|--------|---------|-----------------|
| **Center** | Centroid (mean) | Medoid (actual point) |
| **Outliers** | Sensitive | Robust |
| **Distance** | Euclidean | Any metric |
| **Speed** | Fast O(n·K·p) | Slow O(K·n²) |
| **Scalability** | Good | Poor (use CLARA/CLARANS) |
| **Categorical Data** | No | Yes |
| **Initialization** | k-means++ | BUILD phase |

### When to Use K-Medoids
| Scenario | Use K-Medoids? |
|----------|----------------|
| Outliers present | ✓ Yes |
| Non-Euclidean distance | ✓ Yes |
| Categorical/mixed data | ✓ Yes |
| Interpretability needed | ✓ Yes |
| Large n (>10K) | ✗ Use CLARA/CLARANS |
| Spherical clusters, no outliers | ✗ K-Means better |

---

## GATE Tricks

> [!tip] **K-Medoids Quick Rules**
> - **Medoid = actual data point** (not mean)
> - **Robust to outliers** — outlier can't pull medoid
> - **Any distance metric** — Manhattan, Cosine, custom
> - **PAM = exact but slow** O(K·n²)
> - **CLARA/CLARANS** for large datasets
> - **Works with categorical data** (unlike K-Means)

> [!warning] **GATE Traps**
> - **Much slower than K-Means** — don't use for large n without CLARA
> - **Still needs K specified** — no automatic K selection
> - **Local optima** — multiple runs recommended
> - **Distance matrix O(n²) memory** — impractical for very large n
> - **Not guaranteed global optimum** — local search

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| K-Means | K-Medoids | Centroid (mean) vs Medoid (actual point) |
| PAM | CLARA | Exact on sample vs sampling-based |
| Medoid | Median | Multivariate generalization of median |
| K-Medoids | DBSCAN | Medoid-based vs Density-based |

---

## Common Mistakes

1. **Using PAM on large datasets** → use CLARA/CLARANS
2. **Not computing distance matrix efficiently** → O(n²) bottleneck
3. **Assuming global optimum** → only local
4. **Forgetting K must be specified**
5. **Using Euclidean when other metric better**

---

## Memory Tricks

> [!tip] **Medoid** = **Med**ian-like = actual data point
> 
> **PAM** = **P**artitioning **A**round **M**edoids
> 
> **CLARA** = **C**lustering **L**arge **A**pplications
> 
> **Robust** = outlier can't pull medoid (unlike centroid)

---

## Previous GATE Patterns

- **Comparison**: K-Means vs K-Medoids (robustness, distance metrics)
- **Algorithm**: PAM BUILD and SWAP phases
- **Scalability**: CLARA/CLARANS for large n
- **Distance metrics**: When K-Medoids preferred (non-Euclidean)
- **Categorical data**: K-Medoids works, K-Means doesn't

---

## Revision Summary

```
K-MEDOIDS (PAM)
├── Objective: min Σ d(x, mₖ) where mₖ ∈ Cₖ (actual point)
├── Medoid = point minimizing sum of distances to cluster
├── PAM Algorithm:
│   ├── BUILD: Greedy initialization
│   └── SWAP: Try all medoid↔non-medoid swaps, keep improving
├── Robust to outliers (unlike K-Means)
├── Works with ANY distance metric
├── Handles categorical/mixed data
├── Complexity: O(K·n²) — slow for large n
├── CLARA: Sample → PAM → best medoids → assign all
├── CLARANS: Randomized neighbor search
└── Still needs K specified, local optima possible
```

---

## Related Notes

- [[18 Clustering]]
- [[19 K Means]]
- [[21 Hierarchical Clustering]]
- [[Formula Sheet]]

---

#machine-learning #gate-da #kmedoids #clustering #revision