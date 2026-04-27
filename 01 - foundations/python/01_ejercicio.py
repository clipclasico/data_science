#Notas de un estudiante - Práctica de listas

notas = []

nota1 = float(input("Ingrese la nota 1: "))
notas.append(nota1)

nota2 = float(input("Ingrese la nota 2: "))
notas.append(nota2)

nota3 = float(input("Ingrese la nota 3: "))
notas.append(nota3)

nota4 = float(input("Ingrese la nota 4: "))
notas.append(nota4)

nota5 = float(input("Ingrese la nota 5: "))
notas.append(nota5)

print(notas)

sum = 0

for nota in notas:
    sum += nota

prom = sum/len(notas)
print(prom)

print(max(notas))
print(min(notas))

