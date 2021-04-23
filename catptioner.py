#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw


def getFullCaption():
    inputTone = input("Tone: ")
    tone = ("[ " + inputTone.upper() + " ] ")
    captionText = input("Caption: ")
    fullCaption = tone + captionText
    return fullCaption


def getFilePath():
    inputFilePath = input("Enter path to file: ")
    return inputFilePath


def getOutputName():
    outputName = input("Enter output file name: ")
    return outputName


def checkForSplit():
    text = getFullCaption()
    if len(text) >= 42:
        splitStrings = []
        n = (text.find(" ", 42))
        for index in range(0, len(text), n):
            splitStrings.append(text[index: index + n])
        return splitStrings
    else:
        return text


def drawText():
    # appearance variables
    img = Image.open(getFilePath())
    font = ImageFont.truetype("cinecavDmono.ttf", 19)

    # size variables
    x, y = (20, 400)
    imgw, imgh = img.size

    # image resizing
    if (imgw, imgh) == (710, 473):
        print("The image is the recommended size.")
    else:
        print("The image is " + str(imgw) + "x" + str(imgh) + ".\nResizing image to 710x473.")
        img = img.resize((710, 473), Image.ANTIALIAS)

    # text
    captionText = checkForSplit()
    draw = ImageDraw.Draw(img)

    # edit the image and save
    if type(captionText) == list:
        for line in captionText:
            w, h = font.getsize(line)

            draw.rectangle((x, y, x + w, y + h), fill="black")
            draw.text((x, y), line, fill="white", font=font)

            y += 24
        img.save(getOutputName() + ".jpg")
    # less clunky now !
    else:
        y = 430
        w, h = font.getsize(captionText)

        draw.rectangle((x, y, x + w, y + h), fill="black")
        draw.text((x, y), captionText, fill="white", font=font)

        img.save(getOutputName() + ".jpg")


drawText()
