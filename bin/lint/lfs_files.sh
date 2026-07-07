#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

set -euo pipefail
FILES=()

filter_and_collect() {
    local input_file
    while IFS= read -r input_file; do
        [[ -z "$input_file" ]] && continue
        [[ -e "$input_file" ]] || continue
        FILES+=("$input_file")
    done
}

if [ "$#" -gt 0 ]; then
    filter_and_collect < <(printf "%s\n" "$@")
else
    filter_and_collect < <(git ls-files || true)
fi

mapfile -t LFS_FILES < <(git lfs ls-files -n || true)

declare -A lfs_map
for f in "${LFS_FILES[@]}"; do
    lfs_map["$f"]=1
done

mapfile -t DELETED_FILES < <(git ls-files -d || true)

declare -A deleted_map
for f in "${DELETED_FILES[@]}"; do
    deleted_map["$f"]=1
done

for file in "${FILES[@]}"; do
    if [[ -z "${lfs_map[$file]+x}" ]]; then
        continue
    fi
    if [[ -n "${deleted_map[$file]+x}" ]]; then
        continue
    fi

    size=$(stat --format=%s "$file" 2>/dev/null || echo 0)
    if [ "$size" -eq 0 ]; then
        continue
    fi

    if [ "$size" -gt 512000 ]; then
        echo "LFS file $file is larger than 500 KB ($size bytes). Please reduce its size."
        exit 1
    fi
done
