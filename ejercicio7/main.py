lista1 = []
lista2 = []
lista3 = []
for inicio in range(1,6):
	lista1.append(int(input("Introduce el elemento %d del valor1:" % inicio)))
for inicio in range(1,6):
	lista2.append(int(input("Introduce el elemento %d del valor2:" % inicio)))

for inicio in range(0,5):
	lista3.append(lista1[inicio] + lista2[inicio])

print("La suma de los valores son:")
for numero in lista3:
	print(numero," ",end="")

