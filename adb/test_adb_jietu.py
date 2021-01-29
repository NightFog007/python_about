import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
# import pyscreenshot as ImageGrab
import numpy as np
from cv2 import cv2 
from aip import AipOcr
import subprocess
import random
import time


import aircv as ac
def matchImg(imgsrc,imgobj,confidencevalue=0.8):#imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
    print(match_result)
    print(match_result['rectangle'][0]) #匹配的图片中心点
    x1 = match_result['rectangle'][0][0]
    y1 = match_result['rectangle'][0][1]
    # res = (0,0)
    # res[0] = int(match_result['rectangle'][0][0]) * 2.5
    # res[1] = int(match_result['rectangle'][0][1]) * 2.5
    x1 = int(x1 * 2.5)  #! 使用minicap截屏的图片,拿到的坐标必须乘以2.5才是实际手机屏幕坐标
    y1 = int(y1 * 2.5)
    return x1,y1

res = matchImg('home.jpg','123.png',0.8)
print(res)

def getScreen():
    subprocess.run(f"adb shell screencap -p /sdcard/aa.png", capture_output=True)
    subprocess.run(f"adb.exe pull /sdcard/screen.png", capture_output=True)
    # time.sleep(2)
    fprint("手机截图成功")
    
# getScreen()

# d = u2.connect_usb('18bcc735')
# phone_x = 2400
# phone_y = 1800

