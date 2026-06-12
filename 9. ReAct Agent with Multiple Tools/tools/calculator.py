"""
Scientific Calculator Tool

Capabilities:
- Arithmetic
- Algebra
- Equation Solving
- Differentiation
- Integration
- Limits
- Matrix Operations
- Statistics
"""

from typing import Any

import numpy as np
import sympy as sp
from langchain.tools import tool


# @tool
def scientific_calculator(query: str) -> str:
    """
    Perform advanced scientific calculations.

    Scientific Calculator Tool

    Capabilities:
    - Arithmetic
    - Algebra
    - Equation Solving
    - Differentiation
    - Integration
    - Limits
    - Matrix Operations
    - Statistics

    Examples:
        2 + 2
        solve(x**2 + 5*x + 6)
        diff(sin(x))
        integrate(x**2)
        limit(sin(x)/x, x, 0)
        matrix([[1,2],[3,4]])
        mean([1,2,3,4])
    """

    try:
        query = query.strip()

        x = sp.Symbol("x")

        local_dict = {
            "x": x,
            "sin": sp.sin,
            "cos": sp.cos,
            "tan": sp.tan,
            "log": sp.log,
            "sqrt": sp.sqrt,
            "pi": sp.pi,
            "E": sp.E,
        }

        # --------------------------
        # Solve equations
        # --------------------------
        if query.startswith("solve("):
            expr = query[6:-1]
            result = sp.solve(sp.sympify(expr))
            return str(result)

        # --------------------------
        # Differentiate
        # --------------------------
        if query.startswith("diff("):
            expr = query[5:-1]
            result = sp.diff(sp.sympify(expr), x)
            return str(result)

        # --------------------------
        # Integrate
        # --------------------------
        if query.startswith("integrate("):
            expr = query[10:-1]
            result = sp.integrate(sp.sympify(expr), x)
            return str(result)

        # --------------------------
        # Limit
        # --------------------------
        if query.startswith("limit("):
            content = query[6:-1]
            expr, var, value = [
                item.strip() for item in content.split(",")
            ]

            result = sp.limit(
                sp.sympify(expr),
                sp.Symbol(var),
                float(value),
            )

            return str(result)

        # --------------------------
        # Matrix
        # --------------------------
        if query.startswith("matrix("):
            matrix_data = eval(query[7:-1])

            matrix = np.array(matrix_data)

            return (
                f"Matrix:\n{matrix}\n\n"
                f"Determinant: {np.linalg.det(matrix)}\n"
                f"Inverse:\n{np.linalg.inv(matrix)}"
            )

        # --------------------------
        # Statistics
        # --------------------------
        if query.startswith("mean("):
            values = eval(query[5:-1])
            return str(np.mean(values))

        if query.startswith("median("):
            values = eval(query[7:-1])
            return str(np.median(values))

        if query.startswith("std("):
            values = eval(query[4:-1])
            return str(np.std(values))

        # --------------------------
        # General SymPy Evaluation
        # --------------------------
        result = sp.sympify(
            query,
            locals=local_dict,
        )

        return str(sp.N(result))

    except Exception as e:
        return f"Calculation Error: {str(e)}"
    
