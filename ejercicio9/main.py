temperaturas = []
for inicio in range(1, 6):
    temperatura = []
    temperatura.append(int(input("Día %d. Temperatura máxima:" % inicio)))
    temperatura.append(int(input("Día %d. Temperatura mínima:" % inicio)))
    temperaturas.append(temperatura)

print("Temperatura media de cada día")
print("===================")

inicio = 1
for temperatura in temperaturas:
    print("Día %d. Temperatura media: %f:" % (inicio, sum(temperatura) / len(temperatura)))
    inicio += 1

temp_min = temperaturas[0][1];
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]

print(" Los días con menos temperatura ")
print("==========================")
inicio = 1
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print("Día %d" % inicio)
    inicio += 1

existe_temperatura = False
print("Días con temperatura máxima")
print("===========================")
temp_max = int(input("Introduce una temperatura:"))
inicio = 1
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print("Día %d" % inicio)
        existe_temperatura = True
    inicio += 1
if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")

