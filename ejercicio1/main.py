import random
lista_valores = []

for indice in range(1,11):
	lista_valores.append(random.randint(1,10))

for numero in lista_valores:
	print(numero," ",numero ** 2," ",numero ** 3)

