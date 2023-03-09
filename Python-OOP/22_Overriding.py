# Learn Python in Arabic #116 - اعادة الكتابة علي الدوال Overriding in Python
class person:
    def printtype(self):
        print('person')
class custmur(person):
    def printtype(self):
        print('Customer')
    pass
class employee(person):
    def printtype(self):
        print('employee')
    pass
class doctor (employee):
    def printtype(self):
        print('doctor')
    pass
p = person()
c = custmur()
e = employee()
d = doctor()

p.printtype()
c.printtype()
e.printtype()
d.printtype()