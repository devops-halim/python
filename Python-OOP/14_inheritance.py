# Learn Python in Arabic #106 - الوراثة inheritance in Python
# Learn Python in Arabic #107 - الوراثة عملي inheritance in Python
class person:
    name = 'peson'
    address = 'UAE'
    def printdata(self):
        print (self.name + ';' + self.address)

class employee(person):
    pass

emp1 = employee()
print(emp1.name)
print(emp1.address)
print('=================')

emp1.printdata()