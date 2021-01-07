from PIL import Image,ImageDraw,ImageFont
import string
from time import sleep


def distributeWeights(chars, minInterval = 0, maxInterval = 255):
    minValue = chars[0][0]
    maxValue = chars[0][0]
    for char in chars:
        if minValue > char[0]:
            minValue = char[0]
        if maxValue < char[0]:
            maxValue = char[0]
    
    toRet = []
    for char in chars:
        toRet.append((minInterval + (char[0] - minValue)*(maxInterval-minInterval)/(maxValue-minValue), char[1]))
    return toRet

def getGeneralSize(chars, font):
    generalWidth = 0
    generalHeight = 0

    for char in chars:
        # get the size of the biggest char
        textWidth, textHeight = font.getsize(char)

        if generalWidth < textWidth:
            generalWidth = textWidth
        if generalHeight < textHeight:
            generalHeight = textHeight
    return generalWidth, generalHeight

def getWeightedChars():
    printables = string.printable
    font = ImageFont.truetype("consola.ttf", 28, encoding="unic")
    generalWidth, generalHeight = getGeneralSize(printables, font)

    chars = []
    for char in printables:
        # calculate darkness of the img
        canvas = Image.new('RGB', (generalWidth, generalHeight), "white")
        draw = ImageDraw.Draw(canvas)
        draw.text((0,0), char, 'black', font)
        pixels = canvas.load()
        totalSum = int()
        for i in range(generalWidth):
            for j in range(generalHeight):
                totalSum = totalSum + sum(pixels[i,j])
        totalSum = totalSum / (generalHeight*generalWidth*3)
        if (totalSum > 190 and totalSum < 191):
            break
        chars.append((abs(totalSum-255), char))
    chars.sort()
    chars = distributeWeights(chars)
    return chars

def getChar(val, chars):
    minDif = None
    for i, char in enumerate(chars):
        if minDif is None:
            minDif = (abs(val-char[0]), i)
        elif minDif[0] > abs(val-char[0]):
            minDif = (abs(val-char[0]), i)
    return chars[minDif[1]][1]

""" 
wChars = getWeightedChars()
print(wChars) """
