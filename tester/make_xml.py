#Python 有三种方法解析XML:  SAX，DOM，以及 ElementTree

#SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。
#DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存
#ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

# 这里使用elementTree  
# https://www.cnblogs.com/thisyan/p/9699939.html

#思路
#1. 解析xml文件,找到body下面的各个节点变量 
#2. 找到哪些节点是变量(枚举值,区间值,必填值等)
#3. 找到哪些节点之间相互关联, 例如A节点为a,  则B节点必须为b.   C节点为1, 则D节点不准为空
#4. 直接遍历所有可能值,生成所有的xml报文 (先完成全部遍历, 后续再考虑用等价类优化)

# xml例子

# <?xml version="1.0" encoding="ISO-8859-1"?>
# <data>
# 　　<body>
# 　　　　<aaa>1</aaa>
# 　　　　<bbb>2008</bbb>
# 　　　　<ccc>1</ccc>
#       <ddd>10</ddd>
# 　　　　<eee>119</eee>
# 　　</body>
# </data>

# aaa必须为0或者1
# bbb必填 2008
# ccc 必填 1 3 5
# ddd 必填 10-12
# eee 当aaa为0时必填119,  aaa为1时可以为空


import xml.etree.ElementTree  as ET
import os
import random 

import xlrd


ran = random.randint(1,100)

# 参数分别为 当前案例标题, 当前案例xml报文内容, 文件名
# 最终生成的文件名, 会加一个1-100随机整数为后缀
def res_xml(title , iitem,filename):

    temp = iitem
        # 以下是生成xml
    root = ET.Element('body')   # 创建根节点调用方法Element
    for key , value in temp.items():
     
        ET.SubElement(root,key).text =  value 
        
    tree = ET.ElementTree(root)
        
    res_filename = './' +  filename + str(ran) + '.xml'
    # tree.write('./new.xml',encoding='utf-8')
    tree.write(res_filename,encoding='utf-8')

    data = ''
    # with open('./new.xml', 'r') as f:
    with open(res_filename, 'r') as f:

        data =  f.read()  
        # print(data)


    # filename = 'new_all.txt'
    txtfilename =  filename + str(ran) +  '.txt'
    with open(txtfilename, 'a') as file_object:
        file_object.write(title)
        file_object.write("\n")
        file_object.write(data)
        file_object.write("\n")
        file_object.write("\n")
        file_object.write("\n")



tree = ET.ElementTree()  # 实例化Element对象
root = tree.parse("./test.xml")  # 载入XML文件, root指向根节点 
print("+===========+")
print(len(root))
print(root.tag)   # 根节点



bd = root.find('body')


temp = {} 

chil = bd
for i in chil:
    # print(i.tag)   #输出 aaa, bbb, ccc, ddd ,eee
    # temp[i.tag] = 0
    tp = i.tag 
    temp[tp] = chil.find(tp).text  #将每个xml节点值转换为字典


print("以下涉及到excel部分:&&&&&&&&**********************")

# 打开文件
data = xlrd.open_workbook('./dataInfo.xlsx')

# 查看工作表
data.sheet_names()
print("sheets：" + str(data.sheet_names()))

# 通过文件名获得工作表,获取工作表1
table = data.sheet_by_name('demo')

# 获取某个单元格的值，例如获取B3单元格值
cel_B3 = table.cell(3,2).value
# print("第三行第二列的值：" + cel_B3)
print( cel_B3)

names = table.col_values(0) # 取出报文题的节点名字
names.pop(0)  #删除第一个excel列头
print(names)

values = table.col_values(1) #取出有效值集合
values.pop(0)
print(values)

# 生成有效用例
x = 0
for i in values:
    # print(i)
    
    name = names[x]
    print("测试区间↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print(name)
    
    values = i.split('|')
    for j in values:
        test1 = temp.copy() 

        test1[name]= j
        title = name + ' = ' + j
        print(test1)
        res_xml(title,test1,'trueFile')

    print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    x = x + 1   
 

errs = table.col_values(2) #取出异常值集合
errs.pop(0)
# print(errs)

x = 0
for i in errs:
    # print(i)
    name = names[x]
    print("测试区间↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print(name)
    
    values = i.split('|')
    for j in values:
        test1 = temp.copy() 

        test1[name]= j
        title = name + ' = ' + j
        res_xml(title, test1,'wrongfile')
        print(test1)

    print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    x = x + 1 


needs = table.col_values(3) #字节点是否为必填,针对必填项生成异常测试案例

needs.pop(0)
# print(needs)

x = 0
for i in needs:
    name = names[x]
    print("测试区间↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print(name)
    if i is '1':
        test1 = temp.copy() 
        test1[name]= ' '
       
        title = name + '为空'
        res_xml(title,test1,'wrongfile')
        print(test1)

    print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    x = x + 1 

