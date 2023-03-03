# Learn Python in Arabic #100 - اضافة خصائص سرية في كلاس secret attribute or method in class
class emp:
    __name ='empty'
    def __printname(self):
        print('Halllo '+self.__name)
    def printname(self):
        self.__printname()
    
e1 = emp()
#print(e1.name)
e1.printname()
#print(e1.name)