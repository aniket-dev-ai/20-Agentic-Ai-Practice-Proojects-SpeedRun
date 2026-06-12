from langchain.tools import tool
from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()

@tool
def python_repl_tool(code: str) -> str:
    """A Python shell.

    Use this to execute python commands.

    Input should be a valid python command.

    If you want to see the output of a value, you should print it out with `print(...)`.
    """
    return python_repl.run(code)
 