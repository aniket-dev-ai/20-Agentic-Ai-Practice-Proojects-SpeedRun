# 🚀 LangGraph StateGraph Workflows: Advanced LLM Orchestration

**A modular collection of intelligent AI workflows demonstrating sequential, parallel, conditional, and iterative execution using LangGraph and Google Gemini.**

## 📌 Project Overview

As Large Language Models (LLMs) evolve from simple text generators into complex reasoning engines, orchestrating their tasks becomes critical. This project is a comprehensive suite of AI workflows built with **LangGraph**. It demonstrates how to construct highly reliable, multi-step AI systems using state machines.

By modeling processes as Directed Graphs, this repository provides production-ready patterns for **prompt chaining**, **parallel processing**, **iterative refinement**, and **conditional routing**. Whether it's evaluating an essay across multiple criteria simultaneously or auto-generating viral social media posts through an iterative feedback loop, this project serves as a blueprint for advanced AI engineering.

## ✨ Key Features

* **Stateful Execution:** Utilizes LangGraph's `StateGraph` and Python's `TypedDict` to persist and pass data cleanly between workflow nodes.
* **Conditional Routing:** Dynamic decision-making paths based on mathematical computations or LLM-driven sentiment analysis.
* **Iterative Refinement (Self-Correction):** Cyclic multi-agent workflows where LLMs generate, evaluate, and optimize content until quality standards are met.
* **Parallel Processing:** Simultaneous execution of independent LLM tasks (e.g., grading different aspects of an essay) before aggregating results.
* **Structured Output:** Integration with Pydantic schemas to force strict, parsable JSON outputs from the Gemini model.
* **Visual Debugging:** Built-in Mermaid graph generation to visually map and debug AI execution paths.

## 📂 Folder Structure Overview

```text
10. LangGraph StateGraph Workflow
├── Conditional workflow
│   ├── QuadatricEquationWorkflow.ipynb
│   └── ReviewReplyWorkflow.ipynb
├── Iterative workflow
│   └── X post generator.ipynb
├── parallel_workflow
│   ├── first_workflow.ipynb
│   └── llm_workflow.ipynb
└── sequential_workflow
    ├── sequential_workflow-prompt_chaining.ipynb
    ├── sequential_workflow.ipynb
    └── sequential_workflow2.ipynb

```

## 📄 File-by-File Breakdown

| Directory | Notebook | Core Functionality |
| --- | --- | --- |
| **Conditional** | `QuadatricEquationWorkflow` | Solves quadratic equations using a state-machine. Calculates the discriminant and uses conditional logic to route the state to the correct root calculation node. |
| **Conditional** | `ReviewReplyWorkflow` | A sentiment analysis pipeline. Uses structured output to force the LLM to classify a customer review as "positive" or "negative", updating the state accordingly. |
| **Iterative** | `X post generator` | An automated social media engine. Features three specialized agents (Generator, Evaluator, Optimizer) that iteratively draft, review, and refine a post until it passes quality checks or hits a max loop limit. |
| **Parallel** | `first_workflow` | A fast data-processing graph. Calculates cricket batting statistics (strike rate, boundary percentage) across parallel nodes before aggregating them into a final summary. |
| **Parallel** | `llm_workflow` | A multi-agent grading system. Evaluates essays by running independent LLM nodes for language, analysis, and clarity simultaneously, then aggregates scores and feedback. |
| **Sequential** | `sequential_workflow-prompt_chaining` | Demonstrates prompt chaining. Node 1 generates a structured markdown outline from a topic; Node 2 uses that outline to write a complete blog post. |
| **Sequential** | `sequential_workflow` | A hybrid calculation and classification pipeline. Computes a user's BMI mathematically, then passes the result to an LLM to categorize the health status. |
| **Sequential** | `sequential_workflow2` | The foundational building block. A simple, linear Q&A workflow to establish the basics of state tracking and LangGraph node compilation. |

## 🛠️ Tech Stack

* **Frameworks:** LangGraph, LangChain
* **AI/LLM:** Google Gemini API (`gemini-3.1-flash-lite`, `gemini-3.5-flash`)
* **Data Validation:** Pydantic (Structured Outputs)
* **Language:** Python 3.10+
* **Environment:** Jupyter Notebooks, IPython (Mermaid visualization)

## ⚙️ How the System Works

The architecture relies on LangGraph's core principles:

1. **State Definition:** Each workflow defines a strict schema (e.g., `UPSCState`, `tweetState`) to hold inputs, intermediate variables, and outputs.
2. **Nodes:** Python functions or LLM calls that receive the current state, perform logic, and return updates to mutate the state.
3. **Edges:** The wiring that connects nodes.
* *Standard Edges* pass data sequentially or in parallel.
* *Conditional Edges* use custom routing functions to determine the next step based on real-time state values.


4. **Compilation:** The graph is compiled into a highly resilient workflow capable of looping, branching, and aggregating complex operations.

## 🚀 Setup & Run Instructions

1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies:**
```bash
pip install langgraph langchain-google-genai pydantic python-dotenv jupyter

```


3. **Environment Variables:**
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GOOGLE_API_KEY=your_gemini_api_key_here

```


4. **Run the Notebooks:**
Launch Jupyter and execute the `.ipynb` files block by block to see the state machines in action:
```bash
jupyter notebook

```



## 🎯 Use Cases

* **Automated Content Creation:** The prompt-chaining and iterative workflows are perfect for generating high-quality blogs, marketing copy, or social media posts with built-in quality control.
* **Intelligent Document Processing:** The parallel essay grading workflow can be adapted for automated resume parsing, legal document review, or academic grading.
* **Smart Customer Support:** The conditional routing workflow serves as a baseline for triaging customer support tickets based on sentiment and urgency.

## 🔮 Future Improvements

* **Human-in-the-Loop (HITL):** Introduce manual approval checkpoints for iterative generation workflows before final output.
* **API Deployment:** Wrap the compiled LangGraph workflows in FastAPI or LangServe to deploy them as production-ready microservices.
* **Memory Integration:** Attach persistent memory (e.g., SQLite or PostgreSQL backends) to the state graphs to remember user context across multiple sessions.

## 💡 Conclusion

This repository highlights a modern approach to AI development. By moving past simple, zero-shot LLM prompts and embracing stateful, graph-based orchestration, these workflows ensure greater reliability, predictability, and capability in generative AI applications. It is an essential foundation for anyone building scalable, multi-agent LLM systems.