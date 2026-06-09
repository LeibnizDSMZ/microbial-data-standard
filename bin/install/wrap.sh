#!/usr/bin/env bash

set -euo pipefail

cmd=()
files=()

found_sep=false
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
