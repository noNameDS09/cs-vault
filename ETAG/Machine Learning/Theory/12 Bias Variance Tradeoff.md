---
tags: [machine-learning, gate-da, bias-variance, tradeoff, revision]
---

# 12 Bias-Variance Tradeoff

> [!note] Fundamental decomposition of prediction error: **MSE = Bias² + Variance + Irreducible Error**

---

## Overview

The bias-variance tradeoff explains why models that are too simple (high bias) or too complex (high variance) both perform poorly. Understanding this is crucial for model selection and regularization.

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Bias** | Systematic error: $E[\hat{f}(x)] - f(x)$ |
| **Variance** | Sensitivity to training data: $E[(\hat{f}(x) - E[\hat{f}(x)])^2]$ |
| **Irreducible Error** | Noise: $\sigma^2 = Var(\epsilon)$ |
| **Underfitting** | High bias, low variance |
| **Overfitting** | Low bias, high variance |

---

## Formulae

### Bias-Variance Decomposition (Squared Error Loss)
$$
E[(Y - \hat{f}(x))^2] = \underbrace{[E[\hat{f}(x)] - f(x)]^2}_{\text{Bias}^2} + \underbrace{E[(\hat{f}(x) - E[\hat{f}(x)])^2]}_{\text{Variance}} + \underbrace{\sigma^2}_{\text{Irreducible}}
$$

### For a Single Prediction Point $x$
$$
\text{MSE}(x) = \text{Bias}^2(x) + \text{Var}(x) + \sigma^2
$$

### Bias Definition
$$
\text{Bias}(\hat{f}(x)) = E[\hat{f}(x)] - f(x)
$$
- $E[\hat{f}(x)]$ = average prediction over all training sets
- $f(x)$ = true function

### Variance Definition
$$
\text{Var}(\hat{f}(x)) = E[(\hat{f}(x) - E[\hat{f}(x)])^2]
$$
- How much $\hat{f}(x)$ varies across different training sets

### Expected Test MSE (Averaged over $x$)
$$
E_{X,Y}[\text{MSE}] = E_X[\text{Bias}^2(X)] + E_X[\text{Var}(X)] + \sigma^2
$$

---

### Concrete Example: Polynomial Regression

For polynomial degree $d$:
- **Low $d$ (e.g., linear)**: High bias (can't capture curvature), Low variance
- **High $d$ (e.g., degree 10)**: Low bias (fits training perfectly), High variance (wiggly)

### Ridge Regression Bias-Variance
$$
\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} X^T y
$$
$$
\text{Bias} = -\lambda (X^T X + \lambda I)^{-1} \beta \quad (\text{increases with } \lambda)
$$
$$
\text{Variance} = \sigma^2 (X^T X + \lambda I)^{-1} X^T X (X^T X + \lambda I)^{-1} \quad (\text{decreases with } \lambda)
$$

---

## Meaning of Variables

| Symbol | Meaning |
|--------|---------|
| $f(x)$ | True underlying function |
| $\hat{f}(x)$ | Learned predictor (random, depends on training data) |
| $\sigma^2$ | Irreducible noise variance |
| $\lambda$ | Regularization parameter |

---

## Important Properties

### Bias-Variance Tradeoff
- **Cannot reduce both simultaneously** (for fixed model class)
- **Complexity increases**: Bias ↓, Variance ↑
- **Optimal complexity**: Minimizes total error

### Model Complexity vs Error

<image src="https://imgs.search.brave.com/cD1uJ8E4wbXuffbS5Ep6Urd0YPiWceupS-RPEzpOrLk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dHV0b3JpYWxzcG9p/bnQuY29tL21hY2hp/bmVfbGVhcm5pbmcv/aW1hZ2VzL2JpYXNf/dmFyaWFuY2VfdHJh/ZGVvZmYuanBn"></image>

### Sources of Bias
- Model class too simple (e.g., linear for non-linear truth)
- Regularization too strong ($\lambda$ too large)
- Insufficient features

### Sources of Variance
- Model class too complex (e.g., high-degree polynomial)
- Too many features relative to $n$
- Regularization too weak
- Unstable algorithms (e.g., deep decision trees)

---

## Mathematical Intuition

**Stein's Lemma / SURE**: For linear estimators $\hat{y} = H y$:
$$
E[||y - \hat{y}||^2] = ||y - H y||^2 + 2\sigma^2 \text{tr}(H) - n\sigma^2
$$
- $||y - H y||^2$ = training error (related to bias)
- $\text{tr}(H)$ = effective degrees of freedom (related to variance)

**Bagging Reduces Variance**: Average $B$ models trained on bootstrap samples:
$$
\text{Var}(\bar{f}) = \frac{1}{B} \text{Var}(f) + \frac{B-1}{B} \text{Cov}(f_1, f_2)
$$
If models uncorrelated, variance reduces by $1/B$.

**Boosting Reduces Bias**: Sequentially fit residuals, builds additive model.

---

## Algorithms / Techniques

### Controlling Bias-Variance

| Technique           | Effect on Bias       | Effect on Variance |
| ------------------- | -------------------- | ------------------ |
| More complex model  | ↓                    | ↑                  |
| Regularization (↑λ) | ↑                    | ↓                  |
| More data           | ~same                | ↓                  |
| Feature selection   | ↑ (if remove useful) | ↓                  |
| Bagging (RF)        | ~same                | ↓↓                 |
| Boosting            | ↓↓                   | ↑ (if overfit)     |
| Ensemble            | ~same                | ↓                  |

### Learning Curves
- **High Bias**: Training error ≈ Test error (both high), adding data doesn't help
- **High Variance**: Training error << Test error, adding data helps

---

## Comparison Tables

### High Bias vs High Variance Symptoms

| Symptom | High Bias (Underfit) | High Variance (Overfit) |
|---------|---------------------|------------------------|
| Training Error | High | Low |
| Test Error | High | High |
| Gap (Test - Train) | Small | Large |
| Adding Data Helps? | No | Yes |
| Model Complexity | Too Low | Too High |
| Regularization | Too Strong | Too Weak |

### Linear Models: Bias-Variance with Regularization

| $\lambda$ | Bias | Variance | Model |
|-----------|------|----------|-------|
| 0 (OLS) | Low | High | Unregularized |
| Optimal | Balanced | Balanced | **Best test error** |
| → ∞ | High | Low | Constant (mean) |

---

## GATE Tricks

> [!tip] **Bias-Variance Quick Rules**
> - **Test Error = Bias² + Variance + σ²** (always!)
> - **More data reduces variance**, not bias
> - **Regularization increases bias, decreases variance**
> - **Bagging (Random Forest) reduces variance**
> - **Boosting reduces bias**
> - **Learning curves**: Gap = variance; Level = bias + variance
> - **Irreducible error σ²** = noise floor (can't beat)

> [!warning] **GATE Traps**
> - **Bias-Variance decomposition only holds for MSE** (squared error loss)
> - **Training error is NOT bias** (training error = bias² + variance - variance of noise)
> - **Cross-validation estimates test error**, not bias/variance separately
> - **Bias can be negative?** No, Bias² ≥ 0 always

---

## Frequently Confused Concepts

| Concept A | Concept B | Difference |
|-----------|-----------|------------|
| Bias | Variance | Systematic vs random error |
| Training Error | Bias | Training error includes variance |
| Underfitting | Overfitting | High bias vs high variance |
| Regularization | Early Stopping | Both control complexity |
| Bagging | Boosting | Variance reduction vs bias reduction |

---

## Common Mistakes

1. **Confusing training error with bias** → training error = bias² + variance - σ²/n (optimism)
2. **Thinking more data fixes bias** → only fixes variance
3. **Over-regularizing** → high bias, underfitting
4. **Not plotting learning curves** → can't diagnose bias vs variance
5. **Assuming low training error = good model** → could be overfitting!

---

## Memory Tricks

> [!tip] **Bias** = "Biased toward simple" = underfit (can't capture complexity)
> 
> **Variance** = "Varies with data" = overfit (memorizes noise)
> 
> **Tradeoff** = "Can't have both low" = U-shaped test error
> 
> **More data** = "Variance's best friend" = reduces variance
> 
> **Regularization** = "Bias's friend, Variance's enemy"

---

## Previous GATE Patterns

- **Numerical**: Given bias=2, variance=3, σ²=1 → MSE = 4+3+1=8
- **Learning curves**: Identify high bias vs high variance from curves
- **Model selection**: Choose complexity minimizing CV error
- **Regularization path**: Effect of λ on bias/variance
- **Bagging vs Boosting**: Which reduces bias vs variance
- **Polynomial degree**: Effect on bias/variance

---

## Revision Summary

```
BIAS-VARIANCE TRADEOFF
├── MSE = Bias² + Variance + σ² (irreducible)
├── Bias = E[f̂(x)] - f(x) = systematic error
├── Variance = E[(f̂(x) - E[f̂(x)])²] = sensitivity to data
├── Underfitting: High bias, low variance (too simple)
├── Overfitting: Low bias, high variance (too complex)
├── More data → reduces variance only
├── Regularization (λ↑) → bias↑, variance↓
├── Bagging (RF) → reduces variance
├── Boosting → reduces bias
├── Learning curves: Gap = variance, Level = bias + variance
└── Optimal complexity: minimum of U-shaped test error
```

---

## Related Notes

- [[11 Decision Trees]] (Pruning = bias-variance control)
- [[05 Ridge Regression]] (λ controls tradeoff)
- [[13 Cross Validation]] (CV estimates test error)
- [[17 Unsupervised Learning]] (Bias-variance in clustering?)
- [[Formula Sheet]]

---

#machine-learning #gate-da #bias-variance #tradeoff #revision