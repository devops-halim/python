# Learn Python in Arabic #34 - الاستمرار في التكرار continue in loop Python


from itertools import count


count = int (input("Enter nummber: "))
mysum = 0
for x in range(count):
    num = int(input("Enter the number: "+ str(x+1) + ": "))
    if num ==0 : continue
    mysum += num
    print("sum OK")
print(mysum)