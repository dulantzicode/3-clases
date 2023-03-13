from os import system
system('cls')

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"
  # el método 'repr' hace, básicamente lo mismo que el métod 'str'
  # si bien 'str' se usa para devover cadena más "elegantes", mientras
  # que 'repr' se usa para devolver datos menos procesados.
  # Su uso básico suele ser en el debugging para comprobar los datos
  # que están enviando una API o así.    


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))