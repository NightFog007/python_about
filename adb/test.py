import os 
import time
import random

# os.system('adb devices')
# 抖音点赞坐标 983 1337
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()
# os.system()

class Manager():
    def __init__(self,default_ts = 0.5 , *args,**kwargs):
        self.default_ts = default_ts
        
    # 滑动        
    def input_swipe(self,sx,sy,ex,ey,ts=0):
        os.system("adb shell input swipe {0} {1} {2} {3} {4}".format(sx,sy,ex,ey,ts))
        time.sleep(self.default_ts+0.2)
    
    # 输入文本
    def input_text(self,text):
        os.system("adb shell am broadcase -a ADB_INPUT_TEXT --es msg '{}' ".format(text))
        time.sleep(self.default_ts-0.2)

    # 点击
    def ipnut_tap(self,x,y):
        os.system("adb shell input tap {0} {1}".format(x,y))
        time.sleep(self.default_ts+0.3)
    
    # 键入键值    
    def input_keyevent(self,key):
        os.system("adb shell input keyevent {0}".format(key))
        time.sleep(self.default_ts)