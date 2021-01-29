import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
# import pyscreenshot as ImageGrab
import numpy as np
from cv2 import cv2 
from aip import AipOcr

""" 你的APPID AK SK """
APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

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
            print("找到了匹配图")
            print(loc)
            zipped = zip(*loc[::-1])  #list[::-1] 相当于起点为最后的一个,终点为第一个,然后一次减少一个
            positions[teNum] = (list(zipped))[0]
            print(positions[teNum])
            
        else:
            print("Can not found pic: ")

        end = time.time()
        print("时间：")
        print(end - start)

        return positions[teNum]  
    

a = 'home.jpg'
b = '123.png'
get_pay_keyboard_number_location(a,b,0.8)