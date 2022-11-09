# Learn Python in Arabic #67 - تهيئة التاريخ و الوقت format Date And Time Python
import datetime
now = datetime.datetime.now()

print(now.strftime("%I:%M:&S %p" ))
print(now.strftime("%d %B %Y" ))

print(now.strftime("%I:%M:&S %p %%" ))


print(now.strftime("%d %B %Y" ))


# kurze für tages name
print(now.strftime("%a"))
# name das tages
print(now.strftime("%A"))
# abkurzung  monat
print(now.strftime("%b"))
# monate
print(now.strftime("%B"))
# time und date in kuze form
print(now.strftime("%c"))
# 
print(now.strftime("%d"))
#
print(now.strftime("%H"))
#
print(now.strftime("%I"))
#
print(now.strftime("%j"))
#
print(now.strftime("%m"))
#
print(now.strftime("%M"))
#
print(now.strftime("%p"))
#
print(now.strftime("%S"))
#
print(now.strftime("%x"))
#
print(now.strftime("%X"))
#
print(now.strftime("%y"))
#
print(now.strftime("%Y"))

 













