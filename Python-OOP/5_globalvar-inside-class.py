# Learn Python in Arabic #97 - متغيرات عامة global var inside class Python
x =0
class employee:
    emp_ID = 0
    emp_name = ''
    emp_adress = ''
    emp_gehalt = 0
   
    # def cahngx(self,num):
    #     global x
    #     x = num
    def __init__(self):
        global x
        x +=1
    def getdata(self):
        return  str(self.emp_ID) + ';' + self.emp_name + ';' + self.emp_adress + ';' + str(self.emp_gehalt)
    def showdata(self):
        print(self.getdata())
emp01 = employee()
emp02 = employee()
emp03 = employee()
emp04 = employee()


emp1=employee()
#emp1.cahngx(9)
print(x)