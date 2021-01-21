import uiautomator2 as u2
d = u2.connect_usb('18bcc735')

from aip import AipOcr
""" 你的APPID AK SK """

APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

import time 
import random
# import pyscreenshot as ImageGrab

import numpy as np
from cv2 import cv2 

# d = u2.connect('10.0.157.39')
# print(d.info)

# com.netease.mhxyhtb

# d.click(0.902, 0.484)
d.click(0.058, 0.355) #屏蔽所有摊位和玩家



def get_pay_keyboard_number_location(impath, target,fit_num): #fit_num是匹配度,如 0.95,0.85

        print("start find pic")
        positions = {}

        start = time.time()
        img_rgb = cv2.imread(impath)

        teNum = "done"

        template = cv2.imread(target)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
      
        threshold = fit_num  # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
            # positions[teNum] = zip(*loc[::-1])[0]  # python2的写法
            print("找到了匹配图")
            zipped = zip(*loc[::-1])  #list[::-1] 相当于起点为最后的一个,终点为第一个,然后一次减少一个
            print(list(zipped))
            positions[teNum] = (list(zipped))[0]
            
        else:
            print("Can not found pic: ")

        end = time.time()
        print("时间：")
        print(end - start)

        return positions[teNum]  
    

# d.screenshot("home.jpg")    
image = d.screenshot(format='opencv')
cv2.imwrite('home.jpg', image)
a = 'home.jpg'
b = '1122.png'
# get_pay_keyboard_number_location(a,b,0.9)

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
    print(i['words'])

    if i['words'] == '帮派主管':
        print("到了帮派主管")
        weizhi = i['location']
        x  = weizhi['left']
        y = weizhi['top']
        x = (x +60)/2400
        y = (y -58)/1080

        print(i['location'])
        print(x)
        print(y)
        
        
d.click(x, y)