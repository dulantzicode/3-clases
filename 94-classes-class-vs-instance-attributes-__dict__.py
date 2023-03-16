from os import system
system('cls')


class Website:
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)

# El método __dict__ convierte el valor en un diccionario que tiene como key los 
# nombres de los argumentos, y como valores los valores de los argumentos.
# En este caso solo hay un argumento



class DifferentWebsite:
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)

# Los atributos de las instancias son propios de cada instancia.
# Los atributos de una clase son iguales para todas las instancias,
# y no podemos acceder a ellos de la misma forma que a los de las instancias.
# por ejemplo, si accedemos al argumento title sí funciona
print(dw_two.title)
# Pero si intentamos hacer un __dict__ solo devolverá un diccionario vacío
print(dw_two.__dict__)