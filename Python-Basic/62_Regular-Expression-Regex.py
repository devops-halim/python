# Learn Python in Arabic #68 - التعبييرات القياسية Regular Expression Regex Python
# سي شارب C# REGULAR EXPRESSION IN A GENERAL #071

import re

test = input("Enter yourname:")
patt = "^[A-Z][a-z]+\s[a-z]+$"

v= re.match(patt,test)
print (v)
if v == None: print("NO")
else: print ("yes")