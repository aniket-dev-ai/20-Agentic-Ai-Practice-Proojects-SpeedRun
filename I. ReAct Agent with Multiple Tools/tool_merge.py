# tool.py

from tools.calculator import scientific_calculator
from tools.csv_analyzer import load_csv_data
from tools.datetime_tool import date_difference
from tools.pdf_reader import extract_pdf_text
from tools.python_repl import python_repl_tool
from tools.summarizer import summarize_text
from tools.unit_converter_tool import unit_converter , convert_temperature
from tools.weather_tool import get_weather
from tools.web_Search import search_tool


ALL_TOOLS = [
    scientific_calculator,
    load_csv_data,
    date_difference,
    extract_pdf_text,
    python_repl_tool,
    summarize_text,
    unit_converter,
    convert_temperature,
    get_weather,
    search_tool,
]