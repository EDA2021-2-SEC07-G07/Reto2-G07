"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def print_obras_tecnica(author):
    """
    Imprime la información del autor seleccionado
    """
    if author:
        print("\n")
        for book in lt.iterator(author):
            print('Titulo: ' + book['Title'] + '  Medio: ' + book['Medium'] + '  Año: ' + book['Date'])
        print("\n")
    else:
        print('No se encontro el autor.\n')

def print_artistas(author):
    """
    Imprime la información del autor seleccionado
    """
    if author:
        print("\n")
        for artistas in lt.iterator(author):
            print('Nombre: ' + artistas['DisplayName'] + '  Nacio: ' + artistas['BeginDate']+ 
            '  Murio: ' + artistas['EndDate']+ '  Nacionalidad: ' + artistas['Nationality']
            + '  Genero: ' + artistas['Gender'])
        print("\n")
    else:
        print('No se encontro el autor.\n')

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Autores nacidos en un rango especififico")
    print("3- obras de un nacionalidada especifica")
    print("4- Obras por medio especifico")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time = time.process_time()
        print("Cargando información de los archivos ....")
        cont = controller.initCatalog()
        controller.loadData(cont)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)

    elif int(inputs[0]) == 2:
        año1 = input("Buscando libros del año?: ")
        año2 = input("Buscando libros del año?: ")
        respuesta = controller.primer_req(cont,año1,año2)
        print(('-'*5) + "Estos son los 3 primeros artistas del rango dado"+ ('-'*5))
        print_artistas(respuesta[0])
        print(('-'*5) + "Estos son los 3 ultimos artistas del rango dado"+ ('-'*5))
        print_artistas(respuesta[1])

    elif int(inputs[0]) == 3:
        start_time = time.process_time()
        año2 = input("Escriba la nacionalidad que desea concoer as obras totales: ")
        valores = controller.obras_nacionaloidad(cont,año2)
        print('la cantidad de obras de esta nacionalidad es de: ' + str(valores))
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)

    elif int(inputs[0]) ==4:
        start_time = time.process_time()
        tecnica_nombre = input("Nombre de la tecnica que quiere saber el total de obras: ")
        tecnica_obras = controller.getBooksByAuthor(cont, tecnica_nombre)
        print('Total de libros: ' + str(lt.size(tecnica_obras['obras'])))
        cantidad = input("Numero de obras antiguas que desea ver: ")
        if int(cantidad) > lt.size(tecnica_obras['obras']):
            print("El numero es mayor al de la cantidad de obras de la tecnica")
        else: 
            ordenadas = controller.sortantiguas(tecnica_obras['obras'],int(cantidad))
            print_obras_tecnica(ordenadas)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
    else:
        sys.exit(0)
sys.exit(0)
