from subprocess import check_output
from PIL import ImageColor

def rgb():
    color_hex = check_output(["grabc"]).decode()
    color = ImageColor.getcolor(color_hex, "RGB")
    return color