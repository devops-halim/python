# Learn Python in Arabic #57 - عرض ملفات و مجلدات show files folders isfile Python
from genericpath import isfile
import os
files = os.listdir("path/to/your/files")
#for file in files : print(files)
for file in files:
    if os.path.isfile("path/to/your/files/"+ file):
        print(file)
for file in files:
    if not os.path.isfile("path/to/your/files/"+ file):
        print(file)