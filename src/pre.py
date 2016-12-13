#!/usr/bin/env python

import subprocess
import dothat.backlight as backlight
import dothat.lcd as lcd

# Get the current SSID
SSID = subprocess.check_output(['iwgetid', '-r'])

# Show status on the LCD display
if SSID != "":
    backlight.rgb(255, 0, 0)
    lcd.clear()
    lcd.write("Not connected")
else:
    backlight.rgb(0, 255, 0)
    lcd.clear()
    lcd.write("SSID: " + SSID)
