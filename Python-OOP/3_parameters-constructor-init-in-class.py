# Learn Python in Arabic #95 - دالة بناء بوسائط parameters constructor init in class Pyt

class employee:
    emp_ID = 0
    emp_name = ''
    emp_adress = ''
    emp_gehalt = 0

    def __init__(self,empID,empname,  empadress, empgehalt ):
        self.emp_ID = empID
        self.emp_name = empname
        self.emp_adress = empadress
        self.emp_gehalt = empgehalt
        

    def getdata(self):
        return  str(self.emp_ID) + ';' + self.emp_name + ';' + self.emp_adress + ';' + str(self.emp_gehalt)
    def showdata(self):
        print(self.getdata())
emp1= employee(10101,'halim','jena',900)
emp1.showdata()
    