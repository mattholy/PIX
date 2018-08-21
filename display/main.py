#!/usr/bin/python
# -*- coding: utf-8 -*-
import epd2in7
import topIcon as ti 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
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
    data2=html2.read().decode("utf-8")
    #将JSON编码的字符串转换回Python数据结构
    ss2=json.loads(data2)
    info2=ss2['weatherinfo']
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

def makeButtom(targetScr):#绘制底栏
    menuFont = ImageFont.truetype('/usr/share/fonts/opentype/SourceHanSerifCN-Bold.otf', 15)#设定操作指示器字体
    targetScr.text((7, 244), '返回', font = menuFont, fill = 0)
    targetScr.text((60, 244), '▲', font = menuFont, fill = 0)
    targetScr.text((103, 244), '▼', font = menuFont, fill = 0)
    targetScr.text((140, 244), '确认', font = menuFont, fill = 0)
    targetScr.line((0, 244, 176, 244), fill = 0)
    targetScr.line((44, 244, 44, 264), fill = 0)
    targetScr.line((88, 244, 88, 264), fill = 0)
    targetScr.line((132, 244, 132, 264), fill = 0)

def makeTop(targetScr):#绘制顶栏
    menuFont = ImageFont.truetype('/usr/share/fonts/truetype/dejavn/DejaVuSans.ttf', 10)#设定操作指示器字体
    targetScr.rectangle((0, 0, 176, 20), fill = 0)#状态栏
    targetScr.text((1, 0), os.popen('date +%Y-%m-%d').read(), font = menuFont, fill = 255)#日期
    targetScr.text((1, 10), os.popen('date +%H:%M').read(), font = menuFont, fill = 255)#时间
    cursor = 0
    cursor += ti.netInfo(targetScr,cursor)
def textAlign(tarScreen,strTo,align,fontName,verticalPos,horiStart,horiEnd,fillType):
    if align == 1:
        lenPos=fontName.getsize(strTo)[0]
        tarScreen.text((horiStart,verticalPos), strTo, font =fontName, fill = fillType)
    elif align == 2:
        lenPos=fontName.getsize(strTo)[0]
        tarScreen.text(((horiEnd-horiStart)/2-lenPos/2+horiStart,verticalPos), strTo, font =fontName, fill = fillType)
    elif aligh == 3:
        lenPos=fontName.getsize(strTo)[0]
        tarScreen.text((horiEnd-lenPos,verticalPos), strTo, font =fontName, fill = fillType)


def main():
    epd = epd2in7.EPD()
    epd.init()
    clearScreen = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)#新建一个屏幕clearScreen作为主页
    mainScreen = ImageDraw.Draw(clearScreen)#开始绘制该屏幕
    menuFont = ImageFont.truetype('/usr/share/fonts/opentype/SourceHanSerifCN-Regular.otf', 15)#设定操作指示器字体
    tilteFont = ImageFont.truetype('/usr/share/fonts/opentype/SourceHanSerifCN-Regular.otf', 35)
    #clearScreen主页布局：开始绘制
    mainScreen.text((2, 20), '位置：', font = menuFont, fill = 0)
    mainScreen.text((2+menuFont.getsize('位置：')[0], 20), getWeather('城市'), font = menuFont, fill = 0)
    textAlign(mainScreen,getWeather('气温'),2,tilteFont,40,0,176,0)
    textAlign(mainScreen,getWeather('天气'),2,menuFont,80,0,176,0)
    textAlign(mainScreen,getWeather('风向')+getWeather('风速'),2,menuFont,97,0,176,0)
    makeTop(mainScreen)
    makeButtom(mainScreen)
    #结束主页绘制
    epd.display_frame(epd.get_frame_buffer(clearScreen))#push到屏幕显示

if __name__ == '__main__':
    main()
    oldTime=os.popen('date +%H:%M').read()
    oldIP=os.popen('hostname -I').read()
    while True:
        if oldTime!=os.popen('date +%H:%M').read() or oldIP!=os.popen('hostname -I').read():
            main()
            oldTime=os.popen('date +%H:%M').read()
            oldIP=os.popen('hostname -I').read()