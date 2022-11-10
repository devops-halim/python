# Learn Python in Arabic #79 - انشاء دالة ترجع قيم Create Function has return Python
def hi(name):
    return "Hallo " + name

h1 = hi("ali")
h2 = hi("Halim")

print(h1)
print(h2)

def add(num1 ,num2, ope):

    r = 0
    if ope =='+':
        r = num1 + num2
    elif ope =='-':
        r = num1 - num2
    elif ope =='*':
        r = num1 * num2
    else:
        if num2==0:num2=1
        r = num1/num2
    return r
r1= add(7,7,'+')
r2= add(7,7,'-')
r3= add(7,7,'*')
r4= add(7,7,'/')

print(r1)
print(r2)
print(r3)
print(r4)