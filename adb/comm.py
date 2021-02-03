import os
import random
import re
import subprocess
import time
from time import sleep
import adbutils
import aircv as ac
# import pyscreenshot as ImageGrab
import numpy as np
import uiautomator2 as u2
import websocket
from aip import AipOcr
from cv2 import cv2
from PIL import Image

""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

d = u2.connect_usb('DLQ0216505001224')

def open_ditu():
    x = 193.6
    y = 100
    d.click(x, y)
    sleep(1)
    
    
# 点击战斗中的重置按钮
def click_reset_button():
    d.click(1711,1020)
    
def get_09():
    return int(random.choice('0123456789'))

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

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    

def get_random_num(x):
    return random.randint(0,x)         #返回0-x的随机整数

def jiepin(name='home.jpg'):
    # d = adbutils.adb.device('18bcc735')  # 小米10青春版
    d = adbutils.adb.device('DLQ0216505001224')   # 华为

    lport = d.forward_port(7912 )
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:{}/minicap".format(lport))

    index = 0
    # start = time.time()
    while True:
        data = ws.recv()
        if not isinstance(data, (bytes, bytearray)):
            # print(data)
            continue
        # with open("home.jpg" , "wb") as f:
        with open(name , "wb") as f:
            f.write(data)
            index += 1
        # print(index)
        if index > 0:
            break

    # duration = time.time() - start
    # print("Image per second: %.2f" % (100/duration))
    ws.close()
    
#^ 找图函数
def matchImg(imgsrc,imgobj,confidencevalue=0.8):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
    # print(match_result)
    # print(match_result['rectangle'][0]) #匹配的图片中心点
    x1 = match_result['rectangle'][0][0]
    y1 = match_result['rectangle'][0][1]
    # res = (0,0)
    # res[0] = int(match_result['rectangle'][0][0]) * 2.5
    # res[1] = int(match_result['rectangle'][0][1]) * 2.5
    x1 = int(x1 * 2.5)  #! 使用minicap截屏的图片,拿到的坐标必须乘以2.5才是实际手机屏幕坐标
    y1 = int(y1 * 2.5)
    return x1,y1

# res = matchImg('home.jpg','123.png',0.8)
# print(res)

# def quyu_jietu(x,y,width,height,name='temp'):
#^  区域截图,参数分别是 (左上角x, 左上角y, 右下角x, 右下角y)
def quyu_jietu(left,upper,right,lower,name='temp'):
    jiepin()
    img = Image.open("home.jpg")
    # img_c = img.crop([img.size[0]/4,img.size[1]/4,img.size[0]*3/4,img.size[1]*3/4])
    img_c = img.crop([left,upper,right,lower])
    img_c.save(name+'.jpg')
    
  
# quyu_jietu(50,12,140,33) #区域截图,左上角地图名字
def get_where_now():
    quyu_jietu(50,12,140,33,'place')
    x = 0 
    y = 0
    image = get_file_content('place.jpg')

    options = {}
    options["probability"] = "true"
    Result=client.general(image)
    # Result=client.accurate(image)
    show=Result['words_result']
    for i in show:
        # print(i['words'])
        res_word = i['words']
        # xx = re.findall(r"(.+?)的好(.+?)",res_word)
        # if len(xx)>0:
        #     print("找到了: " + res_word)
        #     weizhi = i['location']
        #     print(i)
        #     x  = weizhi['left']
        #     y = weizhi['top']     
        #     break
    
    # 返回场景中文,如 江南野外
    return res_word  



#^ 判断人物是否在移动,静止返回-1
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


#^ 判断人物是否在移动,静止返回-1,在移动返回0,只判断一次,实时返回
def isMove_once():
    over = 0
        
    jiepin()
    img_path = 'home.jpg'
    # 左上角
    # x1 = 500 * 0.8 *0.4
    # y1 = 400  *0.4
    # 右下角
    # x4 = 1800 * 0.8 *0.4
    # y4 = 800  *0.4  
    
    # 右上角
    # x1=  1865* 0.8 *0.4
    # y1 = 153 *0.4  
    x1 = 1608* 0.8 *0.4
    y1 = 138 *0.4 
    
    # 右下角
    x4 = 1745* 0.8 *0.4
    y4 = 916 *0.4  
    
    img_hex1 = get_pic(img_path,x1,y1)
    img_hex4 = get_pic(img_path,x4,y4)
    
    jiepin('home2.jpg')
    time.sleep(0.5)
    img_path = 'home2.jpg'
    img_hex11 = get_pic(img_path,x1,y1)
    img_hex44 = get_pic(img_path,x4,y4)   

    if img_hex1 == img_hex11 and img_hex4 == img_hex44 :
        print("人物已静止")
        over = -1
        return -1
    else:
        print("人物在移动")
        return 0



# 判断人物是否在战斗,不在战斗返回-1,在战斗返回0,只判断一次,实时返回
def isFight_once():
    
    over = -1
    quyu_jietu(22,65,88,88,'fight')
    x = 0 
    y = 0
    image = get_file_content('fight.jpg')

    options = {}
    options["probability"] = "true"
    Result=client.general(image)
    print(Result)
    show=Result['words_result']
    # print(show)
    time.sleep(2)
    
    if len(show)>0:
        res_word = show[0]['words']

        xx = re.findall(r"(.+?)回合",res_word)
        if len(xx)>0:
            print("人物在战斗中 " )  
            click_reset_button()
            over = 0
            time.sleep(1)
        else:
            print("人物不在战斗")
            over = -1
              

    return over  

# fight_res = isFight_once()
# print(fight_res)


