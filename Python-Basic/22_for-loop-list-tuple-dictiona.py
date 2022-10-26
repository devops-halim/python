# Learn Python in Arabic #27 - تكرار القوائم و الصفوف و القاموس for loop list tuple dictiona
from math import fabs


names = ["ame", "ahmad ", "adel","murat", "halim" ]
for name in names:
    print ("hallo "+name)

l1 = [77,99,55,5,5.5,"hallo", True, False]
for v in l1:
    print (v)
    print (type(v ))
d1 = {"name":"Ahmad", "salary":2500, "city":"jena"}
for vv in d1:
    print(d1 [vv])