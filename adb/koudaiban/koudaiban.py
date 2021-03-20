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
    

# x1 =  get_pic('a1.jpg',1,1)
# x2 = get_pic('b1.jpg',1,1)
# x3=  get_pic('c1.jpg',1,1)
# x4 = get_pic('a2.jpg',1,1)
# x5 =  get_pic('b2.jpg',1,1)
# x6 = get_pic('c2.jpg',1,1)
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(x6)

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
    cv2.imwrite('home.jpg', image)
    sleep(1)   
    
# def jiepin():
#     nn = random.choice("012345679abcdefghijklmn")
#     # d = adbutils.adb.device('18bcc735')  # 小米10青春版
#     d = adbutils.adb.device('emulator-5554')   # 华为
#     lport = d.forward_port(7912 )
#     ws = websocket.WebSocket()
#     ws.connect("ws://localhost:{}/minicap".format(lport))

#     index = 0
#     # start = time.time()
#     while True:
#         data = ws.recv()
#         if not isinstance(data, (bytes, bytearray)):
#             # print(data)
#             continue
#         # with open("home{nx}.jpg".format(nx = nn) , "wb") as f:
#         with open("home.jpg" , "wb") as f:
#             f.write(data)
#             index += 1
#         # print(index)
#         if index > 0:
#             break

#     # duration = time.time() - start
#     # print("Image per second: %.2f" % (100/duration))
#     ws.close()

def click_renwu():
    x = 390
    y = 1370
    d.click(x,y)
    
# click_renwu()



    
def click_shimen():
    x = 440
    y = 475
    d.click(x,y)
    # 点菜单
    # return 0
    
def click_zhuagui():
    x = 425- num_r()
    y = 1132- num_r()
    d.click(x,y)   
    
def click_shimen_renwu():
    x = 773 - num_r()
    y = 1248 - num_r()
    d.click(x,y)   
    sleep(0.2)
    x = 773
    y = 1248
    d.click(x,y)

def click_zhidaole():
    x = 773- num_r()
    y = 1248- num_r()
    d.click(x,y)  
    
    
# jiepin()
def quyu_jietu(x,y,width,height,name='temp'):

    # jiepin()
    img = Image.open("home.jpg")
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

        

def click_next_page(): #当前页面没找到目标鬼,则点击四次右下角的下一页按钮
    x = 953- num_r()
    y = 1703- num_r()
    d.click(x,y)
    d.click(x,y)
    d.click(x,y)
    d.click(x,y)
    sleep(2)
    
def click_renwu():
    quyu_click(436,2178,514,2255)

def click_zhuagui_caidan():    
    quyu_click(125,1469,981,1641)
    
def click_bangmangzhuagui():
    quyu_click(784,2034,1004,2081)
    
def sell_hulu_zhuagui():
    # 点击宝库
    quyu_click(245,1384,367,1497)
    sleep(1)
    new_sleep(1)
    for i in range(3):
        # 点击出售
        quyu_click(100,2230,328,2275)
        sleep(1)
        new_sleep(1)
        # 点击确定
        quyu_click(644,1388,893,1438)
        new_sleep(1)
    
    # 关闭卖葫芦界面
    delay_sleep()
    x = 1026+ random_num(2)
    y = random.sample(range(263,301),1)
    d.click(x,y[0])
    new_sleep(1)
        
    
    
    
def zhuagui_click_all_button(): 
    
    # 从进入主界面开始
    sleep(1)
    new_sleep()
    click_renwu()
    
    sleep(1)
    new_sleep()
    click_zhuagui_caidan()
    
    sleep(2)
    
    print("开始点击右下角")
    while 1> 0:

        jiepin()
        
        kaishi = matchImg('home.jpg','./main_pic/wenzi_kaishi.jpg')
        
        chufa = matchImg('home.jpg','./main_pic/wenzi_chufa.jpg')

        zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
        
        pintu = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')
        
        finish = matchImg('home.jpg','./main_pic/zhuagui_finish.jpg')

        
        isfight = 0
        
        if kaishi[0]>0:
            zhaogui()
            # d.click(kaishi[0],kaishi[1])
        elif chufa[0] > 0:
            quyu_click(784,690,1033,723)
            # d.click(chufa[0],chufa[1])
        elif zhandou[0] > 0:
            #在fighting, 循环判断fighting是否结束
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('fighting中')
                else:
                    isfight = 0
                    print('fighting结束')
        elif pintu[0]>0:
            print("是拼图")
            sigongge()
            # send_message()
        elif finish[0]>0:
            
            sleep(5)
            
            delay_sleep()
            quyu_click(1027,238,1034,294)
            
            delay_sleep()
            sell_hulu_zhuagui()
            
            sleep(1)
            tuichu()
            sleep(random_num(2))
            # 点击选择角色的按钮
            quyu_click(1567,606,1586,623)
            
            # d.click(1450,640) 
            send_message_to_slack('zhuagui结束')
            
            send_message()
            sys.exit()
            # print("开始进行师门任务")
            # d.click(334- num_r(),726- num_r())
            # sleep(2)
            # shimen_click_all_button()
          
        click_youxiajiao() 
        new_sleep(2)
        click_bangmangzhuagui()
        click_bangmangzhuagui() 
        # click_youxiajiao()
        # click_youxiajiao() 
        new_sleep(2)
        click_bangmangzhuagui()
        # x = 688
        # y = 1257
        # d.click(x,y)
        # d.click(x,y)
        # d.click(x,y)
        # d.click(x,y)
        
        # if finish_flag[0] == 0:
        #     x = 688
        #     y = 1257
        #     d.click(x,y)
        #     d.click(x,y)
        #     d.click(x,y)
        #     d.click(x,y)
        # else:
        #     print("抓鬼任务结束,结束程序")
        #     sys.exit()
        sleep(3)

def click_all_button_simen(): #右下角继续任务的按钮,可以放个线程一直点击
    while 1 >  0:
        # wancheng = matchImg('home.jpg','huluman.jpg')
        # print(wancheng)
        # if wancheng[0] > 0:
        #     d.click(627,1208)
        #     sleep(1)
            
        finish_flag = matchImg('home.jpg','renwu_jieshu.jpg')
        if finish_flag[0] == 0:
            print("继续师门任务")

            click_youxiajiao()
            click_youxiajiao()
            click_youxiajiao()
            click_youxiajiao()
            sleep(2)
            click_youxiajiao()
            # d.click(x,y)
            sleep(3)
            # if flag == 0:
            #     d.click(x,y)
            #     d.click(x,y)
            #     d.click(x,y)
            #     sleep(5)
            # else :
            #     pass               
        else:            
            sys.exit()
        sleep(3)      
        
        
def click_kaishi():  #识别要找的鬼后,点击这个开始按钮
    print("点击开始")
    # sleep(1)
    # x = 600- num_r()
    # y = 1411- num_r()
    # d.click(x,y)
    new_sleep(2)
    quyu_click(443,1391,675,1433)

    

def shimen_nvyi():
    
    n  = 0
    
    
    while n < 2:
        
        # for x in range(4):
    
        jiepin()

        sttr = ['10_you','10_shang','10_xia','10_zuo','20_you','20_shang','20_xia','20_zuo','30_you','30_shang','30_xia','30_zuo','40_you','40_shang','40_xia','40_zuo','50_you','50_shang','50_xia','50_zuo','70_you','70_shang','70_xia','70_zuo']
        # name = 'mamian'
        for i in sttr:
            gui_pic = './shimen_wupin/nvyi/nvyi{}.jpg'.format(i)
            # gui_pic = 'mamian_shang.jpg'
            # print(gui_pic)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0 :
                
                d.click(res[0],res[1])
                n = n + 1
                
        
        click_next_page()
        

    
    return 0 


def shimen_fuhuoyao():
    
    n  = 0
    
    
    while n < 2:
        
        # for x in range(4):
    
        jiepin()

        sttr = ['you','shang','xia','zuo','you2','shang2','xia2','zuo2']
        # name = 'mamian'
        for i in sttr:
            gui_pic = './shimen_wupin/fuhuoyao_{}.jpg'.format(i)
            # gui_pic = 'mamian_shang.jpg'
            # print(gui_pic)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0 :
                
                d.click(res[0],res[1])
                n = n + 1
                
        
        click_next_page()
        

    
    return 0  


    
      
def find_gui(name):
    
    for x in range(4):
    
    # while x < 0:
    
        jiepin()

        sttr = ['you','shang','xia','zuo']
        # name = 'mamian'
        for i in sttr:
            gui_pic = './new_gui_pic/{}_{}.jpg'.format(name,i)
            # gui_pic = 'mamian_shang.jpg'
            print(gui_pic)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0 and res[1]>0:
                
                d.click(res[0],res[1])
                x = 0
                return 0
        
        click_next_page()
        

    
    return 0  


def find_gui2(name):
    
    for x in range(4):
    
    # while x < 0:
    
        jiepin()

        sttr = ['you','shang','xia','zuo','you2','shang2','xia2','zuo2']
        # name = 'mamian'
        for i in sttr:
            gui_pic = './new_gui_pic/{}_{}.jpg'.format(name,i)
            # gui_pic = 'mamian_shang.jpg'
            print(gui_pic)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0 and res[1]>0:
                
                d.click(res[0],res[1])
                x = 0
                return 0
        
        click_next_page()
        

    
    return 0 


def find_xianglu():
    
    x = -1
    
    for i in range(4):
    
        jiepin()
        
        # sttr = ['you','shang','xia','zuo']
        xianglu_name = ['xianglu_zuo.jpg','xianglu_you.jpg','xianglu_shang.jpg','xianglu_xia.jpg']
        # name = 'mamian'
        for i in xianglu_name:
            gui_pic = './new_gui_pic/{}'.format(i)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0:
                
                d.click(res[0],res[1])
                x = 0
                return 0
        
        click_next_page()
        
    
    return 0   

def find_jiu():
    
    x = -1
    
    for i in range(5):
    
        jiepin()
        
        # sttr = ['you','shang','xia','zuo']
        jiu_name = ['hugu_shang.jpg','hugu_you.jpg','hugu_zuo.jpg','meihua_shang.jpg','meihua_xia.jpg','meihua_you.jpg','meihua_zuo.jpg','shedan_shang.jpg','shedan_you.jpg','shedan_zuo.jpg','zhenlu_shang.jpg','zhenlu_xia.jpg','zhenlu_you.jpg','zhenlu_zuo.jpg']
        # name = 'mamian'
        for i in jiu_name:
            gui_pic = './new_jiu/{}'.format(i)
            # gui_pic = 'mamian_shang.jpg'
            # print(gui_pic)
            
            res = matchImg('home.jpg',gui_pic)
            if res[0]>0 and res[1]>0:
                
                d.click(res[0],res[1])
                x = 0
                return 0
        
        click_next_page()
        

    
    return 0  

def isPintu(): #^ 是拼图则返回-1
    # jiepin()
    sleep(1)
    nn = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')
    if nn[0]>0 and nn[1]>0:
        return -1
    else:
        return 0

# find_gui('yegui')

def zhaogui():
    
    # jiepin()
    # pintu = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')
    # print(pintu)
    jiangshi = matchImg('home.jpg','./new_gui_pic/wenzi_jiangshi.jpg')
    niutou = matchImg('home.jpg','./new_gui_pic/wenzi_niutou.jpg') 
    mamian = matchImg('home.jpg','./new_gui_pic/wenzi_mamian.jpg') 
    yegui = matchImg('home.jpg','./new_gui_pic/wenzi_yegui.jpg') 
    kulouguai = matchImg('home.jpg','./new_gui_pic/wenzi_kulouguai.jpg') 
    paojiu = matchImg('home.jpg','./new_gui_pic/wenzi_jiu.jpg')
    xianglu = matchImg('home.jpg','./new_gui_pic/wenzi_xianglu.jpg')
    lazhu = matchImg('home.jpg','./new_gui_pic/wenzi_lazhu.jpg')
    huangzhi = matchImg('home.jpg','./new_gui_pic/wenzi_huangzhi.jpg')
    huangjin = matchImg('home.jpg','./new_gui_pic/wenzi_huangjin.jpg')
    
    # xunwu = matchImg('home.jpg','./new_gui_pic/wenzi_xunwu.jpg') 

    if jiangshi[0] > 0 :
        click_kaishi()
        sleep(1)
        find_gui('jiangshi')
    elif niutou[0] > 0:
        click_kaishi()
        sleep(1)
        print("找牛头")
        # find_gui('niutou')
        find_gui2('niutou')
    elif mamian[0] > 0:
        click_kaishi()
        sleep(1)
        find_gui2('mamian')
    elif yegui[0] > 0:
        click_kaishi()
        sleep(1)
        find_gui('yegui')
    elif kulouguai[0] > 0:
        click_kaishi()
        sleep(1)
        # find_gui('kulouguai')
        find_gui2('kulouguai')
    elif paojiu[0]>0:
        click_kaishi()
        sleep(1)
        find_jiu()
    elif xianglu[0]>0:
        click_kaishi()
        sleep(1)
        find_xianglu()
    elif lazhu[0]>0:
        click_kaishi()
        sleep(1)
        find_gui('lazhu')
    elif huangzhi[0]>0:
        click_kaishi()
        sleep(1)
        find_gui('huangzhi')
    elif huangjin[0]>0:
        click_kaishi()
        sleep(1)
        find_gui('huangjin')
    # elif  pintu[0]>0:
    #     print("是拼图")
    #     sigongge()
        
    # elif xunwu[0] > 0:
    else:
        # send_message()
        send_message_to_slack('来手动处理')
    
    
        
        
    
    
    
    
    # if res_word == '骷髅怪':
    #     find_gui('kulouguai')
    # elif res_word == '僵尸':
    #     find_gui('jiangshi')
    # elif res_word == '牛头':
    #     find_gui('niutou')
    # elif res_word == '马面':
    #     find_gui('mamian')
    # elif res_word == '野鬼':
    #     find_gui('yegui') 
    # # elif res_word == '泡成的':
    # elif show[0]['location']['top'] == 11:
    #     #要找酒, 弹出提示框,手动找
    #     # sys.exit()
    #     find_jiu()
    
   
    
    # quyu_jietu(420,670,560,740)
    
    # over = -1
    # x = 0 
    # y = 0
    # image = get_file_content('temp.jpg')

    # show = []
    # options = {}
    # options["probability"] = "true"
    # Result=client.general(image)
    # print(Result)
    # try:
        
    #     show=Result['words_result']
    #     print(show)
    
    # except:
    #     pass 
    
    # time.sleep(1)
    
    # if len(show)>0:
        
    #     click_kaishi()
    #     sleep(1)
    #     res_word = show[0]['words']
    #     # print(res_word)
        
    #     click_kaishi()
    #     sleep(2)

    #     if res_word == '骷髅怪':
    #         find_gui('kulouguai')
    #     elif res_word == '僵尸':
    #         find_gui('jiangshi')
    #     elif res_word == '牛头':
    #         find_gui('niutou')
    #     elif res_word == '马面':
    #         find_gui('mamian')
    #     elif res_word == '野鬼':
    #         find_gui('yegui') 
    #     # elif res_word == '泡成的':
    #     elif show[0]['location']['top'] == 11:
    #         #要找酒, 弹出提示框,手动找
    #         # sys.exit()
    #         find_jiu()



def isFight_once():  #fighting中,返回-1
    res = 0
    xx = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
    if xx[0]> 0 and xx[1] > 0:
        print("fighting中")
        res = -1

    return res

# zhaogui()



def sigongge():
       
    x1 = 340
    y1 = 1149
    
    x2 = 754
    y2 = 1100
    
    x3 = 324
    y3 = 1543
    
    x4 = 762
    y4 = 1541
    
    flag = 1 
    
    while flag > 0 :
    
        # xA1 = 124 #!
        # yA1 = 900

        # xB1=  529 #!
        # yB1= 900

        # xC1 = 124   #!
        # yC1 = 1307

        # # xD1 = 4 
        # # yD1=805

        # xA2 = 550 #!
        # yA2 = 900

        # xB2 = 953 #!
        # yB2 = 900
        
        # xC2 = 550   #!
        # yC2 = 1307
        
        # # xD2= 800  
        # # yD2=805
        
        # pic_test = './main_pic/pintu_beijing.jpg'
        # jiepin()
        
        # quyu_jietu(xA1,yA1,xA1+10,yA1+10,'a1')
        # # quyu_jietu(xB1-10,yB1,xB1,yB1+10,'b1')
        # quyu_jietu(xB1,yB1,xB1+6,yB1+10,'b1')

        # quyu_jietu(xC1,yC1-10,xC1+10,yC1,'c1')
        # # quyu_jietu(xD1,yD1,xD1-10,yD1-10,'d1')
        # quyu_jietu(xA2,yA2,xA2+6,yA2+10,'a2')
        # # quyu_jietu(xB2-10,yB2,xB2,yB2+7,'b2')
        # quyu_jietu(xB2,yB2,xB2+7,yB2+7,'b2')

        # quyu_jietu(xC2,yC2-10,xC2+6,yC2,'c2')
        # quyu_jietu(xD2,yD2,xD2-10,yD2-10,'d2')
        
        xA1 = 120  #!
        yA1 = 900

        xB1=  530  #!
        yB1= 900

        xC1 = 120    #!
        yC1 = 1307

        # xD1 = 4 
        # yD1=805

        xA2 = 546 #!
        yA2 = 900

        xB2 = 958#!  
        yB2 = 900
        
        xC2 = 546 #!  
        yC2 = 1307
        
        # xD2= 800  
        # yD2=805
        
        pic_test = './main_pic/pintu_beijing.jpg'
        jiepin()
        
        quyu_jietu(xA1,yA1,xA1+5,yA1+10,'a1')
        # quyu_jietu(xB1-10,yB1,xB1,yB1+10,'b1')
        quyu_jietu(xB1,yB1,xB1+6,yB1+10,'b1')

        quyu_jietu(xC1,yC1-10,xC1+5,yC1,'c1')
        # quyu_jietu(xD1,yD1,xD1-10,yD1-10,'d1')
        quyu_jietu(xA2,yA2,xA2+6,yA2+10,'a2')
        # quyu_jietu(xB2-10,yB2,xB2,yB2+7,'b2')
        quyu_jietu(xB2,yB2,xB2+4,yB2+7,'b2')

        quyu_jietu(xC2,yC2-10,xC2+6,yC2,'c2')
        
        
        a1 = matchImg(pic_test,'a1.jpg',0.92)
        b1 = matchImg(pic_test,'b1.jpg',0.92)
        c1 = matchImg(pic_test,'c1.jpg',0.92)
        a2 = matchImg(pic_test,'a2.jpg',0.92)
        b2 = matchImg(pic_test,'b2.jpg',0.92)
        c2 = matchImg(pic_test,'c2.jpg',0.92)
        
        # print("******************")
        # print("a1: " + str(a1))
        # print("b1: " + str(b1))
        # print("c1: " + str(c1))
        # print("a2: " + str(a2))
        # print("b2: " + str(b2))
        # print("c2: " + str(c2))
        # print("******************")


        
        # 设置两个标志位,确认1和2默认初始值是否正确,如果正确,则代码会把这两个标志位设为0,最后3和4交换位置.
        one_flag = 1
        two_flag=1
        
        one_is_two = 0
        
        if a1[0]> 0:
            if b1[0]>0:
                if c1[0]>0:
                    print("1是一号位,不处理")
                    #1是一号位,不处理
                    one_flag = 0
                    pass
                else:
                    #1是二号位,先处理2,再来处理1,放到下面2号位处理逻辑里去处理, 这里设置标记
                    print("是二号位,先处理2,再来处理1")
                    one_is_two = 1
            else:
                print("1是三号位, 1和3互换")
                # 1是三号位, 1和3互换
                d.click(x1- num_r(),y1- num_r())
                sleep(1)
                d.click(x3- num_r(),y3- num_r()) 
        else:
            print("1是四号位, 1和4互换")
            # 1是四号位, 1和4互换
            d.click(x1- num_r(),y1- num_r())
            sleep(1)
            d.click(x4- num_r(),y4- num_r())

        
        
        # print("处理2")
        sleep(3)
        # print(a2)
        if a2[0]> 0:
            if b2[0]>0:
                if c2[0]>0:
                    print("2是一号位.")
                    # 2是一号位.
                    d.click(x2- num_r(),y2- num_r())
                    sleep(1)
                    d.click(x1- num_r(),y1- num_r())  
                    #^ 2和1交换一次后,必须把1是二号位的标志清0,防止最后又交换一次.
                    one_is_two = 0 
                else:
                    print("2是二号位,不处理")
                    # 2是二号位,不处理
                    two_flag = 0
                    pass
            else:
                print("2是三号位, 2和3互换")
                # 2是三号位, 2和3互换
                d.click(x2- num_r(),y2- num_r())
                sleep(1)
                d.click(x3- num_r(),y3- num_r()) 
        else:
            print("2是四号位, 2和4互换")
            # 2是四号位, 2和4互换
            d.click(x4- num_r(),y4- num_r())
            sleep(1)
            d.click(x2- num_r(),y2- num_r())

        
        # 如果1是二号位,则在最后把1和2互换.    
        if one_is_two == 0:
            # print(one_is_two)
            pass
        else:
            sleep(2)
            d.click(x1- num_r(),y1- num_r())
            sleep(1)
            d.click(x2- num_r(),y2- num_r()) 
            
        sleep(1)
        
        # # 如果1是一号位,2是二号位,则3和4交换一次
        # if  one_flag == 0 and  two_flag== 0:
        #     d.click(x3,y3)
        #     sleep(1)
        #     d.click(x4,y4) 
        
        # d.click(x3,y3)
        # sleep(1)
        # d.click(x4,y4)
        
        #^ 执行完一次拼图后,如果仍然在拼图界面,则再次进行拼图
        sleep(1)
        jiepin()
        pintu = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')
        
        if pintu[0]>0:
            flag = 1
            print("仍然需要再次拼图")
        else:
            flag = 0
        
    
    

def send_message():
    # cmd = 'display notification \"' + \
    # "Notificaton memo" + '\" with title \"手动处理\"'
    cmd = 'display notification \"' + \
    "Notificaton memo" + '\" with title \"手动处理\"'
    call(["osascript", "-e", cmd])        
        

    
# jiepin()

# find_gui('kulou')

def zhuagui_liucheng():
    print("进入抓鬼流程")
    while 1>0:
        jiepin()
        sleep(1)
        res = isFight_once()
        # res = 1
        if res < 0:
            sleep(5)
        # else:
        #     zhaogui()
    
# jiepin()



def zhuagui_finish():
    
    # click_zhuagui()
    # sleep(2)
    # 创建两个线程
    try:
        _thread.start_new_thread( click_all_button,() )
        # _thread.start_new_thread( zhuagui_liucheng,())
    except:
        print ("Error: 无法启动线程")

    while 1:
        pass



def shimen_click_all_button(): #右下角继续任务的按钮,可以放个线程一直点击
    print("开始点击右下角")
    while 1> 0:

        jiepin()
        
        # kaishi = matchImg('home.jpg','./main_pic/wenzi_kaishi.jpg')
        
        # chufa = matchImg('home.jpg','./main_pic/wenzi_chufa.jpg')

        zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
        
        pintu = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')

        xunwu = matchImg('home.jpg','./new_gui_pic/wenzi_xunwu.jpg') 
        
        finish = matchImg('home.jpg','./main_pic/shimen_finish.jpg') 
        
        
        isfight = 0
        
        if zhandou[0] > 0:
            #在fighting, 循环判断fighting是否结束
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('fighting中')
                else:
                    isfight = 0
                    print('fighting结束')
        elif pintu[0]>0:
            print("是拼图")
            sigongge()
            # send_message()
        elif xunwu[0]>0:
            # send_message()
            send_message_to_slack('寻物')
        elif finish[0]>0:
            # send_message()
            tuichu()
            sleep(random_num(2))
            d.click(1450,640) # 切换角色
            send_message_to_slack('师m结束')
            sys.exit()
            
            
        
        # if kaishi[0]>0:
        #     zhaogui()
        #     # d.click(kaishi[0],kaishi[1])
        # elif chufa[0] > 0:
        #     d.click(chufa[0],chufa[1])
        # elif zhandou[0] > 0:
        #     #在fighting, 循环判断fighting是否结束
        #     isfight = 1
        #     while isfight > 0:
        #         jiepin()
        #         sleep(0.5)
        #         zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
        #         if zhandou[0] > 0:
        #             isfight = 1
        #             print('fighting中')
        #         else:
        #             isfight = 0
        #             print('fighting结束')
        # elif pintu[0]>0:
        #     print("是拼图")
        #     sigongge()
        #     send_message()
          
        click_youxiajiao() 
        sleep(1) 
        click_youxiajiao()
        
    

def shimen_finish():
    
    # click_shimen()
    # sleep(2)
    # 创建两个线程
    try:
        _thread.start_new_thread( click_all_button_simen,() )
        _thread.start_new_thread( shimen_liucheng,())
    except:
        print ("Error: 无法启动线程")

    while 1:
        pass
    
# click_all_button()
# jiepin()


#^ 判断如果是寻物任务,则弹出提示,手工执行
def shimen_isFindsomething():
    res = matchImg('home.jpg','wenzi_xunwu.jpg')
    fuhuoyao = matchImg('home.jpg','./shimen_wupin/wenzi_fuhuoyao.jpg') 
    nvyi = matchImg('home.jpg','./shimen_wupin/wenzi_nvyi.jpg') 
    
    if res[0]==0:
        #不是寻物任务
        pass
    elif fuhuoyao[0]>0:
        
        shimen_fuhuoyao()
    elif nvyi[0]>0:
        
        shimen_nvyi()
    else:
        #是寻物任务
        # send_message()
        send_message_to_slack('寻物')
        
        sleep(10)
        return 1
    
def shimen_liucheng():
    
    while 1> 0:
        
        shimen_isFindsomething()
    
        nn = isPintu()
        if nn == -1:
            print("是拼图")
            flag = 1
            # pintu()
            sigongge()
   
def fengyao():  
    finish_flag = 1
    while finish_flag > 0:
        jiepin()
        sleep(1)

        finish = matchImg('home.jpg','./main_pic/fengyao_finish.jpg',0.98)
        print(finish)
        if finish[0]>0:
            finish_flag = 0
            # send_message()
            send_message_to_slack('封妖结束')
            tuichu()
        else:
            finish_flag = 1
            weizhi = [(919,1169),(234,1177),(535,1176),(919,1169)]
            xy = weizhi[random_num(3)]
            
            # x1 = 234 - 2* num_r()
            # y1 = 1177- 2* num_r()
            x1 = xy[0] - num_r()
            y1 = xy[1] - num_r()
            d.click(x1 , y1)
            sleep(20-num_r())
            
def tuichu():
    sleep(1)
    new_sleep()
    # 点击'更多'
    quyu_click(949,2175,1010,2211)
    # d.click(984,2205)
    sleep(1)
    new_sleep()
    
    # 点击 '系统'
    quyu_click(962,2003,1009,2058)
    # d.click(978,2053)
    sleep(1)
    new_sleep()
    
    # 点击'账号管理'
    quyu_click(813,1097,940,1242)
    # d.click(855,1162)
    sleep(1)
    new_sleep()
    
    # 点击 '切换角色'
    quyu_click(249,1392,496,1432)
    # d.click(356,1404)
    sleep(1)
    new_sleep()
    
    # 点击 '确定'
    quyu_click(679,1215,820,1254)
    # d.click(733,1270)
    sleep(1)
    new_sleep()

def denglu():
    # 选择账号后,点击'口袋'两个字
    xx = random.sample(range(2179,2265),1)
    yy= random.sample(range(605,679),1)
    
    # xx = 2265
    # yy = 679
    d.click(xx[0],yy[0])
    

    
    new_sleep()
    sleep(1)
    
    # 确认进入口袋版
    xx = random.sample(range(1352,1520),1)
    yy= random.sample(range(658,705),1)
    d.click(xx[0],yy[0])
    
    new_sleep()
    sleep(2)
    
    

def fengyao_all(): 
    
    # 2179 < x < 2265
    # 605< y < 679 
    
    denglu()
    
    n1=(1209,467)
    n2 = (1701,437)
    n3 = (1243,847)
    n4 = (1719,775)
    
    
    xx = random.sample(range(632 ,674),1)
    yy= random.sample(range(262,332),1)
     
     
    sleep(random_num(2))
    d.click(xx[0],yy[0]) # 点击上方活动选项图标
    sleep(random_num(2)+1)
    # d.click(627,545)# 点击 封妖
    quyu_click(702,517,761,578)

    sleep(random_num(2))
    
    
    
    
    finish_flag = 1
    while finish_flag > 0:
        jiepin()
        sleep(1)

        finish = matchImg('home.jpg','./main_pic/fengyao_finish.jpg',0.98)
        print(finish)
        if finish[0]>0:
            finish_flag = 0
            # send_message()
            
            tuichu()
            sleep(random_num(2))
            # 切换角色
            quyu_click(1567,606,1586,623)
            
            # d.click(1450,640) 
            send_message_to_slack('封妖结束')
            
        else:
            finish_flag = 1
            quyu_click(119,1098,981,1275)
            # weizhi = [(919,1169),(234,1177),(535,1176),(919,1169)]
            # xy = weizhi[random_num(3)]
            
            # x1 = 234 - 2* num_r()
            # y1 = 1177- 2* num_r()
            # x1 = xy[0] - num_r()
            # y1 = xy[1] - num_r()
            # d.click(x1 , y1)
            sleep(10-num_r())    

    
# shimen_liucheng()

# shimen_finish()
# pintu()

# zhuagui_finish()
# sys.exit()

# fengyao()

# jiepin()   
# click_youxiajiao() 
# yegui = matchImg('home.jpg','youxiajiao_chufa.jpg',0.3) 
# yegui = matchImg('home.jpg','./gui_pic/wenzi_kulouguai.jpg',0.3) 
# yegui = matchImg('home.jpg','new_kulouguai.jpg',0.3) 
#!----------------------------2021.01.28真机---------↓↓↓↓↓
# jiepin()  
# qianwang = matchImg('home.jpg','./main_pic/wenzi_xunwu.jpg') 
# qianwang = matchImg('home.jpg','./main_pic/youxiajiao_qianwan.jpg')
# if qianwang[0]>0:
#     d.click(qianwang[0],qianwang[1])

# zhuagui_finish()

# def click_kaishi():
#     d.click(520,1420)
    
    # 968
    # 1718
 
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
    sell_hulu_zhuagui()
    
