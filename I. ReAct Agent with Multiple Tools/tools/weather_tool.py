from langchain_community.utilities.openweathermap import OpenWeatherMapAPIWrapper
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Initialize the wrapper (ensure OPENWEATHERMAP_API_KEY is set in your environment)
weather_wrapper = OpenWeatherMapAPIWrapper()

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a specific location."""
    return weather_wrapper.run(location)

# Now you can pass 'get_weather' to your agent's tool list