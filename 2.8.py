# -*- coding:utf-8 -*-

import time
import webbrowser

total = 2
count = 0

print ("It is working.\n"+ "Now is " + time.ctime())
while(count < total):
    time.sleep(5) #休息两小时(可修改）
    webbrowser.open("https://www.baidu.com/")
    count += 1
