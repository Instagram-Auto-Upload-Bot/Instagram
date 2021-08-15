import os
from PIL import Image, ImageFont, ImageDraw

class ratio:
    """Attributes: ratio.ratios\n
    ratio.ratios:\n
    `Dict` of ratio tuples for generating Instagram photos:\n
    Keys: `1:1` `1.91:1` `4:5`
    """
    ratios = {
        "1:1": (1080, 1080),
        "1.91:1": (1080, 1350),
        "4:5": (1080, 608)
    }

def photo_gen(*, ratio:tuple, tcolour:str="#000000", bgcolour:str="#FFFFFF", string:str):
    """
    Function that is used to generate photos:\n
    Usage: `photo_gen(ratio="Tuple, can be found in ratio.ratios", tcolour="Hex colour code for the text", bgcolour="Hex colour code for the background", string="Text"):`
    """
    img = Image.new("RGB", ratio, bgcolour)
    string = string

    ftfont = os.path.abspath(
        os.path.join(
            #msjh.ttf Microsoft Jhenghei
            #hogc.ttf HigashiOme Gothic C
            os.path.dirname(__file__), 'fonts/nsscb.ttf'
        )
    )

    font = ImageFont.truetype(font=ftfont, size=75)
    w, h = font.getsize(string)


    draw = ImageDraw.Draw(img)
    draw.text((ratio[0]/2, ratio[1]/2), string,
              font=font, fill=tcolour, anchor="mm", align='center')

    img.save("output.jpg")
    if __name__ == "__main__":
        img.show()

if __name__ == "__main__":
    photo_gen(ratio=ratio.ratios["4:5"], string="awd")
