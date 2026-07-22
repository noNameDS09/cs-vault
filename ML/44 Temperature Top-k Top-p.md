# 44 Temperature, Top-k, Top-p Sampling

tags:
#llm
#sampling
#hyperparameters
#genai
#placements
#interview

---

## Why this topic matters
LLMs don't always output the same response for the same input. **Sampling parameters** (Temperature, Top-k, Top-p) control how **creative** vs. **deterministic** the output is. Understanding these is crucial for tuning LLM behavior for different use cases (creative writing vs. code generation vs. Q&A).

## Learning Objectives
- Understand how LLMs generate tokens.
- Learn about Temperature and its effect on creativity.
- Understand Top-k and Top-p (Nucleus) sampling.
- Know when to use each parameter.

## Prerequisites
- [[35 LLM Fundamentals]]
- [[36 Prompt Engineering]]

---

## Intuition
Imagine you're at an **ice cream shop** choosing flavors.

**Greedy (No Sampling)**:
- You **always** pick your favorite flavor (Chocolate).
- **Result**: Predictable, but boring.

**Temperature (Creativity Knob)**:
- **Low Temp (0.1)**: You mostly pick Chocolate, occasionally Vanilla.
- **High Temp (1.5)**: You might pick Chocolate... or try Wasabi, Pickle, or Sardine flavors!

**Top-k**:
- You only consider your **Top 5** favorite flavors. Ignore everything else.

**Top-p (Nucleus)**:
- You consider flavors until they add up to **90% probability**. If Chocolate + Vanilla + Strawberry = 90%, you pick from those three.

**Sampling parameters** control how "adventurous" the LLM is when choosing the next word.

---

## Detailed Explanation

### How LLMs Generate Tokens

At each step, an LLM outputs a **probability distribution** over all possible next tokens.

Example:
```
Input: "The cat sat on the"

Possible next tokens:
- "mat" (40%)
- "couch" (25%)
- "floor" (15%)
- "bed" (10%)
- "table" (5%)
- ... other words (5%)
```

**Question**: Which token do we pick?

### Sampling Strategies

#### 1. Greedy Decoding (No Sampling)

**Method**: Always pick the **most probable** token.

```
Pick: "mat" (40% - highest probability)
```

**Pros**: Deterministic, consistent.
**Cons**: Boring, repetitive, no creativity.

**Use Case**: Code generation, math problems, factual Q&A.

#### 2. Temperature Sampling

**Method**: Adjust the probability distribution before sampling.

- **Temperature (T)** scales the logits (raw scores) before softmax.
- **Formula**: `new_probability = softmax(logit / T)`

**Effect**:
- **T < 1 (e.g., 0.1)**: Makes high-probability tokens MORE likely.
  - "mat" becomes 70%, "couch" becomes 20%, etc.
  - **Result**: Conservative, focused, deterministic.
  
- **T = 1**: Original distribution (no change).

- **T > 1 (e.g., 1.5)**: Makes probabilities more uniform.
  - "mat" becomes 25%, "couch" becomes 18%, "floor" becomes 15%, etc.
  - Low-probability tokens (like "table", "chair") get a chance.
  - **Result**: Creative, diverse, unpredictable.

```mermaid
graph LR
    Temp[Temperature]
    Temp --> Low[Low (0.1-0.5)]
    Temp --> Mid[Medium (0.7-1.0)]
    Temp --> High[High (1.2-2.0)]
    
    Low --> Deterministic[Deterministic, Focused]
    Mid --> Balanced[Balanced]
    High --> Creative[Creative, Random]
```

**Use Cases**:
- **Low T (0.1-0.3)**: Code, math, factual Q&A.
- **Medium T (0.7-1.0)**: General conversation, writing.
- **High T (1.2-2.0)**: Creative writing, brainstorming, poetry.

**Note**: T = 0 is equivalent to greedy decoding in some implementations.

#### 3. Top-k Sampling

**Method**: Only consider the **Top K** most probable tokens. Set all others to zero. Then sample from those K.

```
Top-k = 3:
Consider: "mat" (40%), "couch" (25%), "floor" (15%)
Ignore: "bed", "table", ...

Renormalize: "mat" (50%), "couch" (31%), "floor" (19%)
Sample from these three.
```

**Pros**: Prevents sampling from long-tail (rare, weird tokens).
**Cons**: K is fixed; might exclude good options or include bad ones.

**Use Case**: Balanced creativity; prevents nonsensical outputs.

#### 4. Top-p (Nucleus) Sampling

**Method**: Consider the **smallest set of tokens** whose cumulative probability exceeds **P**. Then sample from that set.

```
Top-p = 0.9:
Cumulative probabilities:
- "mat": 40%
- "couch": 40% + 25% = 65%
- "floor": 65% + 15% = 80%
- "bed": 80% + 10% = 90% ✓ (reached 90%)

Consider: "mat", "couch", "floor", "bed"
Ignore: "table", ...

Sample from these four.
```

**Pros**: Adapts to the distribution; no fixed K.
**Cons**: Slightly more complex.

**Use Case**: Often better than Top-k; more adaptive.

### Combining Parameters

You can combine **Temperature + Top-k + Top-p**:

```python
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[...],
    temperature=0.7,
    top_p=0.9,
    # top_k is not available in OpenAI API, but is in other models
)
```

**Typical Combinations**:
- **Deterministic (Code)**: T=0.1, Top-p=1.0 (no filtering).
- **Balanced (Chat)**: T=0.7, Top-p=0.9.
- **Creative (Writing)**: T=1.2, Top-p=0.95.

---

## Real-world Example

**Content Generation Platform**

A company uses GPT-4 to generate marketing copy.

**Scenario 1: Product Descriptions**
- **Goal**: Consistent, SEO-friendly descriptions.
- **Settings**: T=0.3, Top-p=0.9.
- **Result**: Similar structure, focused on keywords, reliable.

**Scenario 2: Social Media Posts**
- **Goal**: Engaging, varied, creative captions.
- **Settings**: T=1.0, Top-p=0.95.
- **Result**: Diverse, unique, attention-grabbing.

**Scenario 3: Brainstorming Campaign Ideas**
- **Goal**: Wild, out-of-the-box ideas.
- **Settings**: T=1.5, Top-p=1.0.
- **Result**: Some crazy ideas, but also innovative concepts.

---

## Advantages
- **Control**: Fine-tune creativity vs. consistency.
- **Diversity**: Generate multiple varied outputs for the same prompt.
- **Use Case Optimization**: Tailor sampling to the task.

## Limitations
- **Non-Deterministic**: Same prompt can give different outputs.
- **Tuning Required**: Need to experiment to find optimal settings.
- **Model-Dependent**: Different models respond differently to temperature.

---

## Common Interview Questions
- **What does temperature do in an LLM?**
- **Difference between Top-k and Top-p sampling?**
- **When would you use high vs. low temperature?**
- **What is greedy decoding?**
- **How do you make an LLM more deterministic?**
- **What parameters would you use for code generation?**
- **Explain Nucleus Sampling (Top-p).**

### Interview Answer Tips
- Use the **ice cream analogy** for intuition.
- Emphasize that **temperature scales probabilities**, not directly picks tokens.
- Note that **Top-p is more adaptive** than Top-k.

---

## Common Mistakes
- Using high temperature for factual tasks (introduces errors).
- Setting temperature > 2 (outputs become incoherent).
- Forgetting that sampling makes outputs **non-deterministic**.
- Confusing Top-p with confidence threshold.

---

## Summary
Sampling parameters control how LLMs choose tokens. Temperature adjusts creativity (low = focused, high = diverse). Top-k limits choices to K tokens. Top-p (Nucleus) considers tokens until cumulative probability exceeds p. Use low temperature for code/facts, high temperature for creative tasks. These parameters are essential for tuning LLM behavior.

---

## Practice Questions
1. What happens when you set temperature to 0?
2. How does temperature affect the probability distribution?
3. What is the difference between Top-k and Top-p?
4. When would you use Top-k sampling?
5. Why is Top-p considered more adaptive than Top-k?
6. What sampling settings would you use for generating poetry?
7. Can temperature be negative?
8. How do you ensure deterministic output from an LLM?

---

## Mini Project Ideas
1. **Temperature Experiment**: Generate 10 outputs at different temperatures and compare diversity.
2. **Sampling Comparison**: Compare greedy vs. Top-p vs. Top-k on the same prompt.
3. **Creative Writer**: Build a tool that generates story ideas with high temperature and curates the best ones.

---

## Further Reading
- [[35 LLM Fundamentals]]
- [[36 Prompt Engineering]]
- [[52 Fine-tuning vs Prompt Engineering]]