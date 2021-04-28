import win32gui
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
  if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

 
# for h,t in hwnd_title.items():
#   if t is not "":
#     print(h, t)


from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys

import time
import win32gui, win32ui, win32con, win32api
from send_text import send_message_to_slack
import random
import pyscreenshot as ImageGrab
import sys
import numpy as np
import time
from cv2 import cv2 
from time import sleep

def get_pay_keyboard_number_location(impath, target,fit_num): #fit_num是匹配度,如 0.95,0.85

        print("start find pic")
        positions = {}

        # start = time.time()
        img_rgb = cv2.imread(impath)

        teNum = "done"

        template = cv2.imread(target)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
       
       
        threshold = fit_num  # 匹配度参数，1为完全匹配
        loc = np.where(res >= threshold)
        if len(loc) > 0:
            # positions[teNum] = zip(*loc[::-1])[0]  # python2的写法
            
            zipped = zip(*loc[::-1])  #list[::-1] 相当于起点为最后的一个,终点为第一个,然后一次减少一个
            positions[teNum] = (list(zipped))[0]
            
        else:
            print("Can not found pic: ")

        # end = time.time()
        # print(end - start)

        return positions[teNum]  








def zhaotu(fenbianlv):

#   impath1 = "haha"+str(fenbianlv)+'.jpg'
    impath1 = 'screenshot.jpg'
    targetPath_a = "yellow" +str(fenbianlv)+'.jpg'


    win32gui.EnumWindows(get_all_hwnd, 0)

    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()

    while 1>0:

                                  

        img = screen.grabWindow(hwnd    ).toImage()
        img.save("screenshot.jpg")



        try:
            ls = get_pay_keyboard_number_location(impath1, targetPath_a,0.97) #在键盘图片找到字母a
            # print(ls)
            print('有提示框')

            send_message_to_slack('弹出框待解决')
        except:
            print("无提示框")
          
        sleep(5)


zhaotu(1792)
# zhaotu(3584)
# win32gui.EnumWindows(get_all_hwnd, 0)

# hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
# app = QApplication(sys.argv)
# screen = QApplication.primaryScreen()
# while 1>0:
#     sleep(5)      

#     img = screen.grabWindow(hwnd).toImage()
#     img.save("screenshot.jpg")
#     print("success")


