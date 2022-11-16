# Learn Python in Arabic #94 - دالة بناء الكلاس constructor init in class Python
class employee:
    emp_ID = 0
    emp_name = ''
    emp_adress = ''
    emp_gehalt = 0

    def getdata(self):
        return  str(self.emp_ID) + ';' + self.emp_name + ';' + self.emp_adress + ';' + str(self.emp_gehalt)
    def showdata(self):
        print(self.getdata())
    def __init__(self):
        print('New object from employee')

emp1 = employee()
emp2 = employee()
emp3 = employee()
emp4 = employee()
emp5 = employee()