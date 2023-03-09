# Learn Python in Arabic #104 - حذف خصائص من كائن delattr attribute in Python
class emp:
    name = 'empty'

emp1=emp()
emp1.name = 'testing'
emp1.city='germany'
delattr(emp1,'name')
delattr(emp1,'city')

print(emp1.name)
#print(emp1.city)
