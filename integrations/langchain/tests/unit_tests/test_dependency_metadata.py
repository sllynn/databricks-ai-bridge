import subprocess
import sys
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


def test_standard_import_does_not_eagerly_load_unrelated_integrations():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from databricks_langchain import ChatDatabricks; "
            "import sys; "
            "assert 'databricks_langchain.checkpoint' not in sys.modules; "
            "assert 'databricks_langchain.genie' not in sys.modules; "
            "assert 'databricks_langchain.vectorstores' not in sys.modules",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
