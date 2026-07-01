# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

import os
from pathlib import Path
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SchemaPaths:
    json_schema: Path
    docs_mermaid: Path
    docs_schema: Path
    docs_config: Path


def load_schema_paths() -> SchemaPaths:
    json_schema_path = os.getenv("JSON_SCHEMA")
    docs_mermaid_path = os.getenv("DOCS_MERMAID")
    docs_config_path = os.getenv("DOCS_CONFIG")
    docs_schema_path = os.getenv("DOCS_SCHEMA")

    if not json_schema_path:
        raise ValueError("JSON_SCHEMA environment variable not set")
    if not docs_mermaid_path:
        raise ValueError("DOCS_MERMAID environment variable not set")
    if not docs_schema_path:
        raise ValueError("DOCS_SCHEMA environment variable not set")
    if not docs_config_path:
        raise ValueError("DOCS_CONFIG environment variable not set")

    json_schema = Path(json_schema_path)
    docs_mermaid = Path(docs_mermaid_path)
    docs_schema = Path(docs_schema_path)
    docs_config = Path(docs_config_path)

    if not (json_schema.exists() and json_schema.is_file()):
        raise FileNotFoundError(f"JSON schema file does not exist: {json_schema}")

    if not (docs_config.exists() and docs_config.is_file()):
        raise FileNotFoundError(f"Docs config file does not exist: {docs_config}")

    if not (docs_mermaid.exists() and docs_mermaid.is_file()):
        raise FileNotFoundError(f"Docs mermaid file does not exist: {docs_mermaid}")

    if not (docs_schema.exists() and docs_schema.is_dir()):
        raise FileNotFoundError(f"Docs schema directory does not exist: {docs_schema}")

    return SchemaPaths(
        json_schema=json_schema,
        docs_mermaid=docs_mermaid,
        docs_schema=docs_schema,
        docs_config=docs_config,
    )
