# Learn Python in Arabic #75 - قراءة ملفات csv comma separated value csv Python
import csv


f = open('69.csv')
read = csv.reader(f) # read from the csv file
gruop1 = next(read)
print('g1 ', gruop1)
gruop2 = next(read)
print('g2', gruop2)
gruop3 = next(read)
print('g3', gruop3)
f.close()


