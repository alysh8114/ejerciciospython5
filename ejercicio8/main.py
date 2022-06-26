nombres = []
edades = []

while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))
    if nombre == "*": break;

edad_max = max(edades)

print("Todos los alumnos mayores de edad")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)

print("Los alumnos mayores (los que tienen mas edad)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for nombre, edad in zip(nombres, edades):
    if edad == edad_max:
        print(nombre)