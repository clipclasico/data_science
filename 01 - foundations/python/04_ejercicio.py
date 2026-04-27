#Notas aprobadas y reprobadas

notas = []
aprobadas = []
reprobadas = []

aprob_cant = 0
reprob_cant = 0

suma_aprobadas = 0
suma_reprobadas = 0


for i in range(8):
    x = float(input(f"Ingrese nota {i+1} : "))
    notas.append(x)

for nota in notas:
    if nota >= 61:
        aprobadas.append(nota)
        aprob_cant += 1
        suma_aprobadas += nota
    else:
        reprobadas.append(nota)
        reprob_cant +=1
        suma_reprobadas += nota

if len(aprobadas) > 0:
    promedio_aprobado = suma_aprobadas/len(aprobadas)
else:
    promedio_aprobado = 0

if len(reprobadas) > 0:
    promedio_reprobado = suma_reprobadas/len(reprobadas)
else:
    promedio_reprobado = 0



print("Notas: ", notas)
print("Aprobadas: ", aprobadas)
print("Cantidad de aprobadas: ", aprob_cant)
print("Promedio aprobadas: ", promedio_aprobado)

print("Reprobadas: ", reprobadas)
print("Cantidad de reprobadas: ", reprob_cant)
print("Promedio reprobadas: ", promedio_reprobado)