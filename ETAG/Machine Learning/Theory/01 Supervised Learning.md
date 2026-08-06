---
tags: [machine-learning, gate-da, supervised-learning, revision]
---

# 01 Supervised Learning

> [!note] Learning from labeled data $(x_i, y_i)$ to predict $y$ for new $x$

---

## Overview

Supervised learning learns a mapping $f: \mathcal{X} \to \mathcal{Y}$ from training examples $\{(x_i, y_i)\}_{i=1}^n$. Two main types:

- **Regression**: $y \in \mathbb{R}$ (continuous)
- **Classification**: $y \in \{1, ..., K\}$ (discrete)

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Training Set** | Data used to fit model: $\{(x_i, y_i)\}_{i=1}^n$ |
| **Test Set** | Unseen data for final evaluation |
| **Validation Set** | Data for hyperparameter tuning |
| **Features** | Input variables $x \in \mathbb{R}^p$ |
| **Target/Label** | Output variable $y$ |
| **Hypothesis Space** | Set of candidate functions $\mathcal{H}$ |
| **Loss Function** | $L(y, \hat{y})$ measures prediction error |
| **Risk** | Expected loss: $R(f) = E[L(Y, f(X))]$ |
| **Empirical Risk** | Training loss: $\hat{R}(f) = \frac{1}{n}\sum L(y_i, f(x_i))$ |

---

## Formulae

### Empirical Risk Minimization (ERM)
$$
\hat{f} = \arg\min_{f \in \mathcal{H}} \frac{1}{n}\sum_{i=1}^n L(y_i, f(x_i))
$$

### Expected Prediction Error (Test MSE)
$$
E[(Y - \hat{f}(X))^2] = \underbrace{[E[\hat{f}(X)] - f(X)]^2}_{\text{Bias}^2} + \underbrace{E[(\hat{f}(X) - E[\hat{f}(X)])^2]}_{\text{Variance}} + \underbrace{\sigma^2}_{\text{Irreducible}}
$$

### Bias-Variance Decomposition
$$
\text{MSE} = \text{Bias}^2 + \text{Variance} + \sigma^2
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of training samples |
| $p$ | Number of features |
| $X$ | Design matrix $(n \times p)$ |
| $y$ | Target vector $(n \times 1)$ |
| $\hat{f}$ | Learned predictor |
| $f$ | True underlying function |
| $\sigma^2$ | Irreducible noise variance |
| $\mathcal{H}$ | Hypothesis space |

---

## Important Properties

### Assumptions (Typical)
1. **i.i.d. data**: $(x_i, y_i) \sim P(X,Y)$ independently
2. **Stationarity**: $P(X,Y)$ same for train and test
3. **Sufficient capacity**: $\mathcal{H}$ contains good approximation of $f$

### Advantages
- Clear objective (minimize loss)
- Theoretical guarantees (generalization bounds)
- Many algorithms available

### Disadvantages
- Requires labeled data (expensive)
- Overfitting risk with complex models
- Distribution shift breaks guarantees

---

## Mathematical Intuition

**Goal**: Find $f$ that minimizes expected loss on new data.

**Core tension**: 
- **Simple models** (low variance, high bias) → underfit
- **Complex models** (low bias, high variance) → overfit

**Regularization** controls this tradeoff by penalizing complexity.

---

## Algorithms

### Generic Supervised Learning Pipeline
```
1. Split data: Train / Val / Test
2. Choose model class (hypothesis space)
3. Choose loss function
4. Train: minimize empirical risk on train set
5. Tune hyperparameters on validation set
6. Final evaluation on test set
```

---

## Complexity

| Aspect | Typical |
|--------|---------|
| Training | $O(n \cdot p \cdot \text{iterations})$ to $O(n^3)$ |
| Prediction | $O(p)$ to $O(n)$ |
| Space | $O(n \cdot p)$ |

---

## Comparison Tables

### Regression vs Classification

| Aspect | Regression | Classification |
|--------|-----------|----------------|
| Target | Continuous | Discrete classes |
| Loss | MSE, MAE, Huber | Cross-entropy, Hinge |
| Output | $\hat{y} \in \mathbb{R}$ | $\hat{y} \in \{1..K\}$ or probabilities |
| Metrics | $R^2$, RMSE, MAE | Accuracy, F1, AUC |

### Common Loss Functions

| Loss          | Formula                                                                                                                            | Use Case                           |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| MSE           | $\frac{1}{n}\sum(y_i-\hat{y}_i)^2$                                                                                                 | Regression (sensitive to outliers) |
| MAE           | $\frac{1}{n}\sum y_i-\hat{y}_i$                                                                                                    | Regression (robust)                |
| Huber         | $\begin{cases} \frac{1}{2}(y-\hat{y})^2 &y-\hat{y}\leq \delta \\ \delta y-\hat{y} - \frac{1}{2}\delta^2 & \text{else} \end{cases}$ | Robust regression                  |
| Cross-Entropy | $-\sum y \log \hat{y}$                                                                                                             | Classification                     |
| Hinge         | $\max(0, 1-y\hat{y})$                                                                                                              | SVM                                |

---

## GATE Tricks

> [!tip] **Supervised Learning Quick Rules**
> - **Always split**: Train/Val/Test (or use CV)
> - **Feature scaling**: Required for distance-based (KNN, SVM) and gradient-based (NN, LR)
> - **Regularization**: Add $\lambda \|\theta\|^2$ to prevent overfitting
> - **Class imbalance**: Use F1, AUC, or weighted loss instead of accuracy
> - **i.i.d. assumption**: If violated, standard guarantees don't hold

> [!warning] **Common GATE Traps**
> - Confusing empirical risk (training error) with true risk (test error)
> - Assuming low training error = good model (overfitting!)
> - Using test set for hyperparameter tuning (data leakage)

---

## Frequently Confused Concepts

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Training Error | Test Error | Training = on seen data, Test = on unseen |
| Bias | Variance | Bias = systematic error, Variance = sensitivity to data |
| Parameters | Hyperparameters | Parameters learned from data, Hyperparameters set before training |
| Regression | Classification | Continuous vs discrete target |

---

## Common Mistakes

1. **No validation set** → hyperparameter tuning on test set (overfitting to test)
2. **No feature scaling** → gradient descent fails, distance metrics biased
3. **Ignoring class imbalance** → accuracy misleading (e.g., 99% class 0 → 99% accuracy by predicting all 0)
4. **Data leakage** → using target info in features, or test data in preprocessing

---

## Memory Tricks

> [!tip] **ERM = Empirical Risk Minimization** = "Error Rate Minimization" on training data
> 
> **Bias** = "Biased towards simple" (underfit)
> 
> **Variance** = "Varies with data" (overfit)

---

## Previous GATE Patterns

- **Numerical**: Compute bias/variance given predictor distribution
- **Conceptual**: Identify overfitting/underfitting from learning curves
- **MCQ**: Choose correct loss function for given problem
- **Theory**: Generalization bound interpretation (VC dimension, Rademacher complexity)

---

## Revision Summary

```
SUPERVISED LEARNING ESSENTIALS
├── Two types: Regression (continuous) / Classification (discrete)
├── Goal: Minimize Expected Risk E[L(Y, f(X))]
├── Practical: Minimize Empirical Risk (training loss) + Regularization
├── Bias-Variance Tradeoff: MSE = Bias² + Variance + σ²
├── Train/Val/Test split OR Cross-Validation
├── Feature scaling for distance/gradient methods
├── Class imbalance → use F1/AUC, not accuracy
└── No data leakage!
```

---

## Related Notes

- [[02 Regression]]
- [[12 Bias Variance Tradeoff]]
- [[13 Cross Validation]]
- [[06 Logistic Regression]]
- [[17 Unsupervised Learning]]

---

#machine-learning #gate-da #supervised-learning #revision