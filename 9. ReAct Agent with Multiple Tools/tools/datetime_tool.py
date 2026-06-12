from datetime import datetime
from langchain.tools import tool


@tool
def date_difference(start_date: str, end_date: str) -> str:
    """
    Calculate the number of days between two dates.

    Args:
        start_date: Date in YYYY-MM-DD format.
        end_date: Date in YYYY-MM-DD format.
    """

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        days = (end - start).days

        return (
            f"Days between {start_date} and {end_date}: "
            f"{abs(days)} days (signed difference: {days})"
        )

    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."
    
                      