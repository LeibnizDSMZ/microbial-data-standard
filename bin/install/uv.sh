#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT


ROOT="$(dirname "$(realpath "$0")")/../.."

set -a

source "$ROOT/package.env"

echo "$UV_CACHE_DIR"
echo "$UV_INSTALL_DIR"
echo "$UV_PYTHON_INSTALL_DIR"
echo "$UV_PYTHON_BIN_DIR"
echo "$UV_TOOL_DIR"
echo "$UV_TOOL_BIN_DIR"
echo "$UV_NO_MODIFY_PATH"
echo "$UV_VERSION"

[[ -d "$UV_INSTALL_DIR" ]] || (curl -LsSf "https://astral.sh/uv/$UV_VERSION/install.sh" | sh)
"$UVE" python install "$PYV" --force
rm -rf .venv
"$UVE" venv --python="$PYV" --relocatable --link-mode=copy --seed
"$UVE" pip install --upgrade pip

set +a
