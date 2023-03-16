import os
os.system('cls')

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag in tags:
    print(str(tag) + ': ' + tag.render())
   

for tag in tags:
    print(tag.render())


# pruebas
class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")
    
    # esto es una Clase abstracta. Lo que está indicando es que en otra u otras
    # clases hijas (Child Classes) se definirá las funciones inidicadas
    # en este caso render() .
    # Con ello conseguimos que las ChildClasses soliciten los argumentos y no haga
    # falta duplicar códigos para la obtención de los mismos.  


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags_2 = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag_2 in tags_2:
    print(str(tag_2) + ': ' + tag_2.render())
   

for tag_2 in tags_2:
    print(tag_2.render())