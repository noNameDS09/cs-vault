# 06 Feature Engineering

tags:
#ml
#data
#placements
#interview

---

## Why this topic matters
"Feature Engineering is the secret sauce of Machine Learning." You can have the most powerful algorithm, but if you give it bad features, it will fail. In interviews, this is where you show creativity and domain knowledge.

## Learning Objectives
- Understand what a "Feature" is.
- Learn Encoding techniques for categorical data.
- Learn Scaling techniques for numerical data.
- Understand Feature Selection.

## Prerequisites
- [[04 Python for ML]]
- [[05 Data Cleaning]]

---

## Intuition
Imagine you are hiring a **Chef**.
- **Raw Data**: A pile of vegetables, meat, and spices.
- **Features**: The chopped, marinated, and measured ingredients ready to cook.
- **Model**: The cooking process.

If you throw whole onions and uncut meat into a pan (Raw Data), the dish will be terrible. If you chop them perfectly (Feature Engineering), even a mediocre cook (Simple Model) can make a great dish.

---

## Detailed Explanation

### 1. What is a Feature?
A feature is an individual measurable property or characteristic of the phenomena you are observing.
- **Example**: In a House Price Predictor, features are: `Area`, `Bedrooms`, `Location`, `Age`.
- **Goal**: Transform raw data into features that better represent the underlying problem to the ML model.

### 2. Encoding (Converting Text to Numbers)
ML models only understand numbers. You must convert text (Categories) into numbers.

#### A. Label Encoding
Assign a unique number to each category.
- **Use Case**: Ordinal Data (Order matters).
- **Risk**: Model might think "Red (2)" > "Blue (1)".
```python
# Low:0, Medium:1, High:2
df['Education'] = df['Education'].map({'Low':0, 'Medium':1, 'High':2})
```

#### B. One-Hot Encoding
Create a new column for each category with 0 or 1.
- **Use Case**: Nominal Data (No order).
- **Risk**: Too many columns if you have many categories.
```python
# Color: Red, Blue, Green
# Becomes:
# Red | Blue | Green
# 1   | 0    | 0
# 0   | 1    | 0
df = pd.get_dummies(df, columns=['Color'])
```

### 3. Scaling (Normalizing Numbers)
Different features have different scales (e.g., `Age` is 0-100, `Salary` is 0-100,000). Algorithms like KNN and Neural Networks get confused by this.

#### A. Min-Max Scaling (Normalization)
Squashes values between 0 and 1.
$$X_{new} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

#### B. Standardization (Z-Score)
Centers data around 0 with a standard deviation of 1.
$$X_{new} = \frac{X - \mu}{\sigma}$$

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])
```

### 4. Feature Selection
Removing irrelevant features to reduce noise and overfitting.
- **Correlation Matrix**: Remove features that are highly correlated with each other.
- **Recursive Feature Elimination (RFE)**: Let the model tell you which features are useless.

---

## Real-world Example
**Credit Score Prediction**
- **Raw**: "John Doe", "123 Main St", "Paid on time".
- **Engineered**: 
  - `Is_Employed` (1/0)
  - `Income_Debt_Ratio` (Calculated)
  - `Payment_History_Score` (Encoded: Late=0, OnTime=1)
  - `Age_Group` (Binned: 18-25, 26-40, etc.)

---

## Advantages
- Boosts accuracy significantly (often more than changing the model).
- Reduces training time (fewer features).
- Helps simpler models perform like complex ones.

## Limitations
- Requires domain knowledge.
- Can lead to overfitting if you engineer too many specific features.

---

## Common Interview Questions
- **What is One-Hot Encoding and when do you use it?**
- **Why do we need Feature Scaling?**
- **What is the difference between Normalization and Standardization?**
- **How do you handle high-cardinality categorical features?**

### Interview Answer Tips
- Mention that **Tree-based models (Random Forest)** don't need scaling, but **Distance-based models (KNN, K-Means)** do.
- Explain **Dummy Variable Trap** (dropping one column after One-Hot Encoding).

---

## Common Mistakes
- Applying One-Hot Encoding to ordinal data (losing order information).
- Fitting the Scaler on the Test set (Data Leakage). Always fit on Train, transform on Test.

---

## Summary
Feature Engineering transforms raw data into a format that ML models can understand. It involves Encoding (text $\rightarrow$ numbers) and Scaling (normalizing ranges). It is often the most critical step in the ML pipeline.

---

## Practice Questions
1. Why can't we feed text data directly into an ML model?
2. What is the "Dummy Variable Trap"?
3. Which algorithms require feature scaling?
4. How would you encode a "Month" feature? (Ordinal or One-Hot?)
5. What happens if you don't scale features for a KNN model?

---

## Mini Project Ideas
1. **Titanic Dataset**: Perform One-Hot Encoding on 'Sex' and 'Embarked'. Scale 'Age' and 'Fare'.
2. **House Prices**: Create a new feature "Total Rooms" = "Bedrooms" + "Bathrooms".

---

## Further Reading
- [[05 Data Cleaning]]
- [[10 Model Evaluation]]
- [[16 Random Forest]]