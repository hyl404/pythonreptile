import keyboard
from  PIL import ImageGrab
from time import sleep
import tkinter as tk
from aip import AipOcr
def screenShot():
     if keyboard.wait(hotkey="win+shift+s")==None:
          sleep(0.1)
          image = ImageGrab.grabclipboard()
          image.save('example.jpg')
screenShot()
