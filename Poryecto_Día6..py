import os
from pathlib import Path
from os import system

# Definicion de ruta e impresión
mi_ruta = Path(Path.home(), "Recetas")
# informar al usuario cuantas recetas hay
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador
def inicio():
    system('clear')
    print('*'*50)
    print("Bienvenido al administraddor de recetas")
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en '{mi_ruta}")
    print(f"El total de recetas es: {contar_recetas(mi_ruta)}")
    print('*' * 50)
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print('''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoria
        [4] - Elimnar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()
    return int(eleccion_menu)
def volver_inicio():
    eleccion_volver = 'x'
    while eleccion_volver.lower() != 'v':
        eleccion_volver = input("\nPresione V para vovler al menú")

def mostrar_categorias(ruta):
    print("Categorias")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion = 'x'

    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista)+1):
        eleccion = input("\nElije una categoria: ")

    return lista[int(eleccion) - 1]

def mostrar_recetas(ruta):
    print("Recetas")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def elegir_receta(lista):
    eleccion = 'x'

    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input(f'\nElige una receta: ')

    return lista[int(eleccion) - 1]

def leer_receta(receta):
    print(Path(receta).read_text())

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada ')
        else:
            print("Lo siento, esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eleminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')

finalizar = False

while finalizar == False:
    menu = inicio()
    if menu == 1:
        # Mostrar categorias
        categorias = mostrar_categorias(mi_ruta)
        # Elegir categoria
        eleccion = elegir_categoria(categorias)
        # mostrar recetas
        mostrar = mostrar_recetas(eleccion)
        # Elegir recta
        receta_elegida = elegir_receta(mostrar)
        # leer receta
        leer_receta(receta_elegida)
        # volver al inicio
        volver_inicio()
        pass
    elif menu == 2:
        # Mostrar categorias
        categorias = mostrar_categorias(mi_ruta)
        # Elegir categoria
        eleccion = elegir_categoria(categorias)
        # Crear una receta
        crear_receta(eleccion)
        # volver al inicio
        volver_inicio()
        pass
    elif menu == 3:
        # crear una categoria
        crear_categoria(mi_ruta)
        # volver al inicio
        volver_inicio()
        pass
    elif menu == 4:
        # Mostrar categorias
        categorias = mostrar_categorias(mi_ruta)
        # Elegir categoria
        eleccion = elegir_categoria(categorias)
        # mostrar recetas
        mostrar = mostrar_recetas(eleccion)
        # Elegir recta
        receta_elegida = elegir_receta(mostrar)
        # eliminar receta
        eliminar_receta(receta_elegida)
        # volver al inicio
        volver_inicio()
        pass
    elif menu == 5:
        # Mostrar categorias
        categorias = mostrar_categorias(mi_ruta)
        # Elegir categoria
        eleccion = elegir_categoria(categorias)
        # eliminar categoria
        eleminar_categoria(eleccion)
        # volver al inicio
        volver_inicio()
        pass
    elif menu == 6:
        finalizar = True
        pass
