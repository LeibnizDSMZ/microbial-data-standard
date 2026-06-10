import shutil
from dataclasses import fields
import subprocess
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


def git_add_schema_files(schema_paths: SchemaPaths) -> None:
    git_path = shutil.which("git")
    if not git_path:
        raise FileNotFoundError("Git executable not found")
    git_executable = Path(git_path).resolve()
    if not git_executable.exists() or not git_executable.is_file():
        raise FileNotFoundError(f"Invalid git executable: {git_executable}")
    allowed_base = Path.cwd().resolve()
    paths_to_add: list[str] = []
    for field in fields(schema_paths):
        pat = getattr(schema_paths, field.name)
        if not isinstance(pat, Path):
            raise TypeError(f"Unsafe path detected: {pat}")
        pat = pat.resolve()
        if not (allowed_base == pat or allowed_base in pat.parents):
            raise ValueError(f"Path outside allowed directory: {pat}")
        if not pat.exists():
            raise FileNotFoundError(f"Path does not exist: {pat}")
        if "\x00" in (pat_str := str(pat)):
            raise ValueError("invalid path")
        paths_to_add.append(pat_str)
    command = [str(git_executable), "add", *paths_to_add]
    result = subprocess.run(  # noqa: S603
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True,
        shell=False,
        cwd=allowed_base,
        env={"PATH": "/usr/bin:/bin", "LC_ALL": "C"},
        timeout=30,
    )
    if result.returncode:
        raise subprocess.CalledProcessError(
            result.returncode, command, result.stdout, result.stderr
        )
