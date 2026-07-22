# 13 Random Forest

tags:
#ml
#ensemble
#placements
#interview

---

## Why this topic matters
Random Forest is the "workhorse" of Machine Learning. In hackathons and tabular data competitions, it often beats deep learning. It fixes the overfitting problem of Decision Trees by using the **Wisdom of Crowds**.

## Learning Objectives
- Understand Ensemble Learning.
- Learn the concept of Bagging.
- Explain why "Random" is in the name.

## Prerequisites
- [[11 Decision Trees]]

---

## Intuition
Imagine you are predicting the winner of a football match.
- **Decision Tree**: One expert gives a prediction. They might be having a bad day.
- **Random Forest**: You ask 100 random experts and take a **Vote**. Even if some are wrong, the majority usually agrees on the right answer.

This is **Ensemble Learning**: Combining multiple weak models to form a strong one.

---

## Detailed Explanation

### 1. Ensemble Learning
The idea that a group of "average" models can beat a single "perfect" model.

### 2. Bagging (Bootstrap Aggregating)
Random Forest uses Bagging to build diverse trees:
- **Bootstrap**: Create random subsets of the data (with replacement). Some rows are repeated, some are left out.
- **Aggregating**: Combine predictions (Average for Regression, Majority Vote for Classification).

```mermaid
flowchart TD
    Data[Original Data]
    Data --> S1[S1: Bootstrap Sample A]
    Data --> S2[S2: Bootstrap Sample B]
    Data --> S3[S3: Bootstrap Sample C]
    S1 --> T1[Tree 1]
    S2 --> T2[Tree 2]
    S3 --> T3[Tree 3]
    T1, T2, T3 --> Vote[Majority Vote]
    Vote -- Result --> Final[Final Prediction]
```

### 3. Why "Random" Forest?
Not only does it sample rows, but it also samples **Features** at each split.
- In a normal tree, you check all features to find the best split.
- In Random Forest, at each node, you only check a random subset (e.g., $\sqrt{features}$).

This forces the trees to be **uncorrelated** (diverse). If all trees are identical, the ensemble adds no value.

### 4. Out-of-Bag (OOB) Error
Rows that were not used to train a specific tree ("Out-of-Bag") can serve as a test set for that tree. This gives us a free validation score!

---

## Real-world Example
**E-Commerce Recommendation**
Amazon uses Random Forests (and variants) to categorize products. Multiple "experts" (trees) vote on whether a product is "Electronics", "Books", or "Toys". If 80 trees say "Electronics," it's labeled as such.

---

## Advantages
- **Robust**: Doesn't overfit easily (unlike a single tree).
- **Versatile**: Works for Classification and Regression.
- **Handles Missing Data**: Can handle NaNs gracefully.
- **Feature Importance**: Tells you which features matter.

## Limitations
- **Slow**: 100 trees are slower to train/run than 1 tree.
- **Black Box**: Hard to interpret the logic of 100 trees combined.
- **Not Linear**: Cannot extrapolate trends (predict future values outside the training range).

---

## Common Interview Questions
- **Why is Random Forest better than a single Decision Tree?**
- **What is Bagging?**
- **Why do we select random features for each split?**
- **What is Out-of-Bag (OOB) error?**

### Interview Answer Tips
- Mention **Variance Reduction**. Random Forest reduces variance by averaging decorrelated trees.
- Explain that **Randomness** ensures diversity among trees.

---

## Common Mistakes
- Thinking it prevents overfitting 100%. (It reduces it, but a forest of 1,000 deep trees can still overfit).
- Using it for extrapolation (e.g., predicting next year's sales based on past years).

---

## Summary
Random Forest is an Ensemble method that builds many Decorrelated Decision Trees via Bagging and takes a majority vote. It is the default "go-to" algorithm for tabular data.

---

## Practice Questions
1. What is the main difference between Bagging and Boosting?
2. Why do we sample both rows (Bootstrap) and features (Random)?
3. How does Random Forest calculate the final prediction for Regression?
4. Can you parallelize training a Random Forest?
5. What does "Feature Importance" mean in a Forest?

---

## Mini Project Ideas
1. **Feature Importance**: Train a Random Forest on the Titanic dataset. Plot the relative importance of each feature.
2. **OOB Score**: Train a RF with `oob_score=True`. Compare OOB score to cross-validation score.

---

## Further Reading
- [[11 Decision Trees]]
- [[15 Boosting]]
- [[25 Cross-Validation]]