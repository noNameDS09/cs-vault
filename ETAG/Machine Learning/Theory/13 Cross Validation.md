---
tags: [machine-learning, gate-da, cross-validation, model-selection, revision]
---

# <mark style="background:rgba(240, 200, 0, 0.2)">13 Cross Validation</mark>

> [!note] Technique for estimating model performance on unseen data and selecting hyperparameters

---

## Overview

Cross-validation (CV) partitions data into complementary subsets for training and validation. Provides less biased and lower variance estimate of test error than single train/test split.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **K-Fold CV** | Split data into K folds, train on K-1, validate on 1, repeat K times |
| **LOOCV** | Leave-One-Out: K = n (each sample is test set once) |
| **Stratified CV** | Preserves class proportions in each fold |
| **Nested CV** | Outer loop for performance estimation, inner for hyperparameter tuning |
| **Time Series CV** | Forward chaining (no random shuffling) |

---

## Formulae

<font color="#f79646">### K-Fold Cross Validation</font>
Split data into $K$ folds $D_1, ..., D_K$ of equal size.

For $k = 1$ to $K$:
- Train on $D \setminus D_k$
- Compute validation error $L_k = \frac{1}{|D_k|} \sum_{i \in D_k} L(y_i, \hat{f}^{(-k)}(x_i))$

**CV Estimate**:
$$
CV = \frac{1}{K} \sum_{k=1}^K L_k
$$

<font color="#f79646">### Leave-One-Out CV (LOOCV)</font>
Special case $K = n$:
$$
LOOCV = \frac{1}{n} \sum_{i=1}^n L(y_i, \hat{f}^{(-i)}(x_i))
$$
where $\hat{f}^{(-i)}$ = model trained on all data except $(x_i, y_i)$

### LOOCV Shortcut for Linear Models
For linear smoothers $\hat{y} = H y$ (ridge, OLS, smoothing splines):
$$
LOOCV = \frac{1}{n} \sum_{i=1}^n \left( \frac{y_i - \hat{y}_i}{1 - h_{ii}} \right)^2
$$
where $h_{ii}$ = diagonal of hat matrix $H$

*No need to retrain n times!*

<font color="#f79646">### Stratified K-Fold</font>
- Each fold has approximately same class distribution as full dataset
- Essential for imbalanced classification

### Standard Error of CV
$$
SE(CV) = \frac{\text{std}(L_1, ..., L_K)}{\sqrt{K}}
$$
*Useful for comparing models (error bars)*

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $K$ | Number of folds (typically 5 or 10) |
| $D_k$ | $k$-th fold (validation set) |
| $L_k$ | Validation error on fold $k$ |
| $h_{ii}$ | Leverage (hat matrix diagonal) |
| $\hat{f}^{(-k)}$ | Model trained without fold $k$ |

---

## Important Properties

### Bias-Variance of CV Estimator
| Method | Bias | Variance |
|--------|------|----------|
| Train/Test Split | High (depends on split) | Low |
| LOOCV | **Lowest** (uses n-1 samples) | **High** (highly correlated folds) |
| 10-Fold CV | Low | Medium |
| 5-Fold CV | Slightly higher | Lower |

### When to Use Which
- **Small $n$ ($n < 100$)**: LOOCV
- **Medium $n$ ($100 < n < 10^4$)**: 10-fold or 5-fold
- **Large $n$ ($n > 10^4$)**: Single split or 5-fold (computational)
- **Imbalanced classes**: Stratified K-fold
- **Time series**: Forward chaining (no shuffle)

### Nested Cross Validation
**Essential when tuning hyperparameters!**

```
Outer Loop (Performance Estimation):
  For each outer fold:
    Inner Loop (Hyperparameter Tuning):
      For each inner fold:
        Train with hyperparameters
      Select best hyperparameters
    Train on outer train with best hyperparams
    Evaluate on outer test
```

*Without nested CV: hyperparameter selection leaks into performance estimate (optimistic bias)*

---

## Mathematical Intuition

**LOOCV as Approximate Leave-One-Out Likelihood**:
- Each training set size = $n-1$ (maximizes training data)
- But folds highly correlated (overlap = $n-2$ samples)
- High correlation → high variance of CV estimate

**K-Fold Tradeoff**:
- Smaller $K$ → less correlation → lower variance, higher bias
- Larger $K$ → more training data → lower bias, higher variance
- $K=5$ or $10$ is sweet spot (empirically)

**Hat Matrix Shortcut**:
- For linear estimators, $\hat{y}^{(-i)}$ can be computed from full fit
- Sherman-Morrison formula gives exact LOOCV without retraining

---

## Algorithms

### Standard K-Fold CV
```python
from sklearn.model_selection import KFold

kf = KFold(n_splits=10, shuffle=True, random_state=42)
scores = []
for train_idx, val_idx in kf.split(X):
    model.fit(X[train_idx], y[train_idx])
    scores.append(model.score(X[val_idx], y[val_idx]))
cv_score = np.mean(scores)
```

### Stratified K-Fold
```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
```

### Grid Search with CV
```python
from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1]}
grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X, y)
best_params = grid.best_params_
```

### Nested CV
```python
from sklearn.model_selection import cross_val_score, GridSearchCV

inner_cv = KFold(n_splits=5)
outer_cv = KFold(n_splits=5)
grid = GridSearchCV(SVC(), param_grid, cv=inner_cv)
nested_score = cross_val_score(grid, X, y, cv=outer_cv).mean()
```

---

## Complexity

| Method | Training Runs | Time Complexity |
|--------|---------------|-----------------|
| Train/Test | 1 | $O(1 \times \text{train})$ |
| K-Fold | K | $O(K \times \text{train})$ |
| LOOCV | n | $O(n \times \text{train})$ |
| LOOCV (linear shortcut) | 1 | $O(\text{train} + n)$ |
| Nested CV | $K_{outer} \times K_{inner}$ | $O(K_{outer} \times K_{inner} \times \text{train})$ |

---

## Comparison Tables

### CV Methods Summary

| Method | Training Size | Bias | Variance | Compute |
|--------|---------------|------|----------|---------|
| Holdout | ~70% | High | Low | 1× |
| 5-Fold | 80% | Medium | Medium | 5× |
| 10-Fold | 90% | Low | Medium | 10× |
| LOOCV | n-1 | **Lowest** | **High** | n× (or 1× linear) |

### CV for Different Problems

| Problem Type | Recommended CV |
|--------------|----------------|
| Standard Classification | Stratified 10-fold |
| Standard Regression | 10-fold |
| Imbalanced Classification | Stratified 5/10-fold |
| Time Series | Forward Chaining |
| Small Dataset (<100) | LOOCV |
| Hyperparameter Tuning | Nested CV |

---

## GATE Tricks

> [!tip] **Cross Validation Quick Rules**
> - **Default: 10-fold CV** (good bias-variance tradeoff)
> - **Small n**: LOOCV (or 5-fold if computation matters)
> - **Classification**: Always **Stratified** (preserves class ratios)
> - **Hyperparameter tuning**: **Nested CV** (otherwise optimistic bias!)
> - **LOOCV shortcut**: $\frac{1}{n}\sum(\frac{y_i-\hat{y}_i}{1-h_{ii}})^2$ for linear models
> - **Time series**: No shuffle! Use forward chaining

> [!warning] **GATE Traps**
> - **Using test set for hyperparameter tuning** → data leakage!
> - **Non-stratified CV on imbalanced data** → some folds may miss minority class
> - **Shuffling time series** → destroys temporal structure, leaks future info
> - **Reporting CV mean without std** → can't compare models statistically
> - **Preprocessing before CV** (scaling, PCA, feature selection) → data leakage! Must do inside CV loop

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| K-Fold | LOOCV | K=n vs K=5/10 |
| CV | Train/Test Split | Multiple splits vs one |
| Inner CV | Outer CV | Hyperparameter tuning vs performance estimation |
| Stratified | Regular | Preserves class distribution |
| Forward Chaining | Random CV | Temporal order preserved |

---

## Common Mistakes

1. **Doing feature selection / PCA / scaling BEFORE CV** → Must be inside each fold!
2. **Using same CV for model selection and final evaluation** → Need nested CV
3. **Not setting random_state** → Non-reproducible splits
4. **Ignoring class imbalance** → Use StratifiedKFold
5. **Shuffling time series data** → Use TimeSeriesSplit
6. **Comparing models without error bars** → Use SE(CV) or statistical test

---

## Memory Tricks

> [!tip] **K-Fold** = "K folds, K trains, average"
> 
> **LOOCV** = "Leave One Out" = n folds
> 
> **Stratified** = "Strata" = layers = preserve class ratios
> 
> **Nested** = "Inside another" = inner for tuning, outer for eval
> 
> **Forward Chaining** = "Walk forward" = past predicts future

---

## Previous GATE Patterns

- **Numerical**: Compute LOOCV from hat matrix diagonal
- **Conceptual**: Identify data leakage in CV pipeline
- **Comparison**: 5-fold vs 10-fold vs LOOCV bias/variance
- **Time series**: Correct CV strategy
- **Nested CV**: When needed, why single CV insufficient
- **Preprocessing in CV**: What must be inside vs outside

---

## Revision Summary

```
CROSS VALIDATION
├── K-Fold: K splits, avg validation error
├── LOOCV: K=n, lowest bias, highest variance
├── Stratified: Preserves class distribution (classification!)
├── LOOCV shortcut (linear): 1/n Σ((yᵢ-ŷᵢ)/(1-hᵢᵢ))²
├── Hyperparameter tuning → Nested CV (outer eval, inner tune)
├── Time series → Forward chaining (no shuffle!)
├── Preprocessing (scaling, PCA, feature selection) MUST be INSIDE CV
├── Default: 10-fold stratified
├── SE(CV) = std(fold_scores)/√K for error bars
└── Data leakage = optimistic bias → avoid!
```

---

## Related Notes

- [[12 Bias Variance Tradeoff]] (CV estimates test error = bias²+variance)
- [[05 Ridge Regression]] (LOOCV shortcut via hat matrix)
- [[11 Decision Trees]] (Pruning parameter selection via CV)
- [[14 Neural Networks]] (Hyperparameter tuning via CV)
- [[Formula Sheet]]

---

#machine-learning #gate-da #cross-validation #model-selection #revision