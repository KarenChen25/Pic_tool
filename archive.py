import os
from os import walk
from PIL import Image, ImageFilter

GAME_TYPE_LIST = [7,8,9,12,14,15,18]
LANG_LIST = ['cn','en','tw']
GAME_FOLDER_LIST = ['01_Slot','04_Fish','05_BarGame','07_Bingo','08_Card']
for t in GAME_FOLDER_LIST:
  dirPath = r"Y:\02_game\{}".format(t)
  for dirs in os.listdir(dirPath):
    print("目錄：", dirs)
    for n in GAME_TYPE_LIST:
        for m in range (0,999):
            for l in LANG_LIST:
                for t in GAME_FOLDER_LIST:
                  mt = str(n) + str('%03d' %m)
                  if mt in dirs:
                    file_path = (r"C:\Users\yasakakumo\Desktop\208x170\{}_208x170_{}.png".format(mt,l)) #檔案所在的資料夾
                    pathroot = (r"{}\{}\01_Web_source\WEB_Icon{}".format(dirPath,dirs,mt))

                    if os.path.isfile(file_path): 
                      if not os.path.isdir(pathroot):
                          print("where is the fucking folder? "+pathroot)
                          continue
                    if os.path.isfile(file_path):
                      im = Image.open(file_path)
                      im.save(r"{}\{}_208x170_{}.png".format(pathroot,mt,l),'png') #檔案搬移到的資料夾