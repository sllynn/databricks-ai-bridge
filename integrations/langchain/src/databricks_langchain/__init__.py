"""
**Re-exported Unity Catalog Utilities**

This module re-exports selected utilities from the Unity Catalog open source package.

Available aliases:

- :class:`databricks_langchain.UCFunctionToolkit`
- :class:`databricks_langchain.UnityCatalogTool`
- :class:`databricks_langchain.DatabricksFunctionClient`
- :func:`databricks_langchain.set_uc_function_client`

Refer to the Unity Catalog `documentation <https://docs.unitycatalog.io/ai/integrations/langchain/#using-unity-catalog-ai-with-langchain>`_ for more information.
"""

from importlib import import_module
from typing import Any

_EXPORTS = {
    "ChatDatabricks": ("databricks_langchain.chat_models", "ChatDatabricks"),
    "AsyncCheckpointSaver": (
        "databricks_langchain.checkpoint",
        "AsyncCheckpointSaver",
    ),
    "CheckpointSaver": ("databricks_langchain.checkpoint", "CheckpointSaver"),
    "DatabricksEmbeddings": (
        "databricks_langchain.embeddings",
        "DatabricksEmbeddings",
    ),
    "GenieAgent": ("databricks_langchain.genie", "GenieAgent"),
    "DatabricksMCPServer": (
        "databricks_langchain.multi_server_mcp_client",
        "DatabricksMCPServer",
    ),
    "DatabricksMultiServerMCPClient": (
        "databricks_langchain.multi_server_mcp_client",
        "DatabricksMultiServerMCPClient",
    ),
    "MCPServer": ("databricks_langchain.multi_server_mcp_client", "MCPServer"),
    "AsyncDatabricksStore": ("databricks_langchain.store", "AsyncDatabricksStore"),
    "DatabricksStore": ("databricks_langchain.store", "DatabricksStore"),
    "VectorSearchRetrieverTool": (
        "databricks_langchain.vector_search_retriever_tool",
        "VectorSearchRetrieverTool",
    ),
    "DatabricksVectorSearch": (
        "databricks_langchain.vectorstores",
        "DatabricksVectorSearch",
    ),
    "set_uc_function_client": ("unitycatalog.ai.core.base", "set_uc_function_client"),
    "DatabricksFunctionClient": (
        "unitycatalog.ai.core.databricks",
        "DatabricksFunctionClient",
    ),
    "UCFunctionToolkit": ("unitycatalog.ai.langchain.toolkit", "UCFunctionToolkit"),
    "UnityCatalogTool": ("unitycatalog.ai.langchain.toolkit", "UnityCatalogTool"),
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


# Expose all integrations to users under databricks-langchain
__all__ = [
    "AsyncCheckpointSaver",
    "AsyncDatabricksStore",
    "ChatDatabricks",
    "CheckpointSaver",
    "DatabricksEmbeddings",
    "DatabricksStore",
    "DatabricksVectorSearch",
    "GenieAgent",
    "VectorSearchRetrieverTool",
    "UCFunctionToolkit",
    "UnityCatalogTool",
    "DatabricksFunctionClient",
    "set_uc_function_client",
    "DatabricksMultiServerMCPClient",
    "DatabricksMCPServer",
    "MCPServer",
]
