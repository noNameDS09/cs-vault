
### 1. Bias-Variance Tradeoff

A model has very low training error but significantly higher test error. Which of the following is the most likely explanation?

A. High bias and low variance  
B. Low bias and high variance  
C. High bias and high variance  
D. Low bias and low variance

---

### 2. Gradient Descent

For a differentiable convex loss function, batch gradient descent converges to the global minimum if:

A. The learning rate is exactly 1.  
B. The learning rate is sufficiently small.  
C. The number of features is less than the number of samples.  
D. The initial weights are all zeros.

---

### 3. Linear Regression

Suppose (X^TX) is singular. Which of the following can still produce a unique solution?

A. Ordinary Least Squares  
B. Ridge Regression  
C. Principal Component Analysis  
D. Gradient Descent with zero initialization

---

### 4. Logistic Regression

The decision boundary learned by logistic regression is:

A. Always nonlinear  
B. Always quadratic  
C. Linear in the feature space used for training  
D. Independent of the feature values

---

### 5. Regularization

L1 regularization primarily encourages:

A. Larger weights  
B. Sparse models  
C. Higher variance  
D. Increased training accuracy

---

### 6. Support Vector Machines

In a hard-margin SVM, the optimization objective minimizes:

A. Training error only  
B. Margin width  
C. Norm of the weight vector while correctly classifying all samples  
D. Number of support vectors

---

### 7. Kernel Methods

Which of the following is a valid requirement for a kernel function?

A. It must always be linear.  
B. It must satisfy Mercer's condition.  
C. It must have positive outputs only.  
D. It must be differentiable everywhere.

---

### 8. Decision Trees

Information Gain is based on:

A. Mean Squared Error  
B. Euclidean Distance  
C. Entropy Reduction  
D. Variance Inflation

---

### 9. Random Forest

Compared to a single decision tree, a Random Forest primarily reduces:

A. Bias only  
B. Variance only  
C. Training time only  
D. Feature dimensionality

---

### 10. Naive Bayes

The "naive" assumption in Naive Bayes is that:

A. Features are normally distributed.  
B. Features are conditionally independent given the class label.  
C. Class priors are equal.  
D. Features are mutually exclusive.

---

### 11. K-Means Clustering

K-Means is guaranteed to:

A. Find the globally optimal clustering.  
B. Converge in a finite number of iterations.  
C. Produce balanced clusters.  
D. Work correctly for categorical features without modification.

---

### 12. Principal Component Analysis

The first principal component corresponds to the direction:

A. Of minimum variance  
B. Maximizing projected variance  
C. Maximizing reconstruction error  
D. Orthogonal to all data points

---

### 13. Neural Networks

Which activation function is most susceptible to the vanishing gradient problem?

A. ReLU  
B. Leaky ReLU  
C. Sigmoid  
D. ELU

---

### 14. Backpropagation

Backpropagation computes gradients efficiently using:

A. Bayes' theorem  
B. Chain Rule of Calculus  
C. Singular Value Decomposition  
D. Dynamic Programming

---

### 15. Cross Validation

In k-fold cross-validation, each sample appears in the validation set:

A. Once  
B. Twice  
C. k times  
D. Never

---

### 16. Evaluation Metrics

For a highly imbalanced binary classification problem, which metric is generally more informative than accuracy?

A. Mean Absolute Error  
B. F1-score  
C. Mean Squared Error  
D. R² Score

---

### 17. Maximum Likelihood Estimation

Maximum Likelihood Estimation chooses parameters that:

A. Maximize posterior probability  
B. Maximize the likelihood of observed data  
C. Minimize model complexity only  
D. Maximize prior probability

---

### 18. Expectation-Maximization (EM)

The EM algorithm alternates between:

A. Feature Selection and Classification  
B. Gradient Descent and Regularization  
C. Expectation and Maximization steps  
D. Training and Validation

---

### 19. Reinforcement Learning

The discount factor (\gamma) in reinforcement learning primarily controls:

A. Exploration rate  
B. Learning rate  
C. Importance of future rewards  
D. Number of actions

---

### 20. Curse of Dimensionality

As the dimensionality of the feature space increases, which statement is generally true?

A. Distance-based methods become more effective.  
B. Data becomes denser.  
C. The volume of the space increases rapidly, requiring more data.  
D. PCA always increases classification accuracy.




# **ANSWERS**

---

# Q1. Bias-Variance Tradeoff

**Answer:** **B. Low bias and high variance**

### Explanation

A model with **very low training error** but **high test error** is **overfitting**.

- Low Bias → Fits training data well.
- High Variance → Poor generalization on unseen data.

> [!tip]
> **Overfitting = Low Bias + High Variance**

---

# Q2. Gradient Descent

**Answer:** **B. The learning rate is sufficiently small.**

### Explanation

For a differentiable convex loss function, Gradient Descent converges to the global minimum when the learning rate $\eta$ is sufficiently small.

A very large learning rate may overshoot the minimum and diverge.

---

# Q3. Linear Regression

**Answer:** **B. Ridge Regression**

### Explanation

Ordinary Least Squares (OLS) computes

$$
\mathbf{w}=(X^TX)^{-1}X^Ty
$$

If $X^TX$ is singular, the inverse does not exist.

Ridge Regression modifies the equation to

$$
\mathbf{w}=(X^TX+\lambda I)^{-1}X^Ty
$$

where $\lambda>0$.

Since $X^TX+\lambda I$ is positive definite, it is always invertible.

> [!important]
> Ridge Regression always provides a unique solution.

---

# Q4. Logistic Regression

**Answer:** **C. Linear in the feature space used for training**

### Explanation

The decision boundary is

$$
w^Tx+b=0
$$

Hence Logistic Regression always learns a **linear decision boundary** in the feature space.

Adding polynomial features makes the boundary nonlinear only in the original input space.

---

# Q5. Regularization

**Answer:** **B. Sparse models**

### Explanation

L1 Regularization minimizes

$$
J(w)=L(w)+\lambda\sum_{i=1}^{n}|w_i|
$$

It forces many coefficients to become exactly zero.

| Regularization | Effect |
|---------------|--------|
| L1 | Sparse model (Feature Selection) |
| L2 | Shrinks weights |

> [!tip]
> **L1 → Sparse**
>
> **L2 → Small weights**

---

# Q6. Support Vector Machines

**Answer:** **C. Norm of the weight vector while correctly classifying all samples**

### Explanation

The hard-margin SVM optimization problem is

$$
\min \frac{1}{2}\|w\|^2
$$

Subject to

$$
y_i(w^Tx_i+b)\ge1
$$

Minimizing $\|w\|$ maximizes the margin.

> [!important]
> SVM = Maximum Margin Classifier

---

# Q7. Kernel Methods

**Answer:** **B. It must satisfy Mercer's condition.**

### Explanation

A valid kernel must correspond to an inner product in some higher-dimensional feature space.

Mercer's theorem states that the kernel matrix

$$
K_{ij}=K(x_i,x_j)
$$

must be **Positive Semi-Definite (PSD).**

Examples:

- Linear Kernel
- Polynomial Kernel
- Gaussian (RBF) Kernel

---

# Q8. Decision Trees

**Answer:** **C. Entropy Reduction**

### Explanation

Entropy is

$$
H(S)=-\sum_i p_i\log_2p_i
$$

Information Gain is

$$
IG=H(S)-\sum_i\frac{|S_i|}{|S|}H(S_i)
$$

The split with the highest Information Gain is selected.

---

# Q9. Random Forest

**Answer:** **B. Variance only**

### Explanation

Random Forest averages predictions from many Decision Trees.

This averaging reduces variance while keeping bias approximately unchanged.

> [!tip]
> Bagging reduces variance.

---

# Q10. Naive Bayes

**Answer:** **B. Features are conditionally independent given the class label.**

### Explanation

Naive Bayes assumes

$$
P(x_1,x_2,\ldots,x_n|y)
=
\prod_{i=1}^{n}P(x_i|y)
$$

Although this assumption is rarely true exactly, Naive Bayes performs surprisingly well.

---

# Q11. K-Means Clustering

**Answer:** **B. Converge in a finite number of iterations.**

### Explanation

The K-Means objective is

$$
J=\sum_{i=1}^{k}\sum_{x\in C_i}\|x-\mu_i\|^2
$$

Each iteration decreases (or leaves unchanged) the objective function.

Since only finitely many cluster assignments exist, convergence is guaranteed.

> [!warning]
> K-Means converges to a **local optimum**, not necessarily the global optimum.

---

# Q12. Principal Component Analysis (PCA)

**Answer:** **B. Maximizing projected variance**

### Explanation

The covariance matrix is

$$
\Sigma=\frac{1}{n-1}X^TX
$$

The first principal component is the eigenvector corresponding to the largest eigenvalue.

It captures the maximum variance in the data.

---

# Q13. Neural Networks

**Answer:** **C. Sigmoid**

### Explanation

Sigmoid activation is

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Its derivative is

$$
\sigma'(x)=\sigma(x)(1-\sigma(x))
$$

For large positive or negative values,

$$
\sigma'(x)\approx0
$$

This causes the **Vanishing Gradient Problem**.

---

# Q14. Backpropagation

**Answer:** **B. Chain Rule of Calculus**

### Explanation

Backpropagation computes gradients using the Chain Rule.

For example,

$$
\frac{\partial L}{\partial w}
=
\frac{\partial L}{\partial a}
\cdot
\frac{\partial a}{\partial z}
\cdot
\frac{\partial z}{\partial w}
$$

This allows efficient training of deep neural networks.

---

# Q15. Cross Validation

**Answer:** **A. Once**

### Explanation

In **k-fold Cross Validation**

- Dataset is divided into $k$ folds.
- Each fold is used once for validation.
- Remaining $k-1$ folds are used for training.

Thus every sample appears exactly once in the validation set.

---

# Q16. Evaluation Metrics

**Answer:** **B. F1-score**

### Explanation

Accuracy is

$$
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
$$

For imbalanced datasets, accuracy can be misleading.

F1-score is

$$
F1=\frac{2PR}{P+R}
$$

where

$$
P=\frac{TP}{TP+FP}
$$

and

$$
R=\frac{TP}{TP+FN}
$$

F1 balances Precision and Recall.

---

# Q17. Maximum Likelihood Estimation (MLE)

**Answer:** **B. Maximize the likelihood of observed data**

### Explanation

MLE estimates parameters as

$$
\hat{\theta}
=
\arg\max_{\theta}P(D|\theta)
$$

where

- $D$ = observed data
- $\theta$ = model parameters

Unlike MAP estimation, MLE does not use prior probabilities.

---

# Q18. Expectation-Maximization (EM)

**Answer:** **C. Expectation and Maximization steps**

### Explanation

The EM algorithm alternates between

### E-Step

Estimate the expected values of hidden variables.

### M-Step

Update parameters by maximizing the expected log-likelihood.

Common applications:

- Gaussian Mixture Models (GMM)
- Hidden Markov Models (HMM)

---

# Q19. Reinforcement Learning

**Answer:** **C. Importance of future rewards**

### Explanation

The return is

$$
G_t
=
R_{t+1}
+
\gamma R_{t+2}
+
\gamma^2R_{t+3}
+\cdots
$$

where

- $\gamma=0$ → Only immediate rewards matter.
- $\gamma\approx1$ → Future rewards become important.

---

# Q20. Curse of Dimensionality

**Answer:** **C. The volume of the space increases rapidly, requiring more data.**

### Explanation

As dimensionality increases,

- Data becomes sparse.
- Distances become less meaningful.
- More training samples are required.

This phenomenon is known as the **Curse of Dimensionality**.

> [!important]
> Distance-based algorithms like **KNN** become less effective in very high-dimensional spaces.

---

# Quick Revision Table

| Topic               | Key Formula / Idea                     |
| ------------------- | -------------------------------------- |
| Linear Regression   | $\mathbf{w}=(X^TX)^{-1}X^Ty$           |
| Ridge Regression    | $\mathbf{w}=(X^TX+\lambda I)^{-1}X^Ty$ |
| Logistic Regression | $w^Tx+b=0$                             |
| Entropy             | $H=-\sum p\log_2p$                     |
| Information Gain    | $IG=H(S)-H(\text{children})$           |
| Sigmoid             | $\sigma(x)=\frac{1}{1+e^{-x}}$         |
| F1 Score            | $\frac{2PR}{P+R}$                      |
| Return (RL)         | $G_t=\sum\gamma^kR_{t+k+1}$            |
| MLE                 | $\hat{\theta}=\arg\max P(D\theta)$     |
| K-Means Objective   | $\sum\|x-\mu\|^2$                      |

> [!success]
> These notes are fully compatible with **Obsidian**, **MathJax**, and PDF export.

