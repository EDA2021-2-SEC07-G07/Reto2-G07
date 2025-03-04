﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(catalog)
    loadAristas(catalog)


def loadBooks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    booksfile = cf.data_dir + 'Moma/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        model.addBook(catalog, book)

def loadAristas(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    booksfile = cf.data_dir + 'Moma/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        model.addArtistas(catalog, book)

# Funciones de ordenamiento

def sortantiguas(catalog,size):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.sortantiguas(catalog,size)
    return orden

def sortCantidades(catalog):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.sortCantidades(catalog)
    return orden

def SortAños(catalog):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.SortAños(catalog)
    return orden

def sortobras(catalog):
    """
    Ordena los artistas por nacimiento
    """
    orden = model.sortobras(catalog)
    return orden

# Funciones de consulta sobre el catálogo

def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo

def getBooksYear(catalog, year):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.getBooksByYear(catalog, year)
    return books

def primer_req(catalog, año1, año2):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.primer_req(catalog, año1, año2)
    return books

def segundo_req(catalog, fecha_inicial, fecha_final):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.segundo_req(catalog, fecha_inicial, fecha_final)
    return books

def tercer_req(catalog, artista):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.tercer_req(catalog, artista)
    return books

def quinto_req(catalog, departamento):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.quinto_req(catalog, departamento)
    return books

def cantidad_tecnicas(catalog):
    tecnicas = model.cantidad_tecnicas(catalog)
    return tecnicas

def funcion_prueba_req3(catalog, artista):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.funcion_prueba_req3(catalog, artista)
    return books


def cuarto_req(catalogo):
    orden = model.cuarto_req(catalogo)
    return orden

def cuarto_req_10Primeros(lista, catalogo):
    top = model.cuarto_req_10Primeros(lista, catalogo)
    return top

def primeros_ultimos(lista, catalogo):
    prim_ulti = model.primeros_ultimos(lista, catalogo)
    return prim_ulti