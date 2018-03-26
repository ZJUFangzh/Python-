'''将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image, ImageDraw, ImageFont


def add_text(img):
    # 读取图片信息
    draw = ImageDraw.Draw(img)
    # 创建字体
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=80)
    fillcolor = '#ff0000'
    width, height = img.size
    # 给图片加上文字
    draw.text((40, 40), 'Hello,Miss Zhang', font=myfont, fill=fillcolor)
    img.save(r'C:\Users\Fang\Desktop\result.jpg', 'jpeg')


img = Image.open(r'C:\Users\Fang\Desktop\1.jpg')
add_text(img)
