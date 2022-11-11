# Learn Python in Arabic #92 - انشاء كلاس مع الخصائص و الوظائف Create class attributes metho
# Learn Python in Arabic #93 - كائن من الكلاس Create instance object from class Python

class employee:
    emp_ID = 0
    emp_name = ''
    emp_adress = ''
    emp_gehalt = 0

    def getdata(self):
        return  str(self.emp_ID) + ';' + self.emp_name + ';' + self.emp_adress + ';' + str(self.emp_gehalt)
    def showdata(self):
        print(self.getdata())
emp1 = employee()
emp1.emp_ID = 10231
emp1.emp_name = 'halim'
emp1.emp_adress = 'jena'
emp1.emp_gehalt = 900
emp1.showdata()

emp2 = employee()
emp2.emp_ID = 1111
emp2.emp_name = 'omar'
emp2.emp_adress = 'syria'
emp2.emp_gehalt = 10000
emp2.showdata()

emp3 = employee()
emp3.emp_ID = 222220
emp3.emp_name = 'max'
emp3.emp_adress = 'Erfurt'
emp3.emp_gehalt = 1500
emp3.showdata()