# Learn Python in Arabic #103 - خصائص في كلاس getattr attribute in Python
class emp:
    name='empty'
emp1 = emp()
print(getattr(emp1,'name'))

emp2=emp()
emp2.name= 'max muster'
print(getattr(emp2,'name'))

