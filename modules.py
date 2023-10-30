import time
localtime=time.asctime(time.localtime(time.time() ) )
print("Lcal time is :",localtime)

import calendar
cal=calendar.month(2021,10)
print("Cal is here \n",cal)

import time
print("Start time is :%s"%time.ctime())
time.sleep(5)
print("End time is   : %s"%time.ctime())
