# _*_ coding : utf-8 _*_
# @Time:2021/9/23 8:34
# @Author:xiu-du-du
# @File:列表高级
# @Project:ggpy

# append() 在list中末尾添加新元素
# 返回值：None
dishList=['凉菜','炒菜']
print(dishList)
dishList.append('野菜')
print(dishList)

# insert() 给list中指定下标的位置添加新元素
# 返回值：None
numList=['a','b','c']
print(numList)
numList.insert(0,'num')
print(numList)

# extend() 将一个列表中的元素添加到另一个列表中
# 返回值：None
nameList1=['tim','jim','jon']
nameList2=['tim','jim','jon']
print(nameList1)
nameList1.extend(nameList2)
print(nameList1)
print(nameList2)








