# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
# Concatenación

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30 # ACORDATE QUE len(lista) es un número siempre y se puede operar con el


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# EJERCICIO OPCIONAL




#ejercicio 1 
# list  = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# print(list [7 : 14])

# #ejercicio 2 
# # Ejercicio 2: Intercambio de posiciones
# # Dada la siguiente lista:
# # numeros = [10, 20, 30, 40, 50]
# # Intercambia la primera y la última posición de la lista.

# numeros = [10, 20, 30, 40, 50]
# numeros[0], numeros[-1] = numeros[-1], numeros[0]


# # Otra forma de hacerlo
# primer_numero = numeros[0]
# ultimo_numero = numeros[-1]

# numeros[0] = ultimo_numero
# numeros[-1] = primer_numero

# print(numeros)  

# ejercicio 3
# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
# Concatenación
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
# print(sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista = [1, 2, 3]
lista1 = lista + [1, 2, 3]
# print(lista1)

# ejercicios 5
# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30 # ACORDATE QUE len(lista) es un número siempre y se puede operar con el
# lista = [10, 20, 30, 40, 50, 60, 70]
# elemento = lista.remove(30)
# print(lista)

# Otra forma de hacerlo es 
# lista = [10, 20, 30, 40, 50, 60, 70, 80]
# centro = len(lista) // 2
# print(lista[centro])

# ejercicio opcional

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# EJERCICIO OPCIONAL
lista = [1, 2, 3, 4, 5, 6] 
lista.reverse()
# print(lista)

# Otra forma de hacerlo
lista = [1, 2, 3, 4, 5, 6, 7, 8] 
centro = len(lista) // 2



primera_mitad = lista[0:centro]
segunda_mitad = lista[centro:]

primera_mitad.reverse()
# O sino
# primera_mitad = primera_mitad[desde:hasta:-1 pasos (si pasas -1 invierte el orden)]

print(primera_mitad + segunda_mitad)
# O sino en una sola linea sin guardar en variables las mitades es asi
print(lista[0:centro][::-1] + lista[centro:])