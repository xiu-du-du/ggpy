# _*_ coding : utf-8 _*_
# @Time:2021/9/23 14:59
# @Author:xiu-du-du
# @File:字典高级_查询
# @Project:ggpy

personDict={'name':'小明','age':28}

# 使用[]的方式，访问personDict中的值
# 如果访问不存在的值，会报错'KeyError'
# print(personDict["name"])
# print(personDict['age'])
# print(personDict['sex'])

# 使用get()的方式，获取personDict中的值
# 如果访问不存在的值，不会报错，只会返回None
print(personDict.get('name'))
print(personDict.get('age'))
print(personDict.get('sex'))