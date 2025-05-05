from PIL import ImageEnhance

class Img:
    def __init__(self):
        self.img = None
        self.contrast = 0
        self.light = 0
        self.size = 70

    def set_default(self):
        self.contrast = 0
        self.light = 0
        self.size = 70

    def adjust_light(self, num):
        self.light += num

    def adjust_contrast(self, num):
        self.contrast += num

    def adjust_size(self, num):
        self.size = max(1, self.size + num)

    def load_image(self, img):
        self.img = img.resize((self.size, self.size))
        if self.contrast != 0:
            self.img = ImageEnhance.Contrast(self.img).enhance(1 + self.contrast * 0.2)
        if self.light != 0:
            self.img = ImageEnhance.Brightness(self.img).enhance(1 + self.light * 0.2)
