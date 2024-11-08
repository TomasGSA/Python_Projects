from datetime import *
import os
import re
import time
from pathlib import Path
import math

inicio = time.time()

ruta = '/Users/tomasguerrero/Desktop/Python/pythonProject/Dia9/Proyecto+Dia+9/Mi_Gran_Directorio'

patron = r'N\D{3}-\d{5}'

fecha_actual = date.today()

num_encontrados = []

archivos_encontrados = []


def buscar_numeros(archivo, patron):
    abrir_file = open(archivo, 'r')
    texto = abrir_file.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numeros(Path(carpeta, a), patron)
            if resultado != '':
                num_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {fecha_actual.day}/{fecha_actual.month}/{fecha_actual.year}')
    print('\n')
    print("ARCHIVO\t\t\tNRO.SERIE")
    print("-------\t\t\t----------")
    for a in archivos_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encontrados: {len(num_encontrados)}')
    final = time.time()
    tiempo_final = final - inicio
    print(f'Duración de la busqueda: {math.ceil(tiempo_final)}')


crear_listas()
mostrar()
