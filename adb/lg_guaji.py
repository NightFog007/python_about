import uiautomator2 as u2
from PIL import Image
import os
import time 
import random
import re
import numpy as np
from cv2 import cv2 
from aip import AipOcr

from fast_screenshot import jiepin

from time import sleep 
# from comm import isMove,isMove_once,isFight_once,get_random_num,get_09,open_ditu

import aircv as ac



# d = u2.connect_wifi('192.168.205.180')
# d = u2.connect_adb_wifi("10.0.0.1:5555")

d = u2.connect_usb('113038e8')

# start()  

while 1>0:
    
    d.click(340,1024)
    sleep(3)
    d.click(340,1024)
    sleep(5)
    d.click(340,1024)
    sleep(180)        

        




