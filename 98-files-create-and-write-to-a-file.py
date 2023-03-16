from os import system
system('cls')


file_builder = open("logger.txt", "w+")
# la función open() crea o accede a un archivo.
# El primer argumento es el nombre del fichero, el segundo indica los permisos que
# tiene. En este caso 'w+' indica permiso de escritura.  


for i in range(900):
    if i< 900-1:
        file_builder.write(f"I'm on line {i + 1}\n")
    else:
        file_builder.write(f"I'm on line {i + 1}")


file_builder.write("\nHey, I'm in a file!")  # escribe en el fichero indicado en el
                                             # objeto. Sobreescribe lo que hubiera.

file_builder.close()    #cierra el fichero