#!/usr/bin/env python
# -*- coding: utf-8 -*-


# __instruction__='ws的例子'

from common import Common
# 建立和WebSocket接口的链接
con = Common('ws://echo.websocket.org','ws')
# 获取返回结果
result = con.send('Hello, World...')
#打印日志
print(result)
#释放WebSocket的长连接
del con