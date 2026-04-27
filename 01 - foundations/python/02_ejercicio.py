#Temperaturas de la semana

temperaturas = []

for i in range(7):
    temp = float(input("Ingrese la temperatura del dia: "))
    temperaturas.append(temp)

print(temperaturas)

suma = 0

for tempe in temperaturas:
    suma += tempe

prom = suma/len(temperaturas)
print("el promedio es de: ", prom)

print("La temperatura más alta registrada es de: ", max(temperaturas))
print("La temperatura más baja registrada es de: ", min(temperaturas))


calurosos = 0

for dia in temperaturas:
    if dia > 30:
        calurosos += 1
        print(dia, "grados es Caluroso")
    else:
        print(dia, "grados es Fresquito")

print("días calurosos: ", calurosos)