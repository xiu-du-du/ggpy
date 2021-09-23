# _*_ coding : utf-8 _*_
# @Time:2021/9/23 11:20
# @Author:xiu-du-du
# @File:切片
# @Project:ggpy

# 字符串切片
nameStr='Hello Python'
print(nameStr[1:6:2])
print(nameStr[::-1])
print(nameStr[-1:-5:-1])
print(nameStr[5:1:-1])
# 方向错误，返回空
print(nameStr[-1:-5:1])
print(nameStr[1:5:-1])


# 元组切片
nameTuple=(1,5,6,7,8,9)
print(nameTuple[1:7:2])
print(nameTuple[-1:-7:-2])

# 列表切片
nameList=[5,3,6,7,8]
print(nameList[1:5:2])
print(nameList[-1:-5:-2])










