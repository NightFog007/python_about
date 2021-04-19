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
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
sys.path.append('../')
import _thread
import time
from subprocess import call
from time import sleep

from random import randint as r
# from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,quyu_click,new_sleep,delay_sleep

import adbutils
import aircv as ac
import websocket

""" 你的APPID AK SK """
APP_ID = '17235153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

flag = 0

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

def random_num(x):
    return int(r(1,x))

# 获取像素点
def get_pic(image_path,pixelX,pixelY):
    img_src = Image.open(image_path)
    img_src = img_src.convert('RGBA')
    str_strlist = img_src.load()
    RGBA = str_strlist[pixelX, pixelY]
    img_src.close()
    # hex_str = '#'
    hex_str=''
    for i in RGBA:
        num = int(i) # 将RGBA的数值转换成数字类型
        hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
    # return  hex_str
    # return int('0x'+hex_str , 16)  # 返回整型
    return RGBA
    



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
    
def jiepin():
    image = d.screenshot(format='opencv')
    cv2.imwrite('home_zhuagui.jpg', image)
    sleep(1)   
    

    
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

        




def send_message():
    # cmd = 'display notification \"' + \
    # "Notificaton memo" + '\" with title \"手动处理\"'
    cmd = 'display notification \"' + \
    "Notificaton memo" + '\" with title \"手动处理\"'
    call(["osascript", "-e", cmd])        
        





def jishiqi(n):
    for i in range(0,n):
        print(i)
        sleep(1)

   
    

def open_ditu():
    quyu_click(206,75,309,116)  
    new_sleep()
    




# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

# d = u2.connect_usb('18bcc735')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

  
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
    print(match_result)
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



def close_guojingditu():
    quyu_click(1777,35,1814,70)
    new_sleep()
        

def jiepin2(filename='home_zhuagui.jpg'):
    image = d.screenshot(format='opencv')
    cv2.imwrite(filename, image)
    

def open_daoju():
    quyu_click(2109,1030,2129,1037)
    new_sleep()

def open_changan7():
    quyu_click(1180,330,1244,381)
    quyu_click(1180,330,1244,381)
    new_sleep()
    
def go_yizhan():
    quyu_click(1204,803,1208,807)
    new_sleep()
    
def close_t5_ditu():
    sleep(0.5)
    x = 1676 #关闭地图
    y = 63
    d.click(x, y)
        
    
def close_jingwai_ditu():
    sleep(0.5)
    x = 1750 #关闭地图
    y = 256
    d.click(x, y)     


# jiepin()
a = 'home_zhuagui.jpg'
b = '123.png'
# open_ditu()
# res = matchImg(a,b)
# print(res)

def close_jingwaiditu():
    quyu_click(1976,288,2000,300)
    new_sleep()
    
def close_daoju(): 
    quyu_click(1830,104,1864,123)
    new_sleep()


    
        

    
def open_ff():  ## ff放在第二行第四个位置
    open_daoju()
    # sleep(1)
    # quyu_click(1714,444,1751,505)
    # quyu_click(1714,444,1751,505)
    # new_sleep()
    
    # open_wupin()
    sleep(2)
    jiepin()
    sleep(1)
    feixingfu = matchImg('home_zhuagui.jpg','./feixingfu.jpg')
    if feixingfu[0] > 0:
        d.click(feixingfu[0],feixingfu[1])
        d.click(feixingfu[0],feixingfu[1])
    else:
        print("没找到飞行符")
    
    sleep(1)
    new_sleep()

            
    
def go_baoxiangguo():
    open_ff()
    quyu_click(984,595,991,622)
    new_sleep()
 
def go_xiliang():
    open_ff()
    quyu_click(985,442,1000,444)
    new_sleep()
    
def go_jianye():
    open_ff()
    quyu_click(1437,651,1475,674)
    new_sleep()
    
def go_yewai():
    open_daoju()
    sleep(1)
    open_changan7()
    d.click(1874,900)
    new_sleep()
    close_daoju()
    sleep(1)
    d.click(2336,931)
    sleep(2)
    
    
def open_al77():
    open_daoju()
    sleep(1)
    quyu_click(1600,292,1653,360)
    quyu_click(1600,292,1653,360)
    new_sleep()

def go_ne():
    open_al77()
    
    quyu_click(704,269,720,286)
    new_sleep()
    close_daoju()
    
    quyu_click(60,186,62,188)    


def open_cs77():
    open_daoju()
    sleep(1)
    quyu_click(1723,310,1765,351)
    quyu_click(1723,310,1765,351)
    new_sleep()
    
def open_zz77():
    open_daoju()
    sleep(1)
    quyu_click(1190,446,1236,492)
    quyu_click(1190,446,1236,492)
    new_sleep()        

def go_jingwai_left():
    open_zz77()
    d.click(685,900)
    new_sleep()
    close_daoju()
    sleep(1)
    d.click(82,961)
    sleep(2)
    
  

  
def go_guojing():
    open_daoju()
    open_changan7()
    
    d.click(555,904)
    new_sleep()
    close_daoju()
    sleep(1)
    d.click(114,955)
    sleep(2)
    

def go_pt():
    go_guojing()
    new_sleep()
    open_ditu()
    d.click(1440,829)
    new_sleep()
    close_guojingditu()
    new_sleep()
    sleep(30)
    d.click(1209,493)
    sleep(1)
    new_sleep()
    quyu_click(1907,507,1912,510)
        
def go_jingwai_right():
    go_guojing()
    new_sleep()
    open_ditu()
    d.click(904,834)
    new_sleep()
    close_guojingditu()
    new_sleep()
    sleep(63)  
    d.click(5,20)
    sleep(3)
    
def go_wz():
    go_jingwai_right()
    new_sleep()
    open_ditu()
    d.click(1950,536)
    sleep(1)
    new_sleep()
    close_jingwaiditu()
    sleep(28)
    d.click(2035,127)
    sleep(3)
    d.click(2336,205)
    sleep(2)


            
    
def jingwai_go_move():
    
    xiaoditu_zuobiao = [(1678,458),(1255,445),(393,440),(1255,445),(393,440)]
        
    x = int(random.choice('01234'))
    xx = xiaoditu_zuobiao[x]
    open_ditu()
    sleep(1)
    d.click(xx[0],xx[1])
    # close_t5_ditu()
    sleep(3)
    close_jingwai_ditu()


# s = isMove
# if s < 0:

def start(zuobiao,close):
    print("kaishi")
    
    gogogo  = 1
    while gogogo>0: 

        
        #^ 判断人物是否在移动,静止返回-1,在移动返回0,只判断一次,实时返回
        panduan1 = isMove_once()  
        # panduan2 = isFight_once()
        
        

        if  panduan1 ==0:
            while panduan1 == 0:
                sleep(1)
                panduan1 = isMove_once() 
                
                
        jiepin()
        zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
        if zhandou[0]>0:
        # if panduan1 ==0 :
        
        # isfight = 0 
        # if zhandou[0]>0:
            print("战斗中")
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('战斗中')
                else:
                    isfight = 0
                    print('战斗结束')
        else:
            # go_move()
            # jingwai_go_move()
            # huaguoshan_go_move()
            # haidi1_go_move()
            daidui_go_move(zuobiao,close)
            sleep(5)
            

        # 如果人物静止且不在战斗中,点小地图
        # 如果人物移动中, panduan1 = 0 ,跳过 
        # 如果人物战斗中, panduan2 = 0 ,跳过
            
        # if panduan1 < 0 and panduan2 < 0 :
        # if panduan1 < 0 and zhandou[0] == 0:
            # x = get_random_num(11)

# start(huaguoshan_zuobiao,huaguoshan_close)          

    
    



# 驿站老板对话框    
# def go_guojing_():
#     quyu_click(1882,503,2132,546)
#     new_sleep()
    

    
def goin_difu():    
    x = 1004
    y = 195
    
    d.click(x,y)
    new_sleep()
    
def ditu_guojing_to_difu():    
    # x = 768
    # y  =175
    # d.click(x,y)
    # quyu_click(768,175,770,176)
    x = 1004
    y = 195
    d.click(x,y)
    new_sleep()
    

def go_difu():
    d.click(1046,134)
    sleep(3)
    # new_sleep()
    # quyu_click(763,176,765,178)
    # new_sleep()
    
        
    
def go_zhongkui():    
    x = 1125
    y = 576
    d.click(x,y)

def close_difu_ditu():
    quyu_click(1820,105,1847,134)
    new_sleep()

   



 
def click_zhongkui():
    quyu_click(1077,521,1079,528) #点击钟馗npc
    new_sleep()
    
def ling_zhuagui():
    quyu_click(1941,584,2123,606) # 好的,我帮你 
    new_sleep()
    

def go_difang():
    
    sleep(1)
    jiepin()
    sleep(2)
    wz = matchImg('home_zhuagui.jpg','./difang/wenzi_wz.jpg') 
    jingwai = matchImg('home_zhuagui.jpg','./difang/wenzi_jingwai.jpg')
    ne = matchImg('home_zhuagui.jpg','./difang/wenzi_ne.jpg')
    al = matchImg('home_zhuagui.jpg','./difang/wenzi_al.jpg')
    cs = matchImg('home_zhuagui.jpg','./difang/wenzi_cs.jpg')
    jianye = matchImg('home_zhuagui.jpg','./difang/wenzi_jianye.jpg')
    yewai = matchImg('home_zhuagui.jpg','./difang/wenzi_yewai.jpg')
    zz = matchImg('home_zhuagui.jpg','./difang/wenzi_zz.jpg')
    xiliang = matchImg('home_zhuagui.jpg','./difang/wenzi_xiliang.jpg')
    # baoxiang = matchImg('home_zhuagui.jpg','./difang/wenzi_baoxiang.jpg')
    pt = matchImg('home_zhuagui.jpg','./difang/wenzi_pt.jpg')   
    
    
    
    if wz[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_wz()
    elif jingwai[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_jingwai_left()
    elif ne[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_ne()
    elif al[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        open_al77()
    elif cs[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        open_cs77()
    elif jianye[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_jianye()
    elif yewai[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_yewai()
    elif zz[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        new_sleep()
        open_zz77()
    elif xiliang[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_xiliang()
    elif pt[0]>0:
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_pt()
    else:
        image = d.screenshot(format='opencv')
        cv2.imwrite('baoxiang_wenzi_jiepin.jpg', image)
        sleep(1)  
        # send_message_to_slack('没找到地方')
        # sleep(10)
        quyu_click(1360,856,1378,915) #找到目的地.点击掉钟馗的对话框, 等抓到宝象国文字的图片后,这句代码可以合并到if的最上面
        go_baoxiangguo()
        
    sleep(2)
    send_message_to_slack('到达目的地')

def start_zhuagui():
    
    # jiepin()
    # zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
    # if zhandou[0]>0:
    #     print("战斗中")
    #     isfight = 1
    #     while isfight > 0:
    #         jiepin()
    #         sleep(0.5)
    #         zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
    #         if zhandou[0] > 0:
    #             isfight = 1
    #             print('战斗中')
    #         else:
    #             isfight = 0
    #             print('战斗结束')
    #             gogo_lingrenwu()
    # else:
    #     print('战斗结束')
    #     gogo_lingrenwu()
    #     sleep(1)
    #     go_difang()
        
    #     temp = 0
    #     while temp < 1:
    #         jiepin()
    #         sleep(1)
    #         zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
    #         if zhandou[0] < 0:
    #             temp = 0
    #             sleep(5)
    #         else:
    #             temp  =  2
    xx = 0
    while xx < 1:        
        jiepin()
        zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
        if zhandou[0]>0:
            print("战斗中")
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('战斗中')
                else:
                    isfight = 0
                    print('战斗结束')
                    # gogo_lingrenwu()
        else:
            print('战斗结束')
            
            
        gogo_lingrenwu_one_fly()
        sleep(1)
        go_difang()
        
        temp = 0
        while temp < 1:
            print("寻找gui中")
            jiepin()
            sleep(3)
            zhandou = matchImg('home_zhuagui.jpg','./qingchun-huihe.jpg')
            print(zhandou)
                
            if zhandou[0] > 0:
                print("进入了战斗")
                temp  =  2  
            else:
                print("没有进入战斗")
                temp = 0
                sleep(5)      

# 77只飞一次
def gogo_lingrenwu_one_fly():
    
    # xiangdui_zuobiao = [(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(11,22)]

    xinzuobiao = [(1354,459),(1294,573),(1111,606),(1171,621),(1151,417)]
    # zhao_yizhanlaoban = [(1100,473),(1106,454),(999,600),(916,615),(848,580),(897,472),(11,22)]
    
    
    open_daoju()  
    sleep(2)
    open_changan7() 
    sleep(2)
    go_yizhan() 
    delay_sleep()
    close_daoju()
    delay_sleep()
    
        
    for i in xinzuobiao:        
  
        d.click(i[0],i[1])
        delay_sleep()
        print('当前用的坐标是: %s ' % str(i) )
        
        jiepin2()
        sleep(2)
        yy = matchImg('home_zhuagui.jpg','queren_flag.jpg')
        if yy[0] > 0:
            sleep(1)
            d.click(yy[0],yy[1])
            print("找到了")
            break

        if i[0] == 1151:
            print("没找到")
            
            
            send_message_to_slack("出错了,没找到")
            nx  = 1
            while nx > 0:
                
                jiepin2()
                sleep(1)
                yy = matchImg('home_zhuagui.jpg','queren_flag.jpg')
                if yy[0] > 0:
                    sleep(1)
                    d.click(yy[0],yy[1])
                    print("找到了")
                    nx = 0
                    break
                
                sleep(3)



    delay_sleep()
    open_ditu()
    new_sleep()
    
    ditu_guojing_to_difu()
    new_sleep()
    close_guojingditu()
    sleep(20)
    goin_difu()
    delay_sleep()
    delay_sleep()
    open_ditu()
    new_sleep()
    go_zhongkui()
    new_sleep()
    close_difu_ditu()
    sleep(22)
    new_sleep()
    click_zhongkui()
    delay_sleep()
    # ling_zhuagui()
    # sleep(1)
    quyu_click(1918,654,1935,659)
    new_sleep()
    
    

 
# 每次都用77飞
def gogo_lingrenwu():
    
    # xiangdui_zuobiao = [(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(11,22)]

    
    # zhao_yizhanlaoban = [(1100,473),(1106,454),(999,600),(916,615),(848,580),(897,472),(11,22)]
    
    zhao_yizhanlaoban = [(1430,457),(1382,408),(1520,422),(1524,483),(1361,491) ,(1461,432)    ]
    # open_daoju()  

    # open_changan7() 
    # go_yizhan() 
    # sleep(0.8)
    # close_daoju()
    # new_sleep()
    
        
    for i in zhao_yizhanlaoban:
        
        open_daoju()  

        open_changan7() 
        go_yizhan() 
        sleep(0.8)
        close_daoju()

  
        d.click(i[0],i[1])
        delay_sleep()
        print('当前用的坐标是: %s ' % str(i) )
        
        jiepin2()
        sleep(2)
        yy = matchImg('home_zhuagui.jpg','queren_flag.jpg')
        if yy[0] > 0:
            sleep(1)
            d.click(yy[0],yy[1])
            print("找到了")
            break

        if i[0] == 1461:
            print("没找到")
            
            
            send_message_to_slack("出错了,没找到")
            nx  = 1
            while nx > 0:
                
                jiepin2()
                sleep(1)
                yy = matchImg('home_zhuagui.jpg','queren_flag.jpg')
                if yy[0] > 0:
                    sleep(1)
                    d.click(yy[0],yy[1])
                    print("找到了")
                    nx = 0
                    break
                
                sleep(3)



    delay_sleep()
    open_ditu()
    new_sleep()
    
    ditu_guojing_to_difu()
    new_sleep()
    close_guojingditu()
    sleep(20)
    goin_difu()
    delay_sleep()
    delay_sleep()
    open_ditu()
    new_sleep()
    go_zhongkui()
    new_sleep()
    close_difu_ditu()
    sleep(22)
    new_sleep()
    click_zhongkui()
    delay_sleep()
    # ling_zhuagui()
    # sleep(1)
    quyu_click(1918,654,1935,659)
    new_sleep()

    
     

# jiepin()
# gogo_lingrenwu()

start_zhuagui()
# go_wz()

# jiepin()    
# yy = matchImg
# ('home_zhuagui.jpg','queren_flag.jpg')
# if yy[0] > 0:
#     # sleep(1)
#     # d.click(yy[0],yy[1])
#     print("找到了")      
    
#~ 1.抓鬼   
# zhuagui_click_all_button()

#~ 2.师门
# shimen_click_all_button()

#~ 3.封妖
# fengyao()

# action = sys.argv[1]

# if action == 'zhuagui':
#     zhuagui_click_all_button()
# elif action == 'shimen':
#     shimen_click_all_button()
# elif action == 'fengyao':
#     fengyao_all()
# else:
#     # denglu()
#     # sell_hulu_zhuagui()
#     # quyu_click(1490,229,1810,512) #空白区域
#     # click_renwu()
#     # click_kongbai()
    
#     # quyu_click(2220,1006,2270,1027) #点击自动
#     goin_difu()
    

        