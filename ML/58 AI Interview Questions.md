# 58 AI Interview Questions

tags:
#interview
#placements
#ml
#llm
#question-bank

---

## Why this topic matters
This is your final preparation guide. It consolidates the most frequently asked questions across all categories: ML Fundamentals, Deep Learning, GenAI/LLM, and Scenario-based problems.

## Learning Objectives
- Review key concepts across all topics.
- Practice answering common interview questions.
- Prepare for scenario-based problem-solving.

## Prerequisites
- All previous notes in this vault.

---

## Part 1: ML Fundamentals

### Basic Concepts
1. **What is the Bias-Variance Tradeoff?**
   - *Answer Hint*: Bias = underfitting (too simple), Variance = overfitting (too complex). Trade-off is finding the sweet spot.

2. **Explain the difference between Supervised and Unsupervised Learning.**
   - *Answer Hint*: Supervised has labels (prediction), Unsupervised finds patterns (clustering).

3. **What is Overfitting and how do you prevent it?**
   - *Answer Hint*: Model memorizes training data. Prevention: Regularization, Cross-Validation, More Data, Simpler Model.

4. **What is Cross-Validation and why use it?**
   - *Answer Hint*: K-Fold CV splits data into K parts, trains K times. Gives robust performance estimate.

5. **Precision vs. Recall: When to prioritize each?**
   - *Answer Hint*: Precision (Spam filter: don't mark legit mail as spam). Recall (Cancer detection: catch all cases).

### Algorithms
6. **How does a Decision Tree decide where to split?**
   - *Answer Hint*: Gini Impurity or Information Gain. Wants pure nodes.

7. **Explain Random Forest vs. Gradient Boosting.**
   - *Answer Hint*: RF = Bagging (parallel, reduces variance). GB = Boosting (sequential, reduces bias).

8. **What is the Kernel Trick in SVM?**
   - *Answer Hint*: Projects data to higher dimensions to make it linearly separable without computing the transformation.

9. **Why do we need to scale features for KNN but not for Decision Trees?**
   - *Answer Hint*: KNN uses distance (affected by scale). Trees split based on thresholds (scale-invariant).

10. **What is the Curse of Dimensionality?**
    - *Answer Hint*: As features increase, data becomes sparse, and models perform worse.

---

## Part 2: Deep Learning

11. **What is an Activation Function? Why is ReLU popular?**
    - *Answer Hint*: Adds non-linearity. ReLU is simple, fast, and solves vanishing gradient.

12. **Explain Backpropagation in simple terms.**
    - *Answer Hint*: Calculate error at output, propagate backwards to adjust weights using Gradient Descent.

13. **What is the Vanishing Gradient problem?**
    - *Answer Hint*: Gradients become tiny in deep networks, stopping early layers from learning. Solved by ReLU, Skip Connections.

14. **Difference between CNN and RNN?**
    - *Answer Hint*: CNN = Spatial data (images). RNN = Sequential data (text, time series).

15. **What is Transfer Learning?**
    - *Answer Hint*: Use a pre-trained model (e.g., ResNet) and fine-tune it on your data. Saves time and data.

---

## Part 3: Generative AI & LLMs

16. **What is an LLM and how does it work?**
    - *Answer Hint*: Transformer-based model that predicts next token. Uses Attention mechanism.

17. **Explain RAG (Retrieval-Augmented Generation).**
    - *Answer Hint*: Retrieve relevant docs from a vector DB, then pass them to LLM as context. Reduces hallucinations.

18. **What is the difference between Fine-tuning and Prompt Engineering?**
    - *Answer Hint*: Fine-tuning changes weights (expensive, specialized). Prompt engineering changes input (cheap, flexible).

19. **What are Embeddings?**
    - *Answer Hint*: Vector representations of text that capture semantic meaning.

20. **What is Attention?**
    - *Answer Hint*: Mechanism that lets the model focus on relevant parts of the input sequence.

21. **What are Hallucinations and how do you reduce them?**
    - *Answer Hint*: LLM making up facts. Reduce with RAG, better prompts, grounding.

22. **Explain the difference between Dense and Sparse Retrieval.**
    - *Answer Hint*: Dense = Vector search (semantic). Sparse = Keyword search (BM25).

23. **What is a Vector Database?**
    - *Answer Hint*: DB optimized for storing and searching high-dimensional vectors (embeddings).

24. **What is Prompt Engineering? Give examples.**
    - *Answer Hint*: Crafting inputs to get better outputs. Zero-shot, Few-shot, CoT.

25. **What are AI Agents?**
    - *Answer Hint*: LLMs with tools, memory, and planning. Can take actions, not just generate text.

---

## Part 4: Scenario-Based Questions

26. **Design a Spam Detection System.**
    - *Approach*: Naive Bayes or Logistic Regression. Features: Word frequency, sender reputation. Metric: Precision (don't block legit mail).

27. **How would you detect Fraud in Credit Card transactions?**
    - *Approach*: Imbalanced data → Use Anomaly Detection or Random Forest. Metric: Recall (catch all fraud). Use SMOTE for balancing.

28. **Design a Movie Recommendation System.**
    - *Approach*: Collaborative Filtering (user-user) or Content-Based (movie features). Mention Cold Start problem.

29. **You have a model with 99% accuracy but it's useless. Why?**
    - *Answer Hint*: Imbalanced dataset. 99% of data is one class. Check Confusion Matrix.

30. **How would you deploy an LLM for a customer service chatbot with low latency?**
    - *Approach*: Use a smaller model (distilled), cache common responses, use RAG for facts, batch requests if possible.

31. **Your model performed well in training but poorly in production. Why?**
    - *Answer Hint*: Data Drift (production data changed), Training-Serving Skew (different preprocessing), or Overfitting.

32. **How do you handle missing data in a dataset?**
    - *Approach*: Drop (if small), Impute (mean/median), or Predict missing values.

33. **Design a system to summarize long legal documents.**
    - *Approach*: RAG architecture. Chunk documents, embed, retrieve relevant sections, pass to LLM with "Summarize this" prompt.

34. **How would you detect if an AI model is biased?**
    - *Approach*: Evaluate on different demographic slices. Check for disparate impact. Use fairness metrics.

35. **You need to build a sentiment analysis tool for Twitter. What steps do you take?**
    - *Approach*: Collect tweets → Clean (remove emojis, URLs) → Embed → Train Classifier (or use LLM with prompts) → Evaluate F1-Score.

---

## Part 5: HR & Behavioral Questions

36. **Tell me about an AI project you worked on.**
    - *Tip*: Use STAR method (Situation, Task, Action, Result). Mention challenges and how you overcame them.

37. **How do you stay updated with AI trends?**
    - *Tip*: Mention specific blogs (HuggingFace, ArXiv), courses, or projects.

38. **Describe a time your model failed. What did you learn?**
    - *Tip*: Be honest. Focus on debugging and iteration.

39. **Why do you want to work in AI/ML?**
    - *Tip*: Connect personal passion with company's mission.

40. **Explain a complex AI concept to a non-technical person.**
    - *Tip*: Use analogies (e.g., "ML is like teaching a child...").

---

## Last-Minute Revision Checklist
- [ ] Bias-Variance Tradeoff
- [ ] Precision vs. Recall
- [ ] Overfitting prevention
- [ ] How Random Forest works
- [ ] CNN vs. RNN
- [ ] What is an LLM?
- [ ] RAG architecture
- [ ] Fine-tuning vs. Prompt Engineering
- [ ] What are Embeddings?
- [ ] AI Agents basics

---

## Further Reading
- [[01 Introduction to AI]]
- [[09 Bias-Variance Tradeoff]]
- [[35 LLM Fundamentals]]
- [[50 RAG]]
- [[53 AI Agents]]