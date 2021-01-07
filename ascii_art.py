from font import getWeightedChars, getChar

def generateAsciiImage(img):
    chars = getWeightedChars()
    img = img.resize((120,80))
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