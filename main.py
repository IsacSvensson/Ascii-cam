from PIL import Image
import cv2
from time import sleep
import sys
from ascii_art import generateAsciiImage
# import only system from os 
from os import system, name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():
    camera = cv2.VideoCapture(0)

    count = 0
    while count < 10:
        return_value, image = camera.read()

        cv2.imwrite('image.png', image)
        count += 1
            
        img = Image.open("image.png")
        asciiImage = generateAsciiImage(img)
        clear()
        print(asciiImage)
    
    del(camera)

if __name__ == "__main__":
    main()