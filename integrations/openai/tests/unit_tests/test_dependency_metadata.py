from pathlib import Path

import tomllib


def test_databricks_connect_is_only_requested_by_explicit_unity_catalog_extra():
    project = tomllib.loads((Path(__file__).parents[2] / "pyproject.toml").read_text())["project"]

    assert "unitycatalog-openai>=0.2.0" in project["dependencies"]
    assert all(
        "unitycatalog-openai[databricks]" not in dependency
        for dependency in project["dependencies"]
    )
    assert project["optional-dependencies"]["unitycatalog-databricks"] == [
        "unitycatalog-openai[databricks]>=0.2.0"
    ]
