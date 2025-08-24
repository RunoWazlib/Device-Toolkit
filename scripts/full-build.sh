# !/bin/bash
# Clear previous builds
rm -rf build/ dist/ src/*.c src/*.cpp src/*.so
# Build the project from .toml file
pip install -e .