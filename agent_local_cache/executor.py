from typing import Dict, Any, List
from agent_local_cache.cache import LocalContextCache
from agent_local_cache.tools import Tool

class ToolExecutor:
    """
    Executes tool calls, optionally checking a local cache first.
    """
    def __init__(self, tools: List[Tool], cache: LocalContextCache):
        self.tools_by_name: Dict[str, Tool] = {tool.name: tool for tool in tools}
        self.cache = cache

    def execute(self, tool_name: str, args: Dict[str, Any]) -> Any:
        """
        Executes a tool call. Checks the local cache first.
        """
        # 1. Check local cache
        cached_result = self.cache.get(tool_name, args)
        if cached_result is not None:
            print(f"[ToolExecutor] Cache hit for '{tool_name}' with args {args}. Returning cached result.")
            return cached_result

        # 2. If not in cache, execute the actual tool
        tool = self.tools_by_name.get(tool_name)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found.")

        print(f"[ToolExecutor] Cache miss for '{tool_name}' with args {args}. Executing tool...")
        try:
            result = tool.func(**args)
            # 3. Store result in cache
            self.cache.set(tool_name, args, result)
            return result
        except Exception as e:
            print(f"[ToolExecutor] Error executing tool '{tool_name}': {e}")
            raise
