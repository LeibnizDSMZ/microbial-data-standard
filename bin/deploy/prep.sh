#!/bin/bash

root_path=$(dirname "$(realpath "$0")")

echo "prep setup"
dnf clean all && rm -rf /var/cache/dnf
dnf -y install dnf-plugins-core
dnf upgrade --refresh -y
echo -e "copy health"
cp "$root_path/health.sh" / && chmod +x /health.sh
echo -e "copy entrypoint"
cp "$root_path/entrypoint.sh" / && chmod +x /entrypoint.sh
echo "prep finished"
