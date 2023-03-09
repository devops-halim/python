# Learn Python in Arabic #102 - اضافة خصائص في كلاس setattr attribute in Python
class emp:
    pass

emp1=emp()
setattr(emp1,'name','test')
setattr(emp1,'city','jena')
setattr(emp1,'gehalt','1600')
print(emp1.name)
print(emp1.city)
print(emp1.gehalt)
