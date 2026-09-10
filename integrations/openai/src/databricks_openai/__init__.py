"""
**Re-exported Unity Catalog Utilities**

This module re-exports selected utilities from the Unity Catalog open source package.

Available aliases:

- :class:`databricks_openai.UCFunctionToolkit`
- :class:`databricks_openai.DatabricksFunctionClient`
- :func:`databricks_openai.set_uc_function_client`

Refer to the Unity Catalog `documentation <https://docs.unitycatalog.io/ai/integrations/openai/#using-unity-catalog-ai-with-the-openai-sdk>`_ for more information.
"""

from importlib import import_module
from typing import Any

_EXPORTS = {
    "set_uc_function_client": ("unitycatalog.ai.core.base", "set_uc_function_client"),
    "DatabricksFunctionClient": (
        "unitycatalog.ai.core.databricks",
        "DatabricksFunctionClient",
    ),
    "UCFunctionToolkit": ("unitycatalog.ai.openai.toolkit", "UCFunctionToolkit"),
    "McpServerToolkit": (
        "databricks_openai.mcp_server_toolkit",
        "McpServerToolkit",
    ),
    "ToolInfo": ("databricks_openai.mcp_server_toolkit", "ToolInfo"),
    "AsyncDatabricksOpenAI": (
        "databricks_openai.utils.clients",
        "AsyncDatabricksOpenAI",
    ),
    "DatabricksOpenAI": ("databricks_openai.utils.clients", "DatabricksOpenAI"),
    "VectorSearchRetrieverTool": (
        "databricks_openai.vector_search_retriever_tool",
        "VectorSearchRetrieverTool",
    ),
}


def __getattr__(name: str) -> Any:
    """Load public integrations only when callers request them."""
    target = _EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attribute = target
    value = getattr(import_module(module_name), attribute)
    globals()[name] = value
    return value


# Expose all integrations to users under databricks-openai
__all__ = [
    "VectorSearchRetrieverTool",
    "UCFunctionToolkit",
    "DatabricksFunctionClient",
    "set_uc_function_client",
    "DatabricksOpenAI",
    "AsyncDatabricksOpenAI",
    "McpServerToolkit",
    "ToolInfo",
]
