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