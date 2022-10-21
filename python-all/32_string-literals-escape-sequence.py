# Learn Python in Arabic #37 - السلاسل النصية string literals escape sequence Python

str1 = "\N{copyright sign}\n"
print (str1)
str2 = "\N{registered sign}"
print (str2)
str3 = "\N{up down arrow}"
str4 ="\N{left right arrow}"
print (str3 , str4)
str5 = "\x50" #--> 2 input araic hanat 8 bit
str6 = "\u0042" # --> 16 bit
str7 = "\U00000056" # --> 32 bit
print(str5, str6 , str7)
