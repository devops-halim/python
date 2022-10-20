# Learn Python in Arabic #29 - تكرار القوائم و الصفوف و القاموس while loop list tuple dictio
myt = ("hallo", 55.77, True , "jena", False,2022)
x = 0
while x < len(myt):
    print(myt[x])
    x+=1
print ("___________________")
a = 0
myl = ["hallo", 55.77, True , "jena", False,2022]
a = 0
while a < len(myt):
    print(myt[a])
    a+=1
print ("___________________")
myD = {"name":"jans", "ghalt":2500, "stadt":"Gera"}
print (list (myD.keys()) [0])
mykeyes = list(myD.keys())
y=0
while y < len(myD):
    print (myD[mykeyes[y]])
    y+=1
