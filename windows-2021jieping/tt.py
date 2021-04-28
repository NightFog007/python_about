from pynput.keyboard import Key, Controller
# keyboard = Controller()
# keyboard.type('中文测试test')
# keyboard.press(Key.ctrl.value) #windows下使用
# keyboard.press('a')
# keyboard.release('a')
# keyboard.release(Key.ctrl.value) #windows下使用
# keyboard.press(Key.ctrl.value) #windows下使用
# keyboard.press('c')
# keyboard.release('c')
# keyboard.release(Key.ctrl.value) #windows下使用
# keyboard.press(Key.ctrl.value) #windows下使用
# keyboard.press('v')
# keyboard.release('v')
# keyboard.release(Key.ctrl.value) #windows下使用

ids = [
'梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2104[68803258])',
'梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2404[68798358])',
'梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2304[68810276])',
'梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2204[68808310])'
]



from pynput.keyboard import Key, Controller
import win32gui
import win32con
import win32api
from time import sleep
import shutil
import io
import sys
import os
import time
from skimage.metrics import structural_similarity
import cv2 as cv
from PIL import Image
from PyQt5.QtWidgets import QApplication
import constant as c
import numpy as np
from matplotlib import pyplot as plt
#######
#######
from pymouse import PyMouse
from pykeyboard import PyKeyboard

hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

def shot():
    win32gui.EnumWindows(get_all_hwnd, 0)
    # mhxy_title = i 
    for h,t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            mhxy_title = t
            # mhxy_title = '梦幻西游 ONLINE - (北京1区[喜大普奔] - 神★太子★[68430584])'
    # mhxy_title = '梦幻西游 ONLINE - (北京1区[喜大普奔] - ″落红染素妆[37528547])'
    print(mhxy_title)
    # hwnd = win32gui.FindWindow(None, mhxy_title)
    # app = QApplication(sys.argv)
    # # desktop_id = app.desktop().winId()
    # screen = QApplication.primaryScreen()
    # # img_desk = screen.grabWindow(desktop_id).toImage()
    # img_sc = screen.grabWindow(hwnd).toImage()
    # # img_desk.save(c.img_desktop_path)
    # img_sc.save(c.img_sc_path)
    # # print(f'img_desktop save to -> {os.path.abspath(c.img_desktop_path)}')
    # print(f'img_mhxy save to -> {os.path.abspath(c.img_sc_path)}')
    # if mhxy_title == '':
    #     print('mhxy not start')
    #     return False
    return True

chuangkouname='梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2204[68808310])'
chuangkouname='梦幻西游 ONLINE - (北京1区[喜大普奔] - wodiao2404[68798358])'


for i in ids:



    hwnd = win32gui.FindWindow(None, i)
    # app = QApplication(sys.argv)
    win32gui.ShowWindow(hwnd,1) 

    win32gui.SetForegroundWindow(hwnd) 

    # win32api.keybd_event(18,0,0,0)  #ctrl键位码是17
    # win32api.keybd_event(70,0,0,0)  #f4键位码是86
    # win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    # win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)


    sleep(1)
    k = PyKeyboard()
    # k.type_string('hello world')
    k.press_key(k.alt_key)
    k.press_key('f')
    k.release_key('f')
    k.release_key(k.alt_key)

    sleep(1)

# sleep(1)
# k.tap_key(k.numpad_keys[5],n=3)
# keyboard = Controller()
# # keyboard.type('中文测试test')
# keyboard.press(Key.alt.value) #windows下使用
# keyboard.press('f')
# keyboard.release('f')
# keyboard.release(Key.alt.value) #windows下使用
# keyboard.press(Key.ctrl.value) #windows下使用
# keyboard.press('c')
# keyboard.release('c')
# keyboard.release(Key.ctrl.value) #windows下使用
# keyboard.press(Key.ctrl.value) #windows下使用
# keyboard.press('v')
# keyboard.release('v')
# keyboard.release(Key.ctrl.value) #windows下使用

