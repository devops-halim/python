# Learn Python in Arabic #115 - خصائص الكلاس bases Built In Attributes in Python
class other:
    pass
class otherdata:
    email= ''
    phonr= ''
class person:
    name = ''
    address = ''
class employee(person, otherdata,other):
    empid = 0
class doctor(employee) :
    pass

print ( otherdata.__bases__ )
print(employee.__bases__)
print(doctor.__bases__)