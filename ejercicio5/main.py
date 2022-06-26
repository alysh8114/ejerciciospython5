import random
lista = []
for inicio in range(1,11):
	lista.append(random.randint(1,10))

lista.sort()

for numeros in lista:
	print(numeros," ",end="")
