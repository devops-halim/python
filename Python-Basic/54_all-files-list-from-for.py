# Learn Python in Arabic #60 - قائمة ملفات من تكرار all files list from for Python
import os

allfiles = [f for f in os.listdir("myfiles")] 
for files in allfiles: print(files)

files2 = [ n for n in os.listdir("myfolder") if os.path.isfile("myfiles"+ n)]
for file in files2: print(file)