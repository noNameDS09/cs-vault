# 54 LangChain Basics

tags:
#langchain
#llm
#orchestration
#genai
#placements
#interview

---

## Why this topic matters
**LangChain** is the most popular framework for building LLM applications. It provides abstractions for chaining prompts, integrating tools, managing memory, and building complex workflows. Understanding LangChain is essential for rapidly prototyping AI applications and is frequently mentioned in AI engineering job descriptions.

## Learning Objectives
- Understand what LangChain is and why it's popular.
- Learn key LangChain concepts (Chains, Agents, Memory).
- Understand how to integrate LLMs with external data.
- Know common LangChain patterns and use cases.

## Prerequisites
- [[35 LLM Fundamentals]]
- [[42 Function Calling with LLMs]]
- [[50 RAG]]

---

## Intuition
Imagine you're building a **LEGO castle**.

**Without LangChain**:
- You have to mold each brick from scratch.
- Connect pipes, wires, and mechanisms manually.
- Every castle is built differently.

**With LangChain**:
- You have pre-made **LEGO bricks** (prompts, chains, agents).
- **Snap them together** in different combinations.
- Reuse patterns, share with others, build faster.

**LangChain** is a **toolkit of LEGO bricks** for building LLM applications.

---

## Detailed Explanation

### What is LangChain?

**LangChain** is a Python/JavaScript framework for developing applications powered by language models.

**Core Philosophy**: LLMs are most powerful when combined with:
- **External Data** (databases, APIs, documents).
- **Computation** (calculators, code execution).
- **Memory** (conversation history, state).
- **Other LLMs** (multi-agent workflows).

### Key Concepts

#### 1. Prompts and Prompt Templates

**Prompt Template**: A reusable prompt with variables.

```python
from langchain.prompts import PromptTemplate

template = """
You are a helpful assistant specializing in {topic}.
Answer the following question: {question}

Answer:
"""

prompt = PromptTemplate.from_template(template)
formatted = prompt.format(topic="machine learning", question="What is overfitting?")
```

**Benefit**: Reuse prompts, separate logic from content.

#### 2. Chains

**Chain**: A sequence of steps (prompts, LLM calls, transformations).

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(topic="AI safety", question="What are guardrails?")
```

**Sequential Chain**: Multiple chains in sequence.

```python
from langchain.chains import SequentialChain

# Chain 1: Generate summary
summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

# Chain 2: Translate summary
translate_chain = LLMChain(llm=llm, prompt=translate_prompt, output_key="translation")

# Combine
overall_chain = SequentialChain(
    chains=[summary_chain, translate_chain],
    input_variables=["text"],
    output_variables=["summary", "translation"]
)

result = overall_chain({"text": "Long article..."})
```

#### 3. Agents

**Agent**: LLM that can **use tools** (search, calculator, APIs).

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper

llm = OpenAI()
search = GoogleSearchAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Search Google for current information"
    ),
    Tool(
        name="Calculator",
        func=lambda x: str(eval(x)),
        description="Evaluate math expressions"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent.run("What is 15% of $250?")
```

**How it works**:
1. LLM decides which tool to use.
2. Tool executes.
3. LLM uses result to generate final answer.

#### 4. Memory

**Memory**: Maintain conversation history across turns.

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

conversation.predict(input="My name is John")
# "Nice to meet you, John!"

conversation.predict(input="What's my name?")
# "Your name is John." (remembers from history!)
```

**Types of Memory**:
- **Buffer Memory**: Full history.
- **Summary Memory**: Summarize old messages.
- **Vector Store Memory**: Retrieve relevant past messages.

#### 5. Document Loaders and Splitters

**Loaders**: Read documents from various sources.

```python
from langchain.document_loaders import PyPDFLoader, WebBaseLoader

# PDF
loader = PyPDFLoader("document.pdf")
docs = loader.load()

# Web
loader = WebBaseLoader("https://example.com")
docs = loader.load()
```

**Splitters**: Chunk documents for RAG.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
```

#### 6. Vector Stores and Retrievers

**Vector Store**: Store and search embeddings.

```python
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# Search
results = vectorstore.similarity_search("What is AI?", k=3)
```

**Retriever**: Abstract interface for retrieval.

```python
retriever = vectorstore.as_retriever()
docs = retriever.get_relevant_documents("What is AI?")
```

---

## Real-world Example

**Research Assistant Chatbot**

```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

# Load research papers
docs = load_papers()  # Custom loader

# Chunk and embed
chunks = split_documents(docs)
vectorstore = FAISS.from_documents(chunks, OpenAIEmbeddings())

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Query
result = qa_chain({"query": "What are the latest findings on cancer immunotherapy?"})

print(result["result"])  # Answer
print(result["source_documents"])  # Cited papers
```

---

## Advantages
- **Rapid Prototyping**: Build complex workflows quickly.
- **Modular**: Reuse components (chains, agents, memory).
- **Ecosystem**: Integrations with 100+ tools and services.
- **Community**: Large community, many examples and tutorials.

## Limitations
- **Abstraction Overhead**: Can be overkill for simple tasks.
- **Performance**: Additional layers add latency.
- **Complexity**: Debugging complex chains can be challenging.
- **Vendor Lock-in**: Migrating away from LangChain requires rewriting.

---

## Common Interview Questions
- **What is LangChain and what problem does it solve?**
- **Explain the difference between Chains and Agents.**
- **How do you add memory to a LangChain application?**
- **What are document loaders and splitters?**
- **How would you build a RAG system with LangChain?**
- **What are the limitations of LangChain?**
- **When would you NOT use LangChain?**

### Interview Answer Tips
- Emphasize that LangChain **abstracts common patterns** (RAG, agents, memory).
- Mention that it's **not always necessary** for simple LLM integrations.
- Note that **understanding the underlying concepts** (prompts, chains, retrieval) is more important than the framework itself.

---

## Common Mistakes
- Using LangChain for every LLM task (over-engineering).
- Not understanding the abstraction (black box usage).
- Ignoring built-in integrations (reinventing the wheel).
- Forgetting to handle errors in chains and agents.

---

## Summary
LangChain is a framework for building LLM applications with composable components: Prompts, Chains, Agents, Memory, and Retrievers. It enables rapid prototyping of complex workflows like RAG systems and multi-tool agents. While powerful, it can be overkill for simple use cases. Understanding core LLM concepts is more important than the framework itself.

---

## Practice Questions
1. What is the main benefit of using LangChain?
2. Explain the difference between a Chain and an Agent.
3. How do you add conversation memory in LangChain?
4. What is a document loader?
5. How would you build a RAG system with LangChain?
6. When would you NOT use LangChain?
7. What is a retriever in LangChain?
8. Name three LangChain integrations you know.

---

## Mini Project Ideas
1. **Simple Chatbot**: Build a conversation bot with memory using LangChain.
2. **RAG System**: Create a document Q&A system with FAISS and LangChain.
3. **Research Agent**: Build an agent that can search the web and summarize findings.

---

## Further Reading
- [[35 LLM Fundamentals]]
- [[42 Function Calling with LLMs]]
- [[50 RAG]]
- [[53 AI Agents]]
- [[43 Structured Outputs]]