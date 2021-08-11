import xml.etree.ElementTree  as ET
import os
import random 
# 20210811 test
import xlrd
import linecache
import csv
ran = random.randint(1,100)

# header路径
header_path = './data/header.txt'

# 人工案例, 每个接口执行此脚本前,根据接口文档, 自己录入. 
file_path = './data/testcase.xlsx'

# body示例文件, 每个接口执行此脚本前,通过转换 ./data/temp.xlsx拿到
example_body = './data/test.xml'

# 最终生成案例的保存地址
case_path  = './post_sat/test.csv'

with open(case_path,"w+",encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,lineterminator='\n')
    writer.writerows([["testname","testraw","resdata"]])

# 参数分别为 当前案例标题, 当前案例xml报文Body内容, 文件名
def res_xml(title , iitem, filename):

    ret_data = ''

    # 设置接口的断言判断语句
    if filename == 'trueFile':
        ret_data = "tests[\"ReturnCode\"] = responseBody.has(\"000000\")"     
    else:
        ret_data = "tests[\"ReturnCode\"] = responseBody.has(\"FUS27777\")"


    temp = iitem
    # 以下是生成xml
    root = ET.Element('Body')   # 调用方法Element创建根节点Body
    req  = ET.SubElement(root,'Request')  # 根节点的子节点为Request

    # 将xlsx文件里的字段,放到Request里
    for key , value in temp.items():
     
        ET.SubElement(req,key).text =  value 
        
    # 组装xml    
    tree = ET.ElementTree(root)
    
    # 生成各个xml文件
    res_filename = './res/' +  filename + str(ran) + '.xml'
    tree.write(res_filename,encoding='utf-8')

    # 将xml文件内容转为txt文件
    data = ''
    with open(res_filename, 'r',encoding='utf-8') as f:
        data =  f.read()  
    txtfilename = './res/' + filename + str(ran) +  '.txt'

    # 各接口XML报文的<Body>字段之前内容,每个接口执行此脚本前,手工放入header.txt文件.
    header = ''
    with open(header_path, 'r',encoding='utf-8') as f:
        header =  f.read()  




    # test.csv用于保存最终案例. 每个接口执行此脚本前, 手工复制项目内的test_base.csv文件,并改名为test.csv文件即可.
    with open(case_path,"a",encoding='utf-8') as csvfile:
        # csvfile.seek(1)
        # csvfile.truncate()
        writer = csv.writer(csvfile,lineterminator='\n')
        raw_res = header + data+  ' </Service>]]></arg0></pub:request></soapenv:Body></soapenv:Envelope>'
        writer.writerows([[title,raw_res,ret_data]])







tree = ET.ElementTree()  # 实例化Element对象
root = tree.parse(example_body)  # 载入XML文件, root指向根节点 

bd = root[0].find('Request')

temp = {} 

chil = bd
for i in chil:
    # print(i.tag)  
    # temp[i.tag] = 0
    tp = i.tag 
    temp[tp] = chil.find(tp).text  #将每个xml节点值转换为字典


# 打开人工案例文件
data = xlrd.open_workbook(file_path)

# 查看工作表
data.sheet_names()
print("sheets：" + str(data.sheet_names()))

na = data.sheet_names()

# 通过文件名获得工作表,获取工作表1
# table = data.sheet_by_name('demo')
table = data.sheet_by_name(na[0])

names = table.col_values(0) # 取出报文体的节点名字
names.pop(0)  #删除第一个excel列头,'name'

values = table.col_values(1) #取出有效值集合
values.pop(0) # 删除 'value'


# 根据案例文件的value列, 生成有效用例
x = 0
for i in values:
    # print(i)
    
    name = names[x]
    
    values = i.split('|')
    for j in values:
        test1 = temp.copy() 

        test1[name]= j
        title = name + ' = ' + j + '  T'+  str(ran)
        res_xml(title,test1,'trueFile')
   
    x = x + 1   
 


# 根据案例文件的err列, 生成异常用例
errs = table.col_values(2) #取出异常值集合
errs.pop(0)
# print(errs)

x = 0
for i in errs:
    # print(i)
    name = names[x]
    
    values = i.split('|')
    for j in values:
        test1 = temp.copy() 

        test1[name]= j
        title = name + ' = ' + j  + '  F'+  str(ran)
        res_xml(title, test1,'wrongfile')

 
    x = x + 1 


#根据案例文件的need列,字节点是否为必填,针对必填项生成异常测试案例
needs = table.col_values(3) 
needs.pop(0)
# print(needs)

x = 0
for i in needs:
    name = names[x]

    if i == '1':
        test1 = temp.copy() 
        test1[name]= ' '
       
        title = name + '为空'  + '  F'+  str(ran)
        res_xml(title,test1,'wrongfile')



    x = x + 1 

