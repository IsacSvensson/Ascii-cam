"""
Main module for ASCII-CAM app.
Reads pictures from webcamera and generates a ASCII-stream in terminal.
"""
import threading
import msvcrt
from PIL import Image
from helpers import clear, adjustmentThread, helpMenu, Camera, ThreadArgs
from image_handler import Img
from font import generateAsciiImage


def main():
    """
    Main function for app handles camera, creating of thread and
    """
    camera = Camera()
    img = Img()
    threadArgs = ThreadArgs()

    # Include img object in threadArgs to be able to change settings from thread
    threadArgs.currentImg = img
    # Create and start thread
    thread = threading.Thread(target=adjustmentThread, args=(threadArgs,))
    thread.start()
    helpMenu()
    while threadArgs.status:
    # Status sets to false when pressing 'q'
        if threadArgs.pressedKey == 'h':
            # Flushes input buffer
            while msvcrt.kbhit():
                msvcrt.getch()
            helpMenu()
            threadArgs.pressedKey = None
        if not camera.takePhoto():
            # If error accured exit program
            threadArgs.status = False
            break
        imgFile = Image.open("image.png")
        img.loadImage(imgFile)
        asciiImage = generateAsciiImage(img)
        clear()
        print(asciiImage)
    camera.destroy()
    # Flushes input buffer
    while msvcrt.kbhit():
        msvcrt.getch()

if __name__ == "__main__":
    main()
