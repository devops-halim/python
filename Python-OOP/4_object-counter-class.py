# Learn Python in Arabic #96 - عداد الكائن object counter class Python
from itertools import count
class employee:
    objectscount = count(0)
    index = 0
    emp_ID = 0
    emp_name = ''
    emp_adress = ''
    emp_gehalt = 0
    def __init__(self) :
        self.index = next(self.objectscount)

    def getdata(self):
        return  str(self.emp_ID) + ';' + self.emp_name + ';' + self.emp_adress + ';' + str(self.emp_gehalt)
    def showdata(self):
        print(self.getdata())
emp1= employee()
emp2= employee()
emp3= employee()
emp4= employee()
emp5= employee()
print (emp1.index) 
print (emp2.index)
print (emp3.index)
print (emp4.index)
print (emp5.index)

print(emp1.objectscount)


