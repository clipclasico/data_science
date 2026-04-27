# Top 3 notas

notas = []

for i in range(8):
    x = float(input("Ingrese la nota: "))
    notas.append(x)

print("Notas: ", notas)

notasordenadas = sorted(notas, reverse=True)

print("Top 3: ", notasordenadas[0:3])

print("Peores 3: ", notasordenadas[-3:])