# Learn Python in Arabic #66 - تخصيص التاريخ و الوقت custom Date And Time Python
import datetime
now = datetime.datetime.now()
d = now.day
m = now.month
y = now.year
# houer
h = now.hour
mi = now.minute
se = now.second
ms = now.microsecond
print(d)
print(m) 
print(y)
print(h)
print(mi)
print(se)
print(ms)
d2 = str(now.day)
m2 = str(now.month)
y2 = str(now.year)
h2 = str(now.hour)
mi2 = str(now.minute)
se2 = str(now.second)
ms2 = str(now.microsecond)
print (d2 + "-" + m2 + "-" + y2  )
print (d2 + "/" + m2 + "/" + y2 )
print (d2 + "_" + m2 + "_" + y2 + "  " + h2 + ":" + mi2 + ":" + ms2    )


