#Juego de adivinar número

import random

def generar_numero():
    return random.randint(1,10)

def verificar_numero(numero_secreto, intento):
        if intento > numero_secreto:
            print("El intento es mayor que el número.")
            return False
        elif intento < numero_secreto:
            print("El intento es menor que el número.")
            return False
        else:
             print("Correcto")
             return True

print("Bienvenido al juego.")

numero_secreto = generar_numero()
acertado = False



while not acertado:
     intento = int(input("Ingrese un número: "))
     acertado = verificar_numero(numero_secreto, intento)