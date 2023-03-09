class web:
    def create(self,body='',name='page'):
        file = open(name+'.html', 'w+')
        file.write('<!DOCTYPE html> \n')
        file.write('<html> \n')
        file.write('   <head> \n')
        file.write('        <title> My page </title> \n')
        file.write('    </head> \n')
        file.write('    <body> \n')
        file.write(body)
        file.write('    </body> \n')
        file.write('</html> \n')
        file.close
        import os
        os.system(name+'.html')
w = web()
w.create('<h1> hallo </h1>')
w.create('<h1> hallo 2 </h1>', 'page2')
w.create('<h1> hallo 3 </h1>', 'page3')
w.create('<h1> hallo 4 </h1>', 'page4')
w.create('<h1> hallo 5 </h1>', 'page5')
w.create('<h1> hallo 6 </h1>', 'page6')