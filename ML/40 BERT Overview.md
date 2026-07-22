# 40 BERT Overview

tags:
#nlp
#bert
#transformers
#llm
#placements
#interview

---

## Why this topic matters
**BERT** (Bidirectional Encoder Representations from Transformers) revolutionized NLP in 2018 and remains foundational for understanding modern language models. While newer models exist, BERT introduced key concepts (bidirectional context, masked language modeling) that are still relevant. Interviewers expect you to understand BERT's architecture and contributions.

## Learning Objectives
- Understand what BERT is and why it was groundbreaking.
- Learn about bidirectional context.
- Understand Masked Language Modeling (MLM).
- Know BERT's limitations and successors.

## Prerequisites
- [[26 Transformers Overview]]
- [[35 LLM Fundamentals]]
- [[39 Embeddings]]

---

## Intuition
Imagine you're filling in a blank in a sentence:

*"I love to eat ____ with my coffee."*

**Unidirectional models (before BERT)**: Read only left-to-right (or right-to-left).
- They see: "I love to eat" → predict next word.
- They **don't see** "with my coffee" when predicting the blank.

**BERT (Bidirectional)**: Reads **both directions at once**.
- It sees: "I love to eat [MASK] with my coffee."
- It uses **full context** from both sides to predict "cookies" or "croissants."

BERT is like a reader who can look at the **entire sentence simultaneously**, not just word by word.

---

## Detailed Explanation

### What is BERT?

**BERT** = **B**idirectional **E**ncoder **R**epresentations from **T**ransformers

Created by Google (2018), BERT is a **Transformer Encoder-based** model that:
- Reads text **bidirectionally** (both left and right context).
- Uses **Masked Language Modeling (MLM)** for pretraining.
- Generates **contextual embeddings** (word vectors depend on full sentence).

### Key Innovations

#### 1. Bidirectional Context

Before BERT:
- **GPT**: Left-to-right (can't see future words).
- **ELMo**: Separate left-to-right and right-to-left, then combined.

**BERT**: Truly bidirectional. Sees **all words at once**.

```
Sentence: "I went to the bank to deposit money."

Word: "bank"
Left context: "I went to the"
Right context: "to deposit money"
BERT sees: BOTH → Knows it's a financial bank, not a river bank.
```

#### 2. Masked Language Modeling (MLM)

**Pretraining Task**:
1. Take a sentence.
2. Randomly mask 15% of words: `"I love [MASK] cookies."`
3. Model predicts the masked words.

**Why MLM?**
- Forces model to understand **context from both sides**.
- Learns deep bidirectional representations.

**Problem with standard L-R models**: They can't do this because they haven't seen the "future" words yet.

#### 3. Next Sentence Prediction (NSP)

**Secondary Pretraining Task**:
- Given two sentences, predict if Sentence B follows Sentence A.

**Example**:
- Sentence A: "I went to the store."
- Sentence B: "I bought milk." → **IsNext: Yes**
- Sentence B: "The sky is blue." → **IsNext: No**

**Purpose**: Helps BERT understand relationships between sentences (useful for Q&A, NLI).

**Note**: Later research showed NSP wasn't as helpful as thought. Newer models (RoBERTa) removed it.

### BERT Architecture

```mermaid
graph TD
    subgraph "Input"
    Tokens[Token Embeddings]
    Position[Position Embeddings]
    Segment[Segment Embeddings]
    end
    
    Tokens & Position & Segment --> Add[Add & LayerNorm]
    Add --> Transformer[Transformer Encoder Layers (12 or 24)]
    Transformer --> Output[Contextual Embeddings]
    
    subgraph "Output Heads"
    MLM[Masked LM Head]
    NSP[Next Sentence Prediction Head]
    end
    
    Output --> MLM
    Output --> NSP
```

**Variants**:
- **BERT-Base**: 12 layers, 768 hidden, 12 attention heads, 110M parameters.
- **BERT-Large**: 24 layers, 1024 hidden, 16 attention heads, 340M parameters.

### BERT Variants and Successors

| Model | Improvement | Key Change |
| :--- | :--- | :--- |
| **BERT** (2018) | Original | Bidirectional, MLM, NSP |
| **RoBERTa** (2019) | Better training | Removed NSP, trained longer, more data |
| **DistilBERT** (2019) | Faster, smaller | Distilled from BERT (40% smaller, 60% faster) |
| **ALBERT** (2019) | More efficient | Parameter sharing across layers |
| **ELECTRA** (2020) | Faster training | Replaced MLM with discrimination task |

### How to Use BERT

**Option 1: Feature Extraction**
- Use BERT to generate embeddings.
- Feed embeddings to a downstream model (e.g., classifier).

**Option 2: Fine-Tuning** (Most Common)
- Add a task-specific layer (e.g., classification head).
- Fine-tune entire BERT + head on your task.

```python
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Fine-tune on sentiment analysis dataset
```

---

## Real-world Example

**Google Search (2019)**
- Google integrated BERT into Search to better understand queries.
- Example query: "2019 brazil traveler to usa need a visa"
- **Before BERT**: Focused on "traveler to usa", missed the direction.
- **With BERT**: Understood "brazil traveler TO usa" (not "usa traveler to brazil").
- **Result**: More accurate search results for 10% of queries.

---

## Advantages
- **Bidirectional Context**: Captures full sentence meaning.
- **State-of-the-Art**: Dominated NLP benchmarks (GLUE, SQuAD) on release.
- **Transferable**: One pretrained model works for many tasks.
- **Contextual**: Handles polysemous words (words with multiple meanings).

## Limitations
- **Computationally Heavy**: 110M+ parameters, slow inference.
- **Fixed Context**: Limited to 512 tokens.
- **MLM Gap**: Masking during training but not inference creates a mismatch.
- **Superseded**: Newer models (RoBERTa, DeBERTa, LLMs) are better.

---

## Common Interview Questions
- **What is BERT and why was it groundbreaking?**
- **What does "bidirectional" mean in BERT?**
- **Explain Masked Language Modeling.**
- **What is Next Sentence Prediction?**
- **Difference between BERT and GPT?**
- **What are some BERT variants?**
- **How do you use BERT for a classification task?**

### Interview Answer Tips
- Emphasize that **bidirectional** was the key innovation.
- Mention that BERT uses **only the Encoder** part of Transformers.
- Note that **GPT is Decoder-only** (unidirectional), **BERT is Encoder-only** (bidirectional).

---

## Common Mistakes
- Thinking BERT can generate text (it can't; it's Encoder-only).
- Confusing BERT with GPT (unidirectional vs. bidirectional).
- Forgetting that BERT has a 512 token limit.
- Not knowing that newer models improved on BERT.

---

## Summary
BERT is a bidirectional Transformer Encoder model that uses Masked Language Modeling to learn deep contextual representations. It reads text from both directions simultaneously, capturing full sentence context. BERT dominated NLP in 2018-2020 but has been superseded by more efficient models. It's Encoder-only (can't generate text), limited to 512 tokens, and is best used via fine-tuning for downstream tasks.

---

## Practice Questions
1. What does bidirectional mean in the context of BERT?
2. How does Masked Language Modeling work?
3. Why can't BERT generate text like GPT?
4. What is the difference between BERT-Base and BERT-Large?
5. What is the purpose of Next Sentence Prediction?
6. Why was RoBERTa better than BERT?
7. What is the maximum sequence length for BERT?
8. How do you fine-tune BERT for a new task?

---

## Mini Project Ideas
1. **Sentiment Analysis**: Fine-tune BERT on a movie review dataset.
2. **BERT vs. LSTM**: Compare BERT and LSTM on the same text classification task.
3. **Mask Filling**: Use a pretrained BERT to fill in masked words in custom sentences.

---

## Further Reading
- [[26 Transformers Overview]]
- [[35 LLM Fundamentals]]
- [[39 Embeddings]]
- [[34 Tokenization]]