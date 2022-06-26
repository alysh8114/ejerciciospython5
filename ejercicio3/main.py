notas = []
for inicio in range(1,6):
	while True:
		nota = int(input("Introduce la nota %d:" % inicio))
		if nota>=0 and nota<=10: break
	notas.append(nota)

print("Resultado de notas: ",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("La nota media: ",sum(notas)/len(notas))
print("La nota más alta: ",max(notas))
print("La nota menor: ",min(notas))