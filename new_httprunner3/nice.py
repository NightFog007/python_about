import os
import sys
from typing import List, Dict, Text, Union, Any

from loguru import logger

from pydantic import BaseModel,Field
from typing import Union


class Person(BaseModel):
    name:str
    gender: str = "man"  #默认值
    time: Union[int, str]='demo1' #允许多种数据类型
    # password: str = Field(alias = "key") #修改已定义的字段名,后续使用时,方式是p5=Person(key='123456')

p1 = Person(name="tom") #直接传值
print(p1.json())

p2 = {"name":"Jim"} #通过字典传入
p2 = Person(**p2)
print(p2.json())

p3 = Person.copy(p1) #通过其他的实例化对象传入
print(p3.json())

p4 = Person(name=123) #pydantic在数据传输时会直接进行数据类型转换，因此，如果数据传输格式错误，但是可以通过转换变换为正确的数据类型是，数据传输也可以成功
print(p4.json())



def ensure_path_sep(path: Text) -> Text:
    """ ensure compatibility with different path separators of Linux and Windows
    """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return path

# print(ensure_path_sep('.\\my_file\\12dwq\\12\\d12d\\12d'))
