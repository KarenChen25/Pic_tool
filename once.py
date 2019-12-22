
from PIL import Image, ImageFilter
import os



MT = input('輸入MT：')
path = (r"C:\Icon_all\{}".format(MT))
if not os.path.isdir(path):
    os.mkdir(path)

def get_lang(i):
    if i == 0 :
        return 'cn'
    elif i == 1 :
        return 'en'
    else :
        return 'tw'


# 正方形
for k in range(0,3):
    lang = get_lang(k)
    for i in range(0,8):
        im = Image.open(r"Icon_kit\{}\Square_{}.jpg".format(MT,lang))
        width = [80,128,140,180,200,300,472,500]
        ratio = float(width[i])/im.size[0]#取W值
        height = int(im.size[1]*ratio)
        nim = im.resize( (width[i], height), Image.LANCZOS )
        nim.save(r"C:\\Icon_all\{}\{}_{}x{}_{}.jpg".format(MT,MT,width[i],width[i],lang),'jpeg') #JPG files
        nim.save(r"C:\\Icon_all\{}\{}_{}x{}_{}.png".format(MT,MT,width[i],width[i],lang),'png') #PNG files


# 金框
for k in range(0,3):
    lang = get_lang(k)
    im_circle=Image.open(r"Icon_kit\{}\Circle_{}.png".format(MT,lang))
    cr = im_circle.crop((13,14,486,487))
    nim = cr.resize((128,128), Image.LANCZOS)
    cr2 = im_circle.crop((0,18,500,485))
    nim2 = cr2.resize((146,136), Image.LANCZOS)
    cr3 = im_circle.crop((-497,18,500,485))
    nim3 = cr3.resize((291,136), Image.LANCZOS)
    nim4 = cr2.resize((110,102), Image.LANCZOS)
    nim3.paste( nim4, (18, 17) )
    nim.save(r"C:\\Icon_all\{}\{}_128x128(圓)_{}.png".format(MT,MT,lang),'png')
    nim2.save(r"C:\\Icon_all\{}\{}_146x136(圓)_{}.png".format(MT,MT,lang),'png')
    nim3.save(r"C:\\Icon_all\{}\{}_291x136(圓)_{}.png".format(MT,MT,lang),'png')

# 長方形
for k in range(0,3):
    lang = get_lang(k)
    logo=Image.open(r"Icon_kit\{}\Logo_{}.png".format(MT,lang))
    main=Image.open(r"Icon_kit\{}\Main.png".format(MT))
    if int(main.size[0]) == 1920 :

        # 250*203
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).convert('RGBA')
        main1 = main.crop((320,260,1600,1300))
        rect1 = Image.new("RGBA", bg.size)
        rect1 = Image.alpha_composite(rect1, bg)
        rect1 = Image.alpha_composite(rect1, main1)
        rect1 = Image.alpha_composite(rect1, logo)
        rect1.resize((250,203), Image.LANCZOS).convert('RGB').save(r"C:\\Icon_all\{}\{}_250x203_{}.jpg".format(MT,MT,lang),'jpeg')
        rect1.resize((250,203), Image.LANCZOS).save(r"C:\\Icon_all\{}\{}_250x203_{}.png".format(MT,MT,lang),'png')


        # 190*240
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((300,240), Image.LANCZOS).crop((55,0,245,240)).convert('RGBA')
        main2 = main.crop((360,22,1560,1537)).resize((190,240), Image.LANCZOS)
        logo2 = logo.resize((190,154), Image.LANCZOS).crop((0,-73,190,167))
        award2 = award.resize((250,203), Image.LANCZOS).crop((60,0,250,240))
        rect2 = Image.new("RGBA", bg.size)
        rect2 = Image.alpha_composite(rect2, bg)
        rect2 = Image.alpha_composite(rect2, main2)
        rect2 = Image.alpha_composite(rect2, logo2)
        rect2.convert('RGB').save(r"C:\\Icon_all\{}\{}_190x240_{}.jpg".format(MT,MT,lang),'jpeg')
        rect2.save(r"C:\\Icon_all\{}\{}_190x240_{}.png".format(MT,MT,lang),'png')


        # 338*206
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((338,206), Image.LANCZOS).convert('RGBA')
        main3 = main.crop((130,260,1790,1300)).resize((338,206), Image.LANCZOS)
        logo3 = logo.resize((240,206), Image.LANCZOS).crop((-49,-10,289,196))
        award3 = award.resize((250,203), Image.LANCZOS).crop((-88,0,250,206))
        rect3 = Image.new("RGBA", bg.size)
        rect3 = Image.alpha_composite(rect3, bg)
        rect3 = Image.alpha_composite(rect3, main3)
        rect3 = Image.alpha_composite(rect3, logo3)
        rect3.convert('RGB').save(r"C:\\Icon_all\{}\{}_338x206_{}.jpg".format(MT,MT,lang),'jpeg')
        rect3.save(r"C:\\Icon_all\{}\{}_338x206_{}.png".format(MT,MT,lang),'png')

        # 146*136
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((146,136), Image.LANCZOS).convert('RGBA')
        main4 = main.crop((320,194,1600,1386)).resize((146,136), Image.LANCZOS)
        logo4 = logo.resize((146,119), Image.LANCZOS).crop((0,-21,146,115))
        award4 = award.resize((193,157), Image.LANCZOS).crop((47,0,193,136))
        rect4 = Image.new("RGBA", bg.size)
        rect4 = Image.alpha_composite(rect4, bg)
        rect4 = Image.alpha_composite(rect4, main4)
        rect4 = Image.alpha_composite(rect4, logo4)
        rect4 = Image.alpha_composite(rect4, award4)
        rect4.convert('RGB').save(r"C:\\Icon_all\{}\{}_146x136_{}.jpg".format(MT,MT,lang),'jpeg')
        rect4.save(r"C:\\Icon_all\{}\{}_146x136_{}.png".format(MT,MT,lang),'png')
        
        # 176*234
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((250,234), Image.LANCZOS).crop((36,0,212,234)).convert('RGBA')
        main5 = main.crop((384,16,1536,1544)).resize((176,234), Image.LANCZOS)
        logo5 = logo.resize((176,144), Image.LANCZOS).crop((0,-80,176,154))
        award5 = award.resize((250,203), Image.LANCZOS).crop((74,0,250,234))
        rect5 = Image.new("RGBA", bg.size)
        rect5 = Image.alpha_composite(rect5, bg)
        rect5 = Image.alpha_composite(rect5, main5)
        rect5 = Image.alpha_composite(rect5, logo5)
        rect5.convert('RGB').save(r"C:\\Icon_all\{}\{}_176x234_{}.jpg".format(MT,MT,lang),'jpeg')
        rect5.save(r"C:\\Icon_all\{}\{}_176x234_{}.png".format(MT,MT,lang),'png')

        #208*170
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).convert('RGBA')
        rect1.resize((208,170), Image.LANCZOS).save(r"C:\\Icon_all\{}\{}_208x170_{}.png".format(MT,MT,lang),'png')
    else:
        # 250*203
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).convert('RGBA')
        rect1 = Image.new("RGBA", main.size)
        rect1 = Image.alpha_composite(rect1, bg)
        rect1 = Image.alpha_composite(rect1, main)
        rect1 = Image.alpha_composite(rect1, logo)
        rect1.convert('RGB').resize((250,203), Image.LANCZOS).save(r"C:\\Icon_all\{}\{}_250x203_{}.jpg".format(MT,MT,lang),'jpeg')
        rect1.resize((250,203), Image.LANCZOS).save(r"C:\\Icon_all\{}\{}_250x203_{}.png".format(MT,MT,lang),'png')


        # 190*240
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((300,240), Image.LANCZOS).crop((55,0,245,240)).convert('RGBA')
        main2 = main.resize((190,154), Image.LANCZOS).crop((0,-43,190,197))
        logo2 = logo.resize((190,154), Image.LANCZOS).crop((0,-43,190,197))
        rect2 = Image.new("RGBA", bg.size)
        rect2 = Image.alpha_composite(rect2, bg)
        rect2 = Image.alpha_composite(rect2, main2)
        rect2 = Image.alpha_composite(rect2, logo2)
        rect2.save(r"C:\\Icon_all\{}\{}_190x240_{}.png".format(MT,MT,lang),'png')


        # 338*206
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((338,206), Image.LANCZOS).convert('RGBA')
        main3 = main.resize((240,206), Image.LANCZOS).crop((-49,0,289,206))
        logo3 = logo.resize((240,206), Image.LANCZOS).crop((-49,0,289,206))
        rect3 = Image.new("RGBA", bg.size)
        rect3 = Image.alpha_composite(rect3, bg)
        rect3 = Image.alpha_composite(rect3, main3)
        rect3 = Image.alpha_composite(rect3, logo3)
        rect3.convert('RGB').save(r"C:\\Icon_all\{}\{}_338x206_{}.jpg".format(MT,MT,lang),'jpeg')
        rect3.save(r"C:\\Icon_all\{}\{}_338x206_{}.png".format(MT,MT,lang),'png')

        # 146*136
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((146,136), Image.LANCZOS).convert('RGBA')
        main4 = main.resize((146,119), Image.LANCZOS).crop((0,-8,146,128))
        logo4 = logo.resize((146,119), Image.LANCZOS).crop((0,-8,146,128))
        rect4 = Image.new("RGBA", bg.size)
        rect4 = Image.alpha_composite(rect4, bg)
        rect4 = Image.alpha_composite(rect4, main4)
        rect4 = Image.alpha_composite(rect4, logo4)
        rect4.convert('RGB').save(r"C:\\Icon_all\{}\{}_146x136_{}.jpg".format(MT,MT,lang),'jpeg')
        rect4.save(r"C:\\Icon_all\{}\{}_146x136_{}.png".format(MT,MT,lang),'png')
        
        # 176*234
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).resize((250,234), Image.LANCZOS).crop((36,0,212,234)).convert('RGBA')
        main5 = main.resize((176,144), Image.LANCZOS).crop((0,-45,176,189))
        logo5 = logo.resize((176,144), Image.LANCZOS).crop((0,-45,176,189))
        rect5 = Image.new("RGBA", bg.size)
        rect5 = Image.alpha_composite(rect5, bg)
        rect5 = Image.alpha_composite(rect5, main5)
        rect5 = Image.alpha_composite(rect5, logo5)
        rect5.convert('RGB').save(r"C:\\Icon_all\{}\{}_176x234_{}.jpg".format(MT,MT,lang),'jpeg')
        rect5.save(r"C:\\Icon_all\{}\{}_176x234_{}.png".format(MT,MT,lang),'png')
        
        #208*170
        bg = Image.open(r"Icon_kit\{}\Background.png".format(MT)).convert('RGBA')
        rect1.resize((208,170), Image.LANCZOS).save(r"C:\\Icon_all\{}\{}_208x170_{}.png".format(MT,MT,lang),'png')