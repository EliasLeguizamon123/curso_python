###
# Ejercicio 1
# Quiero crear una calculadora
# Para esto necesito que primero me preguntes el tipo de operacion que quiero realizar
# (suma, resta, multiplicacion, división)
# Luego me pregunte el primer numero
# Luego me pregunte el segundo numero
# Por ultimo quiero que me muestres el resultado de la operación
# Ejemplo:
# Suma 10 y 10
# Resultado: 20
# Suma 10 y 5
# Resultado: 15
# OPcional: Quiero que tengas en cuenta si yo paso tipos incorrectos a la calculadora (str) ERROR: No podes operar con un string. arr, tupla, dict 
# Respuesta del error: El tipo de dato {type} es incorrecto 
###

# 1- funcion principal que pregunta la operacion y los numeros y dependiendo de eso, esa funcion ejecuta suma, resta, multiplicacion o división

# Si se complica usar if else solamente hacer la suma


#utilize if y elif para poner las 4 condiciones y use el == para cada operacion y cree la variable resultado
#agregue la opcion de que imprima un saludo al final



# ================= respuesta ================

# Tengo dudas como poner si es un str y dar la respuesta.

# operacion = input("Elige una operación (+, -, *, /): ")
# num1 = int (input("Ingresa el primer número: "))
# num2 = int (input("Ingresa el segundo número: "))

# if operacion == '+':
#     resultado = num1 + num2
#     print(f"El resultado es: {resultado}")

# elif operacion == '-':
#     resultado = num1 - num2
#     print(f"El resultado es: {resultado}")

# elif operacion == '*':
#     resultado = num1 * num2
#     print(f"El resultado es: {resultado}")

# elif operacion == '/':
#     resultado = num1 / num2
#     print(f"El resultado es: {resultado}")

# nombre = input("Ingrese nombre: ")
# print("Muchas gracias por todo " + nombre)



# ================= respuesta mejorada ================


# Una funcion auxiliar hace solamente una cosa, no hace mas que una cosa criterios S.O.L.I.D   S: Single responsibility principle
def calcular(operacion, num1, num2):
    """
    Calcular el resultado de una operación
    :param operacion: operación a realizar
    :param num1: primer número
    :param num2: segundo número
    :return: resultado de la operación
    """
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        return num1 / num2
    else:
        return None # TODO: Explicar por que no se devuelve nada

operacion = input("Elige una operación (+, -, *, /): ")

if operacion not in ['+', '-', '*', '/']:
    print("Opcion incorrecta")
    exit()

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

resultado = calcular(operacion, int(num1), int(num2))

print(f"El resultado es: {resultado}")
