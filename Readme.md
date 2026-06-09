# 10-Day LangChain & LangGraph Practice Sprint 

This repository documents my 10-day hands-on journey to build practical projects with **LangChain** and **LangGraph**.

The goal is simple:
- Learn by building
- Progress from basics to advanced workflows
- Finish each day with something runnable
- Strengthen my skills in chains, tools, agents, RAG, memory, graphs, and multi-agent systems

---

## 🎯 What I’m doing in these 10 days

I’m following a structured learning path that moves from **LCEL and tools** to **RAG, memory, agents, and LangGraph workflows**.

### Day 1: LCEL Basics
- Build a simple prompt → model pipeline
- Learn `invoke()`, `batch()`, and `stream()`
- Practice composing chains with `|`

### Day 2: Custom Tools
- Create custom tools using `@tool`
- Connect a tool to a basic agent
- Understand when the agent should call a tool

### Day 3: Document Loader + RAG
- Load a document or web page
- Split text into chunks
- Create embeddings and store them in a vector database
- Build a simple Q&A RAG system

### Day 4: Short-Term Memory
- Build a conversational agent with memory
- Use checkpointers for thread persistence
- Make the bot remember earlier messages

### Day 5: Structured Output
- Return answers in JSON or Pydantic format
- Enforce schema-based output
- Practice clean structured responses

### Day 6: Web-Enabled RAG
- Connect search APIs like Tavily or SerpAPI
- Retrieve live information from the web
- Generate answers using fresh context

### Day 7: Python REPL Agent
- Let the agent write and execute Python code
- Use Python as a tool for calculations or data tasks
- Capture tool output and feed it back into the response

### Day 8: SQL Query Agent
- Connect to a SQLite/PostgreSQL database
- Convert plain English to SQL
- Return database answers in a readable format

### Day 9: LangGraph Workflow
- Build a `StateGraph`
- Add nodes, edges, and conditional routing
- Understand state flow in LangGraph

### Day 10: Advanced Agent Demo
- Combine multiple ideas into one project
- Add either multi-agent orchestration, checkpointing, or human-in-the-loop interaction
- Finalize the repository with documentation and demo notes

---

## 🧰 Tech Stack

- Python
- LangChain
- LangGraph
- OpenAI / Anthropic models
- Chroma / Pinecone / FAISS
- SQLite / PostgreSQL
- Tavily / SerpAPI
- Pydantic

---

## 📁 Repository Structure

```bash
.
├── day-01-lcel-basics/
├── day-02-custom-tools/
├── day-03-rag-document-qa/
├── day-04-memory-agent/
├── day-05-structured-output/
├── day-06-web-rag/
├── day-07-python-repl-agent/
├── day-08-sql-agent/
├── day-09-langgraph-workflow/
├── day-10-final-project/
└── README.md