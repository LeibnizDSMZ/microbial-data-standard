#!/bin/bash

echo "clean setup"
make uninstall
# python
dnf -y remove bzip2-devel ncurses-devel libffi-devel \
    readline-devel openssl-devel sqlite-devel tk-devel
# misc
dnf -y remove git make wget
# TODO: some packages are colliding with systemd-udev dependencies
# dnf -y group remove "Development Tools"
# autoremove
dnf -y autoremove
# mesc
rm -r /var/cache/dnf && rm -rf /etc/pki/rpm-gpg/* && dnf clean all
echo "cleanup finished"
