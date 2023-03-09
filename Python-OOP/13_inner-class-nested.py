# Learn Python in Arabic #105 - كلاس متداخل inner class nested in Python
class computer:
    name ='pc'
    generation = 5
    class hard:
        name ='hard'
        capacity = 0
        speed = 0
    class ram :
        name = 'ram'
        ramtype = 'ram'
        size =0

r1 = computer.ram()
print (r1.name)
com1 = computer()
print (com1.name)
print (com1.ram.ramtype)
print(com1.hard.name)
