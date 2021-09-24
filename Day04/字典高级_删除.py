# _*_ coding : utf-8 _*_
# @Time:2021/9/23 15:13
# @Author:xiu-du-du
# @File:字典高级_删除
# @Project:ggpy

personDict={'name':'小明','age':18}

# del 删除字典中某个键值对
# 如果使用del删除整个字典，不保留字典对象，会将字典对象删除掉
# del personDict['name']
# print(personDict)

# clear 清空字典，保留字典对象
personDict.clear()
print(personDict)
