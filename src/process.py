#!/usr/bin/env python

import subprocess
import dothat.backlight as backlight
import dothat.lcd as lcd


def main():
    # Get the current SSID
    SSID = None
    try:
        SSID = subprocess.check_output(["iwgetid", "-r"]).strip()
    except subprocess.CalledProcessError:
        # If there is no connection subprocess throws a 'CalledProcessError'
        pass

    # Show status on the LCD display
    if SSID is None:
        backlight.rgb(255, 0, 0)
        lcd.clear()
        lcd.write("Not connected")
    else:
        backlight.rgb(0, 255, 0)
        lcd.clear()
        lcd.write("SSID: " + SSID)


if __name__ == "__main__":
    main()
