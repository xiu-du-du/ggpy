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


'''--------------------修改---------------------'''
# 指定列表中元素的下标修改元素的值
cityList=['北京','深圳','上海']
cityList[2]='杭州'
print(cityList)


'''--------------------查找--------------------'''
# 查询元素是否在列表中
newFood=input('输入你想吃的食物：')
foodList=['米饭','面条']
if newFood in foodList:
    print('有这个食物')
else:
    print('没有这个食物')

# 查询元素是否不在列表中
newName=input('请输入你的姓名：')
nameList=['张三','小明']
if newName not in nameList:
    print('不认识')
else:
    print('认识')


'''--------------------删除--------------------'''
# del 根据下标进行删除
numList=[1,2,3,4,5,6]
del numList[4]
print(numList)

# pop() 删除列表中末尾的元素
# 返回删除元素的值
aList=['1','2','3','4','5','50']
print(type(aList.pop()))
print(aList)

# remove() 根据对应元素值删除列表中的元素
bList=[1,2,3,4,5,6]
bList.remove(5)
print(bList)

