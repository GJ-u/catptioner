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
        text = splitStrings[0]
        nextText = splitStrings[1]
        return text, nextText
    else:
        return text


def drawText():
    # appearance variables
    img = Image.open(getFilePath())
    font = ImageFont.truetype("cinecavDmono.ttf", 19)

    # size variables
    x, y = (20, 430)
    x2, y2 = (20, 407)
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
    if type(captionText) == tuple:
        w, h = font.getsize(captionText[1])
        w2, h2 = font.getsize((captionText[0]))

        draw.rectangle((x, y, x + w, y + h), fill="black")
        draw.rectangle((x2, y2, x2 + w2, y2 + h2), fill="black")

        draw.text((x2, y2), captionText[0], fill="white", font=font)
        draw.text((x, y), captionText[1], fill="white", font=font)

        img.save(getOutputName() + ".jpg")

    # yes i know this is clunky sorry

    else:
        w, h = font.getsize(captionText)

        draw.rectangle((x, y, x + w, y + h), fill="black")
        draw.text((x, y), captionText, fill="white", font=font)

        img.save(getOutputName() + ".jpg")


drawText()
