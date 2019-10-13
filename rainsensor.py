# -*- coding: utf-8 -*-
#2019/03/03~
print('[ Rain Senser ]')
from line.linepy import *
import RPi.GPIO as GPIO
from time import sleep
import time, datetime
# 初期設定
GPIO.setmode(GPIO.BCM)
# GPIO 15 をデジタル入力に設定
GPIO.setup(15, GPIO.IN)
print('[ APP SET ]')
app = "IOSIPAD\t8.12.2\tTalkBot\t11.2.5"
try:
    print('[ LOAD LOGIN ]')
    f = open('authtoken.txt', 'r')
    authtk = f.read()
    f.close()
    client = LINE(authtk, speedThrift=False, appName=app)
    print('[AUTHTOKEN]\n%s\n' % (str(client.authToken)))
    f = open('authtoken.txt', 'w')
    f.write(str(client.authToken))
    f.close()
    print('[ Client SET COMPLETE! ]')
except Exception as e:
    print('== Failed LOGIN ==\n\n'+str(e)+'\n\n==================')

clientPoll = OEPoll(client)
twn=True
while True:
    now = datetime.datetime.now()
    date = '{:%Y/%m/%d %H:%M:%S}'.format(now)
    sendmid = "" # 送り相手のmid
    if GPIO.input(15) == 1:
        if twn != True:
            client.sendMessage(sendmid,"{時刻: %s}\n\n▶晴れました！"%(date))
            print(sendmid,"時刻: %s\n晴れました！"%(date))
            twn=True
            sleep(10)
    else:
        if twn != False:
            client.sendMessage(sendmid,"{時刻: %s}\n▶雨が降り始めました！"%(date))
            print(sendmid,"時刻: %s\n\n雨が降り始めました！"%(date))
            twn=False
            sleep(10)