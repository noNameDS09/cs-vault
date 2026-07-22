# 39 Embeddings

tags:
#embeddings
#nlp
#llm
#vector-search
#placements
#interview

---

## Why this topic matters
Embeddings are the **universal language** of AI. They convert anything (text, images, audio) into vectors that capture meaning. Embeddings power **semantic search**, **RAG systems**, **recommendation engines**, and **LLMs**. Understanding embeddings is crucial for any AI role.

## Learning Objectives
- Understand what embeddings are and why we need them.
- Learn about word, sentence, and document embeddings.
- Understand cosine similarity for finding similar items.
- Know modern embedding models (sentence-transformers, etc.).

## Prerequisites
- [[33 Text Preprocessing]]
- [[34 Tokenization]]
- [[38 Word2Vec]]
- [[51 Vector Databases]]

---

## Intuition
Imagine you're organizing **movies** in a "concept space".

Each movie gets coordinates based on its themes:
- **Action score**: 0 to 1
- **Comedy score**: 0 to 1
- **Romance score**: 0 to 1
- **Sci-Fi score**: 0 to 1

**Die Hard**: [0.9, 0.1, 0.0, 0.3] (action, low comedy, no romance, some sci-fi)
**The Hangover**: [0.3, 0.9, 0.2, 0.0]
**Titanic**: [0.2, 0.3, 0.9, 0.0]

Movies close together in this space are **similar**!

**Embeddings** are just this, but with **hundreds of dimensions** and learned automatically by neural networks.

---

## Detailed Explanation

### What are Embeddings?

Embeddings are **dense vector representations** that capture semantic meaning.

- **Text**: "I love cats" → `[0.2, -0.4, 0.8, 0.1, ..., 0.5]` (384 or 768 dimensions)
- **Images**: Picture of cat → `[0.3, -0.1, 0.9, 0.2, ..., 0.6]`
- **Audio**: Sound of meowing → `[0.4, -0.3, 0.7, 0.0, ..., 0.4]`

**Key property**: Similar items have **similar vectors** (close in vector space).

### Types of Embeddings

#### 1. Word Embeddings

Each word gets a vector.

- **Word2Vec**: 300 dimensions, static (one vector per word).
- **GloVe**: Global vectors for word representation.
- **FastText**: Includes subword information.

**Limitation**: "bank" (river) and "bank" (money) have the same vector.

#### 2. Sentence/Document Embeddings

Entire sentences or documents get a single vector.

**Models**:
- **Sentence-BERT (SBERT)**: Optimized for sentence similarity.
- **Universal Sentence Encoder (USE)**: Google's general-purpose encoder.

**Use case**: Semantic search, clustering documents.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = [
    "The cat sat on the mat",
    "A kitten rested on the rug",
    "The dog barked loudly"
]

embeddings = model.encode(sentences)

# embeddings[0] and embeddings[1] will be very similar
# embeddings[2] will be different
```

#### 3. Contextual Embeddings (BERT, GPT)

Modern embeddings that **depend on context**.

- **BERT**: Each word's vector depends on the entire sentence.
- **GPT**: Embeddings are contextual and autoregressive.

**Example**:
- "I went to the **bank** to deposit money" → Different vector than:
- "I sat by the river **bank**"

**Advantage**: Handles polysemous words (words with multiple meanings).

### Similarity Metrics

How do we measure if two embeddings are "similar"?

#### Cosine Similarity (Most Common)

Measures the **angle** between two vectors.

```
Cosine Similarity = (A · B) / (||A|| × ||B||)
```

**Range**: -1 (opposite) to +1 (identical), with 0 meaning orthogonal.

```
"A cat is cute" vs. "A kitten is adorable" → 0.85 (very similar)
"A cat is cute" vs. "The stock market crashed" → 0.10 (not similar)
```

#### Other Metrics:
- **Dot Product**: Faster, but depends on vector magnitude.
- **Euclidean Distance**: Actual distance in space.

### Popular Embedding Models

| Model | Dimensions | Use Case | Speed |
| :--- | :--- | :--- | :--- |
| **all-MiniLM-L6-v2** | 384 | General purpose, fast | Very Fast |
| **all-mpnet-base-v2** | 768 | High quality | Medium |
| **text-embedding-ada-002** | 1536 | OpenAI API | API Call |
| **BGE-Large** | 1024 | State-of-the-art | Slow |
| **E5-Large** | 1024 | Multilingual | Slow |

### Embeddings in RAG Systems

Embeddings are **critical** for RAG ([[50 RAG]]):

```
User Query → Embedding Model → Query Vector
                                 ↓
Documents → Embedding Model → Document Vectors → Vector Database
                                 ↓
                    Find vectors closest to Query Vector
                                 ↓
                         Return top K documents
```

---

## Real-world Example

**Semantic Search in an E-commerce App**

User searches: "comfortable running shoes"

**Keyword search**: Only finds products with "comfortable", "running", "shoes".

**Semantic search with embeddings**:
- Finds products with "cushioned jogging sneakers" (no keyword match, but semantically similar!)
- Embeddings capture that:
  - "comfortable" ≈ "cushioned"
  - "running" ≈ "jogging"
  - "shoes" ≈ "sneakers"

---

## Advantages
- **Semantic Understanding**: Captures meaning, not just keywords.
- **Cross-Modal**: Can compare text, images, audio in same space.
- **Efficient**: Similarity search is fast (with vector databases).
- **Transferable**: Pre-trained embeddings work out-of-the-box.

## Limitations
- **Dimensionality**: High-dimensional vectors (384-1536) require specialized databases.
- **Domain-Specific**: General embeddings may not work for specialized domains (medical, legal).
- **Bias**: Embeddings can inherit biases from training data.
- **Cost**: Generating embeddings for large datasets is expensive.

---

## Common Interview Questions
- **What are embeddings?**
- **Difference between word and sentence embeddings?**
- **How do you find similar documents using embeddings?**
- **What is cosine similarity?**
- **Why are contextual embeddings better than Word2Vec?**
- **How are embeddings used in RAG systems?**
- **What's the difference between BERT and Word2Vec embeddings?**

### Interview Answer Tips
- Emphasize that embeddings capture **semantic meaning**, not just syntax.
- Mention that **cosine similarity** is the standard way to compare embeddings.
- Explain that modern embeddings are **contextual** (unlike Word2Vec).

---

## Common Mistakes
- Thinking 1 word = 1 embedding (modern LLMs use subword embeddings).
- Using Euclidean distance instead of cosine similarity.
- Not normalizing embeddings before similarity search.
- Forgetting that embeddings are just numbers (no inherent meaning without context).

---

## Summary
Embeddings convert text (or images, audio) into dense vectors that capture semantic meaning. Similar items have similar vectors. Cosine similarity measures how similar two embeddings are. Modern contextual embeddings (BERT, SBERT) are better than static ones (Word2Vec). Embeddings are fundamental to semantic search and RAG systems.

---

## Practice Questions
1. What do embeddings represent?
2. How is cosine similarity calculated?
3. Why can't we use Word2Vec for RAG systems?
4. What's the difference between word and sentence embeddings?
5. Why are contextual embeddings better?
6. What would be the cosine similarity between identical documents?
7. Can embeddings from different models be compared?
8. How do you handle out-of-vocabulary words with embeddings?

---

## Mini Project Ideas
1. **Semantic Search**: Build a search engine for documents using sentence embeddings.
2. **Recommendation System**: Recommend similar articles based on embedding similarity.
3. **Embedding Visualization**: Use t-SNE to visualize embeddings in 2D.
4. **Cross-Modal Search**: Use CLIP embeddings to search images with text.

---

## Further Reading
- [[34 Tokenization]]
- [[38 Word2Vec]]
- [[50 RAG]]
- [[51 Vector Databases]]
- [[52 Fine-tuning vs Prompt Engineering]]