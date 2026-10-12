from typing import Dict, Any, Callable, Optional
import json

class LocalContextCache:
    """
    A simple in-memory cache for tool results.
    This cache stores responses based on tool name and arguments.
    """
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}

    def get(self, tool_name: str, args: Dict[str, Any]) -> Optional[Any]:
        """
        Retrieves a cached result for a given tool call.
        """
        tool_cache = self._cache.get(tool_name)
        if tool_cache:
            # Use JSON serialization of args for a stable cache key
            args_key = json.dumps(args, sort_keys=True)
            return tool_cache.get(args_key)
        return None

    def set(self, tool_name: str, args: Dict[str, Any], result: Any):
        """
        Stores a result for a given tool call in the cache.
        """
        if tool_name not in self._cache:
            self._cache[tool_name] = {}
        args_key = json.dumps(args, sort_keys=True)
        self._cache[tool_name][args_key] = result
        print(f"[Cache] Stored result for '{tool_name}' with args {args}")

    def clear(self):
        """
        Clears the entire cache.
        """
        self._cache = {}
        print("[Cache] Cleared all cache entries.")
