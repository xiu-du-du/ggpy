# _*_ coding : utf-8 _*_
# @Time:2021/9/25 6:21
# @Author:xiu-du-du
# @File:urllib模块
# @Project:ggpy

# 导入 urllib 模块
import urllib.request
url='http://www.baidu.com'

# 发送请求获取返回值
response=urllib.request.urlopen(url)
print(response)
print(type(response))
# 获取页面中的源码
# read() 返回是字节形式的二进制数据
# decode('编码格式') --> 解码：二进制 --> 字符串
content=response.read().decode('utf-8')
print(content)




