lista1 = []
lista2 = []
for inicio in range(1, 6):
    lista1.append(input("Dame la cadena %s:" % inicio))

lista2 = lista1[::-1]

for cadena in lista2:
    print(cadena)