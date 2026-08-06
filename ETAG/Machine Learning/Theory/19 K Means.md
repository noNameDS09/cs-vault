---
tags: [machine-learning, gate-da, kmeans, clustering, unsupervised-learning, revision]
---

# 19 K Means

> [!note] Centroid-based clustering minimizing **Within-Cluster Sum of Squares (WCSS)**

---

## Overview

K-Means partitions data into K clusters by iteratively assigning points to nearest centroid and updating centroids to cluster means. Simple, fast, and widely used — but assumes spherical clusters.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Centroid** | Mean of points in cluster: $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$ |
| **WCSS** | Within-Cluster Sum of Squares: $\sum_k \sum_{x \in C_k} ||x - \mu_k||^2$ |
| **Assignment Step** | Assign each point to nearest centroid |
| **Update Step** | Recompute centroids as cluster means |
| **k-means++** | Smart initialization to avoid poor local optima |

---

## Formulae

### Objective Function (WCSS)
$$
J = \sum_{k=1}^K \sum_{x \in C_k} ||x - \mu_k||^2
$$
where $\mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x$

### Algorithm Steps
**1. Initialize** K centroids $\mu_1, ..., \mu_K$ (random or k-means++)

**2. Assignment Step** (E-step):
$$
C_k = \{x : k = \arg\min_j ||x - \mu_j||^2\}
$$

**3. Update Step** (M-step):
$$
\mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x
$$

**4. Repeat 2-3 until convergence** (assignments don't change or max iterations)

### Convergence
- Objective decreases monotonically
- Converges to **local minimum** (not global)
- Finite number of partitions → guaranteed convergence in finite steps

### k-means++ Initialization
```
1. Choose first centroid uniformly at random from data
2. For each remaining centroid:
   - Compute D(x) = distance to nearest existing centroid
   - Choose next centroid with probability ∝ D(x)²
3. Proceed with standard K-Means
```

### Choosing K
**Elbow Method**: Plot WCSS vs K, find "elbow" where diminishing returns start

**Silhouette Score**: 
$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$
Average over all points — maximize over K

**Gap Statistic**: Compare log(WCSS) to null reference distribution

### Complexity
| Aspect | Complexity |
|--------|------------|
| Time per iteration | $O(n \cdot K \cdot p)$ |
| Total time | $O(n \cdot K \cdot p \cdot \text{iter})$ |
| Space | $O(n \cdot p + K \cdot p)$ |
| With k-means++ init | $O(n \cdot K \cdot p)$ extra |

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $K$ | Number of clusters |
| $\mu_k$ | Centroid of cluster $k$ |
| $C_k$ | Set of points assigned to cluster $k$ |
| $||x - \mu_k||^2$ | Squared Euclidean distance |
| WCSS | Within-Cluster Sum of Squares |

---

## Important Properties

### Assumptions / Limitations
1. **Spherical clusters** — equal variance in all directions
2. **Similar cluster sizes** — works poorly with imbalanced clusters
3. **Euclidean distance** — sensitive to outliers
4. **K known** — must specify number of clusters
5. **Convex clusters** — fails on non-convex shapes (crescents, circles)

### Relationship to Other Methods
- **K-Means = Gaussian Mixture Model** with $\Sigma_k = \sigma^2 I$, $\pi_k = 1/K$, hard assignment
- **K-Means = EM** for isotropic Gaussians with equal variance
- **Kernel K-Means**: Apply kernel trick for non-linear boundaries

### Variants
| Variant | Description |
|---------|-------------|
| **K-Means++** | Better initialization |
| **Mini-batch K-Means** | Subsample for large n |
| **K-Medoids** | Robust to outliers (actual points as centers) |
| **Fuzzy C-Means** | Soft assignment |
| **Kernel K-Means** | Non-linear via kernel trick |

---

## Mathematical Intuition

**Voronoi Diagram**: K-Means partitions space into convex polytopes (Voronoi cells) bounded by perpendicular bisectors between centroids.

**Coordinate Descent**: Alternating minimization of $J$:
- Fix $\mu$, optimize assignments → each point to nearest centroid
- Fix assignments, optimize $\mu$ → mean minimizes sum of squared distances

**Local Optima**: Different initializations → different solutions. Global optimum NP-hard.

---

## Algorithms

### Standard K-Means
```python
def kmeans(X, K, max_iter=300):
    # Initialize centroids
    centroids = X[np.random.choice(n, K, replace=False)]
    
    for _ in range(max_iter):
        # Assignment
        distances = np.sum((X[:, None] - centroids[None])**2, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Update
        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])
        
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids
```

### K-Means++ Initialization
```python
def kmeans_plusplus(X, K):
    centroids = [X[np.random.randint(n)]]
    for _ in range(1, K):
        dists = np.min([np.sum((X - c)**2, axis=1) for c in centroids], axis=0)
        probs = dists / dists.sum()
        centroids.append(X[np.random.choice(n, p=probs)])
    return np.array(centroids)
```

---

## Comparison Tables

### K-Means vs Variants

| Aspect | K-Means | K-Means++ | Mini-batch | K-Medoids |
|--------|---------|-----------|------------|-----------|
| **Init** | Random | Smart | Random | Random |
| **Convergence** | Local opt | Better local | Approximate | Local opt |
| **Speed** | Fast | Fast | **Very fast** | Slow |
| **Outliers** | Sensitive | Sensitive | Sensitive | **Robust** |
| **Large n** | Good | Good | **Best** | Poor |

### When K-Means Works / Fails

| Scenario | Works? |
|----------|--------|
| Spherical, well-separated | ✓ Yes |
| Different densities | ✗ No |
| Non-convex shapes (rings) | ✗ No |
| High dimensions (unscaled) | ✗ No |
| Outliers present | ✗ No |

---

## GATE Tricks

> [!tip] **K-Means Quick Rules**
> - **Objective**: Minimize WCSS = $\sum ||x - \mu||^2$
> - **Centroid** = **Mean** of cluster points
> - **Always scale features** first!
> - **k-means++ init** = much better than random
> - **Multiple runs** (n_init=10) to avoid local optima
> - **Elbow method** on WCSS for choosing K
> - **Silhouette** for evaluating clustering quality

> [!warning] **GATE Traps**
> - **K-Means assumes spherical clusters** — fails on elongated/ring shapes
> - **Sensitive to outliers** — single outlier can pull centroid
> - **Random initialization** → different results each run
> - **K must be specified** — no automatic K selection
> - **Doesn't work well with imbalanced cluster sizes**
> - **Distance metric fixed to Euclidean** (usually)

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| K-Means | K-Medoids | Centroid (mean) vs Medoid (actual point) |
| K-Means | GMM | Hard vs Soft; Spherical vs Elliptical |
| K-Means | KNN | Unsupervised clustering vs Supervised classification |
| WCSS | TSS | Within-cluster vs Total sum of squares |

---

## Common Mistakes

1. **Not scaling features** → wrong distances
2. **Single run** → stuck in bad local optimum
3. **Using on non-spherical clusters** → use DBSCAN/GMM
4. **Ignoring outliers** → preprocess or use K-Medoids
5. **Choosing K arbitrarily** → use elbow/silhouette

---

## Memory Tricks

> [!tip] **K-Means** = **K** cluster **Means** (centroids are means)
> 
> **WCSS** = **W**ithin-**C**luster **S**um of **S**quares
> 
> **k-means++** = "Plus plus" = better initialization
> 
> **Voronoi** = perpendicular bisectors between centroids

---

## Previous GATE Patterns

- **Numerical**: One iteration of K-Means (compute new centroids)
- **Elbow plot**: Interpret WCSS vs K curve
- **k-means++**: Probability proportional to squared distance
- **Complexity**: Time/space complexity
- **Limitations**: When K-Means fails
- **Comparison**: K-Means vs K-Medoids vs Hierarchical

---

## Revision Summary

```
K-MEANS
├── Objective: min WCSS = Σ||x - μₖ||²
├── Centroid μₖ = mean of cluster points
├── Algorithm: Alternate assignment + update
├── Converges to LOCAL minimum (not global)
├── k-means++ init: prob ∝ distance² to nearest centroid
├── FEATURE SCALING MANDATORY
├── Choose K: Elbow (WCSS), Silhouette, Gap Statistic
├── Complexity: O(n·K·p·iter) time, O(n·p) space
├── Assumptions: Spherical, similar size, convex clusters
├── Fails on: Non-convex, imbalanced, outliers, high-dim (unscaled)
├── Variants: K-Means++, Mini-batch, Kernel K-Means
└── K-Means = Hard EM for isotropic Gaussians
```

---

## Related Notes

- [[18 Clustering]]
- [[20 K Medoids]]
- [[21 Hierarchical Clustering]]
- [[23 Principal Component Analysis]] (for visualization)
- [[Formula Sheet]]

---

#machine-learning #gate-da #kmeans #clustering #revision