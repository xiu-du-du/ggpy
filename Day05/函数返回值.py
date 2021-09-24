# _*_ coding : utf-8 _*_
# @Time:2021/9/23 17:30
# @Author:xiu-du-du
# @File:函数返回值
# @Project:ggpy

# 函数 返回值
def num(a,b):
    return a+b
print(num(15,6))

# 案例练习
def buyIceCream(money):
    if money>=5:
        return '冰淇淋'
    else:
        return '钱不够'

gold=int(input('请输入你带了多少钱:'))
res=buyIceCream(gold)
print(res)




