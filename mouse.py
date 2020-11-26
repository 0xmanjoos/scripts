import pyautogui as p
import time
l = []
def main():
        i = 0
        print("Move your mouse around!")
        time.sleep(1)
        while i < 500:
            if p.position() == p.position():
                pass
            else:
                l.append(p.position())
                i += 1
        print("Moving mouse now..")
        time.sleep(1)
        for i in l:
            p.moveTo(i)
if __name__ == "__main__":
    main()
