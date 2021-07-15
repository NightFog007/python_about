import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
import re
import numpy as np
from cv2 import cv2 
from aip import AipOcr

import sys 

sys.path.append('../')
from fast_screenshot import jiepin

from time import sleep 
from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu,quyu_jietu

import aircv as ac

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import time 

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

client = WebClient(token='xoxb-878537608886-1683457705654-Vx4DSD1U2yGuIc2GCxmpVwhI')

def send_message_to_slack(content):

    try:
        response = client.chat_postMessage(channel='梦幻', text=content)
        # assert response["message"]["text"] == "Hello world!"
        # print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
        
    time.sleep(10)  



# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

d = u2.connect_usb('DLQ0216505001224')

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
 
def close_haidi1_ditu():
    sleep(0.5)
    x = 1606 #关闭地图
    y = 110
    d.click(x, y) 
            
             
def close_huaguoshan_ditu():
    sleep(0.5)
    x = 1586 #关闭地图
    y = 129
    d.click(x, y) 
    
def daidui_go_move(zuobiao,close_ip):
    # xiaoditu_zuobiao = [(641,276),(669,896),(1512,294),(1507,920),(1058,562)] 

    xiaoditu_zuobiao = zuobiao
        
    x = int(random.choice('01234'))
    xx = xiaoditu_zuobiao[x]
    open_ditu()
    sleep(1)
    d.click(xx[0],xx[1])
    sleep(1)
    x = close_ip[0] #关闭地图
    y = close_ip[1]
    d.click(x, y) 
            
def haidi1_go_move():
    
    
    xiaoditu_zuobiao = [(641,276),(669,896),(1512,294),(1507,920),(1058,562)] 
        
    x = int(random.choice('01234'))
    xx = xiaoditu_zuobiao[x]
    open_ditu()
    sleep(1)
    d.click(xx[0],xx[1])
    # close_t5_ditu()
    sleep(2)
    close_haidi1_ditu()
            
def huaguoshan_go_move():
    
    
    xiaoditu_zuobiao = [(1433,317),(1062,302),(698,297),(697,851),(1413,862)] 
        
    x = int(random.choice('01234'))
    xx = xiaoditu_zuobiao[x]
    open_ditu()
    sleep(1)
    d.click(xx[0],xx[1])
    # close_t5_ditu()
    sleep(2)
    close_huaguoshan_ditu()
    

def jiepin2():
    image = d.screenshot(format='opencv')
    cv2.imwrite('home.jpg', image)
    
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





#! 打开小地图移动
def go_move(ditu = 't5'):
    # now = ditu 
    # if now == 't5':
    #     # xiaoditu_zuobiao = [(520,482),(997,270),(1095,307),(1372,445),(1342,565),(1600,565),(1360,667),(102,825),(990,640),(1132,780),(652,685),(540,407)]
    #     xiaoditu_zuobiao = [(396,567),(641,712),(662,680),(974,241),(791,481)]
    # elif now =='t6':
    #     xiaoditu_zuobiao = [(520,482),(997,270),(1095,307),(1372,445),(1342,565),(1600,565),(1360,667),(102,825),(990,640),(1132,780),(652,685),(540,407)]
    # elif now == 'jingwai':
    #     xiaoditu_zuobiao = [(1678,458),(1255,445),(393,440),(1255,445),(393,440)]
       
    xiaoditu_zuobiao = [(396,567),(641,712),(662,680),(974,241),(791,481)] 
    # x = get_09()
    x = int(random.choice('01234'))
    xx = xiaoditu_zuobiao[x]
    open_ditu()
    sleep(1)
    d.click(xx[0],xx[1])
    close_t5_ditu()
    # close_jingwai_ditu()
    
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
        zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
        if zhandou[0]>0:
        # if panduan1 ==0 :
        
        # isfight = 0 
        # if zhandou[0]>0:
            print("战斗中")
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
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

def open_daoju():
    new_sleep()
    quyu_click(1675,1023,1710,1037)
    new_sleep()

def open_changan7():
    new_sleep()
    quyu_click(948,298,1000,375)
    quyu_click(948,298,1000,375)
    new_sleep()
    
def go_yizhan():
    new_sleep()
    quyu_click(956,807,963,811)
    new_sleep()
    
    
def click_yizhan():
    x = 874
    y = 434
    d.click(x,y)
    
    x = 1050
    y  = 520


# 驿站老板对话框    
def go_guojing():
    new_sleep()
    quyu_click(1500,507,1712,530)
    new_sleep()
    
def close_guojingditu():
    x = 1566
    y = 49
    d.click(x,y)    
    
def goin_difu():    
    x = 633
    y = 233
    d.click(x,y)
    
def ditu_guojing_to_difu():    
    # x = 768
    # y  =175
    # d.click(x,y)
    quyu_click(768,175,770,176)
    
def go_zhongkui():    
    x = 888
    y = 571
    d.click(x,y)

def close_difu_ditu():
    new_sleep()
    quyu_click(1578,115,1605,149)
    new_sleep()

   

    
def close_daoju():    
    new_sleep()
    quyu_click(1588,93,1611,115)
    new_sleep()

def go_difu():
    # x = 763
    # y = 176
    # d.click(x,y)
    new_sleep()
    quyu_click(763,176,765,178)
    new_sleep()
 
def click_zhongkui():
    new_sleep()
    quyu_click(841,530,842,536) #点击钟馗npc
    new_sleep()
    
def ling_zhuagui():
    new_sleep()
    quyu_click(1500,628,1643,669) # 好的,我帮你 
    new_sleep()
    
    
def go_pt():
    return 1
    
def go_jingwai_right():
    open_daoju()  

    open_changan7() 
    go_yizhan() 
    sleep(0.8)
    close_daoju()
    new_sleep()
    
    nx  = 1
    while nx > 0:
        send_message_to_slack("处理一下")
        jiepin2()
        sleep(1)
        yy = matchImg('home.jpg','queren_flag.jpg')
        if yy[0] > 0:
            sleep(1)
            d.click(yy[0],yy[1])
            print("找到了")
            nx = 0
            break
        
        sleep(3)
        
    sleep(1)
    new_sleep()
    open_ditu()
    
    new_sleep()
    d.click(653,831)
    new_sleep()
    quyu_click(1551,50,1578,72) #关闭国境地图

    
    sleep(65)
    
    d.click(134,202) #去境外
    sleep(5)  #sleep后到达境外
    
    

def start_zhuagui():
    
    jiepin()
    zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
    if zhandou[0]>0:
        
    # if panduan1 ==0 :
    
    # isfight = 0 
    # if zhandou[0]>0:
        print("战斗中")
        isfight = 1
        while isfight > 0:
            jiepin()
            sleep(0.5)
            zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
            if zhandou[0] > 0:
                isfight = 1
                print('战斗中')
            else:
                isfight = 0
                print('战斗结束')
                gogo_lingrenwu()
    else:
        print('战斗结束')
        gogo_lingrenwu()
 
 

def gogo_lingrenwu():
    
    # xiangdui_zuobiao = [(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(11,22)]

    
    zhao_yizhanlaoban = [(1100,473),(1106,454),(999,600),(916,615),(848,580),(897,472),(11,22)]
    
    
    open_daoju()  

    open_changan7() 
    go_yizhan() 
    sleep(0.8)
    close_daoju()
    new_sleep()
    
        
    for i in zhao_yizhanlaoban:
        
        # open_daoju()  

        # open_changan7() 
        # go_yizhan() 
        # sleep(0.8)
        # close_daoju()
        # new_sleep()

  
        d.click(i[0],i[1])
        new_sleep()
        print('当前用的坐标是: %s ' % str(i) )
        
        jiepin2()
        sleep(2)
        yy = matchImg('home.jpg','queren_flag.jpg')
        if yy[0] > 0:
            sleep(1)
            d.click(yy[0],yy[1])
            print("找到了")
            break

        if i[0] == 11:
            print("没找到")
            
            
            nx  = 1
            while nx > 0:
                send_message_to_slack("出错了,没找到")
                jiepin2()
                sleep(1)
                yy = matchImg('home.jpg','queren_flag.jpg')
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
    ling_zhuagui()
     


# xiangdui_zuobiao = [(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(1197,395),(1116,454),(1278,425),(1292,333),(1196,344)]

# for i in xiangdui_zuobiao:
    
#     open_daoju()  


#     open_changan7() 
#     sleep(1)
#     go_yizhan() 
#     sleep(0.8)
#     close_daoju()
#     sleep(2)

#     d.click(i[0],i[1])
#     sleep(1)
    
#     jiepin2()
#     sleep(1)
#     yy = matchImg('home.jpg','queren_flag.jpg')
#     if yy[0] > 0:
#         sleep(1)
#         d.click(yy[0],yy[1])
#         print("找到了")
#         break



# sleep(2)
# open_ditu()
# time.sleep(1)
# ditu_guojing_to_difu()
# sleep(1)
# close_guojingditu()
# sleep(20)
# goin_difu()
# sleep(5)
# open_ditu()
# sleep(1)
# go_zhongkui()
# sleep(1)
# close_difu_ditu()
# sleep(20)
# click_zhongkui()
# sleep(2)
# ling_zhuagui()


#(274,41)
# start_zhuagui()
# jiepin2()

go_jingwai_right()