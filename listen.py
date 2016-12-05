#!/usr/bin/env python
#-- coding: utf-8 --
import time
import os
import mail
def mytime():
 now = int(time.time())
 timeArray = time.localtime(now)
 otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
 return otherStyleTime
while 1:
    time.sleep(1)
    m=mytime()
    java_pid_nu=os.popen('ps aux | grep java | grep -v grep | wc -l')
    if java_pid_nu.read() == '2':
        java_sub_process=('ps aux | grep java | grep -v grep |awk \'{print $2}\' | xargs pmap -x | wc -l')
        print r'java_process is fine'
        if java_sub_process.read() > 1000:
            mail.pysendmail('cy.chen@networkgrand.com','cy.chen@networkgrand.com','java_sub_process','异常')
            print r'java_sub_process is not good'
        else:
            mail.pysendmail('cy.chen@networkgrand.com','cy.chen@networkgrand.com','java_sub_process','正常')
            print r'java_sub_process is fine'
    else:
        mail.pysendmail('cy.chen@networkgrand.com','cy.chen@networkgrand.com','java_process','异常')
        print r'java_process is not good'
        print java_pid_nu.read()