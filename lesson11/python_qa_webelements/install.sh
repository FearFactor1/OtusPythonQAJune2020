#!/bin/bash

FILE=env/

if [ -d "$FILE" ]; then
    source env/bin/activate
else
    python3 -m venv env &&
    source env/bin/activate
fi

pip install -U pip &&
pip install -Ur requirements.txt

echo "Done!"