# Learn Python in Arabic #111 - خصائص الكلاس name Built In Attributes in Python
class employee:
    'This is employee class Testing '
    name = 'emty name'
    address = 'empty address '

class doctor :
    pass
class computer:
    class hard:
        pass
emp = employee()
print (employee.__name__)
#print(emp.__name__)
print (doctor.__name__)
print (computer.__name__)
print (computer.hard.__name__)