import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
import re
# import pyscreenshot as ImageGrab
import numpy as np
from cv2 import cv2 
from aip import AipOcr

from fast_screenshot import jiepin

from time import sleep 

import aircv as ac

""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



# d = u2.connect_usb('18bcc735')
phone_x = 2400
phone_y = 1800
# d = adbutils.adb.device('DLQ0216505001224')   # 华为
d = u2.connect_usb('DLQ0216505001224')
# jiepin()

def find_donghai_chuanfu():
    image = get_file_content('home.jpg')
    Result=client.general(image)

    #! 电源按键在屏幕下面,这样摆放手机.

    # print(Result["words_result_num"])
    show=Result['words_result']
    for i in show:
        # print(i['words'])    
        
        x = i['words']
        xx = re.findall(r"(.+?)傲来(.+?)",x)
        
        if len(xx) > 0:
        
        # find_text = '傲来'
        # find_text = re.findall(r"",find_text)[0]
        # if i['words'] == find_text:
            print("找到了目标")
            print(x)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']
            x  = x + 80
            y  = y -100
            # 下面是帮派主管的偏移值
            # x = (x +60) / phone_x
            # y = (y -58) / phone_y
            # 下面是东海湾船夫的偏移值
            # x = (x - 10 ) / phone_x
            # y = (y - 26) / phone_y        
        
            # x = x / phone_x
            # y = y / phone_y

            print(i['location'])
            print(x)
            print(y)
            d.click(x,y)
            

def find_donghai_chuanfu():
    image = get_file_content('home.jpg')
    Result=client.general(image)

    #! 电源按键在屏幕下面,这样摆放手机.

    # print(Result["words_result_num"])
    show=Result['words_result']
    for i in show:
        # print(i['words'])    
        
        x = i['words']
        xx = re.findall(r"(.+?)傲来(.+?)",x)
        
        if len(xx) > 0:
        
        # find_text = '傲来'
        # find_text = re.findall(r"",find_text)[0]
        # if i['words'] == find_text:
            print("找到了目标")
            print(x)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']
            x  = x + 80
            y  = y -100
            # 下面是帮派主管的偏移值
            # x = (x +60) / phone_x
            # y = (y -58) / phone_y
            # 下面是东海湾船夫的偏移值
            # x = (x - 10 ) / phone_x
            # y = (y - 26) / phone_y        
        
            # x = x / phone_x
            # y = y / phone_y

            print(i['location'])
            print(x)
            print(y)
            d.click(x,y)

# def jiepin():
#     image = d.screenshot(format='opencv')
#     cv2.imwrite('home.jpg', image)
#     sleep(1)


# 手机找图  https://www.cnblogs.com/meitian/p/7417582.html
def matchImg(imgsrc,imgobj,confidencevalue=0.8):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
        print(match_result)
        print(match_result['rectangle'][0]) #匹配的图片中心点
    # return match_result
        return match_result['rectangle'][0]
    else:
        print("没找到图片!")
        return 0


def pinbi(d):
    d.click(0.058, 0.355) #屏蔽所有摊位和玩家 


""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)






def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 获取当前目录路径
path = os.path.abspath(os.path.dirname(__file__))

def pinbi(d):
    d.click(0.058, 0.355) #屏蔽所有摊位和玩家    



# d.screenshot("home.jpg")    
# # image = d.screenshot(format='opencv')
# # cv2.imwrite('home.jpg', image)
# # a = 'home.jpg'
# # b = '1122.png'
# # get_pay_keyboard_number_location(b,b,0.7)

# image = get_file_content('home.jpg')
# options = {}

# options["probability"] = "true"

# # Result=client.basicGeneralUrl(url,options)
# # Result=client.basicGeneral(image)
# # Result=client.basicAccurate(image)
# Result=client.general(image)


# #! 电源按键在屏幕下面,这样摆放手机.

# # print(Result["words_result_num"])
# show=Result['words_result']
# for i in show:
#     # print(i['words'])

#     if i['words'] == '帮派主管':
#         print("到了帮派主管")
#         weizhi = i['location']
#         x  = weizhi['left']
#         y = weizhi['top']
#         x = (x +60) / phone_x
#         y = (y -58) / phone_y
    
#         # x = x / phone_x
#         # y = y / phone_y

#         print(i['location'])
#         print(x)
#         print(y)
     



#! 这里x和y是屏幕截图的坐标,非真实手机坐标
def get_pic(image_path,pixelX,pixelY):
    img_src = Image.open(image_path)
    img_src = img_src.convert('RGBA')
    str_strlist = img_src.load()
    RGBA = str_strlist[pixelX, pixelY]
    img_src.close()
    hex_str = '#'
    for i in RGBA:
        num = int(i) # 将RGBA的数值转换成数字类型
        hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
    return hex_str


def wait():
    time.sleep(1)


# img_path= a

# while not os.path.exists(a):
#     time.sleep(1)
# x = x/2400
# y = y/1080   
# img_RGBA = get_RGBA(img_path, x, y)

# print(img_RGBA)

# img_hex = RGBA_to_Hex(img_RGBA)


#^ 人物在移动的话返回0,静止返回-1
def isMove():
    over = 0
    while over > -1 :
        
        jiepin()
        img_path = 'home.jpg'
        # 左上角
        x1 = 500
        y1 = 400
        # 右上角
        x2 = 1800
        y2 = 400
        # 左下角
        x3 = 600
        y3 = 800
        # 右下角
        x4 = 1800
        y4 = 800    
        img_hex1 = get_pic(img_path,x1,y1)
        # img_hex2 = get_pic(img_path,x2,y2)
        # img_hex3 = get_pic(img_path,x3,y3)
        img_hex4 = get_pic(img_path,x4,y4)
        
        jiepin()

        
        time.sleep(2)
        img_path = 'home.jpg'
        img_hex11 = get_pic(img_path,x1,y1)
        img_hex44 = get_pic(img_path,x4,y4)   

        if img_hex1 == img_hex11 and img_hex4 == img_hex44 :
            print("人物已静止")
            over = -1
            return -1
        else:
            print("人物在移动")
            # return 0

#^ 从打开帮派总管界面 到 点击领取任务的流程
def lingrenwu():
    
    # 回帮派对话框
    x = 2006
    y = 212
    d.click(x, y)
    sleep(2)


    # 帮派走到金库
    x = 1400
    y = 396
    d.click(x, y)
    sleep(2)

    # 走到白虎堂总管
    x = 1265
    y = 537
    d.click(x, y)
    sleep(3)

    # 点击白虎堂总管
    x = 1160
    y = 484
    d.click(x, y)
    sleep(2)


    # 领任务
    x = 2008
    y = 194
    d.click(x, y)
    sleep(2)
    
# 出帮派
# x  = 1553
# y  = 902
# d.click(x, y)
# sleep(2)

def open_ditu():
    x = 242
    x = 193.6
    y = 100
    d.click(x, y)
    sleep(0.5)
    


def close_ditu():
    x = 1945
    y = 85
    d.click(x, y)
    sleep(2)


# 小地图 长安去野外
def ditu_changan_yewai():
    # 19:07:15
    # 19:08:32 从进入此函数,到人物静止.
    open_ditu()
    x = 1858 * 0.7475
    y = 875
    d.click(x, y)
    sleep(2)
    x = 1945 * 0.7475 # 关闭地图
    y = 85
    d.click(x, y)
    sleep(2)
    
   

# ditu_changan_yewai()
# open_ditu()    
# chu_changan()
# close_ditu()
# 长安出到野外
def chu_changan_kouzi():
    x = 2107
    y = 1015
    d.click(x, y)
    sleep(2)
    
# chu_changan_kouzi()   
# 小地图 野外去建邺
def ditu_yewai_jianye():
    # 19:10:05
    # 19:10:35
    open_ditu()
    x = 1760
    y = 616
    d.click(x, y)
    sleep(1)
    x = 1824 #关闭地图
    y = 137
    d.click(x, y)
    sleep(1)       
    
  
# ditu_yewai_jianye()
# sleep(30)

# 野外进建邺
def jin_jianye_kouzi():
    x = 2189
    y = 403
    d.click(x, y)
    sleep(2)    

# jin_jianye_kouzi()



def ditu_jianye_donghai():
    # 19:11:00
    # 19:11:45
    open_ditu()
    x = 1850
    y = 747
    d.click(x, y)
    sleep(1)
    x = 1942 #关闭地图
    y = 96
    d.click(x, y)
    sleep(2)       


# ditu_jianye_donghai()
# sleep(35)

def chu_jianye_donghai():
    x = 2076
    y = 705
    d.click(x, y)
    sleep(3)    

# chu_jianye_donghai()

def ditu_donghai_al():
    open_ditu()
    x = 1330
    y = 805
    d.click(x, y)
    sleep(1)
    x = 1717 #关闭地图
    y = 133
    d.click(x, y)
    sleep(8)    



# ditu_donghai_al()





# 船夫的对话框
def donghai_qu_aolai():
    x = 2040
    y = 538
    d.click(x, y)
    sleep(2)

def ditu_aolai_techan():
    open_ditu()
    # x = 936
    x = 748.8
    y = 740
    d.click(x, y)
    sleep(1)
    # x = 1755 #关闭地图
    x = 1404
    y = 89
    d.click(x, y)
    sleep(1) 
    
        
    
def click_al_techan():    
    jiepin()
    al_techan = matchImg('home.jpg','./pic/al_techan.png',0.95)  #! home.jpg必须即时更新
    d.click(al_techan[0],al_techan[1])
    sleep(2)


# click_al_techan()
def npc_woyaojiaoyi():         
    x = 2027
    y = 530
    d.click(x, y)
    sleep(2) #! 未完成

def ditu_aolai_huaguoshan():
    open_ditu()
    x = 1725
    y = 225
    d.click(x, y)
    sleep(1)
    x = 1730 #关闭地图
    y = 86
    d.click(x, y)
    sleep(1) 
    
def chu_aolai_huaguoshan():  
    x = 2220
    y = 250
    d.click(x, y)
    sleep(3) 
    
def ditu_huaguoshan_beiju():
    open_ditu()
    x = 1019
    y = 349
    d.click(x, y)
    sleep(1)
    x = 1820 #关闭地图
    y = 148
    d.click(x, y)
    sleep(1) 


def click_huaguoshantudi():  
    jiepin()  
    al_techan = matchImg('home.jpg','./pic/huaguoshan_tudi.png',0.75)  #! home.jpg必须即时更新
    d.click(al_techan[0],al_techan[1])
    sleep(2)     
    
# click_huaguoshantudi()
    
def npc_shide_woyaoqu():
    x = 2000
    y = 530
    d.click(x, y)
    sleep(2)
    
def ditu_beiju_csjiaowai():
    open_ditu()
    x = 1674
    y = 893
    d.click(x, y)
    sleep(1)
    x = 1800 #关闭地图
    y = 124
    d.click(x, y)
    sleep(1) 
    
    
# ditu_beiju_csjiaowai()
    
def click_bj_dundigui():
    x = 1260
    y = 565
    d.click(x, y)
    sleep(2)     
    
# 北俱去郊外    
# click_bj_dundigui()    
# npc_shide_woyaoqu()

def ditu_csjiaowai_cs():
    open_ditu()
    x = 1586
    y = 239
    d.click(x, y)
    sleep(1)
    x = 1735 #关闭地图
    y = 142
    d.click(x, y)
    sleep(1) 

def jin_cs():
    x = 1233
    y = 118
    d.click(x, y)
    sleep(2)        
    

def ditu_cs_shangren():
    open_ditu()
    x = 1533
    y = 768
    d.click(x, y)
    sleep(1)
    x = 1607 #关闭地图
    y = 125
    d.click(x, y)
    sleep(1)     


def click_cs_shangren():    
    x = 1675
    y = 540
    d.click(x, y)
    sleep(2)  









    
    
    
    
      
    
    
        
# ditu_changan_yewai()
# # sleep(90)

# kk = 0    
# kk = isMove()
# if kk < 0:
#     chu_changan_kouzi()        




# ditu_yewai_jianye()  
# # sleep(35)
# kk = isMove()
# if kk < 0:
#     # chu_changan_kouzi()  
#     jin_jianye_kouzi()

# ditu_jianye_donghai()  
# # sleep(50)

# kk = isMove()
# if kk < 0:
#     chu_jianye_donghai() 

# ditu_donghai_al()  
# sleep(8)
    # 找船夫
# find_donghai_chuanfu()


# sleep(5)

# npc_shide_woyaoqu()

# ditu_aolai_techan()
# # sleep(20)
# kk = isMove()
# if kk < 0:
#     #点击特产商人
#     click_al_techan()


# ditu_aolai_huaguoshan()
# # sleep(60)
# kk = isMove()
# if kk < 0:
#     chu_aolai_huaguoshan()

# ditu_huaguoshan_beiju()
# # sleep(25)
# kk = isMove()
# if kk < 0:
#     pinbi(d)
#     click_huaguoshantudi()
#     npc_shide_woyaoqu()
# sleep(2)

# ditu_beiju_csjiaowai()
# # sleep(45)
# kk = isMove()
# if kk < 0:
#     click_bj_dundigui()
#     npc_shide_woyaoqu()

# ditu_csjiaowai_cs()
# # sleep(35)
# kk = isMove()
# if kk < 0:
#     jin_cs()

# ditu_cs_shangren()
# # sleep(10)
# kk = isMove()
# if kk < 0:
#     click_cs_shangren()
#     sleep(1)
#     npc_woyaojiaoyi()

# while 1:
#     isMove()

    