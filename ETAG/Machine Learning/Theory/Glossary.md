---
tags: [machine-learning, gate-da, glossary, revision]
---

# Glossary

> [!note] Alphabetical reference of all ML terminology for GATE DA 2027

---

## A

| Term | Definition |
|------|------------|
| **Accuracy** | Ratio of correct predictions to total predictions: $\frac{TP+TN}{TP+TN+FP+FN}$ |
| **Activation Function** | Non-linear function applied to neuron output (e.g., Sigmoid, ReLU, Tanh) |
| **AdaBoost** | Adaptive Boosting - ensemble method that weights misclassified samples higher |
| **Adjusted R²** | R² adjusted for number of predictors: $1 - \frac{(1-R^2)(n-1)}{n-p-1}$ |
| **Agglomerative Clustering** | Bottom-up hierarchical clustering - starts with each point as cluster, merges iteratively |
| **Anisotropic** | Having different properties in different directions (e.g., Gaussian with different variances) |
| **Autoencoder** | Neural network trained to reconstruct its input - used for dimensionality reduction |

---

## B

| Term | Definition |
|------|------------|
| **Backpropagation** | Algorithm to compute gradients in neural networks using chain rule |
| **Bagging** | Bootstrap Aggregating - ensemble of models trained on bootstrap samples |
| **Bias** | Error from overly simplistic assumptions: $Bias(\hat{f}) = E[\hat{f}(x)] - f(x)$ |
| **Bias-Variance Tradeoff** | Total Error = Bias² + Variance + Irreducible Error |
| **Binary Classification** | Classification with exactly two classes |
| **Bootstrap Sample** | Random sample with replacement from dataset (size = original) |
| **Bottleneck Layer** | Compressed hidden layer in autoencoder (dimensionality reduction) |

---

## C

| Term | Definition |
|------|------------|
| **Classification** | Predicting discrete class labels |
| **Complete Linkage** | Hierarchical clustering distance = max distance between points in clusters |
| **Confusion Matrix** | Table showing TP, FP, TN, FN for classification evaluation |
| **Cost Function** | Function minimized during training (synonym: Loss Function, Objective Function) |
| **Cross-Entropy Loss** | $-\sum y_i \log(\hat{y}_i)$ for classification |
| **Cross Validation** | Technique to estimate model performance on unseen data |
| **Curse of Dimensionality** | Data becomes sparse in high dimensions; distance metrics lose meaning |

---

## D

| Term | Definition |
|------|------------|
| **Decision Boundary** | Hypersurface separating different classes in feature space |
| **Decision Tree** | Tree-structured classifier with decision rules at internal nodes |
| **Dendrogram** | Tree diagram showing hierarchical clustering merges/splits |
| **Dimensionality Reduction** | Reducing number of features while preserving information |
| **Discriminant Analysis** | Classification by finding linear combinations of features |
| **Divisive Clustering** | Top-down hierarchical clustering - starts with one cluster, splits recursively |

---

## E

| Term | Definition |
|------|------------|
| **Entropy** | Measure of impurity: $H = -\sum p_i \log_2 p_i$ |
| **Epoch** | One complete pass through entire training dataset |
| **Euclidean Distance** | $\sqrt{\sum (x_i - y_i)^2}$ - standard L2 distance |
| **Explained Variance** | Variance captured by principal components: $\frac{\lambda_i}{\sum \lambda}$ |

---

## F

| Term | Definition |
|------|------------|
| **F1 Score** | Harmonic mean of precision and recall: $2 \cdot \frac{Precision \times Recall}{Precision + Recall}$ |
| **False Negative (FN)** | Actual positive, predicted negative |
| **False Positive (FP)** | Actual negative, predicted positive |
| **Feedforward Network** | Neural network with no cycles (information flows forward only) |
| **Feature** | Input variable (predictor, independent variable) |
| **Feature Scaling** | Normalizing/standardizing features to similar ranges |
| **Forward Propagation** | Computing outputs layer by layer from input to output |

---

## G

| Term | Definition |
|------|------------|
| **Gini Impurity** | $1 - \sum p_i^2$ - measure of node impurity in decision trees |
| **Gradient Descent** | Iterative optimization: $\theta := \theta - \alpha \nabla J(\theta)$ |
| **Generalization** | Model's ability to perform well on unseen data |

---

## H

| Term | Definition |
|------|------------|
| **Hidden Layer** | Neural network layer between input and output |
| **Hierarchical Clustering** | Clustering that builds tree of clusters (agglomerative/divisive) |
| **Hyperparameter** | Parameter set before training (e.g., k in KNN, λ in Ridge) |
| **Hyperplane** | Decision boundary in SVM: $w^T x + b = 0$ |

---

## I

| Term | Definition |
|------|------------|
| **Information Gain** | Reduction in entropy: $IG = H(parent) - \sum \frac{n_{child}}{n_{parent}} H(child)$ |
| **Irreducible Error** | Noise in data that no model can eliminate ($\sigma^2$) |

---

## K

| Term | Definition |
|------|------------|
| **K-Means** | Centroid-based clustering minimizing within-cluster sum of squares |
| **K-Medoids** | Clustering using actual data points as centers (more robust to outliers) |
| **K-Nearest Neighbors (KNN)** | Instance-based classifier using majority vote of k nearest points |
| **Kernel Trick** | Mapping data to higher dimension implicitly via kernel function |
| **Kurtosis** | Measure of tail heaviness of distribution |

---

## L

| Term | Definition |
|------|------------|
| **L1 Regularization (Lasso)** | Adds $\lambda \sum |\beta_j|$ - produces sparse solutions |
| **L2 Regularization (Ridge)** | Adds $\lambda \sum \beta_j^2$ - shrinks coefficients |
| **LDA** | Linear Discriminant Analysis - maximizes between-class / within-class variance |
| **Leave-One-Out CV (LOOCV)** | K-fold CV with k = n (each sample is test set once) |
| **Linear Regression** | Predicts continuous target: $y = \beta_0 + \beta_1 x_1 + ... + \beta_p x_p + \epsilon$ |
| **Logistic Regression** | Classification via sigmoid: $P(y=1|x) = \frac{1}{1+e^{-(\beta_0+\beta^T x)}}$ |
| **Loss Function** | Measures discrepancy between prediction and truth |

---

## M

| Term | Definition |
|------|------------|
| **Manhattan Distance** | $\sum |x_i - y_i|$ - L1 distance |
| **Margin** | Distance from decision boundary to nearest points (SVM) |
| **Maximum Likelihood Estimation (MLE)** | Parameter estimation maximizing likelihood of observed data |
| **Mean Squared Error (MSE)** | $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$ |
| **Memory Trick** | Mnemonic for remembering concepts/formulas |
| **MLP** | Multi-Layer Perceptron - feedforward neural network with hidden layers |
| **Model Selection** | Choosing best model/hyperparameters via validation |

---

## N

| Term | Definition |
|------|------------|
| **Naive Bayes** | Probabilistic classifier assuming feature independence given class |
| **Neural Network** | Composable differentiable functions with learnable parameters |
| **Normalization** | Scaling features to [0,1] range |
| **Number of Features (p)** | Dimensionality of input space |

---

## O

| Term | Definition |
|------|------------|
| **One-Hot Encoding** | Representing categorical variables as binary vectors |
| **Outlier** | Data point significantly different from others |
| **Overfitting** | Low training error, high test error (high variance) |
| **Orthogonal** | Vectors with dot product = 0 (PCA components are orthogonal) |

---

## P

| Term | Definition |
|------|------------|
| **PCA** | Principal Component Analysis - linear dimensionality reduction via eigendecomposition |
| **Precision** | $\frac{TP}{TP+FP}$ - of predicted positives, how many are actually positive |
| **Principal Components** | Eigenvectors of covariance matrix (directions of max variance) |
| **Probability Density Function (PDF)** | Function describing likelihood of continuous random variable |

---

## Q

| Term | Definition |
|------|------------|
| **Quadratic Discriminant Analysis (QDA)** | LDA with class-specific covariance matrices |

---

## R

| Term | Definition |
|------|------------|
| **Random Forest** | Ensemble of decorrelated decision trees (bagging + feature subsampling) |
| **Recall (Sensitivity)** | $\frac{TP}{TP+FN}$ - of actual positives, how many were predicted positive |
| **Regression** | Predicting continuous target values |
| **Regularization** | Adding penalty to loss to prevent overfitting |
| **Residual** | Difference between actual and predicted: $e_i = y_i - \hat{y}_i$ |
| **Ridge Regression** | Linear regression with L2 penalty: $\min ||y-X\beta||^2 + \lambda||\beta||^2$ |

---

## S

| Term | Definition |
|------|------------|
| **Sample** | Single observation/row in dataset (n = number of samples) |
| **Sigmoid** | $\sigma(z) = \frac{1}{1+e^{-z}}$ - maps to (0,1) |
| **Single Linkage** | Hierarchical clustering distance = min distance between points in clusters |
| **Softmax** | $\frac{e^{z_i}}{\sum e^{z_j}}$ - multi-class probability distribution |
| **Standardization** | Scaling features to zero mean, unit variance: $z = \frac{x-\mu}{\sigma}$ |
| **Stochastic Gradient Descent (SGD)** | Gradient descent with batch size = 1 |
| **Support Vectors** | Data points defining SVM margin (non-zero Lagrange multipliers) |
| **SVM** | Support Vector Machine - max-margin classifier |

---

## T

| Term | Definition |
|------|------------|
| **Test Set** | Held-out data for final evaluation |
| **Training Set** | Data used to fit model parameters |
| **True Negative (TN)** | Actual negative, predicted negative |
| **True Positive (TP)** | Actual positive, predicted positive |

---

## U

| Term | Definition |
|------|------------|
| **Underfitting** | High training error, high test error (high bias) |
| **Unsupervised Learning** | Learning patterns from unlabeled data |

---

## V

| Term | Definition |
|------|------------|
| **Variance** | Error from sensitivity to training data: $Var(\hat{f}) = E[(\hat{f} - E[\hat{f}])^2]$ |
| **Validation Set** | Data for hyperparameter tuning/model selection |

---

## W

| Term | Definition |
|------|------------|
| **Weight Decay** | L2 regularization in neural networks |
| **Within-Cluster Sum of Squares (WCSS)** | $\sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2$ - K-Means objective |

---

## X

| Term | Definition |
|------|------------|
| **XOR Problem** | Non-linearly separable problem requiring hidden layer |

---

## Related Notes

- [[Formula Sheet]]
- [[01 Supervised Learning]]
- [[17 Unsupervised Learning]]

---

#machine-learning #gate-da #glossary #revision