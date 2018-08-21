#! /usr/bin/python
# coding = utf-8
import urllib.request
import json

ApiUrl="http://www.weather.com.cn/data/cityinfo/101270101.html"
html=urllib.request.urlopen(ApiUrl)
#读取并解码
data=html.read().decode("utf-8")
#将JSON编码的字符串转换回Python数据结构
ss=json.loads(data)
info=ss['weatherinfo']
print(info)