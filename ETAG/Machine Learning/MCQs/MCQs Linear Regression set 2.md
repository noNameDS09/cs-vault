

### Q1. Simple Linear Regression

Consider the simple linear regression model

$$  
y_i=\beta_0+\beta_1x_i+\epsilon_i,\qquad i=1,\dots,n  
$$

where

$$  
S_{xx}=\sum_{i=1}^{n}(x_i-\bar{x})^2.  
$$

The ordinary least-squares estimate of $\beta_1$ is:

**A.**

$$  
\frac{\sum x_i y_i}{\sum x_i^2}  
$$

**B.**

$$  
\frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sum (x_i-\bar{x})^2}  
$$

**C.**

$$  
\frac{\sum (x_i-\bar{x})y_i}{\sum x_i^2}  
$$

**D.**

$$  
\frac{\sum x_i(y_i-\bar{y})}{\sum (x_i-\bar{x})}  
$$

---

### Q2. OLS Estimator and Normal Equations

In a linear regression model $y=X\beta+\epsilon$, suppose $X$ has full column rank. The ordinary least-squares estimator is

$$  
\hat{\beta}=(X^TX)^{-1}X^Ty.  
$$

Which one of the following statements is **always true**?

**A.** $\hat{\beta}$ is always equal to the true $\beta$.

**B.** $X\hat{\beta}=y$ for every $y$.

**C.** The residual vector $e=y-X\hat{\beta}$ is orthogonal to every column of $X$.

**D.** The residual vector always equals zero.

---

### Q3. Residuals with an Intercept

Consider a linear regression model with an intercept. After fitting by ordinary least squares, which quantity is necessarily zero?

**A.**

$$  
\sum_{i=1}^{n}x_i e_i  
$$

**B.**

$$  
\sum_{i=1}^{n}e_i  
$$

**C.** Both A and B

**D.** Neither A nor B

---

### Q4. Hat Matrix

Suppose the feature matrix is $X\in\mathbb{R}^{n\times p}$, and $X^TX$ is invertible. The matrix

$$  
H=X(X^TX)^{-1}X^T  
$$

used in ordinary least squares is called the **hat matrix**. Which statement about $H$ is correct?

**A.** $H^2=0$

**B.** $H^2=H$

**C.** $H^{-1}=H$

**D.** $H$ is necessarily diagonal

---

### Q5. Ridge Regression

In a linear regression problem, consider the ridge objective

$$  
J(\beta)=\lVert y-X\beta\rVert_2^2+\lambda\lVert\beta\rVert_2^2,  
\qquad \lambda>0.  
$$

The corresponding closed-form solution is:

**A.**

$$  
(X^TX)^{-1}X^Ty  
$$

**B.**

$$  
(X^TX+\lambda I)^{-1}X^Ty  
$$

**C.**

$$  
(X^TX-\lambda I)^{-1}X^Ty  
$$

**D.**

$$  
(X^TX)^{-1}(X^Ty+\lambda I)  
$$

---

### Q6. Prediction

Let the fitted simple linear regression line be

$$  
\hat{y}=2+3x.  
$$

For an observed value $x=4$, the predicted value of $y$ is:

**A.** 8

**B.** 10

**C.** 12

**D.** 14

---

### Q7. Gauss–Markov Theorem

Consider ordinary least squares under the classical model assumptions:

$$  
y=X\beta+\epsilon,  
$$

$$  
E[\epsilon\mid X]=0,  
$$

$$  
\operatorname{Var}(\epsilon\mid X)=\sigma^2I.  
$$

Which statement about $\hat{\beta}$ is correct?

**A.** $\hat{\beta}$ is biased but has minimum variance.

**B.** $\hat{\beta}$ is unbiased and is the best linear unbiased estimator.

**C.** $\hat{\beta}$ is always equal to $\beta$.

**D.** $\hat{\beta}$ is unbiased only when $X$ is diagonal.

---

### Q8. Perfect Multicollinearity

Two features $x_1$ and $x_2$ are perfectly linearly dependent, i.e.

$$  
x_2=5x_1.  
$$

For a linear regression model containing both $x_1$ and $x_2$ as predictors, which statement is correct?

**A.** The OLS coefficient estimates are uniquely determined.

**B.** $X^TX$ is guaranteed to be diagonal.

**C.** $X^TX$ is singular.

**D.** The residual sum of squares must be zero.

---

### Q9. Direct OLS Calculation

Suppose the data consist of the points

$$  
(1,2),\quad (2,4),\quad (3,6).  
$$

The ordinary least-squares line with an intercept is

$$  
\hat{y}=\hat{\beta}_0+\hat{\beta}_1x.  
$$

What are $\hat{\beta}_0$ and $\hat{\beta}_1$?

**A.** $\hat{\beta}_0=0,\ \hat{\beta}_1=2$

**B.** $\hat{\beta}_0=1,\ \hat{\beta}_1=2$

**C.** $\hat{\beta}_0=0,\ \hat{\beta}_1=1$

**D.** $\hat{\beta}_0=2,\ \hat{\beta}_1=1$

---

### Q10. Sum of Fitted Values

In ordinary least squares, if the model includes an intercept and the fitted values are $\hat{y}_i$, which identity is necessarily satisfied?

**A.**

$$  
\sum_{i=1}^{n}y_i=\sum_{i=1}^{n}\hat{y}_i  
$$

**B.**

$$  
\sum_{i=1}^{n}y_i^2=\sum_{i=1}^{n}\hat{y}_i^2  
$$

**C.**

$$  
\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=0  
$$

**D.**

$$  
\hat{y}_i=y_i\quad\text{for every }i  
$$

---

# Answer Table

|Q. No.|Correct Answer|Key Reason|
|--:|:-:|---|
|1|**B**|OLS slope is $\displaystyle \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}$|
|2|**C**|Normal equations give $X^Te=0$, so residuals are orthogonal to the columns of $X$|
|3|**C**|With an intercept, $e\perp\mathbf{1}$; also $e\perp X$|
|4|**B**|The hat matrix is an orthogonal projection, hence $H^2=H$|
|5|**B**|Ridge solution is $(X^TX+\lambda I)^{-1}X^Ty$|
|6|**D**|$2+3(4)=14$|
|7|**B**|By the Gauss–Markov theorem, OLS is BLUE under the stated assumptions|
|8|**C**|Perfect linear dependence makes $X$ rank-deficient, hence $X^TX$ is singular|
|9|**A**|All points lie exactly on $y=2x$, so intercept $=0$ and slope $=2$|
|10|**A**|With an intercept, residuals sum to zero, so $\sum y_i=\sum\hat{y}_i$|

---
---
### Q1. Zero OLS Slope

In simple linear regression with an intercept, the estimated slope is zero. Which statement must be true?

**A.** $x$ and $y$ are independent.

**B.** The sample covariance between $x$ and $y$ is zero.

**C.** The sample variance of $y$ is zero.

**D.** Every residual is zero.

---

### Q2. OLS Normal Equation

Consider the OLS problem

$$  
\min_{\beta}\lVert y-X\beta\rVert_2^2.  
$$

At the optimum, which equation must hold?

**A.**

$$  
X(y-X\hat{\beta})=0  
$$

**B.**

$$  
X^T(y-X\hat{\beta})=0  
$$

**C.**

$$  
y-X\hat{\beta}=0  
$$

**D.**

$$  
X^TX\hat{\beta}=0  
$$

---

### Q3. Square Full-Rank Design Matrix

Suppose $X$ is an $n\times p$ matrix with full column rank. If $n=p$, then:

**A.** The OLS fitted values equal $y$ exactly.

**B.** The residuals must be zero.

**C.** Both A and B

**D.** Neither A nor B

---

### Q4. Coefficient of Determination

In a regression model with an intercept, let $R^2$ denote the coefficient of determination. Which statement is correct?

**A.** $R^2$ can never be negative for ordinary least squares with an intercept.

**B.** $R^2$ is always equal to the correlation coefficient.

**C.** $R^2$ must be less than $0$.

**D.** $R^2$ is independent of the fitted values.

---

### Q5. OLS Without an Intercept

Consider the one-feature model

$$  
y_i=\beta x_i+\epsilon_i  
$$

with **no intercept**, and suppose

$$  
x=  
\begin{bmatrix}  
1\  
2  
\end{bmatrix},  
\qquad  
y=  
\begin{bmatrix}  
3\  
5  
\end{bmatrix}.  
$$

What is the OLS estimate of $\beta$?

**A.** $2$

**B.** $\frac{13}{5}$

**C.** $\frac{13}{3}$

**D.** $\frac{5}{2}$

---

### Q6. Unbiasedness of OLS

Suppose the OLS estimator is

$$  
\hat{\beta}=(X^TX)^{-1}X^Ty.  
$$

Under the model

$$  
y=X\beta+\epsilon  
$$

with

$$  
E[\epsilon\mid X]=0,  
$$

which is correct?

**A.**

$$  
E[\hat{\beta}\mid X]=0  
$$

**B.**

$$  
E[\hat{\beta}\mid X]=X\beta  
$$

**C.**

$$  
E[\hat{\beta}\mid X]=\beta  
$$

**D.**

$$  
E[\hat{\beta}\mid X]=(X^TX)^{-1}  
$$

---

### Q7. Ridge Regression Shrinkage

In ridge regression, as $\lambda$ increases from $0$ toward a very large value, the magnitude of the regression coefficients generally:

**A.** Increases without bound.

**B.** Decreases toward zero.

**C.** Remains exactly unchanged.

**D.** Becomes equal to the OLS coefficients.

---

### Q8. Eigenvalues of the Hat Matrix

Let

$$  
H=X(X^TX)^{-1}X^T.  
$$

Which eigenvalues can the hat matrix $H$ have?

**A.** Only $-1$ and $1$

**B.** Only $0$ and $1$

**C.** Any real number

**D.** Only positive values strictly less than $1$

---

### Q9. Influential Observation

Consider the points

$$  
(1,1),\quad (2,2),\quad (3,10).  
$$

Which observation is most likely to have a large influence on the fitted regression line?

**A.** $(1,1)$

**B.** $(2,2)$

**C.** $(3,10)$

**D.** All observations have identical influence

---

### Q10. Calculating $R^2$

In simple linear regression with an intercept, suppose the total sum of squares is

$$  
SST=100  
$$

and the residual sum of squares is

$$  
SSE=20.  
$$

What is $R^2$?

**A.** $0.20$

**B.** $0.40$

**C.** $0.80$

**D.** $5$

---

# Answer Table

|Q. No.|Correct Answer|Verification / Reason|
|--:|:-:|---|
|1|**B**|OLS slope $\displaystyle =\frac{S_{xy}}{S_{xx}}$; zero slope implies $S_{xy}=0$ when $S_{xx}>0$|
|2|**B**|Differentiating the objective gives the normal equation $X^T(y-X\hat{\beta})=0$|
|3|**C**|A square full-rank $X$ is invertible, so $X\hat{\beta}=y$ and residuals are zero|
|4|**A**|With an intercept, $\displaystyle R^2=1-\frac{SSE}{SST}$, so $0\leq R^2\leq1$|
|5|**B**|$\displaystyle \hat{\beta}=\frac{x^Ty}{x^Tx}=\frac{1(3)+2(5)}{1^2+2^2}=\frac{13}{5}$|
|6|**C**|$\displaystyle E[\hat{\beta}\mid X]=(X^TX)^{-1}X^TE[y\mid X]=\beta$|
|7|**B**|Ridge penalizes coefficient magnitude; increasing $\lambda$ shrinks coefficients toward zero|
|8|**B**|$H$ is symmetric and idempotent, so its eigenvalues satisfy $\lambda^2=\lambda$, giving $0$ or $1$|
|9|**C**|The point has a comparatively large $x$-value and a large deviation in $y$, making it influential|
|10|**C**|$\displaystyle R^2=1-\frac{SSE}{SST}=1-\frac{20}{100}=0.8$|

---
---

### Q1. Unbiased Estimator of $\sigma^2$

Consider the linear regression model

$$  
y=X\beta+\epsilon  
$$

with

$$  
E[\epsilon\mid X]=0.  
$$

Let

$$  
\hat{\beta}=(X^TX)^{-1}X^Ty.  
$$

Which quantity is an unbiased estimator of $\sigma^2$, assuming the usual homoscedastic-noise model and $\operatorname{rank}(X)=p$?

**A.**

$$  
\frac{\lVert y-X\hat{\beta}\rVert_2^2}{n}  
$$

**B.**

$$  
\frac{\lVert y-X\hat{\beta}\rVert_2^2}{n-p}  
$$

**C.**

$$  
\frac{\lVert y-X\hat{\beta}\rVert_2^2}{p}  
$$

**D.**

$$  
\frac{\lVert y-X\hat{\beta}\rVert_2^2}{n-1}  
$$

---

### Q2. Intercept with Centered Predictors

Suppose the columns of $X$ are centered, so that each predictor has mean zero, and the regression model contains an intercept. Which is true about the OLS estimate of the intercept?

**A.**

$$  
\hat{\beta}_0=0  
$$

**B.**

$$  
\hat{\beta}_0=\bar{y}  
$$

**C.**

$$  
\hat{\beta}_0=\bar{x}  
$$

**D.** It cannot be determined without knowing $X^TX$.

---

### Q3. Transformation of a Predictor

Consider the transformation of a predictor

$$  
z=ax+b,\qquad a\neq0.  
$$

In a simple linear regression model with an intercept, which quantity remains unchanged?

**A.** The estimated slope coefficient

**B.** The estimated intercept coefficient

**C.** The fitted values

**D.** The numerical value of the predictor

---

### Q4. Multicollinearity

In multiple linear regression, suppose two predictors are highly correlated but not perfectly correlated. Which consequence is most likely?

**A.** OLS becomes impossible to compute.

**B.** The coefficient estimates can have high variance.

**C.** The residuals must be zero.

**D.** $R^2$ must become zero.

---

### Q5. Regression Through the Origin

Let

$$  
X=  
\begin{bmatrix}  
1\  
2\  
3  
\end{bmatrix},  
\qquad  
y=  
\begin{bmatrix}  
2\  
4\  
6  
\end{bmatrix}  
$$

for a regression **through the origin**:

$$  
y=\beta x+\epsilon.  
$$

The OLS estimate of $\beta$ is:

**A.** $1$

**B.** $2$

**C.** $3$

**D.** $4$

---

### Q6. OLS Residual Properties

In ordinary least squares with an intercept, the residual vector is

$$  
e=y-\hat{y}.  
$$

Which statement is **not necessarily true**?

**A.**

$$  
\sum_i e_i=0  
$$

**B.**

$$  
e^TX=0  
$$

**C.**

$$  
e^T\hat{y}=0  
$$

**D.**

$$  
\lVert e\rVert_2=0  
$$

---

### Q7. Shifting the Response Variable

Suppose

$$  
\hat{y}=5+2x  
$$

is the fitted regression line. If every observed $y_i$ is increased by $10$ while all $x_i$ remain unchanged, the new fitted line is:

**A.**

$$  
\hat{y}=5+2x  
$$

**B.**

$$  
\hat{y}=15+2x  
$$

**C.**

$$  
\hat{y}=5+12x  
$$

**D.**

$$  
\hat{y}=15+12x  
$$

---

### Q8. Perfect Fit and $R^2$

Consider ordinary least squares with an intercept. If $R^2=1$, which statement must be true?

**A.** Every predictor has zero variance.

**B.** The residual sum of squares is zero.

**C.** The coefficient estimates are all zero.

**D.** The total sum of squares is zero.

---

### Q9. Ridge Regression as $\lambda\to0^+$

In ridge regression,

# $$  
\hat{\beta}_{\lambda}

(X^TX+\lambda I)^{-1}X^Ty.  
$$

Assume $X^TX$ is invertible. What happens as $\lambda\to0^+$?

**A.** $\hat{\beta}_{\lambda}\to0$

**B.** $\hat{\beta}_{\lambda}$ approaches the OLS estimator

**C.** $\hat{\beta}_{\lambda}$ approaches $X^Ty$

**D.** $\hat{\beta}_{\lambda}$ becomes undefined

---

### Q10. Direct OLS Slope Calculation

Three observations are given by

$$  
(1,2),\quad(2,3),\quad(4,7).  
$$

For simple linear regression with an intercept, what is the OLS slope?

**A.** $\frac{3}{2}$

**B.** $\frac{5}{3}$

**C.** $\frac{17}{14}$

**D.** $2$

---

# Answer Table

|Q. No.|Correct Answer|Cross-check|
|--:|:-:|---|
|1|**B**|$E[SSE]=(n-p)\sigma^2$, so $\displaystyle \frac{SSE}{n-p}$ is unbiased|
|2|**B**|With centered predictors, $\displaystyle \hat{\beta}_0=\bar{y}-\sum_j\hat{\beta}_j\bar{x}_j=\bar{y}$|
|3|**C**|Rescaling/recentering $x$ changes coefficients but represents the same fitted line|
|4|**B**|Near multicollinearity makes $X^TX$ ill-conditioned, increasing coefficient variance|
|5|**B**|$\displaystyle \hat{\beta}=\frac{x^Ty}{x^Tx}=\frac{2+8+18}{1+4+9}=2$|
|6|**D**|OLS residuals need not be zero unless the model fits perfectly|
|7|**B**|Adding $10$ to every response shifts fitted values and the intercept by $10$; slope is unchanged|
|8|**B**|$\displaystyle R^2=1-\frac{SSE}{SST}=1\Rightarrow SSE=0$, provided $SST>0$|
|9|**B**|$\displaystyle (X^TX+\lambda I)^{-1}X^Ty\to(X^TX)^{-1}X^Ty$ as $\lambda\to0^+$|
|10|**C**|$\displaystyle \bar{x}=\frac73,\ \bar{y}=4,\ S_{xy}=\frac{17}{3},\ S_{xx}=\frac{14}{3}$, hence slope $\displaystyle =\frac{17}{14}$|

---
---
 