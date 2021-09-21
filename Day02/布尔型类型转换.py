# _*_ coding : utf-8 _*_
# @Time:2021/9/22 2:53
# @Author:xiu-du-du
# @File:布尔型类型转换
# @Project:ggpy

# 除了0以外的所有正负整数进行bool转换，值全都为True
a=10
print(type(bool(a)))
print(bool(a))

a=-5
print(type(bool(a)))
print(bool(a))

a=0
print(type(bool(a)))
print(bool(a))

# 字符串不为空，值都为True
a='123abc'
print(type(bool(a)))
print(bool(a))

a='1.55'
print(type(bool(a)))
print(bool(a))

a=''
print(type(bool(a)))
print(bool(a))


# 浮点数不为0，值都为True
a=5.99
print(type(bool(a)))
print(bool(a))

a=0.0
print(type(bool(a)))
print(bool(a))

# 列表中有数据，值都为True
nameList=['a','b']
print(type(nameList))
print(type(bool(nameList)))
print(bool(nameList))

nameList=[]
print(type(nameList))
print(type(bool(nameList)))
print(bool(nameList))

# 元祖中有数据，值都为True
nameTuple=('a','b','c')
print(type(nameTuple))
print(type(bool(nameTuple)))
print(bool(nameTuple))

nameTuple=()
print(type(nameTuple))
print(type(bool(nameTuple)))
print(bool(nameTuple))

# 字典中有数据，值都为True
nameDict={'name':'a','age':18}
print(type(nameDict))
print(type(bool(nameDict)))
print(bool(nameDict))

nameDict={}
print(type(nameDict))
print(type(bool(nameDict)))
print(bool(nameDict))

# 什么情况下为False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
