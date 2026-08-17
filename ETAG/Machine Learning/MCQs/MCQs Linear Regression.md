Absolutely — here is the **same set**, with every mathematical expression converted to **Obsidian-friendly LaTeX** using `$...$` for inline expressions and `$$...$$` for display expressions.

## Linear Regression — MCQ Set 1

### Q1. [PYQ-based | Least Squares]

Consider the data points

$$  
(-1,2),\quad (2,-4),\quad (3,5)  
$$

A model of the form

$$  
y=wx  
$$

is fitted using ordinary least squares. The optimal value of $w$ is:

**A.** $\frac{11}{14}$

**B.** $\frac{15}{14}$

**C.** $\frac{13}{14}$

**D.** $\frac{17}{14}$

---

### Q2. [GATE-level | Simple Linear Regression]

For a simple linear regression model

$$  
y=\beta_0+\beta_1x+\epsilon  
$$

suppose the sample means are $\bar{x}=4$ and $\bar{y}=10$, and the estimated slope is $\hat{\beta}_1=2.5$.

What is the estimated intercept?

**A.** $0$

**B.** $2.5$

**C.** $5$

**D.** $10$

---

### Q3. [Conceptual | OLS]

In ordinary least squares linear regression, the objective function is

$$  
J(\mathbf{w})=|\mathbf{y}-X\mathbf{w}|_2^2.  
$$

Which statement is **always true** at the optimal solution $\mathbf{w}^*$, assuming the minimum exists?

**A.** $X\mathbf{w}^*=\mathbf{y}$

**B.** $X^T(\mathbf{y}-X\mathbf{w}^*)=0$

**C.** $\mathbf{y}-X\mathbf{w}^*=0$

**D.** $X^TX=I$

---

### Q4. [GATE-level | Multiple Linear Regression]

Consider

$$  
X=  
\begin{bmatrix}  
1&1\  
1&2\  
1&3  
\end{bmatrix},  
\qquad  
y=  
\begin{bmatrix}  
2\  
4\  
6  
\end{bmatrix}.  
$$

The least-squares solution for

$$  
y=\beta_0+\beta_1x  
$$

is:

**A.** $(\beta_0,\beta_1)=(0,2)$

**B.** $(\beta_0,\beta_1)=(1,2)$

**C.** $(\beta_0,\beta_1)=(2,1)$

**D.** $(\beta_0,\beta_1)=(0,3)$

---

### Q5. [NPTEL-level | Transformation]

Suppose the original simple linear regression model is

$$  
y=\beta_0+\beta_1x.  
$$

Now every input value is transformed as

$$  
x'=x+c  
$$

where $c$ is a constant.

Which statement about the fitted regression line is correct?

**A.** Both slope and intercept remain unchanged.
**B.** Slope changes, but intercept remains unchanged.
**C.** Slope remains unchanged, while intercept changes.
**D.** Both slope and intercept necessarily change.

---

### Q6. [GATE-level | Ridge Regression]

Consider ridge regression with objective

# $$  
J(\mathbf{w})

|\mathbf{y}-X\mathbf{w}|_2^2  
+  
\lambda|\mathbf{w}|_2^2,  
\qquad \lambda>0.  
$$

Assume $X^TX$ is invertible. The optimal parameter vector is:

**A.** $(X^TX)^{-1}X^Ty$
**B.** $(X^TX+\lambda I)^{-1}X^Ty$
**C.** $(X^TX-\lambda I)^{-1}X^Ty$$
**D.**$(X^TX)^{-1}(X^Ty+\lambda I)$

---

### Q7. [Conceptual | Ridge Regression]

Which of the following is the primary purpose of ridge regression?

**A.** To eliminate all features having small coefficients

**B.** To reduce overfitting by penalizing large coefficients

**C.** To guarantee zero training error

**D.** To convert a regression problem into a classification problem

---

### Q8. [GATE-level | Residuals]

A linear regression model with an intercept is fitted using ordinary least squares. Let the residuals be

$$  
e_i=y_i-\hat{y}_i.  
$$

Which quantity is necessarily zero?

A. $\sum_i y_i$  
B. $\sum_i \hat{y}_i$  
C. $\sum_i e_i$  
D. $\sum_i e_i^2$

---

### Q9. [GATE-level | $R^2$]

A regression model produces

$$  
SSE=20  
$$

and

$$  
SST=100.  
$$

The coefficient of determination $R^2$ is:

**A.** $0.20$

**B.** $0.50$

**C.** $0.80$

**D.** $1.20$

---

### Q10. [High-level GATE | Design Matrix]

Consider multiple linear regression

$$  
y=X\beta+\epsilon  
$$

where $X$ has dimensions $n\times p$, with $n>p$.

Which condition is sufficient for the ordinary least-squares solution

$$  
\hat{\beta}=(X^TX)^{-1}X^Ty  
$$

to be uniquely defined?

**A.** $X$ must have $n$ linearly independent columns.

**B.** $X$ must have $p$ linearly independent columns.

**C.** $X$ must have $n$ linearly independent rows.

**D.** $X^TX$ must be a $p\times n$ matrix.

---

# Answers + One-line Explanations

**Q1 → A. $\frac{11}{14}$**

For regression through the origin,

# $\hat{w} = \frac{\sum x_i y_i}{\sum x_i^2} = \frac{11}{14}$

---

**Q2 → A. $0$**

Using $\hat{\beta}_0\bar{y}-\hat{\beta}_1\bar{x},$

we get

$$  
10-(2.5)(4)=0.  
$$

---

**Q3 → B. $X^T(\mathbf{y}-X\mathbf{w}^*)=0$**

The OLS gradient condition gives

$$  
X^T(\mathbf{y}-X\mathbf{w}^*)=0,  
$$

meaning the residual vector is orthogonal to the column space of $X$.

---

**Q4 → A. $(0,2)$**

The points lie exactly on

$$  
y=2x,  
$$

so the least-squares fit has zero residual error with intercept $0$ and slope $2$.

---

**Q5 → C. Slope remains unchanged, while intercept changes.**

Shifting $x$ horizontally changes the intercept but does not change the slope.

---

**Q6 → B. $(X^TX+\lambda I)^{-1}X^Ty$**

Ridge modifies the normal equations by adding the regularization term $\lambda I$:

$$  
(X^TX+\lambda I)\mathbf{w}=X^Ty.  
$$

Therefore,

# $$  
\hat{\mathbf{w}}

(X^TX+\lambda I)^{-1}X^Ty.  
$$

---

**Q7 → B. To reduce overfitting by penalizing large coefficients**

Ridge shrinks coefficients toward zero through an $L_2$ penalty but generally does not make them exactly zero.

The objective contains

$$  
\lambda|\mathbf{w}|_2^2.  
$$

---

**Q8 → C. $\sum_i e_i=0$**

OLS with an intercept always has residuals summing to zero:

$$  
\sum_i e_i=0.  
$$

---

**Q9 → C. $0.80$**

# $$  
R^2

1-\frac{SSE}{SST}  
$$

Therefore,

# $$  
R^2=
1-\frac{20}{100}=
0.8.  
$$

---

**Q10 → B. $X$ must have $p$ linearly independent columns.**

$X^TX$ is invertible exactly when the columns of $X$ are linearly independent, i.e. $X$ has full column rank:

$$  
\operatorname{rank}(X)=p.  
$$

The question mix here reflects the actual GATE DA emphasis: regression questions can require direct computation as well as linear-algebra reasoning rather than merely recalling definitions. The 2025 paper's regression question is a good example of this.

**Next set will be harder:** more numerical questions involving normal equations, covariance/variance, multiple regression, ridge, feature scaling, and gradient descent.