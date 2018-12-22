# led_shim_loop_png
Loop a PNG file on your LED SHIM from Pimoroni

Inspired by the technic used by Pimoroni to colour the keybow-firmware (see https://github.com/pimoroni/keybow-firmware), I wanted to replicated this on other LED only hardware.

I choosed the CharlyPlex 28 RGB LED from @Pimoroni LED SHIM (see https://github.com/pimoroni/led-shim) because that is a lot of RGB on a single line with a simple API.

The idea is to have a PNG file that contain on each line the RGB colour you want for your LED. Two format are supported, the 1 pixel wide format will control all the LED with the same colour and the 28 pixels wide format that control each LED individually. If you have less that 28 pixels, not all LED will be used, if you have more pixels, only the first 28 pixels will be used.

To read from PNG file, I used PyPNG (see https://github.com/drj11/pypng) available under MIT licence.

Two samples files are provided and comming directly from keybow firmware:
-* default.png : a 40 pixels wide rainbow
-* heartbeat.png : a one pixel wide red blinking

Usage:
    python3 loop.py file.png

