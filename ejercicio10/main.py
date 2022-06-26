tabla = []
for inicio_fila in range(1,6):
	fila = []
	for inicio_columna in range(1,6):
		fila.append(int(input("Introduce el número de la fila %d y columna %d:" % (inicio_fila,inicio_columna))))
	tabla.append(fila)

inicio_fila = 1
for fila in tabla:
	print("La suma de los elementos de la fila %d es %d" % (inicio_fila,sum(fila)))
	inicio_fila += 1

for inicio_columna in range(1,6):
	suma = 0
	for fila in tabla:
		suma = suma + fila[inicio_columna - 1]
	print("La suma de los elementos de la columna %d es %d" % (inicio_columna,suma))

