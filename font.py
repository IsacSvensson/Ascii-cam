"""
Module for handling weighting chars and drawing the ascii-picture
"""
import string
from PIL import Image, ImageDraw, ImageFont


def distributeWeights(chars, minInterval=0, maxInterval=255):
    """
    Distributes the wheighted characters over the given interval
    Returns a list of tuples countaining the weighted characters

    Params:
        List: chars - Containg tuples with undistributed weight and associated character
        Int: minInterval - minimum value in distributed system
        Int: maxInterval - maximum value in distributed system
    Returns:
        List: tuples countaining distributed weight and character
    """
    minValue = chars[0][0]
    maxValue = chars[0][0]
    for char in chars:
        if minValue > char[0]:
            minValue = char[0]
        if maxValue < char[0]:
            maxValue = char[0]

    toRet = []
    # Distribute values between minInterval and maxInterval
    # (minIntv + (unDistWeight - minVal)*(maxIntv-minIntv)/(maxVal-minVal)
    for char in chars:
        weight = minInterval + (char[0] - minValue)*(maxInterval-minInterval)
        weight = weight / (maxValue-minValue)
        toRet.append((weight, char[1]))
    return toRet

def getGeneralSize(chars, font):
    """
    Calculates the width and height from the largest characters

    Params:
        List: chars - Containing single characters
        Font: font - Object of the class Font in PIL.ImageFont
    Returns:
        int: width
        int: height
    """
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
    """
    Creates a list of all printable characters, calculates the "blackness" of
    the characters and then create and return a distibuted list of the characters

    Returns:
        List: Containing tuples with weight and the character
    """
    printables = string.printable
    font = ImageFont.truetype("consola.ttf", 28, encoding="unic")
    generalWidth, generalHeight = getGeneralSize(printables, font)

    chars = []
    for count, char in enumerate(printables):
        # calculate darkness of the img
        canvas = Image.new('RGB', (generalWidth, generalHeight), "white")
        draw = ImageDraw.Draw(canvas)
        draw.text((0, 0), char, 'black', font)
        pixels = canvas.load()
        totalSum = int()
        for i in range(generalWidth):
            for j in range(generalHeight):
                totalSum = totalSum + sum(pixels[i, j])
        totalSum = totalSum / (generalHeight*generalWidth*3)
        if count == 95:
            break
        chars.append((abs(totalSum-255), char))
    chars.sort()
    chars = distributeWeights(chars)
    return chars

def getChar(val, chars):
    """
    Gets a character whith the corresponding "blackness" to the pixel

    Params:
        Numeric value: val - value to match to characters
        List: chars - weighted characters list
    Returns:
        String: Containg one single character
    """
    minDif = None
    for i, char in enumerate(chars):
        if minDif is None:
            minDif = (abs(val-char[0]), i)
        elif minDif[0] > abs(val-char[0]):
            minDif = (abs(val-char[0]), i)
    return chars[minDif[1]][1]


def generateAsciiImage(imgObj, chars):
    """
    Functions for generating the ascii picture

    Params:
        Img: imgObj - Object of class Img
    Returns:
        String: Containing the picture as ASCII-art
    """
    img = imgObj.img
    size = img.size
    pix = img.load()
    val = []
    for i in range(0, size[1]):
        val.append([])
        for j in range(0, size[0]):
            val[i].append((pix[j, i][0]*0.299 + pix[j, i][1]*0.587 + pix[j, i][2]*0.114))

    toPrint = str()
    for i in range(0, size[1]):
        row = str()
        for j in range(0, size[0]):
            row = row + getChar(val[i][j], chars)*3
        toPrint = toPrint + '\n' + row
    return toPrint
