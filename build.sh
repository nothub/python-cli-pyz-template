#!/usr/bin/env bash

set -e

pip3 install zipapps -U

# docker
if ! python3 -m zipapps --version >/dev/null 2>&1; then
  pip3 install zipapps -U
fi

python3 -m zipapps -c -a main.py -m main -o app -r requirements.txt -p "/usr/bin/env python3"
