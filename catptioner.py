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



def drawText():
    # appearance variables
    img = Image.open(getFilePath())
    font = ImageFont.truetype("cinecavDmono.ttf", 19)

    # size variables
    x, y = (20, 430)
    imgw, imgh = img.size

    # image resizing
    if (imgw, imgh) == (710, 473):
        print("The image is the recommended size.")
    else:
        print("The image is " + str(imgw) + "x" + str(imgh) + "\nResizing image to 710x473.")
        img = img.resize((710, 473), Image.ANTIALIAS)

    # text + background variables
    text = getFullCaption()
    w, h = font.getsize(text)

    # edit the image
    draw = ImageDraw.Draw(img)
    draw.rectangle((x, y, x + w, y + h), fill="black")
    draw.text((x, y), text, fill="white", font=font)
    img.save(getOutputName() + ".jpg")


drawText()
