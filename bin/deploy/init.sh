#!/bin/bash

pyv="3.11.2"
dist="/tmp/build"
build="$dist/build.tar.gz"
pyenv="$PYENV_ROOT"

echo "install project"
make build && make runBuild
mkdir "$dist" && mv dist/*.tar.gz "$build"
echo "clean python"
make uninstall && rm -rf "$pyenv"
echo "install required python"
dnf -y install gcc openssl-devel bzip2-devel libffi-devel \
    zlib-devel wget make xz
dnf -y remove python3-pip
wget "https://www.python.org/ftp/python/$pyv/Python-$pyv.tar.xz"
tar -xf "Python-$pyv.tar.xz"
cd "Python-$pyv" && ./configure --enable-optimizations
make -j "$(nproc)" && make install
rm /usr/bin/python && ln -s /usr/local/bin/python3 /usr/bin/python
python -V
cd ..
echo "finished python"
python -m pip install "$build"
rm -rf "$dist"
echo "project installed"
