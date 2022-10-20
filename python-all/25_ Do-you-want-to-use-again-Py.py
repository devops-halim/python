# Learn Python in Arabic #30 - هل تريد استخدام البرنامج مرة اخري Do you want to use again Py
num1 = int (input("Enter number 1: ") )
num2 = int (input("Enter number 2: ") )
r = num1 + num2
print (r)
print ("###################################################")
weiderholen = "y"
while weiderholen == "y":
    num1 = int (input("Enter number 1: ") )
    num2 = int (input("Enter number 2: ") )
    r = num1 + num2
    print (r)
    weiderholen = input ("Programm weiderholen (y/n)")
    