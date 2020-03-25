import xml.etree.ElementTree  as ET
import os
import random 
import xlrd
import linecache
import csv
ran = random.randint(1,100)

file_path = './data/temp.xlsx'

# 打开文件
data = xlrd.open_workbook(file_path)

# 查看工作表
data.sheet_names()
print("sheets：" + str(data.sheet_names()))

for i in data.sheet_names():

        # 通过文件名获得工作表,获取工作表1
    table = data.sheet_by_name(i)

    names = table.col_values(0) # 取出报文 的节点名字

    root = ET.Element('Body')   # 创建根节点调用方法Element
    stu  = ET.SubElement(root,'Request')

    for key   in names:
        
        ET.SubElement(stu,key).text =  ' '
            
    tree = ET.ElementTree(root)
            
    # res_filename =  'xmlFile'+ i + str(ran) + '.xml'
    res_filename =  'test'+  '.xml'

    tree.write(res_filename,  encoding='utf-8')
