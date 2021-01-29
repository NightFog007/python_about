import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
import re
import numpy as np
from cv2 import cv2 
from aip import AipOcr

from fast_screenshot import jiepin

from time import sleep 

from comm import matchImg,isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu

import aircv as ac

""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

d = u2.connect_usb('DLQ0216505001224')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
def zhaoguai():
    x = 0 
    y = 0
    image = get_file_content('home.jpg')

    #这里使用url网页图片，也可以使用本地图片，方法可以查看文档接口说明
    options = {}

    options["probability"] = "true"
    Result=client.general(image)

    show=Result['words_result']
    for i in show:
        print(i['words'])
        res_word = i['words']
        xx = re.findall(r"(.+?)蟆(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']            
            break

        xx = re.findall(r"(.+?)髅(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']            
            break
        
        xx = re.findall(r"(.+?)狸(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']            
            break
        
        xx = re.findall(r"(.+?)头(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']            
            break
        
        xx = re.findall(r"(.+?)妖(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            x  = weizhi['left']
            y = weizhi['top']            
            break
        
    x = int(x  * 2.5)
    y = int(y  * 2.5)                                             
    return x,y

def zhaoziji():
    x = 0 
    y = 0
    image = get_file_content('home.jpg')

    #这里使用url网页图片，也可以使用本地图片，方法可以查看文档接口说明
    options = {}
    # options["detect_direction"] = "true"
    options["probability"] = "true"
    # Result=client.general(image)
    Result=client.accurate(image)
    show=Result['words_result']
    for i in show:
        print(i['words'])
        res_word = i['words']
        xx = re.findall(r"(.+?)的好(.+?)",res_word)
        if len(xx)>0:
            print("找到了: " + res_word)
            weizhi = i['location']
            print(i)
            x  = weizhi['left']
            y = weizhi['top']     
            break
        
    x = int(x  * 2.5)
    y = int(y  * 2.5)
    return x,y    
         
def jiepin2():
    image = d.screenshot(format='opencv')
    cv2.imwrite('home.jpg', image)
    sleep(1)   
    
def close_t5_ditu():
    sleep(0.5)
    x = 1676 #关闭地图
    y = 63
    d.click(x, y)
        
         
# jiepin()
              
# guaiwu = zhaoguai()
# print(guaiwu)

# ziji = zhaoziji()
# print(ziji)


# if guaiwu[0] < ziji[0]:
#     # 人物移动到怪物左边
#     npcx = guaiwu[0]
#     npcy = guaiwu[1]
#     d.click(npcx -5, npcy - 5)
# else:
#     #人物移动到怪物右边
#     npcx = guaiwu[0]
#     npcy = guaiwu[1]
#     d.click(npcx + 5, npcy - 5)

# jiepin()
a = 'home.jpg'
b = '123.png'
# open_ditu()
# res = matchImg(a,b)
# print(res)

xiaoditu_zuobiao = [(520,482),(997,270),(1095,307),(1372,445),(1342,565),(1600,565),(1360,667),(102,825),(990,640),(1132,780),(652,685),(540,407)]

# s = isMove
# if s < 0:

while 1: 


    panduan1 = isMove_once()
    panduan2 = isFight_once()

    # 如果人物静止且不在战斗中,点小地图
    # 如果人物移动中, panduan1 = 0 ,跳过 
    # 如果人物战斗中, panduan2 = 0 ,跳过
        
    if panduan1 < 0 and panduan2 < 0 :
        # x = get_random_num(11)
        x = get_09()
        xx = xiaoditu_zuobiao[x]
        open_ditu()
        d.click(xx[0],xx[1])
        close_t5_ditu()
        # close_ditu



