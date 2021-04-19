import os
import random
import re
import sys
import time
from send_text import send_message_to_slack
# import pyscreenshot as ImageGrab
import numpy as np
import uiautomator2 as u2
from aip import AipOcr
from cv2 import cv2
from PIL import Image

sys.path.append('../')
import _thread
import time
from subprocess import call
from time import sleep

from random import randint as r
# from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu,quyu_click,new_sleep,delay_sleep

import adbutils
import aircv as ac
import websocket

""" 你的APPID AK SK """
APP_ID = '17235153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

flag = 0

mudidi = 'null'

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


#^ 判断人物是否在移动,静止返回-1,在移动返回0,只判断一次,实时返回
def isMove_once():
    over = 0
        
    jiepin()
    img_path = 'home_yabiao.jpg'

    
    x1 = 621
    y1 = 503
    
    x4 = 2099
    y4 = 585
       
    img_hex1 =  get_pic(img_path,x1,y1)
    img_hex4 =  get_pic(img_path,x4,y4)
    
    jiepin('home_yabiao2.jpg')
    time.sleep(0.5)
    img_path = 'home_yabiao2.jpg'
    img_hex11 =  get_pic(img_path,x1,y1)
    img_hex44 =  get_pic(img_path,x4,y4)   

    if img_hex1 == img_hex11 and img_hex4 == img_hex44 :
        print("静止")
        over = -1
        return -1
    else:
        print("移动")
        return 0



def quyu_click(x1,y1,x2,y2):
    xx = random.sample(range(x1,x2),1)
    yy= random.sample(range(y1,y2),1)
    d.click(xx[0],yy[0])
    
def new_sleep(x=2):
    # n = int(r(1,x))
    n = round(random.uniform(0,x),1)
    sleep(n)
    
def delay_sleep(x=3):
    n = round(random.uniform(1,x),1)    
    sleep(n)

def num_r():
    return int(r(1,5))

def open_wupin():
    d.click(2124,1047)
    sleep(1)
    new_sleep()
    quyu_click(1179,203,1276,222)
    sleep(1)
    new_sleep()
    
def close_wupin():    
    d.click(1849,112)
    new_sleep()

def random_num(x):
    return int(r(1,x))


def open_ditu():
    new_sleep()
    quyu_click(213,100,360,125)
    new_sleep()


    

d = u2.connect_usb('18bcc735')  #小米10青春版
# d = u2.connect_usb('113038e8') # 小米mix2
# d = u2.connect_usb('emulator-5554')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

# d.click(5,5)

def click_youxiajiao():
    # x = 888
    # y = 2052
    x= 840 #~ 这里可以点击 关闭葫芦
    y = 2094
    d.click(x,y)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
def jiepin(pic_name='home_yabiao.jpg'):
    image = d.screenshot(format='opencv')
    cv2.imwrite(pic_name, image)
    sleep(1)   
    


def click_zhidaole():
    x = 773- num_r()
    y = 1248- num_r()
    d.click(x,y)  
    
    
# jiepin()
def quyu_jietu(x,y,width,height,name='temp'):

    # jiepin()
    img = Image.open("home_yabiao.jpg")
    # img_c = img.crop([img.size[0]/2,img.size[1]/4+255,img.size[0]*3/4,img.size[1]*2/4])
    img_c = img.crop([x,y,width,height])
    img_c.save(name+'.jpg')
    
#^ 找图函数
def matchImg(imgsrc,imgobj,confidencevalue=0.8):#imgsrc=原始图像，imgobj=待查找的图片
    sleep(0.2)
    try:      
        imsrc = ac.imread(imgsrc)
    except:
        sleep(1)
        imsrc = ac.imread(imgsrc)
        
    imobj = ac.imread(imgobj)
    x1 = 0
    y1 = 0
 
    match_result = ac.find_template(imsrc,imobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    # print(match_result)
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
        # print(match_result)
    # print(match_result['rectangle'][0]) #匹配的图片中心点
        # x1 = match_result['rectangle'][0][0]
        # y1 = match_result['rectangle'][0][1]
        x1 = match_result['result'][0]
        y1 = match_result['result'][1]
    # res = (0,0)
    # res[0] = int(match_result['rectangle'][0][0]) * 2.5
    # res[1] = int(match_result['rectangle'][0][1]) * 2.5
        # x1 = int(x1 * 2.5)  #! 使用minicap截屏的图片,拿到的坐标必须乘以2.5才是实际手机屏幕坐标
        # y1 = int(y1 * 2.5)
        x1 = int(x1)
        y1 = int(y1)
        # print(x1,y1)
        
    return x1,y1

        


def isFight_once():  #fighting中,返回-1
    res = 0
    xx = matchImg('home_yabiao.jpg','wenzi_huihe.jpg')
    if xx[0]> 0 and xx[1] > 0:
        print("fighting中")
        res = -1

    return res

# zhaogui()


    

def send_message():
    # cmd = 'display notification \"' + \
    # "Notificaton memo" + '\" with title \"手动处理\"'
    cmd = 'display notification \"' + \
    "Notificaton memo" + '\" with title \"手动处理\"'
    call(["osascript", "-e", cmd])        
        

 
# place = 'datangrukou.jpg'    
# 到达了place返回0 ,没到达place返回-1
def walk(place):
    
    #判断是否在移动,如果在移动则不处理,如果是静止,则判断是否进入战斗,如果进入战斗则点击自动,如果没进入战斗,则自动寻路去目的地
    temp = 1
    while temp > 0:
        yidong = isMove_once()   # 静止返回-1,在移动返回0,只判断一次,实时返回
        if yidong > -1 :
            # 在移动,不作处理
            delay_sleep()
            pass
        else:
            zhandou = isFight_once() # #fighting中,返回-1
            if zhandou == -1 :
                #在战斗中
                quyu_click(2236,1000,2269,1020) #点自动
                new_sleep()
                quyu_click(2236,1000,2269,1020) #取消自动
                new_sleep()
                quyu_click(2236,1000,2269,1020) #再点一次自动
                new_sleep()
                sleep(8)  
            
            else:
                # 判断是否到达目的地或入口
                # 如果没有到达目的地,则继续打开地图走
                jiepin()
                sleep(1)
                daolema = matchImg('home_yabiao.jpg','./yabiaofile/'+place)
                if daolema[0]>0:
                    #到达目的地入口了
                    return 0
                else:
                    # 还没有到目的地
                    return -1    

def send_biao_npc(x1,y1,x2,y2):
    new_sleep()
    click_geiyu()
    delay_sleep()
    quyu_click(x1,y1,x2,y2)
    delay_sleep()
    jiepin()
    sleep(1)
    biaoyin = matchImg('./home_yabiao.jpg','./yabiaofile/biaoyin.jpg')
    if biaoyin[0]>0:
        d.click(biaoyin[0],biaoyin[1])
        delay_sleep()
        quyu_click(769,935,906,979) #确定
        new_sleep()
    else:
        send_message_to_slack('没有镖银')
    new_sleep()
    
        
def fei_yuanshoucheng():
    open_wupin()
    sleep(2)
    jiepin()
    sleep(1)
    hongse77 = matchImg('home_yabiao.jpg','./hongse77.jpg')
    if hongse77[0]>0:
        d.click(hongse77[0],hongse77[1])
        d.click(hongse77[0],hongse77[1])
        
    delay_sleep()
    d.click(962,881)  #飞 袁守城
    new_sleep()
    close_wupin()
    
def xinshouzhuxian():
    new_sleep()
    quyu_click(2100,392,2108,404)  #新手主线
    new_sleep()
    

def jishiqi(n):
    for i in range(0,n):
        print(i)
        sleep(1)
    
def click_kongbai():
    new_sleep()
    quyu_click(1490,229,1810,512) #空白区域
    
def click_renwu():
    new_sleep()
    quyu_click(2100,356,2140,398) 
    

    
def close_ditu():
    new_sleep()
    jiepin()
    sleep(1)
    temp = matchImg('./home_yabiao.jpg','./yabiaofile/closeIcon.jpg')
    new_sleep()
    if temp[0]>0:
        nn  = random_num(9)
        d.click(temp[0]+nn,temp[1]+nn)
        
    else:
        send_message_to_slack('没找到地图关闭按钮')

def click_geiyu():
    new_sleep()
    quyu_click(1304,1002,1357,1026)    
    new_sleep()
    
def ca_dt():
    open_ditu()
    delay_sleep()
    d.click(1311,214)
    delay_sleep()
    close_ditu()
    sleep(60)
    d.click(768,31)
    sleep(5)
    
def ditu_ca_xx(x,y):  #长安地图上去xx点
    open_ditu()
    delay_sleep()
    d.click(x,y)
    sleep(1)
    new_sleep()
    close_ditu()
    
def ca_hs():
    new_sleep()
    ditu_ca_xx(1794,218)
    # sleep(45)
    nn = -1
    while nn < 0 :
        nn = walk('huasheng_rukou.jpg')    #到达了place返回0 ,没到达place返回-1    
        
    
    d.click(1360,100) #进hs
    sleep(1)
    new_sleep()
    open_ditu()
    d.click(1551,520) # 去空度房
    close_ditu()
    sleep(20)
    d.click(1243,330) # 进空度房
    sleep(2)
    new_sleep()
    send_biao_npc(1073,468,1075,473)  #给镖给空度
    new_sleep()

    
    
    
                

    
    
def send_chengyaojin():
    new_sleep()
    open_ditu()
    delay_sleep()
    d.click(1216,572)
    new_sleep()
    close_ditu()
    sleep(10)
    d.click(820,508)
    sleep(2)
    d.click(1175,457)
    sleep(5)
    send_biao_npc(1019,360,1022,388)
    delay_sleep()
    

def yabiao_chengyaojin():
    # new_sleep()
    # ca_dt()
    # delay_sleep()
    # send_chengyaojin()
    # new_sleep()
    
    new_sleep()
    open_ditu()
    delay_sleep()
    d.click(1311,214)
    sleep(1)
    new_sleep()
    close_ditu()
    delay_sleep()
    
    nn = -1
    while nn < 0 :
        nn = walk('datang_rukou.jpg')    #到达了place返回0 ,没到达place返回-1    
    
    delay_sleep()    
    d.click(768,31)
    sleep(5)
    
    delay_sleep()
    send_chengyaojin()
    new_sleep()
    
          

def chubiaoju():
    nn = random_num(8)
    d.click(970+nn,954+nn)
    sleep(5)
    new_sleep()
    d.click(1113+nn,840+nn)   
 
def yabiao():
    new_sleep()
    open_wupin()
    delay_sleep()
    jiepin()
    sleep(1)
    biaoju77 = matchImg('./home_ybiao.jpg','./yabiaofile/baise77.jpg')   ##~ 旗子坐标是525,155
    if biaoju77[0] > 0:
        d.click(biaoju77[0],biaoju77[1])
        d.click(biaoju77[0],biaoju77[1])
    delay_sleep()
    quyu_click(1905,378,2101,423) # 送我去那里
    delay_sleep()
    close_wupin()
    delay_sleep()
    d.click(1579,489) # 进镖局
    sleep(2)
    d.click(1479,419) #走近npc
    sleep(4)
    d.click(1602,507) # 点击npc
    delay_sleep()
    jiepin()
    sleep(1)
    shifoulingrenwu = matchImg('./home_ybiao.jpg','./yabiaofile/wenzi_sijibiao.jpg')
    if shifoulingrenwu[0] > 0:
        quyu_click(1904,600,2000,643)  #点击四级镖银
        delay_sleep()
        quyu_click(1914,650,2100,690) # 选 储备金模式
        delay_sleep()
        jiepin()  #保存目的地截图
        sleep(1)
        chengyaojin = matchImg('./home_ybiao.jpg','./yabiaofile/wenzi_chengyaojin.jpg')
        
        delay_sleep()        
        click_kongbai()
        delay_sleep()
        
        ##~ 出镖局
        chubiaoju()
        
        
        ##~ 去目的地
        if chengyaojin[0]>0:
            mudidi = 'chengyaojin'
            # yabiao_chengyaojin()
            
            new_sleep()
            # ca_dt()
            open_ditu()
            delay_sleep()
            d.click(1311,214)
            delay_sleep()
            close_ditu()
            sleep(60)
            d.click(768,31)
            sleep(5)
            
            delay_sleep()
            send_chengyaojin()
            new_sleep()
            
            #判断是否在移动,如果在移动则不处理,如果是静止,则判断是否进入战斗,如果进入战斗则点击自动,如果没进入战斗,则自动寻路去目的地
            temp = 1
            while temp > 0:
                yidong = isMove_once()   # 静止返回-1,在移动返回0,只判断一次,实时返回
                if yidong > -1 :
                    # 在移动,不作处理
                    pass
                else:
                    zhandou = isFight_once() # #fighting中,返回-1
                    if zhandou == -1 :
                        #在战斗中
                        quyu_click(2236,1000,2269,1020) #点自动
                        new_sleep()
                        quyu_click(2236,1000,2269,1020) #取消自动
                        new_sleep()
                        quyu_click(2236,1000,2269,1020) #再点一次自动
                        new_sleep()
                        sleep(8)  
                    
                    else:
                        # 判断是否到达目的地或入口
                        # 如果没有到达目的地,则继续打开地图走
                        pass
            
            
        elif kongdu[0]>0:
            yabiao_kongdu()
        
    else:
        send_message_to_slack('没打开领任务界面')
        sleep(60)
        
    #~ 押镖结束,回镖局
    

        
        
        
    
    
          
    
    
      
    
#~ 1.抓鬼   
# zhuagui_click_all_button()

#~ 2.师门
# shimen_click_all_button()

#~ 3.封妖
# fengyao()

action = sys.argv[1]

if action == 'zhuagui':
    zhuagui_click_all_button()
elif action == 'shimen':
    shimen_click_all_button()
elif action == 'fengyao':
    fengyao_all()
else:
    # denglu()
    # sell_hulu_zhuagui()
    # qihao()
    # quyu_click(1490,229,1810,512) #空白区域
    # click_renwu()
    # click_kongbai()
    
    # quyu_click(2220,1006,2270,1027) #点击自动
    # yabiao()
    # ca_dt()
    # send_chengyaojin()
    # send_biao_npc(1019,360,1022,388)
    # isMove_once()
    
    # yabiao_chengyaojin()
                    
    # ca_hs()
    
    # jiepin()
    # xx=matchImg('home_yabiao.jpg','./yabiaofile/datang_rukou.jpg')   
    # print(xx)
    # new_sleep()

    # open_ditu()
    # delay_sleep()
    # d.click(1311,214)
    # delay_sleep()
    # close_ditu()
    # sleep(60)
    
    
    # d.click(768,31)
    # sleep(5)
    
    # delay_sleep()
    # send_chengyaojin()
    # new_sleep()
    
    
                        
