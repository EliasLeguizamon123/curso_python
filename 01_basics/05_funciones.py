###
# 05 - Funciones 
# Las funciones son bloques de codigo que se pueden reutilizar 
### 

def decir_hola():
    print("Hola")
print("hola")

decir_hola()

# Definir una funcion no es lo mismo que llamarla, en el codigo que tenemos mas arriba se ejecuta primero el print que esta DESPUES
# de la funcion y despues la funcion por que se la invoca despues del segundo print

# Podes definir funciones que reciban parametros

# decir_hola("Matias") 


def decir_hola_con_nombre(nombre: str):
    print(f"Hola {nombre}")

# Cuando yo paso un argumento a una funcion, puedo definir previamente de que tipo es el argumento

decir_hola_con_nombre("Matias")
decir_hola_con_nombre(nombre="Matias")

decir_hola_con_nombre(123)

# TODO: explicar returns, errores de returns, etc.