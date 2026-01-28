###
# 03 - Listas
# Pueden contener elementos de diferentes tipos
### 

# Arrays.

lista = [1, 2, 3, 4, 5]

lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]

lista3 = ["uno", 2, 1.2, True, None]

lista4: list[str] = ["banana", "apple", "orange"]

lista5 = [[1, [1, [1, [1, 2]]]], [3, 4], [5, 6]] # se define como matriz  


# Acceso a elementos por indice

# print(lista[0]) # 1
# print(lista2[1]) # dos
# print(lista3[4]) # 1.2
# print(lista5[0][1][1][1][0])

# Slicing (rebanado) de listas
 
lista = [1, 2, 3, 4, 5]


# Hay mas magia todavia ( [desde:hasta:paso]) 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(lista[0:10:2]) # [1, 3, 5, 7, 9]
# print(lista[1:10:2]) # [2, 4, 6, 8, 10]
# print(lista[2:10:2]) # [3, 5, 7, 9]

# print(lista[::-1])

# Modificar una lista

# Modificar 1 solo elemento

lista = [1, 2, 3, 4, 5]

lista[0] = 190

print(lista)


# Agregar elementos

lista = [1, 2, 3, 4, 5]

lista1 = lista + [6, 7, 8, 9, 10]

print(lista1)

# Pero es todavia mejor y mas eficiente hacer esto

lista = [1, 2, 3, 4, 5]
lista += [6, 7, 8, 9, 10]
print(lista)

# Esto es lo mismo pero mejor por que no se crea una nueva lista

# Hay otros metodos de listas que son un poco mas complejos pero que son param listas inmutables

lista = [1, 2, 3, 4, 5]

# Agregar
lista.append(6)

print(lista)

# Sacar
elemento = lista.pop()

print(elemento)
print(lista)

# Otros metodos que tienen las listas

len("hola") # 5
len(lista) # Devuelve la cantidad de elementos de una lista en int
max(lista) # Devuelve el mayor elemento de una lista
min(lista) # Devuelve el menor elemento de una lista
sum(lista) # Devuelve la suma de todos los elementos de una lista

# Agregar un elemento en el indice que vos quieras (indice, elemento)
lista.insert(0, 190)
lista.insert(2, 19)
print(lista)

# remover un elemento en el indice que vos quieras (indice)

elemento = lista.remove(190)

print(lista)

# eliminar todos los elementos que tenga una lista

# lista.clear()

# print(lista)

# Dar vuelta una lista

lista.reverse()

print(lista)
