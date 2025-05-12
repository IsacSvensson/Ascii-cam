import string
from bisect import bisect_left
from PIL import Image, ImageDraw, ImageFont
from functools import cache

class AsciiFont:
    def __init__(self, font_path, size=28):
        self.font = ImageFont.truetype(font_path, size)
        self.chars = self._weight_chars()

    def _weight_chars(self):
        chars = [c for c in string.printable if c not in string.whitespace]
        _, _, w, h = max(self.font.getbbox(c) for c in chars)
        weighted = []
        for char in chars:
            img = Image.new('L', (w, h), 255)
            ImageDraw.Draw(img).text((0, 0), char, fill=0, font=self.font)
            brightness = sum(img.getdata()) / (w * h)
            weighted.append((255 - brightness, char))
        weighted.sort()
        values = [(v, c) for v, c in weighted]
        return values

    @cache
    def get_char(self, val):
        idx = bisect_left([w[0] for w in self.chars], val)
        idx = min(idx, len(self.chars) - 1)
        return self.chars[idx][1]

    def render_ascii(self, img_obj):
        if img_obj.img is None:
            return "[Waiting for camera...]"
        w, h = img_obj.img.size
        pix = img_obj.img.load()
        return "\n".join(
            ''.join(self.get_char(pix[x, y]) * 2 for x in range(w)) for y in range(h)
        )