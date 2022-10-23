# Learn Python in Arabic #49 - القراءة من الملف read readlines file r open Python
file = open("43_myfile.txt", "r")
print(file.readline())
text = file.read()
print(text)
file.seek(0)
mylines = file.readlines()
print(mylines)
