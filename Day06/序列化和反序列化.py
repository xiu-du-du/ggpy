# _*_ coding : utf-8 _*_
# @Time:2021/9/24 11:16
# @Author:xiu-du-du
# @File:序列化和反序列化
# @Project:ggpy
import json
# dumps(对象名)  序列化
# newFile=open(r'demo\save.txt','w')
# nameList=['zs','ls']
# newStr=json.dumps(nameList)
# newFile.write(newStr)
# newFile.close()

# dump(对象名,文件名)  序列化
# newFile=open(r'demo\save1.txt','w')
# nameList=['zs','ls']
# json.dump(nameList,newFile)
# newFile.close()

# loads(对象名) 反序列化
# readFile=open(r'demo\save1.txt','r')
# readCount=readFile.read()
# print(type(json.loads(readCount)))
# print(json.loads(readCount))
# readFile.close()

# load(文件名) 反序列化
readFile=open(r'demo\save1.txt','r')
res=json.load(readFile)
print(type(res))
print(res)
readFile.close()