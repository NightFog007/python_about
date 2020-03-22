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

import xlrd



# 参数为每个test1
def res_xml(iitem):

    temp = iitem
        # 以下是生成xml
    root = ET.Element('body')   # 创建根节点调用方法Element
    for key , value in temp.items():

        # 创建子节点用方法SubElement，其中第一个参数为他的父节点，第二个参数为该节点的标签
        # 第三个参数为该节点的属性（可选）
        # student = ET.SubElement(root,key)
        # 创建子节点，其父节点为student，用text来设置该节点的内容
        ET.SubElement(root,key).text =  value 
        # ET.SubElement(student,'age').text = '22'

        # xml的写工作完成后调用ElementTree方法创建一颗xml树
        # 其参数为Element类型，即这颗树的根
    tree = ET.ElementTree(root)
        # ElementTree对象调用write方法，将数写入到xml文件中
        # 第一个参数为文件路径，第二个参为编码格式（记得写）
    tree.write('./new.xml',encoding='utf-8')

    data = ''
    with open('./new.xml', 'r') as f:
        data =  f.read()  
        # print(data)

    filename = 'new_all.txt'
    with open(filename, 'a') as file_object:
        file_object.write(data)
        file_object.write("\n")





tree = ET.ElementTree()  # 实例化Element对象
root = tree.parse("./test.xml")  # 载入XML文件, root指向根节点 
print("+===========+")
print(len(root))
print(root.tag)   # 根节点



bd = root.find('body')

# print("测试区间↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
# # print(len(bd))
# for ch in bd:
#     print(ch.tag , ": ", ch.text)

# print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")


# ch1 = root[0]  #按下标索引子节点 
# print(ch1.tag) 
# # print(ch1.find('aaa').text)  #找到根节点下,aaa节点的值

# ch2 = ch1[0]  #按下标索引子节点 
# print(ch2.tag) 
# print(ch2.text) 

# print("*******")

# # root1是根节点下一级子节 count
# root1 = root[0]
# chil = root1
# print("chil is : %s",chil)

temp = {} 

chil = bd
for i in chil:
    # print(i.tag)   #输出 aaa, bbb, ccc, ddd ,eee
    # temp[i.tag] = 0
    tp = i.tag 
    temp[tp] = chil.find(tp).text  #将每个xml节点值转换为字典

# for key,value in temp.items():
#     print(key  , "is " , value)
 

print("init value is %s " , temp)   
print("****************************")


# aaa必须为0或者1
# bbb必填 2008
# ccc 必填 1 3 5
# ddd 必填 10-12
# eee 当aaa为0时必填119,  aaa为1时可以为空

# #正确值
# aaa = [0,1]
# bbb = 2008
# ccc = [1,3,5]
# ddd = [10,11,12]
# eee = 119 if (aaa ==1)  else None 


# # 此数组记录必填节点名称,用于生成异常案例. 
# notnull = ['aaa','bbb','ddd']

# #错误值
# a = 2
# b = 999
# c = 8
# d = 55


# test1 = temp.copy() 
# for i in aaa:
#     test1['aaa'] = i
#     print(test1)

# print("****")

# test1 = temp.copy() 
# for i in ccc:
#     test1['ccc'] = i
#     print(test1)

# print("****")
# test1 = temp.copy() 
# for i in ddd:
#     test1['ddd'] = i
#     print(test1)

# print("****")
# test1 = temp.copy()


# test1['aaa'] = 0
# test1['eee'] =  119
# print(test1)

# test1['aaa'] = 1 
# test1['eee'] =  None
# print(test1)

# print("temp is  %s", temp)

# print("以下是错误案例:")

# test1 = temp.copy() 
# test1['aaa'] = a 
# print(test1)

# test1 = temp.copy() 

# test1['bbb'] = b 
# print(test1)

# test1 = temp.copy()
# test1['ccc'] = c 
# print(test1)

# test1 = temp.copy()
# test1['ddd'] = d 
# print(test1)

# test1 = temp.copy()
# test1['aaa'] = 0
# test1['eee'] = 999
# print(test1)




# for key in notnull:
#     test1 = temp.copy()
#     test1[key] = None 
#     print(test1)



print("以下涉及到excel部分:&&&&&&&&**********************")

# 打开文件
data = xlrd.open_workbook('./dataInfo.xlsx')

# 查看工作表
data.sheet_names()
print("sheets：" + str(data.sheet_names()))

# 通过文件名获得工作表,获取工作表1
table = data.sheet_by_name('demo')

# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
# table = data.sheet_by_index(0)

# 获取行数和列数
# 行数：table.nrows
# 列数：table.ncols
# print("总行数：" + str(table.nrows))
# print("总列数：" + str(table.ncols))

# 获取整行的值 和整列的值，返回的结果为数组
# 整行值：table.row_values(start,end)
# 整列值：table.col_values(start,end)
# 参数 start 为从第几个开始打印，
# end为打印到那个位置结束，默认为none
# print("整行值：" + str(table.row_values(0)))

# print("整列值：" + str(table.col_values(2)))

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
        print(test1)
        res_xml(test1)

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
        res_xml(test1)
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
        res_xml(test1)
        print(test1)

    print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    x = x + 1 

