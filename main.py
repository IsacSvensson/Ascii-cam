"""
Main module for ASCII-CAM app.
Reads pictures from webcamera and generates a ASCII-stream in terminal.
"""
import threading
import msvcrt
from helpers import clear, adjustmentThread, helpMenu, SettingThreadArgs, \
    CameraThreadArgs, cameraThread
from imageHandler import Img
from font import generateAsciiImage, getWeightedChars


def main():
    """
    Main function for app handles camera, creating of thread and
    """
    img = Img()
    settingThreadArgs = SettingThreadArgs()
    chars = getWeightedChars()
    # Include img object in threadArgs to be able to change settings from thread
    settingThreadArgs.currentImg = img
    camThreadArgs = CameraThreadArgs(img, settingThreadArgs)
    # Create and start thread
    settingsThread = threading.Thread(target=adjustmentThread, args=(settingThreadArgs,))
    camThread = threading.Thread(target=cameraThread, args=(camThreadArgs,))
    settingsThread.start()
    camThread.start()
    helpMenu()
    while settingThreadArgs.status:
    # Status sets to false when pressing 'q'
        if settingThreadArgs.pressedKey == 'h':
            # Flushes input buffer
            while msvcrt.kbhit():
                msvcrt.getch()
            helpMenu()
            settingThreadArgs.pressedKey = None
        asciiImage = generateAsciiImage(img, chars)
        clear()
        print(asciiImage)
    # Flushes input buffer
    while msvcrt.kbhit():
        msvcrt.getch()

if __name__ == "__main__":
    main()
