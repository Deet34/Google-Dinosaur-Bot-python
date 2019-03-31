from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates:
    replayBtn = (480, 445)
    dinosaur = (260, 475)

def restart():
    pyautogui.click(Cordinates.replayBtn)

def space():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    time.sleep(0.17)
    #print("Jump")
    pyautogui.keyUp("space")



def main():
    dis = 130
    sp = 0.17

    def space():
        pyautogui.keyUp("down")
        pyautogui.keyDown("space")
        time.sleep(sp)
        # print("Jump")
        pyautogui.keyUp("space")

    def imageGrab():
        box = (
        Cordinates.dinosaur[0], Cordinates.dinosaur[1], Cordinates.dinosaur[0] + dis, Cordinates.dinosaur[1] + 10)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        #print(a.sum())
        return a.sum()

    restart()
    t = time.time()
    gr = 1547
    sek = 10
    grPlus = 150
    disPlus = 15
    s = 0

    while True:
        if imageGrab() != gr:
            space()


        else:
            pyautogui.keyDown("down")


        if time.time() - t > 10:
            print(f"Zwiększam skok - {sek} sekund mineło")
            gr += grPlus
            dis += disPlus
            t += 10
            sek += 10
            s += 10


        if s == 50:
            sp = 0


        if s == 60:
            grPlus *= 2
            disPlus *= 2
            s = 0


main()