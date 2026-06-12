from agent import run_agent
from print import inspect_agent_response

if __name__ == "__main__":
    query = "What is the latest news on WWE?"
    response = run_agent(query)
    print("Agent Response:")
    inspect_agent_response(response)
    