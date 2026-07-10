#!/bin/bash

# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

set -euo pipefail

echo "update"
dnf -y update
echo "installing requirements"
dnf -y install python3.13 python3.13-pip git git-lfs make wget coreutils-single jq vim which
dnf -y group install "Development Tools"
dnf -y install bzip2-devel ncurses-devel libffi-devel \
    readline-devel openssl-devel sqlite-devel tk-devel
ln -s /usr/bin/python3.13 /usr/bin/python
ln -s /usr/bin/pip3.13 /usr/bin/pip
dnf -y install nodejs libatomic
echo "requirements installed"
