#!/bin/bash

dist="/tmp/build"
build="$dist/build.tar.gz"

echo "install project"
make build && make runBuild
mkdir "$dist" && mv dist/*.tar.gz "$build"
echo "project build"
