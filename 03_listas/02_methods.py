###
# 02 - Repaso y utilidades extra sobre listas
### 

# cuantas veces aparece un elemento
lista = [10, 199, 2026, 10, 4, 854]
lista1 = ["manzana", "pera", "uva", "naranja", "banana", "Pera", "Manzana"]
lista_tarjetas = ["Visa", "Mastercard", "American Express", "Discover", "Mercado Pago"]

print(lista.count(10))

# comprueba si existe x en una lista
if "pera" in lista1:
    print("pera si esta en la lista")

# Ordenamiento de listas sort y sorted

# Por defecto ordena de menor a mayor
lista.sort()
print(lista)

# No devuelve nada, solamente modifica la lista original

# Si queres devolver el ordenamiento usas sorted()
lista_ordenada = sorted(lista)
# print(lista_ordenada)


# Si vos queres definir como ordenar la lista usas el parametro key

lista1.sort()
# print(lista1)

# Entonces haces esto
lista1.sort(key=str.lower)
print(lista1)
