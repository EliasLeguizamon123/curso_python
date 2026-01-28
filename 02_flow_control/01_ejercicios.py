###
# EJERCICIOS BLOQUE IF 
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# funciones, input, return, if, else 

# Ejercicio 2: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
# funciones, input, return, if, else 

# Ejercicio 3: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# ejercicio 3 : (tuve problemas)

def edades(edad):
    # Este tipo de validaciones es una buena forma de evitar que el usuario no haga algo que no deberia y siempre lo mejor es hacerlas al principio
    if edad < 0:
        return(f"Edad no válida (debe ser un número positivo).")

    if type(edad) != int:
        return(f"Edad no válida (debe ser un número).")

    # javascript
    # Try catch

    if edad >= 65:
        return(f"Eres un Adulto Mayor.")
    elif edad >= 18:
        return(f"Eres un Adulto.")
    elif edad >= 13: 
        return(f"Eres un Adolescente.")
    elif edad >= 3:
        return(f"Eres un Niño.")
    else:
        return(f"Eres un Bebé.")
        
    # if edad <= 2:
    #     return(f"Eres un Bebé.")
    # elif edad>3 <= 12:
    #     return(f"Eres un Niño.")
    # elif edad>=13<=17:
    #     return(f"Eres un Adolescente.")
    # elif edad <=18 <= 64:
    #     return(f"Eres un Adulto.")
    # elif edad >= 65:
    #     return(f"Eres un Adulto Mayor.")
    # else:
    #     print("Edad no válida (debe ser un número positivo).")

edad = int(input("Ingrese su edad "))

resultado = edades(edad)
print(resultado)






# 1 respuesta: 

# ejercicio 1 :

# def encontrar_mayor(num1, num2):
#     if num1 > num2:
#         return f"El número mayor es: {num1}"
#     elif num2 > num1:
#         return f"El número mayor es: {num2}"
#     else:
#         return "Ambos números son iguales"

# num1 = input("Introduce el primer número: ")
# num2 = input("Introduce el segundo número: ")

# resultado = encontrar_mayor(num1, num2)
# print(resultado)

# # ejercicio 2 :

# def año_bisiesto(año):
#     """
#     Agregaria validaciones de tipo de dato (int, float, etc), o de longitud de cadena 0000 - 9999 / 00 - 00
#     """
#     if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#         return f"El año es bisiesto"
#     else :
#         return f"el año no es bisiesto"

# año = int(input("Introduce el año: "))
# resultado = año_bisiesto(año)
# print(resultado)