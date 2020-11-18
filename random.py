#!/usr/bin/env python3
import pyautogui as p
i = 0
print("move your mouse around")
while i < 1000:
    if p.position() == p.position():
        pass
    else:
        i += 1
        bits = ""
        bits += str(p.position())
        bits = bits.strip(" () ,")
        bits = bits.replace(',', '')
        bits = bits.replace(" ", "")
        with open("random.txt", "a") as f:
            f.write(bits)
            f.flush()
