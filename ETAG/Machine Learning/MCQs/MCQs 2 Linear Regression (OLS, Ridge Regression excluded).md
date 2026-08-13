# Linear Regression — 30 GATE DA–Style Questions

> **Note:** These questions focus on **Linear Regression concepts** and deliberately exclude **OLS derivations** and **Ridge Regression**.

---

## Easy

### Q1. What does $\beta_1$ represent?

In the model

$$  
y = \beta_0 + \beta_1x + \epsilon  
$$

A) Expected value of $y$ when $x=0$  
B) Change in expected $y$ for a unit increase in $x$  
C) Variance of $y$  
D) Correlation between $x$ and $y$

---

### Q2. Prediction from a regression equation

If the regression equation is

$$  
\hat{y} = 5 + 3x  
$$

what is the predicted value of $y$ when $x=4$?

A) 12  
B) 15  
C) 17  
D) 20

---

### Q3. Residual

A residual in regression is:

A) $y-\bar{y}$  
B) $\hat{y}-y$  
C) $y-\hat{y}$  
D) $x-\bar{x}$

---

### Q4. Squared prediction errors

Which metric is most directly based on the squared prediction errors?

A) MAE  
B) MSE  
C) Accuracy  
D) Precision

---

### Q5. Interpretation of $R^2$

If $R^2=0.81$, the model explains approximately what fraction of the variability in the response?

A) 8.1%  
B) 19%  
C) 81%  
D) 90%

---

### Q6. Perfect predictions

If all predicted values exactly equal the observed values, the MSE is:

A) 0  
B) 1  
C) $-1$  
D) Cannot be determined

---

### Q7. Multiple Linear Regression

In multiple linear regression,

$$  
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \epsilon  
$$

$\beta_1$ represents:

A) Effect of $x_1$, ignoring $x_2$  
B) Effect of $x_1$, holding $x_2$ fixed  
C) Effect of $x_2$, holding $x_1$ fixed  
D) Correlation between $x_1$ and $x_2$

---

### Q8. Regression Problem

Which of the following is a regression problem?

A) Predict whether an email is spam  
B) Predict house price  
C) Predict whether a patient has a disease  
D) Predict whether a transaction is fraudulent

---

### Q9. Sign of the Regression Slope

If $x$ and $y$ have a strong negative linear relationship, the slope of the simple linear regression is generally:

A) Positive  
B) Negative  
C) Zero  
D) Always equal to $-1$

---

### Q10. Mean Absolute Error

MAE is defined as:

A) Mean of squared errors  
B) Mean of absolute errors  
C) Square root of mean squared errors  
D) Maximum absolute error

---

# Medium

### Q11. Calculating a Residual

Consider

$$  
\hat{y} = 10 + 2x  
$$

For $x=5$, the actual value is $y=18$. What is the residual?

A) $-2$  
B) 0  
C) 2  
D) 8

---

### Q12. Calculating MSE

Suppose the actual values are $[2,4,6]$ and predictions are $[1,5,6]$.

What is the MSE?

A) $\frac{2}{3}$  
B) $1$  
C) $2$  
D) $3$

---

### Q13. Training vs Test Error

A model has:

- Training MSE = 2
    
- Test MSE = 25
    

This most strongly suggests:

A) Underfitting  
B) Overfitting  
C) Perfect generalization  
D) No relationship between variables

---

### Q14. High Training and Test Error

A model has very high training error and very high test error. This is most consistent with:

A) Overfitting  
B) Underfitting  
C) Data leakage  
D) Multicollinearity only

---

### Q15. Representing Nonlinear Relationships

Which transformation can allow a nonlinear relationship to be represented using a linear regression model?

A) Adding polynomial features  
B) Removing the response variable  
C) Randomly shuffling the target  
D) Converting all values to zero

---

### Q16. Multicollinearity

Consider

$$  
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \epsilon  
$$

If $x_1$ and $x_2$ are highly correlated, the main issue is:

A) Heteroscedasticity  
B) Multicollinearity  
C) Autocorrelation  
D) Underflow

---

### Q17. Effect of Multicollinearity

Which statement about multicollinearity is TRUE?

A) It necessarily makes predictions impossible.  
B) It can make individual coefficient estimates unstable.  
C) It always increases $R^2$ to 1.  
D) It means the target has zero variance.

---

### Q18. Heteroscedasticity

If the variance of residuals increases as $x$ increases, this is an example of:

A) Homoscedasticity  
B) Heteroscedasticity  
C) Multicollinearity  
D) Normalization

---

### Q19. Desirable Residual Plot

Which residual plot is generally desirable for a well-specified linear regression?

A) Random scatter around zero  
B) Clear U-shaped pattern  
C) Clear increasing trend  
D) Clear decreasing trend

---

### Q20. Interpretation of $R^2$

Suppose a model gives $R^2=0.95$. Which statement is necessarily true?

A) The model is causal.  
B) The model will perform well on unseen data.  
C) 95% of the observed response variability is explained by the model.  
D) The correlation between every predictor and target is 0.95.

---

# GATE-Level

### Q21. Training vs Test $R^2$

A regression model has:

- Training $R^2=0.99$
    
- Test $R^2=0.52$
    

Which is the most likely explanation?

A) Overfitting  
B) Underfitting  
C) Perfect generalization  
D) Target variable has zero variance

---

### Q22. Increasing the Target

Consider the model

$$  
\hat{y} = 4 + 3x  
$$

If every target value $y$ is increased by 10 while $x$ remains unchanged, the new regression model's intercept and slope are expected to be:

A) Intercept +10, slope unchanged  
B) Intercept unchanged, slope +10  
C) Both increase by 10  
D) Both remain unchanged

---

### Q23. Scaling the Predictor

Suppose every $x$ value is multiplied by 2 while $y$ is unchanged.

If the original regression slope is $b$, the new slope with respect to the transformed variable $x'=2x$ is:

A) $2b$  
B) $\frac{b}{2}$  
C) $b+2$  
D) $b$

---

### Q24. $R^2$ vs Adjusted $R^2$

A regression model includes 20 predictors and 100 observations.

Adding another predictor causes $R^2$ to increase slightly but adjusted $R^2$ to decrease.

What does this indicate?

A) The new predictor improves the model substantially.  
B) The new predictor does not provide enough additional explanatory power to justify its complexity.  
C) The original model had $R^2=0$.  
D) The new predictor must be perfectly correlated with the target.

---

### Q25. MAE vs MSE

Which situation is most likely to make MAE preferable to MSE?

A) When large errors should receive disproportionately high penalties  
B) When the data contain substantial outliers and we want less sensitivity to them  
C) When all errors are zero  
D) When the response is categorical

---

### Q26. U-Shaped Residual Pattern

A regression model's residuals show a clear U-shaped pattern against $x$.

The most likely issue is:

A) Nonlinear relationship not captured by the model  
B) Perfect linearity  
C) Multicollinearity necessarily  
D) Zero variance

---

### Q27. Comparing MAE

Consider two models evaluated on the same test set:

|Model|MAE|MSE|
|---|--:|--:|
|A|4|100|
|B|5|30|

Which model has smaller average absolute error?

A) A  
B) B  
C) Both equal  
D) Cannot determine

---

### Q28. Leverage and Influence

A single observation has an extremely large residual and is far from the center of the predictor values.

Such an observation may have:

A) High leverage and potentially high influence  
B) Zero leverage  
C) Zero residual  
D) No effect on the fitted model

---

### Q29. Perfect Linear Dependence

Suppose two predictors $x_1$ and $x_2$ are perfectly linearly dependent:

$$  
x_2 = 3x_1  
$$

In an ordinary multiple linear regression model containing both predictors, the coefficient parameters are:

A) Always uniquely identifiable  
B) Not uniquely identifiable  
C) Always zero  
D) Always equal

---

### Q30. Calculating MAE and MSE

A model predicts:

$$  
[10,20,30]  
$$

while actual values are:

$$  
[12,18,33]  
$$

Which statement is correct?

A) MAE = 2  
B) MSE = 5  
C) RMSE = 5  
D) MAE = 3

---

# Answer Key

| Q   | Ans | Q   | Ans   | Q   | Ans                   |
| --- | --- | --- | ----- | --- | --------------------- |
| 1   | B   | 11  | **A** | 21  | A                     |
| 2   | C   | 12  | **A** | 22  | A                     |
| 3   | C   | 13  | B     | 23  | B                     |
| 4   | B   | 14  | B     | 24  | B                     |
| 5   | C   | 15  | A     | 25  | B                     |
| 6   | A   | 16  | B     | 26  | A                     |
| 7   | B   | 17  | B     | 27  | A                     |
| 8   | B   | 18  | B     | 28  | A                     |
| 9   | B   | 19  | A     | 29  | B                     |
| 10  | B   | 20  | C     | 30  | **No correct option** |

---

## Important Formulas

### Simple Linear Regression

$$  
\hat{y} = \beta_0 + \beta_1x  
$$

### Multiple Linear Regression

$$  
\hat{y} = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_px_p  
$$

### Residual

$$  
e_i = y_i - \hat{y}_i  
$$

### Mean Absolute Error

$$  
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|  
$$

### Mean Squared Error

$$  
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2  
$$

### Root Mean Squared Error

$$  
RMSE = \sqrt{MSE}  
$$

### Coefficient of Determination

$$  
R^2 = 1-\frac{SS_{res}}{SS_{tot}}  
$$