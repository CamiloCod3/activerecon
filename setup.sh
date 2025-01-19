#!/bin/bash
# Remove old environment and recreate a clean one
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install .
echo "Installation complete. Virtual environment is ready and project is installed."