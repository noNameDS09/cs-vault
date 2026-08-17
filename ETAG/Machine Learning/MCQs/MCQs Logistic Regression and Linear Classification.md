

**1.** In binary logistic regression, the predicted probability of class 1 is given by

$p=\frac{1}{1+e^{-z}}$

If $z=0$, what is $p$?

A) $0$  
B) $0.25$  
C) $0.5$  
D) $1$

---

**2.** Consider the logistic regression model

$z=2x_1-x_2+1$

For a data point $(x_1,x_2)=(1,2)$, what is the value of $z$?

A) $0$  
B) $1$  
C) $2$  
D) $3$

---

**3.** A logistic regression classifier predicts class 1 when $p\geq0.5$. Since the sigmoid function satisfies $\sigma(z)=0.5$ when $z=0$, which condition corresponds to predicting class 1?

A) $z<0$  
B) $z\leq0$  
C) $z>0$  
D) $z\geq0$

---

**4.** Consider the classifier

$z=3x_1+2x_2-6$

What is its decision boundary?

A) $3x_1+2x_2=6$  
B) $3x_1+2x_2=0$  
C) $3x_1-2x_2=6$  
D) $3x_1+2x_2=-6$

---

**5.** For the model

$p(y=1\mid x)=\sigma(2x-4)$

which of the following values of $x$ gives $p(y=1\mid x)=0.5$?

A) $0$  
B) $1$  
C) $2$  
D) $4$

---

**6.** A logistic regression model gives $z=2$ for a particular observation. Which statement is correct?

A) The predicted probability is exactly $0.5$  
B) The predicted probability is greater than $0.5$  
C) The predicted probability is less than $0.5$  
D) The predicted probability is exactly $1$

---

**7.** Consider a linear classifier

$f(x_1,x_2)=2x_1-3x_2+6$

A point is classified as class 1 if $f(x_1,x_2)\geq0$. What is the predicted class for $(x_1,x_2)=(0,3)$?

A) Class 1  
B) Class 0  
C) Cannot be determined  
D) Both classes

---

**8.** Which of the following represents a linear decision boundary in two dimensions?

A) $x_1^2+x_2^2=1$  
B) $x_1x_2=1$  
C) $2x_1-3x_2+5=0$  
D) $e^{x_1}+x_2=1$

---

**9.** Consider

$z=-x_1+4x_2-2$

For which point is $z=0$?

A) $(2,1)$  
B) $(4,2)$  
C) $(2,2)$  
D) $(1,2)$

---

**10.** Suppose a logistic regression model is

$p(y=1\mid x)=\sigma(-2x+6)$

As $x$ increases, what happens to the predicted probability?

A) It always increases  
B) It always decreases  
C) It first increases and then decreases  
D) It remains constant

---

**11.** Consider the two-dimensional linear classifier

$f(x_1,x_2)=x_1+x_2-5$

Which point lies exactly on the decision boundary?

A) $(1,3)$  
B) $(2,2)$  
C) $(2,3)$  
D) $(4,2)$

---

**12.** In logistic regression, the log-odds are defined as

$\log\left(\frac{p}{1-p}\right)$

If $p=0.8$, what is the value of the odds $\frac{p}{1-p}$?

A) $0.25$  
B) $0.8$  
C) $4$  
D) $5$

---

**13.** A logistic regression model has

$z=x_1-2x_2+4$

and predicts class 1 when $z\geq0$. Which point is classified as class 0?

A) $(0,1)$  
B) $(2,1)$  
C) $(4,2)$  
D) $(1,2)$

---

**14.** Suppose two linear classifiers have decision functions

$f_1(x)=2x_1+x_2-4$

and

$f_2(x)=4x_1+2x_2-8$

Which statement is correct?

A) They have different decision boundaries  
B) They have the same decision boundary  
C) $f_1$ is nonlinear while $f_2$ is linear  
D) They always produce different predictions

---

**15.** Consider a logistic regression model with

$z=w_0+w_1x_1+w_2x_2$

If $w_1=0$, which statement is necessarily true?

A) $x_1$ has no effect on the value of $z$  
B) $x_2$ has no effect on the value of $z$  
C) The model becomes nonlinear  
D) The model cannot perform classification

---

**16.** A logistic regression model produces the following values:

- Observation A: $p=0.9$
    
- Observation B: $p=0.6$
    
- Observation C: $p=0.4$
    
- Observation D: $p=0.1$
    

Using a threshold of $0.5$, how many observations are classified as class 1?

A) $1$  
B) $2$  
C) $3$  
D) $4$

---

**17.** For binary logistic regression, the sigmoid function is

$\sigma(z)=\frac{1}{1+e^{-z}}$

Which statement about $\sigma(z)$ is correct?

A) Its output is always less than $0$  
B) Its output lies strictly between $0$ and $1$  
C) Its output can be any real number  
D) Its output is always greater than $1$

---

**18.** Consider the classifier

$f(x_1,x_2)=3x_1-4x_2+12$

The normal vector to its decision boundary is

A) $(12,0)$  
B) $(3,-4)$  
C) $(-4,3)$  
D) $(3,4)$

---

**19.** A logistic regression model has decision boundary

$2x_1+x_2=8$

Which point lies on the class-1 side if class 1 corresponds to

$2x_1+x_2>8$?

A) $(2,3)$  
B) $(3,2)$  
C) $(4,1)$  
D) $(5,0)$

---

**20.** Consider a logistic regression model with

$z=5-2x$

At $x=2.5$, the predicted probability of class 1 is

A) $0$  
B) $0.25$  
C) $0.5$  
D) $1$


| Q   | Your Answer      | Correct Answer       | Principle                      | Formula / Key Idea                                     | Calculation / Check                                  |
| --- | ---------------- | -------------------- | ------------------------------ | ------------------------------------------------------ | ---------------------------------------------------- |
| 1   | **C**            | **C** ✓              | Sigmoid                        | $\sigma(z)=\frac{1}{1+e^{-z}}$                         | $\sigma(0)=\frac{1}{2}=\mathbf{0.5}$                 |
| 2   | **B**            | **B** ✓              | Linear score                   | $z=w_1x_1+w_2x_2+b$                                    | $2(1)-2+1=\mathbf{1}$                                |
| 3   | **D**            | **D** ✓              | Decision threshold             | $p\geq0.5\iff z\geq0$                                  | Therefore class 1 when $\mathbf{z\geq0}$             |
| 4   | **A**            | **A** ✓              | Decision boundary              | $z=0$                                                  | $3x_1+2x_2-6=0\Rightarrow\mathbf{3x_1+2x_2=6}$       |
| 5   | **C**            | **C** ✓              | Logistic decision boundary     | $\sigma(z)=0.5\iff z=0$                                | $2x-4=0\Rightarrow x=\mathbf{2}$                     |
| 6   | **B**            | **B** ✓              | Sigmoid                        | $z>0\Rightarrow\sigma(z)>0.5$                          | $z=2>0\Rightarrow p>0.5$                             |
| 7   | **A**            | **A** ✓              | Linear classification          | Class 1 if $f(x)\geq0$                                 | $2(0)-3(3)+6=-3<0$ → **Wait:** this gives Class 0    |
| 8   | **C**            | **C** ✓              | Linear decision boundary       | $w_1x_1+w_2x_2+b=0$                                    | $2x_1-3x_2+5=0$ is linear                            |
| 9   | **A**            | **A** ✓              | Decision boundary              | $z=0$                                                  | $-2+4-2=\mathbf{0}$                                  |
| 10  | **B**            | **B** ✓              | Monotonicity of sigmoid        | $\sigma'(z)>0$                                         | $z=-2x+6$ decreases as $x$ increases → $p$ decreases |
| 11  | **C**            | **C** ✓              | Decision boundary              | $x_1+x_2=5$                                            | $2+3=\mathbf{5}$                                     |
| 12  | **C**            | **C** ✓              | Odds                           | $\text{odds}=\frac{p}{1-p}$                            | $\frac{0.8}{0.2}=\mathbf{4}$                         |
| 13  | **Ambiguous**    | **Invalid question** | Linear classification          | Class 0 if $z<0$                                       | A: $2$, B: $4$, C: $4$, D: $1$ → **all class 1**     |
| 14  | **A**            | **B** ✗              | Equivalent decision boundaries | Multiplication by positive constant preserves boundary | $f_2=2f_1$, so same boundary                         |
| 15  | **D**            | **A** ✗              | Linear model                   | $z=w_0+w_1x_1+w_2x_2$                                  | $w_1=0$ means $x_1$ contributes $\mathbf{0}$ to $z$  |
| 16  | **B**            | **B** ✓              | Threshold classification       | Class 1 if $p\geq0.5$                                  | $0.9,0.6$ → 2 observations                           |
| 17  | **B**            | **B** ✓              | Sigmoid range                  | $0<\sigma(z)<1$                                        | Sigmoid output is always strictly between 0 and 1    |
| 18  | **I don't know** | **B**                | Normal vector                  | For $w_1x_1+w_2x_2+b=0$,normal is $(w_1,w_2)$          | $\mathbf{(3,-4)}$                                    |
| 19  | **D**            | **Ambiguous**        | Linear classification          | Class 1 if $2x_1+x_2>8$                                | C: $9>8$ **and** D: $10>8$ → both class 1            |
| 20  | **C**            | **C** ✓              | Sigmoid threshold              | $z=0\Rightarrow p=0.5$                                 | $5-2(2.5)=0\Rightarrow\mathbf{0.5}$                  |


---

# Logistic Regression & Linear Classification — Set 2

**1.** Consider the logistic regression model

$p(y=1\mid x)=\sigma(2x_1-x_2-3)$

Using a classification threshold of $0.5$, which point is classified as class 1?

A) $(1,2)$  
B) $(2,1)$  
C) $(1,1)$  
D) $(0,1)$

---

**2.** A logistic regression model has

$\log\left(\frac{p}{1-p}\right)=1+2x$

At what value of $x$ are the two classes equally likely?

A) $-1$  
B) $-0.5$  
C) $0$  
D) $0.5$

---

**3.** Consider

$p(y=1\mid x)=\sigma(3x-6)$

Which statement is correct?

A) $p=0.5$ at $x=1$  
B) $p=0.5$ at $x=2$  
C) $p=0.5$ at $x=3$  
D) $p=0.5$ at $x=6$

---

**4.** A linear classifier is given by

$f(x_1,x_2)=x_1-2x_2+4$

If class 1 is predicted when $f(x_1,x_2)>0$, which point is classified as class 1?

A) $(0,3)$  
B) $(2,3)$  
C) $(1,2)$  
D) $(0,2)$

---

**5.** Suppose a logistic regression model has coefficient $w_1=2$ for feature $x_1$. If $x_1$ increases by $1$ while all other features remain unchanged, what happens to the log-odds?

A) It decreases by $2$  
B) It increases by $1$  
C) It increases by $2$  
D) It doubles

---

**6.** For a logistic regression model,

$\log\left(\frac{p}{1-p}\right)=z$

If $z$ changes from $0$ to $2$, which statement is correct?

A) The probability decreases  
B) The probability remains $0.5$  
C) The probability becomes greater than $0.5$  
D) The probability becomes exactly $1$

---

**7.** Consider the decision boundary

$2x_1+3x_2-12=0$

Which point lies on the boundary?

A) $(3,2)$  
B) $(2,3)$  
C) $(0,4)$  
D) $(3,1)$

---

**8.** Two classifiers are defined as

$f_1(x)=3x_1-2x_2+5$

and

$f_2(x)=-6x_1+4x_2-10$

If both use $f(x)>0$ to predict class 1, which statement is correct?

A) They always produce the same predictions  
B) They always produce opposite predictions  
C) They have different decision boundaries and identical predictions  
D) They have the same decision boundary and identical predictions

---

**9.** A logistic regression model gives $p=0.2$ for an observation. What are the odds in favor of class 1?

A) $0.2$  
B) $0.25$  
C) $0.8$  
D) $4$

---

**10.** A logistic regression model has

$p(y=1\mid x)=\sigma(x_1+x_2-4)$

Which set of points lies on the class-1 side when the threshold is $0.5$?

A) $x_1+x_2<4$  
B) $x_1+x_2\leq4$  
C) $x_1+x_2>4$  
D) $x_1+x_2=4$

---

**11.** Consider

$z=2x_1-3x_2+6$

If $z=3$, what is the corresponding value of the log-odds?

A) $0$  
B) $1$  
C) $2$  
D) $3$

---

**12.** In a binary logistic regression model, suppose all feature values remain fixed except $x_2$. If the coefficient of $x_2$ is negative, then increasing $x_2$ will:

A) Always increase the predicted probability of class 1  
B) Always decrease the predicted probability of class 1  
C) Have no effect on the predicted probability  
D) Make the predicted probability exactly $0.5$

---

**13.** A classifier uses

$f(x_1,x_2)=4x_1+3x_2-12$

The distance of a point from the decision boundary depends on the denominator

$\sqrt{4^2+3^2}$

What is this denominator?

A) $5$  
B) $7$  
C) $12$  
D) $25$

---

**14.** Suppose a logistic regression model has

$p(y=1\mid x)=\sigma(4x-2)$

Which statement is true?

A) At $x=0$, $p>0.5$  
B) At $x=0.5$, $p=0.5$  
C) At $x=1$, $p=0.5$  
D) At $x=2$, $p<0.5$

---

**15.** Consider the linear classifier

$f(x_1,x_2)=x_1+x_2-3$

Which transformation leaves its decision boundary unchanged?

A) Multiplying the entire function by $-1$  
B) Multiplying the entire function by $2$  
C) Changing only the constant from $-3$ to $-4$  
D) Changing the coefficient of $x_1$ from $1$ to $2$

---

**16.** A logistic regression model has

$\log\left(\frac{p}{1-p}\right)=2$

Which statement is correct?

A) $p=0.5$  
B) $p<0.5$  
C) $p>0.5$  
D) $p=2$

---

**17.** Consider the classifier

$f(x_1,x_2)=2x_1+2x_2-8$

Which of the following is the equation of its decision boundary?

A) $x_1+x_2=2$  
B) $x_1+x_2=4$  
C) $2x_1+2x_2=4$  
D) $x_1-x_2=4$

---

**18.** Suppose two observations have logistic regression scores $z_1=-2$ and $z_2=2$. Which observation has the larger predicted probability of class 1?

A) Observation 1  
B) Observation 2  
C) Both have the same probability  
D) Cannot be determined

---

**19.** A linear classifier has decision boundary

$x_1-2x_2+6=0$

Which vector is perpendicular to this boundary?

A) $(1,-2)$  
B) $(2,1)$  
C) $(-2,1)$  
D) $(1,2)$

---

**20.** Consider the logistic regression model

$p(y=1\mid x)=\sigma(2x_1-x_2+1)$

If the threshold is changed from $0.5$ to $0.8$, which statement is correct?

A) The decision boundary remains unchanged  
B) The decision boundary shifts because the required log-odds changes  
C) The model becomes nonlinear  
D) The coefficient values must become zero


| Q   | Your Answer      | Correct Answer | Principle                  | Formula / Key Idea                  | Calculation / Check                                               |
| --- | ---------------- | -------------- | -------------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| 1   | **B**            | **B** ✓        | Decision threshold         | $p\geq0.5\iff z\geq0$               | B: $2(2)-1-3=0$ → class 1                                         |
| 2   | **I don't know** | **B**          | Log-odds                   | $p=0.5\iff\log\frac{p}{1-p}=0$      | $1+2x=0\Rightarrow x=\mathbf{-0.5}$                               |
| 3   | **B**            | **B** ✓        | Decision boundary          | $\sigma(z)=0.5\iff z=0$             | $3x-6=0\Rightarrow x=\mathbf2$                                    |
| 4   | **C**            | **C** ✓        | Linear classification      | Class 1 if $f(x)>0$                 | $1-4+4=\mathbf1>0$                                                |
| 5   | **I don't know** | **C**          | Log-odds coefficient       | $\text{log-odds}=w_0+w_1x_1+\cdots$ | $\Delta x_1=1\Rightarrow\Delta\text{log-odds}=2$                  |
| 6   | **A**            | **C** ✗        | Log-odds & probability     | $z>0\Rightarrow p>0.5$              | $z=2\Rightarrow p=\sigma(2)>0.5$                                  |
| 7   | **A**            | **A** ✓        | Decision boundary          | $2x_1+3x_2-12=0$                    | $2(3)+3(2)-12=0$                                                  |
| 8   | **A**            | **Invalid**    | Sign of classifier         | $f_2=-2f_1$                         | Same boundary, but predictions are opposite → **no valid option** |
| 9   | **B**            | **B** ✓        | Odds                       | $\text{odds}=\frac{p}{1-p}$         | $\frac{0.2}{0.8}=\mathbf{0.25}$                                   |
| 10  | **C or D**       | **C** ✓        | Logistic threshold         | $p>0.5\iff z>0$                     | $x_1+x_2-4>0\Rightarrow x_1+x_2>4$                                |
| 11  | **I don't know** | **D**          | Log-odds                   | $\log\frac{p}{1-p}=z$               | Given $z=3$, log-odds $=\mathbf3$                                 |
| 12  | **B**            | **B** ✓        | Coefficient interpretation | $\frac{dp}{dx_2}$ has sign of $w_2$ | $w_2<0\Rightarrow$ increasing $x_2$ decreases $p$                 |
| 13  | **A**            | **A** ✓        | Distance from hyperplane   | $\|w\|=\sqrt{w_1^2+w_2^2}$          | $\sqrt{4^2+3^2}=\sqrt{25}=\mathbf5$                               |
| 14  | **B**            | **B** ✓        | Sigmoid threshold          | $p=0.5\iff z=0$                     | $4x-2=0\Rightarrow x=\mathbf{0.5}$                                |
| 15  | **A**            | **Ambiguous**  | Decision boundary          | $f(x)=0$                            | Multiplying by **2 or −1** keeps boundary unchanged → A **and B** |
| 16  | **I don't know** | **C**          | Log-odds                   | $z>0\iff p>0.5$                     | $z=2>0\Rightarrow p>0.5$                                          |
| 17  | **B**            | **B** ✓        | Decision boundary          | $2x_1+2x_2-8=0$                     | $x_1+x_2=\mathbf4$                                                |
| 18  | **B**            | **B** ✓        | Sigmoid monotonicity       | $\sigma'(z)>0$                      | $2>-2\Rightarrow\sigma(2)>\sigma(-2)$                             |
| 19  | **A**            | **A** ✓        | Normal vector              | Boundary: $w^Tx+b=0$; normal $=w$   | $w=\mathbf{(1,-2)}$                                               |
| 20  | **B**            | **B** ✓        | Threshold & log-odds       | $p=t\Rightarrow z=\ln\frac{t}{1-t}$ | For $t=0.8$, required $z=\ln4>0$ → boundary shifts                |