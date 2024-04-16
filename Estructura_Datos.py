'''
Created on 15 abr. 2024

@author: Joan Sanchez
'''
"""hay 4 tipos de estructuras, las listas, las tuplas, los dicccionarios
y los sets***

***las listas son estructuras de datos que permiten almacenar elementos
de manera ordenadas, mantienen el orden en el que son declarados y los 
elementos pueden repetirse sin problema"""

lenguajes = ["Python", "Java", "Golang"] 
print(lenguajes)

lista = [1, 2.0, True, "python", 1]
print(lista)

print (lenguajes[0])

print (lenguajes[2])

print(lenguajes[-1])

print(lenguajes[-3])

print(lenguajes[0:2])

#Podemos añadir otra lista dentro de una lista ya existentente, para ello:

programacion = [lenguajes,"Dedicacion", "Practica"]

print (programacion)

"""al haber otra lista dentro de la lista de programacion, para consultar los
dentro de programacion, debemos enfatisar que nos encontramos en la primera lista
y luego elegir la posicion del objeto al que queremos hacer mencion"""

print (programacion[0][0])

"""Si queremos reemplazar basta con colocar la posicion en la lista, y luego
asignar con un = el valor nuevo"""

lenguajes[0] = "Dart" 
print(lenguajes)

"""Si quieres añadir otro elemento a la lista, puedes usar la funcion .append 
esta opcion colocara en nuevo elemento al final de la lista"""

lenguajes.append("python")
print (lenguajes)

otros_lenguajes = ["C++", ".Net"]

"""con extend en lugar de añadir la lista completa, solo se añadiran los valores
dentro de la misma"""

lenguajes.extend(otros_lenguajes)

print (lenguajes)

lenguajes.append(otros_lenguajes)

print (lenguajes)


"""Las tuplas son basicamente listas que no se puede editar luego, a diferencia
de las listas, sus valores se deben colocar entre parentesis"""

lenguajes_tupla = ("java", "HTML", "Python")

print(lenguajes_tupla)

lenguajes_tupla[0] = "python" #da error por lo antes mecnionado
