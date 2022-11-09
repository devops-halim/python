# Learn Python in Arabic #70 - معالجة الأخطاء و الاستثناءات Errors Exceptions Python
try: 
    n1= [1,2,3]
    n1[3]= 8
except IndexError as sa:
    print(sa)
finally:
    print('END')
try:
    num1 = int (input("Enter nzumber 1: "))
    num2 = int (input("Enter nzumber 2: "))
    r = num1 / num2
    print(r)
except ZeroDivisionError as ex:
    print(ex)
except:
    print("ERRORR")