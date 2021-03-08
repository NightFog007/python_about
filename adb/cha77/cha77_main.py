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
# from fast_screenshot import jiepin

from time import sleep 
# from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu,quyu_jietu

import aircv as ac



# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

d = u2.connect_usb('113038e8') # 小米mix3

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
                
                
        # jiepin()
        zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
        if zhandou[0]>0:
        # if panduan1 ==0 :
        
        # isfight = 0 
        # if zhandou[0]>0:
            print("战斗中")
            isfight = 1
            while isfight > 0:
                # jiepin()
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



def open_changan7():
    x = 977
    y = 306
    d.click(x,y)
    d.click(x,y)
    
def go_yizhan():
    x = 973
    y = 808
    d.click(x,y)
    d.click(x,y)
    
def click_yizhan():
    x = 874
    y = 434
    d.click(x,y)
    
    x = 1050
    y  = 520
    
    883
    533
    
    1131
    438
    
    905 
    501

# 驿站老板对话框    
def go_guojing():
    x = 1609
    y = 521
    d.click(x,y)
    
def close_guojingditu():
    x = 1566
    y = 49
    d.click(x,y)    
    
def goin_difu():    
    x = 633
    y = 233
    d.click(x,y)
    
def ditu_guojing_to_difu():    
    x = 768
    y  =175
    d.click(x,y)
    
def go_zhongkui():    
    x = 888
    y = 579
    d.click(x,y)

def close_difu_ditu():
    x =     1575
    y  =130
    d.click(x,y)
    

    


def go_difu():
    x = 763
    y = 176
    d.click(x,y)
 
def click_zhongkui():
    x = 808
    y = 614
    d.click(x,y)
    
def ling_zhuagui():
    x = 1619
    y  =646
    d.click(x,y)   


def start_zhuagui():
    
    # jiepin()
    zhandou = matchImg('home.jpg','./wenzi_huihe.jpg')
    if zhandou[0]>0:
        
    # if panduan1 ==0 :
    
    # isfight = 0 
    # if zhandou[0]>0:
        print("战斗中")
        isfight = 1
        while isfight > 0:
            # jiepin()
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
    
    xiangdui_zuobiao = [(1197,395),(1116,454),(1278,425),(1292,333),(1196,344),(1197,395),(1116,454),(1278,425),(1292,333),(1196,344)]

    for i in xiangdui_zuobiao:
        
        open_daoju()  


        open_changan7() 
        sleep(1)
        go_yizhan() 
        sleep(0.8)
        close_daoju()
        sleep(2)

  
        d.click(i[0],i[1])
        sleep(1)
        
        jiepin2()
        sleep(1)
        yy = matchImg('home.jpg','queren_flag.jpg')
        if yy[0] > 0:
            sleep(1)
            d.click(yy[0],yy[1])
            print("找到了")
            break





    sleep(2)
    open_ditu()
    time.sleep(1)
    ditu_guojing_to_difu()
    sleep(1)
    close_guojingditu()
    sleep(20)
    goin_difu()
    sleep(5)
    open_ditu()
    sleep(1)
    go_zhongkui()
    sleep(1)
    close_difu_ditu()
    sleep(22)
    click_zhongkui()
    sleep(2)
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

xianling_jia=(2280,816)

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


# start_zhuagui()
# jiepin2()


def open_daoju():
    x = 2129
    y = 1047
    d.click(x,y)
    
def close_daoju():    
    x = 1799
    y = 104
    d.click(x,y)

def open_fashu():
    x = 2010
    y = 1022
    d.click(x,y)

def open_xianling():
    x = 1991
    y = 878
    d.click(x,y)    
    
    
def mai77(i=19):
    

    
    
    x = 2077  # 点中紫色77
    y = 202
    
    x = 1695  # 红色77
    y = 335
    d.click(x,y)   
    
    sleep(0.6)
    if i == 19:  # 买19个77
        
        x = 2198  # 点击数量框
        y = 810
        d.click(x,y)  
        
        sleep(0.6)
        x = 2076 # 点击 数字 9
        y = 667
        d.click(x,y)  
        
        sleep(0.5)
        x = 2220 # 点击确定按钮
        y = 677
        d.click(x,y)
    else:
        for x in range(1,i):
            d.click(xianling_jia[0],xianling_jia[1])
            sleep(0.2)
        

    
    sleep(0.8)
    x = 2138 # 点购买按钮
    y = 948
    d.click(x,y)
    
    sleep(1)
    x = 2282 # 关闭仙灵
    y = 86
    d.click(x,y)
    
    


def cha7():
    weizhi_18ge77=[(1438,343),(1573,343),(1686,343),
    (1179,466),(1306,466),(1438,466),(1573,466),(1686,466),
    (1179,602),(1306,602),(1438,602),(1573,602),(1686,602),
    (1179,720),(1306,720),(1438,720),(1573,720),(1686,720),]
    
    for i in weizhi_18ge77:
        d.click(i[0],i[1])
        d.click(i[0],i[1])
        sleep(0.2)
  
# 点击背包的第二个位置(FF)        
def click_ff():
    x = 1306
    y =  343
    d.click(x,y)
    d.click(x,y)
    
# 飞到宝象国FF    
def fly_baoxiang():
    open_daoju()
    sleep(0.3)
    
    click_ff()
    
    sleep(1)
    x = 964
    y =  584
    d.click(x,y)
    
    close_daoju()
    
def open_cangku():
    x = 983
    y = 390
    d.click(x,y)
    sleep(1)
    x = 2054
    y = 677
    d.click(x,y)
    
def close_cangku():    
    x = 1800
    y = 106
    d.click(x,y)



cangkujiemian_beibao=[
        (1500,400),(1600,400),(1730,400),
        (1230,500),(1362,500),(1500,500),(1600,500),(1730,500),
        (1230,625),(1362,625),(1500,625),(1600,625),(1730,625),
        (1230,760),(1362,760),(1500,760),(1600,760),(1730,760),
        ]   
        
def baocun77(name='huodong'):
    
    # if name == 'huodong':
    #     cangkujiemian_beibao=[
    #     (1500,400),(1600,400),(1730,400),
    #     (1230,500),(1362,500),(1500,500),(1600,500),(1730,500),
    #     (1230,625),(1362,625),(1500,625),(1600,625),(1730,625),
    #     (1230,760),(1362,760),(1500,760),(1600,760),(1730,760),
    #     ] 
    # elif name == 'no_huodong':  # 非活动7,默认一次只做6个
    #     cangkujiemian_beibao=[
    #     (1500,400),(1600,400),(1730,400),
    #     (1230,500),(1362,500),(1500,500)
    #     ]
    # else:
    #     pass
    
    for i in cangkujiemian_beibao:
        d.click(i[0],i[1])
        d.click(i[0],i[1])
        sleep(0.5)

# 点击一次,切换到下一个仓库
def change_cangku():
    x =  777
    y = 925
    d.click(x,y)


# 点击背包的第一个位置(放飞行7)
def open_feixing7():
    x =  1194
    y = 334
    d.click(x,y)
    d.click(x,y)
    
def click_77_huanggong():
    x = 770
    y = 336
    d.click(x,y)

def click_77_huodongNPC():
    x = 1096
    y = 617
    d.click(x,y)    


def click_77_qinqiong():
    x = 716
    y = 711
    d.click(x,y)       
    
def click_77_chengyaojin():
    x = 1253
    y = 233
    d.click(x,y)   
    d.click(x,y)
    
def click_77_hs():
    x = 1753
    y = 230
    d.click(x,y)
    
def click_77_shudian():
    x = 1763
    y = 740
    d.click(x,y)
    
    
# wangfuren
def click_77_wangdashao():
    x = 1460
    y = 799
    d.click(x,y)   
 
 
def click_77_shuang():
    x = 968
    y = 462
    d.click(x,y) 
    
def click_77_jiudian():
    x = 1628
    y = 485
    d.click(x,y) 
    
def click_77_fangwu():
    x = 1774
    y = 587
    d.click(x,y) 
    
def click_77_yizhan():
    x = 1173
    y = 802
    d.click(x,y) 
    
def click_77_shanghui():
    x = 1305
    y = 856
    d.click(x,y) 
    
def click_77_yewai():
    x = 1814
    y = 886
    d.click(x,y) 
    
def click_77_guojing():
    x = 530
    y = 896
    d.click(x,y)  
    
def click_cs_1():
    x = 1296
    y = 223
    d.click(x,y) 
    
def click_cs_2():
    x = 982
    y = 314
    d.click(x,y) 
    
def click_cs_3():
    x = 1101
    y = 461
    d.click(x,y) 
    
def click_cs_4():
    x = 988
    y = 564
    d.click(x,y) 
    
def click_cs_5():
    x = 1327
    y = 541
    d.click(x,y) 
    
def click_cs_6():
    x = 966
    y = 794
    d.click(x,y) 
    
def click_cs_7():
    x = 1381
    y = 896
    d.click(x,y) 

def click_al_1():
    x = 709
    y = 279
    d.click(x,y) 
    
def click_al_2():
    x = 791
    y = 488
    d.click(x,y) 
    
def click_al_3():
    x = 883
    y = 779
    d.click(x,y) 
    
def click_al_4():
    x = 1327
    y = 439
    d.click(x,y) 
    
def click_al_5():
    x = 1650
    y = 261
    d.click(x,y) 
    
def click_al_6():
    x = 1532
    y = 558
    d.click(x,y) 
    
def click_al_7():
    x = 1429
    y = 816
    d.click(x,y) 
    
# 五彩旗盒点击'使用'按钮后,不同场景,选择不同颜色的77
# 长安活动=蓝色,默认值
# 长安抓鬼=红色
# 长寿=绿色
# 傲来=黄色
# 朱紫= 白色
def color_77(color):
    #点击颜色列表
    x=1017
    y=960
    d.click(x,y)
    sleep(0.2)
    
    green_zuobiao = (986,585)
    red_zuobiao = (986,686)
    yellow_zuobiao = (986,785)
    white_zuobiao = (986,881)
    
    if color == 'green':
        d.click(green_zuobiao[0],green_zuobiao[1])
    elif color == 'red':
        d.click(red_zuobiao[0],red_zuobiao[1])
    elif color == 'yellow':
        d.click(yellow_zuobiao[0],yellow_zuobiao[1])
    elif color == 'white':
        d.click(white_zuobiao[0],white_zuobiao[1])
    
    
 
'''
1. 打开背包   111
2. 飞到点位1  
3. 打开法术栏 111
4. 点击仙灵  11111
5. 买19个77  111 
6. 关闭仙灵   111
7. 双击19个77的位置  111
8. 飞到宝象国ff 111 
9. 打开仓库 11 
10. 19个位置,放入仓库1 1111
11. 打开背包 111
12. 飞到点位2 111
13. 打开法术栏 
14. 点击仙灵
15. 买19个77
16. 关闭仙灵
17. 双击19个77的位置
18. 飞到宝象国ff
19. 打开仓库
'''

def make_77(name):
    
    
        
    
    #~ 从1开始  
    for n in range(1,8):
    # for n in range(4,5):
    
        open_daoju()
        sleep(0.5)
        
        open_feixing7()
        sleep(0.6)
        
        
        if n == 1:
            if name == 'cs':
                click_cs_1()
            elif name == 'al':
                click_al_1()
            else:
                click_77_shuang()
        elif n == 2:
            if name == 'cs':
                click_cs_2()
            elif name == 'al':
                click_al_2()
            else:
                click_77_jiudian()
        elif n == 3:
            if name == 'cs':
                click_cs_3()
            elif name == 'al':
                click_al_3()
            else:            
                click_77_fangwu()
        elif n == 4:
            if name == 'cs':
                click_cs_4()
            elif name == 'al':
                click_al_4()
            else:            
                click_77_yizhan()
        elif n == 5:
            if name == 'cs':
                click_cs_5()
            elif name == 'al':
                click_al_5()
            else:            
                click_77_shanghui()
        elif n == 6:
            if name == 'cs':
                click_cs_6()
            elif name == 'al':
                click_al_6()
            else:            
                click_77_yewai()
        elif n == 7:
            if name == 'cs':
                click_cs_7()
            elif name == 'al':
                click_al_7()
            else:            
                click_77_guojing()
        else:
            return 0 
        
        # click_77_shudian()    
            
            
        sleep(1)
        
        close_daoju()
        sleep(1)
        open_fashu()
        sleep(0.8)
        open_xianling()
        
        sleep(0.8)
        mai77(19)
        
        open_daoju()
        sleep(0.8)
        cha7()
        sleep(1)
        close_daoju()
        sleep(1)
        fly_baoxiang()
        sleep(2)
        
        open_cangku()
        sleep(1)
        
        # n = 7
        for i in range(1,n):
            change_cangku()
            sleep(1)
        
        # 把77存入仓库
        sleep(1)
        baocun77('huodong')
        
        sleep(1)
        close_cangku()
        sleep(3)

def make_CA77(xx):
    # for n in range(2,8):
    for n in range(1,8):
    
        open_daoju()
        sleep(0.5)
        
        open_feixing7()
        sleep(0.6)
        
        # n = 6
        if n == 1:
            click_77_shuang()
        elif n == 2:
            click_77_jiudian()
        elif n == 3:
            click_77_fangwu()
        elif n == 4:
            click_77_yizhan()
        elif n == 5:
            click_77_shanghui()
        elif n == 6:
            click_77_yewai()
        elif n == 7:
            click_77_guojing()
        else:
            return 0 
        
        # click_77_shudian()    
            
            
        sleep(1)
        
        close_daoju()
        sleep(1)
        open_fashu()
        sleep(0.8)
        open_xianling()
        
        sleep(0.8)
        mai77(xx)
        
        open_daoju()
        sleep(0.8)
        cha7()
        sleep(0.5)
        close_daoju()
        
        fly_baoxiang()
        sleep(1)
        
        open_cangku()
        sleep(1)
        
        # n = 7
        for i in range(1,n):
            change_cangku()
            sleep(0.5)
        
        # 把77存入仓库
        sleep(1)
        baocun77()
        
        sleep(1)
        close_cangku()
        sleep(3)
    

def make_huodong77():
    for n in range(1,8):
    # for n in range(4,8):
        open_daoju()
        sleep(0.5)
        
        open_feixing7()
        sleep(0.6)
        
        # n = 4
        if n == 1:
            click_77_huanggong()
        elif n == 2:
            click_77_huodongNPC()
        elif n == 3:
            click_77_qinqiong()
        elif n == 4:
            click_77_chengyaojin()
        elif n == 5:
            click_77_wangdashao()
        elif n == 6:
            click_77_shudian()
        elif n == 7:
            click_77_hs()
        else:
            return 0 
        
        # click_77_shudian()    
            
            
        sleep(1)
        
        close_daoju()
        sleep(1)
        open_fashu()
        sleep(0.8)
        open_xianling()
        
        sleep(0.8)
        mai77()
        
        open_daoju()
        sleep(0.8)
        cha7()
        sleep(0.5)
        close_daoju()
        
        fly_baoxiang()
        sleep(1)
        
        open_cangku()
        sleep(1)
        
        # n = 7
        for i in range(1,n):
            change_cangku()
            sleep(0.5)
        
        # 把77存入仓库
        sleep(1)
        baocun77('huodong')
        
        sleep(1)
        close_cangku()
        sleep(3)
        
        
# make_huodong77()        
        
cangkujiemian_cangku=[
        (500,400),(628,400),(756,400),(892,400),(1011,400),
        (500,500),(628,500),(756,500),(892,500),(1011,500),
        (500,625),(628,625),(756,625),(892,625),(1011,625),
        (500,760),(628,760),(756,760)
    ]

# 参数k, 分别为0,1,2,3,4,5,6,7,8
def get_77_to_body(k):
    #点击仓库管理员
    
    #各自拿出仓库1-7的两个77
    
    for n in range(0,7):
            
        for i in range(k*2,(k+1)*2):
            d.click(cangkujiemian_cangku[i][0],cangkujiemian_cangku[i][1])
            d.click(cangkujiemian_cangku[i][0],cangkujiemian_cangku[i][1])
            sleep(0.6)
            
        change_cangku()            
        sleep(1)
        

# get_77_to_body()

def open_fabaolan():
    open_daoju()
    sleep(0.5)
    x = 645
    y  = 933
    d.click(x,y)
    
def close_fabao():
    x = 1794
    y = 120
    d.click(x,y)    

# 使用五彩旗盒,先把五彩旗盒装备在身上第一个位置
def open_qihe(name_77):        
    
    # 点击五彩旗盒
    x = 541
    y = 314
    d.click(x,y)

    # 点击'使用'按钮
    x = 590
    y = 790    
    d.click(x,y)
    
    hecheng7_weizhi = [
(0,0),(0,0),(1180,369),(1302,369),(1437,369),
(924,492),(1053,492),(1180,492),(1302,492),(1437,492),
(924,623),(1053,623),(1180,623),(1302,623),(1437,623),
(924,751),(1053,751),(1180,751),(1302,751),(1437,751),
        ]
    
    sleep(1)
    
    #~ 选择不同颜色
    if name_77 == 'ca':
        color_77('red')
    elif name_77 == 'cs':
        color_77('green')
    elif name_77 == 'al':
        color_77('yellow')
    elif name_77 == 'zz':
        color_77('white')
        
    sleep(1)
    
    # 每次合成两面77,位置分别是:
    one_77 = [2,4,6,8,10,12,14]
    
    for i in one_77:
        d.click(hecheng7_weizhi[i][0],hecheng7_weizhi[i][1])
        sleep(0.7)
    
    # 点击'合旗'按钮
    x = 1412
    y = 978
    d.click(x,y)
    sleep(1)
    
    # 点击'使用'按钮
    x = 590
    y = 790    
    d.click(x,y)
    sleep(1)
    

    
    two_77 = [3,5,7,9,11,13,15]
    for i in two_77:
        d.click(hecheng7_weizhi[i][0],hecheng7_weizhi[i][1])
        sleep(0.7)
    
    # 点击'合旗'按钮
    x = 1412
    y = 978
    d.click(x,y)
    
    sleep(2)
    close_fabao()
    close_fabao()
    
    # 把合成的77放入仓库
    sleep(1)
    fly_baoxiang()
    sleep(1)
    open_cangku()
    sleep(0.5)
    d.click(cangkujiemian_beibao[0][0],cangkujiemian_beibao[0][1])
    sleep(0.1)
    d.click(cangkujiemian_beibao[0][0],cangkujiemian_beibao[0][1])
    sleep(0.3)
    d.click(cangkujiemian_beibao[1][0],cangkujiemian_beibao[1][1])
    sleep(0.1)
    d.click(cangkujiemian_beibao[1][0],cangkujiemian_beibao[1][1])
    

 # 插完7个点位的77并存入仓库后,打开仓库,自动合成77,并存入第一个仓库 ,一共会合成9面77       
# def hecheng77(n=18):
def hecheng77(name_77,n=18):
    #~ 如果从仓库第一个7开始合成,i的循环要从0开始
    # for i in range(6,9):
    for i in range(0,int(n/2)):
        get_77_to_body(i)
        close_cangku()  
        sleep(1)  
        open_fabaolan()
        sleep(1)
        open_qihe(name_77)
    

action = sys.argv[1]
action2 = sys.argv[2]
action3 = sys.argv[3]


if action == 'huodong':
    make_huodong77()
# elif action == 'shimen':
#     shimen_click_all_button()
# elif action == 'fengyao':
#     fengyao()
elif action == 'ca':
    make_CA77(19)
elif action =='cs':
    make_77('cs')
elif action =='al':
    make_77('al')
elif action == 'heqi':
    name_77 = action2
    hecheng77(name_77, int(action3))
else:
    pass
    
# make_huodong77()
# sleep(2)
# open_cangku()
# sleep(2)
# hecheng77()

#! 活动7插和合成(合成旗需要打开仓库界面)
'''
python3 cha77_main.py huodong 2 2
python3 cha77_main.py  heqi huodong 18 
'''

#! 长安7插和合成(第三个参数可以忽略)
'''
python3 cha77_main.py ca 6 3
python3 cha77_main.py heqi ca 18
'''

