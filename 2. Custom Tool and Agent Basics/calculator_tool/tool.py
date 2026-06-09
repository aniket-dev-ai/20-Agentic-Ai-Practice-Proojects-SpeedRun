from langchain_core.tools import tool

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """ 
    Args:
        a (float): _description_
        b (float): _description_
        operation (str): _description_

    Raises:
        ValueError: _description_

    Returns:
        float: _description_
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else float('inf')
    else:
        raise ValueError("Invalid operation. Supported operations: add, subtract, multiply, divide.")
