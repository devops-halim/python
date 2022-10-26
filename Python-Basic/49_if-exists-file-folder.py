# Learn Python in Arabic #55 - التحقق من وجود ملفات و مجلدات if exists file folder Python
import os

if not os.path.exists("myfolder"):
    os.mkdir("myfolder")

if os.path.exists("my.txt"):
    print("yes")
else:
    print("no")
if os.path.exists("myfolder"):
    print("yes Dir")
else:
    print("no Dir")
