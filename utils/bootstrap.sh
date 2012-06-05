#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Not running in a virtualenv???  That's just crazy... I'm out."
    exit 1
fi

# Setup the core first
pip install --upgrade nose coverage
pip install --upgrade -r requirements.txt
python setup.py develop
