#!/bin/bash

echo "Upgrading Dist Tools..."

pip install --upgrade setuptools wheel twine

clear
echo "Building Distribution..."

python3 setup.py sdist bdist_wheel

clear
echo "Executing Distribution..."

python3 -m twine upload dist/*

echo "Done!"
