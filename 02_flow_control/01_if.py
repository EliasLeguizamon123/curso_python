### 
# 01 - Sentencias condicionales (if, elif, else)
# Permite ejecutar una secuencia de comandos dependiendo de una condición
# anidaciones mas complejas
###


# el if es una condicion, es un bloque de codigo que se ejecuta si la condicion es verdadera, si la condicion es falsa ese bloque no se ejecuta
# Si yo quisiera representar el if como un tipo de dato, seria un booleano

# es_mayor_de_edad = True

# if es_mayor_de_edad:
#     print("Soy mayor de edad")
# else:
#     print("Soy menor de edad")


# print("Elif es un bloque if que puede anidarse")

# edad = 18
# # Solamente se va a ejecutar la condicion >= 18
# if edad >= 18: 
#     print("Soy mayor de edad")
# elif edad >= 13:
#     print("Soy un adolescente")
# elif edad >= 10:
#     print("Soy un niño")
# else:
#     print("Soy un bebe")


# Esto es lo mismo pero a la vez es distinto por que se van a ejecutar todas las condiciones de mas abajo
# if edad >= 18: 
#     print("Soy mayor de edad")

# if edad >= 13:
#     print("Soy un adolescente")

# if edad >= 10:
#     print("Soy un niño")

# if edad >= 0:
#     print("Soy un bebe")



### 
# 01.2 - Operadores lógicos (and: todo, or: alguno, not: no)
# Permite ejecutar una secuencia de comandos dependiendo de dos condiciones
###


print("and: todas las condiciones deben ser verdaderas")

edad = 18
tengo_registro = False
nombre = "Juan"

# APIS => Rutas
if edad >= 18 and tengo_registro and nombre == "Juan":
    print("Puedo manejar")
else: 
    print("No puedo manejar")


# Ruta: Te devuelve todos los autos rojos que la patente empiecen con "A" y que el dueño tenga más de 25 años y que los numeros de la pantente sean de 10 dígitos


print("or: alguna de las condiciones debe ser verdadera")

edad = 15
tengo_registro = False
nombre = "Juan"

if edad >= 18 or tengo_registro or nombre == "Juan":
    print("Puedo manejar")
else:
    print("No puedo manejar")

print("not: la condicion debe ser falsa")

edad = None

if not edad:
    print("Es un usuario antiguo del sistema")
else:
    print("Les cobramos el impuesto a nuevo usuario")

llamada = None
operador = "Maty"

if not llamada and operador == "Maty":
    print("Bajarle el sueldo")


# not in => es un operador logico que devuelve True si un elemento no esta en una lista 


### 
# 01.3 - Operadores ternarios (?:)
# Permite ejecutar un bloque if en una sola linea
# {codigo si cumple la condicion} if {condicion} else {codigo si no cumple la condicion}
###

# es un if que se ejecuta en una sola linea



# es_mayor_de_edad = True if edad >= 18 else False


valor: str = input("saludame: ")

print(f"hola {valor}" if valor == "hola" else "adios")

cant_tikets = int(input("Ingresa cantidad de tiquetes: "))

print(f"Puedes comprar {cant_tikets} tiquetes") if type(cant_tikets) == int else print("No puedes comprar tiquetes")