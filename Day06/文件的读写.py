# _*_ coding : utf-8 _*_
# @Time:2021/9/24 11:07
# @Author:xiu-du-du
# @File:文件的读写
# @Project:ggpy

# write() 写入数据
# 写入模式'w'
# 每次写入数据会清空原来的数据然后再写
fileChange=open(r'demo\test.txt','w')
fileChange.write('Hello,Python! I Am Here.')
fileChange.close()
# 只读模式'r'
fileChange=open(r'demo\test.txt','r')
newFile=fileChange.readline()   # 读取一行
fileChange.readlines()   # 读取多行，返回列表形式
print(newFile)
fileChange.close()
# 添加模式'a'
# 每次写入数据不会清空原来数据，会在原来的数据后接着写入
fileChange=open(r'demo\test.txt','a')
fileChange.write('Hello,Python! I Am Here.\n')
fileChange.close()









