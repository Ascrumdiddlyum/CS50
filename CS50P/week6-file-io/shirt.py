import sys
from PIL import Image, ImageOps
from pathlib import Path

def check_arg(argument):
    if len(argument) < 3:
        sys.exit("Too few command-line arguments")

    if len(argument) > 3:
        sys.exit("Too many command-line arguments")

    for arg in argument[-2:]:
        if not arg.endswith((".jpg", ".jpeg", ".png")):
            sys.exit("Invalid input")


def check_extension(argument):
    ext1 = Path(argument[1]).suffix.lower()
    ext2 = Path(argument[2]).suffix.lower()
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

def paste_img(argument):
    try:
        muppet_img = Image.open(argument[1])
        shirt_img = Image.open("shirt.png")
        shirt_size = shirt_img.size
        fit_muppet = ImageOps.fit(muppet_img, shirt_size)
        fit_muppet.paste(shirt_img, mask=shirt_img)
        fit_muppet.save(argument[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

check_arg(sys.argv)
check_extension(sys.argv)
paste_img(sys.argv)