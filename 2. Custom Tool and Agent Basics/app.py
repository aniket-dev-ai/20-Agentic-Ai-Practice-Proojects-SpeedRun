from Agent.agent import run_agent
from print import inspect_agent_response

query = "What is the capital of France and what is 5 multiplied by 7?"


response = run_agent(query)
inspect_agent_response(response)