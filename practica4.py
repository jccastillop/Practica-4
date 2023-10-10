#Ejercicio de clase

cantidad = int(input("\nCuantos estudiantes desea ingresar:\n"))

#Este diccionario almacena los resultados academicos

resultado = {}

for i in range(0, cantidad):
    print("\n----------------------Datos---------------------\n")
    print('Ingresando datos del estudiante: ')
    nombre = input("Ingresa el nombre del estudiante numero {0}° ".format(i))
    notas=[]

    for j in range(0, 3):
        nota = float(input("Ingresa la nota {0} ".format(j+1)))
        notas.append(nota)

    resultado.setdefault(nombre,notas)

print(resultado)

print("\n----------Fin de los datos--------------\n")

for nombre, notas in resultado.items():
    print("-"*50)
    fila = nombre.ljust(10)
    for nota in notas:
        fila += "| "+str(nota).ljust(10)

    print(fila)

fila += "| "+str(round((sum(notas) / len(notas)), 2)).ljust(10)
print(fila)