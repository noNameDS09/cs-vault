# 15 Naive Bayes

tags:
#ml
#probabilistic
#nlp
#placements
#interview

---

## Why this topic matters
Naive Bayes is a probabilistic algorithm based on **Bayes' Theorem**. It's incredibly efficient for text classification (Spam Detection, Sentiment Analysis) and remains a strong baseline for NLP tasks.

## Learning Objectives
- Understand Bayes' Theorem.
- Learn why it's called "Naive."
- Understand its application in NLP.

## Prerequisites
- Basic probability knowledge.

---

## Intuition
Imagine you are a **Detective** trying to guess if an email is Spam.
You know that:
1. 90% of Spam emails contain the word "Winner."
2. Only 1% of Normal emails contain "Winner."
3. You see the word "Winner" in this email.

**Naive Bayes** calculates: *"Given that 'Winner' is present, what is the probability this is Spam?"*

It's "Naive" because it assumes every word is independent. It thinks "Winner" and "Lottery" appearing together is just a coincidence, not a phrase.

---

## Detailed Explanation

### 1. Bayes' Theorem
$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$

In ML terms:
$$P(Spam | Words) = \frac{P(Words | Spam) \times P(Spam)}{P(Words)}$$

- **Posterior**: $P(Spam|Words)$ - What we want to find.
- **Likelihood**: $P(Words|Spam)$ - How often these words appear in spam.
- **Prior**: $P(Spam)$ - Overall chance of any email being spam.

### 2. The "Naive" Assumption
It assumes **Conditional Independence**.
$$P(Words | Spam) = P(W_1 | Spam) \times P(W_2 | Spam) \times ...$$
This simplifies calculation massively, even though words are actually related (context).

### 3. Variants
- **Gaussian**: For continuous numerical data (assumes Normal distribution).
- **Multinomial**: For word counts (Document Classification).
- **Bernoulli**: For binary features (Word present or not).

### 4. Laplace Smoothing
What if a word never appears in training data? Probability = 0, which kills the whole product.
**Smoothing** adds a small constant (usually +1) to counts to avoid zero probabilities.

---

## Real-world Example
**Gmail Spam Filter**
Gmail uses Naive Bayes (as part of a larger system) to scan emails.
- It calculates probabilities for words like "Free," "Click Here," "Urgent."
- If the combined probability of Spam > 90%, it moves the email to the Spam folder.

---

## Advantages
- **Fast**: Extremely efficient training and prediction.
- **Small Data**: Works well with limited training data.
- **Text**: Excellent for high-dimensional text data.

## Limitations
- **Independence Assumption**: It cannot learn that "New York" is a city, not two separate words "New" and "York."
- **Zero Frequency**: Needs smoothing for unseen words.

---

## Common Interview Questions
- **Why is Naive Bayes called "Naive"?**
- **What is Bayes' Theorem?**
- **Why is it good for text classification?**
- **What is Laplace Smoothing?**

### Interview Answer Tips
- Mention that despite being "Naive," it works surprisingly well in practice.
- Explain that it's a **Generative Model** (learns how data is generated).

---

## Common Mistakes
- Using it for data where features are highly correlated (violates assumption).
- Forgetting smoothing (leads to errors on unseen words).

---

## Summary
Naive Bayes uses Bayes' Theorem to calculate class probabilities. It assumes feature independence, which is "naive" but makes it incredibly fast and effective for text classification.

---

## Practice Questions
1. What is the "Naive" assumption in Naive Bayes?
2. How do you handle a word that never appeared in training?
3. Why is Naive Bayes good for multi-class problems?
4. Can Naive Bayes be used for numeric data?
5. What is the difference between Prior and Posterior?

---

## Mini Project Ideas
1. **Spam Classifier**: Build a Naive Bayes spam detector using the SMS Spam Collection dataset.
2. **Sentiment Analysis**: Classify movie reviews as Positive or Negative.

---

## Further Reading
- [[33 Text Preprocessing]]
- [[39 Embeddings]]
- [[11 Logistic Regression]]