#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

set -euo pipefail
root_path=$(dirname "$(realpath "$0")")
source "$root_path/../../package.env"

echo "prep setup"
dnf clean all && rm -rf /var/cache/dnf
update-ca-trust extract
dnf upgrade -y
dnf -y install epel-release
dnf -y install dnf-plugins-core
dnf config-manager --set-enabled crb
dnf upgrade --refresh -y
echo -e "copy health"
cp "$root_path/health.sh" / && chmod +x /health.sh
echo -e "copy entrypoint"
cp "$root_path/entry_dev.sh" /entry_dev.sh && chmod +x /entry_dev.sh
cp "$root_path/entry_prod.sh" /entry.sh && chmod +x /entry.sh
echo "prep finished"
