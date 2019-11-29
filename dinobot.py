# http://www.trex-game.skipser.com/
from PIL import ImageGrab,ImageOps
import pyautogui,time
from numpy import *

time.sleep(3)
# pyautogui.click(pyautogui.locateCenterOnScreen('dino.png'))

class Coordinates():
    replaybtn=(953,466)
    dinosaur=(673,500)

def replaygame():
    pyautogui.click(Coordinates.replaybtn)

def pressspace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jumpu")
    pyautogui.keyUp('space')

def imageGrab():
    box=(Coordinates.dinosaur[0],Coordinates.dinosaur[1],Coordinates.dinosaur[0]+715,Coordinates.dinosaur[1]+31)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return a.sum()


def main():
    replaygame()
    while True:
        if (imageGrab !=1208):
            pressspace()
            time.sleep(0.1)


main()