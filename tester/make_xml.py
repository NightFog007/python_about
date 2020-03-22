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

#正确值
aaa = [0,1]
bbb = 2008
ccc = [1,3,5]
ddd = [10,11,12]
eee = 119 if (aaa ==1)  else None 


# 此数组记录必填节点名称,用于生成异常案例. 
notnull = ['aaa','bbb','ddd']

#错误值
a = 2
b = 999
c = 8
d = 55


test1 = temp.copy() 
for i in aaa:
    test1['aaa'] = i
    print(test1)

print("****")

test1 = temp.copy() 
for i in ccc:
    test1['ccc'] = i
    print(test1)

print("****")
test1 = temp.copy() 
for i in ddd:
    test1['ddd'] = i
    print(test1)

print("****")
test1 = temp.copy()


test1['aaa'] = 0
test1['eee'] =  119
print(test1)

test1['aaa'] = 1 
test1['eee'] =  None
print(test1)

print("temp is  %s", temp)

print("以下是错误案例:")

test1 = temp.copy() 
test1['aaa'] = a 
print(test1)

test1 = temp.copy() 

test1['bbb'] = b 
print(test1)

test1 = temp.copy()
test1['ccc'] = c 
print(test1)

test1 = temp.copy()
test1['ddd'] = d 
print(test1)

test1 = temp.copy()
test1['aaa'] = 0
test1['eee'] = 999
print(test1)




for key in notnull:
    test1 = temp.copy()
    test1[key] = None 
    print(test1)

