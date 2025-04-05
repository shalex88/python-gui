#!/bin/bash

sudo apt install python3-venv python3-tk -y && \
python3 -m venv python-gui && \
. ./python-gui/bin/activate && \
pip install -r dependencies.txt && \
./gui-app.py