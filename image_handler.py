from PIL import Image, ImageEnhance

class Img:
    def __init__(self):
        self.img = None
        self.contrast = 0
        self.light = 0

    def loadImage(self, img):
        self.img = img.resize((120,80))
        if self.contrast != 0:
            contrastEnh = ImageEnhance.Contrast(self.img)
            self.img = contrastEnh.enhance(1+self.contrast*0.2)
        if self.light != 0:
            lightEnh = ImageEnhance.Brightness(self.img)
            self.img = lightEnh.enhance(1+self.light*0.2)