#!/bin/bash

echo "update"
dnf -y update
echo "installing requirements"
dnf -y install rust cargo python3 python3-pip git git-lfs make wget coreutils-single jq vim
dnf -y group install "Development Tools"
dnf -y install bzip2-devel ncurses-devel libffi-devel \
    readline-devel openssl-devel sqlite-devel tk-devel
ln -s /usr/bin/python3 /usr/bin/python
echo "requirements installed"
