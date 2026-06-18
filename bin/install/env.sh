#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

declare -A SEEN_FILES

load_env_file() {
    local env_file="$1"
    [ -f "$env_file" ] || return

    [[ -n "${SEEN_FILES[$env_file]}" ]] && return
    SEEN_FILES[$env_file]=1

    while IFS= read -r line || [ -n "$line" ]; do
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ -z "$line" ]] && continue

        if [[ "$line" =~ ^([A-Za-z_][A-Za-z0-9_]*)=(.*)$ ]]; then
            key="${BASH_REMATCH[1]}"
            value="${BASH_REMATCH[2]}"
            value="${value%\"}"
            value="${value#\"}"
            value="${value%\'}"
            value="${value#\'}"

            if [ -z "${!key+x}" ]; then
                printf '%s := %s\n' "$key" "$value"
            fi

            if [[ -f "$value" && "$value" =~ (^\.env|\.env$) && ! "$value" =~ license ]]; then
                load_env_file "$value"
            fi
        fi
    done < "$env_file"
}

for env in "$@"; do
    load_env_file "$env"
done
