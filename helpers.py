"""
Contains diverse functions for app
"""
from os import system, name
from time import sleep
import cv2
import keyboard
from PIL import Image
from imageHandler import Img

class CameraThreadArgs:
    """
    Class for handling args for camera thread.
    """
    def __init__(self, img, settings):
        self.camera = Camera()
        self.img = img
        self.setArgs = settings
    def startCam(self):
        """
        Continuisly takes new photos til the user press 'q'
        """
        while self.setArgs.status:
            if not self.camera.takePhoto():
            # If error accured exit program
                self.setArgs.status = False
                break
            imgFile = Image.open("image.png")
            self.img.loadImage(imgFile)
        self.camera.destroy()

class SettingThreadArgs:
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
                break
            if keyboard.is_pressed('up'):
                self.pressedKey = 'up'
                self.currentImg.contrast = self.currentImg.contrast + 1
            if keyboard.is_pressed('down'):
                self.currentImg.contrast = self.currentImg.contrast - 1
                self.pressedKey = 'down'
            if keyboard.is_pressed('left'):
                self.pressedKey = 'left'
                self.currentImg.light = self.currentImg.light - 1
            if keyboard.is_pressed('right'):
                self.currentImg.light = self.currentImg.light + 1
                self.pressedKey = 'right'
            if keyboard.is_pressed('h'):
                self.pressedKey = 'h'
            if keyboard.is_pressed('+'):
                self.currentImg.size = self.currentImg.size + 10
                self.pressedKey = '+'
            if keyboard.is_pressed('-'):
                self.currentImg.size = self.currentImg.size - 10
                self.pressedKey = '-'
            if keyboard.is_pressed('.'):
                self.currentImg.size = self.currentImg.size + 10
                self.pressedKey = '.'
            if keyboard.is_pressed(','):
                self.currentImg.size = self.currentImg.size - 10
                self.pressedKey = ','
            sleep(0.1)

class Camera:
    """
    Class for handling opencv camera-object
    """
    def __init__(self):
        """
        Inits Camera class
        """
        self.camObj = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    def takePhoto(self):
        """
        Takes a snapshot with camera and saves to disk

        Returns:
            Bool: True if success, False if Error
        """
        returnValue, image = self.camObj.read()
        if not returnValue:
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

def cameraThread(camArgs):
    """
    Func for camera thread
    """
    camArgs.startCam()

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
