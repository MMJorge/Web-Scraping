import bs4
import requests
from urllib3 import request

# Crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
#lista de titulos con 4 o 5 estrellas
titulo_rating_alto = []

#Iterar paginas
for pagina in range(1,51):

    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:

        #chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #Guradar titulo en variable
            tirulo_libro = libro.select('a')[1]['title']

            #Agregar libro a la lista
            titulo_rating_alto.append(tirulo_libro)

#Ver los libros de 4 y 5 estrellas en consola
for t in titulo_rating_alto:
    print(t)