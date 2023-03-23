from os import system
system('cls')

# Nota: doble __ se pronuncia Dunder

# los nombres de las classes comienzan con mayúscula
class Invoice:

  # Las funciones dentro de una clase necesitan como mínimo
  # un argumento (se usa self). Si hay más, self es el primero.
  def greeting(self):
    return 'Hi there'


inv_one = Invoice()        # se crea una instancia de la clase
print(inv_one.greeting())



# Coding Exercise
# Create a class named Garage. Add a method to the Garage class named open_door that returns a string (EX: "The door opens").
# Finally, instantiate a new object named home. You do not need to print anything.


class Garage:
  def open_door(self):
    return "The door opens"
  
home = Garage()
print (home.open_door())