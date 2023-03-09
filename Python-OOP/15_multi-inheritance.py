# Learn Python in Arabic #108 - الوراثة المتعددة multi inheritance in Python
class otherdata:
    email='example@ex.cpm'
    phone = '12345678910'

class person:
    name = 'peson'
    address = 'UAE'
    def printdata(self):
        print (self.name + ';' + self.address)

class employee(person,otherdata):
    pass

emp1 = employee()
print(emp1.name)
print(emp1.address)
print('=================')

emp1.printdata()
print('=================')
print (emp1.email)
print(emp1.phone)