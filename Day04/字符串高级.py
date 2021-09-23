# _*_ coding : utf-8 _*_
# @Time:2021/9/23 7:13
# @Author:xiu-du-du
# @File:字符串高级
# @Project:ggpy

# len() --> 获取长度
# 返回值:int,返回字符串的长度
print(len('Hello Python'))

# find() --> 查找内容
# 返回值:int,返回要查询内容所在的下标
print('Hello Python'.find('n'))

# startswith() --> 匹配开头
# 返回值:bool,返回True或False
print('Hello Python'.startswith('He'))

# endswith() --> 匹配结尾
# 返回值:bool,返回True或False
print('Hello Python'.endswith('n'))

# count() --> 计算出现次数
# 返回值:int,返回次数
print('Hello Python'.count('l'))

# replace() --> 替换字符串内指定内容，可以指定替换多少次
# 返回值:string,返回替换后的字符串
print('Hello Python'.replace('Python', 'World'))
print('Hello Python'.replace('l', 'c',1))

# split() --> 切割字符串
# 返回值:list,返回切割后的子串
print('Hello Python'.split(' '))

# upper() --> 全部转换成大写
# 返回值:string,返回转换后的字符串
print('Hello Python'.upper())

# lower() --> 全部转换成小写
# 返回值:string,返回转换后的字符串
print('Hello Python'.lower())

# strip() --> 去除字符串首尾的空格
print("   Hello Python   ".strip())

# join() --> 字符串穿插拼接
# 返回值:string,返回穿插拼接后的字符串
print('#'.join('Hello Python'))
