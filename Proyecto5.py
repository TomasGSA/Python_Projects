from random import choice

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def eligir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñoprstwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has eligido una letra correcta")
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_ocualta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_ocualta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_ocualta and letra_elegida in letras_correctas:
        print("Ya has encontrado esta letra, intenta con otra letra")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_ocualta)

    return vidas, fin, coincidencias

def perder():
    print(f"""Te has quedado sin vidas
              La palabra era {palabra}""")

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print(f"""Felicitaciones, has encontrado la palabra !!!""")
    return True


palabra, letras_unicas = eligir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print(f"letras incorrectas: " + '-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado



