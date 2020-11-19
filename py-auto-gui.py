#!/usr/bin/env python3
import pyautogui as p
def coord():
    while True:
        if p.position() == p.position():
            pass
        else:
            print(p.position())
def popup():
    inp = input("What do you want the alert to say?: ")
    p.alert(text=inp, title='haxxed', button='OK')
def size():
    print(p.size())
def screenshot():
    lol = input("What do you want to name the image: ")
    photo = lol + ".png"        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    p.screenshot(photo)         #  This is for basic demo uses of pyautogui, it seems like a very cool module #
def main():                     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    print("""
[1] Track Mouse Position
[2] Popup
[3] Get Screen Size
[4] Screenshot
""")
    ask = input("Enter: ")
    if ask == "1":
        coord()
    elif ask == "2":
        popup()
    elif ask == "3":
        size()
    elif ask == "4":
        screenshot()
    else:
        print("That was not a choice")
if __name__ == "__main__":
    main()
