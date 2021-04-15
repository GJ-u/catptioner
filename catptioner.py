from PIL import Image, ImageFont, ImageDraw


def getFullCaption():
    inputTone = input("Tone: ")
    tone = ("[ " + inputTone.upper() + " ] ")
    captiontext = input("Caption: ")
    fullCaption = tone + captiontext
    return fullCaption


def getFilePath():
    inputFilePath = input("Enter path to file: ")
    return inputFilePath


def getOutputName():
    outputName = input("Enter output file name: ")
    return outputName


def drawText():
    # appearance variables
    img = Image.open(getFilePath())
    draw = ImageDraw.Draw(img)
    text = getFullCaption()
    font = ImageFont.truetype("cinecavDmono.ttf", 150)

    # size variables
    x, y = (200, 2750)
    w, h = font.getsize(text)

    # edit the image
    draw.rectangle((x, y, x + w, y + h), fill='black')
    draw.text((x, y), text, fill=(250, 250, 250), font=font)
    img.save(getOutputName() + '.jpg')

    # done

drawText()
