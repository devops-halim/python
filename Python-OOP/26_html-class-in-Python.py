class web:
    def create(self,body='',name='page'):
        file = open(name+'.html', 'w+')
        content = '''<!DOCTYPE html> 
<html> 
   <head> 
        <title> My page </title> 
    </head> 
    <body> 
        {my}
  </body> 
</html>
'''.format(my=body)
        file.write(content)
        file.close
        import webbrowser
        webbrowser.open_new_tab(name+'.html')
w = web()
w.create('<h1> hallo </h1>')
w.create('<h1> hallo 2 </h1>', 'page2')
w.create('<h1> hallo 3 </h1>', 'page3')
w.create('<h1> hallo 4 </h1>', 'page4')
w.create('<h1> hallo 5 </h1>', 'page5')
w.create('<h1> hallo 6 </h1>', 'page6')