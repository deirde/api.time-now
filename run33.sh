#!/bin/bash

sudo kill -9 $(sudo lsof -t -i:8080) &> /dev/null
pip3 install setuptools
pip3 install -r requirements
python3 bootstrap.py
