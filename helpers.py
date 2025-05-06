from os import system, name
from sys import stdin
from time import sleep
import cv2
import keyboard
import numpy as np
from PIL import Image, ImageOps
from image_handler import Img
import sys

class CameraThreadArgs:
    def __init__(self, img, settings):
        self.camera = Camera()
        self.img = img
        self.setArgs = settings

    def start_cam(self):
        while self.setArgs.status:
            success, frame = self.camera.take_photo()
            if not success:
                self.setArgs.status = False
                break
            im_pil = ImageOps.grayscale(Image.fromarray(frame))
            self.img.load_image(im_pil)
        self.camera.destroy()

class SettingThreadArgs:
    def __init__(self):
        self.pressedKey = None
        self.status = True
        self.currentImg = Img()

    def listen(self):
        key_map = {
            'q': lambda: setattr(self, 'status', False),
            'up': lambda: self.currentImg.adjust_contrast(1),
            'down': lambda: self.currentImg.adjust_contrast(-1),
            'left': lambda: self.currentImg.adjust_light(-1),
            'right': lambda: self.currentImg.adjust_light(1),
            '+': lambda: self.currentImg.adjust_size(10),
            '-': lambda: self.currentImg.adjust_size(-10),
            '.': lambda: self.currentImg.adjust_size(1),
            ',': lambda: self.currentImg.adjust_size(-1),
            'r': lambda: self.currentImg.set_default(),
            'h': lambda: None,
        }
        while self.status:
            for key, action in key_map.items():
                if keyboard.is_pressed(key):
                    self.pressedKey = key
                    action()
                    break
            sleep(0.1)

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def take_photo(self):
        ret, frame = self.cam.read()
        if not ret:
            print("Error: Could not read camera")
            return False, None
        return True, frame

    def destroy(self):
        self.cam.release()
        cv2.destroyAllWindows()

def camera_thread(cam_args):
    cam_args.start_cam()

def adjustment_thread(args):
    args.listen()

def clear():
    clear_console()

def help_menu():
    print("""
    ASCII Camera by Isac Svensson
    -----------------------------
    h = Help
    q = Quit
    Arrow keys = Adjust contrast/brightness
    +/-/. , = Adjust image size
    r = Reset settings
    Press Enter to return.
    """)
    input()

def clear_console():
    sys.stdout.write("\033[H")  # ANSI escape sequence
    sys.stdout.flush()