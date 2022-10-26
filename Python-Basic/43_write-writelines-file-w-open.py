# Learn Python in Arabic #48 - الكتابة علي الملف write writelines file w open Python
file = open("43_myfile.txt", "w")
file.write("Hallo germany\n")
file.write("how old are you\n")

names = ["max\n","muster\n","adm\n", "jul\n", "ali"]
file.writelines(names)
file.close

