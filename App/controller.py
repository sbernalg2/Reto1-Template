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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.newDataStructs()
    return control

# Funciones para la carga de datos

def loadData(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    start_time = getTime()
    model.sort(control["model"])
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time

# Funciones de consulta sobre el catálogo

def getData(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.getData(control["model"], id)
    return data

def req1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    req1 = model.req1(control["model"])
    return req1

def req2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req2 = model.req2(control["model"])
    return req2

def req3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req3 = model.req3(control["model"])
    return req3

def req4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req4 = model.req4(control["model"])
    return req4

def req5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    req5 = model.req5(control["model"])
    return req5

def req6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req6 = model.req6(control["model"])
    return req6

def req7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req7 = model.req7(control["model"])
    return req7

def req8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req8 = model.req8(control["model"])
    return req8

# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
