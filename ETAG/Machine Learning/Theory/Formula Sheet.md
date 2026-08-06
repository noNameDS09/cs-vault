---
tags: [machine-learning, gate-da, formula-sheet, revision]
---

# Formula Sheet - GATE DA 2027 Machine Learning

> [!important] **30-Minute Revision Sheet** - All key formulas grouped by topic, no explanations

---

## 📊 SUPERVISED LEARNING - REGRESSION

### Simple Linear Regression
$$
\hat{y} = \beta_0 + \beta_1 x
$$
$$
\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{Cov(x,y)}{Var(x)}
$$
$$
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$
$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = \frac{SS_{reg}}{SS_{tot}} = r^2
$$
$$
MSE = \frac{1}{n}\sum (y_i - \hat{y}_i)^2, \quad RMSE = \sqrt{MSE}
$$

### Multiple Linear Regression
$$
\hat{y} = \beta_0 + \beta_1 x_1 + ... + \beta_p x_p = X\beta
$$
$$
\hat{\beta} = (X^T X)^{-1} X^T y \quad \text{(Normal Equation)}
$$
$$
R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}
$$

### Ridge Regression (L2)
$$
\min_\beta ||y - X\beta||^2_2 + \lambda ||\beta||^2_2
$$
$$
\hat{\beta}_{ridge} = (X^T X + \lambda I)^{-1} X^T y
$$

### Lasso Regression (L1)
$$
\min_\beta ||y - X\beta||^2_2 + \lambda ||\beta||_1
$$

---

## 📈 SUPERVISED LEARNING - CLASSIFICATION

### Logistic Regression
$$
P(y=1|x) = \sigma(\beta_0 + \beta^T x) = \frac{1}{1 + e^{-(\beta_0 + \beta^T x)}}
$$
$$
\text{Log-odds: } \log\frac{P(y=1|x)}{P(y=0|x)} = \beta_0 + \beta^T x
$$
$$
\text{Cross-Entropy Loss: } J(\beta) = -\frac{1}{n}\sum [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]
$$
$$
\text{Gradient: } \frac{\partial J}{\partial \beta_j} = \frac{1}{n}\sum (\hat{y}_i - y_i)x_{ij}
$$

### K-Nearest Neighbors (KNN)
$$
d(x, x') = \sqrt{\sum (x_i - x'_i)^2} \quad \text{(Euclidean)}
$$
$$
d(x, x') = \sum |x_i - x'_i| \quad \text{(Manhattan)}
$$
$$
\text{Majority vote of } k \text{ nearest neighbors}
$$

### Naive Bayes
$$
P(C_k|x) = \frac{P(C_k)\prod_{i=1}^p P(x_i|C_k)}{P(x)} \propto P(C_k)\prod P(x_i|C_k)
$$
$$
\text{Gaussian NB: } P(x_i|C_k) = \frac{1}{\sqrt{2\pi\sigma_{ik}^2}}e^{-\frac{(x_i-\mu_{ik})^2}{2\sigma_{ik}^2}}
$$

### Linear Discriminant Analysis (LDA)
$$
\delta_k(x) = x^T \Sigma^{-1} \mu_k - \frac{1}{2}\mu_k^T \Sigma^{-1} \mu_k + \log \pi_k
$$
$$
\Sigma = \frac{1}{n-K}\sum_{k=1}^K \sum_{i:y_i=k} (x_i - \mu_k)(x_i - \mu_k)^T
$$
$$
\text{Between-class scatter: } S_B = \sum_{k=1}^K n_k (\mu_k - \mu)(\mu_k - \mu)^T
$$
$$
\text{Within-class scatter: } S_W = \sum_{k=1}^K \sum_{i:y_i=k} (x_i - \mu_k)(x_i - \mu_k)^T
$$
$$
\text{Maximize: } \frac{w^T S_B w}{w^T S_W w} \Rightarrow S_B w = \lambda S_W w
$$

### Support Vector Machine (SVM)
$$
\text{Primal (Hard Margin): } \min_{w,b} \frac{1}{2}||w||^2 \text{ s.t. } y_i(w^T x_i + b) \geq 1
$$
$$
\text{Primal (Soft Margin): } \min_{w,b,\xi} \frac{1}{2}||w||^2 + C\sum \xi_i \text{ s.t. } y_i(w^T x_i + b) \geq 1-\xi_i, \xi_i \geq 0
$$
$$
\text{Dual: } \max_\alpha \sum \alpha_i - \frac{1}{2}\sum\sum \alpha_i \alpha_j y_i y_j x_i^T x_j
$$
$$
\text{Kernels: } K(x_i, x_j) = \phi(x_i)^T \phi(x_j)
$$
$$
\text{RBF Kernel: } K(x_i, x_j) = e^{-\gamma ||x_i - x_j||^2}
$$
$$
\text{Decision: } f(x) = \text{sign}(\sum \alpha_i y_i K(x_i, x) + b)
$$

### Decision Trees
$$
\text{Gini Impurity: } G = 1 - \sum_{k=1}^K p_k^2
$$
$$
\text{Entropy: } H = -\sum_{k=1}^K p_k \log_2 p_k
$$
$$
\text{Information Gain: } IG = H(parent) - \sum \frac{n_{child}}{n_{parent}} H(child)
$$
$$
\text{Gini Gain: } \Delta G = G(parent) - \sum \frac{n_{child}}{n_{parent}} G(child)
$$

---

## ⚖️ BIAS-VARIANCE TRADEOFF
$$
\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
$$
$$
\text{Bias}(\hat{f}) = E[\hat{f}(x)] - f(x)
$$
$$
\text{Variance}(\hat{f}) = E[(\hat{f}(x) - E[\hat{f}(x)])^2]
$$
$$
\text{MSE} = \text{Bias}^2 + \text{Variance} + \sigma^2
$$

---

## 🔄 CROSS VALIDATION
### K-Fold CV
$$
CV = \frac{1}{K}\sum_{k=1}^K L(f^{(-k)}, D_k)
$$
### LOOCV (Leave-One-Out)
$$
LOOCV = \frac{1}{n}\sum_{i=1}^n L(f^{(-i)}, (x_i, y_i))
$$
### LOOCV Shortcut for Linear Models
$$
LOOCV = \frac{1}{n}\sum_{i=1}^n \left(\frac{y_i - \hat{y}_i}{1 - h_{ii}}\right)^2, \quad h_{ii} = X_i(X^T X)^{-1}X_i^T
$$

---

## 🧠 NEURAL NETWORKS

### Activation Functions
$$
\text{Sigmoid: } \sigma(z) = \frac{1}{1+e^{-z}}, \quad \sigma'(z) = \sigma(z)(1-\sigma(z))
$$
$$
\text{Tanh: } \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}, \quad \tanh'(z) = 1 - \tanh^2(z)
$$
$$
\text{ReLU: } \text{ReLU}(z) = \max(0,z), \quad \text{ReLU}'(z) = \begin{cases} 1 & z>0 \\ 0 & z\leq 0 \end{cases}
$$
$$
\text{Softmax: } \sigma(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

### Feedforward
$$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}, \quad a^{[l]} = g^{[l]}(z^{[l]})
$$

### Backpropagation (Chain Rule)
$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot g'^{[l]}(z^{[l]})
$$
$$
\frac{\partial J}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T, \quad \frac{\partial J}{\partial b^{[l]}} = \delta^{[l]}
$$
$$
\text{Output layer: } \delta^{[L]} = \nabla_a J \odot g'^{[L]}(z^{[L]})
$$

### Loss Functions
$$
\text{MSE: } J = \frac{1}{2n}\sum ||y - \hat{y}||^2
$$
$$
\text{Cross-Entropy: } J = -\sum y \log \hat{y}
$$

### Gradient Descent
$$
W := W - \alpha \frac{\partial J}{\partial W}, \quad b := b - \alpha \frac{\partial J}{\partial b}
$$
$$
\text{Momentum: } v := \beta v + (1-\beta)\nabla J, \quad W := W - \alpha v
$$

---

## 🔍 UNSUPERVISED LEARNING

### K-Means
$$
\text{Objective: } \min \sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2
$$
$$
\text{Update centroid: } \mu_i = \frac{1}{|C_i|}\sum_{x \in C_i} x
$$
$$
\text{WCSS (Elbow method): } \sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2
$$

### K-Medoids
$$
\text{Medoid: } m_i = \arg\min_{x \in C_i} \sum_{y \in C_i} d(x, y)
$$
$$
\text{Minimizes sum of pairwise distances within clusters}
$$

### Hierarchical Clustering
$$
\text{Single Linkage: } d(C_i, C_j) = \min_{x\in C_i, y\in C_j} d(x,y)
$$
$$
\text{Complete Linkage: } d(C_i, C_j) = \max_{x\in C_i, y\in C_j} d(x,y)
$$
$$
\text{Average Linkage: } d(C_i, C_j) = \frac{1}{|C_i||C_j|}\sum_{x\in C_i}\sum_{y\in C_j} d(x,y)
$$

### PCA
$$
\text{Covariance: } \Sigma = \frac{1}{n-1}X^T X \quad \text{(centered X)}
$$
$$
\text{Eigendecomposition: } \Sigma v = \lambda v
$$
$$
\text{Principal Components: } Z = X V_k \quad (V_k = \text{top k eigenvectors})
$$
$$
\text{Explained Variance Ratio: } \frac{\lambda_i}{\sum \lambda_j}
$$
$$
\text{Reconstruction: } \hat{X} = Z V_k^T
$$

---

## 📏 DISTANCE METRICS
$$
\text{Euclidean: } d(x,y) = \sqrt{\sum (x_i - y_i)^2}
$$
$$
\text{Manhattan: } d(x,y) = \sum |x_i - y_i|
$$
$$
\text{Minkowski: } d(x,y) = (\sum |x_i - y_i|^p)^{1/p}
$$
$$
\text{Cosine Similarity: } \cos\theta = \frac{x^T y}{||x|| ||y||}
$$
$$
\text{Mahalanobis: } d(x,y) = \sqrt{(x-y)^T \Sigma^{-1} (x-y)}
$$

---

## 🎯 EVALUATION METRICS
$$
\text{Accuracy} = \frac{TP+TN}{TP+TN+FP+FN}
$$
$$
\text{Precision} = \frac{TP}{TP+FP}, \quad \text{Recall} = \frac{TP}{TP+FN}
$$
$$
\text{F1} = 2\frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$
$$
\text{Specificity} = \frac{TN}{TN+FP}
$$
$$
\text{ROC-AUC} = \int_0^1 \text{TPR}(FPR) dFPR
$$

---

## 🔧 REGULARIZATION
$$
\text{Ridge: } \lambda \sum \beta_j^2 \quad \text{(shrinkage, no sparsity)}
$$
$$
\text{Lasso: } \lambda \sum |\beta_j| \quad \text{(sparsity, feature selection)}
$$
$$
\text{Elastic Net: } \lambda_1 \sum |\beta_j| + \lambda_2 \sum \beta_j^2
$$

---

## 📐 MATRIX CALCULUS SHORTCUTS
$$
\frac{\partial a^T X b}{\partial X} = a b^T
$$
$$
\frac{\partial X^T A X}{\partial X} = (A + A^T)X
$$
$$
\frac{\partial ||y - X\beta||^2}{\partial \beta} = -2X^T(y - X\beta)
$$
$$
\frac{\partial \log|X|}{\partial X} = (X^{-1})^T
$$

---

## 🚀 GATE QUICK TRICKS

| Concept | Trick |
|---------|-------|
| Ridge vs Lasso | Ridge: shrink | Lasso: select (sparse) |
| PCA vs LDA | PCA: unsupervised, max variance | LDA: supervised, max separation |
| K-Means vs K-Medoids | K-Means: centroid (mean) | K-Medoids: medoid (actual point) |
| Entropy vs Gini | Entropy: -∑p log p | Gini: 1-∑p² (faster) |
| SVM C parameter | C ↑ = less regularization, harder margin |
| SVM γ in RBF | γ ↑ = tighter fit, more complex boundary |
| LOOCV for linear | Use hat matrix diagonal: (1-hᵢᵢ) |
| Eigenvalues in PCA | λ₁ ≥ λ₂ ≥ ... ≥ λₚ, sum = total variance |
| Bias-Variance | High bias = underfit | High variance = overfit |

---

## Related Notes

- [[Glossary]]
- [[01 Supervised Learning]]
- [[17 Unsupervised Learning]]

---

#machine-learning #gate-da #formula-sheet #revision