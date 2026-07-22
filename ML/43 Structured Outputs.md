# 43 Structured Outputs from LLMs

tags:
#llm
#structured-output
#json
#genai
#placements
#interview

---

## Why this topic matters
LLMs naturally generate **free-form text**, but production systems need **structured data** (JSON, XML, CSV). Extracting structured outputs reliably is critical for integrating LLMs into workflows, databases, and APIs. Interviewers often ask: *"How do you ensure an LLM outputs valid JSON?"*

## Learning Objectives
- Understand why structured outputs are needed.
- Learn techniques to get JSON/structured data from LLMs.
- Understand JSON Mode and constrained decoding.
- Know how to handle parsing errors.

## Prerequisites
- [[35 LLM Fundamentals]]
- [[36 Prompt Engineering]]
- [[42 Function Calling with LLMs]]

---

## Intuition
Imagine you're collecting **survey responses**.

**Unstructured (Free-form text)**:
- Respondent 1: "I'm 25, work in tech, love hiking!"
- Respondent 2: "age: twenty-eight, job is marketing, hobbies include reading"
- Respondent 3: "Thirty years old. Engineer. Enjoy swimming."

**Problem**: How do you analyze this? Every format is different!

**Structured (JSON)**:
```json
{"age": 25, "industry": "tech", "hobby": "hiking"}
{"age": 28, "industry": "marketing", "hobby": "reading"}
{"age": 30, "industry": "engineering", "hobby": "swimming"}
```

**Benefit**: Easy to analyze, store in a database, or feed into another system.

**Structured outputs** force LLMs to generate data in a consistent, machine-readable format.

---

## Detailed Explanation

### Why Do We Need Structured Outputs?

**LLMs Output Text**, but production systems need:
- **JSON** for APIs.
- **Database records** (rows, columns).
- **Configuration files** (YAML, JSON).
- **Code generation** (Python, SQL).
- **Classification labels** (not prose).

**Examples**:
- Extract entities from text → JSON object.
- Classify sentiment → {"sentiment": "positive"}.
- Generate a SQL query → `SELECT * FROM...`.
- Parse a resume → Structured fields (name, email, experience).

### Techniques for Structured Outputs

#### 1. Prompt Engineering (Basic)

Simply **ask** the LLM to output JSON.

```
Prompt:
Extract the name, age, and city from this text. Output ONLY valid JSON.

Text: "John is 30 years old and lives in New York."

Output:
{"name": "John", "age": 30, "city": "New York"}
```

**Pros**: Simple, works with any LLM.
**Cons**: Not guaranteed; LLM might still output prose or invalid JSON.

**Tips**:
- Use "**Output ONLY JSON**" in the prompt.
- Provide a **schema/example**.
- Use **triple backticks** to delimit JSON.

#### 2. Few-Shot Examples

Show the LLM examples of the desired format.

```
Examples:
Input: "Alice, 25, Paris"
Output: {"name": "Alice", "age": 25, "city": "Paris"}

Input: "Bob is 40 and lives in London"
Output: {"name": "Bob", "age": 40, "city": "London"}

Input: "John is 30 years old and lives in New York."
Output:
```

**Benefit**: LLM learns the pattern and follows it.

#### 3. JSON Mode (Native Support)

Some APIs offer a **JSON Mode** that forces valid JSON output.

**OpenAI**:
```python
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[...],
    response_format={"type": "json_object"}
)
```

**Benefit**: Guaranteed valid JSON (API-level enforcement).
**Limitation**: Only available in certain models/APIs.

#### 4. Constrained Decoding / Grammar-Based Decoding

Use libraries that **constrain** the LLM's output at the token level.

**Libraries**:
- **Outlines**: Define a Pydantic schema or regex.
- **Guidance** (Microsoft): Template-based constrained generation.
- **LMQL**: Query language for LLMs with constraints.

**Example with Outlines**:
```python
from outlines import generate
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

model = load_model("...")
generator = generate.json(model, Person)
result = generator("John is 30 and lives in New York.")
# result is guaranteed to be valid Person JSON
```

**How it works**:
- The library **masks** invalid tokens during generation.
- LLM can only generate tokens that conform to the schema.

**Benefit**: 100% valid output, no parsing errors.

#### 5. Post-Processing / Retry Logic

If the LLM outputs invalid JSON:
1. **Parse** the output.
2. If parsing fails, **ask the LLM to fix it**.

```python
import json

try:
    data = json.parse(llm_output)
except json.JSONDecodeError:
    # Ask LLM to fix
    fix_prompt = f"Your JSON was invalid. Please fix it: {llm_output}"
    llm_output = call_llm(fix_prompt)
    data = json.parse(llm_output)
```

**Benefit**: Handles edge cases without constrained decoding.

### Common Structured Output Formats

| Format | Use Case |
| :--- | :--- |
| **JSON** | APIs, databases, configuration |
| **XML** | Legacy systems, RSS feeds |
| **CSV** | Spreadsheets, data export |
| **YAML** | Configuration files |
| **Markdown Tables** | Reports, documentation |
| **SQL** | Database queries |
| **Code** | Python, JavaScript, etc. |

---

## Real-world Example

**Resume Parsing System**

Company receives 1000 resumes in various formats (PDF, Word, plain text).

**Goal**: Extract structured data to store in a database.

**Prompt**:
```
Extract the following fields from this resume:
- name (string)
- email (string)
- phone (string)
- skills (list of strings)
- experience (list of objects with: company, role, start_date, end_date)

Output ONLY valid JSON matching this schema.
```

**Output**:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-1234",
  "skills": ["Python", "Machine Learning", "SQL"],
  "experience": [
    {"company": "TechCorp", "role": "ML Engineer", "start_date": "2020-01", "end_date": "2023-12"},
    {"company": "DataInc", "role": "Data Analyst", "start_date": "2018-06", "end_date": "2019-12"}
  ]
}
```

**Benefit**: All resumes are now in a consistent format, ready for database insertion.

---

## Advantages
- **Machine-Readable**: Easy to integrate with other systems.
- **Validation**: Schema enforcement catches errors.
- **Consistency**: All outputs follow the same format.
- **Automation**: No manual parsing or cleanup needed.

## Limitations
- **LLM Errors**: LLMs can still output invalid formats (without constraints).
- **Token Overhead**: Schemas and examples add tokens (cost).
- **Complexity**: Constrained decoding requires additional libraries.
- **Flexibility Loss**: LLM can't provide nuanced explanations.

---

## Common Interview Questions
- **How do you get structured output from an LLM?**
- **What is JSON Mode?**
- **Difference between prompt engineering and constrained decoding?**
- **How do you handle invalid JSON from an LLM?**
- **What libraries support constrained decoding?**
- **When would you use structured outputs?**
- **Can an LLM output XML or CSV?**

### Interview Answer Tips
- Mention that **prompt engineering is the basic approach**.
- Emphasize that **constrained decoding** (Outlines, Guidance) provides guarantees.
- Note that **JSON Mode** is available in some APIs for enforcement.

---

## Common Mistakes
- Not validating the LLM's output (assume it's always valid).
- Forgetting to specify "Output ONLY JSON" in the prompt.
- Not handling parsing errors gracefully.
- Using overly complex schemas that confuse the LLM.

---

## Summary
Structured outputs convert LLM responses into machine-readable formats like JSON, XML, or CSV. Techniques range from simple prompting to constrained decoding with libraries like Outlines. JSON Mode in some APIs enforces valid JSON. Post-processing can fix invalid outputs. Structured outputs are essential for integrating LLMs into production workflows.

---

## Practice Questions
1. Why can't we trust LLMs to always output valid JSON?
2. What is JSON Mode and which models support it?
3. How does constrained decoding work?
4. What library would you use for schema-based output?
5. How do you handle parsing errors from an LLM?
6. Give an example of when you'd need structured output.
7. Can you get a CSV output from an LLM?
8. What's the difference between few-shot prompting and constrained decoding?

---

## Mini Project Ideas
1. **Resume Parser**: Build a system that extracts structured data from resume text.
2. **Sentiment Classifier**: Get JSON output with sentiment scores from movie reviews.
3. **Schema Validator**: Use Outlines to enforce a Pydantic schema on LLM outputs.

---

## Further Reading
- [[35 LLM Fundamentals]]
- [[36 Prompt Engineering]]
- [[42 Function Calling with LLMs]]
- [[54 LangChain Basics]]