"""
Contains the Img class
"""
from PIL import ImageEnhance

class Img:
    """
    Class for handling the current image
    """
    def __init__(self):
        """
        Inits Img class
        """
        self.img = None
        self.contrast = 0
        self.light = 0
        self.size = 180

    def loadImage(self, img):
        """
        Loads the new image and executes current settings

        Params:
            Image: img - PIL.Image.Image object
        """
        self.img = img.resize((self.size, self.size))
        if self.contrast != 0:
            contrastEnh = ImageEnhance.Contrast(self.img)
            self.img = contrastEnh.enhance(1+self.contrast*0.2)
        if self.light != 0:
            lightEnh = ImageEnhance.Brightness(self.img)
            self.img = lightEnh.enhance(1+self.light*0.2)

    def reset(self):
        """
        Resets contrast and brightness to default values
        """
        self.contrast = 0
        self.light = 0