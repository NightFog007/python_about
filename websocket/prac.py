#引入websocket的create_connection类
from websocket import create_connection

# 建立和WebSocket接口的链接
ws = create_connection("ws://echo.websocket.org")

print("发送 'Hello World' ")
# 发送Hello，World
ws.send("Hello World")

# 将WebSocket的返回值存储result变量
result = ws.recv()

# 打印返回的result
print("返回" + result)

# 关闭WebSocket链接
ws.close()