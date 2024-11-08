from random import *
nombre = input("Ingrese su nombre: ")
print(f"Buenas, {nombre} he pensado en un número entre 1 y 100.\nTienes ocho intentos para adivinar cúal es el número...")

print("Ya! tengo el número... Buena suerte!!!")
vidas = 8
numero_secreto = randint(1,100)
intentos = 0
eleccion = 0
while vidas > 0:
    eleccion = int(input("Tu elección: "))
    if eleccion < 1 or eleccion > 100:
        print("Has seleccionado un número que no esta permitido")
        vidas = vidas
        print(f"{nombre} tiene {vidas} intentos")
    elif eleccion < numero_secreto:
        print("El numero es menor al numero secreto...")
        intentos += 1
        vidas -= 1
        print(f"{nombre} tiene {vidas} intentos")
    elif eleccion > numero_secreto:
        print("Su eleccion es incorrecta. El numero es mayor al numero secreto...")
        intentos += 1
        vidas -= 1
        print(f"{nombre} tiene {vidas} intentos")
    elif eleccion == numero_secreto:
        print(f"Felicidades {nombre}! El número secreto es {numero_secreto}\nTe ha tomado la cantidad de {intentos} intentos")
        print("Adios...")
        break
if eleccion != numero_secreto:
    print(f"Lo siento {nombre} se han acabado los intentos, el numero secreto era {numero_secreto}")
