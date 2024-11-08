from numeros import *


def preguntar():
    print("Bienvenido a la farmacia")

    while True:
        print("[F] - Farmacia\n[P] - Perfumeria\n[C] - Cosmeticos")

        try:
            rubro = input("Seleccione una opcion: ").upper()
            ["P", "F", "C"].index(rubro)
        except ValueError:
            print("Esa opción no es valida")
        else:
            break

    mensaje(rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["P", "F", "C"].index(otro_turno)
        except ValueError:
            print("Esa opción no es valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
