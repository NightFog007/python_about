import os
import uiautomator2 as u2
import time
import adbutils
import websocket



def jiepin():
    # d = adbutils.adb.device('18bcc735')  # 小米10青春版
    d = adbutils.adb.device('DLQ0216505001224')   # 华为

    lport = d.forward_port(7912 )
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:{}/minicap".format(lport))

    index = 0
    # start = time.time()
    while True:
        data = ws.recv()
        if not isinstance(data, (bytes, bytearray)):
            print(data)
            continue
        with open("home.jpg" , "wb") as f:
            f.write(data)
            index += 1
        print(index)
        if index > 0:
            break

    # duration = time.time() - start
    # print("Image per second: %.2f" % (100/duration))
    ws.close()