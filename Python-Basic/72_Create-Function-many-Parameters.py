# Learn Python in Arabic #78 - انشاء دالة بوسائط لا نهائية Create Function many Parameters P

def hiall(*names):
    for name in names:
        print('Hallo ' + name)

hiall("max","muster", "Rami")