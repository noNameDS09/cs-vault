# 20 Hyperparameter Tuning

tags:
#ml
#optimization
#placements
#interview

---

## Why this topic matters
Models have "knobs" you can turn to improve performance. These are **Hyperparameters**. Knowing how to tune them systematically distinguishes a novice from a professional ML engineer.

## Learning Objectives
- Differentiate Parameters vs. Hyperparameters.
- Learn Grid Search, Random Search, and Bayesian Optimization.
- Understand Cross-Validation.

## Prerequisites
- [[10 Linear Regression]]
- [[12 Decision Trees]]

---

## Intuition
Imagine you are tuning a **Radio** to find the best station.
- **Parameters**: The internal wiring of the radio (fixed).
- **Hyperparameters**: The knobs you turn (Frequency, Bass, Treble, Volume).

You can't "learn" the best knob positions from the music. You have to **try** different combinations until it sounds good.

---

## Detailed Explanation

### 1. Parameters vs. Hyperparameters
| | **Parameters** | **Hyperparameters** |
| :--- | :--- | :--- |
| **Source** | Learned from data (e.g., weights, bias). | Set by the human before training. |
| **Examples** | Slope ($w$), Intercept ($b$). | Learning Rate, Tree Depth, K in KNN, C in SVM. |
| **Goal** | Make predictions. | Optimize model performance. |

### 2. Tuning Methods

#### Grid Search
Try **every possible combination** of hyperparameters.
- **Pros**: Exhaustive. Finds the best combo.
- **Cons**: Extremely slow. $10 \times 10 \times 10 = 1000$ models to train.

#### Random Search
Pick **random combinations**.
- **Pros**: Much faster. Often finds a good enough solution.
- **Cons**: Might miss the optimal point.

#### Bayesian Optimization (Advanced)
Use past evaluations to predict promising combinations. (Used by Optuna, Hyperopt).

### 3. Cross-Validation
Don't just split Train/Test once. Split into K folds.
- Train on K-1 folds, Test on 1 fold. Repeat K times.
- Average the scores.
- **Why?**: More robust estimate of performance.

```mermaid
flowchart TD
    subgraph "K-Fold CV (K=5)"
    F1[Fold 1 (Test)] --- F2[Fold 2 (Train)]
    F2 --- F3[Fold 3 (Train)]
    F3 --- F4[Fold 4 (Train)]
    F4 --- F5[Fold 5 (Train)]
    end
    
    subgraph "Next Iteration"
    T1[Fold 1 (Train)] --- T2[Fold 2 (Test)]
    T2 --- T3[Fold 3 (Train)]
    T3 --- T4[Fold 4 (Train)]
    T4 --- T5[Fold 5 (Train)]
    end
```

---

## Real-world Example
**Kaggle Competitions**
Winners don't just pick a model. They run massive Grid/Random searches over:
- `max_depth`: [3, 5, 7, 10, None]
- `learning_rate`: [0.01, 0.1, 0.5]
- `n_estimators`: [100, 200, 500]

Finding the perfect combo can move them from top 100 to top 10.

---

## Advantages
- Maximizes model potential.
- Prevents manual bias (guessing values).
- Cross-validation reduces overfitting to a specific test set.

## Limitations
- **Time-Consuming**: Grid Search can take days.
- **Computational Cost**: Requires significant CPU/GPU resources.

---

## Common Interview Questions
- **Difference between Parameters and Hyperparameters?**
- **Grid Search vs. Random Search?**
- **What is K-Fold Cross-Validation?**
- **Why not use all data for training?**

### Interview Answer Tips
- Mention that **Random Search** often outperforms Grid Search because not all hyperparameters are equally important.
- Explain that CV gives a **more reliable metric** than a single train/test split.

---

## Common Mistakes
- Tuning on the Test Set (Data Leakage). Always use a Validation set or CV.
- Over-tuning: Fitting hyperparameters too specifically to one dataset.

---

## Summary
Hyperparameter Tuning optimizes the "knobs" of ML models. Grid Search is exhaustive but slow; Random Search is faster. Cross-Validation ensures robust evaluation.

---

## Practice Questions
1. Is the learning rate a parameter or hyperparameter?
2. Why is Random Search often better than Grid Search?
3. What is the advantage of 5-Fold CV over 80/20 split?
4. Can you tune hyperparameters manually?
5. What is "Overfitting to the Validation Set"?

---

## Mini Project Ideas
1. **Grid Search**: Use `GridSearchCV` on a Random Forest. Find best `max_depth`.
2. **Learning Curves**: Plot training vs. validation accuracy as you increase training data.

---

## Further Reading
- [[25 Cross-Validation]]
- [[09 Bias-Variance Tradeoff]]
- [[13 Random Forest]]