# _*_ coding : utf-8 _*_
# @Time:2021/9/23 17:44
# @Author:xiu-du-du
# @File:局部变量和全局变量
# @Project:ggpy

# 局部变量：函数内部定义的，函数外部无法调用
# def num():
#     a=1
# print(a)

# 全局变量：函数外部定义的变量，函数内部和外部都可以使用
a=1
def num():
    print(a)
print(a)
num()





