# SPPU AIDS BE SEM VII - Machine Learning In-Sem Exam Answers (SEP 2023)

> **Course**: Machine Learning | **Semester**: VII | **Branch**: AIDS
> **Exam**: In-Semester Examination | **Date**: September 2023
> **Total Marks**: 50

> **Note**: Most questions overlap with [AUG25 Paper](./AUG25.md) and [SEP24 Paper](./SEP24.md). This file contains **only new/unanswered questions** with cross-references to previous papers.

---

## Question 1

### Q1(a) Compare Machine Learning with Traditional programming. [5]

> **Already answered in [AUG25.md Q1(a)](./AUG25.md#q1a-describe-machine-learning-and-highlight-its-key-differences-from-traditional-programming-methods-5-marks)** and [SEP24.md Q1(a)](./SEP24.md#q1a-describe-machine-learning-and-differentiate-it-from-traditional-programming-6-marks).

---

### Q1(b) What is Dimensionality Reduction, Explain any one Dimensionality Reduction technique. [6]

> **PCA** covered in [SEP24.md Q1(b)](./SEP24.md#q1b-explain-principal-component-analysis-used-in-machine-learning-5-marks)  
> **LDA** covered in [AUG25.md Q1(b)](./AUG25.md#q1b-explain-the-main-difference-between-linear-discriminant-analysis-lda-and-principal-component-analysis-pca-in-reducing-dimensions-6-marks) and [SEP24.md Q2(b)](./SEP24.md#q2b-explain-linear-discriminant-analysis-lda-used-in-machine-learning-5-marks)

Below: **General Dimensionality Reduction** + **t-SNE** (non-linear technique not previously covered).

---

#### Dimensionality Reduction

**Definition**: The process of reducing the number of features (dimensions) in a dataset while preserving **important information** (variance, structure, class separability, local neighborhoods).

---

##### Why Reduce Dimensions?

| Reason | Description |
|--------|-------------|
| **Curse of Dimensionality** | Data becomes sparse; distance metrics lose meaning; overfitting risk ↑ |
| **Computational Efficiency** | Faster training/inference; less memory |
| **Visualization** | Project to 2D/3D for human inspection |
| **Noise Reduction** | Discard low-variance/noisy dimensions |
| **Multicollinearity** | Remove correlated features |
| **Feature Extraction** | Create better representations for downstream tasks |

---

##### Taxonomy

```
DIMENSIONALITY REDUCTION
        │
        ├── FEATURE SELECTION (Subset of original features)
        │       ├── Filter Methods (Correlation, MI, Chi², Variance Threshold)
        │       ├── Wrapper Methods (RFE, Forward/Backward Selection)
        │       └── Embedded Methods (Lasso, Tree Importance, Regularization)
        │
        └── FEATURE EXTRACTION (New features = f(original features))
                ├── LINEAR
                │       ├── PCA (Unsupervised, Max Variance)
                │       ├── LDA (Supervised, Max Class Separation)
                │       ├── Factor Analysis (Latent variables)
                │       └── ICA (Independent Components)
                │
                └── NON-LINEAR (Manifold Learning)
                        ├── t-SNE (Local structure, Visualization)
                        ├── UMAP (Local + Global, Scalable)
                        ├── Isomap (Geodesic distances)
                        ├── LLE (Local Linear Embedding)
                        ├── Kernel PCA (Non-linear via kernel trick)
                        └── Autoencoders (Deep Learning)
```

---

#### t-SNE (t-Distributed Stochastic Neighbor Embedding)

**t-SNE** is a **non-linear** dimensionality reduction technique primarily for **visualization** (2D/3D), preserving **local neighborhood structure**.

---

##### Core Idea

> Model **pairwise similarities** in high-dim space with Gaussian distribution, and in low-dim space with **Student's t-distribution** (heavy tails). Minimize KL divergence between the two distributions.

---

##### Algorithm

**Input**: $X \in \mathbb{R}^{n \times d}$, target dimension $d' = 2$ or $3$, perplexity $\text{Perp}$

**Step 1: High-Dimensional Similarities $P_{ij}$**
$$P_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$$
$$P_{ij} = \frac{P_{j|i} + P_{i|j}}{2n}$$
- $\sigma_i$ chosen so that **perplexity** = $2^{H(P_i)}$ matches user-specified value (typically 5-50)
- Perplexity ≈ effective number of neighbors

**Step 2: Low-Dimensional Similarities $Q_{ij}$**
$$Q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}}$$
- Uses **Student's t-distribution with 1 degree of freedom** (Cauchy)
- Heavy tails → allows dissimilar points to be far apart (avoids crowding problem)

**Step 3: Minimize KL Divergence**
$$C = \text{KL}(P \| Q) = \sum_{i \neq j} P_{ij} \log \frac{P_{ij}}{Q_{ij}}$$

**Step 4: Gradient Descent**
$$\frac{\partial C}{\partial y_i} = 4 \sum_j (P_{ij} - Q_{ij}) (y_i - y_j) (1 + \|y_i - y_j\|^2)^{-1}$$
- Optimize $Y = \{y_1, \dots, y_n\}$ using gradient descent with momentum
- **Early exaggeration** (×4 for first 250 iter): encourages clustering

---

##### Key Properties

| Property | Detail |
|----------|--------|
| **Non-linear** | Captures complex manifolds |
| **Local structure** | Preserves neighborhoods (small distances) |
| **Global structure** | **Not** reliably preserved (clusters may be arbitrarily placed) |
| **Stochastic** | Different runs → different layouts (set `random_state`) |
| **No parametric mapping** | Cannot transform new points directly (use parametric t-SNE or approximation) |
| **Computational** | $O(n^2)$ naive; Barnes-Hut $O(n \log n)$ for $n > 10^4$ |

---

##### Perplexity Effect

| Perplexity | Behavior |
|------------|----------|
| **Low (5-10)** | Very local; fragmented clusters |
| **Medium (30-50)** | Balanced (default 30) |
| **High (100+)** | More global; may merge distinct clusters |

---

##### When to Use t-SNE

- **Visualization** of high-dim data (MNIST, gene expression, word embeddings)
- **Exploratory analysis** to discover clusters
- **Not for**: Feature extraction for downstream ML (no transform for new data), preserving global distances

---

##### t-SNE vs PCA vs UMAP

| Aspect | PCA | t-SNE | UMAP |
|--------|-----|-------|------|
| **Linearity** | Linear | Non-linear | Non-linear |
| **Goal** | Max variance | Local structure | Local + Global |
| **Speed** | Fast ($O(nd^2)$) | Slow ($O(n^2)$ or $O(n\log n)$) | Fast ($O(n \log n)$) |
| **New Data** | Transform via $W$ | Requires retraining/approx | Transform via `transform()` |
| **Scalability** | Excellent | Limited (~50k) | Excellent (millions) |
| **Global Structure** | Preserved | Lost | Better preserved |
| **Primary Use** | Preprocessing, Compression | Visualization | Viz + Preprocessing |

---

### Q1(c) Write a note on Reinforcement Learning. [4]

> **Already answered in [AUG25.md Q1(c)](./AUG25.md#q1c-write-a-note-on-reinforcement-learning-4-marks)**.

---

## Question 2

### Q2(a) Explain parametric & nonparametric models in machine learning. [5]

**NEW QUESTION** - Not covered in previous papers.

---

#### Parametric vs Nonparametric Models

---

##### Parametric Models

**Definition**: Models that summarize data using a **fixed, finite number of parameters** $\theta \in \mathbb{R}^p$, independent of training set size $n$.

**Form**: $\hat{f}(x) = f(x; \theta)$ where $\theta$ has fixed dimension $p$.

**Learning**: Estimate $\theta$ from data (MLE, MAP, gradient descent).

---

##### Examples

| Model | Parameters $\theta$ | Count $p$ |
|-------|---------------------|-----------|
| **Linear Regression** | $\beta_0, \beta_1, \dots, \beta_p$ | $p+1$ |
| **Logistic Regression** | $\beta_0, \beta_1, \dots, \beta_p$ | $p+1$ |
| **Linear SVM** | $w \in \mathbb{R}^d, b$ | $d+1$ |
| **Neural Network (fixed architecture)** | Weights + biases | Fixed by architecture |
| **Gaussian Naive Bayes** | $\mu_c, \sigma_c^2, \pi_c$ | $O(C \cdot d)$ |
| **LDA/QDA** | $\mu_c, \Sigma$ | $O(C \cdot d^2)$ |

---

##### Characteristics

| Property | Parametric |
|----------|------------|
| **Model Complexity** | Fixed (determined before seeing data) |
| **Parameters** | Finite, fixed $p$ |
| **Training** | Parameter estimation (often convex) |
| **Inference Speed** | Very fast ($O(p)$) |
| **Storage** | $O(p)$ (just parameters) |
| **Flexibility** | Limited by functional form |
| **Assumptions** | Strong (linearity, Gaussian, etc.) |
| **Risk** | **Underfitting** if model too simple |
| **Sample Efficiency** | High (works with small $n$) |

---

##### Nonparametric Models

**Definition**: Models where the **number of parameters grows with training data size $n$** (or no explicit parametric form). "Nonparametric" ≠ "no parameters" — rather, **parameters are not fixed a priori**.

**Form**: $\hat{f}(x) = g(x; \mathcal{D}_{\text{train}})$ — model is essentially the training data + algorithm.

---

##### Examples

| Model | "Parameters" | Growth |
|-------|--------------|--------|
| **K-Nearest Neighbors (KNN)** | All training points $(x_i, y_i)$ | $O(n)$ |
| **Decision Trees** | Split points, leaf values | $O(\text{nodes}) \propto n$ |
| **Random Forest / Gradient Boosting** | Ensemble of trees | $O(n \cdot \text{trees})$ |
| **Kernel SVM** | Support vectors ($\alpha_i$) | $O(n_{SV}) \leq n$ |
| **Gaussian Process** | Kernel matrix $K$ | $O(n^2)$ |
| **Kernel Density Estimation** | All data points | $O(n)$ |
| **Splines / GAMs** | Knots/coefficients | Grows with flexibility |

---

##### Characteristics

| Property | Nonparametric |
|----------|---------------|
| **Model Complexity** | Adapts to data (grows with $n$) |
| **Parameters** | Effectively infinite / data-dependent |
| **Training** | Often "lazy" (KNN) or greedy (trees) |
| **Inference Speed** | Slower ($O(n)$ or $O(\log n)$ with trees) |
| **Storage** | $O(n)$ (need training data) |
| **Flexibility** | High (can approximate any function) |
| **Assumptions** | Weak (smoothness, continuity) |
| **Risk** | **Overfitting** if not regularized |
| **Sample Efficiency** | Low (needs large $n$) |

---

##### Comparison Summary

| Criterion | Parametric | Nonparametric |
|-----------|------------|---------------|
| **Parameter Count** | Fixed $p$ | Grows with $n$ |
| **Functional Form** | Pre-specified | Learned from data |
| **Examples** | Linear/Logistic Reg, NN (fixed arch), Naive Bayes | KNN, Trees, Kernel SVM, GP |
| **Interpretability** | High (coefficients) | Medium (trees) to Low (ensembles) |
| **Training Time** | Usually faster | Can be slower (esp. kernel methods) |
| **Prediction Time** | $O(p)$ — very fast | $O(n)$ or $O(\log n)$ |
| **Data Requirements** | Works with small $n$ | Needs large $n$ |
| **Extrapolation** | Possible (via parametric form) | Poor (local interpolation) |
| **Regularization** | Explicit ($\lambda \|\theta\|$) | Implicit (pruning, $k$, bandwidth) |

---

##### The "No Free Lunch" Perspective

- **Parametric**: Strong inductive bias → good when bias matches truth; fails if wrong
- **Nonparametric**: Weak inductive bias → flexible but needs more data to constrain

> **Rule of Thumb**: Start parametric (linear/logistic). Move to nonparametric (trees, kernels, NN) when parametric underfits and you have sufficient data.

---

##### Semi-Parametric Models

Hybrid: Fixed parametric component + nonparametric component.

| Model | Parametric Part | Nonparametric Part |
|-------|-----------------|-------------------|
| **Generalized Additive Models (GAM)** | Linear terms | Smooth splines $f_j(x_j)$ |
| **Partially Linear Models** | $X\beta$ | $g(Z)$ |
| **Neural Networks (wide)** | Last layer (linear) | Hidden layers (nonparametric) |
| **Cox Proportional Hazards** | $\beta^T x$ | Baseline hazard $h_0(t)$ |

---

### Q2(b) Differentiate supervised and unsupervised learning techniques. [5]

> **Already answered in [AUG25.md Q2(b)](./AUG25.md#q2b-what-distinguishes-unsupervised-learning-from-supervised-and-semi-supervised-learning-techniques-6-marks)** and [SEP24.md Q2(a)](./SEP24.md#q2a-explain-types-of-machine-learning-6-marks).

---

### Q2(c) Elaborate grouping and grading models. [5]

> **Already answered in [AUG25.md Q2(c)](./AUG25.md#q2c-explain-grouping-and-grading-models-in-machine-learning-with-an-example-4-marks)** and [SEP24.md Q2(c)](./SEP24.md#q2c-differentiate-grouping-and-grading-models-of-machine-learning-4-marks). The 5-mark version requires slightly more detail — see additions below.

---

#### Additional Points for 5-Mark Answer

| Aspect | Additional Detail |
|--------|-------------------|
| **Grouping Algorithms** | Add: Spectral Clustering, Mean Shift, Affinity Propagation, BIRCH |
| **Grading Algorithms** | Add: Ordinal Regression, Learning to Rank (LambdaMART), Calibration methods |
| **Evaluation** | Grouping: Silhouette, Davies-Bouldin, Calinski-Harabasz, ARI (if labels)<br>Grading: AUC, KS Statistic, Gini, Brier Score, Calibration plots |
| **Pipeline** | Show combined workflow: Grouping → Feature Engineering → Grading |

---

## Question 3

### Q3(a) Elaborate random forest regression. [5]

> **Already answered in [AUG25.md Q3(a)](./AUG25.md#q3a-elaborate-decision-tree-regression-and-random-forest-regression-6-marks)** and [SEP24.md Q3(b)](./SEP24.md#q3b-explain-the-random-forest-regression-5-marks).

---

### Q3(b) Differentiate multivariate regression and univariate regression. [4]

> **Already answered in [AUG25.md Q3(b)](./AUG25.md#q3b-differentiate-between-multivariate-regression-and-univariate-regression-4-marks)**.

---

### Q3(c) Define Regression. Explain types of regression. [6]

> **Already answered in [AUG25.md Q4(c)](./AUG25.md#q4c-list-and-explain-any-two-different-types-of-regression-5-marks)** and [SEP24.md Q4(a)](./SEP24.md#q4a-what-is-regression-explain-types-of-regressions-6-marks).

---

## Question 4

### Q4(a) What is underfitting and overfitting in machine Learning explain the techniques to reduce overfitting? [5]

> **Underfitting/Overfitting definitions** covered in [AUG25.md Q4(a)](./AUG25.md#q4a-which-one-of-these-is-underfit-or-overfit-why-comment-with-respect-to-bias-and-variance-6-marks).

Below: **Detailed techniques to reduce overfitting** (new content for this paper).

---

#### Underfitting & Overfitting Recap

| Condition | Training Error | Test Error | Bias | Variance |
|-----------|----------------|------------|------|----------|
| **Underfitting** | High | High | High | Low |
| **Overfitting** | Low | High | Low | High |
| **Good Fit** | Low | Low | Balanced | Balanced |

---

#### Techniques to Reduce Overfitting

---

##### 1. **More Training Data**

- **Most effective** — variance $\propto 1/n$
- Data augmentation (images: rotation, crop, flip; text: back-translation; audio: noise, stretch)
- Synthetic data (SMOTE, GANs, diffusion models)
- Transfer learning / Pre-training on large corpora

---

##### 2. **Regularization**

| Method | Formula | Effect |
|--------|---------|--------|
| **L2 (Ridge)** | $\lambda \|\beta\|_2^2$ | Shrinks weights, keeps all features |
| **L1 (Lasso)** | $\lambda \|\beta\|_1$ | Sparsity + feature selection |
| **Elastic Net** | $\lambda_1 \|\beta\|_1 + \lambda_2 \|\beta\|_2^2$ | Groups correlated features |
| **Dropout (NN)** | Randomly zero units during training | Ensemble effect, prevents co-adaptation |
| **Weight Decay** | Equivalent to L2 for SGD | Standard in deep learning |
| **Label Smoothing** | $y \leftarrow (1-\epsilon)y + \epsilon/K$ | Prevents overconfident predictions |

---

##### 3. **Model Simplification / Architecture Choices**

- **Reduce capacity**: Fewer layers, fewer units, smaller kernel size
- **Pruning**: Remove redundant weights/neurons (magnitude-based, structured)
- **Early Stopping**: Monitor validation loss; stop when it increases
- **Parameter Sharing**: CNNs, RNNs, Transformers (vs fully connected)

---

##### 4. **Cross-Validation & Robust Evaluation**

- **k-Fold CV**: Better generalization estimate than single split
- **Stratified CV**: Preserve class distribution
- **Nested CV**: Unbiased hyperparameter selection
- **Time Series CV**: Walk-forward for temporal data

---

##### 5. **Feature Engineering / Selection**

- **Remove irrelevant features**: Mutual information, variance threshold
- **Dimensionality Reduction**: PCA, LDA, Autoencoders before modeling
- **Domain Knowledge**: Remove leaky/derived features

---

##### 6. **Ensemble Methods**

| Method | Mechanism |
|--------|-----------|
| **Bagging** (Random Forest) | Average decorrelated models → reduces variance |
| **Boosting** (XGBoost, LightGBM) | Sequential correction → reduces bias (can overfit if too many rounds) |
| **Stacking** | Meta-learner on base model predictions |
| **Snapshot Ensembles** | Multiple checkpoints from single training run |

---

##### 7. **Noise Injection**

- **Input Noise**: Gaussian noise to inputs during training
- **Weight Noise**: Bayesian neural networks, DropConnect
- **Gradient Noise**: Add noise to gradients (helps escape sharp minima)

---

##### 8. **Optimization / Training Tricks**

- **Batch Normalization**: Regularizes via batch statistics noise
- **Gradient Clipping**: Prevents exploding gradients
- **Learning Rate Scheduling**: Cosine annealing, warm restarts
- **Stochastic Weight Averaging (SWA)**: Average weights along trajectory → flatter minima

---

##### 9. **Bayesian Approaches**

- **Bayesian Neural Networks**: Distribution over weights → natural regularization
- **MC Dropout**: Approximate Bayesian inference at test time
- **Evidential Deep Learning**: Predict uncertainty directly

---

##### Summary: Overfitting Reduction Checklist

```
□ More data / Data augmentation
□ Regularization (L1/L2/Dropout/Weight Decay)
□ Simpler model / Reduce capacity
□ Early stopping (patience=10-20)
□ Cross-validation (k=5 or 10)
□ Feature selection / Dimensionality reduction
□ Ensemble (Bagging preferred for variance reduction)
□ Noise injection (input, weight, gradient)
□ Batch Normalization
□ Bayesian methods / Uncertainty quantification
□ Monitor: Train vs Val loss gap, Learning curves
```

---

### Q4(b) Explain any two Evaluation Metrics for regression. [5]

> **Already answered in [AUG25.md Q4(b)](./AUG25.md#q4b-explain-any-two-evaluation-metrics-in-regression-model-4-marks)** (MSE, MAE) and [SEP24.md Q3(a)](./SEP24.md#q3a-explain-three-evaluation-metrics-used-for-regression-model-6-marks) (MSE, MAE, R²).

---

### Q4(c) Explain Elastic Net regression in Machine Learning. [5]

> **Mentioned briefly in [SEP24.md Q4(a)](./SEP24.md#q4a-what-is-regression-explain-types-of-regressions-6-marks)** additions. Below is **dedicated detailed explanation** for 5 marks.

---

#### Elastic Net Regression

**Elastic Net** combines **L1 (Lasso)** and **L2 (Ridge)** penalties to get benefits of both: **feature selection** + **grouping of correlated features**.

---

##### Objective Function

$$\hat{\beta}_{\text{enet}} = \arg\min_\beta \left\{ \frac{1}{2n} \|y - X\beta\|_2^2 + \lambda \left[ \alpha \|\beta\|_1 + \frac{1-\alpha}{2} \|\beta\|_2^2 \right] \right\}$$

where:
- $\lambda \geq 0$: Overall regularization strength
- $\alpha \in [0, 1]$: Mixing parameter
  - $\alpha = 1$ → **Lasso**
  - $\alpha = 0$ → **Ridge**
  - $0 < \alpha < 1$ → **Elastic Net**

---

##### Why Elastic Net? (The Lasso Problem)

**Lasso limitation**: With highly correlated features, Lasso **arbitrarily picks one** and zeros the others.

> Example: Gene expression data — genes in same pathway are highly correlated. Lasso selects one gene per pathway randomly.

**Ridge limitation**: Keeps all correlated features (no sparsity).

**Elastic Net solution**: 
- L2 part → **groups correlated features** (similar coefficients)
- L1 part → **sparsity** (zeros out irrelevant groups)

---

##### Geometry

```
Elastic Net Constraint Region (α=0.5):
    
    │ β₂
    │     ╭─────╮
    │   ╱         ╲
    │  │           │   ← Rounded corners (L2)
    │  │           │        but with
    │   ╲         ╱        flat facets (L1)
    │     ╰─────╯
    └───────────── β₁
    
    Corners → sparsity (like Lasso)
    Curved sides → grouping (like Ridge)
```

---

##### Grouping Effect Theorem

For standardized features with correlation $\rho_{jk}$:

$$|\hat{\beta}_j - \hat{\beta}_k| \leq \frac{\|y\|_2}{\lambda(1-\alpha)} \sqrt{2(1-\rho_{jk})}$$

- As $\rho_{jk} \to 1$, $|\hat{\beta}_j - \hat{\beta}_k| \to 0$ → **coefficients become equal**
- Strength controlled by $\lambda(1-\alpha)$ (L2 portion)

---

##### Algorithm: Coordinate Descent

Elastic Net solved via **cyclic coordinate descent** (efficient for sparse solutions):

```
For each λ in λ_path (descending):
    Initialize β = 0 (or warm start from previous λ)
    Repeat until convergence:
        For j = 1 to p:
            # Partial residual excluding feature j
            r_j = y - X_{-j} β_{-j}
            
            # Univariate soft-thresholding with L2 shrinkage
            z_j = X_j^T r_j / n
            β_j = S(z_j, λα) / (1 + λ(1-α))
            
            where S(z, γ) = sign(z) · max(|z| - γ, 0)  # Soft threshold
```

> **Warm starts**: Use solution at $\lambda_k$ as initialization for $\lambda_{k+1}$ → very fast path computation.

---

##### Hyperparameter Selection

| Parameter | Range | Selection Method |
|-----------|-------|------------------|
| $\lambda$ | $\lambda_{\max} \to \lambda_{\min}$ | Cross-validation (CV) on log-spaced grid |
| $\alpha$ | $[0, 1]$ | Grid search (e.g., 0, 0.1, 0.5, 0.9, 1) + CV |

**Typical workflow**:
1. Fix $\alpha$, compute $\lambda$ path via CV → get CV-MSE($\lambda$)
2. Repeat for multiple $\alpha$ values
3. Select $(\alpha^*, \lambda^*)$ minimizing CV error
4. Refit on full data with $(\alpha^*, \lambda^*)$

---

##### When to Use Elastic Net

| Scenario | Why Elastic Net |
|----------|-----------------|
| **$p \gg n$** (high-dimensional) | Lasso part selects features |
| **Correlated predictors** (genomics, spectroscopy, finance) | Ridge part groups them |
| **Sparse true model with grouped signals** | Both properties needed |
| **Better prediction than Lasso/Ridge alone** | Often dominates in CV |

---

##### Comparison Summary

| Property | Ridge | Lasso | Elastic Net |
|----------|-------|-------|-------------|
| **Sparsity** | No | Yes | Yes (tunable) |
| **Feature Selection** | No | Yes | Yes |
| **Correlated Features** | Keeps all (shrinks together) | Picks one arbitrarily | **Groups them** |
| **Groups Correlated** | Implicitly | No | **Explicitly** |
| **Solution Path** | Smooth | Piecewise linear | Piecewise linear |
| **Parameters** | $\lambda$ | $\lambda$ | $\lambda, \alpha$ |
| **Best For** | Multicollinearity, dense signals | Sparse signals, interpretability | **Correlated + Sparse** |

---

##### Practical Tips

1. **Standardize features** before Elastic Net (penalty is scale-sensitive)
2. **Use `sklearn.linear_model.ElasticNetCV`** or `glmnet` (R) for efficient CV
3. **Default $\alpha=0.5$** often works well; try $\{0.1, 0.5, 0.9\}$
4. **$\lambda$ path**: Start from $\lambda_{\max}$ (all zeros) down to $\lambda_{\min} = \epsilon \lambda_{\max}$ ($\epsilon \approx 0.001$)
5. **For classification**: Use `LogisticRegression(penalty='elasticnet', solver='saga')`

---

##### Elastic Net in Scikit-learn

```python
from sklearn.linear_model import ElasticNetCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Pipeline with standardization
model = make_pipeline(
    StandardScaler(),
    ElasticNetCV(
        alphas=np.logspace(-4, 1, 50),  # λ values
        l1_ratio=[0.1, 0.5, 0.7, 0.9, 0.95, 1.0],  # α values
        cv=5,
        max_iter=10000,
        random_state=42
    )
)

model.fit(X, y)
best_alpha = model[-1].alpha_
best_l1_ratio = model[-1].l1_ratio_
coef = model[-1].coef_
selected_features = np.where(coef != 0)[0]
```

---

---

## Cross-Reference Summary

| SEP23 Question | Status | Reference |
|----------------|--------|-----------|
| Q1(a) ML vs Traditional | ✅ Covered | [AUG25 Q1(a)](./AUG25.md#q1a-describe-machine-learning-and-highlight-its-key-differences-from-traditional-programming-methods-5-marks) |
| Q1(b) Dimensionality Reduction + t-SNE | ✅ **NEW** | This file |
| Q1(c) Reinforcement Learning | ✅ Covered | [AUG25 Q1(c)](./AUG25.md#q1c-write-a-note-on-reinforcement-learning-4-marks) |
| Q2(a) Parametric vs Nonparametric | ✅ **NEW** | This file |
| Q2(b) Supervised vs Unsupervised | ✅ Covered | [AUG25 Q2(b)](./AUG25.md#q2b-what-distinguishes-unsupervised-learning-from-supervised-and-semi-supervised-learning-techniques-6-marks) |
| Q2(c) Grouping & Grading | ✅ Covered | [AUG25 Q2(c)](./AUG25.md#q2c-explain-grouping-and-grading-models-in-machine-learning-with-an-example-4-marks) |
| Q3(a) Random Forest Regression | ✅ Covered | [AUG25 Q3(a)](./AUG25.md#q3a-elaborate-decision-tree-regression-and-random-forest-regression-6-marks) |
| Q3(b) Multivariate vs Univariate | ✅ Covered | [AUG25 Q3(b)](./AUG25.md#q3b-differentiate-between-multivariate-regression-and-univariate-regression-4-marks) |
| Q3(c) Regression Types | ✅ Covered | [AUG25 Q4(c)](./AUG25.md#q4c-list-and-explain-any-two-different-types-of-regression-5-marks) |
| Q4(a) Under/Overfitting + Techniques | ✅ Partial | [AUG25 Q4(a)](./AUG25.md#q4a-which-one-of-these-is-underfit-or-overfit-why-comment-with-respect-to-bias-and-variance-6-marks) + **new techniques above** |
| Q4(b) Regression Metrics | ✅ Covered | [AUG25 Q4(b)](./AUG25.md#q4b-explain-any-two-evaluation-metrics-in-regression-model-4-marks) |
| Q4(c) Elastic Net | ✅ **NEW** | This file |

---

## Formula Sheet (SEP23 Specific)

### Dimensionality Reduction
- **PCA**: $S = \frac{1}{n}X^T X$, eigendecomposition
- **LDA**: $S_B w = \lambda S_W w$
- **t-SNE**: $P_{ij} \propto \exp(-\|x_i-x_j\|^2/2\sigma^2)$, $Q_{ij} \propto (1+\|y_i-y_j\|^2)^{-1}$, minimize $\text{KL}(P\|Q)$

### Parametric vs Nonparametric
- Parametric: Fixed $p$ parameters (Linear Reg, NN fixed arch)
- Nonparametric: Parameters grow with $n$ (KNN, Trees, Kernel SVM)

### Overfitting Reduction
- Regularization: $\min \mathcal{L} + \lambda \Omega(\theta)$
- Early Stopping: Stop when $\mathcal{L}_{\text{val}}$ increases
- Dropout: $y = (x \odot m) / (1-p)$ where $m \sim \text{Bernoulli}(1-p)$

### Elastic Net
$$\min_\beta \frac{1}{2n}\|y-X\beta\|_2^2 + \lambda\left[\alpha\|\beta\|_1 + \frac{1-\alpha}{2}\|\beta\|_2^2\right]$$
Soft threshold: $S(z,\gamma) = \text{sign}(z)\max(|z|-\gamma,0)$
Coordinate update: $\beta_j = S(X_j^T r_j / n, \lambda\alpha) / (1 + \lambda(1-\alpha))$

---

## Tags
#SPPU #AIDS #SEM7 #MachineLearning #InSem #SEP23 #ExamAnswers #DimensionalityReduction #TSNE #ParametricVsNonparametric #OverfittingReduction #ElasticNet