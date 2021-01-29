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

""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)





# 小米10青春版
d = u2.connect_usb('18bcc735')
phone_x = 2400
phone_y = 1800

# #华为
# d = u2.connect_usb('DLQ0216505001224')
# phone_x = 1920
# phone_y = 1080


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 获取当前目录路径
path = os.path.abspath(os.path.dirname(__file__))

def pinbi(d):
    d.click(0.058, 0.355) #屏蔽所有摊位和玩家    


# d.screenshot("home.jpg")    
image = d.screenshot(format='opencv')
cv2.imwrite('home.jpg', image)
# a = 'home.jpg'
# b = '1122.png'
# get_pay_keyboard_number_location(b,b,0.7)

image = get_file_content('home.jpg')
options = {}

options["probability"] = "true"

# Result=client.basicGeneralUrl(url,options)
# Result=client.basicGeneral(image)
# Result=client.basicAccurate(image)
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





# img_path= a

# while not os.path.exists(a):
#     time.sleep(1)
# x = 945
# y = 747
# x = x/2400
# y = y/1080   
# img_RGBA = get_RGBA(img_path, x, y)

# print(img_RGBA)

# img_hex = RGBA_to_Hex(img_RGBA)


#^ 人物在移动的话返回0,静止返回1
def isMove(img_path):
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
    
    time.sleep(1)
    img_hex11 = get_pic(img_path,x1,y1)
    img_hex44 = get_pic(img_path,x4,y4)   

    if img_hex1 == img_hex11 and img_hex4 == img_hex44 :
        #人物已静止
        return 1
    else:
        #人物在移动
        return 0





# img_hex = get_pic(img_path,x,y)
# print(img_hex)

# d.click(x, y)