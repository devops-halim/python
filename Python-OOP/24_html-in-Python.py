# Learn Python in Arabic #118 - انشاء و تشغيل صفحة ويب html in Python
file = open('page.html', 'w+')
file.write('<!DOCTYPE html> \n')
file.write('<html> \n')
file.write('   <head> \n')
file.write('        <title> My page </title> \n')
file.write('    </head> \n')
file.write('    <body> \n')
file.write('        <h1 style = "background:navy;color:lightblue;">  \n')
file.write('            Welcmoe back the web from Python \n')
file.write('        </h1> \n')
file.write('    </body> \n')
file.write('</html> \n')



file.close
import os
os.system('page.html')