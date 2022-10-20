# Learn Python in Arabic #33 - الخروج من التكرار break infinity loop Python
for x in range(1, 101):
    # if (x==97):
    #     break
    print (x)
    if (x==50):
        break
print("==============================")
s = 1
while True:
    print (s)
    s+=1
    if s>100:
        break
print("==============================")

from itertools import count
for a in count():
    print(a)
    if a == 500: 
        break