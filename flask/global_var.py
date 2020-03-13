
from flask import Flask, request, g, current_app ,session

from flask_restful import Resource, Api,reqparse

import requests
import json

# gevent
from gevent import monkey, sleep
from gevent.pywsgi import WSGIServer
monkey.patch_all()
# gevent end

import time

# Cache
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
# Cache End



# 请求A: post,并且产生一个变量 key
# 请求B: 需要用到请求A的变量key
# Flask的底层——Werkzeug——是有缓存支持的


	
app = Flask(__name__)

api = Api(app)


app.config.update(DEBUG=True)


# 示例1: 定义两个路由,通过cache传递数据.
@app.route('/asyn/', methods=['GET'])
def test_asyn_one():
    print("asyn has a request!")
    cache.clear()
    timeout = 30
    while (not cache.has('a')) and timeout >0:
        sleep(1)
        timeout = timeout - 1
        print('timeout:', timeout)
    print("a", cache.get('a'))
    return 'hello asyn'
 
 
@app.route('/test/', methods=['GET'])
def test():
    cache.set('a', '1')
    return 'hello test'


# 示例2: 定义flask_restful服务, 这个服务两个请求之间用cache传递数据.
class TTest(Resource):

    def post(self,todo_id):

            if todo_id is '1':
                cache.clear()
                cache.set('a','aaaaaaaaaa')
                return 1

            elif todo_id is '2':
                x = cache.get('a')
                return x



api.add_resource(TTest, '/ttest/<string:todo_id>')


if __name__ == "__main__":
    # app.run()
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
















	
