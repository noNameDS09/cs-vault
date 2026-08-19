# SPPU AIDS BE SEM VII - Machine Learning In-Sem Exam Answers (SEP 2024)

> **Course**: Machine Learning | **Semester**: VII | **Branch**: AIDS
> **Exam**: In-Semester Examination | **Date**: September 2024
> **Total Marks**: 50

> **Note**: Several questions overlap with [AUG25 Paper](./AUG25.md). This file contains **only new/unanswered questions** with cross-references to the previous paper.

---

## Question 1

### Q1(a) Describe Machine Learning and differentiate it from traditional programming. [6]

> **Already answered in [AUG25.md Q1(a)](./AUG25.md#q1a-describe-machine-learning-and-highlight-its-key-differences-from-traditional-programming-methods-5-marks)** (5 marks version). The 6-mark version requires slightly more detail — see below for the **additional points** to include for the extra mark.

---

#### Additional Points for 6-Mark Answer

| Aspect | Additional Detail for 6 Marks |
|--------|-------------------------------|
| **Formal Definition** | Include Tom Mitchell's definition with $E, T, P$ triplet |
| **Learning Paradigms** | Briefly name all 4 types (Supervised, Unsupervised, Semi-Supervised, Reinforcement) with one-line descriptions |
| **Workflow Diagram** | Add the "ML Pipeline" diagram: Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment → Monitoring |
| **When to Use ML vs Traditional** | Decision criteria: Use ML when (1) Rules are unknown/complex, (2) Data patterns change over time, (3) Scale exceeds human coding capacity, (4) Problem involves perception (vision, speech, NLP) |
| **Limitations of ML** | Data dependency, interpretability challenges, bias/fairness risks, computational cost, adversarial vulnerability |

---

#### ML Pipeline Diagram (Additional)

```
┌─────────────┐    ┌──────────────┐    ┌───────────────┐    ┌──────────────┐
│   DATA      │───►│  PREPROCESS  │───►│ FEATURE ENG.  │───►│   TRAINING   │
│ COLLECTION  │    │  (Cleaning,  │    │ (Selection,   │    │ (Algorithm,  │
│ (Raw Data)  │    │  Normalize)  │    │  Extraction)  │    │  Hyperparams)│
└─────────────┘    └──────────────┘    └───────────────┘    └──────┬───────┘
                                                                     │
┌─────────────┐    ┌──────────────┐    ┌───────────────┐           │
│  MONITORING │◄───│  DEPLOYMENT  │◄───│  EVALUATION   │◄──────────┘
│ (Drift,     │    │ (Serving,    │    │ (Metrics,     │
│  Retrain)   │    │  API, A/B)   │    │  Validation)  │
└─────────────┘    └──────────────┘    └───────────────┘
```

---

### Q1(b) Explain Principal Component Analysis used in Machine Learning. [5]

> **Partially covered in [AUG25.md Q1(b)](./AUG25.md#q1b-explain-the-main-difference-between-linear-discriminant-analysis-lda-and-principal-component-analysis-pca-in-reducing-dimensions-6-marks)** as part of PCA vs LDA comparison. Below is a **standalone detailed explanation** of PCA for 5 marks.

---

#### Principal Component Analysis (PCA)

**PCA** is an **unsupervised linear dimensionality reduction** technique that transforms high-dimensional data into a lower-dimensional subspace while preserving **maximum variance**.

---

##### Core Idea

> Find orthogonal directions (principal components) in feature space along which data varies the most. Project data onto top-$k$ components.

---

##### Mathematical Formulation

Given centered data matrix $X \in \mathbb{R}^{n \times d}$ ($\frac{1}{n}\sum_i x_i = 0$):

1. **Covariance Matrix**: $S = \frac{1}{n} X^T X \in \mathbb{R}^{d \times d}$

2. **Objective**: Find projection matrix $W \in \mathbb{R}^{d \times k}$ ($k \ll d$) maximizing variance of projected data:
   $$J(W) = \text{Tr}(W^T S W) = \sum_{i=1}^k w_i^T S w_i$$
   subject to $W^T W = I$ (orthonormal columns)

3. **Solution**: Eigenvectors of $S$ corresponding to the $k$ **largest eigenvalues** $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_k$

4. **Projection**: $Z = X W \in \mathbb{R}^{n \times k}$ (reduced data)

---

##### Variance Explained

- Eigenvalue $\lambda_i$ = variance captured by $i$-th principal component
- **Total Variance** = $\sum_{i=1}^d \lambda_i = \text{Tr}(S)$
- **Proportion of Variance Explained (PVE)** by first $k$ components:
  $$\text{PVE}(k) = \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^d \lambda_i}$$
- Choose $k$ such that $\text{PVE}(k) \geq 0.90$ or $0.95$ (elbow method on scree plot)

---

##### Algorithm Steps

```
PCA(X, k):
    1. Center data: X_centered = X - mean(X, axis=0)
    2. Compute covariance: S = (1/n) * X_centered^T @ X_centered
    3. Eigendecomposition: eigenvalues λ, eigenvectors V = eig(S)
    4. Sort by λ descending: V_sorted = V[:, argsort(λ)[::-1]]
    5. Select top-k: W = V_sorted[:, :k]
    6. Project: Z = X_centered @ W
    7. Return Z, W, λ_sorted[:k]
```

> **Practical Note**: Use SVD on $X$ directly (more numerically stable): $X = U \Sigma V^T$, then $W = V[:, :k]$, $Z = U[:, :k] \Sigma[:k, :k]$

---

##### Properties

| Property | Description |
|----------|-------------|
| **Orthogonality** | $w_i^T w_j = 0$ for $i \neq j$ (uncorrelated components) |
| **Max Variance** | PC1 captures max variance; PC2 captures max remaining variance orthogonal to PC1, etc. |
| **Reconstruction** | $\hat{X} = Z W^T$ minimizes $\|X - \hat{X}\|_F^2$ among all rank-$k$ approximations (Eckart-Young theorem) |
| **Unsupervised** | Does not use labels $y$ |
| **Linear** | Only captures linear correlations |

---

##### Applications

| Application | Description |
|-------------|-------------|
| **Visualization** | Project to 2D/3D for scatter plots |
| **Noise Reduction** | Reconstruct from top-$k$ PCs (denoising) |
| **Feature Extraction** | Use $Z$ as input to downstream models |
| **Compression** | Store $Z$ + $W$ instead of $X$ |
| **Multicollinearity Fix** | PCs are orthogonal → stable regression |
| **Anomaly Detection** | High reconstruction error = anomaly |

---

##### Limitations

- **Linear only** — fails for non-linear manifolds (use Kernel PCA, t-SNE, UMAP)
- **Sensitive to scaling** — **must standardize** features first ($z$-score)
- **Sensitive to outliers** — use Robust PCA or preprocess outliers
- **Interpretability** — PCs are linear combinations of all features
- **Variance ≠ Relevance** — High variance directions may not be predictive

---

### Q1(c) Explain the relationship between Artificial Intelligence, Machine Learning and data science. [4]

---

#### Venn Diagram Relationship

```
         ┌─────────────────────────────────────┐
         │        ARTIFICIAL INTELLIGENCE      │
         │  (Broad: Machines mimicking human   │
         │   intelligence - reasoning,         │
         │   perception, planning, learning)   │
         │                                     │
         │  ┌─────────────────────────────┐    │
         │  │      MACHINE LEARNING       │    │
         │  │  (Subset of AI: Algorithms  │    │
         │  │   that learn from data      │    │
         │  │   without explicit prog.)   │    │
         │  │                             │    │
         │  │  ┌─────────────────────┐    │    │
         │  │  │   DEEP LEARNING     │    │    │
         │  │  │ (Subset of ML:      │    │    │
         │  │  │  Neural Networks    │    │    │
         │  │  │  with many layers)  │    │    │
         │  │  └─────────────────────┘    │    │
         │  └─────────────────────────────┘    │
         │                                     │
         │  ┌─────────────────────────────┐    │
         │  │       DATA SCIENCE          │    │
         │  │  (Interdisciplinary field:  │    │
         │  │   Statistics + CS + Domain  │    │
         │  │   Uses ML as a TOOL         │    │
         │  │   + Data Engineering, Viz,  │    │
         │  │   Storytelling, Deployment) │    │
         │  │                             │    │
         │  │  Overlaps with ML but       │    │
         │  │  NOT a subset of AI         │    │
         │  └─────────────────────────────┘    │
         └─────────────────────────────────────┘
```

---

#### Definitions & Scope

| Field | Scope | Core Focus | Key Tools |
|-------|-------|------------|-----------|
| **Artificial Intelligence (AI)** | Broadest | Building intelligent agents | Search, Logic, Planning, ML, Robotics, NLP, CV |
| **Machine Learning (ML)** | Subset of AI | Learning patterns from data | Supervised/Unsupervised/RL, Neural Nets, Trees |
| **Data Science** | Interdisciplinary (overlaps) | Extracting insights from data | Statistics, ML, Viz, SQL, Big Data, Domain Knowledge |

---

#### Relationship Summary

| Relationship      | Description                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **$ML ⊂ AI$**     | ML is the "learning" component of modern AI; most current AI breakthroughs are ML-driven                                                 |
| **$DS ∩ ML ≠ ∅$** | Data Science **uses** ML as a core tool, but also includes data cleaning, ETL, visualization, experimentation, communication, deployment |
| **$DS ⊄ AI$**     | Data Science includes descriptive analytics, BI, reporting — not necessarily "intelligent"                                               |
| **$AI ⊄ DS$**     | AI includes rule-based systems, robotics, game playing — not necessarily data-driven                                                     |

---

#### Practical Workflow

```
BUSINESS PROBLEM
       │
       ▼
┌──────────────────┐
│  DATA SCIENCE    │ ← Frames problem, collects/cleans data, defines metrics
│  (End-to-end)    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  MACHINE LEARNING│ ← Builds predictive models, tunes, validates
│  (Modeling core) │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  ARTIFICIAL      │ ← Deploys as intelligent service (API, edge, embedded)
│  INTELLIGENCE    │
│ (Product/Service)│
└──────────────────┘
```

---

#### Key Insight

> **AI is the "What" (goal), ML is the "How" (method), Data Science is the "Process" (end-to-end discipline).**

---

## Question 2

### Q2(a) Explain types of Machine Learning. [6]

> **Already answered in [AUG25.md Q2(b)](./AUG25.md#q2b-what-distinguishes-unsupervised-learning-from-supervised-and-semi-supervised-learning-techniques-6-marks)** with detailed comparison table.

---

### Q2(b) Explain Linear Discriminant Analysis (LDA) used in Machine Learning. [5]

> **Already answered in [AUG25.md Q1(b)](./AUG25.md#q1b-explain-the-main-difference-between-linear-discriminant-analysis-lda-and-principal-component-analysis-pca-in-reducing-dimensions-6-marks)** as part of PCA vs LDA. Below is **standalone LDA explanation** for 5 marks.

---

#### Linear Discriminant Analysis (LDA)

**LDA** is a **supervised linear dimensionality reduction** and **classification** technique that projects data onto directions maximizing **class separability**.

---

##### Objective (Fisher's Criterion)

Find projection $W$ maximizing ratio of **between-class scatter** to **within-class scatter**:

$$J(W) = \frac{|W^T S_B W|}{|W^T S_W W|}$$

where:
- $S_B = \sum_{c=1}^C n_c (\mu_c - \mu)(\mu_c - \mu)^T$ (Between-class scatter)
- $S_W = \sum_{c=1}^C \sum_{x \in \mathcal{C}_c} (x - \mu_c)(x - \mu_c)^T$ (Within-class scatter)
- $\mu_c$ = mean of class $c$, $\mu$ = global mean, $n_c$ = samples in class $c$
- $C$ = number of classes

---

##### Solution

Solve generalized eigenvalue problem:
$$S_B w = \lambda S_W w$$

Equivalently: eigenvectors of $S_W^{-1} S_B$ corresponding to largest eigenvalues.

**Maximum components**: $k_{\max} = C - 1$ (since $\text{rank}(S_B) \leq C-1$)

---

##### LDA as Classifier (Generative)

LDA assumes:
1. **Class-conditional densities** are Gaussian: $p(x|y=c) = \mathcal{N}(\mu_c, \Sigma)$
2. **Shared covariance** $\Sigma$ across all classes
3. **Class priors** $\pi_c = P(y=c)$

**Decision Rule** (Linear discriminant function):
$$\delta_c(x) = x^T \Sigma^{-1} \mu_c - \frac{1}{2} \mu_c^T \Sigma^{-1} \mu_c + \log \pi_c$$

Assign $x$ to class with highest $\delta_c(x)$ → **linear decision boundaries**.

---

##### Algorithm

```
LDA(X, y, k):
    1. Compute class means μ_c and global mean μ
    2. Compute S_W (within-class scatter)
    3. Compute S_B (between-class scatter)
    4. Solve S_B w = λ S_W w  →  eigenvectors W (top k)
    5. Project: Z = X @ W
    6. (Optional) For classification: fit Gaussian with shared Σ on Z
    7. Return Z, W
```

---

##### Assumptions

| Assumption              | Implication                                        |
| ----------------------- | -------------------------------------------------- |
| **Gaussian classes**    | $p(xy=c) \sim \mathcal{N}(\mu_c, \Sigma)$          |
| **Equal covariance**    | $\Sigma_c = \Sigma \ \forall c$ (homoscedasticity) |
| **Linear boundaries**   | Optimal only when classes are linearly separable   |
| **Features continuous** | Not ideal for categorical features                 |

---

##### LDA vs PCA Summary

| Aspect | PCA | LDA |
|--------|-----|-----|
| **Supervision** | Unsupervised | Supervised |
| **Goal** | Max variance | Max class separation |
| **Uses labels** | No | Yes |
| **Max components** | $\min(n, d)$ | $C - 1$ |
| **Optimality** | Reconstruction | Classification |
| **Covariance** | Total $S_T$ | $S_W^{-1} S_B$ |

---

##### When to Use LDA

- Classification with **few classes** ($C$ small)
- **Linearly separable** or near-linearly separable classes
- **Small sample size** (works better than QDA when $n$ small)
- **Dimensionality reduction** before another classifier (e.g., LDA → SVM)
- **Interpretability** needed (linear discriminants)

---

### Q2(c) Differentiate Grouping and Grading models of Machine Learning. [4]

> **Already answered in [AUG25.md Q2(c)](./AUG25.md#q2c-explain-grouping-and-grading-models-in-machine-learning-with-an-example-4-marks)**.

---

## Question 3

### Q3(a) Explain three evaluation metrics used for regression model. [6]

> **Partially covered in [AUG25.md Q4(b)](./AUG25.md#q4b-explain-any-two-evaluation-metrics-in-regression-model-4-marks)** (2 metrics: MSE, MAE). Below adds **third metric (R²)** and expands for 6 marks.

---

#### 1. Mean Squared Error (MSE) / Root MSE (RMSE)

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2$$
$$\text{RMSE} = \sqrt{\text{MSE}}$$

| Property              | Detail                                        |
| --------------------- | --------------------------------------------- |
| **Penalty**           | Quadratic — heavily penalizes large errors    |
| **Optimal predictor** | Conditional mean $\mathbb{E}[YX]$             |
| **Units**             | MSE: squared target units; RMSE: target units |
| **Differentiable**    | Yes — used as loss function for training      |
| **Sensitivity**       | High to outliers                              |

**When to use**: General purpose; when large errors are disproportionately bad (safety, finance).

---

#### 2. Mean Absolute Error (MAE)

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$

| Property              | Detail                                   |
| --------------------- | ---------------------------------------- |
| **Penalty**           | Linear — proportional to error magnitude |
| **Optimal predictor** | Conditional median $\text{Median}[YX]$   |
| **Units**             | Target units (directly interpretable)    |
| **Robustness**        | Robust to outliers                       |
| **Differentiable**    | No (at 0) — use Huber loss for training  |

**When to use**: When outliers are noise; business reporting ("avg error = $500").

---

#### 3. Coefficient of Determination ($R^2$)

$$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2} = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$$

where $\bar{y} = \frac{1}{n}\sum y_i$, $\text{SS}_{\text{res}}$ = residual sum of squares, $\text{SS}_{\text{tot}}$ = total sum of squares.

---

##### Interpretation

| $R^2$ Value | Interpretation |
|-------------|----------------|
| $1.0$ | Perfect fit |
| $0.7 - 0.9$ | Strong fit |
| $0.5 - 0.7$ | Moderate fit |
| $0.0$ | Model = horizontal line (mean predictor) |
| $< 0$ | Worse than mean predictor (possible on test set) |

---

##### Properties

| Property | Detail |
|----------|--------|
| **Scale-free** | Unitless — comparable across datasets |
| **Baseline** | Compares against naïve mean predictor |
| **Variance explained** | Proportion of target variance captured by model |
| **Relation to correlation** | For univariate linear regression: $R^2 = \rho_{y,\hat{y}}^2$ |

---

##### Adjusted $R^2$ (for multiple regression)

$$\bar{R}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

where $p$ = number of predictors. Penalizes adding non-informative features.

---

##### Comparison Table

| Metric             | Formula                                                                                 | Scale                    | Outlier Sensitivity         | Optimal Predictor | Best For                               |
| ------------------ | --------------------------------------------------------------------------------------- | ------------------------ | --------------------------- | ----------------- | -------------------------------------- |
| **MSE**            | $\displaystyle \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$                              | Squared units            | High                        | Mean              | Training loss, large-error penalty     |
| **RMSE**           | $\displaystyle \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}$                       | Target units             | High                        | Mean              | Interpretability + MSE properties      |
| **MAE**            | $\displaystyle \frac{1}{n}\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$                     | Target units             | Low                         | Median            | Robust evaluation, business reporting  |
| **$R^2$**          | $\displaystyle 1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{\sum_{i=1}^{n}(y_i-\bar{y})^2}$ | Unitless ($[-\infty,1]$) | Medium (via squared errors) | —                 | Model comparison, variance explained   |
| **Adjusted $R^2$** | $\displaystyle 1-(1-R^2)\frac{n-1}{n-p-1}$                                              | Unitless                 | Medium                      | —                 | Feature selection, multiple regression |

---

##### Practical Recommendation

> **Report all three**: RMSE (scale-aware), MAE (robust typical error), $R^2$ (scale-free goodness-of-fit). Check if $R^2$ on test $\approx$ train (else overfitting).

---

### Q3(b) Explain the Random forest Regression. [5]

> **Already answered in [AUG25.md Q3(a)](./AUG25.md#q3a-elaborate-decision-tree-regression-and-random-forest-regression-6-marks)** (covers both Decision Tree and Random Forest Regression in detail).

---

### Q3(c) Differentiate between Regression and Correlation. [4]

---

#### Regression vs Correlation

| Aspect | **Regression** | **Correlation** |
|--------|----------------|-----------------|
| **Purpose** | Model $Y$ as function of $X$: predict/explain $Y$ | Measure **strength & direction** of linear association |
| **Directionality** | **Asymmetric**: $Y = f(X) + \epsilon$ (dependent vs independent) | **Symmetric**: $\rho(X,Y) = \rho(Y,X)$ |
| **Output** | Equation $\hat{y} = \beta_0 + \beta_1 x + \dots$; predictions | Single number $r \in [-1, 1]$ |
| **Causality** | Can suggest causal direction (with assumptions) | **Never implies causation** |
| **Variables** | One dependent ($Y$), one/more independent ($X$) | Two variables (bivariate) or matrix (multivariate) |
| **Linearity** | Can model non-linear (polynomial, trees, NN) | Pearson = linear only; Spearman = monotonic |
| **Units** | Coefficients in $Y$-units per $X$-unit | Unitless (standardized) |
| **Intercept** | Estimated ($\beta_0$) | Not applicable (centered) |
| **Assumptions** | Linearity, independence, homoscedasticity, normality of residuals | Bivariate normality (Pearson), monotonic (Spearman) |

---

#### Mathematical Relationship

For **simple linear regression** ($Y = \beta_0 + \beta_1 X + \epsilon$):

$$\beta_1 = r \cdot \frac{s_Y}{s_X}, \quad R^2 = r^2$$

where $r$ = Pearson correlation, $s_Y, s_X$ = standard deviations.

- **Slope sign** = correlation sign
- **$R^2$** = squared correlation = proportion of variance explained

---

#### Example

| Scenario | Regression | Correlation |
|----------|------------|-------------|
| **Height → Weight** | Predict weight from height: $\text{Weight} = -50 + 0.8 \times \text{Height}$ | $r = 0.75$ (moderate positive linear association) |
| **Ice cream sales vs Temperature** | Sales = $100 + 5 \times \text{Temp}$ | $r = 0.85$ |
| **Causality?** | Suggests temp *drives* sales | Only says they move together |

---

#### Key Takeaway

> **Correlation** answers *"How strongly do X and Y move together?"*<br>
> **Regression** answers *"How does Y change when X changes? (and predict Y)"*

---

## Question 4

### Q4(a) What is Regression? Explain types of Regressions. [6]

> **Already answered in [AUG25.md Q4(c)](./AUG25.md#q4c-list-and-explain-any-two-different-types-of-regression-5-marks)** (covers Linear and Polynomial Regression). For 6 marks, include **more types**.

---

#### Additional Regression Types for 6-Mark Answer

| Type               | Equation                                                              | Key Feature                   | Use Case                               |
| ------------------ | --------------------------------------------------------------------- | ----------------------------- | -------------------------------------- |
| **Linear**         | $y = \beta_0 + X\beta$                                                | Linear in params              | Baseline, interpretability             |
| **Polynomial**     | $y = \sum_{j=0}^d \beta_j x^j$                                        | Non-linear via basis          | Smooth curves                          |
| **Ridge (L2)**     | $\min \|y-X\beta\|^2 + \lambda\|\beta\|_2^2$                          | Shrinks coefficients          | Multicollinearity, $p \approx n$       |
| **Lasso (L1)**     | $\min \|y-X\beta\|^2 + \lambda\|\beta\|_1$                            | **Feature selection**         | Sparse solutions, $p > n$              |
| **Elastic Net**    | $\min \|y-X\beta\|^2 + \lambda_1\|\beta\|_1 + \lambda_2\|\beta\|_2^2$ | Groups correlated features    | Correlated predictors                  |
| **Logistic**       | $P(y=1x) = \sigma(x^T\beta)$                                          | Classification via regression | Binary outcomes                        |
| **Quantile**       | $\min \sum \rho_\tau(y - x^T\beta)$                                   | Predicts conditional quantile | Robust, prediction intervals           |
| **Robust (Huber)** | $\min \sum L_\delta(y - x^T\beta)$                                    | Less sensitive to outliers    | Noisy data                             |
| **Bayesian**       | $p(\beta y) \propto p(y\beta)p(\beta)$                                | Full posterior uncertainty    | Small data, uncertainty quantification |


---

### Q4(b) Explain Bias-Variance Trade-off with respect to Machine Learning. [5]

> **Already answered in [AUG25.md Q3(c)](./AUG25.md#q3c-explain-bias-variance-trade-off-with-neat-diagram-5-marks)** with detailed diagram and decomposition.

---

### Q4(c) Differentiate Ridge and Lasso Regression techniques. [4]

> **Mentioned in [AUG25.md Q4(c)](./AUG25.md#q4c-list-and-explain-any-two-different-types-of-regression-5-marks)** but not differentiated in detail. Below is **dedicated comparison** for 4 marks.

---

#### Ridge vs Lasso Regression

Both are **regularized linear regression** adding penalty to OLS:

$$\text{Ridge: } \hat{\beta}_{\text{ridge}} = \arg\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_2^2$$
$$\text{Lasso: } \hat{\beta}_{\text{lasso}} = \arg\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_1$$

---

##### Penalty Geometry

||**Ridge (L2)**|**Lasso (L1)**|
|---|---|---|
|**Penalty**|$\displaystyle \lambda \sum_{j=1}^{p}\beta_j^2$|$\displaystyle \lambda \sum_{j=1}^{p}\lvert\beta_j\rvert$|
|**Constraint region**|Circle $\displaystyle \left(\sum_{j=1}^{p}\beta_j^2 \leq t\right)$|Diamond $\displaystyle \left(\sum_{j=1}^{p}\lvert\beta_j\rvert \leq t\right)$|
|**Geometry**|Smooth, round|Sharp corners at axes|
|**Effect on coefficients**|Shrinks coefficients toward $0$|Shrinks coefficients and can set some exactly to $0$|
|**Feature selection**|No automatic feature selection|Performs automatic feature selection|
|**Best suited for**|Multicollinearity and correlated predictors|Sparse models and feature selection|

```
Ridge (L2) Constraint                  Lasso (L1) Constraint

       β₂                                      β₂
       │                                       │
       │      ╭──────╮                         │       ╱╲
       │    ╱          ╲                       │      ╱  ╲
       │   │            │                      │     ╱    ╲
       │   │            │                      │    ╱      ╲
       │    ╲          ╱                       │    ╲      ╱
       │      ╰──────╯                         │     ╲    ╱
       │                                       │      ╲  ╱
       └────────────── β₁                      │       ╲╱
                                               └────────────── β₁

   ∑ βⱼ² ≤ t                              ∑ |βⱼ| ≤ t
   j=1,…,p                                j=1,…,p
```

> **Why Lasso selects features**: Diamond corners hit axes → some $\beta_j = 0$ exactly.

---

##### Closed-form (Ridge) vs Iterative (Lasso)

| | **Ridge** | **Lasso** |
|--|-----------|-----------|
| **Solution** | **Closed-form**: $\hat{\beta} = (X^T X + \lambda I)^{-1} X^T y$ | **No closed-form** — coordinate descent / LARS |
| **Computation** | Fast (direct solve) | Iterative (slower for large $p$) |
| **Path** | Smooth shrinkage | Piecewise linear (LARS) |

---

##### Coefficient Behavior

| Property | Ridge | Lasso |
|----------|-------|-------|
| **Shrinkage** | All coefficients $\to 0$ as $\lambda \to \infty$ | Some coefficients **exactly 0** (sparse) |
| **Feature Selection** | **No** — keeps all features | **Yes** — automatic variable selection |
| **Correlated Features** | Shrinks **together** (shares weight) | Picks **one**, zeros others (arbitrary) |
| **Grouping Effect** | Yes | No (without Elastic Net) |

---

##### When to Use Which

| Scenario | Recommended |
|----------|-------------|
| **Many correlated features** (multicollinearity) | **Ridge** |
| **Feature selection needed** ($p > n$, sparse true model) | **Lasso** |
| **Groups of correlated features** should be selected together | **Elastic Net** ($\alpha \approx 0.5$) |
| **Prediction accuracy primary** | Try both via CV |
| **Interpretability (sparse model)** | **Lasso** |

---

##### Hyperparameter $\lambda$ (or $\alpha$)

- $\lambda = 0$ → OLS (no regularization)
- $\lambda \to \infty$ → Ridge: all $\beta \to 0$; Lasso: all $\beta = 0$
- **Select via Cross-Validation**: $\lambda_{\text{opt}} = \arg\min_\lambda \text{CV-MSE}(\lambda)$

---

##### Summary Table

| Criterion | Ridge (L2) | Lasso (L1) |
|-----------|------------|------------|
| **Penalty** | $\lambda \|\beta\|_2^2$ | $\lambda \|\beta\|_1$ |
| **Sparsity** | No | **Yes** |
| **Feature Selection** | No | **Yes** |
| **Correlated Features** | Handles well (shares coeff) | Picks one arbitrarily |
| **Closed-form Solution** | **Yes** | No |
| **Computation** | Fast | Iterative |
| **Geometric Constraint** | Sphere | Diamond |
| **Best For** | Multicollinearity, dense signals | Sparse signals, interpretability |

---

---

## Cross-Reference Summary

| SEP24 Question | Status | Reference |
|----------------|--------|-----------|
| Q1(a) ML vs Traditional | ✅ Covered | [AUG25 Q1(a)](./AUG25.md#q1a-describe-machine-learning-and-highlight-its-key-differences-from-traditional-programming-methods-5-marks) + additions above |
| Q1(b) PCA | ✅ New detail | This file (standalone) |
| Q1(c) AI/ML/DS Relationship | ✅ New | This file |
| Q2(a) Types of ML | ✅ Covered | [AUG25 Q2(b)](./AUG25.md#q2b-what-distinguishes-unsupervised-learning-from-supervised-and-semi-supervised-learning-techniques-6-marks) |
| Q2(b) LDA | ✅ Covered | [AUG25 Q1(b)](./AUG25.md#q1b-explain-the-main-difference-between-linear-discriminant-analysis-lda-and-principal-component-analysis-pca-in-reducing-dimensions-6-marks) + standalone above |
| Q2(c) Grouping vs Grading | ✅ Covered | [AUG25 Q2(c)](./AUG25.md#q2c-explain-grouping-and-grading-models-in-machine-learning-with-an-example-4-marks) |
| Q3(a) 3 Regression Metrics | ✅ Extended | [AUG25 Q4(b)](./AUG25.md#q4b-explain-any-two-evaluation-metrics-in-regression-model-4-marks) + R² above |
| Q3(b) Random Forest Regression | ✅ Covered | [AUG25 Q3(a)](./AUG25.md#q3a-elaborate-decision-tree-regression-and-random-forest-regression-6-marks) |
| Q3(c) Regression vs Correlation | ✅ New | This file |
| Q4(a) Regression Types | ✅ Covered | [AUG25 Q4(c)](./AUG25.md#q4c-list-and-explain-any-two-different-types-of-regression-5-marks) + additions above |
| Q4(b) Bias-Variance Tradeoff | ✅ Covered | [AUG25 Q3(c)](./AUG25.md#q3c-explain-bias-variance-trade-off-with-neat-diagram-5-marks) |
| Q4(c) Ridge vs Lasso | ✅ New detail | This file |

---

## Formula Sheet (SEP24 Specific)

### PCA
$$S = \frac{1}{n}X^T X, \quad S w = \lambda w, \quad Z = X W_k$$
$$\text{PVE}(k) = \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^d \lambda_i}$$

### LDA
$$S_B = \sum_c n_c (\mu_c - \mu)(\mu_c - \mu)^T, \quad S_W = \sum_c \sum_{x\in C_c} (x-\mu_c)(x-\mu_c)^T$$
$$S_B w = \lambda S_W w, \quad k_{\max} = C-1$$

### Regression Metrics
$$\text{MSE} = \frac{1}{n}\sum(y-\hat{y})^2, \quad \text{RMSE} = \sqrt{\text{MSE}}$$
$$\text{MAE} = \frac{1}{n}\sum|y-\hat{y}|, \quad R^2 = 1 - \frac{\sum(y-\hat{y})^2}{\sum(y-\bar{y})^2}$$
$$\bar{R}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

### Ridge vs Lasso
$$\text{Ridge: } \hat{\beta} = (X^T X + \lambda I)^{-1} X^T y$$
$$\text{Lasso: } \hat{\beta} = \arg\min_\beta \|y-X\beta\|_2^2 + \lambda\|\beta\|_1$$

### Regression vs Correlation
$$\beta_1 = r \frac{s_Y}{s_X}, \quad R^2 = r^2 \quad \text{(simple linear regression)}$$

---

## Tags
#SPPU #AIDS #SEM7 #MachineLearning #InSem #SEP24 #ExamAnswers #PCA #LDA #AI_ML_DS #RegressionMetrics #R2 #RidgeVsLasso #RegressionVsCorrelation