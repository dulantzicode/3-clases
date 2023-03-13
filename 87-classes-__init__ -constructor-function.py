from os import system
system('cls')


# La función __init__ se ejecuta siempre que se instancie la clase.


class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())




# Coding Exercise
# Using our Garage class from the previous guide, add a constructor method
# that builds a property named size, which will represent how many cars 
# will fit in the garage as an integer. 
# Instantiate the home object to be a 2 car garage.

class Garage:
  def __init__(self, size):   # Add your constructor here
    self.size = size
    

  def open_door(self):
    return f'Caben {self.size} coches dentro'
    return "The door opens"
    
home = Garage(5)   # instantiate with a garage size here
print (home.open_door())