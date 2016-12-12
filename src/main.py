#!/usr/bin/env python

import dothat.backlight as backlight
import dothat.lcd as lcd

backlight.rgb(255, 255, 255)
lcd.clear()
lcd.write("Hello World")
