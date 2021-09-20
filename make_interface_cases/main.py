import os
import xlrd , xlwt
from xlutils.copy import copy as xl_copy
import csv
from typing import Dict, List, Any, Union, Text
import itertools
import random 
from shutil import copyfile
import copy
import sys

   
def gen_cartesian_product(*args: List[Dict]) -> List[Dict]:

    if not args:
        return []
    elif len(args) == 1:
        return args[0]

    product_list = []
    for product_item_tuple in itertools.product(*args):
        product_item_dict = {}
        for item in product_item_tuple:
            product_item_dict.update(item)

        product_list.append(product_item_dict)

    # print(product_list)
    return product_list


ran = random.randint(1,100)
# 读excel文件
# file_path = './one_cases.xlsx'
file_path= sys.argv[1]

test_data = xlrd.open_workbook(file_path)
all_sheets = test_data.sheet_names() #=> ['Sheet1', 'Sheet2']
# print(all_sheets)  #=> ['Sheet1', 'Sheet2']

# case_path = './test.csv'
case_path = 'finalcase_'+str(file_path)[:-5]+'.csv'
# 根据sheet名,取出拿到表数据
one_sheet = test_data.sheet_by_name(all_sheets[0]) #这是第一个sheet

# 接口的各个字段值
name_list = one_sheet.col_values(0)[1:]

# 初始化最终用例文件标题
with open(case_path,"w+",encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,lineterminator='\n')
    # writer.writerows([["testname","testraw","resdata"]])
    name_list.append('res')
    writer.writerows([name_list])
    print("创建test.csv第一行完成")


# 打开用例文件
test_data = xlrd.open_workbook(file_path)

# 查看工作表
test_data.sheet_names()
# print("sheets：" + str(test_data.sheet_names()))

na = test_data.sheet_names()

table = test_data.sheet_by_name(na[0])
names = table.col_values(0) # 取出报文体的节点名字
# print(names)

tableRows = table.nrows - 1 #接口字段数量(需要减去第一行)
# tableCols = table.ncols  

# print(tableRows)



title_res = []
ret_data = []

json_res = []
right_sum_data=[]
wrong_sum_data=[]  

for i in range(1,tableRows + 1):

    #每行的数据
    table_data = table.row_values(i)

    #取出各个接口的名字
    keyname = table_data[0]
    keyname = keyname.strip()
    # print(keyname)

    #正确参数的值
    right_value = str(table_data[1]).strip()
    right_value_data = right_value.split('|')
    for j in right_value_data:
        temp_json = {keyname:j}
        # print(temp_json)
        json_res.append(temp_json)
        
    # print(json_res) 
    right_sum_data.append(json_res)       
    json_res=[]

    # print('%s 的正确参数:' % keyname )
    # print(right_value_data)  
    
    #错误参数的值
    wrong_value = str(table_data[2]).strip()
    wrong_value_data = wrong_value.split('|')
    # print(wrong_value_data)
    wrong_sum_data.append(wrong_value_data)
    
    all_value = right_value_data + wrong_value_data  
    
args=right_sum_data
right_post = gen_cartesian_product(*args)

sum_wrong=0
print(wrong_sum_data)     
# sum_wrong = len(wrong_sum_data)
for k in wrong_sum_data:
    for x in k:
        sum_wrong+=1
        
temp_case = []

with open(case_path,"a",encoding='utf-8') as csvfile:
    # csvfile.seek(1)
    # csvfile.truncate()
    #~ 写入正常用例
    for i in right_post:
        # print(i)
        write_data=[]
        
        for key,value in i.items():
            writer = csv.writer(csvfile,lineterminator='\n')
            raw_res = 0
            write_data.append(value)
            temp_case=write_data
                        
        write_data.append(raw_res)    
        writer.writerows([write_data])    
    
    
    # 计算出异常用例个数,然后拷贝一个正常用例,再逐个替换其中的异常字符
    temp_case[-1]=1     # 异常用例返回值定义为1
    
    #~ 写入异常用例
    for i in wrong_sum_data: 
        z=0
        for j in i: 
            copy_temp=copy.deepcopy(temp_case)
            copy_temp[z]=j
            writer.writerows([copy_temp])  
            z+=1     
        


    

