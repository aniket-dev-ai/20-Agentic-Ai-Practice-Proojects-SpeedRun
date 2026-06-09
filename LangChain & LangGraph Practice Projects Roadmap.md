# **🗺️ LangChain & LangGraph Practice Projects Roadmap**

Welcome to your structured learning roadmap\! This document outlines a step-by-step path from beginner to advanced concepts in the 2025 LangChain/LangGraph ecosystem.

## **🟢 Beginner Projects**

### **1\. LCEL Text Generation Pipeline**

* **Difficulty:** 🟢 Beginner  
* **Core Concepts Covered:** LangChain Expression Language (LCEL), Runnable chains, prompt templates, batch/streaming modes.  
* **Tools & Integrations:** OpenAI Chat model (e.g. ChatGPT via LangChain), LangChain LCEL.  
* **Project Description:** Build a simple LCEL pipeline that composes a prompt template with a chat model (e.g. prompt | ChatOpenAI). The chain should generate output (e.g. jokes or summaries) for given inputs. Demonstrate invoking the chain normally, in batch, and in streaming mode.  
* **Key Learning Outcomes:** Master creating and invoking LCEL pipelines using |, understanding how Runnables work, and using invoke(), batch(), and stream() methods to run models efficiently. Learn how prompt templates integrate into the chain.  
* **Suggested Stack:** Python, langchain LCEL (langchain-core), OpenAI (via langchain-openai).

### **2\. Custom Tool and Agent Basics**

* **Difficulty:** 🟢 Beginner  
* **Core Concepts Covered:** Custom tools (via @tool), agent creation, prompt-based tool-calling (ReAct agent).  
* **Tools & Integrations:** Custom Python tool (e.g. a simple web search or calculator), LangChain agent (create\_agent or create\_react\_agent), OpenAI or Anthropic LLM.  
* **Project Description:** Implement a custom tool (e.g. a simple wiki lookup or math calculator with @tool decorator) and integrate it into a conversational agent. For example, create an agent that can answer queries by calling the tool when needed. Show how the agent chooses to use the tool vs. respond directly.  
* **Key Learning Outcomes:** Learn to define tools with typed inputs, names, and descriptions, and attach them to an agent. Understand how an agent (ReAct style) decides to call tools to gather information. Gain experience with LangChain’s agent API and seeing tool calls in action.  
* **Suggested Stack:** Python, langchain tools (@tool), a chat model (OpenAI/Anthropic), any simple API (e.g. Wikipedia or custom function).

### **3\. Retrieval Q\&A with Document Loaders**

* **Difficulty:** 🟢 Beginner  
* **Core Concepts Covered:** Document loaders, text splitters, embeddings, vector stores, Retriever interface, Retrieval-Augmented Generation (RAG).  
* **Tools & Integrations:** LangChain document loaders (e.g. WebBaseLoader, TextLoader), RecursiveCharacterTextSplitter, embeddings (OpenAIEmbeddings or Hugging Face), vector database (Chroma or Pinecone).  
* **Project Description:** Build a simple Q\&A bot over an unstructured text source. Load a document (e.g. a web page or local text file) into LangChain, split it into chunks, and store embeddings in a vector store. Then implement a RAG chain or retrieval agent: when a user asks a question, retrieve relevant chunks and feed them to the LLM for an answer.  
* **Key Learning Outcomes:** Understand the RAG pipeline: ingesting data (loaders, splitters), creating embeddings, using a VectorStore and Retriever. Practice fetching context for a query and generating answers. Learn to call the vector store’s .add\_documents() and .similarity\_search() methods.  
* **Suggested Stack:** Python, langchain document loaders & splitters, langchain-openai embeddings, langchain-chroma or langchain-pinecone, a chat model.

### **4\. Conversational Agent with Short-Term Memory**

* **Difficulty:** 🟢 Beginner  
* **Core Concepts Covered:** Short-term (thread) memory, LangGraph checkpointers, agent state persistence.  
* **Tools & Integrations:** LangChain agent (create\_agent), LangGraph memory saver (e.g. InMemorySaver or PostgresSaver), chat model.  
* **Project Description:** Create a chat agent that remembers the conversation history. Set up a checkpointer when creating the agent so that each thread’s state (messages, etc.) is persisted. For example, have the bot remember the user’s name or preferences. Demonstrate by conversing in a single thread: after a few messages, the agent should recall previous context (e.g. “You said your name is X”) across multiple queries.  
* **Key Learning Outcomes:** Learn to enable short-term memory via checkpointers. See how LangChain agents store state in LangGraph and how using a checkpointer allows resuming threads. Gain familiarity with threading (using thread\_config) and resume/persist conversation context.  
* **Suggested Stack:** Python, langchain agents, langgraph-checkpoint (InMemory or Postgres saver), any LLM model.

### **5\. Structured Output with Output Parsers**

* **Difficulty:** 🟢 Beginner  
* **Core Concepts Covered:** Output parsers and structured output (Pydantic models, JSON schema).  
* **Tools & Integrations:** LangChain structured output utilities, Pydantic, a chat model with JSON support (e.g. GPT-4).  
* **Project Description:** Build an agent that returns answers in a strict JSON or typed format. For example, ask the agent to “List 3 books and their authors in JSON format.” Define a Pydantic model or TypedDict for the expected output schema and use LangChain’s response\_format (or output parser) to enforce it. The agent should return a JSON object that LangChain validates and returns as structured data.  
* **Key Learning Outcomes:** Mastering structured output so that the LLM’s response is parsed into a data object, avoiding unstructured text parsing. Learn to define schemas (Pydantic/BaseModel) for expected answers and use the response\_format parameter to have the agent generate JSON/Pydantic-compliant output.  
* **Suggested Stack:** Python, Pydantic, langchain structured output feature (response\_format), an LLM with native JSON output support (e.g. GPT-4).

## **🟡 Intermediate Projects**

### **6\. Web-Enabled RAG Agent with Search API**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** RAG with live web retrieval, tools integration (SerpAPI/Tavily), LangChain Agents performing multi-step retrieval and generation.  
* **Tools & Integrations:** SerpAPI or Tavily for web search, LangChain retrieval tools (WebBrowserTool or custom search tool), vector store (optional), chat model.  
* **Project Description:** Implement a question-answering agent that can search the web for information. For a user query, first call a search API tool (e.g. SerpAPI) to get relevant links or snippets, and then feed that information to the model for an answer. This mimics an Agentic RAG: the agent acts as orchestrator, retrieving up-to-date info before answering.  
* **Key Learning Outcomes:** Learn to call real-time APIs as tools within an agent loop. Practice designing the agent prompt to know when to use the web search tool. Understand the interplay of retrieval (via API) and generation in a RAG setting.  
* **Suggested Stack:** Python, langchain tools (SerpAPI or Tavily search tool), langchain-openai or other LLM model, optional vector store if caching results.

### **7\. Python REPL Agent**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** Tools for code execution, ReAct agent for programming tasks, @tool decorator for Python REPL.  
* **Tools & Integrations:** LangChain’s Python REPL tool (custom or built-in), langchain-tools for code execution, a powerful LLM.  
* **Project Description:** Create an agent that can write and execute Python code. For example, ask the agent to compute a math problem or generate a chart. The agent should use a Python REPL tool when needed (via a tool call) to run code. Show how the tool’s output (printed or returned value) is fed back to the agent and eventually to the user.  
* **Key Learning Outcomes:** Gain experience using computation tools in an agent. Understand how the agent can decide to invoke the Python tool (using ReAct reasoning) to perform tasks like math or data visualization. Learn to capture the tool’s output and incorporate it into the conversation response.  
* **Suggested Stack:** Python, langchain tools (@tool for Python REPL or \[langchain’s built-in PythonREPLTool\]), an LLM (e.g. GPT-4 or Claude).

### **8\. SQL Database Query Agent**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** SQL tool integration, chaining LLM-generated SQL queries and execution, LangChain SQLChain or Agents.  
* **Tools & Integrations:** LangChain’s SQLDatabase or SQLQueryChain, an example SQLite/PostgreSQL database (or langchain-sql integration), chat model.  
* **Project Description:** Build an agent that answers questions by querying a database. For instance, given a simple table of data (e.g. movies or sales), the user asks a query in plain English, and the agent generates and runs an SQL query to fetch results. The agent then formats the result for the user.  
* **Key Learning Outcomes:** Learn how to set up the SQLDatabase chain or agent such that the LLM generates SQL from natural language, executes it, and handles the output. Understand integration of LangChain with SQL backends and prompt templates for SQL generation.  
* **Suggested Stack:** Python, langchain SQL tools (e.g. SQLDatabaseChain), SQLite (via sqlite3 or an in-memory DB).

### **9\. ReAct Agent with Multiple Tools**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** Custom ReAct agent, multi-tool orchestration, complex prompt engineering.  
* **Tools & Integrations:** Several tools (e.g. web search, calculator, wiki tool), LangChain ReAct agent.  
* **Project Description:** Design an agent with at least 2–3 different tools (e.g. a web search, a calculator, and a Wikipedia lookup). Pose a multi-faceted question that requires using multiple tools in sequence. For example, “What is the square root of the population of France?” – requiring a search (or wiki) for population then calculation. Show the reasoning steps and tool calls.  
* **Key Learning Outcomes:** Practice orchestrating multiple tools in a single agent loop. Learn how the agent can choose the correct tool(s) and chain steps in reasoning. Understand prompt design so the agent knows each tool’s role and when to stop.  
* **Suggested Stack:** Python, langchain agents and tools (e.g. SerpAPI or Wikipedia tool, a calculator tool), LLM model.

### **10\. LangGraph StateGraph Workflow**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** LangGraph StateGraph API, nodes and edges, shared state schema, conditional routing.  
* **Tools & Integrations:** LangGraph (StateGraph), possibly a simple LLM call inside a node, Python code nodes.  
* **Project Description:** Create a LangGraph workflow for a multi-step task. For example, define a StateGraph with a shared state schema and add nodes that perform actions (such as calling the LLM or modifying state). Use conditional edges: e.g. if the state contains a flag, route to one node; else route elsewhere. Demonstrate compiling and invoking the graph on input.  
* **Key Learning Outcomes:** Learn to define a graph by creating a StateGraph, adding nodes (Python functions) and edges (including conditional edges). Understand how nodes receive and update the shared state and how LangGraph manages execution.  
* **Suggested Stack:** Python, langgraph library, any LLM wrapped in a node (or simple functions), TypedDict or Pydantic for state.

### **11\. Multimodal Question Answering Agent**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** Multimodal inputs (text \+ images), LangChain message content blocks, agent that handles images.  
* **Tools & Integrations:** Vision-capable LLM (e.g. GPT-4 Vision, or image-to-text model), LangChain HumanMessage with image content.  
* **Project Description:** Build an agent that can answer questions about an image. For example, load an image (via URL or file), have the user ask “Describe this image” or “What is shown?”, and have the model respond using image understanding. Use LangChain’s multimodal message format to include an image content block along with text.  
* **Key Learning Outcomes:** Experience constructing HumanMessage or AIMessage with mixed content types. Learn how to feed images (URLs or base64) into a chat model. Understand how to parse the model’s multimodal response.  
* **Suggested Stack:** Python, langchain messages (HumanMessage with image content blocks), a multimodal model provider (e.g. Azure’s GPT-4oV, Google Vision API \+ text model).

### **12\. Streaming Chatbot Demo**

* **Difficulty:** 🟡 Intermediate  
* **Core Concepts Covered:** Streaming LLM outputs, real-time updates, LCEL streaming support.  
* **Tools & Integrations:** Chat model with streaming (e.g. OpenAI’s stream=True), LangChain LCEL or Agents.  
* **Project Description:** Create a chat interface (e.g. simple console app) that displays the LLM’s response token-by-token as it arrives. Use a streaming call (stream()) to the chain or chat model so that responses appear incrementally. For example, ask the model to compose a story and print it as it’s being generated.  
* **Key Learning Outcomes:** Learn how to use LangChain’s stream() method for Runnables to get an iterator of tokens or partial messages. Understand how streaming can improve user experience by providing intermediate results.  
* **Suggested Stack:** Python, langchain LCEL or ChatOpenAI(stream=True), asynchronous handling or loop to print streaming content.

## **🔴 Advanced Projects**

### **13\. LangGraph Multi-Agent Supervisor**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** LangGraph multi-agent patterns, create\_supervisor, coordinator and worker agents, agent orchestration.  
* **Tools & Integrations:** LangChain’s Deep Agents or LangGraph Supervisor library (langgraph\_supervisor), multiple specialized agents (e.g. a search agent, a code agent), LLM models.  
* **Project Description:** Implement a multi-agent system using LangGraph’s supervisor pattern. Define several worker agents (e.g. a “research agent” with a search tool and a “coder agent” with Python tool) using create\_react\_agent. Then use create\_supervisor to create a supervisor that delegates user tasks to the appropriate worker based on a prompt. For example, the user gives a compound task (“research X and plot Y”), and the supervisor routes parts to different agents.  
* **Key Learning Outcomes:** Understand hierarchical multi-agent coordination. Learn to use create\_supervisor to tie together multiple agents and a top-level LLM that decides delegation. Practice designing clear roles/prompts for supervisor vs. workers.  
* **Suggested Stack:** Python, langchain, langgraph\_supervisor, LLM provider (GPT-4o or Claude).

### **14\. LangGraph Subgraph Collaboration**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** LangGraph subgraphs, graph composition, state sharing between graphs.  
* **Tools & Integrations:** LangGraph (StateGraph), multiple subgraphs (each a StateGraph), LLM in graph nodes.  
* **Project Description:** Build a complex workflow by composing graphs. For example, create a “travel planner” parent graph and several subgraph agents (flight booking, hotel booking, itinerary). Each subgraph is itself a StateGraph. The parent graph should invoke each subgraph (as a node) to handle its part of the task. Ensure shared keys or state passing so the subgraph outputs feed back to the parent.  
* **Key Learning Outcomes:** Learn how to encapsulate a graph within another graph (subgraph). Understand two approaches: compiling a subgraph as a node when schemas align, or calling graph.invoke inside a node function. Gain experience managing state that flows between parent and child graphs.  
* **Suggested Stack:** Python, langgraph, TypedDict schemas for state, any LLM API for agent nodes.

### **15\. Human-in-the-Loop Workflow**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** LangGraph human oversight, breakpoints, interactive state updates.  
* **Tools & Integrations:** LangGraph (with checkpointers/interrupts), possibly a simple UI or console input, LLM model.  
* **Project Description:** Design an agent workflow that can pause for human input. For example, have the agent make an interim decision and then prompt the user (via the console or UI) before proceeding. You can implement this by inserting a node in the graph that triggers a breakpoint or a wait state. Demonstrate pausing the graph, capturing user input (e.g. confirmation or additional info), then resuming execution.  
* **Key Learning Outcomes:** Learn how LangGraph supports human-in-the-loop by “inspecting and modifying agent state at any point”. Practice adding breakpoints or user-interaction nodes in the graph. Understand how to resume execution from saved state.  
* **Suggested Stack:** Python, langgraph (use features like interrupts or checkpointers), simple frontend or CLI for human input.

### **16\. Persistent LangGraph Workflow with Checkpointing**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** StateGraph persistence, checkpointers, durable execution, LangGraph runtime context.  
* **Tools & Integrations:** LangGraph (StateGraph), langgraph.checkpoint (e.g. PostgresSaver), LLM.  
* **Project Description:** Build a long-running graph that can be stopped and resumed without losing progress. For example, create a multi-step task graph (which may take time or have optional delays) and set up a persistent checkpointer (like PostgreSQL). Simulate a failure or restart mid-execution, then resume the graph from its saved state.  
* **Key Learning Outcomes:** Understand how to compile a graph with a checkpointer to automatically persist state. See how LangGraph’s durable execution works (inspired by Pregel) to allow resuming after interruption.  
* **Suggested Stack:** Python, langgraph with PostgresSaver (or other DB), LLM or dummy tasks.

### **17\. Parallel & Streaming Graph Execution**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** LangGraph parallel edges, super-steps, streaming LLM calls within graph.  
* **Tools & Integrations:** LangGraph (StateGraph), nodes that run concurrently, streaming LLM tools.  
* **Project Description:** Create a graph where multiple nodes execute in parallel on the same step. For example, build a graph that, given a prompt, sends it to two different LLM nodes (perhaps with different models or prompts) in parallel, then combines their outputs. Also, explore streaming inside graph nodes: have a node stream partial results back (e.g. via LangChain’s streaming in a Runnable).  
* **Key Learning Outcomes:** Learn how LangGraph schedules parallel node execution (nodes on the same super-step run simultaneously). Understand how to set up multiple outgoing edges from one node. Practice combining results from parallel branches. Also see how streaming output fits into a graph node’s logic.  
* **Suggested Stack:** Python, langgraph, any LLM (with streaming), concurrency libraries (if needed).

### **18\. Agent Development with LangSmith Tracing**

* **Difficulty:** 🔴 Advanced  
* **Core Concepts Covered:** LangSmith observability, tracing requests and outputs, agent evaluation.  
* **Tools & Integrations:** LangSmith (Studio and Engine), any LangChain agent or graph, LLM.  
* **Project Description:** Build an agent or graph (e.g. one of the above) and enable LangSmith tracing. For example, set LANGSMITH\_TRACING=true and run your agent through a few scenarios. Examine the trace in LangSmith Studio: see the call graph, state transitions, and metrics. Optionally, use LangSmith Engine to detect issues.  
* **Key Learning Outcomes:** Learn to integrate LangSmith into development. Understand how requests are captured and visualized. Use the insights (latency, errors, wrong steps) to iteratively improve your agent. Gain skill in thorough evaluation and debugging of agent behavior.  
* **Suggested Stack:** Python, LangChain/Graph agent, LangSmith account (API key), and follow LangSmith quickstart docs.

*Each project above progressively builds on the previous, covering key LangChain/LangGraph features (chains, tools, agents, memory, RAG, graphs, etc.) and common integrations (OpenAI/Claude LLMs, search APIs, Python execution, SQL, vector DBs, etc.). By completing them in order, a learner will gain comprehensive hands-on experience across the full 2025 LangChain/LangGraph ecosystem.*