#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

def network(myPage,pos):
    myPage.pieslice((144-pos,2,178-pos,36),225,315,fill = 255)
    return 30#图标宽度

def cpuLoad(myPage,pos):
    myPage.rectangle((176-pos-20,2,176-pos,18),fill = 255)
    return 22#图标宽度

def netInfo(myPage,pos):
    menuFont = ImageFont.truetype('/usr/share/fonts/truetype/dejavn/DejaVuSans.ttf', 10)#设定操作指示器字体
    hostnamLen=menuFont.getsize(os.popen('hostname').read())[0]
    ipLen=menuFont.getsize(os.popen('hostname -I').read())[0]
    offLine=menuFont.getsize("OFF-LINE")[0]
    ipAdd=os.popen('hostname -I').read()
    if len(ipAdd)<4:
        myPage.text((172-pos-offLine, 10), 'OFF-LINE', font = menuFont, fill = 255)
    else:
        myPage.text((176-pos-ipLen, 10), ipAdd, font = menuFont, fill = 255)
    myPage.text((176-pos-hostnamLen, 0), os.popen('hostname').read(), font = menuFont, fill = 255)
    return max(hostnamLen,ipLen)#图标宽度