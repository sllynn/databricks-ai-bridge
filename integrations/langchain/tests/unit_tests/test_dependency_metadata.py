from pathlib import Path

import tomllib


def test_databricks_connect_is_only_requested_by_explicit_unity_catalog_extra():
    project = tomllib.loads((Path(__file__).parents[2] / "pyproject.toml").read_text())["project"]

    assert "unitycatalog-langchain>=0.3.0" in project["dependencies"]
    assert all(
        "unitycatalog-langchain[databricks]" not in dependency
        for dependency in project["dependencies"]
    )
    assert project["optional-dependencies"]["unitycatalog-databricks"] == [
        "unitycatalog-langchain[databricks]>=0.3.0"
    ]
