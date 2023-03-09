# Learn Python in Arabic #117 - اسم الكلاس class name in Python
class person :
    def printtype(self):
        print(self.__class__.__name__)
class cusromer(person):
    pass
class employee(person):
    pass
class doctor(employee):
    pass
p = person()
c = cusromer()
e = employee()
d = doctor()
p.printtype()
c.printtype()
e.printtype()
d.printtype()