import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
import re
import numpy as np
from cv2 import cv2 
from aip import AipOcr
from random import randint as r
from fast_screenshot import jiepin
from send_text import send_message_to_slack


from time import sleep 
from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu,quyu_click,new_sleep,delay_sleep

import aircv as ac


def num_r():
    return int(r(1,5))

def random_num(x):
    return int(r(1,x))
# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

d = u2.connect_usb('DLQ0216505001224') # 华为



def num_r():
    return int(r(1,5))

def random_num(x):
    return int(r(1,x))

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
    rd = num_r()
    nx= xx[0]+rd
    ny = xx[1]+rd
    # d.click(xx[0],xx[1])
    d.click(nx,ny)
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
    sleep(1)   
    
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
    
    

def beiju_move():
    open_ditu()
    sleep(1)
    quyu_click(677,286,1451,880)
    
    delay_sleep()
    sleep(1)
    
    # 判断地图是否打开着
    jiepin2()  
    sleep(1)
    ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # print(zhandou)
    
    if(ditu_open[0])>0:
        #关闭地图
        # quyu_click(1549,121,1609,136) 
        quyu_click(1560,116,1605,157)
    
    new_sleep()
    

    
def huaguoshan_move():
    open_ditu()
    sleep(1)
    quyu_click(742,352,1391,846)
    delay_sleep()
    sleep(1)
    
    # 判断地图是否打开着
    jiepin2()  
    sleep(1)
    ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # print(zhandou)
    
    if(ditu_open[0])>0:
        #关闭地图
        quyu_click(1549,121,1609,136) 
    
    new_sleep()
    
def long1_move():
    open_ditu()
    sleep(1)
    quyu_click(392,257,1458,803)
    delay_sleep()
    sleep(1)
    
    
    
    # 判断地图是否打开着
    jiepin2()  
    sleep(1)
    ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # print(zhandou)
    
    if(ditu_open[0])>0:
        #关闭地图
        quyu_click(1637,45,1661,104) 
    
    new_sleep()
    


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
            time_start = time.time() #开始计时

        # isfight = 0 
        # if zhandou[0]>0:
            print("fight中")
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('fighting中')
                    time_end = time.time()    #结束计时
                    time_c= time_end - time_start   #运行所花时间
                    time_c=int(time_c)
                    print('战斗耗时: ' + str(time_c))
                    if time_c > 70:
                        send_message_to_slack('fight超时')
                        time.sleep(30)
                else:
                    isfight = 0
                    print('fighting结束')
        else:
            
            long1_move()
            # huaguoshan_move()
            # beiju_move()
            # daidui_go_move(zuobiao,close)
            sleep(5)
            new_sleep()
            

        # 如果人物静止且不在fighting中,点小地图
        # 如果人物移动中, panduan1 = 0 ,跳过 
        # 如果人物fighting中, panduan2 = 0 ,跳过
            
        # if panduan1 < 0 and panduan2 < 0 :
        # if panduan1 < 0 and zhandou[0] == 0:
            # x = get_random_num(11)

# L1的坐标
long1_zuobiao =    [(467,322),(1335,260),(450,840),(1269,703),(999,267)] 
long1_close= (1641,119)

# L2的坐标
long2_zuobiao =    [(420,264),(446,844),(1407,853),(1488,666),(796,584)] 
long2_close= (1641,119)

# 花果山
huaguoshan_zuobiao =  [(1433,317),(1062,302),(698,297),(697,851),(1413,862)] 
huaguoshan_close = (1586,129)

# 海底1
haidi1_zuobiao = [(641,276),(669,896),(1512,294),(1507,920),(1058,562)] 
haidi1_close = (1606,110)

# 北俱
beiju_zuobiao = [(643,294),(1447,284),(702,525),(640,910),(1425,700)] 
beiju_close = (1575,124)
# start(long1_zuobiao,long1_close)  
start(huaguoshan_zuobiao,huaguoshan_close)
# start(long2_zuobiao,long2_close)          
# start(huaguoshan_zuobiao,huaguoshan_close)          
# start(haidi1_zuobiao,haidi1_close)   
# start(beiju_zuobiao,beiju_close)          




# jiepin()
# zhandou = matchImg('home.jpg','./chongzhi.jpg')
# zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
# print(zhandou)