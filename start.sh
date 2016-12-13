#!/bin/bash

# Enable i2c
modprobe i2c-dev

# Start the pre application
python src/pre.py

# Start resin-wifi-connect
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket
sleep 1
node resin-wifi-connect/src/app.js --clear=false

# Start the post application