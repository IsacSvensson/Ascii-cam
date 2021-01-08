"""
Contains diverse functions for app
"""
from os import system, name
from time import sleep
import cv2
import keyboard
from image_handler import Img

class ThreadArgs:
    """
    Class for handling connetion between main thread and settings thread
    """
    def __init__(self):
        """
        Inits ThreadsArg class
        """
        self.pressedKey = None
        self.status = True
        self.currentImg = Img()

    def listen(self):
        """
        Listens to the keyboard for input from user to change settings,
        display help section or exit program
        """
        while self.status:
            if keyboard.is_pressed('q'):
                self.status = False
                self.pressedKey = 'q'
                print(self.pressedKey)
                break
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
                self.currentImg.light = self.currentImg.light - 1
                print(self.pressedKey)
            if keyboard.is_pressed('right'):
                self.currentImg.light = self.currentImg.light + 1
                self.pressedKey = 'right'
                print(self.pressedKey)
            if keyboard.is_pressed('h'):
                self.pressedKey = 'h'
                print(self.pressedKey)
            if keyboard.is_pressed('+'):
                self.currentImg.size = self.currentImg.size + 10
                self.pressedKey = '+'
                print(self.pressedKey)
            if keyboard.is_pressed('-'):
                self.currentImg.size = self.currentImg.size - 10
                self.pressedKey = '-'
                print(self.pressedKey)
            if keyboard.is_pressed('.'):
                self.currentImg.size = self.currentImg.size + 10
                self.pressedKey = '.'
                print(self.pressedKey)
            if keyboard.is_pressed(','):
                self.currentImg.size = self.currentImg.size - 10
                self.pressedKey = ','
                print(self.pressedKey)
            sleep(0.1)

class Camera:
    """
    Class for handling opencv camera-object
    """
    def __init__(self):
        """
        Inits Camera class
        """
        self.camObj = cv2.VideoCapture(0)
    def takePhoto(self):
        """
        Takes a snapshot with camera and saves to disk

        Returns:
            Bool: True if success, False if Error
        """
        return_value, image = self.camObj.read()
        if not return_value:
            print("Error: Could not read camera")
            return False
        cv2.imwrite('image.png', image)
        return True
    def destroy(self):
        """
        Destroys cameraobject
        """
        self.camObj.release()
        cv2.destroyAllWindows()

def clear():
    """
    Clears screen
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def adjustmentThread(args):
    """
    Function for the thread

    Params:
        ThreadArgs: args - object of class ThreadArgs
    """
    args.listen()

def helpMenu():
    """
    Function for displaying the help section
    """
    logo = """
                                                                                                                              .         .           
             .8.            d888888o.       ,o888888o.     8 8888  8 8888     ,o888888o.           .8.                   ,8.       ,8.          
            .888.         .`8888:' `88.    8888     `88.   8 8888  8 8888    8888     `88.        .888.                 ,888.     ,888.         
           :88888.        8.`8888.   Y8 ,8 8888       `8.  8 8888  8 8888 ,8 8888       `8.      :88888.               .`8888.   .`8888.        
          . `88888.       `8.`8888.     88 8888            8 8888  8 8888 88 8888               . `88888.             ,8.`8888. ,8.`8888.       
         .8. `88888.       `8.`8888.    88 8888            8 8888  8 8888 88 8888              .8. `88888.           ,8'8.`8888,8^8.`8888.      
        .8`8. `88888.       `8.`8888.   88 8888            8 8888  8 8888 88 8888             .8`8. `88888.         ,8' `8.`8888' `8.`8888.     
       .8' `8. `88888.       `8.`8888.  88 8888            8 8888  8 8888 88 8888            .8' `8. `88888.       ,8'   `8.`88'   `8.`8888.    
      .8'   `8. `88888.  8b   `8.`8888. `8 8888       .8'  8 8888  8 8888 `8 8888       .8' .8'   `8. `88888.     ,8'     `8.`'     `8.`8888.   
     .888888888. `88888. `8b.  ;8.`8888    8888     ,88'   8 8888  8 8888    8888     ,88' .888888888. `88888.   ,8'       `8        `8.`8888.  
    .8'       `8. `88888. `Y8888P ,88P'     `8888888P'     8 8888  8 8888     `8888888P'  .8'       `8. `88888. ,8'         `         `8.`8888.
    """
    menu = """
    --------------------------------------------------------------------------------------------------------------------------------------------
    By Isac Svensson, 2020

    Hot keys:
      h/H       - Help (this menu)
      Up ↑      - Increase contrast
      Down ↓    - Decrease contrast
      Right →   - Increase brightness
      Left ←    - Decrease brightness
      +         - Increase size (by 10)
      -         - Decrease size (by 10)
      .         - Increase size (by 1)
      ,         - Decrease size (by 1)

    Press Enter to go back to camera-mode
    """
    clear()
    print(logo)
    print(menu)
    input()
    clear()
