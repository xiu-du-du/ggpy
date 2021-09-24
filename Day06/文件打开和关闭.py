# _*_ coding : utf-8 _*_
# @Time:2021/9/24 9:50
# @Author:xiu-du-du
# @File:文件打开和关闭
# @Project:ggpy

# 创建文件 --> 写入数据 --> 关闭文件
creatFile=open(r'demo\test.txt','w')
creatFile.write('Hello Python')
creatFile.close()
