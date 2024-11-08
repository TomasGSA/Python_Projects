import bs4
from bs4 import BeautifulSoup
import requests

# Crear URL sin numero de pagina

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrella
titulos = []

# Iteracion de paginas

for pagina in range(1, 51):

    # Crear sopa en cada pagina
    url_pagina= url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml-xml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:

         # Chequear estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # Guardar titulo
            titulo_libro = libro.select('a')[1]['title']

            # Agrerar libro a la lista
            titulos.append(titulo_libro)

# Mostrar los libros
for t in titulos:
    print(t)