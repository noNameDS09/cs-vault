---
tags: [machine-learning, gate-da, knn, classification, revision]
---

# 07 K Nearest Neighbour (KNN)

> [!note] Instance-based / lazy learning: classify by majority vote of k nearest neighbors

---

## Overview

KNN is a non-parametric, instance-based classifier. No training phase - just stores training data. Prediction = majority vote of k nearest neighbors.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Lazy Learning** | No model training; computation deferred to prediction |
| **Instance-Based** | Uses training instances directly for prediction |
| **Distance Metric** | Euclidean, Manhattan, Minkowski, Cosine |
| **k** | Number of neighbors (hyperparameter) |
| **Majority Vote** | Most common class among k neighbors |
| **Weighted Vote** | Weight by inverse distance |

---

## Formulae

### Distance Metrics

**Euclidean (L2)**:
$$
d(x, x') = \sqrt{\sum_{j=1}^p (x_j - x'_j)^2}
$$

**Manhattan (L1)**:
$$
d(x, x') = \sum_{j=1}^p |x_j - x'_j|
$$

**Minkowski (General)**:
$$
d(x, x') = \left( \sum_{j=1}^p |x_j - x'_j|^q \right)^{1/q}
$$
- $q=1$: Manhattan
- $q=2$: Euclidean
- $q \to \infty$: Chebyshev (max)

**Cosine Similarity**:
$$
\text{sim}(x, x') = \frac{x^T x'}{||x|| \cdot ||x'||}
$$
$$
d_{\text{cosine}} = 1 - \text{sim}(x, x')
$$

**Mahalanobis** (accounts for covariance):
$$
d(x, x') = \sqrt{(x - x')^T \Sigma^{-1} (x - x')}
$$

### Prediction

**Unweighted Majority Vote**:
$$
\hat{y} = \text{mode}\{y_i : x_i \in N_k(x)\}
$$
where $N_k(x)$ = k nearest neighbors of $x$

**Weighted Vote** (inverse distance):
$$
\hat{y} = \arg\max_c \sum_{x_i \in N_k(x)} w_i \mathbb{I}(y_i = c)
$$
$$
w_i = \frac{1}{d(x, x_i)^\alpha} \quad (\alpha \geq 0)
$$

**Probability Estimate**:
$$
\hat{P}(y=c|x) = \frac{\sum_{x_i \in N_k(x)} w_i \mathbb{I}(y_i = c)}{\sum_{x_i \in N_k(x)} w_i}
$$

### Regression Version
$$
\hat{y} = \frac{1}{k}\sum_{x_i \in N_k(x)} y_i \quad \text{(unweighted)}
$$
$$
\hat{y} = \frac{\sum w_i y_i}{\sum w_i} \quad \text{(weighted)}
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $k$ | Number of neighbors |
| $p$ | Number of features |
| $n$ | Number of training samples |
| $N_k(x)$ | Set of k nearest neighbors of $x$ |
| $d(x, x')$ | Distance between $x$ and $x'$ |
| $w_i$ | Weight for neighbor $i$ |

---

## Important Properties

### Bias-Variance Tradeoff
- **Small k**: Low bias, high variance (overfitting, noisy boundaries)
- **Large k**: High bias, low variance (underfitting, oversmoothed)
- Optimal $k$ typically via cross-validation

### Curse of Dimensionality
- In high dimensions, all points become equidistant
- Distance concentration: $\frac{d_{\max} - d_{\min}}{d_{\min}} \to 0$
- KNN degrades significantly for $p \gg 20$

### Asymptotic Consistency
- As $n \to \infty$, $k \to \infty$, $k/n \to 0$: KNN error → Bayes error
- 1-NN error $\leq 2 \times$ Bayes error

### No Training Phase
- Training: $O(1)$ (just store data)
- Space: $O(np)$
- Prediction: $O(np)$ naive, $O(p \log n)$ with KD-tree

---

## Mathematical Intuition

**Voronoi Diagram**: 1-NN partitions space into cells (Voronoi diagram) where each cell contains points closest to one training sample.

**Decision Boundary**: Piecewise linear (1-NN) or smooth (large k) boundaries formed by perpendicular bisectors between points of different classes.

**Local Averaging**: KNN estimates $P(y|x)$ by local averaging around $x$.

---

## Algorithms

### Naive Prediction
```
1. Compute distances from x to all training points
2. Sort distances, take k smallest
3. Return majority class (or weighted majority)
```

### KD-Tree (for low dimensions, p < 20)
```
Build: Recursively split space on median of highest-variance dimension
Query: Traverse tree, prune branches using bounding boxes
Complexity: O(p n log n) build, O(p log n) query (average)
```

### Ball Tree (better for high dimensions)
```
Build: Recursively partition into hyper-spheres
Query: Use triangle inequality to prune
```

### Cross-Validation for k
```
For k in {1, 3, 5, ..., 31}:
    Compute CV error
Select k with minimum CV error
```

---

## Complexity

| Operation | Naive | KD-Tree (p<20) | Ball Tree |
|-----------|-------|----------------|-----------|
| Training | $O(1)$ | $O(pn \log n)$ | $O(pn \log n)$ |
| Prediction | $O(np)$ | $O(p \log n)$ | $O(p \log n)$ |
| Space | $O(np)$ | $O(np)$ | $O(np)$ |

---

## Comparison Tables

### KNN vs Other Classifiers

| Aspect | KNN | Logistic Regression | SVM | Decision Tree |
|--------|-----|---------------------|-----|---------------|
| Training | None (lazy) | Iterative | Quadratic programming | Greedy |
| Decision Boundary | Piecewise | Linear | Linear/Nonlinear (kernel) | Axis-aligned |
| Interpretability | Low | High | Low | High |
| Feature Scaling | **Critical** | Helpful | Critical | Not needed |
| High Dimensions | Poor | OK | Good (with kernel) | OK |

### Distance Metric Choice

| Data Type | Recommended Metric |
|-----------|-------------------|
| Continuous, similar scales | Euclidean |
| Continuous, different scales | Standardized Euclidean / Mahalanobis |
| Binary / Categorical | Hamming / Jaccard |
| Text (TF-IDF) | Cosine |
| Sparse vectors | Cosine / Jaccard |

---

## GATE Tricks

> [!tip] **KNN Quick Rules**
> - **Feature scaling is MANDATORY** (distance-based!)
> - **k odd** for binary classification (avoids ties)
> - **k = 1**: Overfits, error ≤ 2× Bayes error
> - **k large**: Underfits, approaches majority class
> - **Curse of dimensionality**: KNN fails for high $p$ (use PCA first)
> - **No training time** but **slow prediction** for large $n$
> - **Weighted vote** with $1/d^2$ usually better than uniform

> [!warning] **GATE Traps**
> - Forgetting to scale features → features with large range dominate
> - Using Euclidean on categorical data → meaningless
> - Large $k$ with imbalanced data → always predicts majority class
> - KD-tree degrades to linear scan for $p > 20$

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| KNN (classification) | K-Means (clustering) | Supervised vs Unsupervised |
| Euclidean | Manhattan | L2 vs L1 norm |
| 1-NN | k-NN (k>1) | Noisy vs smooth boundaries |
| Lazy | Eager | No training vs training phase |

---

## Common Mistakes

1. **No feature scaling** → large-scale features dominate distance
2. **Using k=1** → very sensitive to noise/outliers
3. **Even k for binary** → ties possible
4. **High dimensions without PCA** → distance meaningless
5. **Not handling ties** in voting
6. **Using on large datasets** without approximate methods (slow!)

---

## Memory Tricks

> [!tip] **KNN** = "K Nearest Neighbors" = **Lazy** (no training)
> 
> **K-Means** = "K Means" = **Eager** (clustering, unsupervised)
> 
> **Scale features** = "Level the playing field"
> 
> **k odd** = "No ties in binary"

---

## Previous GATE Patterns

- **Numerical**: Compute distances, find neighbors, predict class
- **Distance calculation**: Euclidean, Manhattan, Cosine
- **Effect of k**: Bias-variance tradeoff
- **Curse of dimensionality**: Why KNN fails in high dimensions
- **Comparison**: KNN vs K-Means, KNN vs other classifiers
- **Feature scaling**: Why it's critical for KNN

---

## Revision Summary

```
K-NEAREST NEIGHBORS
├── Lazy learning: no training, just store data
├── Prediction: majority vote of k nearest neighbors
├── Distance: Euclidean (default), Manhattan, Cosine, Mahalanobis
├── FEATURE SCALING MANDATORY!
├── k small → low bias, high variance (overfit)
├── k large → high bias, low variance (underfit)
├── Optimal k via cross-validation
├── Weighted vote: weight = 1/d² (better)
├── Curse of dimensionality: fails for high p
├── 1-NN error ≤ 2 × Bayes error
├── KD-tree for p < 20, Ball tree for higher
└── Regression: average of k neighbor targets
```

---

## Related Notes

- [[20 K Medoids]] (similar but unsupervised)
- [[18 Clustering]]
- [[22 Dimensionality Reduction]] (PCA before KNN)
- [[Formula Sheet]]

---

#machine-learning #gate-da #knn #classification #revision