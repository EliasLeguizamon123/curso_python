# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

lista_original = [1, 2, 3]
copia1 = lista_original[ : ]
copia2 = lista_original.copy()
referencia = lista_original
referencia[0] = 10
print(f"lista original = {lista_original}")
print(f"{copia1}")
print(f"{copia2}")
print(f"Referencia = {referencia}")