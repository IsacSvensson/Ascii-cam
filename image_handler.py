from PIL import Image, ImageEnhance

class Img:
    def __init__(self):
        self.img = None
        self.contrast = 0
        self.light = 0

    def loadImage(self, img):
        self.img = img
        if self.contrast:
            contrastEnh = ImageEnhance.Contrast(img)
            contrastEnh.enhance(self.contrast*0.1)
        if self.light:
            lightEnh = ImageEnhance.Brightness(img)
            lightEnh.enhance(self.light*0.1)
