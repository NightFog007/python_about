from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Header
from fastapi.middleware.cors import CORSMiddleware
import datetime
from threading import Thread

import uvicorn

from fastapi import FastAPI
import os
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles



app = FastAPI(docs_url=None, redoc_url=None)

root = os.path.abspath(os.path.join(os.path.basename(__file__), "../.."))
print(root)



# fake_items_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"ZZZ"}]

@app.get("/notice")
async def 滚动条():
    str1 = '            如果一键开户后数据没有自动复制到粘贴板,请升级到最新版本chrome浏览器.'
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=str1, headers=headers)

@app.get("/one_bugs_percent")
async def 缺陷密度():
    res = 0.9
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)


@app.get("/no_fix_bugs")
async def 遗留缺陷比例():
    res = 3
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)


@app.get("/highest_bugs_percent")
async def 严重问题比例():
    res = 1
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)


@app.get("/security_testes")
async def 安全基线测试():
    res = 0
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

@app.get("/code_reviews")
async def 代码评审():
    res = 95
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

@app.get("/check_tools_haved")
async def 代码质量检查接入率():
    res = 100
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

@app.get("/check_tools_passed")
async def 代码质量检查达标率():
    res = 95
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

@app.get("/unit_test_percent")
async def 单元测试覆盖率():
    res = 0.9
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

@app.get("/res_time")
async def 统计时间():
    return '2021-10-21 19:22:33'

@app.get("/new_result")
async def 新的所有结果():
    
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S')
    
    one_bugs_percent="0.9"
    two_no_fixed_bugs="12%"
    three_online_bugs = "2%"
    four_highest_bugs = "2%"
    five_security_bugs = "0个"
    six_code_reviews = "99分"
    seven_check_tools_haved="100%"
    eight_check_tools_passed="90%"
    nine_unit_test_percent="15%"
    
    # names = ['缺陷密度','遗留缺陷比例','线上问题比例','严重问题比例','安全基线测试','代码评审','代码质量检查接入率','代码质量检查达标率','项目单元测试覆盖率']  
    # defines = ['本月发现缺陷总数/代码行数(千行)','遗留缺陷总数/发现缺陷总数*100%','线上问题总数/发现缺陷总数*100%','(严重问题总数+致命问题总数)/发现缺陷总数*100%','基础安全测试13项,不通过个数','每月>2次,代码量>20%','接入sonarqube服务数/项目服务总数','达标率=扫描指标合格服务数/项目服务总数','单元测试覆盖率']

    # cankao_res=['密度<5','比例<15%','比例<20%','比例<10%','不符合项<1个','得分>80分','100%','100%','>=20%']
    
    
    
    res = [
        ['缺陷密度','本月发现缺陷总数/代码行数(千行)',one_bugs_percent,'密度<5',"Passed",time_str],
        ['遗留缺陷比例','遗留缺陷总数/发现缺陷总数*100%',two_no_fixed_bugs,'比例<15%',"Passed",time_str],
        ['线上问题比例','线上问题总数/发现缺陷总数*100%',three_online_bugs,'比例<20%',"Failed",time_str],
        ['严重问题比例','(严重问题总数+致命问题总数)/发现缺陷总数*100%',four_highest_bugs,'比例<10%',"Passed",time_str],
        ['安全基线测试','基础安全测试13项,不通过个数',five_security_bugs,'不符合项<1个',"Passed",time_str],
        ['代码评审','每月>2次,代码量>20%',six_code_reviews,'得分>80分',"Failed",time_str],
        ['代码质量检查接入率','接入sonarqube服务数/项目服务总数',seven_check_tools_haved,'100%',"Passed",time_str],
        ['代码质量检查达标率','达标率=扫描指标合格服务数/项目服务总数',eight_check_tools_passed,'100%',"Failed",time_str],
        ['项目单元测试覆盖率','单元测试覆盖率',nine_unit_test_percent,'>=20%',"Failed",time_str],
    ]
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)

    




@app.get("/results")
async def 所有结果():
    one_bugs_percent="0.9"
    two_no_fixed_bugs="12%"
    three_online_bugs = "2%"
    four_highest_bugs = "2%"
    five_security_bugs = "0个"
    six_code_reviews = "99分"
    seven_check_tools_haved="100%"
    eight_check_tools_passed="90%"
    nine_unit_test_percent="15%"
    
    res = [
        {one_bugs_percent:"Passed"},
        {two_no_fixed_bugs:"Passed"},
        {three_online_bugs:"Failed"},
        {four_highest_bugs:"Failed"},
        {five_security_bugs:"Passed"},
        {six_code_reviews:"Passed"},
        {seven_check_tools_haved:"Passed"},
        {eight_check_tools_passed:"Failed"},
        {nine_unit_test_percent:"Failed"},
    ]
    
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=res, headers=headers)



if __name__ == '__main__':
  uvicorn.run(app=app,host="0.0.0.0",port=8081)