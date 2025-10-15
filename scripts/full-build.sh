# !/bin/bash
# Clear previous builds
rm -rf build/ dist/ src/*.c src/*.cpp src/*.so

# Automatically detect project root (directory containing this script, then go up one level)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Add project root to PYTHONPATH
export PYTHONPATH="$PROJECT_ROOT:$PYTHONPATH"
echo "Project Module Path: $PYTHONPATH"


# Build the project from .toml file
pip install .