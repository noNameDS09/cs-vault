# 18 Support Vector Machine (SVM)

tags:
#ml
#classification
#placements
#interview

---

## Why this topic matters
SVM is a powerful classifier that finds the "best boundary" between classes. It's especially effective in high-dimensional spaces and is a common interview topic for understanding margins and kernels.

## Learning Objectives
- Understand the concept of Margin.
- Learn what Support Vectors are.
- Understand the Kernel Trick.

## Prerequisites
- [[11 Logistic Regression]]
- Basic Geometry.

---

## Intuition
Imagine you have red and blue balls on a floor.
- **Logistic Regression**: Draws a line somewhere in the middle.
- **SVM**: Draws the line that is **as far as possible** from both the nearest red ball and the nearest blue ball.

SVM doesn't care about all the balls. It only cares about the few balls closest to the boundary. These are called **Support Vectors** because they "support" or hold up the wall.

---

## Detailed Explanation

### 1. Maximum Margin Classifier
SVM finds a hyperplane (line in 2D, plane in 3D) that maximizes the **Margin** (the distance between the hyperplane and the nearest data points of any class).

$$Margin = \frac{2}{||w||}$$

- **Hyperplane**: The decision boundary.
- **Support Vectors**: The data points that lie on the margin lines.

### 2. Soft Margin vs. Hard Margin
- **Hard Margin**: No points allowed inside the margin. (Only works if data is perfectly separable).
- **Soft Margin**: Allows some points to be inside the margin or on the wrong side. Controlled by **C parameter**.
  - **Large C**: Strict (Low Bias, High Variance).
  - **Small C**: Lenient (High Bias, Low Variance).

### 3. The Kernel Trick
What if the data is not linearly separable? (e.g., a red circle inside a blue ring).

SVM uses a **Kernel Function** to project data into a higher dimension where a line can separate it.
- **Linear Kernel**: No projection (fast).
- **RBF Kernel (Radial Basis Function)**: Projects to infinite dimensions (most common).
- **Polynomial Kernel**: Projects to polynomial space.

```mermaid
flowchart TD
    subgraph "2D Space (Not Separable)"
    A[Red Circle inside Blue Ring]
    end
    A --> Kernel[Apply Kernel Trick]
    Kernel --> subgraph "3D Space (Separable)"
    B[Red Cone above Blue Plane]
    end
    B --> Plane[Cut with Hyperplane]
```

---

## Real-world Example
**Handwriting Recognition**
SVM was the state-of-the-art for digit recognition before Deep Learning. It effectively separated images of "3" from "8" in high-dimensional pixel space.

---

## Advantages
- **Effective in High Dimensions**: Works well when features > samples.
- **Memory Efficient**: Only uses Support Vectors at prediction time.
- **Versatile**: Can use different kernels for non-linear problems.

## Limitations
- **Slow Training**: $O(N^2)$ to $O(N^3)$ complexity. Not for large datasets.
- **Sensitive to Noise**: Overlapping classes reduce performance.
- **Black Box**: Hard to interpret with non-linear kernels.

---

## Common Interview Questions
- **What are Support Vectors?**
- **What is the Kernel Trick?**
- **What does the C parameter do?**
- **Why is SVM not suitable for large datasets?**

### Interview Answer Tips
- Mention that SVM tries to **maximize the margin**, not just separate.
- Explain that **Kernels** allow SVM to work in higher dimensions without explicitly computing them.

---

## Common Mistakes
- Using SVM on massive datasets (too slow).
- Forgetting to scale features (SVM is distance-based).
- Using RBF kernel without tuning Gamma.

---

## Summary
SVM finds the optimal hyperplane that maximizes the margin between classes. Using the Kernel Trick, it can solve non-linear problems.

---

## Practice Questions
1. What are Support Vectors?
2. What happens to the margin if you increase C?
3. Why use RBF kernel?
4. Is SVM sensitive to outliers?
5. What is the time complexity of SVM training?

---

## Mini Project Ideas
1. **Kernel Visualization**: Plot decision boundaries of Linear vs. RBF kernel on a toy dataset.
2. **OCR**: Use SVM on a small subset of MNIST to classify digits.

---

## Further Reading
- [[11 Logistic Regression]]
- [[17 PCA]]
- [[26 Regularization]]