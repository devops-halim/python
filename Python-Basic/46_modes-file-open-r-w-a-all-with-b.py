# Learn Python in Arabic #52 - انماط تعامل الملفات modes file open r w a all with b Python
f1 = open("filename.txt","r") # read only musst the file exeit
f2 = open("filename.txt","w") # only write in a file
f3 = open("filename.txt","r+") # read and write and muuste the file ist exeict
f4 = open("filename.txt","w+") # write and read 
f5 = open("filename.txt","a") # over write on file
f2 = open("filename.txt","a+") # read and overwrite

fb1 = open("filename.txt","rb") # bainary read only musst the file exeit
fb2 = open("filename.txt","wb") # bainary only write in a file
fb3 = open("filename.txt","rb+") # bainary read and write and muuste the file ist exeict
fb4 = open("filename.txt","wb+") # bainary write and read 
fb5 = open("filename.txt","ab") # bainary over write on file
fb2 = open("filename.txt","ab+") # bainary read and overwrite