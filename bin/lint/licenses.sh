#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

ROOT="$(dirname "$(realpath "$0")")/../.."
source "$ROOT/package.env"

while IFS= read -r -d '' license; do
  original="${license%.license}"

  if [[ ! -e "$original" ]]; then
    echo "Removing orphan license: $license"
    rm "$license"
  fi
done < <(find "$ROOT" -type f -name "*.license" -print0)

SOFTWARE_LIC="MIT"
DATA_LIC="CC-BY-4.0"
PUB_LIC="CC0-1.0"
YEAR=$(date +%Y)

if [[ -n "$COPYRIGHT" ]]; then
    echo "COPYRIGHT is set: $COPYRIGHT"

    LICENSE_FILES=(
        "$ROOT/LICENSE"
        "$ROOT/LICENSES/$SOFTWARE_LIC.txt"
        "$ROOT/configs/REUSE.toml"
        "$ROOT/.zensical.toml"
    )

    for license_file in "${LICENSE_FILES[@]}"; do
        if [[ ! -f "$license_file" ]]; then
            echo "License file $license_file does not exist"
            exit 1
        fi
        if ! grep -Pv '^[^s]+\s*SPDX-' "$license_file" | grep -q "$COPYRIGHT"; then
            echo "License file $license_file does not exist or COPYRIGHT not found"
            exit 1
        fi
        if ! grep -Pv '^[^s]+\s*SPDX-' "$license_file" | grep -q "$YEAR"; then
            echo "Current year ($YEAR) could not be found in $license_file"
            exit 1
        fi
        if ! grep -Pv '^[^s]+\s*SPDX-' "$license_file" | grep -q -e "$SOFTWARE_LIC" -e "$DATA_LIC" -e "$PUB_LIC"; then
            echo "Neither license ($SOFTWARE_LIC) nor ($DATA_LIC) nor ($PUB_LIC) found in $license_file"
            exit 1
        fi
    done
else
    echo "COPYRIGHT is not set or is empty"
    exit 1
fi


LICENSE_SHORT_FILES=(
    "$ROOT/pyproject.toml"
)

for file_path in "${LICENSE_SHORT_FILES[@]}"; do
    if [ ! -f "$file_path" ]; then
        echo "File not found: $file_path"
        exit 1
    fi

    if ! grep -q "$SOFTWARE_LIC" "$file_path"; then
        echo "License ($SOFTWARE_LIC) not found in $file_path"
        exit 1
    fi
done


FILES=()

IGNORE=(
    '^bin/lint/licenses.sh'
    '^bin/install/wrap.sh'
    '^LICENSES/.+$'
    '^configs/prompt/.+$'
    '^configs/REUSE.toml$'
    '^packages/microbial_strain_data_docs/src/.+\.md$'
    '^packages/microbial_strain_data_docs/REUSE.toml$'
    'uv\.lock$'
    'pnpm-lock.yaml'
)

should_ignore() {
    local name="$1"
    for pattern in "${IGNORE[@]}"; do
        if [[ "$name" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

filter_and_collect() {
    local input_file
    while IFS= read -r input_file; do
        [[ -z "$input_file" ]] && continue
        if should_ignore "$input_file"; then
            continue
        fi
        if [[ -e "$input_file" ]]; then
            FILES+=("$input_file")
        fi
    done
}

if [ "$#" -gt 0 ]; then
    filter_and_collect < <(printf "%s\n" "$@")
else
    filter_and_collect < <(git ls-files)
fi


SOFTWARE=(
    '\.py$'
    '\.sh$'
)

CC_BY_FILES=(
    '\.(jpg|png|ico|webp|avif)$'
)

CC0_FILES=(
    '\.gitignore$'
    '\.gitattributes$'
    '\.env$'
    'package\.env$'
    '\.dockerignore$'
    'shellcheckrc$'
    '\.(md|txt|yaml|yml|json|toml)$'
)

MIT_FILES=(
    'Makefile$'
    'Dockerfile$'
)

MIT_FOLDERS=(
    '^packages/microbial_strain_data_schema$'
)

mit_to_annotate=()
ccby_to_annotate=()
cc0_to_annotate=()

matches_pattern() {
    local value="$1"
    shift
    local -a patterns=("$@")

    for pattern in "${patterns[@]}"; do
        if [[ "$value" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

for file in "${FILES[@]}"; do
    file_name="${file##*/}"
    file_dir="${file%/*}"
    if matches_pattern "$file_name" "${SOFTWARE[@]}"; then
        mit_to_annotate+=("$file")
        continue
    fi
    if matches_pattern "$file_name" "${MIT_FILES[@]}"; then
        mit_to_annotate+=("$file")
        continue
    fi
    if matches_pattern "$file_name" "${CC_BY_FILES[@]}"; then
        ccby_to_annotate+=("$file")
        continue
    fi
    if matches_pattern "$file_dir" "${MIT_FOLDERS[@]}"; then
        mit_to_annotate+=("$file")
        continue
    fi
    if matches_pattern "$file_name" "${CC0_FILES[@]}"; then
        cc0_to_annotate+=("$file")
        continue
    fi
done

if [ ${#mit_to_annotate[@]} -gt 0 ]; then
    echo "annotating MIT"
    reuse annotate -c "$COPYRIGHT" -l "$SOFTWARE_LIC" -y "$YEAR" --merge-copyrights --fallback-dot-license "${mit_to_annotate[@]}"
else
    echo "No MIT files to annotate"
fi

if [ ${#ccby_to_annotate[@]} -gt 0 ]; then
    echo "annotating CC-BY"
    reuse annotate -c "$COPYRIGHT" -l "$DATA_LIC" -y "$YEAR" --merge-copyrights --fallback-dot-license "${ccby_to_annotate[@]}"
else
    echo "No CC-BY files to annotate"
fi

if [ ${#cc0_to_annotate[@]} -gt 0 ]; then
    echo "annotating CC0"
    reuse annotate -c "$COPYRIGHT" -l "$PUB_LIC" -y "$YEAR" --merge-copyrights --fallback-dot-license "${cc0_to_annotate[@]}"
else
    echo "No CC0 files to annotate"
fi

if ! reuse lint; then
    echo "Linting failed!"
    exit 1
fi
