#!/usr/bin/env python

import time
import subprocess
import dothat.touch as touch
import process


def main():
    # Disable touch repeat
    touch.enable_repeat(False)

    while True:
        # Run one process loop
        process.main()

        # Sleep to avoid 100% CPU usage
        time.sleep(5)


@touch.on(touch.BUTTON)
def handle_button(ch, evt):
    # When the button is pressed resin-wifi-connect is started with `--clear'
    # flag set to 'true'. This forces resin-wifi-connect to remove any
    # previously configured WiFi connections.
    print("Button pressed")
    subprocess.call(["node", "resin-wifi-connect/src/app.js", "--clear=true"])


if __name__ == "__main__":
    main()
