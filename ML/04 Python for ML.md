# 04 Python for ML

tags:
#python
#ml
#placements
#interview
#programming

---

## Why this topic matters
Python is the "lingua franca" of AI. In interviews, you will be asked to write Python code to manipulate data, implement algorithms from scratch, or debug ML pipelines. You don't need to be a software architect, but you must master the specific libraries used for ML.

## Learning Objectives
- Understand why Python dominates AI.
- Master the "Big 4" libraries: NumPy, Pandas, Matplotlib, Scikit-Learn.
- Write efficient, vectorized code (avoiding loops).

## Prerequisites
- Basic programming knowledge (variables, loops, functions).

---

## Intuition
Imagine you are a **Carpenter**.
- **General Python** is your hammer and saw. It's good for building anything (websites, scripts, bots).
- **Python for ML** is your specialized set of chisels and planes. You don't use a hammer to shave wood; you use the right tool.
  - Need to do math? **NumPy**.
  - Need to organize data? **Pandas**.
  - Need to draw graphs? **Matplotlib**.
  - Need to build a model? **Scikit-Learn**.

---

## Detailed Explanation

### Why Python?
1. **Simplicity**: Easy to read, looks like English.
2. **Ecosystem**: Huge collection of pre-built libraries (`pip install`).
3. **Community**: If you have an error, someone has already solved it on StackOverflow.
4. **Glue Language**: Python can call C/C++ code (which is fast) under the hood.

### The "Big 4" Libraries

#### 1. NumPy (Numerical Python)
Used for mathematical operations on multi-dimensional arrays.
- **Key Concept**: **Vectorization**. Doing math on entire arrays at once instead of using `for` loops.
```python
# Bad (Slow Loop)
result = []
for x in my_list:
    result.append(x * 2)

# Good (Vectorized)
import numpy as np
arr = np.array([1, 2, 3])
result = arr * 2  # [2, 4, 6]
```

#### 2. Pandas (Data Analysis)
Used for manipulating structured data (like Excel sheets).
- **DataFrame**: A table with rows and columns.
- **Key Operations**: Filtering, grouping, merging, handling missing values.
```python
import pandas as pd
df = pd.read_csv('data.csv')
adults = df[df['age'] > 18]  # Filter
avg_salary = adults['salary'].mean()  # Aggregate
```

#### 3. Matplotlib / Seaborn (Visualization)
Used to create charts and graphs.
- **Matplotlib**: Low-level, highly customizable.
- **Seaborn**: High-level, prettier defaults.
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

#### 4. Scikit-Learn (Machine Learning)
The standard library for classical ML algorithms.
- **API Pattern**: `model.fit(X, y)` and `model.predict(X_test)`.
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Python List Comprehensions
A concise way to create lists. Essential for data cleaning.
```python
# Traditional
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i**2)

# Comprehension
squares = [i**2 for i in range(10) if i % 2 == 0]
```

---

## Real-world Example
**Data Science Pipeline at a Startup**
1. **NumPy**: Calculate the distance between user locations using vector math.
2. **Pandas**: Load 1 million user logs from CSV, filter out bots, and group by country.
3. **Matplotlib**: Plot a histogram of user ages to find the demographic.
4. **Scikit-Learn**: Train a Random Forest to predict which users will churn.

---

## Advantages
- **Rapid Prototyping**: You can test an idea in 10 lines of code.
- **Readability**: Code is easy to share and review.
- **Integration**: Works easily with Deep Learning frameworks (PyTorch, TensorFlow).

## Limitations
- **Speed**: Pure Python is slow. (But NumPy/TensorFlow use C++ under the hood, so it's fast).
- **Mobile**: Not great for building mobile apps directly.

---

## Common Interview Questions
- **Why is Python preferred for ML?**
- **What is the difference between a List and a NumPy Array?**
- **How do you handle missing values in Pandas?**
- **Explain `model.fit()` and `model.predict()`.**

### Interview Answer Tips
- Mention **Vectorization**. It's the #1 performance tip for Python ML code.
- Know the difference between `loc` and `iloc` in Pandas.

---

## Common Mistakes
- Using `for` loops for math operations (slow!).
- Modifying a DataFrame without using `.copy()` (SettingWithCopyWarning).
- Forgetting to normalize data before feeding it to ML models.

---

## Summary
Python is the standard language for AI due to its simplicity and powerful libraries. Mastering NumPy (math), Pandas (data), Matplotlib (viz), and Scikit-Learn (ML) is essential for any ML engineer.

---

## Practice Questions
1. How do you check for missing values in a Pandas DataFrame?
2. What is broadcasting in NumPy?
3. How do you select a specific column in a Pandas DataFrame?
4. Write a list comprehension to filter even numbers from a list.
5. What is the difference between `df.loc[]` and `df.iloc[]`?

---

## Mini Project Ideas
1. **Data Analyzer**: Load a CSV, print basic stats, and plot a histogram using Pandas/Matplotlib.
2. **From Scratch**: Implement Linear Regression using only NumPy (no Scikit-Learn).

---

## Further Reading
- [[05 Data Cleaning]]
- [[06 Feature Engineering]]
- [[11 Linear Regression]]