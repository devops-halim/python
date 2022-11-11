print('Hallo')
print(True)

for x in range (1,11):
    print(x)

def add(num1 ,num2, ope):
    if ope =='+':
        print(num1 + num2)
    elif ope =='-':
         print(num1 - num2)
    elif ope =='*':
        print(num1 * num2)
    else:
        if num2==0:num2=1
        print(num1/num2)
