## Q1(a).Explain the difference between supervised and unsupervised learning with suitable examples.
---
### Supervised vs Unsupervised Learning

| Basis              | Supervised Learning                                                                     | Unsupervised Learning                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Definition         | The model learns from **labeled data**, where input and corresponding output are known. | The model learns from **unlabeled data**, where only input data is available.                                      |
| Objective          | To learn a mapping between input and output and make predictions for new data.          | To discover hidden patterns, structures, or groups in the data.                                                    |
| Training Data      | Requires labeled data.                                                                  | Does not require labeled data.                                                                                     |
| Main Tasks         | Classification and Regression.                                                          | Clustering and Dimensionality Reduction.                                                                           |
| Example Algorithms | Linear Regression, Logistic Regression, Decision Tree, SVM.                             | K-Means, Hierarchical Clustering, PCA.                                                                             |
| Example            | Predict whether an email is **spam or not spam** using previously labeled emails.       | Group customers into different **customer segments** based on their purchasing behavior without predefined groups. |

**Example of Supervised Learning:**  
Suppose we have data containing students' study hours and their corresponding exam scores. A regression model can learn from this labeled data and predict the score of a new student based on their study hours.

**Example of Unsupervised Learning:**  
Suppose we have customer data containing age, income, and purchasing behavior but no predefined customer categories. **K-Means clustering** can automatically group customers with similar characteristics.

**In short:**  
**Supervised Learning → Labeled data → Predict output**  
**Unsupervised Learning → Unlabeled data → Discover patterns/groups**

---

## Q1(b). Compare and contrast machine learning with traditional programming. Include examples to highlight the differences.
---
### Machine Learning vs Traditional Programming

|Basis|Traditional Programming|Machine Learning|
|---|---|---|
|Basic approach|Programmer explicitly defines the rules and logic.|Model learns rules/patterns from data.|
|Input|**Data + Rules/Program**|**Data + Expected Output** during training|
|Output|Result produced according to predefined rules.|A trained model that can make predictions on new data.|
|Rules|Written manually by the programmer.|Learned automatically from training data.|
|Adaptability|Changes require modifying the program/rules.|Can adapt by retraining with new data.|
|Suitable for|Problems with clearly defined rules and logic.|Problems where rules are complex or difficult to explicitly define.|

The basic difference can be represented as:

**Traditional Programming:**

`Data + Program/Rules → Output`

**Machine Learning:**

`Data + Expected Output → Learning Algorithm → Model`

The question of this distinction is explicitly included as **Q1(a), 5 marks** in the uploaded Machine Learning paper.

### Example 1: Spam Email Detection

In traditional programming, the programmer might manually define rules such as:

- If the email contains "win money", mark it as spam.
    
- If there are many suspicious links, mark it as spam.
    
- If the sender is known, consider it legitimate.
    

The program applies these predefined rules to classify emails.

In machine learning, we provide the model with thousands of emails already labeled **Spam** or **Not Spam**. The model learns patterns from these examples and uses the learned model to classify new emails.

### Example 2: House Price Prediction

In traditional programming, we could manually create a formula based on rules such as:

`Price = Area × Rate per sq. ft. + Location adjustment`

The programmer determines these rules.

In machine learning, we provide historical data containing **house features and their actual prices**. A regression algorithm learns the relationship between the features and price, and then predicts the price of a new house.

### Conclusion

Traditional programming depends on **explicitly programmed rules**, whereas machine learning **learns patterns from data**. Traditional programming is preferable when the rules are well-defined, while machine learning is useful when deriving explicit rules is difficult or impractical.

---

## Q2(a). Differentiate between regression and correlation with examples
---
### Regression vs Correlation

|Basis|Regression|Correlation|
|---|---|---|
|Definition|Regression describes the **relationship between variables** and is used to predict a dependent variable from one or more independent variables.|Correlation measures the **strength and direction of association** between two variables.|
|Purpose|Mainly used for **prediction and estimation**.|Mainly used to determine whether variables are **related and how strongly**.|
|Variables|Distinguishes between **dependent (Y)** and **independent (X)** variables.|Treats both variables symmetrically; there is no dependent or independent variable.|
|Output|Produces a **regression equation/model**.|Produces a **correlation coefficient (r)**.|
|Range|Regression coefficients are not restricted to −1 to +1.|Correlation coefficient lies between **−1 and +1**.|
|Direction|Regression describes how Y changes with X.|Correlation indicates positive, negative, or no linear association.|
|Example|Predicting **house price from area**.|Measuring the relationship between **study hours and exam marks**.|

genui{"learning_viz":{"type_id":"CORRELATION"}}

**Example of Regression:**  
If house area is (X) and house price is (Y), regression can establish an equation such as:

							$Y = a + bX$

This equation can be used to **predict the price** of a house when its area is known.

**Example of Correlation:**  
If we calculate the correlation between study hours and exam marks and obtain (r = 0.85), it indicates a **strong positive linear relationship**: students who study more hours tend to have higher marks.

**In short:**  
**Regression → explains/predicts one variable using another.**  
**Correlation → measures the strength and direction of their relationship.**

---

## Q2(b). Explain the difference between univariate and multivariate regression with examples.  
---

### Univariate vs Multivariate Regression

| Basis                           | Univariate Regression                                                              | Multivariate Regression                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Definition                      | Regression involving **one independent variable** to predict a dependent variable. | Regression involving **two or more independent variables** to predict a dependent variable. |
| Number of Independent Variables | One                                                                                | Two or more                                                                                 |
| General Equation                | $Y = a + bX$                                                                       | $Y = a + b_1X_1 + b_2X_2 + \cdots + b_nX_n$                                                 |
| Complexity                      | Relatively simple                                                                  | More complex                                                                                |
| Example                         | Predicting **house price from area**.                                              | Predicting **house price from area, number of bedrooms, and location**.                     |


**Example of Univariate Regression:**  
Suppose we want to predict a student's marks based only on study hours:

				$Marks = a + b(\text{Study Hours})$

Here, **study hours** is the single independent variable.

**Example of Multivariate Regression:**  
Suppose house price is predicted using area, number of bedrooms, and age of the house:

			$Price = a + b_1(Area) + b_2(Bedrooms) + b_3(Age)$

Here, there are **three independent variables**.

**In short:**  
**Univariate regression → 1 independent variable → 1 dependent variable**  
**Multivariate regression → 2 or more independent variables → 1 dependent variable**
