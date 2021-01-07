import keyboard  # using module keyboard
from image_handler import Img
from time import sleep

class pressedKey:
    def __init__(self):
        self.pressedKey = None
        self.status = True
        self.currentImg = Img()

    def listen(self):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    self.status = False
                    self.pressedKey = 'q'
                    print(self.pressedKey)
                    break  # finishing the loop
                if keyboard.is_pressed('up'):
                    self.pressedKey = 'up'
                    self.currentImg.contrast = self.currentImg.contrast + 1
                    print(self.pressedKey)
                if keyboard.is_pressed('down'):
                    self.currentImg.contrast = self.currentImg.contrast - 1
                    self.pressedKey = 'down'
                    print(self.pressedKey)
                if keyboard.is_pressed('left'):
                    self.pressedKey = 'left'
                    self.currentImg.light = self.currentImg.light + 1
                    print(self.pressedKey)
                if keyboard.is_pressed('right'):
                    self.currentImg.light = self.currentImg.light - 1
                    self.pressedKey = 'right'
                    print(self.pressedKey)
                sleep(0.1)
            except:
                break  # if user pressed a key other than the given key the loop will break
