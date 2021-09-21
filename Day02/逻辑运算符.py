# _*_ coding : utf-8 _*_
# @Time:2021/9/22 4:00
# @Author:xiu-du-du
# @File:逻辑运算符
# @Project:ggpy

# and两端都为true，则返回true，反之为false
print(5>1 and 5>2)
print(5>10 and 5>2)
print(5>2 and 5>10)
print(5>11 and 5>12)

# or两端都为false，则返回false，反之为true
print(5>1 or 5>2)
print(5>10 or 5>2)
print(5>2 or 5>10)
print(5>11 or 5>12)

# not取反
print(not True)
print(not False)
print(not 10>20)








