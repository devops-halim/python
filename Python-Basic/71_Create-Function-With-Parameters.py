# Learn Python in Arabic #77 - انشاء دالة بوسائط Create Function With Parameters Python
def hi(name) :
    print("Hallo " + name )

hi("halim")
hi("Rami")
hi("omar")

def add(num1,num2):
    print(num1 + num2)

add(7,7)

def calc(num1,num2,ope):
    if ope == '+':
        print(num1+num2)
    elif ope == '-':
        print(num1-num2)
    elif ope == '*':
        print(num1*num2)
    else:
         if num2 ==0:num2=1
         print(num1/num2)

calc(7,7,'+')  
calc(7,7,'-')
calc(7,7,'*')
calc(7,7,'/')  



