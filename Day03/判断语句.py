# _*_ coding : utf-8 _*_
# @Time:2021/9/22 13:44
# @Author:xiu-du-du
# @File:if判断语句
# @Project:ggpy

# if 语句
userAge=int(input('请输入你的年龄：'))
if userAge>=18:
    print('You Can Drive!')


# if else 语句
genderIsTrue=True
if genderIsTrue:
    print('You Can Drive')
else:
    print("You Can't Drive")

# demo
age=int(input('输入你的年龄：'))
if age>18:
    print("Yes")
else:
    print("No")

# if elif 语句
score=int(input('输入你的成绩：'))
if score>=90:
    print('nice')
elif score>=80:
    print('well')
elif score>=60:
    print('go go go')
else:
    print('trash')



