# Learn Python in Arabic #98 - دالة الهدم destructor object or del class Python
class test : 
    def __init__(self) :
        print (" new objeckt is created")
    def __del__(self):
        print("current object is delete")

t1 = test()
del t1