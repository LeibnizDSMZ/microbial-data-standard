#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

set -euo pipefail

cmd=()
files=()
found_sep=false

if [[ -f ".venv/bin/activate" ]]; then
  source .venv/bin/activate
fi

for arg in "$@"; do
  if [[ "$arg" == "--" ]]; then
    found_sep=true
    continue
  fi

  if [[ "$found_sep" == false ]]; then
    cmd+=("$arg")
  else
    files+=("$arg")
  fi
done

if [[ "$found_sep" == "false" ]]; then
  "${cmd[@]}"
else
  if [[ "${#files[@]}" -eq 0 ]]; then
    exit 0
  fi
  "${cmd[@]}" "${files[@]}"
fi
