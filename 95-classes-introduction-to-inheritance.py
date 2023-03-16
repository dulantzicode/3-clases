from os import system
system('cls')


class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens') #instancia en AdminUser

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
print(kristine.greeting())
#print(kristine.active_users()) # esta no funciona porque no tiene atributos de
                               # instancia en AdminUser (clase hija).
                               # Sin embargo, si tiene una instancia en AdminUser esta
                               # hereda (o comparte) los atrubutos a la clase padre y
                               # se pueden usar sus funciones. 