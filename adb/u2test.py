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
            
            zipped = zip(*loc[::-1])  #list[::-1] 相当于起点为最后的一个,终点为第一个,然后一次减少一个
            positions[teNum] = (list(zipped))[0]
            
        else:
            print("Can not found pic: ")

        end = time.time()
        print(end - start)

        return positions[teNum]  


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
    
    
def T5_move():
    open_ditu()
    
    quyu_click(401,320,1498,790)
    delay_sleep()
    sleep(1)
    
    
    
    # quyu_click(1619,66,1658,78) 
    # # 判断地图是否打开着 #~ 3,26注释掉, 直接点关闭地图的地方,不用判断地图是否打开
    # jiepin2()  
    # sleep(1)
    # ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # # print(zhandou)
    
    # if(ditu_open[0])>0:
    #     #关闭地图
    #     quyu_click(1619,66,1658,78) 
    
        
def long1_move():
    open_ditu()
    
    quyu_click(392,257,1458,803)
    delay_sleep()
    sleep(1)
    
    
    
    quyu_click(1619,66,1658,78) 
    # # 判断地图是否打开着 #~ 3,26注释掉, 直接点关闭地图的地方,不用判断地图是否打开
    # jiepin2()  
    # sleep(1)
    # ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # # print(zhandou)
    
    # if(ditu_open[0])>0:
    #     #关闭地图
    #     quyu_click(1619,66,1658,78) 
    
def long3_move():
    open_ditu()
    sleep(1)
    quyu_click(391,311,1462,842)
    delay_sleep()
    sleep(1)  
    
    
    quyu_click(1619,66,1658,78) 
    # # 判断地图是否打开着 #~ 3,26注释掉, 直接点关闭地图的地方,不用判断地图是否打开
    # jiepin2()  
    # sleep(1)
    # ditu_open = matchImg('home.jpg','./map_cunzai.jpg',0.85)      
    # # print(zhandou)
    
    # if(ditu_open[0])>0:
    #     #关闭地图
    #     quyu_click(1619,66,1658,78) 
    
    new_sleep()


zidong = matchImg('xxx.jpg','./chongzhi_pic.jpg',0.3)
# zidong = get_pay_keyboard_number_location('test_home.jpg','chongzhi_pic.jpg',0.8)
if zidong[0]<=0:
    
    print("取消自动了")
else:
    print("自动 ing")