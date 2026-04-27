#Parte 1
def saludar():
    print("Hola pibes")

saludar()

#Parte 2
def saludos(nombre):
    print(f"Hola {nombre}")

name = input("Ingresa tu nombre: ")
saludos(name)

#Parte 3
def calcular_cuadrado(numero):
    cuadrado = numero*numero
    return cuadrado


num = int(input("Ingresa un número: "))

resultado = calcular_cuadrado(num)
print(resultado)

#Parte 4
def calcular_promedio(notas):
    promedio = sum(notas)/len(notas)
    return promedio

notas = []
for i in range(5):
    nota = int(input(f"Ingrese nota {i+1}: "))

    notas.append(nota)

res = calcular_promedio(notas)
print(res)