from os import system
system('cls')


def pretty_price(price, margin):
    if margin > 0.99:
        margin = margin/100

    return int(price) + margin





print (pretty_price(5.5, 98))

print (pretty_price(100.01 , .99))

print (pretty_price(53.1, 95))



# Profe
def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        # este método comprueba si el primer argumento es una instancia del segundo
        # en este caso comprueba si extension es un valor de tipo 'int' 
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))



#variante
def pretty_price(gross_price, extension):
    if isinstance(extension, float):
        extension = extension
    else:
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))