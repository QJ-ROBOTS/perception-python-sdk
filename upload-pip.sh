#!/bin/bash

rm -rf dist

bash update-version.sh

python3 -m build

python3 -m twine upload dist/*