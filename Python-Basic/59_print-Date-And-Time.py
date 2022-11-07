# Learn Python in Arabic #65 - طباعة التاريخ و الوقت print Date And Time Python
import datetime
dt = datetime.datetime.now()
print(dt)
d = datetime.datetime.now().date()
print(d)
t = datetime.datetime.now().time()
print(t)
myd=datetime.date(2020,1,25)
print(myd)
myt=datetime.time(15,20,10,12345)
print(myt)
