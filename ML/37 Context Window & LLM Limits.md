# 37 Context Window & LLM Limits

tags:
#llm
#context-window
#genai
#placements
#interview

---

## Why this topic matters
Context windows define **how much information an LLM can process at once**. Understanding limits like token budgets, context constraints, and "Lost in the Middle" effects is crucial for building production AI systems. Companies will ask: *"How would you handle documents larger than the context window?"*

## Learning Objectives
- Understand what a context window is.
- Learn about token limits across different models.
- Understand the "Lost in the Middle" phenomenon.
- Learn strategies to handle long documents.

## Prerequisites
- [[35 LLM Fundamentals]]
- [[34 Tokenization]]

---

## Intuition
Imagine you have a **short-term memory** like a goldfish.

You can only hold **7 items** in your head at once:
- If someone lists 10 numbers, you'll forget the middle ones.
- You'll remember the **first few** (primacy effect).
- You'll remember the **last few** (recency effect).
- The **middle**? Gone.

LLMs have the same problem with their **context window**. They can only "pay attention" to a limited number of tokens at once.

---

## Detailed Explanation

### What is the Context Window?

The **context window** is the maximum number of tokens an LLM can process in a single request.

**It includes**:
- System prompt
- All conversation history
- Retrieved documents (in RAG)
- User's current input
- **Both input AND output**!

```
[System] [Conversation History] [Retrieved Docs] [User Input] → [Model Response]
     ↑                      Up to limit (e.g., 128K tokens)        ↑
                    CONTEXT WINDOW
```

### Context Window Sizes (2024-2025)

| Model | Context Window | Best For |
| :--- | :--- | :--- |
| **GPT-3.5** | 4K - 16K | Fast, cheap tasks |
| **GPT-4** | 8K - 128K | Complex reasoning |
| **GPT-4 Turbo** | 128K | Long documents |
| **Claude 2** | 100K | Long-form content |
| **Claude 3** | 200K | Book-length analysis |
| **Gemini 1.5** | 1M+ | Massive context |
| **Llama 3** | 8K | Open-source |

**Note**: Larger context ≠ better. Models often can't **use** all that context effectively.

### The "Lost in the Middle" Effect

**Discovery** (2023): LLMs don't pay equal attention to all parts of the context.

**Finding**:
- **Beginning of context**: High attention ✅
- **Middle of context**: Low attention ❌
- **End of context**: High attention ✅

```
Position in Context →    Beginning    Middle    End
Attention Level →          High        Low       High
Recall Accuracy →          85%         40%       80%
```

**Impact**: Important information in the middle might be **ignored**!

### Practical Example

```
[Document with 50K tokens]

User: "What is the budget mentioned in this report?"

If the budget is on page 25 (middle of context) → Model might miss it!
If the budget is on page 2 or page 49 → Model will find it!
```

### Strategies to Handle Long Documents

#### 1. Chunking + RAG

Don't send the whole document. Instead:
1. Split into chunks (1K tokens each).
2. Use embedding search to find **relevant chunks**.
3. Send only top-K chunks to the LLM.

```
100-page document → 200 chunks → Find 5 relevant chunks → Send 5K tokens to LLM
```

**Benefit**: Stays within context limit, focuses on relevant content.

#### 2. Map-Reduce

For summarization of long documents:
1. **Map**: Split document, summarize each chunk separately.
2. **Reduce**: Combine all chunk summaries into a final summary.

```
Chunks: [1] [2] [3] [4] [5]
        ↓   ↓   ↓   ↓   ↓
Summary: S1, S2, S3, S4, S5
        ↓
   Final Summary
```

#### 3. Hierarchical Processing

Process in layers:
1. Summarize each section.
2. Summarize the summaries.
3. Repeat until you have a single summary.

#### 4. Prioritize Context Placement

Place important information at the **beginning or end**:
- System prompt: Key instructions.
- Context start: Most relevant documents.
- Context end: User query with key details.

#### 5. Iterative Refinement

Multiple passes:
1. First pass: Get a rough answer.
2. Second pass: Ask for missing details.
3. Third pass: Refine and format.

---

## Real-world Example

**Legal Document Analysis**

A 200-page contract needs to be reviewed for specific clauses.

**Bad approach**: Send all 200 pages at once (even if it fits).
- Model will miss details in the middle.
- Slow and expensive.

**Good approach**:
1. Split into 1-page chunks.
2. Search for chunks mentioning "termination", "liability", "renewal".
3. Send top-10 relevant chunks to the LLM.
4. Ask specific questions about those chunks.

---

## Common Interview Questions
-   **What is a context window?**
-   **What happens if you exceed the context window?**
-   **What is the "Lost in the Middle" effect?**
-   **How do you handle documents larger than the context window?**
-   **Does a larger context window always mean better performance?**
-   **How would you design a system to analyze 1000-page documents?**

### Interview Answer Tips
-   Emphasize that **LLMs can't effectively use entire huge contexts**.
-   Mention that **RAG + chunking** is the standard solution.
-   Note that **placing important info at start/end** helps.

---

## Common Mistakes
-   Assuming the model uses all context equally.
-   Sending irrelevant documents just because they fit.
-   Not accounting for output tokens (they count too!).
-   Forgetting that conversation history accumulates.

---

## Summary
The context window is the maximum tokens an LLM can process. Models pay less attention to the middle of the context ("Lost in the Middle"). For long documents, use chunking + RAG, map-reduce, or hierarchical processing. Larger context windows don't guarantee better performance if the model can't attend to all content.

---

## Practice Questions
1. What is included in the context window?
2. Does the output count against the context limit?
3. What is the "Lost in the Middle" effect?
4. How would you summarize a 500-page book with an 8K context model?
5. Why might Claude with 100K context perform worse than expected?
6. Where should you place the most important information in a prompt?
7. What happens when you exceed the context window?
8. Is it better to use a smaller context with relevant content or max context with everything?

---

## Mini Project Ideas
1. **Context Experiment**: Test GPT with documents of varying lengths and measure accuracy.
2. **Chunking Strategy**: Implement different chunk sizes and compare retrieval quality.
3. **Position Testing**: Place key info at beginning, middle, and end of context. Compare recall.

---

## Further Reading
- [[35 LLM Fundamentals]]
- [[34 Tokenization]]
- [[50 RAG]]
- [[36 Prompt Engineering]]