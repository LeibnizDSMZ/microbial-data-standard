#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT
set -euo pipefail

declare -A SEEN_FILES

load_env_file() {
    local env_file="$1"

    if [[ "$env_file" != /* ]]; then
        env_file="$(cd "$(dirname "$env_file")" && pwd)/$(basename "$env_file")"
    fi

    [ -f "$env_file" ] || return

    if [[ -n "${SEEN_FILES[$env_file]+x}" ]]; then
        return
    fi
    SEEN_FILES[$env_file]=1

    # shellcheck disable=SC2094
    while IFS= read -r line || [ -n "$line" ]; do
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ -z "$line" ]] && continue

        if [[ "$line" =~ ^([A-Za-z_][A-Za-z0-9_]*)=(.*)$ ]]; then
            key="${BASH_REMATCH[1]}"
            value="${BASH_REMATCH[2]}"

            # Strip quotes
            value="${value%\"}"
            value="${value#\"}"
            value="${value%\'}"
            value="${value#\'}"

            if [ -z "${!key+x}" ]; then
                printf '%s := %s\n' "$key" "$value"
            fi

            if [[ -f "$value" && "$value" =~ (^\.env|\.env$) && ! "$value" =~ license ]]; then
                # shellcheck disable=SC2094
                local base_dir
                base_dir="$(dirname "$env_file")"

                local potential_path="$value"
                if [[ "$potential_path" != /* ]]; then
                    potential_path="$base_dir/$potential_path"
                fi

                load_env_file "$potential_path"
            fi
        fi
    done < "$env_file"
}

for env in "$@"; do
    load_env_file "$env"
done
