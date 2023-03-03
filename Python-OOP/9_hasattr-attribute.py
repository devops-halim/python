# Learn Python in Arabic #101 - تحقق خصائص في كلاس hasattr attribute in Python
class emp():
    city= 'jena'
    my= ' '
    def test():
        pass
emp1 = emp()

print( hasattr(emp1,'my') )
print( hasattr(emp1,'name') )
print( hasattr(emp1,'test' ))
print( hasattr(emp1,'city') )