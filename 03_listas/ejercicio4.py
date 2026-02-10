# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista =  [5, 2, 8, 1, 9, 4, 2]
lista.sort()
numero_2 = lista.count(2)
# numero_7 = 7 in lista 
print(lista)
print(f"el numero 2 aparece: {numero_2}" + " veces")
# print(f"esta el numero 7 : {numero_7}")

if 7 in lista:
    print("esta el numero 7")
else:
    print("no esta el numero 7")