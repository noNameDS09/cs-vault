# 33 Text Preprocessing

tags:
#nlp
#text-processing
#ml
#placements
#interview

---

## Why this topic matters
Before feeding text to any ML/NLP model, you must clean and prepare it. Raw text is messy: uppercase, punctuation, stopwords, typos. **Text Preprocessing** transforms raw text into a format that models can understand. This is the first step in every NLP pipeline.

## Learning Objectives
- Learn common text preprocessing steps.
- Understand tokenization basics.
- Know when to use each technique.
- Handle special cases (URLs, emojis, mentions).

## Prerequisites
- [[04 Python for ML]]
- [[05 Data Cleaning]]

---

## Intuition
Imagine you're a **Chef** preparing vegetables for a dish.

**Raw Text** = Vegetables straight from the garden (dirty, different sizes, some rotten parts).

**Preprocessing**:
- **Washing** → Removing special characters, URLs.
- **Cutting** → Splitting into words (tokenization).
- **Removing bad parts** → Removing stopwords, punctuation.
- **Uniform sizing** → Lowercasing, lemmatization.

Only then can you cook (train your model)!

---

## Detailed Explanation

### Common Preprocessing Steps

#### 1. Lowercasing
Convert all text to lowercase.
```python
"I Love NLP" → "i love nlp"
```
**Why**: "Love" and "love" should be treated the same.

**Exception**: Case-sensitive tasks (e.g., Named Entity Recognition).

#### 2. Remove Noise
Delete irrelevant content:
- **URLs**: `http://...`, `www....`
- **HTML Tags**: `<div>`, `</p>`
- **Special Characters**: `@`, `#`, `$` (unless important)
- **Punctuation**: `.`, `,`, `!`, `?`
- **Numbers**: Unless they carry meaning (e.g., "5 stars")

```python
"Check out https://example.com! 😊" → "Check out"
```

#### 3. Tokenization
Splitting text into individual words/tokens.
```python
"I love NLP" → ["I", "love", "NLP"]
```

**Types**:
- **Word Tokenization**: Split by words.
- **Character Tokenization**: Split by characters.
- **Subword Tokenization**: Split into subword units (used in BERT, GPT).

#### 4. Remove Stopwords
Filter out common words that carry little meaning:
- "the", "a", "is", "in", "at", "of", "to"

```python
["The", "cat", "is", "sitting"] → ["cat", "sitting"]
```

**Caution**: Sometimes stopwords matter! ("What is it?" vs. "What it is?")

#### 5. Stemming
Reduce words to their **root form** by chopping off endings.
```python
"running" → "run"
"runs" → "run"
"ran" → "ran" (not perfect!)
```

**Common Algorithm**: Porter Stemmer.

**Pros**: Fast, simple.
**Cons**: Can produce non-words (" univer " from "university").

#### 6. Lemmatization
Reduce words to their **dictionary root form** (lemma).
```python
"running" → "run"
"runs" → "run"
"ran" → "run" (correct!)
"better" → "good" (correct!)
```

**Pros**: Produces real words, more accurate.
**Cons**: Slower, requires vocabulary.

#### 7. Handle Special Cases
- **Emojis**: Remove or convert to text (😊 → "smiling face").
- **Mentions**: `@username` → remove or replace with `<USER>`.
- **Hashtags**: `#NLP` → "NLP" (remove #).
- **Repeated Characters**: "soooo" → "so" (normalize).

### Preprocessing Pipeline Example

```python
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

text = "I LOVED the movie! It was AMAZING 😊😍 https://example.com"

# 1. Lowercase
text = text.lower()

# 2. Remove URLs
text = re.sub(r'http\S+|www\S+', '', text)

# 3. Remove special characters & emojis
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 4. Tokenize
tokens = word_tokenize(text)

# 5. Remove stopwords
tokens = [w for w in tokens if w not in stopwords.words('english')]

# 6. Lemmatize
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(w) for w in tokens]

# Result: ['loved', 'movie', 'amazing']
```

---

## Real-world Example

**Twitter Sentiment Analysis**

Raw Tweet:
```
"OMG!!! Just watched the new Marvel movie 😍😍 Best movie EVER!!! 
 Highly recommend it to everyone 🎬🎬 
 #Marvel #Avengers https://t.co/xyz"
```

After Preprocessing:
```
['watch', 'new', 'marvel', 'movie', 'best', 'movie', 'ever', 
 'highly', 'recommend', 'everyone', 'marvel', 'avengers']
```

Now the model can focus on meaningful words instead of noise.

---

## Advantages
- **Reduces Noise**: Removes irrelevant characters and words.
- **Standardizes**: "Running", "RUNNING", "ran" all become "run".
- **Smaller Vocabulary**: Fewer unique words = faster training.
- **Better Performance**: Models learn patterns more effectively.

## Limitations
- **Information Loss**: Removing stopwords can sometimes lose meaning.
- **Over-Normalization**: Lemmatization might merge unrelated words.
- **Context Loss**: "not good" → "good" (negation lost!).
- **Language-Specific**: English tools don't work for other languages.

---

## Common Interview Questions
- **What are the steps in text preprocessing?**
- **Difference between Stemming and Lemmatization?**
- **When should you NOT remove stopwords?**
- **What is tokenization?**
- **How do you handle URLs and emojis in text?**
- **Why is lowercasing important?**

### Interview Answer Tips
- Emphasize that preprocessing depends on the **task** (e.g., don't lemmatize for NER).
- Mention that **modern LLMs** often skip preprocessing (they handle raw text).
- Note that **stemming is faster**, **lemmatization is more accurate**.

---

## Common Mistakes
- Applying all steps blindly without considering the task.
- Removing punctuation in tasks where it matters (e.g., sentiment: "Good!" vs. "Good?").
- Not handling negation (words like "not", "never" should often be kept).
- Forgetting to handle out-of-vocabulary words.

---

## Summary
Text preprocessing cleans and standardizes raw text for ML models. Steps include lowercasing, removing noise, tokenization, stopword removal, and stemming/lemmatization. The exact pipeline depends on the task and language.

---

## Practice Questions
1. What is the difference between stemming and lemmatization?
2. When would you NOT remove stopwords?
3. Why do we lowercase text?
4. What is a token in NLP?
5. How would you handle the phrase "not good" during preprocessing?
6. What happens if you don't remove URLs from text?
7. Which is better: stemming or lemmatization?
8. How do modern LLMs handle preprocessing?

---

## Mini Project Ideas
1. **Tweet Cleaner**: Write a Python script to clean tweets (remove URLs, mentions, hashtags).
2. **Stemmer vs. Lemmatizer**: Compare output of both on a sample text.
3. **Stopword Analysis**: Test sentiment analysis with and without stopword removal.

---

## Further Reading
- [[05 Data Cleaning]]
- [[34 Tokenization]]
- [[38 Word2Vec]]
- [[39 Embeddings]]