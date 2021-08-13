import hashlib
import hmac
import json
import random
import string
from functools import wraps

from flask import Flask, make_response, request

SECRET_KEY = "DebugTalk"

app = Flask(__name__)

#! 搭建接口测试服务端脚本,执行方式:
"""
1. export FLASK_ENV=development

2. export FLASK_APP=app.py

3. flask run
"""

""" storage all users' data
data structure:
    users_dict = {
        'uid1': {
            'name': 'name1',
            'password': 'pwd1'
        },
        'uid2': {
            'name': 'name2',
            'password': 'pwd2'
        }
    }
"""
users_dict = {}

""" storage all token data
data structure:
    token_dict = {
        'device_sn1': 'token1',
        'device_sn2': 'token1'
    }
"""
token_dict = {}


def gen_random_string(str_len):
    """ generate random string with specified length
    """
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))

def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign

def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


def validate_request(func):

    print("进入validate_request")

    @wraps(func)
    def wrapper(*args, **kwargs):
        device_sn = request.headers.get('device_sn', "")
        token = request.headers.get('token', "")

        if not device_sn or not token:
            result = {
                'success': False,
                'msg': "device_sn or token is null."
            }
            response = make_response(json.dumps(result), 401)
            response.headers["Content-Type"] = "application/json"
            return response

        if token_dict.get(device_sn) != token:
            result = {
                'success': False,
                'msg': "Authorization failed!"
            }
            response = make_response(json.dumps(result), 403)
            response.headers["Content-Type"] = "application/json"
            return response

        return func(*args, **kwargs)

    return wrapper


@app.route('/')
def index():
    return "Hello World!"

@app.route('/api/get-token', methods=['POST'])
def get_token():
    print("创建token")
    device_sn = request.headers.get('device_sn', "")
    os_platform = request.headers.get('os_platform', "")
    app_version = request.headers.get('app_version', "")
    data = request.get_json()
    sign = data.get('sign', "")

    expected_sign = get_sign(device_sn, os_platform, app_version)
    print(expected_sign)

    if expected_sign != sign:
        result = {
            'success': False,
            'msg': "Authorization failed!"
        }
        response = make_response(json.dumps(result), 403)
    else:
        token = gen_random_string(16)
        token_dict[device_sn] = token

        result = {
            'success': True,
            'token': token
        }
        response = make_response(json.dumps(result))

    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users')
@validate_request
def get_users():
    users_list = [user for uid, user in users_dict.items()]
    users = {
        'success': True,
        'count': len(users_list),
        'items': users_list
    }
    response = make_response(json.dumps(users))
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/reset-all')
@validate_request
def clear_users():
    users_dict.clear()
    result = {
        'success': True
    }
    response = make_response(json.dumps(result))
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users/<int:uid>', methods=['POST'])
@validate_request
def create_user(uid):
    print("创建用户ing")
    user = request.get_json()
    if uid not in users_dict:
        result = {
            'success': True,
            'msg': "user created successfully."
        }
        status_code = 201
        users_dict[uid] = user
    else:
        result = {
            'success': False,
            'msg': "user already existed."
        }
        status_code = 500

    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users/<int:uid>')
@validate_request
def get_user(uid):
    user = users_dict.get(uid, {})
    if user:
        result = {
            'success': True,
            'data': user
        }
        status_code = 200
    else:
        result = {
            'success': False,
            'data': user
        }
        status_code = 404

    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users/<int:uid>', methods=['PUT'])
@validate_request
def update_user(uid):
    user = users_dict.get(uid, {})
    if user:
        user = request.get_json()
        success = True
        status_code = 200
        users_dict[uid] = user
    else:
        success = False
        status_code = 404

    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/users/<int:uid>', methods=['DELETE'])
@validate_request
def delete_user(uid):
    user = users_dict.pop(uid, {})
    if user:
        success = True
        status_code = 200
    else:
        success = False
        status_code = 404

    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response
