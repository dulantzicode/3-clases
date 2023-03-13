from os import system
system('cls')


class Invoice:

    def __init__(self, client, total):
        self._client = client 
        self._total = total  # por convención se añade un '_' al inicio de la
                             # variable considerada protegida
                             # en el caso de una variable (atributo) que deba ser
                             # privada (no se deba puede acceder desde fuera de la clase, 
                             # o incluso una clase hija), entonces se indica poniendo 
                             # dos '__' antes del nombre de la variable. 
                             # _cliente indicaría que se trata de un atributo que
                             #  no se debe modificar 
                             # __cliente indicaría que, además, es privado. 


    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property                # @property permite crear un decorator
    def client(self):        # esto consiste en una función con el nombre
        return self._client  # de la variable a recuperar que retorna la variable
                             # protegida. 

    @property
    def total(self):
        return self._total
    
    @client.setter              # @nombre_variable.setter permite crear un setter 
    def client(self, client):   # para esa variable protegida. De esta forma se puede 
        self._client = client   # sobreescribir un valor desde fuera de la clase.


google = Invoice('Google', 100)
print(google.formatter())
print(google.client)

google.client = 'Yahoo'

print(google.client)



# Coding Exercise
# We want to ensure that our 'size' attribute can be retrieved,
# but not 'set'. Use the appropriate syntax to protect the size attribute.
# Then, use the 'property' decorator to build a getter to return the protected data.
# You do not need to instantiate the class.

class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size
    self.cars = []

  @property  # add decorator here
  def size(self):
    return self._size

  def open_door(self):
    return "The door opens"
