import sys
import time 

from time import sleep
from tqdm import tqdm
from progress.bar import IncrementalBar
from alive_progress import alive_bar
import PySimpleGUI as sg

# 各种进度条代码

def progress_bar():
    for i in range(1,101):
        print("\r",end="")
        print("Download progress:{}%: ".format(i),"▋" * (i//2),end="")
        sys.stdout.flush()
        time.sleep(0.05)

# progress_bar()


def time_progress():
    scale = 50
    print("执行开始，祈祷不报错".center(scale // 2,"-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = "*" * i
        b = "." * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
        time.sleep(0.1)
    print("\n"+"执行结束，万幸".center(scale // 2,"-"))

# time_progress()

def tpdm_progress():
    # 这里同样的，tqdm就是这个进度条最常用的一个方法
    # 里面存一个可迭代对象
    for i in tqdm(range(1, 500)):
        # 模拟你的任务
        sleep(0.01)

    sleep(0.5)

# tpdm_progress()


def incre_progress():
    mylist = [1,2,3,4,5,6,7,8]
    bar = IncrementalBar('Countdown', max = len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
        bar.finish()

# incre_progress()


def alive_progress():
    items = range(100)                  # retrieve your set of items
    with alive_bar(len(items)) as bar:   # declare your expected total
        for item in items:               # iterate as usual
            # process each item
            bar()
            time.sleep(0.1)

# alive_progress()


def gui_progress():
    mylist = [1,2,3,4,5,6,7,8]
    for i, item in enumerate(mylist):
        sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
        time.sleep(1)

# gui_progress()