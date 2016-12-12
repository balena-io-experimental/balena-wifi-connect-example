#!/bin/bash

# Enable i2c
modprobe i2c-dev

# Start the python application
python src/main.py
