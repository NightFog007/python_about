# 使用| 分割每个节点的枚举值	
#节点为必填，则必填项为1； 0代表非必填	
# 如果两个节点之间有逻辑关系，例如aaa为1时,eee必须为119,否则eee可以为空, 则eee的表示方式为: 119 ; and aaa = 1
# 如果某个值无数据可填写, 用 -  代替.


import xlrd
import os

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
print("总行数：" + str(table.nrows))
print("总列数：" + str(table.ncols))

# 获取整行的值 和整列的值，返回的结果为数组
# 整行值：table.row_values(start,end)
# 整列值：table.col_values(start,end)
# 参数 start 为从第几个开始打印，
# end为打印到那个位置结束，默认为none
print("整行值：" + str(table.row_values(0)))

print("整列值：" + str(table.col_values(2)))

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

for i in values:
    print(i)
   

aValues = values[0].split('|') # 第一个子节点的有效值数组
print("测试区间↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print("测试区间↑↑↑↑↑↑↑↑↑↑↑↑↑↑")

errs = table.col_values(2) #取出异常值集合
errs.pop(0)
print(errs)

needs = table.col_values(3) #字节点是否为必填
needs.pop(0)
print(needs)
