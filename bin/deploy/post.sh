#!/bin/bash

PYT="$(pwd)/.venv/bin"
LOC="$HOME/.local/bin"

echo "installing python-radon"
if "$PYT"/python -m pip install "radon>=5.1,<6"; then
    echo "radon successfully installed"
else
    echo "radon already installed"
fi

mkdir -p "$LOC"

if ln -s "$PYT"/radon "$LOC/radon"; then
    echo "link created"
fi
