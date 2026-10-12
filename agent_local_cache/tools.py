from typing import Callable, Dict, Any, List
from pydantic import BaseModel, Field

class Tool(BaseModel):
    """
    Represents a tool available to the agent.
    """
    name: str = Field(..., description="The unique name of the tool.")
    description: str = Field(..., description="A description of what the tool does.")
    func: Callable[..., Any] = Field(..., exclude=True, description="The actual function implementing the tool's logic.")
    input_schema: Dict[str, Any] = Field(default_factory=dict, description="JSON schema for the tool's input arguments.")

    class Config:
        arbitrary_types_allowed = True

def get_weather(location: str) -> str:
    """Gets the current weather for a specified location."""
    if location.lower() == "london":
        return "It's cloudy with a chance of rain, 15°C."
    elif location.lower() == "new york":
        return "Sunny and clear, 25°C."
    else:
        return f"Weather for {location} not available."

def search_wikipedia(query: str) -> str:
    """Searches Wikipedia for a given query."""
    if "python" in query.lower():
        return "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."
    elif "eiffel tower" in query.lower():
        return "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France."
    else:
        return f"No Wikipedia entry found for '{query}'."

def get_product_price(product_id: str) -> str:
    """Retrieves the price for a given product ID."""
    prices = {"prod123": "$99.99", "prod456": "$19.99"}
    return prices.get(product_id, "Product not found.")

def define_tools() -> List[Tool]:
    """Defines a list of example tools."""
    return [
        Tool(
            name="get_weather",
            description="Gets the current weather for a specified location. Input: {'location': 'string'}",
            func=get_weather,
            input_schema={"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}
        ),
        Tool(
            name="search_wikipedia",
            description="Searches Wikipedia for a given query. Input: {'query': 'string'}",
            func=search_wikipedia,
            input_schema={"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
        ),
        Tool(
            name="get_product_price",
            description="Retrieves the price for a given product ID. Input: {'product_id': 'string'}",
            func=get_product_price,
            input_schema={"type": "object", "properties": {"product_id": {"type": "string"}}, "required": ["product_id"]}
        ),
    ]
