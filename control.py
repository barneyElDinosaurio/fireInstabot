#!/usr/bin/python


import os
import time
from firebase import firebase


import sys
import psutil
import logging

firebase = firebase.FirebaseApplication('https://instagrambot-49b72.firebaseio.com/', None)


while 1 < 2:
    
    reseteo = firebase.get('/user1', 'reseteo')
    reseteo = int(reseteo)
    print reseteo

    if reseteo is 1:

        print reseteo
        print "reseteando programa"
        firebase.put('','/user1/reseteo', '0')
        

        os.system("taskkill /F /IM python.exe")#kill
        os.system("C:\Python27\python C:\Users\M\Desktop\carloco\instabo.py")#born


    time.sleep(20)
