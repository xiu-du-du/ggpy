# _*_ coding : utf-8 _*_
# @Time:2021/9/25 6:35
# @Author:xiu-du-du
# @File:urllib_1个类型6个方法
# @Project:ggpy

import urllib.request
url='http://www.baidu.com'

# 1个类型 --> HTTPResponse
response=urllib.request.urlopen(url)
# print(type(response))

# 6个方法
# read() ---> 按字节读取，为空会读取全部字节(读取速度较慢),返回bytes类型
# content=response.read()
# content=response.read(5)
# print(content)
# print(type(content))

# readline() ---> 读取一行,返回bytes类型
# content=response.readline()
# print(content)
# print(type(content))

# readlines() ---> 读取全部行,返回list类型
# content=response.readlines()
# print(content)
# print(type(content))

# getcode() ---> 获取状态码，如果是200，代表逻辑正确
# content=response.getcode()
# print(content)

# geturl() ---> 获取url的地址
# content=response.geturl()
# print(content)

# getheaders() ----> 获取一些状态信息
# content=response.getheaders()
# print(content)

