import os
import random
import re
import sys
import time

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

import adbutils
import aircv as ac
import websocket

""" 你的APPID AK SK """
APP_ID = '17235153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

flag = 0

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
    x = 425
    y = 1132
    d.click(x,y)   
    
def click_shimen_renwu():
    x = 773
    y = 1248
    d.click(x,y)   
    sleep(0.2)
    x = 773
    y = 1248
    d.click(x,y)

def click_zhidaole():
    x = 773
    y = 1248
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
    x = 953
    y = 1703
    d.click(x,y)
    d.click(x,y)
    d.click(x,y)
    d.click(x,y)
    sleep(2)
    
def zhuagui_click_all_button(): #右下角继续任务的按钮,可以放个线程一直点击
    print("开始点击右下角")
    while 1> 0:
        # finish_flag = matchImg('home.jpg','renwu_jieshu.jpg')
        
        # wancheng = matchImg('home.jpg','huluman.jpg')
        # # print(wancheng)
        # if wancheng[0] > 0:
        #     d.click(627,1208)
        #     sleep(1)
        jiepin()
        
        kaishi = matchImg('home.jpg','./main_pic/wenzi_kaishi.jpg')
        
        chufa = matchImg('home.jpg','./main_pic/wenzi_chufa.jpg')

        zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
        
        pintu = matchImg('home.jpg','./main_pic/pintu_jiemian.jpg')

        
        isfight = 0
        
        if kaishi[0]>0:
            zhaogui()
            # d.click(kaishi[0],kaishi[1])
        elif chufa[0] > 0:
            d.click(chufa[0],chufa[1])
        elif zhandou[0] > 0:
            #在战斗, 循环判断战斗是否结束
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('战斗中')
                else:
                    isfight = 0
                    print('战斗结束')
        elif pintu[0]>0:
            print("是拼图")
            sigongge()
            # send_message()
          
        click_youxiajiao() 
        sleep(1) 
        click_youxiajiao()
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
    sleep(1)
    x = 600
    y = 1411
    d.click(x,y)
    
    
      
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


def find_jiu():
    
    x = -1
    
    while x < 0:
    
        jiepin()
        
        # sttr = ['you','shang','xia','zuo']
        jiu_name = ['hugu_shang.jpg','hugu_xia.jpg','hugu_you.jpg','hugu_zuo.jpg','meihua_shang.jpg','meihua_xia.jpg','meihua_you.jpg','meihua_zuo.jpg','shedan_shang.jpg','shedan_you.jpg','shedan_zuo.jpg','zhenlu_shang.jpg','zhenlu_xia.jpg','zhenlu_you.jpg','zhenlu_zuo.jpg']
        # name = 'mamian'
        for i in jiu_name:
            gui_pic = './jiu_pic/{}'.format(i)
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
    
    
    xunwu = matchImg('home.jpg','./new_gui_pic/wenzi_xunwu.jpg') 

    if jiangshi[0] > 0 :
        click_kaishi()
        sleep(1)
        find_gui('jiangshi')
    elif niutou[0] > 0:
        click_kaishi()
        sleep(1)
        print("找牛头")
        find_gui('niutou')
    elif mamian[0] > 0:
        click_kaishi()
        sleep(1)
        find_gui('mamian')
    elif yegui[0] > 0:
        click_kaishi()
        sleep(1)
        find_gui('yegui')
    elif kulouguai[0] > 0:
        click_kaishi()
        sleep(1)
        find_gui('kulouguai')
    # elif paojiu[0]>0:
    #     find_jiu()
    # elif  pintu[0]>0:
    #     print("是拼图")
    #     sigongge()
        
    elif xunwu[0] > 0:
    # else:
        send_message()
    
    
        
        
    
    
    
    
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



def isFight_once():  #战斗中,返回-1
    res = 0
    xx = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
    if xx[0]> 0 and xx[1] > 0:
        print("战斗中")
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
    
    xA1 = 125
    yA1 = 900

    xB1=  532
    yB1= 900

    xC1 = 125  
    yC1 = 1307

    # xD1 = 4 
    # yD1=805

    xA2 = 556 
    yA2 = 900

    xB2 = 951 
    yB2 = 900
    
    xC2 = 553   
    yC2 = 1307
    
    # xD2= 800  
    # yD2=805
    
    pic_test = './main_pic/pintu_beijing.jpg'
    jiepin()
    
    quyu_jietu(xA1,yA1,xA1+10,yA1+10,'a1')
    quyu_jietu(xB1-10,yB1,xB1,yB1+10,'b1')
    quyu_jietu(xC1,yC1-10,xC1+10,yC1,'c1')
    # quyu_jietu(xD1,yD1,xD1-10,yD1-10,'d1')
    quyu_jietu(xA2,yA2,xA2+10,yA2+10,'a2')
    quyu_jietu(xB2-10,yB2,xB2,yB2+10,'b2')
    quyu_jietu(xC2,yC2-10,xC2+10,yC2,'c2')
    # quyu_jietu(xD2,yD2,xD2-10,yD2-10,'d2')
    a1 = matchImg(pic_test,'a1.jpg',0.9)
    b1 = matchImg(pic_test,'b1.jpg',0.9)
    c1 = matchImg(pic_test,'c1.jpg',0.9)
    a2 = matchImg(pic_test,'a2.jpg',0.9)
    b2 = matchImg(pic_test,'b2.jpg',0.9)
    c2 = matchImg(pic_test,'c2.jpg',0.9)
    
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
            d.click(x1,y1)
            sleep(1)
            d.click(x3,y3) 
    else:
        print("1是四号位, 1和4互换")
        # 1是四号位, 1和4互换
        d.click(x1,y1)
        sleep(1)
        d.click(x4,y4)

    
    
    # print("处理2")
    sleep(3)
    # print(a2)
    if a2[0]> 0:
        if b2[0]>0:
            if c2[0]>0:
                print("2是一号位.")
                # 2是一号位.
                d.click(x2,y2)
                sleep(1)
                d.click(x1,y1)  
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
            d.click(x2,y2)
            sleep(1)
            d.click(x3,y3) 
    else:
        print("2是四号位, 2和4互换")
        # 2是四号位, 2和4互换
        d.click(x4,y4)
        sleep(1)
        d.click(x2,y2)

    
    # 如果1是二号位,则在最后把1和2互换.    
    if one_is_two == 0:
        # print(one_is_two)
        pass
    else:
        sleep(2)
        d.click(x1,y1)
        sleep(1)
        d.click(x2,y2) 
        
    sleep(3)
    
    # 如果1是一号位,2是二号位,则3和4交换一次
    if  one_flag == 0 and  two_flag== 0:
        d.click(x3,y3)
        sleep(1)
        d.click(x4,y4) 
    

def send_message():
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
        
        isfight = 0
        
        if zhandou[0] > 0:
            #在战斗, 循环判断战斗是否结束
            isfight = 1
            while isfight > 0:
                jiepin()
                sleep(0.5)
                zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
                if zhandou[0] > 0:
                    isfight = 1
                    print('战斗中')
                else:
                    isfight = 0
                    print('战斗结束')
        elif pintu[0]>0:
            print("是拼图")
            sigongge()
            # send_message()
        elif xunwu[0]>0:
            send_message()
            
            
        
        # if kaishi[0]>0:
        #     zhaogui()
        #     # d.click(kaishi[0],kaishi[1])
        # elif chufa[0] > 0:
        #     d.click(chufa[0],chufa[1])
        # elif zhandou[0] > 0:
        #     #在战斗, 循环判断战斗是否结束
        #     isfight = 1
        #     while isfight > 0:
        #         jiepin()
        #         sleep(0.5)
        #         zhandou = matchImg('home.jpg','./main_pic/wenzi_huihe.jpg')
        #         if zhandou[0] > 0:
        #             isfight = 1
        #             print('战斗中')
        #         else:
        #             isfight = 0
        #             print('战斗结束')
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
    if res[0]==0:
        #不是寻物任务
        pass
    else:
        #是寻物任务
        send_message()
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
    while 1>0:       
        d.click(234 , 1177)
        sleep(10)
    
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
    fengyao()