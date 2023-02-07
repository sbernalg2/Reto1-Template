"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newDataStructs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    dataStructs = {
        "data": None,
    }

    dataStructs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=compare)

    return dataStructs


# Funciones para agregar informacion al modelo

def addData(dataStructs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = newData(data["id"], data["info"])
    lt.addLast(dataStructs["data"], d)

    return dataStructs


# Funciones para creacion de datos

def newData(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def getData(dataStructs, id):
    """
    Retorna un dato a partir de su ID
    """
    posData = lt.isPresent(dataStructs["data"], id)
    if posData > 0:
        data = lt.getElement(dataStructs["data"], posData)
        return data
    return None


def dataSize(dataStructs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(dataStructs["data"])


def req1(dataStructs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req2(dataStructs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req3(dataStructs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req4(dataStructs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req5(dataStructs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req6(dataStructs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req7(dataStructs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req8(dataStructs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data1, data2):
    """
    Función encargada de comparar dos datos
    """
    if data1["id"] > data2["id"]:
        return 1
    elif data1["id"] < data2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sortCriteria(data1, data2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data1["id"] > data2["id"]


def sort(dataStructs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(dataStructs["data"], sortCriteria)
