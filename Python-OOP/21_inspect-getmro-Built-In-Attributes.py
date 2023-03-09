# Learn Python in Arabic #114 - خصائص الكلاس inspect getmro Built In Attributes in Python
class other:
    pass
class person:
    pass
class employee(person, other):
    pass
#print(employee.__base__)
import inspect
print (inspect.getmro(employee))