#!/bin/bash

echo "update"
dnf -y update
echo "installing requirements"
dnf -y install python3 python3-pip git git-lfs make wget coreutils-single rust cargo
dnf -y group install "Development Tools"
dnf -y install bzip2-devel ncurses-devel libffi-devel \
    readline-devel openssl-devel sqlite-devel tk-devel
ln -s /usr/bin/python3 /usr/bin/python
curl https://pyenv.run | bash
echo "installing mariadb client devel"
wget https://r.mariadb.com/downloads/mariadb_repo_setup
chmod +x mariadb_repo_setup && ./mariadb_repo_setup --skip-check-installed
dnf -y install MariaDB-shared MariaDB-devel MariaDB-client
rm mariadb_repo_setup
echo "requirements installed"
