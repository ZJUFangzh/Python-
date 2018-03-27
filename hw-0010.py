from hw_0001 import generate
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageFilter

import random
import string


def getRandomColor():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))


def getCodePic():
    width = 240
    height = 60
    img = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 40)
    draw = ImageDraw.Draw(img)
    code = generate(4, 1)
    for t in range(4):
        draw.text((60 * t + 10, 0), code[0][t],
                  font=font, fill=getRandomColor())
    for _ in range(random.randint(1500, 3000)):
        draw.point((random.randint(0, width), random.randint(0, height)),
                   fill=getRandomColor())
    img = img.filter(ImageFilter.BLUR)
    img.save('123.jpg', 'jpeg')


getCodePic()
print(generate(4, 1)[0][0])
