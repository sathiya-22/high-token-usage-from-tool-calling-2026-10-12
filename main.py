from agent_local_cache.tools import define_tools
from agent_local_cache.cache import LocalContextCache
from agent_local_cache.executor import ToolExecutor

def simulate_agent_behavior(executor: ToolExecutor):
    """
    Simulates an agent making tool calls to demonstrate caching.
    """
    print("\n--- Simulating Agent Behavior ---")

    # Scenario 1: First call to get_weather (should hit actual tool)
    print("\nAgent asks for weather in London (first time)...")
    weather_london_1 = executor.execute("get_weather", {"location": "london"})
    print(f"Result 1: {weather_london_1}")

    # Scenario 2: Second call to get_weather with same args (should hit cache)
    print("\nAgent asks for weather in London AGAIN (should hit cache)...")
    weather_london_2 = executor.execute("get_weather", {"location": "london"})
    print(f"Result 2: {weather_london_2}")

    # Scenario 3: Call to get_weather with different args (should hit actual tool)
    print("\nAgent asks for weather in New York (first time)...")
    weather_ny_1 = executor.execute("get_weather", {"location": "new york"})
    print(f"Result 3: {weather_ny_1}")

    # Scenario 4: First call to search_wikipedia
    print("\nAgent searches Wikipedia for 'Python' (first time)...")
    wiki_python_1 = executor.execute("search_wikipedia", {"query": "Python programming language"})
    print(f"Result 4: {wiki_python_1}")

    # Scenario 5: Second call to search_wikipedia with same args (should hit cache)
    print("\nAgent searches Wikipedia for 'Python' AGAIN (should hit cache)...")
    wiki_python_2 = executor.execute("search_wikipedia", {"query": "Python programming language"})
    print(f"Result 5: {wiki_python_2}")

    # Scenario 6: First call to get_product_price
    print("\nAgent asks for price of prod123 (first time)...")
    price_1 = executor.execute("get_product_price", {"product_id": "prod123"})
    print(f"Result 6: {price_1}")

    # Scenario 7: Second call to get_product_price with same args (should hit cache)
    print("\nAgent asks for price of prod123 AGAIN (should hit cache)...")
    price_2 = executor.execute("get_product_price", {"product_id": "prod123"})
    print(f"Result 7: {price_2}")

    # Scenario 8: Call to a non-existent product (should hit actual tool and not cache, then store)
    print("\nAgent asks for price of prod999 (first time, not found)...")
    price_not_found = executor.execute("get_product_price", {"product_id": "prod999"})
    print(f"Result 8: {price_not_found}")

    # Scenario 9: Second call to a non-existent product (should hit cache now)
    print("\nAgent asks for price of prod999 AGAIN (should hit cache)...")
    price_not_found_2 = executor.execute("get_product_price", {"product_id": "prod999"})
    print(f"Result 9: {price_not_found_2}")


if __name__ == "__main__":
    # 1. Define available tools
    tools = define_tools()

    # 2. Initialize the local context cache
    cache = LocalContextCache()

    # 3. Create a ToolExecutor, integrating tools and cache
    tool_executor = ToolExecutor(tools, cache)

    # 4. Simulate agent behavior
    simulate_agent_behavior(tool_executor)

    print("\n--- Demonstrating Cache Clearing ---")
    cache.clear()

    print("\nAgent asks for weather in London AFTER cache clear (should hit actual tool again)...")
    weather_london_after_clear = tool_executor.execute("get_weather", {"location": "london"})
    print(f"Result after clear: {weather_london_after_clear}")
