# 34 Tokenization

tags:
#nlp
#tokenization
#llm
#placements
#interview

---

## Why this topic matters
Tokenization is the **first step** in any NLP or LLM pipeline. It converts text into smaller units (tokens) that models can process. Understanding tokenization is crucial for working with LLMs, where **token count = cost**.

## Learning Objectives
- Understand what tokens are.
- Learn different tokenization strategies.
- Understand subword tokenization (used in BERT, GPT).
- Know how tokenization affects LLM costs.

## Prerequisites
- [[33 Text Preprocessing]]
- [[35 LLM Fundamentals]]

---

## Intuition
Imagine you're breaking a **chocolate bar** into pieces.

**Different ways to break it**:
- **Whole bar**: "One big piece" (Word-level)
- **Squares**: "Individual squares" (Subword-level)
- **Cocoa molecules**: "Tiny pieces" (Character-level)

**Tokenization** is deciding how to break text into "pieces" that the model can digest.

- **Too big** (whole sentences): Can't learn patterns.
- **Too small** (characters): Too many pieces, loses meaning.
- **Just right** (subwords): Balances meaning and flexibility.

---

## Detailed Explanation

### What is a Token?

A **token** is a chunk of text that the model processes as a single unit.

**Examples**:
- `"cat"` → 1 token
- `"unbelievable"` → Could be 1 token or multiple (`"un" + "believ" + "able"`)
- `"I'm"` → Could be 1 or 2 tokens (`"I"` + `"'m"`)

**Rule of thumb**: ~4 characters ≈ 1 token (in English).

### Tokenization Strategies

#### 1. Word Tokenization
Split by spaces/punctuation.
```
Text: "I love NLP"
Tokens: ["I", "love", "NLP"]
```

**Pros**: Simple, interpretable.
**Cons**: 
- Large vocabulary (every word needs a token).
- Can't handle unknown words ("ChatGPT" not in vocab → problem!).

#### 2. Character Tokenization
Split into individual characters.
```
Text: "cat"
Tokens: ["c", "a", "t"]
```

**Pros**: 
- Small vocabulary (just all characters).
- Handles any word (even new ones).

**Cons**: 
- Too many tokens (long sequences).
- Loses word meaning ("cat" vs. "tac" have same characters).

#### 3. Subword Tokenization ⭐ (Used in BERT, GPT)

The **best of both worlds**. Frequent words are whole tokens; rare words are split into subwords.

**Algorithms**:
- **BPE (Byte-Pair Encoding)**: Used in GPT models.
- **WordPiece**: Used in BERT.
- **SentencePiece**: Used in T5, multilingual models.

**How BPE works** (simplified):
1. Start with all characters as tokens.
2. Find most common pair: `"t" + "h"` → `"th"`.
3. Merge them. Repeat.
4. After many iterations: common words are whole, rare words are subwords.

**Example**:
```
"unbelievable" → ["un", "believ", "able"]  (3 tokens)
"believe" → ["believ", "e"]               (2 tokens)
"un" → ["un"]                              (1 token)
```

**Key insight**: Subwords capture **morphemes** (meaning units).

### Vocabulary

Tokenizers have a **vocabulary** (vocab): a fixed list of known tokens.

- **GPT-3**: ~50,000 tokens in vocab.
- **BERT**: ~30,000 tokens.

**Out-of-Vocabulary (OOV)**: What if a word isn't in vocab?
- **Word tokenization**: Fails (unk token).
- **Subword tokenization**: Splits into known subwords ("ChatGPT" → ["Chat", "G", "PT"]).

### Tokenization in LLMs

**Important**: LLMs have their own tokenizer!

```python
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
text = "Transformers are powerful"
tokens = tokenizer.encode(text)
print(tokens)        # [18001, 432, 2659, 3166]
print(len(tokens))   # 4 tokens
```

**Cost implication**: LLM APIs charge per token!
- Input: 1000 tokens
- Output: 500 tokens
- **Total cost**: Based on 1500 tokens.

---

## Real-world Example

**ChatGPT Token Counting**

User input: 
```
"Write a 100-word essay about artificial intelligence and its impact on society."
```

Tokenizer breaks this into ~18 tokens:
```
["Write", " a", " 100", "-word", " essay", " about", " artificial", 
 " intelligence", " and", " its", " impact", " on", " society", "."]
```

**OpenAI API costs** (as of 2024):
- GPT-4: $0.03 per 1K input tokens.
- 100 tokens = $0.003 (fraction of a cent).
- 1 million tokens = $30.

---

## Advantages
- **Handles unknown words**: Subword tokenization works on any text.
- **Efficient**: Balances vocabulary size and sequence length.
- **Universal**: Works across languages (mostly).
- **Reversible**: Can reconstruct original text from tokens.

## Limitations
- **Vocabulary constraints**: Limited to pre-defined tokens.
- **Language bias**: English-centric tokenizers struggle with other languages.
- **Edge cases**: Punctuation, emojis can be inconsistent.
- **Cost**: More tokens = higher API costs.

---

## Common Interview Questions
- **What is tokenization?**
- **Difference between word, character, and subword tokenization?**
- **Why do LLMs use subword tokenization?**
- **What is BPE (Byte-Pair Encoding)?**
- **How does tokenization affect LLM costs?**
- **What happens to unknown words?**

### Interview Answer Tips
- Mention that **subword is the industry standard** for LLMs.
- Explain that **1 token ≈ 4 characters** in English.
- Note that **tokenizer choice affects model performance**.

---

## Common Mistakes
- Assuming 1 word = 1 token (not true for LLMs!).
- Not accounting for token count when using paid APIs.
- Ignoring that different models have different tokenizers.
- Forgetting that tokenization is reversible.

---

## Summary
Tokenization breaks text into processable units. Word tokenization is simple but inflexible. Character tokenization handles unknown words but is inefficient. Subword tokenization (BPE, WordPiece) is the best compromise and powers modern LLMs. Token count directly impacts LLM API costs.

---

## Practice Questions
1. How many tokens is "unbelievable" likely to be?
2. What is the main advantage of subword tokenization?
3. Does "ChatGPT" count as 1 or multiple tokens?
4. Why can't we use word tokenization for large language models?
5. What is BPE and how does it work?
6. How would you estimate the cost of processing 10,000 documents?
7. What happens if a word isn't in the tokenizer's vocabulary?
8. Why do different LLMs have different token counts for the same text?

---

## Mini Project Ideas
1. **Token Counter**: Build a web app that counts tokens for any text (using HuggingFace tokenizers).
2. **Tokenizer Comparison**: Compare how GPT-2, BERT, and T5 tokenize the same sentence.
3. **Cost Calculator**: Build a tool that estimates LLM API costs based on input text.

---

## Further Reading
- [[33 Text Preprocessing]]
- [[35 LLM Fundamentals]]
- [[36 Prompt Engineering]]
- [[39 Embeddings]]