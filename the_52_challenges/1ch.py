import sys

a = 0
while a == 0:
    try:
        bill_num =  input("请输入账单金额: ")
        bill_num = float(bill_num)
        if bill_num <= 0 :
            print("金额必须大于0,请重新输入.")
            a = 0
        else:
            a = 1

    except ValueError:
        print("输入非数字,请重新输入.")
        a = 0

a = 0
while a == 0:
    try:
        per_n = input("请输入小费比例: ")
        per_n = float(per_n)
        if per_n <= 0 :
            print("金额必须大于0,请重新输入.")
            a = 0
        else:
            a = 1
    except ValueError:
        print("输入非数字,请重新输入.")
        a = 0



tip_num = bill_num * per_n  / 100

print(tip_num)

sum_num = bill_num + tip_num

print("总金额是: %.2f " % sum_num)


# Tips:
# python str,int,float转换处理
# a_int = int('123') # str -> int
# a_float = float('123')
# a_str = str(789)

# print占位符处理
# print("总金额是: %.2f " % sum_num)


# float取前两位小数. 
# print("总金额是: %.2f " % sum_num)

# 判断一个字符串内容是数字还是字母 . 
# 第一种方式:
# 'abc'.isalpha()  #字符串内容是字母则返回true,否则返回false
# '123'.isdigit()  #字符串内容是数字则返回true,否则返回false
# 第二种方式:
# 直接在try except里用float()转换字符串,数字则直接成功,字符则走异常处理.