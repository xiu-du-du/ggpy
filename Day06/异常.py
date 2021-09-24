# _*_ coding : utf-8 _*_
# @Time:2021/9/24 12:10
# @Author:xiu-du-du
# @File:异常
# @Project:ggpy

# 异常处理方式
# tyr:
#     表达式
# except 异常类型:
#     友好提示
try:
    readFile=open(r'num.txt','r')
    readFile.read()
except FileNotFoundError:
    print('文件找不到')



