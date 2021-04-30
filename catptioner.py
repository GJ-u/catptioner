#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw


def get_full_caption():
    input_tone = input("Tone: ")
    tone = ("[ " + input_tone.upper() + " ] ")
    caption_text = input("Caption: ")
    full_caption = tone + caption_text
    return full_caption


def get_file_path():
    input_file_path = input("Enter path to file: ")
    return input_file_path


def get_output_name():
    output_name = input("Enter output file name: ")
    return output_name


def split_caption_lines():
    text = get_full_caption()
    if len(text) >= 42:
        split_strings = []
        num = (text.find(" ", 42))
        for index in range(0, len(text), num):
            split_strings.append(text[index: index + num])
        if len(split_strings) >= 4:
            print("The caption is too long, please type a shorter caption.\n")
            return split_caption_lines()
        return split_strings
    return text


def draw_text():

    # appearance variables
    img = Image.open(get_file_path())
    font = ImageFont.truetype("cinecavDmono.ttf", 19)

    # size variables
    x, y = (20, 436)
    imgw, imgh = img.size

    # image resizing
    if (imgw, imgh) == (710, 473):
        print("The image is the recommended size.")
    else:
        print("The image is " + str(imgw) + "x" + str(imgh) + ".\nResizing image to 710x473.")
        img = img.resize((710, 473), Image.ANTIALIAS)

    # text
    caption_text = split_caption_lines()
    draw = ImageDraw.Draw(img)

    # edit the image and save
    if isinstance(caption_text, list):
        for line in reversed(caption_text):
            w, h = font.getsize(line)

            draw.rectangle((x, y, x + w, y + h), fill="black")
            draw.text((x, y), line, fill="white", font=font)

            y -= 23
        img.save(get_output_name() + ".jpg")
        # less clunky now !
    else:
        y = 436
        w, h = font.getsize(caption_text)

        draw.rectangle((x, y, x + w, y + h), fill="black")
        draw.text((x, y), caption_text, fill="white", font=font)

        img.save(get_output_name() + ".jpg")


draw_text()
