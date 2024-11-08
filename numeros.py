"""Este archivo está constituido por tres generadores, que se encargarn
de generar un numero y mostralos por pantalla cada vez que un
usuario lo solicite, todo esto, envuelto dentro de una funcion llamada
 mensje que se encarga de imprimir un mensaje indiferentemente de la seleccion
 """


def num_perfumeria():
    for n in range(1, 100):
        yield f"P - {n}"


def num_farmacia():
    for n in range(1, 100):
        yield f"F - {n}"


def num_cosmeticos():
    for n in range(1, 100):
        yield f"C - {n}"


p = num_perfumeria()
f = num_farmacia()
c = num_cosmeticos()


def mensaje(tipo):
    print("\nSu turno es: ")

    if tipo == "P":
        print(next(p))
    elif tipo == "F":
        print(next(f))
    else:
        print(next(c))

    print("\nAguarde y será atendido")
