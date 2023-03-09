# Learn Python in Arabic #113 - خصائص الكلاس base Built In Attributes in Python
class person:
    name = ''
    addess = ''
class employee (person):
    pass

class doctor(employee):
    pass

print( employee.__base__)
print( doctor.__base__)
print (person.__base__)