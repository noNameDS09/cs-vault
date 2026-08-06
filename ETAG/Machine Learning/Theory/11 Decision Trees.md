---
tags: [machine-learning, gate-da, decision-trees, classification, regression, revision]
---

# 11 Decision Trees

> [!note] Recursive partitioning of feature space into axis-aligned rectangles

---

## Overview

Decision trees recursively split the feature space using axis-aligned splits. Each internal node tests a feature, each leaf predicts a value. Used for both classification and regression.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Root Node** | Top node containing all data |
| **Internal Node** | Decision rule: $x_j \leq t$ |
| **Leaf/Terminal Node** | Prediction value |
| **Split** | Partition based on feature threshold |
| **Impurity Measure** | Gini, Entropy (classification), MSE (regression) |
| **Pruning** | Removing branches to prevent overfitting |

---

## Formulae

### Impurity Measures (Classification)

**Gini Impurity**:
$$
G = 1 - \sum_{k=1}^K p_k^2
$$
where $p_k$ = proportion of class $k$ in node

**Entropy**:
$$
H = -\sum_{k=1}^K p_k \log_2 p_k
$$

**Misclassification Error**:
$$
E = 1 - \max_k p_k
$$

### Impurity Measure (Regression)
$$
\text{MSE} = \frac{1}{N} \sum_{i \in \text{node}} (y_i - \bar{y})^2
$$
where $\bar{y}$ = mean target in node

### Information Gain (Split Criterion)
$$
IG = I(\text{parent}) - \sum_{c \in \{\text{left}, \text{right}\}} \frac{N_c}{N} I(\text{child}_c)
$$
- $I$ = Gini, Entropy, or MSE
- Maximize IG = Minimize weighted child impurity

### Gini Gain (Specific)
$$
\Delta G = G_{\text{parent}} - \left( \frac{N_L}{N} G_L + \frac{N_R}{N} G_R \right)
$$

### Best Split Search
For each feature $j$:
- Sort unique values
- Try thresholds between adjacent values
- Compute IG for each
- Pick $(j^*, t^*)$ maximizing IG

### Cost-Complexity Pruning (CCP)
$$
R_\alpha(T) = R(T) + \alpha |\text{leaves}(T)|
$$
- $R(T)$ = total impurity (training error)
- $|\text{leaves}(T)|$ = number of leaves
- $\alpha$ = complexity parameter
- Larger $\alpha$ → smaller tree

### Minimal Cost-Complexity Pruning Algorithm
```
1. Grow large tree T_max
2. For each α: find subtree T_α minimizing R_α(T)
3. Sequence of subtrees T_0 ⊃ T_1 ⊃ ... ⊃ {root}
4. Select α via cross-validation
```

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $p_k$ | Proportion of class $k$ in node |
| $N$ | Number of samples in node |
| $N_L, N_R$ | Samples in left/right child |
| $t$ | Threshold for split $x_j \leq t$ |
| $\alpha$ | Complexity parameter (pruning) |
| $R(T)$ | Training impurity/error of tree T |

---

## Important Properties

### Axis-Aligned Splits
- Decision boundaries are perpendicular to axes
- Rectangular regions in feature space
- Cannot represent diagonal boundaries directly

### Greedy Construction
- Top-down, locally optimal splits
- Not guaranteed globally optimal
- NP-hard to find globally optimal tree

### No Feature Scaling Needed
- Splits based on ordering, not distances
- Invariant to monotonic transformations

### Handling Missing Values
- Surrogate splits (use correlated feature)
- Probabilistic assignment
- Treat as separate category

### Variable Importance
$$
\text{Importance}(j) = \sum_{t \in \text{splits on } j} \frac{N_t}{N} \cdot \text{IG}_t
$$
Sum of weighted impurity decreases over all splits using feature $j$

---

## Mathematical Intuition

**Recursive Partitioning**: Each split divides feature space into two half-spaces $\{x: x_j \leq t\}$ and $\{x: x_j > t\}$.

**Piecewise Constant**: Tree approximates $f(x)$ by constant on each leaf region.

**Information Theory**: Entropy = expected bits to encode class. IG = reduction in uncertainty.

**Bias-Variance**: Deep trees = low bias, high variance. Pruning increases bias, reduces variance.

---

## Algorithms

### CART (Classification and Regression Trees) - Standard
```
function BUILD_TREE(data, depth):
    if stopping_criterion(data):
        return Leaf(mean(data.y) for regression, mode(data.y) for classification)
    
    best_split = None
    best_gain = -∞
    
    for each feature j:
        for each threshold t:
            left, right = split(data, j, t)
            gain = information_gain(data, left, right)
            if gain > best_gain:
                best_gain = gain
                best_split = (j, t)
    
    if best_gain < min_gain:
        return Leaf(...)
    
    left_data, right_data = split(data, best_split)
    return Node(
        feature=best_split.j,
        threshold=best_split.t,
        left=BUILD_TREE(left_data, depth+1),
        right=BUILD_TREE(right_data, depth+1)
    )
```

### Stopping Criteria
- Max depth reached
- Min samples per leaf (e.g., 5)
- Min samples to split (e.g., 10)
- Max leaf nodes
- Min impurity decrease

---

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Training | $O(n p \log n)$ (sorted) | $O(n p)$ |
| Training | $O(n p \cdot \text{depth})$ (naive) | $O(n p)$ |
| Prediction | $O(\text{depth})$ | $O(1)$ |

---

## Comparison Tables

### Gini vs Entropy

| Aspect | Gini | Entropy |
|--------|------|---------|
| Range | $[0, 0.5]$ | $[0, \log_2 K]$ |
| Computation | Faster (no log) | Slower |
| Shape | Similar | Similar |
| Splits | Slightly more balanced | Slightly more balanced |

### Classification vs Regression Trees

| Aspect | Classification | Regression |
|--------|---------------|------------|
| Impurity | Gini / Entropy | MSE / MAE |
| Leaf Value | Majority class | Mean target |
| Split Criterion | Information Gain | MSE Reduction |

### Decision Tree vs Other Models

| Aspect | Decision Tree | Logistic Regression | SVM | Random Forest |
|--------|---------------|---------------------|-----|---------------|
| Interpretability | **High** | Medium | Low | Low |
| Non-linear | Yes | No (linear) | Yes (kernel) | Yes |
| Feature Scaling | Not needed | Needed | Critical | Not needed |
| Missing Values | Handles natively | Needs imputation | Needs imputation | Handles |
| Overfitting | High (unpruned) | Low | Medium | Low (ensemble) |

---

## GATE Tricks

> [!tip] **Decision Tree Quick Rules**
> - **Gini = $1 - \sum p_k^2$** (faster, no log)
> - **Entropy = $-\sum p_k \log p_k$** (information theory)
> - **Both give similar splits** in practice
> - **No feature scaling needed!** (split on order)
> - **Pruning essential** — unpruned trees overfit
> - **Max depth** = main hyperparameter for regularization
> - **Variable importance** = sum of weighted impurity decreases
> - **Handles mixed data types** natively

> [!warning] **GATE Traps**
> - **Greedy** ≠ globally optimal
> - **Axis-aligned splits** → diagonal boundaries need many splits
> - **Unstable** — small data change → different tree
> - **Biased toward features with many levels** (use conditional inference trees)
> - **Depth-first search** in construction → deeper trees preferred

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Gini | Entropy | $1-\sum p^2$ vs $-\sum p\log p$ |
| Pruning | Early Stopping | Post-hoc vs during construction |
| Classification Tree | Regression Tree | Gini/Entropy vs MSE |
| Decision Tree | Random Forest | Single tree vs ensemble of trees |
| CART | C4.5 | CART: binary splits; C4.5: multi-way |

---

## Common Mistakes

1. **No pruning** → severe overfitting
2. **Max depth too large** → memorizes training data
3. **Ignoring class imbalance** → use class weights or balanced subsampling
4. **Using on high-dimensional sparse data** → linear models often better
5. **Not setting random_state** → non-reproducible (due to tie-breaking)

---

## Memory Tricks

> [!tip] **Gini** = "Gini impurity = $1 - \sum p^2$" = probability two random items differ
> 
> **Entropy** = "Information content = $-\sum p \log p$"
> 
> **Information Gain** = "Parent impurity - weighted children impurity"
> 
> **Pruning** = "Cut the dead branches"
> 
> **No scaling** = "Trees don't care about scale, only order"

---

## Previous GATE Patterns

- **Numerical**: Compute Gini/Entropy for given node, compute IG for split
- **Tree construction**: Given data, determine first split
- **Pruning**: Cost-complexity pruning path
- **Variable importance**: Calculate from given tree
- **Comparison**: Gini vs Entropy, Tree vs Linear models
- **Overfitting**: Identify from tree depth / training vs test accuracy

---

## Revision Summary

```
DECISION TREES
├── Recursive partitioning: axis-aligned splits
├── Classification: Gini = 1-Σp², Entropy = -Σp log p
├── Regression: MSE = Σ(y-ȳ)²/N
├── Split: max Information Gain = Parent - weighted children
├── Greedy, top-down (not globally optimal)
├── NO feature scaling needed
├── Overfits without pruning
├── Pruning: Cost-Complexity R_α(T) = R(T) + α|leaves|
├── Variable Importance: Σ weighted IG over splits
├── Handles missing values, mixed types
├── Unstable (small change → different tree)
└── Ensemble (Random Forest, Boosting) fixes instability
```

---

## Related Notes

- [[12 Bias Variance Tradeoff]] (Pruning = bias-variance control)
- [[13 Cross Validation]] (Select α, max_depth via CV)
- [[17 Unsupervised Learning]] (Trees can do clustering)
- [[Formula Sheet]]

---

#machine-learning #gate-da #decision-trees #classification #regression #revision