# _*_ coding : utf-8 _*_
# @Time:2021/9/25 7:19
# @Author:xiu-du-du
# @File:请求对象的定制
# @Project:ggpy

import urllib.request
url='https://www.baidu.com'
# 无法读取到内容，遇到反爬手段
# 需要使用UA伪装，再去请求
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

# 定制一个对象
request=urllib.request.Request(url=url,headers=header)

# 请求定制的对象
response=urllib.request.urlopen(request)

# 读取返回内容
content=response.read().decode('utf8')
print(content)


