###
# 01 - Bucles (while)
# Permiten ejecutar un bucle de codigo repetidamente mientras se cumpla una condicion
###


# Bucle con una simple condicion
contador = 0
# while contador <= 10:
#     print(contador)
    # contador += 1 # Esta parte es super importante por que sino el bucle seria infinito

# Salir del bucle con la palabra reservada break

# while True:
#     contador += 1
#     print(contador)

#     if contador >= 10:
#         break

# while contador <= 10:
#     print(contador)
#     contador += 1
#     if contador % 2 == 0:
#         print(f"{contador} Es Par")
#         break



# Saltar una iteracion con la palabra reservada continue
# continue no deja que el codigo que esta debajo se ejecute si se cumple la condicion

# while contador <= 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     # Esto que esta aca abajo no se va a ejecutar NUNCA si el contador cumple la condicion
#     print(contador)


# Bucle con else
# Cuando se ejecuta el else dentro de un while ? 
# while contador <= 10:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break
# else: # El else NO se ejecuta si el bucle se rompe con break
#     print("El bucle termino correctamente")



# Pedirle al usuario un numero que tiene que ser positivo, sino volve a pedirselo



# while True:
#     numero = int(input("Ingresa un numero que sea positivo: "))
#     if numero > 0:
#         print("Gracias")
#         break
#     else:
#         print("El numero no es positivo, intenta de nuevo")



# Try Except en bucles while

while True:
    try:
        numero = int(input("Ingresa un numero: "))
        if numero > 0:
            print("Gracias")
            break
        else:
            print("El numero no es positivo, intenta de nuevo")
    except:
        print("Error: Debes ingresar un numero")