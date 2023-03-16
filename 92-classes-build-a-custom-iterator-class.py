from os import system
system('cls')

class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):   # esta función nos permite crear el índice inicial
        self.n = 0        # en este caso self.n. Siempre retorna self.
        return self       #  

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:  # Si es el último índice
            player = self.get_player(self.n)    # devolvemos el último valor 
            self.n = 0                          # y reiniciamos el índice 
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)  # instanciamos la clase
process = iter(astros_lineup)   # iniciamos iter para iniciar la variable
                                # de iteración
                                  
print(next(process))            # solicita el valor actual y avanza al siguiente.
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))