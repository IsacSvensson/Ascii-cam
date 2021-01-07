from PIL import Image
import cv2
from time import sleep
import sys
from ascii_art import generateAsciiImage
from key import *
# import only system from os 
from os import system, name 
import threading
from image_handler import Img

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def adjustmentThread(key):
    key.listen()

def main():
    camera = cv2.VideoCapture(0)
    img = Img()
    key = pressedKey()

    key.currentImg = img
    thread = threading.Thread(target=adjustmentThread, args=(key,))
    thread.start()
    while key.status:
        return_value, image = camera.read()

        cv2.imwrite('image.png', image)
            
        img.loadImage(Image.open("image.png"))
        asciiImage = generateAsciiImage(img)
        clear()
        print(asciiImage)
    del(camera)

if __name__ == "__main__":
    main()