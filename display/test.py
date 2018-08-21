#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import json

def getWeather(item):#可选  城市、气温、体感温度、天气、气压、风向、风速、湿度
    ApiUrl="http://www.weather.com.cn/data/cityinfo/101270101.html"
    html=urllib.request.urlopen(ApiUrl)
    #读取并解码
    data=html.read().decode("utf-8")
    #将JSON编码的字符串转换回Python数据结构
    ss=json.loads(data)
    info=ss['weatherinfo']
    #-----------------------------------
    ApiUrl2="http://www.weather.com.cn/data/sk/101270101.html"
    html2=urllib.request.urlopen(ApiUrl2)
    #读取并解码
    data2=html.read().decode("utf-8")
    #将JSON编码的字符串转换回data2
    ss2=json.loads(data2)
    info2=ss['weatherinfo']
    print(data2)
    if item=='城市':
        return info2['city']
    elif item=='气温':
        return info['temp2']
    elif item=='体感温度':
        return info['temp1']
    elif item=='天气':
        return info['weather']
    elif item=='气压':
        return info2['AP']
    elif item=='风向':
        return info2['WD']
    elif item=='风速':
        return info2['WS']
    elif item=='湿度':
        return info2['SD']
    else:
        return 'Opps...Wrong choice'
    

ApiUrl2="http://www.weather.com.cn/data/sk/101270101.html"
html2=urllib.request.urlopen(ApiUrl2)
#读取并解码
data2=html2.read().decode("utf-8")
#将JSON编码的字符串转换回data2
ss2=json.loads(data2)
info2=ss2['weatherinfo']
print(data2)