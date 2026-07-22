# 36 Prompt Engineering

tags:
#llm
#prompt-engineering
#genai
#placements
#interview

---

## Why this topic matters
Prompt Engineering is the **most practical skill** for working with LLMs. It's how you get ChatGPT, Claude, or any LLM to produce high-quality results. Companies hiring AI engineers expect you to know how to craft effective prompts. This skill separates average users from power users.

## Learning Objectives
- Understand Zero-Shot, One-Shot, and Few-Shot prompting.
- Learn Chain-of-Thought prompting.
- Understand system prompts and role-setting.
- Master practical prompting techniques.

## Prerequisites
- [[35 LLM Fundamentals]]
- [[34 Tokenization]]

---

## Intuition
Imagine you're working with a **genius intern** who knows everything but has no common sense.

**Bad instructions**: "Write something about marketing."

**Good instructions**:
> "You are a senior marketing consultant. Write a detailed 3-paragraph report on Q4 digital marketing strategies for a B2B SaaS company. Focus on LinkedIn ads, content marketing, and email campaigns. Include specific metrics to track. Use a professional, data-driven tone."

The second one specifies:
- **Role**: Senior marketing consultant
- **Task**: 3-paragraph report
- **Topic**: Q4 digital marketing for B2B SaaS
- **Focus**: LinkedIn, content, email
- **Style**: Professional, data-driven

**Prompt engineering** is the art of communicating clearly with LLMs.

---

## Detailed Explanation

### Levels of Prompting

#### 1. Zero-Shot Prompting

Asking without any examples.

```
Prompt: "Translate this to French: Hello, how are you?"
Response: "Bonjour, comment allez-vous?"
```

**Use case**: Simple, well-defined tasks where the LLM already knows what to do.

#### 2. One-Shot Prompting

Giving **one example** to show the expected format.

```
Prompt:
Convert to JSON format:
Input: "John Doe, 35, New York"
Output: {"name": "John Doe", "age": 35, "city": "New York"}

Input: "Jane Smith, 28, London"
Output: 
```

**Use case**: When you need a specific output format.

#### 3. Few-Shot Prompting

Giving **multiple examples** so the LLM learns the pattern.

```
Prompt:
Classify sentiment:
Text: "I loved this movie!" → Positive
Text: "This was terrible." → Negative
Text: "It was okay." → Neutral
Text: "The acting was amazing but the plot was weak." → 
```

**Use case**: Complex classification, custom formats, niche tasks.

### Advanced Techniques

#### 4. Chain-of-Thought (CoT) Prompting

Asking the model to **think step by step** before answering.

```
Standard: "What is 23 × 17 + 15?"
CoT: "What is 23 × 17 + 15? Let's think step by step."

Response with CoT:
"First, 23 × 17 = 391
Then, 391 + 15 = 406
Answer: 406"
```

**Impact**: Dramatically improves reasoning, math, and logic tasks.

#### 5. System Prompts (Role Setting)

Setting the **persona** and **behavior** of the LLM.

```
System: "You are a helpful coding assistant. You only answer Python questions. 
Break down complex problems into simple steps. Always include code examples."

User: "How do I read a file?"
Response: "Here's how to read a file in Python:
```python
with open('file.txt', 'r') as f:
    content = f.read()
```"
```

**Use case**: Customizing LLM behavior for specific domains.

#### 6. Delimiters and Structure

Using ``` or `---` or `###` to **separate** different parts of the prompt.

```
### Instructions ###
Summarize the following text in 2 sentences.

### Text ###
[Long article here]

### Summary ###
```

**Benefit**: Prevents confusion between instructions and content.

### 7. Chain-of-Density Prompting

Iteratively improving outputs by asking for more detail.

```
First: "Summarize this article."
Then: "Make the summary more detailed. Include specific numbers and names."
Then: "Add context about why this matters."
```

---

## Best Practices

| Do ✅ | Don't ❌ |
| :--- | :--- |
| Be specific and detailed | Vague, open-ended requests |
| Give examples (few-shot) | Assume the LLM knows your format |
| Set a role/persona | Leave behavior undefined |
| Break complex tasks into steps | Ask for everything in one prompt |
| Use delimiters to organize | Write one giant block of text |
| Specify the output format | Accept whatever format you get |

### Prompt Template

```
# Role
You are [specific expert role].

# Task
[Clear description of what to do].

# Context
[Background information, constraints].

# Examples
[1-3 examples of input → output].

# Output Format
[Exact format: JSON, bullet points, paragraphs].

# Input
[The actual data to process].
```

---

## Real-world Example

**Customer Support Email Response**

```
System: You are a customer support rep for TechCompany. Be polite, empathetic, 
and solution-oriented. Never promise features we don't have.

Task: Respond to this customer complaint about slow loading times.

Customer Email: "Your website is so slow! I've been waiting 5 minutes for a page to load. 
This is unacceptable!"

Response:
```

**LLM Output**:
> "Dear Valued Customer,
>
> Thank you for reaching out, and I sincerely apologize for the frustration you've experienced with our website's loading times. I completely understand how frustrating this must be...
>
> I've escalated this to our engineering team. In the meantime, could you try clearing your browser cache? ...
>
> We appreciate your patience and value your business.
> 
> Best regards, ..."

---

## Common Interview Questions
- **What is prompt engineering?**
- **Difference between zero-shot and few-shot prompting?**
- **What is Chain-of-Thought prompting?**
- **Why are examples (few-shot) helpful?**
- **What is a system prompt?**
- **How do you prevent hallucinations with prompts?**

### Interview Answer Tips
- Mention that prompt engineering is **iterative**—you refine prompts based on results.
- Note that **few-shot > zero-shot** for complex tasks.
- Emphasize that **CoT improves reasoning** significantly.

---

## Common Mistakes
- Not being specific enough.
- Forgetting to set a role/persona.
- Mixing instructions with input data.
- Expecting one prompt to work perfectly (it's iterative!).
- Not using delimiters for clarity.

---

## Summary
Prompt Engineering is the skill of crafting effective inputs for LLMs. Zero-shot is simple requests; few-shot uses examples to teach patterns. Chain-of-Thought improves reasoning. System prompts set behavior. Good prompts are specific, structured, and include examples.

---

## Practice Questions
1. What is the difference between zero-shot and few-shot?
2. When would you use Chain-of-Thought prompting?
3. What is a system prompt?
4. Why are delimiters useful in prompts?
5. How do examples improve LLM outputs?
6. What role does context play in prompting?
7. Can prompt engineering prevent hallucinations?
8. How would you prompt an LLM to write code?

---

## Mini Project Ideas
1. **Prompt Library**: Create a collection of effective prompts for different tasks (summarization, classification, code generation).
2. **Before/After Comparison**: Test zero-shot vs. few-shot on the same task and compare quality.
3. **Chain-of-Thought Demo**: Show how CoT improves math/logic answers.

---

## Further Reading
- [[35 LLM Fundamentals]]
- [[34 Tokenization]]
- [[52 Fine-tuning vs Prompt Engineering]]
- [[53 AI Agents]]