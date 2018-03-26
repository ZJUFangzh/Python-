import os
from PIL import Image

pathDir = 'F:\\123'
os.chdir(pathDir)


def get_imglist():
    img_list = []
    list_dir = os.listdir(pathDir)
    for x in list_dir:
        if '.jpg' in x:
            img_list.append(x)
        else:
            print("This is not a picture: " + x)
    return img_list


def modify_imgsize():
    for filename in get_imglist():
        img = Image.open(filename)
        if max(img.size) > 1136:
            value = max(img.size) / 1136
            newsize = (int(img.size[0] / value), int(img.size[1] / value))
            newimg = img.resize(newsize)
            newimg.save('new_' + filename)
        else:
            print("This picture is availabe:" + filename)


modify_imgsize()
