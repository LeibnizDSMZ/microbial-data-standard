#!/bin/bash


ROOT="$(dirname "$(realpath "$0")")/../.."

ROOT_ENV="$ROOT/package.env"

ENV_FILES=( "$ROOT_ENV" "$MSD_M_ENV" "$MSD_U_ENV")

ALL_ENV=(
    "MAKEFILE_LIST"
    "HOME"
    "PATH"
    "MAKE"
)

IGNORE_ENV=(
    "^UV_.*$"
    "^CMD$"
    "^UV$"
)

should_ignore() {
    local name="$1"
    for pattern in "${IGNORE_ENV[@]}"; do
        if [[ "$name" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

check_env_uniqueness() {
    cmd="$(awk 'match($0, /^.*=/) {print substr($0, RSTART, RLENGTH-1)}' "$1")"
    while IFS= read -r name; do
            [[ -z "$name" ]] && continue
            for known in "${ALL_ENV[@]}"; do
                if [[ "$known" = "$name" ]]; then
                    echo "found duplicate in $1 -> $name [FAIL]"
                    exit 1
                fi
            done
            ALL_ENV+=("$name")
    done <<<"$cmd"
}

check_name_occurrence() {
    norm_reg="\${\?$1}\?"
    make_reg="\$($1)"
    docker_reg="\${\?$1}\?\|environment:[[:space:]]*$1"
    if [[ "$2" = 1 ]]; then
        norm_reg="$1[[:space:]]*=[A-Za-z0-9]*"
        make_reg="$1[[:space:]]*[:+?]\?=[A-Za-z0-9]*\|define[[:space:]]*$1"
        docker_reg="$1[[:space:]]*[:=][A-Za-z0-9]*"
    fi
    if [[ "$(grep -Rnw "$ROOT/bin" -e "$norm_reg" | wc -l)" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -cwe "$make_reg" "$ROOT/Makefile")" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -cwe "$docker_reg" "$ROOT/Dockerfile")" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -cwe "$docker_reg" "$ROOT/docker-compose.yml")" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -cwe "$norm_reg" "$ROOT/lefthook.yml")" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -Rnw "$ROOT/.devcontainer" -e "$docker_reg" | wc -l)" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep -Rnw "$ROOT/configs" -e "$norm_reg" | wc -l)" -gt 0 ]]; then
        return 0
    fi
    if [[ "$(grep --exclude-dir=__pycache__ -Rnw "$PKG" -e "$norm_reg" | wc -l)" -gt 0 ]]; then
        return 0
    fi
    if [[ "$2" = 1 ]]; then
        return 1
    fi
    if [[ "$(grep --exclude-dir=__pycache__ -Rnw "$PKG" -e "$1" | wc -l)" -gt 0 ]]; then
        return 0
    fi
    return 1
}

check_name_rev_occurrence() {
    while IFS= read -r name; do
            [[ -z "$name" ]] && continue
            if should_ignore "$name"; then
                continue
            fi
            found=0
            for known in "${ALL_ENV[@]}"; do
                if [[ "$known" = "$name" ]]; then
                    found=1
                    break
                fi
            done
            if [[ "$found" = 0 ]]; then
                check_name_occurrence "$name" 1
                if [[ "$?" = 1 ]]; then
                    echo "[FAIL] could not find $name -> $1"
                    exit 1
                fi
                echo "[OK] $name found"
            fi
            ALL_ENV+=("$name")
    done <<<"$(awk "$2" "$1")"
}

echo "checking env files"
for env in "${ENV_FILES[@]}"; do
    if [[ ! -f "$env" ]]; then
        echo "missing env file -> $env"
    fi
    check_env_uniqueness "$env"
    echo "[OK] $env"
done
echo "-- occurrence check --"
for name in "${ALL_ENV[@]}"; do
    if should_ignore "$name"; then
        continue
    fi
    check_name_occurrence "$name" 0
    if [[ "$?" = 1 ]]; then
        echo "[FAIL] could not find $name"
        exit 1
    fi
    echo "[OK] $name found"
done
echo "-- reverse occurrence check --"
cmd='{
    while (match($0, /\$[({][A-Z_]+[A-Z0-9_]*[)}]/)) {
        print substr($0, RSTART+2, RLENGTH-3);
        $0 = substr($0, RSTART+RLENGTH)
    }
}'
check_name_rev_occurrence "$ROOT/Makefile" "$cmd"
check_name_rev_occurrence "$ROOT/Dockerfile" "$cmd"
check_name_rev_occurrence "$ROOT/docker-compose.yml" "$cmd"

while SEP=' ' read -ra files; do
    for file in "${files[@]}"; do
        check_name_rev_occurrence "$file" "$cmd"
    done
done <<<"$(find "$ROOT/.devcontainer" -type f)"

while SEP=' ' read -ra files; do
    for file in "${files[@]}"; do
        check_name_rev_occurrence "$file" "$cmd"
    done
done <<<"$(find "$ROOT/configs" -type f)"

while SEP=' ' read -ra files; do
    for file in "${files[@]}"; do
        check_name_rev_occurrence "$file" "$cmd"
    done
done <<<"$(find "$PKG" -type f -regex '.*/packages/[^/]*/[^/]*')"

cmd='{
    while (match($0, /\$[A-Z_]+[A-Z0-9_]*/)) {
        print substr($0, RSTART+1, RLENGTH-1);
        $0 = substr($0, RSTART+RLENGTH)
    }
}'
while SEP=' ' read -ra files; do
    for file in "${files[@]}"; do
        check_name_rev_occurrence "$file" "$cmd"
    done
done <<<"$(find "$ROOT/bin" -type f)"

while SEP=' ' read -ra files; do
    for file in "${files[@]}"; do
        check_name_rev_occurrence "$file" "$cmd"
    done
done <<<"$(find "$PKG" -type f -regex '.*/packages/[^/]*/bin/.*')"
