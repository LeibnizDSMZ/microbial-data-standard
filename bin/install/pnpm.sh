#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

set -euo pipefail
ROOT="$(dirname "$(realpath "$0")")/../.."

set -a

source "$ROOT/package.env"

echo "$PNPM_HOME"
echo "$PNPM_VERSION"

if [[ ! -x "$PNPM_HOME" ]]; then
    curl -fsSL https://get.pnpm.io/install.sh | sh -
fi
echo "$PKG_DOCS"
cd "$PKG_DOCS" && "$PNPME" install --frozen-lockfile

set +a
