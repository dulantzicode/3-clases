from os import system
system('cls')

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]  # similar a un return, pero no corta la función.
            idx += 1                     # solo la detiene y si es llamada
                                         # de nuevo continúa donde lo dejó, por eso 
                                         # continúa dentro del bucle while y el 
                                         # incremento del índice está fuera del bucle
                                         # if y del yield. De esta forma no es necesario
                                         # volver a llamar al método, sino solo hacer next.
                                         # El valor devuelto no se almacena en memoria

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"
    

    


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

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup)) # se usa la función __next__ del núcleo
print(next(astros_lineup)) # al usar yield no hace falta definirla.
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))