from PIL import Image, ImageFilter
import os

GAME_TYPE_LIST = [7,8,9,12,15,18]
LANG_LIST = ['cn','en','tw']


# 以下是新增規格
for n in GAME_TYPE_LIST:
    for m in range (0,999):
        for l in LANG_LIST:
            mt = str(n) + str('%03d' %m)
            path = (r"Icon_kit\{}".format(mt))
            if os.path.isfile(path):
                '''
                若MT存在指令範例
                im = Image.open(r"D:\karen\pic_tool\Icon_kit\{}_208x170_{}.png".format(mt,l))
                im.resize((20,170), Image.LANCZOS).save(r"D:\karen\pic_tool\Icon_kit\{}_20x170_{}.png".format(mt,l),'png')
                '''
            else:
                pass





