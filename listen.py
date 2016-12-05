#!/usr/bin/env python
import time
import os
import mail
def mytime():
 now = int(time.time())
 timeArray = time.localtime(now)
 otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
 return otherStyleTime
while 1:
    time.sleep(5)
    m=mytime()
    java_pid_nu=os.system('ps aux | grep java | grep -v grep | wc -l')
    if java_pid_nu!=1:
        print m+'err'
    else:
        java_sub_process=('ps aux | grep java | grep -v grep |awk \'{print $2}\' | xargs pmap -x | wc -l')
        if java_sub_process>1000:
            mail.pysendmail('cy.chen@networkgrand.com','cy.chen@networkgrand.com','java_sub_process','异常','smtp.mxhichina.com','cy.chen@networkgrand.com','123qwe!@#QWE')
        else:
            mail.pysendmail('cy.chen@networkgrand.com','cy.chen@networkgrand.com','java_sub_process','正常','smtp.mxhichina.com','cy.chen@networkgrand.com','123qwe!@#QWE')
